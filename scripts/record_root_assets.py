"""Record the primary agent's ImageGen atlases and intentional thumbnail aliases."""
from pathlib import Path
from PIL import Image
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
groups = []

def group(name, cols, rows, names, *, prompt=None, limitations=None, history=None):
    path = ROOT / 'assets' / 'atlases' / (name + '.png')
    if not path.is_file():
        raise FileNotFoundError(path)
    with Image.open(path) as image:
        width, height = image.size
        mode = image.mode
    slots = []
    for source, index in names:
        row, col = divmod(index, cols)
        slots.append(dict(sourcePath=source, index=index, row=row, column=col,
                          uv=[col/cols, row/rows, 1/cols, 1/rows]))
    record = dict(id=name, path=path.relative_to(ROOT).as_posix(),
                  promptPath=prompt or 'prompts/' + name + '.txt',
                  columns=cols, rows=rows, width=width, height=height, mode=mode,
                  sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                  generationMode='built-in-imagegen', status='generated',
                  slots=slots, limitations=limitations or [],
                  qa='Generated output visually reviewed; pixel dimensions and alpha read from saved PNG.')
    if history:
        record['promptHistory'] = history
    groups.append(record)

def sprites(name, cols, rows, expressions, **kw):
    group(name, cols, rows, [('images/sy '+value+'.png', index) for value,index in expressions], **kw)

sprites('syrup-normal-a',4,3,list(zip(
    ['reg','hmm','oh','proud','embarrassed','grr','grr2','indifferent','thanks','point','smirk','yo'],range(12))),
    limitations=['Sprites are newly drawn upper-body/upper-thigh portraits, not pixel-identical full source canvases.'])
sprites('syrup-normal-b',4,3,[('aww',0),('cool',1),('crystalball',2),('dakara',3),
    ('frick',4),('hahano',6),('heeey',7),('heh',8),('tch',9),('um',10)],
    limitations=['Cells 5 and 11 are spare generated variants and are intentionally not assigned to source slots.'])
sprites('syrup-winter',4,3,list(zip(
    ['cold','coldcomfort','coldhey','coldhmm','coldhuh','coldsass','coldscared','coldsmirk','coldstop','coldthought','coldyeah','coldyell'],range(12))))
sprites('syrup-after-coat-v2',3,2,list(zip(
    ['colder','colderawkward','colderhey','coldersmile','colderstop','colderyeah'],range(6))),
    prompt='prompts/syrup-after-coat.txt',
    history=['prompts/syrup-after-coat.txt','prompts/syrup-after-coat-v2.txt'],
    limitations=['The saved RGBA PNG contains hidden RGB outside the sprites, but sampled outside pixels have alpha=0; use alpha-aware rendering.'])

group('backgrounds-shop-v2',2,2,[(f'images/bg {x}.jpg',i) for i,x in enumerate(['shop','shop2','shopext','nightshop'])],
      prompt='prompts/backgrounds-shop.txt', history=['prompts/backgrounds-shop.txt','prompts/backgrounds-shop-v2.txt'],
      limitations=['New scene geometry differs from the source. Day and night counterparts share the new candy-shop setting; shop2 has a caramel palette correction.'])
group('backgrounds-cottage',2,2,[(f'images/bg {x}.jpg',i) for i,x in enumerate(['cottage','cottagedoor','cottageint','nightcottage'])])
group('backgrounds-ice',2,2,[(f'images/bg {x}.jpg',i) for i,x in enumerate(['icecave','icecave2','mountain','snow'])])
group('backgrounds-town',2,2,[('images/bg lab.png',0),('images/bg library.jpg',1),('images/bg market.jpg',2),('images/bg cabin.jpg',3)],
      limitations=['New backgrounds use somewhat more line detail than the original while keeping the limited pastel palettes.'])
group('title-bilingual',1,2,[('tl/chinese/images/title.png',0),('images/title.png',1)],
      limitations=['English title lettering uses tight decorative spacing. The eight Chinese title characters were visually checked.'])
# Generated lettering crosses the nominal half-canvas boundary. Keep each title
# inside its measured band; this does not modify the original ImageGen PNG.
groups[-1]['slots'][0]['uv']=[0,60/groups[-1]['height'],1,310/groups[-1]['height']]
groups[-1]['slots'][1]['uv']=[0,420/groups[-1]['height'],1,440/groups[-1]['height']]
group('storybook-frames',2,4,[(x,i) for i,x in enumerate([
    'images/storybook.jpg','images/storybook2.jpg','images/splash.jpg',
    'images/gallery/galframe_idle.png','images/gallery/galframe_hover.png',
    'images/gallery/galframe_insensitive.png','images/bg black.png'])],
    limitations=['Source author logo is replaced by a new candy emblem; the original author credit remains in the report.',
                 'The source uniform transition color is represented by a newly generated dark tile, with slight tonal texture.'])
group('effects-menu',4,3,[(x,i) for i,x in enumerate([
    'images/clouds.png','images/flowers1.png','images/flowers2.png','images/flowers3.png',
    'images/light1.png','images/light2.png','images/light3.png','images/pastfilter.png',
    'images/ani1.png','images/ani2.png','images/ani3.png'])],
    limitations=['Effects are new interpretive redraws. The memory filter uses sparse cream flecks rather than an identical source texture.',
                 'Animation cells are three new phases; timing is documented separately in the source analysis.'])

def collect_other_groups():
    result = list(groups)
    for filename in ['generated-characters.json','generated-cg-bs.json','generated-ui.json']:
        path = ROOT / 'analysis' / filename
        if path.is_file():
            data = json.loads(path.read_text(encoding='utf-8'))
            result += data.get('groups', data.get('atlases', []))
    return result

lookup = {}
for item in collect_other_groups():
    path = item.get('path',item.get('atlas'))
    for slot in item.get('slots',item.get('cells',[])):
        source = slot.get('sourcePath',slot.get('source',slot.get('original_path')))
        if source and path:
            lookup[source] = (item,slot)

aliases = {
    'images/gallery/gal_cabin.jpg':'images/bg cabin.jpg',
    'images/gallery/gal_cottage.jpg':'images/bg cottage.jpg',
    'images/gallery/gal_lab.jpg':'images/bg lab.png',
    'images/gallery/gal_market.jpg':'images/bg market.jpg',
    'images/gallery/gal_mountain.jpg':'images/bg mountain.jpg',
    'images/gallery/gal_shop.jpg':'images/bg shop.jpg',
    'images/mmsyrup.png':'images/sy reg.png',
    'images/mmsyrup2.png':'images/sy smirk.png',
    'images/mmgum.png':'images/gum dress.png',
    'images/mmgum2.png':'images/gum yay.png',
    'images/mmpas.png':'images/pas smile.png',
    'images/mmpas2.png':'images/pas eheh.png',
    'images/mmbs.png':'images/bs hey.png',
    'images/mmbs2.png':'images/bs smirk.png',
    'images/mmtof.png':'images/tof nyan.png',
    'images/mmtof2.png':'images/tof myow.png',
}
derived_groups = {}
for target, source in aliases.items():
    if source not in lookup:
        continue
    base, cell = lookup[source]
    path = base.get('path',base.get('atlas'))
    if not (ROOT / path).is_file():
        continue
    name = 'derived-' + base.get('id',base.get('name',Path(path).stem))
    if name not in derived_groups:
        with Image.open(ROOT/path) as image:
            width,height=image.size
            mode=image.mode
        derived_groups[name]=dict(id=name,path=path,promptPath=base.get('promptPath',base.get('prompt',base.get('prompt_path'))),
            columns=base['columns'],rows=base['rows'],width=width,height=height,mode=mode,
            sha256=hashlib.sha256((ROOT/path).read_bytes()).hexdigest(),
            generationMode='built-in-imagegen',status='generated',slots=[],
            limitations=['Intentional thumbnail reuse of a newly generated background or character pose, rendered with CSS UVs. This is not a separate image generation.'])
    cols, rows = base['columns'],base['rows']
    row, col = cell.get('row',0),cell.get('column',cell.get('col',0))
    uv=cell.get('uv',[col/cols,row/rows,1/cols,1/rows])
    derived_groups[name]['slots'].append(dict(sourcePath=target,index=cell.get('index',row*cols+col),row=row,column=col,uv=uv,derived_from=source))
groups.extend(derived_groups.values())
output=ROOT/'analysis'/'generated-root.json'
output.write_text(json.dumps(dict(groups=groups),ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(dict(groups=len(groups),direct_slots=sum(len(g['slots']) for g in groups if not g['id'].startswith('derived-')),
                     derived_slots=sum(len(g['slots']) for g in groups if g['id'].startswith('derived-')))))
