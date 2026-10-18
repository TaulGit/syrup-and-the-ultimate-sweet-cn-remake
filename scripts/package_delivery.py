"""Package only the remake, new generated PNGs, prompts, and analysis metadata."""
import json
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import hashlib

ROOT=Path(__file__).resolve().parent.parent
manifest=json.loads((ROOT/'analysis/generated-assets.json').read_text(encoding='utf8'))
groups={}
for g in manifest['groups']:
    if g['status']!='generated':continue
    item=groups.setdefault(g['path'], {'slots':0,'prompts':[], 'ids':[]})
    item['slots']+=len(g['slots']);item['ids'].append(g['id'])
    for p in g.get('promptHistory',[g['promptPath']]):
        if p not in item['prompts']:item['prompts'].append(p)
lines=['# 全套视觉素材与提示词索引','',
       '33 张最终图集覆盖中文版 397 个源槽位。381 个直接新绘槽位，16 个缩略图复用；包含原作本来为空的 GUI 组件。图集原始 PNG 保持生成工具输出，切片通过归一化 UV 使用。', '',
       '每项提示词为英文，按创建、修正顺序列出。来源是本次实际使用的文件；最终映射与 SHA-256 见 [generated-assets.json](../analysis/generated-assets.json)。', '',
       '| 图集 | 映射槽位 | 创建与修正提示词 |','|---|---:|---|']
for file,g in groups.items():
    links=' → '.join(f'[{Path(p).name}]({Path(p).name})' for p in g['prompts'])
    lines.append(f'| [{Path(file).name}](../{file}) | {g["slots"]} | {links} |')
if (ROOT/'assets/cover.png').is_file():
    lines.extend(['', '## 发布封面', '', '[独立生成封面](../assets/cover.png) · [创建提示词](cover.txt)。封面独立于原作 397 个槽位，不参与图集覆盖数量。'])
(ROOT/'prompts/README.md').write_text('\n'.join(lines)+'\n',encoding='utf8')

files=[]
for name in ['index.html','package.json','README.md','star-letter.json','star-letter.mock.mjs','.gitignore','.gitattributes']:
    files.append(ROOT/name)
for folder in ['game','assets','prompts','preview','scripts','tests']:
    files.extend(p for p in (ROOT/folder).rglob('*') if p.is_file() and '__pycache__' not in p.parts)
for p in (ROOT/'analysis').rglob('*'):
    if p.is_file() and not {'reference','evidence'}.intersection(p.relative_to(ROOT/'analysis').parts) and p.name not in ['atlas-qa.jpg','delivery-receipt.json']:
        files.append(p)
out=ROOT/'release';out.mkdir(exist_ok=True)
target=out/'希乐普与终极糖果-中文网页重制-完整工程.zip'
with ZipFile(target,'w',compression=ZIP_DEFLATED,compresslevel=6) as archive:
    for p in sorted(set(files)):
        archive.write(p,p.relative_to(ROOT).as_posix())
with ZipFile(target) as archive:
    assert archive.testzip() is None
    names=archive.namelist()
    assert not any(x.startswith(('analysis/reference/','dist/')) for x in names)
    assert len([x for x in names if x.startswith('assets/atlases/') and x.endswith('.png')])==33
receipt={'file':target.relative_to(ROOT).as_posix(),'files':len(names),'bytes':target.stat().st_size,'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'includesOriginalGameAssets':False,'includesGeneratedAtlasCount':33}
(ROOT/'analysis/delivery-receipt.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(receipt,ensure_ascii=False))
