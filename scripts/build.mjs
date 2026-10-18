import {readFile,writeFile,mkdir,cp,readdir,stat} from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const manifest=JSON.parse(await readFile(path.join(root,'analysis/generated-assets.json'),'utf8'));
if(!manifest.coverage.complete)throw Error('视觉素材尚未覆盖全部中文版槽位');
const assets=manifest.assets.filter(a=>['generated','derived'].includes(a.status)).map(({sourcePath,path,uv,category,description})=>({sourcePath,path,uv,category,description}));
await writeFile(path.join(root,'game/assets.json'),JSON.stringify(assets));
const dist=path.join(root,'dist');await mkdir(dist,{recursive:true});
await cp(path.join(root,'index.html'),path.join(dist,'index.html'));
await cp(path.join(root,'game'),path.join(dist,'game'),{recursive:true});
const files=[...new Set(assets.map(a=>a.path))];
for(const file of files){const target=path.join(dist,file);await mkdir(path.dirname(target),{recursive:true});await cp(path.join(root,file),target);}
const all=[];async function walk(p){for(const e of await readdir(p,{withFileTypes:true})){const q=path.join(p,e.name);if(e.isDirectory())await walk(q);else all.push({path:path.relative(dist,q).replaceAll('\\','/'),size:(await stat(q)).size});}}await walk(dist);
await writeFile(path.join(root,'analysis/build-report.json'),JSON.stringify({assetSlots:assets.length,atlasFiles:files.length,files:all,totalBytes:all.reduce((n,a)=>n+a.size,0)},null,2));
console.log(JSON.stringify({ok:true,assetSlots:assets.length,atlasFiles:files.length,files:all.length,totalBytes:all.reduce((n,a)=>n+a.size,0)}));
