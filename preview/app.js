const $ = selector => document.querySelector(selector);
const labels = {
  background: '场景背景', character_sprite: '角色立绘', gallery_concept: '角色设定',
  gallery_extra: '追加插画', gallery_thumbnail: '画廊缩略图', gallery_ui: '画廊界面',
  gui_component: '界面组件', localized_image: '本地化图片', menu_animation: '菜单动画',
  menu_portrait: '菜单肖像', screen_art: '全屏画面', solid_background: '纯色背景',
  story_cg: '剧情插画', title_art: '标题画面', visual_effect: '视觉特效',
};
const characters = { Syrup: '希乐普', Gumdrop: '甘姆德洛普', Pastille: '帕斯提耶', Butterscotch: '巴塔斯可琪', Toffee: '托菲', Treat: '德莉特', Wolf: '狼', 'Chocolate Twins': '查克利双子' };
const wardrobes = { labcoat: '实验服', wintercoat: '冬装', labcoat_after_lending_wintercoat: '借出外套后', long_hair_candy_body: '长发糖果形态', short_hair_shop_uniform: '短发店员制服', shop_uniform: '店员制服', winter_outfit: '冬装', witch: '魔女服', chubby_witch: '糖果变化形态', snowy_witch: '雪地服装', borrowed_wintercoat: '借来的冬装', default: '默认', pink_fur: '粉色皮毛', gray_white_fur: '灰白皮毛' };
const state = { inventory: null, generated: null, assets: [], atlases: [], mappings: new Map(), category: '', role: '', status: '', query: '', page: 1, pageSize: 40, detail: null, detailMode: 'single', detailToken: 0, story: null };
const imageCache = new Map();

function el(tag, className, text) {
  const item = document.createElement(tag);
  if (className) item.className = className;
  if (text !== undefined) item.textContent = text;
  return item;
}
function normalizePath(value) { return typeof value === 'string' ? value.replaceAll('\\', '/').replace(/^\.\//, '').replace(/^\//, '') : ''; }
function localPath(value, directory) {
  const clean = normalizePath(value);
  if (!clean.startsWith(`${directory}/`) || clean.split('/').some(part => !part || part === '..' || part === '.')) return null;
  return clean;
}
function localURL(value) { return `/${value.split('/').map(encodeURIComponent).join('/')}`; }
function pretty(value = '') {
  let text = value;
  for (const [name, translated] of Object.entries({ ...characters, ...wardrobes }).sort((a, b) => b[0].length - a[0].length)) text = text.replaceAll(name, translated);
  return text;
}
function list(value) { return Array.isArray(value) ? value : value && typeof value === 'object' ? Object.values(value) : []; }
function normalizeUV(value, cell, atlas) {
  if (Array.isArray(value) && value.length === 4 && value.every(Number.isFinite)) {
    const [x, y, width, height] = value;
    if (x >= 0 && y >= 0 && width > 0 && height > 0 && x + width <= 1.00001 && y + height <= 1.00001) return [x, y, width, height];
  }
  const columns = Number(cell.columns || atlas.columns), rows = Number(cell.rows || atlas.rows);
  if (columns > 0 && rows > 0) {
    const index = Number(cell.index ?? cell.cell ?? 0);
    const column = Number(cell.column ?? cell.col ?? index % columns), row = Number(cell.row ?? Math.floor(index / columns));
    if (column >= 0 && column < columns && row >= 0 && row < rows) return [column / columns, row / rows, 1 / columns, 1 / rows];
  }
  return null;
}

function normalizeGenerated(data, inventory) {
  const groups = new Map((inventory.generation_groups || []).map(group => [group.id, group]));
  const raw = Array.isArray(data) ? data : [...list(data?.atlases), ...list(data?.groups), ...list(data?.outputs), ...list(data?.images)];
  if (!raw.length && data?.assets) raw.push(...list(data.assets));
  if (data?.mappings && !Array.isArray(data.mappings)) {
    for (const [source, mapping] of Object.entries(data.mappings)) raw.push({ ...mapping, source });
  } else if (Array.isArray(data?.mappings)) raw.push(...data.mappings);
  const atlases = [], mapping = new Map(), dedup = new Map();
  raw.forEach((entry, index) => {
    if (!entry || typeof entry !== 'object') return;
    const id = entry.id || entry.group_id || entry.atlas_id || entry.name || `atlas-${index + 1}`;
    const group = groups.get(id);
    const fileCandidate = entry.atlas || entry.atlas_path || entry.output_path || entry.output_file || entry.generated_path || entry.image_path || entry.path || entry.file || (typeof entry.output === 'string' ? entry.output : entry.output?.path);
    const file = localPath(fileCandidate, 'assets');
    const key = file || id;
    let atlas = dedup.get(key);
    if (!atlas) {
      const status = String(entry.status || entry.generation_status || (file ? 'ready' : 'pending')).toLowerCase();
      const promptValue = entry.promptPath || entry.prompt_path || entry.prompt_file || (typeof entry.prompt === 'string' && localPath(entry.prompt, 'prompts') ? entry.prompt : null);
      atlas = { id, name: entry.title_zh || entry.title || entry.name || id, file,
        status: ['invalid', 'failed', 'error', 'rejected'].includes(status) ? 'failed' : ['prompted', 'pending', 'queued', 'generating', 'not_generated', 'planned', 'waiting'].includes(status) ? 'pending' : file ? 'ready' : 'pending',
        statusText: entry.status_message || entry.error || '',
        columns: entry.columns || entry.cols || entry.grid?.columns || group?.columns,
        rows: entry.rows || entry.grid?.rows || group?.rows,
        width: Number(entry.width || entry.image_width || 0), height: Number(entry.height || entry.image_height || 0),
        promptPath: localPath(promptValue, 'prompts'),
        promptPaths: [...new Set([...list(entry.promptHistory), promptValue].map(value => localPath(value, 'prompts')).filter(Boolean))],
        promptText: !promptValue && typeof entry.prompt === 'string' ? entry.prompt : '',
        note: entry.note || entry.description_zh || '', slots: [],
      };
      if (fileCandidate && !file) { atlas.status = 'failed'; atlas.statusText = '新图路径需要位于 assets/ 目录。'; }
      dedup.set(key, atlas); atlases.push(atlas);
    }
    let cells = [...list(entry.slots), ...list(entry.cells)];
    const sourcePaths = entry.source_paths || entry.sources;
    if (!cells.length && Array.isArray(sourcePaths)) cells = sourcePaths.map((source, index) => typeof source === 'string' ? { source, index } : { ...source, index });
    const directSource = entry.source_path || entry.original_path || entry.source;
    if (!cells.length && directSource) cells = [{ ...entry, source: directSource }];
    if (!cells.length && group) cells = group.slots || [];
    cells.forEach((cell, index) => {
      if (typeof cell === 'string') cell = { source: cell, index };
      const source = cell.sourcePath || cell.original_path || cell.source_path || cell.source || cell.original || cell.path;
      const sources = [...(Array.isArray(source) ? source : source ? [source] : []), ...list(cell.aliases), ...list(cell.source_paths)];
      const uv = normalizeUV(cell.uv || cell.uv_rect || cell.crop_uv, { index, ...cell }, atlas);
      const slot = { atlas, uv, index: cell.index ?? cell.cell ?? index, description: cell.expression || cell.description_zh || '', sources: sources.map(normalizePath).filter(Boolean) };
      atlas.slots.push(slot);
      for (const path of slot.sources) {
        const current = mapping.get(path);
        if (!current || current.atlas.status !== 'ready' || atlas.status === 'ready') mapping.set(path, slot);
      }
    });
  });
  // Pixel-identical source files can legitimately share one generated slot.
  const pixelMapping = new Map();
  for (const asset of inventory.assets) if (mapping.has(asset.path) && asset.pixel_sha256) pixelMapping.set(asset.pixel_sha256, { slot: mapping.get(asset.path), original: asset.path });
  for (const asset of inventory.assets) {
    if (!mapping.has(asset.path) && pixelMapping.has(asset.pixel_sha256)) {
      const shared = pixelMapping.get(asset.pixel_sha256);
      mapping.set(asset.path, { ...shared.slot, sharedWith: shared.original });
    }
  }
  return { atlases, mapping };
}

async function readJSON(url, optional = false) {
  const response = await fetch(url, { cache: 'no-store' });
  if (optional && response.status === 404) return null;
  if (!response.ok) throw new Error(`${url}：HTTP ${response.status}`);
  return response.json();
}
function assetStatus(asset) {
  const slot = state.mappings.get(asset.path);
  return slot && slot.uv ? slot.atlas.status : 'pending';
}
function statusBadge(status, text) {
  return el('span', `status-badge ${status}`, text || ({ ready: '✦ 已生成', pending: '◌ 待生成', failed: '！生成异常' }[status] || '◌ 待生成'));
}
function placeholder(message = '待生成', icon = '✧') {
  const box = el('div', 'pending-art'); box.append(el('span', '', icon), el('p', '', message)); return box;
}
function loadImage(atlas) {
  if (!atlas.file) return Promise.reject(new Error('未关联图集文件。'));
  if (!imageCache.has(atlas.file)) {
    imageCache.set(atlas.file, new Promise((resolve, reject) => {
      const image = new Image();
      image.onload = () => { atlas.width = image.naturalWidth; atlas.height = image.naturalHeight; resolve(image); };
      image.onerror = () => reject(new Error('无法读取新图集文件。'));
      image.src = localURL(atlas.file);
    }));
  }
  return imageCache.get(atlas.file);
}
function cropElement(slot) {
  const crop = el('div', 'crop');
  const [x, y, width, height] = slot.uv;
  crop.style.backgroundImage = `url("${localURL(slot.atlas.file)}")`;
  crop.style.backgroundSize = `${100 / width}% ${100 / height}%`;
  crop.style.backgroundPosition = `${width < 1 ? 100 * x / (1 - width) : 0}% ${height < 1 ? 100 * y / (1 - height) : 0}%`;
  const updateAspect = () => crop.style.setProperty('--crop-aspect', String(slot.atlas.width * width / (slot.atlas.height * height) || 1));
  updateAspect();
  loadImage(slot.atlas).then(updateAspect).catch(() => { crop.replaceWith(el('p', 'error-text', '图集文件读取失败，请刷新进度。')); });
  return crop;
}
function updateStats() {
  const total = state.assets.length, ready = state.assets.filter(asset => assetStatus(asset) === 'ready').length;
  const ratio = total ? Math.round(ready / total * 100) : 0;
  $('#total-count').textContent = total;
  $('#ready-count').textContent = ready;
  $('#atlas-count').textContent = state.atlases.filter(atlas => atlas.status === 'ready').length;
  $('#nav-count').textContent = total;
  $('#progress-count').textContent = `${ratio}%`;
  $('#progress-bar').style.width = `${ratio}%`;
}
function fillFilters() {
  const roleSelect = $('#role-filter'); roleSelect.replaceChildren(el('option', '', '全部角色')); roleSelect.firstChild.value = '';
  const roles = [...new Set(state.assets.map(asset => asset.role).filter(Boolean))];
  for (const role of roles) { const option = el('option', '', characters[role] || role); option.value = role; roleSelect.append(option); }
  roleSelect.value = state.role;
  const counts = {}; for (const asset of state.assets) counts[asset.category] = (counts[asset.category] || 0) + 1;
  const categories = [{ key: '', title: '全部素材', count: state.assets.length }, ...Object.entries(counts).map(([key, count]) => ({ key, title: labels[key] || key, count }))];
  const filters = $('#category-filters'); filters.replaceChildren();
  for (const category of categories) {
    const button = el('button', `category-chip${state.category === category.key ? ' active' : ''}`, category.title);
    button.append(el('span', '', category.count)); button.setAttribute('aria-pressed', String(state.category === category.key));
    button.addEventListener('click', () => { state.category = category.key; state.page = 1; fillFilters(); renderAssets(); });
    filters.append(button);
  }
}
function filteredAssets() {
  const query = state.query.trim().toLowerCase();
  return state.assets.filter(asset => (!state.category || asset.category === state.category) && (!state.role || asset.role === state.role) && (!state.status || assetStatus(asset) === state.status) && (!query || `${asset.path} ${asset.description_zh} ${pretty(asset.description_zh)} ${characters[asset.role] || ''} ${labels[asset.category] || ''}`.toLowerCase().includes(query)));
}
function renderAssets() {
  const filtered = filteredAssets(), pages = Math.max(1, Math.ceil(filtered.length / state.pageSize)); state.page = Math.min(state.page, pages);
  $('#results-count').textContent = filtered.length;
  const grid = $('#asset-grid'); grid.replaceChildren();
  for (const asset of filtered.slice((state.page - 1) * state.pageSize, state.page * state.pageSize)) {
    const slot = state.mappings.get(asset.path), status = assetStatus(asset);
    const card = el('button', 'asset-card'); card.type = 'button'; card.setAttribute('aria-label', `${pretty(asset.description_zh) || asset.path}，${status === 'ready' ? '已生成' : status === 'failed' ? '生成异常' : '待生成'}，查看详情`);
    const thumb = el('div', `thumb${status === 'ready' ? ' checkerboard' : ''}`);
    thumb.append(status === 'ready' ? cropElement(slot) : placeholder(status === 'failed' ? '图集待检查' : '待生成'));
    thumb.append(statusBadge(status));
    const info = el('div', 'card-info'); info.append(el('p', 'card-category', labels[asset.category] || asset.category), el('h3', '', pretty(asset.description_zh) || asset.path.split('/').at(-1)), el('span', 'filename', asset.path));
    const bottom = el('div', 'card-bottom'); bottom.append(el('span', '', `${asset.width} × ${asset.height}`), el('span', '', slot?.uv ? `槽位 ${Number(slot.index) + 1} ↗` : '等待绘制 ↗'));
    info.append(bottom); card.append(thumb, info); card.addEventListener('click', () => openDetail(asset)); grid.append(card);
  }
  $('#empty-state').hidden = filtered.length > 0;
  $('#page-indicator').textContent = `${state.page} / ${pages} 页 · 共 ${filtered.length} 项`;
  $('#previous-page').disabled = state.page <= 1; $('#next-page').disabled = state.page >= pages;
}
function renderAtlases() {
  const grid = $('#atlas-grid'); grid.replaceChildren();
  for (const atlas of state.atlases) {
    const card = el('button', 'atlas-card'); card.type = 'button';
    if (atlas.status === 'ready') { const image = el('img', ''); image.loading = 'lazy'; image.src = localURL(atlas.file); image.alt = `${atlas.name} 完整图集`; card.append(image); }
    else { const thumb = el('div', 'thumb'); thumb.append(placeholder(atlas.status === 'failed' ? '图集待检查' : '待生成')); card.append(thumb); }
    const info = el('div', 'atlas-info'); info.append(statusBadge(atlas.status), el('h3', '', atlas.name), el('p', '', `${atlas.columns || '—'} 列 × ${atlas.rows || '—'} 行 · ${atlas.slots.length} 个映射槽位`), el('p', '', atlas.file || '尚未生成图集文件'));
    card.append(info); card.addEventListener('click', () => {
      const source = atlas.slots.flatMap(slot => slot.sources).find(source => state.assets.some(asset => asset.path === source));
      const asset = state.assets.find(asset => asset.path === source);
      if (asset) openDetail(asset, 'whole');
      else openDetail({ path: '（图集级预览）', description_zh: atlas.name, category: 'atlas', width: atlas.width || '—', height: atlas.height || '—' }, 'whole', { atlas, uv: [0, 0, 1, 1], index: 0 });
    }); grid.append(card);
  }
  $('#atlas-empty').hidden = state.atlases.length > 0;
}

function metadataRow(list, title, value) { list.append(el('dt', '', title), el('dd', '', value || '—')); }
async function openDetail(asset, mode = 'single', overrideSlot) {
  const token = ++state.detailToken;
  state.detail = { asset, slot: overrideSlot || state.mappings.get(asset.path) }; state.detailMode = mode;
  const { slot } = state.detail, status = slot?.uv ? slot.atlas.status : 'pending';
  $('#detail-category').textContent = labels[asset.category] || '生成图集';
  $('#detail-title').textContent = pretty(asset.description_zh) || asset.path.split('/').at(-1);
  $('#detail-status').replaceChildren(statusBadge(status));
  const metadata = $('#detail-metadata'); metadata.replaceChildren();
  metadataRow(metadata, '原始文件', asset.path);
  metadataRow(metadata, '原始尺寸', `${asset.width} × ${asset.height} px`);
  metadataRow(metadata, '新图文件', slot?.atlas.file || '待生成');
  metadataRow(metadata, '生成状态', { ready: '已生成，可查看', pending: '尚未生成', failed: slot?.atlas.statusText || '生成异常，或图集文件尚未到位' }[status]);
  metadataRow(metadata, '图集槽位', slot?.uv ? `第 ${Number(slot.index) + 1} 槽 · UV ${slot.uv.map(value => Number(value.toFixed(4))).join(', ')}` : '尚未关联生成槽位');
  if (asset.role) metadataRow(metadata, '角色 / 形态', `${characters[asset.role] || asset.role}${asset.wardrobe ? ` / ${wardrobes[asset.wardrobe] || asset.wardrobe}` : ''}`);
  if (slot?.sharedWith) metadataRow(metadata, '重复文件', `与 ${slot.sharedWith} 的像素内容一致，共享新图槽位。`);
  $('#open-atlas').hidden = !slot?.atlas.file || status !== 'ready';
  if (slot?.atlas.file) $('#open-atlas').href = localURL(slot.atlas.file);
  $('#single-view').disabled = !slot?.uv; $('#whole-view').disabled = !slot?.atlas.file;
  $('#copy-prompt').disabled = true; $('#copy-prompt').textContent = '复制';
  $('#detail-prompt').textContent = '正在读取提示词…';
  $('#prompt-note').textContent = slot?.atlas.promptPaths?.join(' → ') || slot?.atlas.promptPath || '生成清单尚未关联提示词文件。';
  renderDetailStage();
  if (!$('#asset-dialog').open) $('#asset-dialog').showModal();
  let prompt = slot?.atlas.promptText || '';
  try {
    if (slot?.atlas.promptPaths?.length || slot?.atlas.promptPath) {
      const paths = slot.atlas.promptPaths?.length ? slot.atlas.promptPaths : [slot.atlas.promptPath];
      const parts = await Promise.all(paths.map(async path => {
        const response = await fetch(localURL(path), { cache: 'no-store' });
        if (!response.ok) throw new Error(`提示词文件暂不可用（HTTP ${response.status}）。`);
        return `# ${path}\n\n${await response.text()}`;
      }));
      prompt = parts.join('\n\n---\n\n');
    }
    if (token !== state.detailToken) return;
    $('#detail-prompt').textContent = prompt || '该项尚未关联绘制提示词。图集生成后，请在 generated-assets.json 中登记 prompt_path 或 prompt。';
    $('#copy-prompt').disabled = !prompt;
    if (!slot?.atlas.promptPath && prompt) $('#prompt-note').textContent = '来自生成清单的内嵌提示词。';
  } catch (error) { if (token === state.detailToken) $('#detail-prompt').textContent = error.message; }
}
function renderDetailStage() {
  const { asset, slot } = state.detail, stage = $('#detail-stage'); stage.replaceChildren();
  $('#single-view').classList.toggle('active', state.detailMode === 'single'); $('#whole-view').classList.toggle('active', state.detailMode === 'whole');
  if (!slot || !slot.uv || slot.atlas.status !== 'ready') {
    stage.append(placeholder(slot?.atlas.status === 'failed' ? '图集文件待检查' : '这一份素材还在等待绘制'));
    $('#detail-caption').textContent = '原始图片不作为交付预览展示。'; return;
  }
  if (state.detailMode === 'whole') {
    const image = el('img'); image.alt = `${slot.atlas.name} 完整生成图集`; image.src = localURL(slot.atlas.file); stage.append(image);
    $('#detail-caption').textContent = `${slot.atlas.name} · 完整图集 · ${slot.atlas.columns || '—'} × ${slot.atlas.rows || '—'} 分格`;
  } else {
    stage.append(cropElement(slot)); $('#detail-caption').textContent = `${asset.path} · 第 ${Number(slot.index) + 1} 槽 · CSS UV 预览`;
  }
}
function renderStory() {
  const story = state.story;
  if (!story) { $('#story-summary').replaceChildren(el('p', 'muted', '剧情结构文件暂不可用，可先查看完整分析报告。')); return; }
  $('#story-summary').replaceChildren(...[['labels', '个段落'], ['menus', '次选择'], ['choices', '个选项']].map(([key, title]) => {
    const item = el('span'); item.append(el('strong', '', story.counts[key]), document.createTextNode(title)); return item;
  }), (() => { const item = el('span'); item.append(el('strong', '', story.endings.length), document.createTextNode('种结局')); return item; })());
  const endings = $('#ending-grid'); endings.replaceChildren();
  const labelMap = new Map(story.labels.map(label => [label.name, label]));
  for (const [index, ending] of story.endings.entries()) {
    const card = el('article', 'ending-card'); card.append(el('span', 'ending-number', String(index + 1).padStart(2, '0')), el('h3', '', ending.title_zh), el('p', '', labelMap.get(ending.label)?.summary_zh || '按分支条件进入对应结局。'), el('code', '', ending.achievement_id));
    const details = el('details'); details.append(el('summary', '', '查看结构条件'), el('pre', '', ending.condition)); card.append(details); endings.append(card);
  }
  const menus = [];
  function walk(body) { for (const item of body || []) { if (item.kind === 'menu') { menus.push(item); for (const choice of item.choices) walk(choice.body); } else if (item.kind === 'if') for (const branch of item.branches) walk(branch.body); } }
  for (const label of story.labels) walk(label.body);
  const menuList = $('#menu-list'); menuList.replaceChildren();
  for (const [index, menu] of menus.sort((a, b) => a.line - b.line).entries()) {
    const item = el('details', 'menu-item'), summary = el('summary', '', `${String(index + 1).padStart(2, '0')} · ${menu.summary_zh || `选择节点 ${menu.line}`}`);
    summary.append(el('code', '', `L${menu.line}`)); const choices = el('ul');
    for (const choice of menu.choices) choices.append(el('li', '', `${choice.text_zh || choice.text_en}${choice.condition ? '（满足解锁条件时出现）' : ''}`));
    item.append(summary, choices); menuList.append(item);
  }
}
function switchView(view) {
  if (!['assets', 'atlases', 'story', 'reports'].includes(view)) view = 'assets';
  for (const section of document.querySelectorAll('.view')) section.hidden = section.id !== `${view}-view`;
  for (const button of document.querySelectorAll('.nav-button')) { const active = button.dataset.view === view; button.classList.toggle('active', active); if (active) button.setAttribute('aria-current', 'page'); else button.removeAttribute('aria-current'); }
  history.replaceState(null, '', `#${view}`);
}

async function load() {
  $('#refresh').disabled = true; $('#refresh').classList.add('loading');
  const notice = $('#notice'); notice.hidden = true; notice.classList.remove('error'); imageCache.clear();
  try {
    const [inventory, generated, story] = await Promise.all([readJSON('/analysis/asset-inventory.json'), readJSON('/analysis/generated-assets.json', true), readJSON('/analysis/story-graph.json', true).catch(() => null)]);
    if (!Array.isArray(inventory.assets)) throw new Error('素材清单格式不完整，缺少 assets 数组。');
    state.inventory = inventory; state.generated = generated; state.assets = inventory.assets.filter(asset => !asset.path.startsWith('tl/') || asset.path.startsWith('tl/chinese/')); state.story = story;
    const normalized = normalizeGenerated(generated, inventory); state.atlases = normalized.atlases; state.mappings = normalized.mapping;
    await Promise.all(state.atlases.filter(atlas => atlas.status === 'ready').map(async atlas => {
      try { const response = await fetch(localURL(atlas.file), { method: 'HEAD', cache: 'no-store' }); if (!response.ok) { atlas.status = 'failed'; atlas.statusText = `图集文件尚未到位（HTTP ${response.status}）。`; } }
      catch { atlas.status = 'failed'; atlas.statusText = '无法读取图集文件。'; }
    }));
    updateStats(); fillFilters(); renderAssets(); renderAtlases(); renderStory();
    if (!generated) { notice.textContent = '素材清单已就绪。尚未找到生成清单 generated-assets.json，当前显示全部待生成项；新图集登记后，点击「刷新进度」即可查看。'; notice.hidden = false; }
    else {
      const failed = state.atlases.filter(atlas => atlas.status === 'failed').length;
      if (failed) { notice.textContent = `${failed} 份图集文件暂不可用，相关槽位已标记为「生成异常」。生成完成或修正清单后，可刷新检查。`; notice.hidden = false; }
    }
  } catch (error) {
    notice.classList.add('error'); notice.textContent = `素材清单暂时无法读取：${error.message} 请确认使用 npm start 启动查看器。`; notice.hidden = false;
  } finally { $('#refresh').disabled = false; $('#refresh').classList.remove('loading'); }
}

for (const button of document.querySelectorAll('.nav-button')) button.addEventListener('click', () => switchView(button.dataset.view));
window.addEventListener('hashchange', () => switchView(location.hash.slice(1)));
$('#search').addEventListener('input', event => { state.query = event.target.value; state.page = 1; renderAssets(); });
$('#role-filter').addEventListener('change', event => { state.role = event.target.value; state.page = 1; renderAssets(); });
$('#status-filter').addEventListener('change', event => { state.status = event.target.value; state.page = 1; renderAssets(); });
$('#refresh').addEventListener('click', load);
$('#previous-page').addEventListener('click', () => { state.page--; renderAssets(); });
$('#next-page').addEventListener('click', () => { state.page++; renderAssets(); });
$('#close-dialog').addEventListener('click', () => $('#asset-dialog').close());
$('#asset-dialog').addEventListener('click', event => { if (event.target === $('#asset-dialog')) $('#asset-dialog').close(); });
$('#asset-dialog').addEventListener('close', () => { state.detailToken++; });
$('#single-view').addEventListener('click', () => { state.detailMode = 'single'; renderDetailStage(); });
$('#whole-view').addEventListener('click', () => { state.detailMode = 'whole'; renderDetailStage(); });
$('#copy-prompt').addEventListener('click', async () => {
  try { await navigator.clipboard.writeText($('#detail-prompt').textContent); $('#copy-prompt').textContent = '已复制'; }
  catch { $('#copy-prompt').textContent = '请选中文本复制'; }
});
document.addEventListener('keydown', event => { if (event.key === '/' && !$('#asset-dialog').open && !['INPUT', 'TEXTAREA', 'SELECT'].includes(document.activeElement.tagName)) { event.preventDefault(); switchView('assets'); $('#search').focus(); } });
switchView(location.hash.slice(1));
load();
