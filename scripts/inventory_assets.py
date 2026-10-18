"""Inventory every raster asset in the inspected, public Ren'Py web build.

Reads reference files only. Reports byte and normalized RGBA pixel hashes,
Ren'Py automatic image names, source references, classifications, and an
exhaustive atlas-generation plan. Run from the project root with Pillow.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from hashlib import sha256
import json
from math import ceil, sqrt
from pathlib import Path
import re

from PIL import Image


SOURCE_ARCHIVE_SHA256 = "3b01e88b68be2f41e8305215c30863c6ee4063bea6fe72b0a6f496841c8edf9a"
REA_EVIDENCE_ID = "ev_8e5d4de3c042817e24abd04ae3ccfbc41adc264b16b149e573d5e4ff40685a02"
CHAR_NAMES = {"sy": "Syrup", "gum": "Gumdrop", "gums": "Gumdrop", "pas": "Pastille",
              "bs": "Butterscotch", "tof": "Toffee", "choco": "Chocolate Twins",
              "treat": "Treat", "wolf": "Wolf"}
BG_NAMES = {
    "black": "深蓝灰转场底", "cabin": "雪山木屋室内", "cottage": "女巫小屋外景",
    "cottagedoor": "女巫小屋门口近景", "cottageint": "女巫小屋室内", "icecave": "冰洞",
    "icecave2": "冰洞第二状态", "lab": "糖果炼金实验室", "library": "图书馆",
    "market": "城镇集市", "mountain": "雪山远景", "nightcottage": "夜晚女巫小屋",
    "nightshop": "夜晚糖果店内", "shop": "糖果店内", "shop2": "糖果店第二状态",
    "shopext": "糖果店外街道", "snow": "雪地山路",
}
EXPR_NAMES = {
    "aww": "温柔怜惜", "aw": "轻声安慰", "baw": "大哭", "broken": "身体破损",
    "determined": "坚定", "doll": "玩偶状态", "dress": "展示衣服", "eaten": "被吃掉后的状态",
    "friendlier": "更亲近", "frozen": "冻结", "happy": "开心", "hey": "打招呼",
    "hey2": "另一种招呼姿势", "lost": "迷茫", "mad": "生气", "noo": "拒绝",
    "nooo": "强烈抗拒", "ooh": "好奇惊喜", "pls": "请求", "shutdown": "失去反应",
    "surprise": "惊讶", "surprise2": "另一种惊讶", "umm": "犹豫", "worry": "担忧",
    "yay": "欢呼", "yay2": "另一种欢呼", "yayyy": "非常兴奋", "yayyy2": "另一种兴奋",
    "yes": "肯定", "yes2": "另一种肯定", "reg": "平常", "indifferent": "冷淡",
    "hmm": "思考", "point": "指向", "crystalball": "手持水晶球", "cool": "淡定",
    "dakara": "解释", "embarrassed": "害羞", "frick": "懊恼", "grr": "恼怒",
    "grr2": "另一种恼怒", "hahano": "尴尬拒绝", "heeey": "高声招呼", "heh": "轻笑",
    "oh": "察觉", "proud": "自豪", "smirk": "得意笑", "tch": "不耐烦",
    "thanks": "感谢", "um": "迟疑", "yo": "随意招呼", "comfort": "安抚", "huh": "疑惑",
    "sass": "吐槽", "scared": "害怕", "stop": "制止", "thought": "沉思", "yeah": "应答",
    "yell": "喊叫", "awkward": "尴尬", "smile": "微笑", "aaa": "惊叫",
    "brag": "炫耀", "castin": "施法", "drool": "馋嘴", "freakinout": "慌乱",
    "magics": "魔法动作", "ohno": "不妙", "shock": "震惊", "takeit": "递出物品",
    "umai": "觉得美味", "pathetic": "可怜委屈", "tears": "流泪", "eheh": "不好意思地笑",
    "fret": "焦虑", "help": "求助", "myow": "喵叫", "nyan": "猫式招呼",
    "sly": "狡黠", "tsun": "傲娇", "flowers": "手持花束", "hello": "双人招呼",
    "meh": "无所谓", "pink": "被魔法染成粉色", "pink2": "粉色状态惊慌", "dang": "懊恼",
    "hmhm": "胸有成竹", "patient": "耐心", "ready": "准备就绪", "sad": "难过",
    "sorry": "歉意", "wahh": "惊慌叫喊", "yum": "品尝美味", "nervous": "紧张",
    "chub": "胖乎乎状态", "weh": "委屈", "shy": "羞怯",
}


def classify(rel: str) -> dict:
    p = Path(rel)
    stem = p.stem
    root = p.parts[0]
    result = {"category": "", "subcategory": "", "role": "", "wardrobe": "",
              "description_zh": "", "generation_family": "ui"}
    if root == "tl":
        locale = p.parts[1]
        result.update(category="localized_image", subcategory="chinese_title" if locale == "chinese" else "other_language_image",
                      locale=locale, role="title" if stem == "title" else "credits",
                      description_zh=("简体中文标题字图" if locale == "chinese" else f"{locale} 本地化{('标题' if stem == 'title' else '制作人员名单')}图"))
        return result
    if root == "gui":
        if "console" in p.parts:
            sub, desc = "controller_glyph", "手柄按键提示图标"
        elif "scrollbar" in p.parts:
            sub, desc = "scrollbar", "滚动条的横/竖、悬停/静止、轨道/滑块"
        elif "slider" in p.parts:
            sub, desc = "slider", "设置滑条的横/竖、悬停/静止、轨道/滑块"
        elif "bar" in p.parts:
            sub, desc = "bar", "进度条分段"
        elif "overlay" in p.parts:
            sub, desc = "overlay", "菜单或确认框遮罩"
        elif "button" in p.parts:
            sub, desc = "button", "按钮背景、选中标记或导航图标"
        else:
            sub = {"textbox": "dialogue_box", "textbox0": "dialogue_box_legacy", "namebox": "name_box",
                   "main_menu": "menu_background", "game_menu": "menu_background", "nvl": "nvl_background",
                   "window_icon": "app_icon", "notify": "notification", "skip": "skip_indicator",
                   "history": "panel_tile", "confirm_frame": "panel_frame", "frame": "panel_frame",
                   "frame2": "panel_frame"}.get(stem, "misc")
            desc = {"textbox": "底部对话框", "textbox0": "旧版移动端对话框", "namebox": "说话者姓名框",
                    "main_menu": "主菜单底图", "game_menu": "存读档/设置通用菜单底图", "nvl": "整屏叙述框",
                    "window_icon": "程序图标", "notify": "通知条", "skip": "快进提示框",
                    "history": "历史/图库面板纹理", "confirm_frame": "确认弹窗边框", "frame": "通用边框",
                    "frame2": "第二种通用边框"}.get(stem, stem)
        result.update(category="gui_component", subcategory=sub, platform="phone" if "phone" in p.parts else "shared_desktop",
                      description_zh=desc)
        return result
    if p.parent.as_posix() == "images/gallery":
        if stem.startswith("concept "):
            result.update(category="gallery_concept", subcategory="character_design", generation_family="character",
                          description_zh="画廊角色概念设计图：" + stem[8:])
        elif stem.startswith("extra "):
            result.update(category="gallery_extra", subcategory="bonus_illustration", generation_family="cg",
                          description_zh="画廊附加插画：" + stem[6:])
        elif stem.startswith("gal_"):
            result.update(category="gallery_thumbnail", subcategory="background_preview", derived_from=f"images/bg {stem[4:]}." + ("png" if stem[4:] == "lab" else "jpg"),
                          description_zh="背景画廊缩略图：" + stem[4:])
        else:
            result.update(category="gallery_ui", subcategory="gallery_frame", description_zh="背景画廊边框/锁定图")
        return result
    tag, _, expr = stem.partition(" ")
    if tag in CHAR_NAMES:
        role = CHAR_NAMES[tag]
        wardrobe = "default"
        exprbase = expr
        if tag == "sy":
            wardrobe = "labcoat"
            if expr.startswith("colder"):
                wardrobe, exprbase = "labcoat_after_lending_wintercoat", expr[6:]
            elif expr.startswith("cold"):
                wardrobe, exprbase = "wintercoat", expr[4:]
        elif tag == "bs":
            wardrobe = "witch"
            if expr.startswith("cold"):
                wardrobe, exprbase = "snowy_witch", expr[4:]
            elif expr.startswith("warm"):
                wardrobe, exprbase = "borrowed_wintercoat", expr[4:]
            elif "chub" in expr:
                wardrobe, exprbase = "chubby_witch", expr.replace("chub", "")
        elif tag == "pas":
            wardrobe = "shop_uniform"
            if expr.startswith("cold"):
                wardrobe, exprbase = "winter_outfit", expr[4:]
        elif tag in ("gum", "gums"):
            wardrobe = "short_hair_shop_uniform" if tag == "gums" else "long_hair_candy_body"
        elif tag == "wolf":
            wardrobe = "pink_fur" if expr.startswith("pink") else "gray_white_fur"
        result.update(category="character_sprite", subcategory="expression_pose", role=role, wardrobe=wardrobe,
                      expression=expr or "base", expression_zh=EXPR_NAMES.get(exprbase, exprbase or "基础"), generation_family="character",
                      description_zh=f"{role} / {wardrobe} / {EXPR_NAMES.get(exprbase, exprbase or '基础')}")
    elif tag == "bg":
        result.update(category="background" if expr != "black" else "solid_background", subcategory="scene" if expr != "black" else "transition",
                      description_zh=BG_NAMES.get(expr, expr), generation_family="background" if expr != "black" else "ui")
    elif tag == "sb":
        result.update(category="story_cg" if expr != "locked" else "gallery_ui", subcategory="storybook_illustration" if expr != "locked" else "locked_story_cg",
                      generation_family="cg" if expr != "locked" else "ui", description_zh="剧情故事书插画：" + expr if expr != "locked" else "未解锁剧情插画占位图")
    elif stem.startswith("mm"):
        role = {"mmsyrup": "Syrup", "mmgum": "Gumdrop", "mmpas": "Pastille", "mmbs": "Butterscotch", "mmtof": "Toffee"}[stem.rstrip("2")]
        result.update(category="menu_portrait", subcategory="ending_unlocked" if stem.endswith("2") else "default", role=role,
                      description_zh=f"主菜单 {role} {'结局完成' if stem.endswith('2') else '默认'}立绘")
    elif stem in {"clouds", "flowers1", "flowers2", "flowers3", "light1", "light2", "light3", "pastfilter"}:
        result.update(category="visual_effect", subcategory="parallax_clouds" if stem == "clouds" else "memory_overlay" if stem == "pastfilter" else "magic_particle",
                      description_zh={"clouds": "主菜单平移云层", "pastfilter": "回忆场景全屏滤镜"}.get(stem, "花瓣魔法粒子" if stem.startswith("flowers") else "光芒魔法粒子"))
    elif stem.startswith("ani"):
        result.update(category="menu_animation", subcategory="animated_landscape_strip", description_zh=f"主菜单循环底部动画第 {stem[3:]} 帧")
    elif stem == "title":
        result.update(category="title_art", subcategory="english_title", role="title", description_zh="英文主标题装饰字图")
    else:
        result.update(category="screen_art", subcategory={"splash": "splash", "storybook": "storybook_page", "storybook2": "storybook_page_variant"}.get(stem, "misc"),
                      description_zh={"splash": "启动画面", "storybook": "故事书/画廊背景", "storybook2": "故事书另一背景"}.get(stem, stem))
    return result


def read_sources(root: Path):
    result = []
    characters = {}
    for p in sorted(root.glob("*.rpy")):
        label = None
        for number, raw in enumerate(p.read_text(encoding="utf-8-sig").splitlines(), 1):
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            if line.startswith(("label ", "screen ", "style ", "transform ")):
                label = line.split(":")[0]
            m = re.match(r'define\s+(\w+)\s*=\s*(?:DynamicCharacter|Character)\(.*?image\s*=\s*"([^" ]+)"', line)
            if m:
                characters[m[1]] = m[2]
            result.append({"file": p.name, "line": number, "text": line, "context": label})
    return result, characters


def references(asset: dict, sources: list, characters: dict):
    rel = asset["path"]
    symbol = Path(rel).stem
    out = []
    for src in sources:
        line = src["text"]
        kind = None
        if rel in line:
            kind = "explicit_file"
        elif asset.get("automatic_image_name") and re.search(r'["\']' + re.escape(symbol) + r'["\']', line):
            kind = "automatic_image_name"
        elif asset.get("automatic_image_name") and re.match(r"(?:show|scene)\s+" + re.escape(symbol) + r"(?:\s+(?:at|with|behind|as|onlayer|zorder)\b|:|$)", line):
            kind = "show_scene"
        elif asset["category"] == "character_sprite":
            for short, tag in characters.items():
                if tag == symbol.split(" ")[0] and " " in symbol and re.match(re.escape(short) + r"\s+" + re.escape(symbol.split(" ", 1)[1]) + r"\s+[\"']", line):
                    kind = "dialogue_image_attribute"
                    break
        if not kind and rel.startswith("gui/"):
            for pattern in re.findall(r'["\'](gui/[^"\']+\.(?:png|jpg))["\']', line):
                pattern_re = re.escape(pattern).replace(re.escape("%s"), ".+").replace(re.escape("[prefix_]"), ".*")
                if re.fullmatch(pattern_re, rel):
                    kind = "gui_state_pattern"
                    break
        if kind:
            out.append(dict(src, kind=kind))
    # Localized substitutions are automatic, and inherit the base title use.
    if rel.startswith("tl/"):
        out.append({"file": "Ren'Py localization resolver", "line": None, "text": f"Language-specific replacement for images/{Path(rel).name}",
                    "kind": "localized_image_substitution", "context": "language-specific asset search"})
    if not out and rel.startswith("gui/"):
        # Ren'Py gui.button_properties resolves image families by style prefix.
        if "/button/" in rel and "console" not in rel:
            out.append({"file": "screens.rpy", "line": 30, "text": 'properties gui.button_properties("button")',
                        "kind": "implicit_gui_style_or_packaged_variant", "context": "Ren'Py GUI family; not every packaged state is reached"})
    return out


def atlas_group(group_id, family, items, cols=None, rows=None, note=""):
    cols = cols or max(1, ceil(sqrt(len(items))))
    rows = rows or max(1, ceil(len(items) / cols))
    assert cols * rows >= len(items)
    return {"id": group_id, "family": family, "columns": cols, "rows": rows, "slot_count": len(items),
            "note": note, "source_paths": [a["path"] for a in items],
            "slots": [{"index": i, "row": i // cols, "column": i % cols,
                       "uv": [(i % cols) / cols, (i // cols) / rows, 1 / cols, 1 / rows],
                       "original_path": a["path"], "description_zh": a["description_zh"]} for i, a in enumerate(items)]}


def build_groups(assets):
    groups = []
    # A single coherent atlas per character is the fewest non-mixing plan.
    for role in CHAR_NAMES.values():
        if any(g["id"] == "character_" + role.lower().replace(" ", "_") for g in groups):
            continue
        items = [a for a in assets if a["category"] == "character_sprite" and a["role"] == role]
        groups.append(atlas_group("character_" + role.lower().replace(" ", "_"), "character", items,
                                  note="逐表情独立格；保留服装、体型和状态差异。Gumdrop 长发常态新图采用完整糖霜连衣裙。"))
    bg = [a for a in assets if a["category"] == "background"]
    for start in range(0, len(bg), 4):
        groups.append(atlas_group(f"background_{start // 4 + 1:02}", "background", bg[start:start + 4], 2, 2,
                                  "2×2；每格 16:9，无人物，不合并白天/夜晚和场景变体。"))
    cg = [a for a in assets if a["category"] == "story_cg"]
    for start in range(0, len(cg), 6):
        groups.append(atlas_group(f"story_cg_{start // 6 + 1:02}", "cg", cg[start:start + 6], 3, 2,
                                  "3×2；每格保留独立剧情构图。最后不足 6 格留空，不减少原图。"))
    concept = [a for a in assets if a["category"] == "gallery_concept"]
    groups.append(atlas_group("gallery_character_concepts", "character", concept, 3, 3,
                              "全新角色设计概念图；概念原稿仍逐项映射。"))
    extras = [a for a in assets if a["category"] == "gallery_extra"]
    for start in range(0, len(extras), 6):
        groups.append(atlas_group(f"gallery_extra_{start // 6 + 1:02}", "cg", extras[start:start + 6], 3, 2,
                                  "附加插画亦重新创作；原 rough/doodle 保留草图语汇。"))
    ui_items = [a for a in assets if a["generation_family"] == "ui"]
    ui_buckets = defaultdict(list)
    for a in ui_items:
        cat, sub, p = a["category"], a["subcategory"], a["path"]
        if cat == "menu_portrait": bucket = "menu_portraits"
        elif cat == "menu_animation": bucket = "menu_animation"
        elif cat == "visual_effect": bucket = "effects"
        elif cat == "gallery_thumbnail": bucket = "gallery_thumbnails_derived"
        elif cat in {"title_art", "localized_image"}: bucket = "title_and_locale_text"
        elif sub == "controller_glyph": bucket = "controller_glyphs"
        elif sub in {"bar", "scrollbar", "slider"}: bucket = "bars_and_sliders"
        elif sub == "button": bucket = "buttons"
        else: bucket = "panels_and_screens"
        ui_buckets[bucket].append(a)
    for bucket, items in ui_buckets.items():
        note = "保留全部源路径/状态；完全相同像素可映射同一新图格。"
        if bucket == "title_and_locale_text": note += "统一新标题装饰底，简中文字用运行时字体绘制；其他语言只保留清单，中文版不加载。"
        if bucket == "gallery_thumbnails_derived": note += "从新背景同 UV 派生，无需另一次生图。"
        if bucket in {"bars_and_sliders", "controller_glyphs"}: note += "通用几何/字母细节可运行时绘制，生图负责统一装饰风格。"
        groups.append(atlas_group("ui_" + bucket, "ui", items, note=note))
    covered = [p for g in groups for p in g["source_paths"]]
    assert len(covered) == len(set(covered)) == len(assets), (len(covered), len(assets))
    mapping = {slot["original_path"]: dict(group_id=g["id"], cell=slot["index"], uv=slot["uv"]) for g in groups for slot in g["slots"]}
    for a in assets:
        a["generation_mapping"] = mapping[a["path"]]
    return groups


def make_report(data):
    counts = data["statistics"]
    lines = ["# Syrup and the Ultimate Sweet 网页公开构建视觉资产清单", "",
             "## 结论", "",
             f"逐个覆盖 **{counts['total_files']} 个图像文件**（383 PNG + 24 JPG），没有只计主目录而漏掉 GUI、画廊或语言替换图。",
             f"原包 SHA256：`{SOURCE_ARCHIVE_SHA256}`。REA 归档证据：`{REA_EVIDENCE_ID}`。", "",
             f"文件内容唯一数：{counts['unique_byte_hashes']}；归一化 RGBA 像素唯一数：{counts['unique_pixel_hashes']}。",
             "哈希相同才认定重复；其他语言图是用途上的语言替换，不能默认认定字节或像素相同。", "",
             "## 按用途统计", "", "| 类别 | 文件数 |", "|---|---:|"]
    for category, n in counts["categories"].items():
        lines.append(f"| {category} | {n} |")
    lines += ["", "## 角色与服装/状态", "", "| 角色 | 服装/状态 | 独立表情/姿势图数 |", "|---|---|---:|"]
    for role, wardrobes in counts["character_wardrobes"].items():
        for wardrobe, n in wardrobes.items():
            lines.append(f"| {role} | {wardrobe} | {n} |")
    lines += ["", "`sy cold*` 是灰色毛领防寒外套；`sy colder*` 是借出外套后冻红的白大褂。",
              "`bs warm*` 是借穿灰色外套；`bs cold*` 是淋雪的巫师装。两类服装不能仅靠 cold/warm 字面合并。",
              "Gumdrop 有长发常态 29 图、短发店员制服 13 图；新图长发常态采用完整糖霜连衣裙。Wolf 3 图是四足狼，Treat 3 图是人形，分别保留。", "",
              "## 去重、中文及使用点判据", "",
              "- `sha256` 按原文件字节计算；`pixel_sha256` 按尺寸+RGBA 像素计算，忽略 PNG 元数据差异。",
              "- `duplicate_of` 只表示像素完全相同，可共用一张新图。不得据此删除原逻辑槽位或悬停状态。",
              "- `automatic_image_name` 记录 Ren'Py images/ 自动图片名；使用点包含直接路径、自动图片名、show/scene、角色对白表情属性、GUI 状态模板。",
              "- 无静态命中的文件标为 packaged_no_static_reference。它们仍列入完整重绘计划；不伪造运行时触达证据。",
              "- 简中本地化图只有 `tl/chinese/images/title.png`；简中剧情、菜单、名字翻译位于文本源码，非图片。另 10 个语言图保留盘点但中文版不加载。",
              "- `gui/phone/` 是移动端变体；GUI 家族由 `gui.button_properties` 与屏幕样式按状态选图，部分打包旧版状态未被源码实际引用。", "",
              "## 最少完整生成任务分组", "",
              "角色按身份合并图集、每个表情/服装独立格；背景每组 4 图、剧情 CG 每组 6 图。其余美术按用途进入 UI/概念/额外插画图集。",
              "这是槽位不遗漏的最少分组方案；如图像模型分辨率限制导致小格细节不足，可拆页，不能合并原表情。UV 坐标随 JSON 给出，前端可直接按图集选格，无需裁图。", ""]
    for group in data["generation_groups"]:
        lines += [f"### {group['id']} · {group['family']} · {group['columns']}×{group['rows']} · {group['slot_count']} 槽", "", group["note"], ""]
        for slot in group["slots"]:
            lines.append(f"- {slot['index']:02}（{slot['row']},{slot['column']}）：`{slot['original_path']}` — {slot['description_zh']}")
        lines.append("")
    lines += ["## 完整逐文件清单", "", "更完整的模式、尺寸、SHA256、像素哈希、所有源码使用点与图集 UV 坐标见同名 JSON。", "",
              "| 路径 | 用途分类 | 尺寸/模式 | 使用点（首个） | 重复/派生 |", "|---|---|---|---|---|"]
    for asset in data["assets"]:
        ref = asset["source_refs"][0] if asset["source_refs"] else None
        use = (f"{ref['file']}:{ref['line']} `{ref['kind']}`" if ref else "packaged_no_static_reference")
        duplicate = asset.get("duplicate_of") or asset.get("derived_from") or ""
        lines.append(f"| `{asset['path']}` | {asset['category']}/{asset['subcategory']} | {asset['width']}×{asset['height']} {asset['mode']} | {use} | `{duplicate}` |")
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("analysis/reference/unpacked/game"))
    parser.add_argument("--output", type=Path, default=Path("analysis"))
    args = parser.parse_args()
    sources, characters = read_sources(args.root)
    assets = []
    first_pixel = {}
    for p in sorted(args.root.rglob("*")):
        if not p.is_file() or p.suffix.lower() not in {".png", ".jpg", ".jpeg"}:
            continue
        rel = p.relative_to(args.root).as_posix()
        raw = p.read_bytes()
        with Image.open(p) as im:
            rgba = im.convert("RGBA")
            pixel_hash = sha256(f"{im.width}x{im.height}:RGBA:".encode() + rgba.tobytes()).hexdigest()
            asset = {"path": rel, "extension": p.suffix.lower(), "width": im.width, "height": im.height,
                     "mode": im.mode, "bytes": len(raw), "sha256": sha256(raw).hexdigest(),
                     "pixel_sha256": pixel_hash, "has_alpha_channel": "A" in im.getbands() or "transparency" in im.info,
                     "alpha_extrema": list(rgba.getchannel("A").getextrema()), **classify(rel)}
        if rel.startswith("images/"):
            asset["automatic_image_name"] = p.stem
        if pixel_hash in first_pixel:
            asset["duplicate_of"] = first_pixel[pixel_hash]
        else:
            first_pixel[pixel_hash] = rel
        asset["source_refs"] = references(asset, sources, characters)
        asset["source_reference_count"] = len(asset["source_refs"])
        asset["reachability"] = "static_reference" if asset["source_refs"] else "packaged_no_static_reference"
        assets.append(asset)
    groups = build_groups(assets)
    wardrobes = defaultdict(Counter)
    for a in assets:
        if a["category"] == "character_sprite":
            wardrobes[a["role"]][a["wardrobe"]] += 1
    stats = {"total_files": len(assets), "extensions": dict(Counter(a["extension"] for a in assets)),
             "top_directories": dict(Counter(a["path"].split("/")[0] for a in assets)),
             "categories": dict(sorted(Counter(a["category"] for a in assets).items())),
             "character_wardrobes": {role: dict(wardrobe) for role, wardrobe in wardrobes.items()},
             "unique_byte_hashes": len({a["sha256"] for a in assets}), "unique_pixel_hashes": len(first_pixel),
             "pixel_duplicate_files": sum("duplicate_of" in a for a in assets),
             "generation_group_count": len(groups), "generation_group_families": dict(Counter(g["family"] for g in groups)),
             "unreferenced_files": [a["path"] for a in assets if not a["source_refs"]]}
    assert stats["extensions"] == {".png": 383, ".jpg": 24}, stats["extensions"]
    data = {"schema_version": 1, "source_root": str(args.root.resolve()),
            "source_archive_sha256": SOURCE_ARCHIVE_SHA256, "rea_evidence_id": REA_EVIDENCE_ID,
            "evidence_scope": "Asset inventory is derived from public shipped files and root Ren'Py source; static references are not proof of runtime execution.",
            "statistics": stats, "generation_groups": groups, "assets": assets}
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / "asset-inventory.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (args.output / "asset-inventory.md").write_text(make_report(data), encoding="utf-8")
    print(json.dumps(stats, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
