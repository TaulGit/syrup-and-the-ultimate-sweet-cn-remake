import http from 'node:http';
import { createReadStream } from 'node:fs';
import { realpath, stat } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = await realpath(path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..'));
const host = process.env.HOST || '127.0.0.1';
const port = Number(process.env.PORT || 4173);
if (!['127.0.0.1', 'localhost', '::1'].includes(host)) throw new Error('HOST 必须是本机回环地址。');
if (!Number.isInteger(port) || port < 1 || port > 65535) throw new Error('PORT 必须为 1–65535。');

const mime = {
  '.html': 'text/html; charset=utf-8', '.js': 'text/javascript; charset=utf-8',
  '.css': 'text/css; charset=utf-8', '.json': 'application/json; charset=utf-8',
  '.md': 'text/markdown; charset=utf-8', '.txt': 'text/plain; charset=utf-8',
  '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg',
  '.webp': 'image/webp', '.svg': 'image/svg+xml', '.ico': 'image/x-icon',
};

function insideRoot(filename) {
  const relative = path.relative(root, filename);
  return relative !== '..' && !relative.startsWith(`..${path.sep}`) && !path.isAbsolute(relative);
}

function respond(res, status, text, method = 'GET') {
  res.writeHead(status, { 'Content-Type': 'text/plain; charset=utf-8', 'Cache-Control': 'no-store', 'X-Content-Type-Options': 'nosniff' });
  res.end(method === 'HEAD' ? undefined : text);
}

const server = http.createServer(async (req, res) => {
  if (!['GET', 'HEAD'].includes(req.method)) {
    res.setHeader('Allow', 'GET, HEAD');
    return respond(res, 405, '仅支持 GET 和 HEAD。', req.method);
  }
  try {
    let pathname;
    try { pathname = decodeURIComponent((req.url || '/').split('?')[0]); }
    catch { return respond(res, 400, 'URL 编码无效。', req.method); }
    if (pathname.includes('\0') || pathname.includes('\\') || pathname.split('/').some(part => part === '..')) {
      return respond(res, 403, '不能访问此路径。', req.method);
    }
    if (pathname === '/') pathname = '/index.html';
    if (['/preview', '/preview/'].includes(pathname)) pathname = '/preview/index.html';
    const parts = pathname.split('/').filter(Boolean);
    if (!['index.html', 'game', 'preview', 'assets', 'analysis', 'prompts'].includes(parts[0]) ||
        (parts[0] === 'analysis' && parts[1] === 'reference')) {
      return respond(res, 404, '文件不存在。', req.method);
    }
    const candidate = path.resolve(root, `.${pathname}`);
    if (!insideRoot(candidate)) return respond(res, 403, '不能访问此路径。', req.method);
    const filename = await realpath(candidate);
    if (!insideRoot(filename)) return respond(res, 403, '不能访问工作区外的文件。', req.method);
    const resolvedParts = path.relative(root, filename).split(path.sep);
    if (resolvedParts[0] === 'analysis' && resolvedParts[1] === 'reference') return respond(res, 404, '文件不存在。', req.method);
    const info = await stat(filename);
    if (!info.isFile()) return respond(res, 404, '文件不存在。', req.method);
    const contentType = mime[path.extname(filename).toLowerCase()];
    if (!contentType) return respond(res, 404, '此文件类型不在查看器交付范围内。', req.method);
    res.writeHead(200, {
      'Content-Type': contentType, 'Content-Length': info.size,
      'Cache-Control': 'no-store', 'X-Content-Type-Options': 'nosniff',
      'Referrer-Policy': 'no-referrer',
    });
    if (req.method === 'HEAD') return res.end();
    createReadStream(filename).on('error', () => res.destroy()).pipe(res);
  } catch (error) {
    if (!res.headersSent) respond(res, error.code === 'ENOENT' || error.code === 'ENOTDIR' ? 404 : 500,
      error.code === 'ENOENT' || error.code === 'ENOTDIR' ? '文件不存在。' : '读取文件失败。', req.method);
    else res.destroy();
  }
});

server.on('error', error => {
  console.error(error.code === 'EADDRINUSE' ? `端口 ${port} 已被使用，可设置 PORT 后重新启动。` : error.message);
  process.exitCode = 1;
});
server.listen(port, host, () => console.log(`游戏：http://${host === '::1' ? '[::1]' : host}:${port}/  素材查看器：/preview/`));
