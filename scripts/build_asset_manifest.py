#!/usr/bin/env python3
"""Merge generated-asset receipts without mistaking plans for generated files.

Default invocation may report a partial build. Use --require-complete for the
final gate and --qa-overview for an analysis-only checkerboard contact sheet.
Original images are read for validation and duplicate analysis only.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import hashlib
import json
import math
import os
from pathlib import Path, PurePosixPath
import tempfile

from PIL import Image, ImageDraw, ImageFont


DEFAULT_MANIFESTS = (
    "analysis/generated-root.json",
    "analysis/generated-characters.json",
    "analysis/generated-cg-bs.json",
    "analysis/generated-ui.json",
)
GENERATED = {"generated", "derived"}


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def sha256(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def clean_path(value):
    return str(value or "").replace("\\", "/")


def atomic_write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=path.parent, suffix=".tmp", delete=False
        ) as stream:
            temporary = Path(stream.name)
            stream.write(text)
        os.replace(temporary, path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def inside(root, value):
    candidate = (root / value).resolve()
    candidate.relative_to(root.resolve())
    return candidate


def expected_exclusion(asset):
    # The Chinese title remains required. No other asset category is excluded.
    path = clean_path(asset["path"])
    return path.startswith("tl/") and not path.startswith("tl/chinese/")


def canonical_group(raw, receipt):
    group = dict(raw)
    group["id"] = raw.get("id", raw.get("name", ""))
    group["path"] = clean_path(raw.get("path", raw.get("atlas", "")))
    group["promptPath"] = clean_path(raw.get("promptPath", raw.get("prompt", "")))
    group["receiptPath"] = receipt
    group["reportedStatus"] = raw.get("status", "pending")
    group["status"] = "pending"
    group["generationMode"] = raw.get("generationMode", "built-in-imagegen")
    group["limitations"] = list(raw.get("limitations", []))
    group["slots"] = []
    columns = raw.get("columns", 0)
    rows = raw.get("rows", 0)
    group["columns"], group["rows"] = columns, rows
    for fallback, cell in enumerate(raw.get("slots", raw.get("cells", []))):
        slot = dict(cell)
        slot["sourcePath"] = clean_path(
            cell.get("sourcePath", cell.get("source", cell.get("original_path", "")))
        )
        index = cell.get("index", cell.get("cell", fallback))
        row = cell.get("row", index // columns if columns else 0)
        column = cell.get("column", index % columns if columns else 0)
        slot.update(index=index, row=row, column=column)
        slot["uv"] = cell.get(
            "uv", [column / columns, row / rows, 1 / columns, 1 / rows]
            if columns and rows else None,
        )
        group["slots"].append(slot)
    # Keep canonical field names in the public manifest.
    for key in ("name", "atlas", "prompt", "cells"):
        group.pop(key, None)
    return group


def build(root, inventory_path, manifest_paths):
    inventory = load_json(root / inventory_path)
    originals = inventory["assets"]
    by_source = {clean_path(a["path"]): a for a in originals}
    errors, warnings, missing_receipts = [], [], []
    if len(by_source) != len(originals):
        errors.append("Inventory contains duplicate original paths.")
    source_root = Path(inventory.get("source_root", ""))
    if not source_root.is_dir():
        source_root = root / "analysis/reference/unpacked/game"

    source_errors = []
    source_pixel_cache = {}
    original_byte_hashes = set()
    for source, asset in by_source.items():
        path = source_root / source
        if not path.is_file():
            source_errors.append(f"{source}: original analysis reference missing")
            continue
        try:
            digest = sha256(path)
            original_byte_hashes.add(digest)
            if asset.get("sha256") and digest != asset["sha256"]:
                source_errors.append(f"{source}: original SHA256 differs from inventory")
            with Image.open(path) as image:
                if [image.width, image.height] != [asset["width"], asset["height"]]:
                    source_errors.append(f"{source}: original dimensions differ from inventory")
                if asset.get("mode") and image.mode != asset["mode"]:
                    source_errors.append(f"{source}: original mode differs from inventory")
        except (OSError, ValueError) as exc:
            source_errors.append(f"{source}: cannot inspect original: {exc}")
    errors.extend(source_errors)

    def true_pixel_duplicate(left, right):
        if left not in by_source or right not in by_source:
            return False
        first, second = by_source[left], by_source[right]
        if (first["width"], first["height"]) != (second["width"], second["height"]):
            return False
        # The inventory hash is only a candidate filter. Actual pixels decide.
        if first.get("pixel_sha256") != second.get("pixel_sha256"):
            return False
        for source in (left, right):
            if source not in source_pixel_cache:
                with Image.open(source_root / source) as image:
                    source_pixel_cache[source] = image.convert("RGBA").tobytes()
        return source_pixel_cache[left] == source_pixel_cache[right]

    groups = []
    ids = set()
    source_claims = defaultdict(list)
    for receipt in manifest_paths:
        receipt_path = root / receipt
        if not receipt_path.is_file():
            missing_receipts.append(receipt)
            continue
        data = load_json(receipt_path)
        for raw in data.get("groups", data.get("atlases", [])):
            group = canonical_group(raw, receipt)
            local_errors = []
            if not group["id"] or group["id"] in ids:
                local_errors.append("missing or repeated group id")
            ids.add(group["id"])
            columns, rows = group["columns"], group["rows"]
            if not all(isinstance(n, int) and n > 0 for n in (columns, rows)):
                local_errors.append("rows and columns must be positive integers")
            occupied = defaultdict(list)
            for slot in group["slots"]:
                source = slot["sourcePath"]
                source_claims[source].append((group, slot))
                if source not in by_source:
                    local_errors.append(f"unknown sourcePath: {source}")
                index, row, column = slot["index"], slot["row"], slot["column"]
                if not all(isinstance(n, int) for n in (index, row, column)):
                    local_errors.append(f"{source}: slot indices must be integers")
                elif rows and columns:
                    if not (0 <= row < rows and 0 <= column < columns):
                        local_errors.append(f"{source}: row/column outside grid")
                    if index != row * columns + column:
                        local_errors.append(f"{source}: index disagrees with row/column")
                uv = slot["uv"]
                if (not isinstance(uv, (list, tuple)) or len(uv) != 4
                    or not all(isinstance(n, (int, float)) and math.isfinite(n) for n in uv)):
                    local_errors.append(f"{source}: UV must have four finite numbers")
                elif not (uv[0] >= 0 and uv[1] >= 0 and uv[2] > 0 and uv[3] > 0
                          and uv[0] + uv[2] <= 1 + 1e-9
                          and uv[1] + uv[3] <= 1 + 1e-9):
                    local_errors.append(f"{source}: UV outside image")
                occupied[(row, column)].append(source)
            for cell, sources in occupied.items():
                if len(sources) > 1:
                    first_slot = next(s for s in group["slots"] if s["sourcePath"] == sources[0])
                    for source in sources[1:]:
                        slot = next(s for s in group["slots"] if s["sourcePath"] == source)
                        if true_pixel_duplicate(source, sources[0]):
                            slot.setdefault("derived_from", sources[0])
                        else:
                            # Explicit thumbnail/variant derivations must name
                            # their origin instead of claiming a unique redraw.
                            if not (slot.get("derived_from") or first_slot.get("derived_from")):
                                local_errors.append(f"cell {cell} used by nonduplicate sources: {sources}")
            image = None
            try:
                path = inside(root, group["path"])
                if not group["path"] or "analysis/reference" in group["path"]:
                    raise ValueError("output must be a project asset, not an original reference")
                if path.is_file():
                    with Image.open(path) as opened:
                        image = opened.copy()
                    digest = sha256(path)
                    group["actualSha256"] = digest
                    if group.get("sha256") and digest != group["sha256"]:
                        local_errors.append("output SHA256 disagrees with receipt")
                    if digest in original_byte_hashes:
                        local_errors.append("output is byte-identical to an original reference")
                    for field, value in (("width", image.width), ("height", image.height), ("mode", image.mode)):
                        if field in group and group[field] != value:
                            local_errors.append(f"output {field} disagrees with receipt")
                        group[field] = value
                    group["sha256"] = digest
                    group["bytes"] = path.stat().st_size
                    alpha = image.convert("RGBA").getchannel("A")
                    group["alphaExtrema"] = list(alpha.getextrema())
                    if columns and rows:
                        group["unusedCells"] = []
                        for row in range(rows):
                            for column in range(columns):
                                box = (round(column * image.width / columns), round(row * image.height / rows),
                                       round((column + 1) * image.width / columns), round((row + 1) * image.height / rows))
                                if box[2] <= box[0] or box[3] <= box[1]:
                                    local_errors.append(f"cell {(row, column)} has no pixels")
                                    continue
                                empty = alpha.crop(box).getextrema()[1] == 0
                                if (row, column) not in occupied:
                                    group["unusedCells"].append({"row": row, "column": column, "fullyTransparent": empty})
                        for slot in group["slots"]:
                            uv = slot["uv"]
                            if not isinstance(uv, (list, tuple)) or len(uv) != 4:
                                continue
                            box = (round(uv[0] * image.width), round(uv[1] * image.height),
                                   round((uv[0] + uv[2]) * image.width), round((uv[1] + uv[3]) * image.height))
                            empty = alpha.crop(box).getextrema()[1] == 0
                            slot["fullyTransparent"] = empty
                            original = by_source.get(slot["sourcePath"], {})
                            allowed_empty = slot.get("expected_empty", False) or original.get("alpha_extrema") == [0, 0]
                            if empty and not allowed_empty:
                                local_errors.append(f"{slot['sourcePath']}: required visible source maps to an empty generated cell")
                elif group["reportedStatus"] == "generated":
                    local_errors.append("receipt says generated but output file is missing")
                prompt = group["promptPath"]
                if group["reportedStatus"] == "generated" and (not prompt or not inside(root, prompt).is_file()):
                    local_errors.append("generated group has no saved prompt file")
            except (OSError, ValueError, TypeError) as exc:
                local_errors.append(f"cannot validate output: {exc}")
            group["validation"] = {"passed": not local_errors, "errors": local_errors}
            if local_errors:
                group["status"] = "invalid"
                errors.extend(f"{group['id']}: {item}" for item in local_errors)
            elif image is not None and group["reportedStatus"] == "generated":
                group["status"] = "generated"
            else:
                group["status"] = "pending"
            groups.append(group)

    duplicate_claims = {source: claims for source, claims in source_claims.items() if len(claims) > 1}
    for source in duplicate_claims:
        errors.append(f"{source}: claimed in multiple slots/groups")

    assets = []
    for source, original in by_source.items():
        asset = {
            "sourcePath": source,
            "category": original.get("category"),
            "description": original.get("description_zh", ""),
            "sourceWidth": original["width"],
            "sourceHeight": original["height"],
            "sourceMode": original.get("mode"),
            "sourceSha256": original.get("sha256"),
            "sourcePixelSha256": original.get("pixel_sha256"),
            "sourceReachability": original.get("reachability"),
            "status": "pending",
            "limitations": [],
        }
        if expected_exclusion(original):
            asset.update(status="excluded", excludedReason="Non-Chinese localization image; Chinese output scope.")
        elif source in duplicate_claims:
            asset.update(status="invalid", validationErrors=["Source path has multiple slot claims."])
        elif source in source_claims:
            group, slot = source_claims[source][0]
            asset.update(
                status=group["status"], groupId=group["id"], path=group["path"],
                promptPath=group["promptPath"], index=slot["index"], row=slot["row"],
                column=slot["column"], uv=slot["uv"], columns=group["columns"], rows=group["rows"],
                generationMode=group["generationMode"], limitations=list(group["limitations"]),
            )
            for field in ("width", "height", "mode", "sha256"):
                if field in group:
                    asset[field] = group[field]
            if slot.get("derived_from"):
                asset["derived_from"] = clean_path(slot["derived_from"])
                if asset["status"] == "generated":
                    asset["status"] = "derived"
                asset["derivationReason"] = slot.get("derivationReason", slot.get("note", "Explicit role thumbnail or variant reuse of a generated image cell."))
                asset["limitations"].extend(slot.get("limitations", []))
            if slot.get("fullyTransparent"):
                asset["fullyTransparent"] = True
                asset["limitations"].append("Intentionally transparent GUI state, matching the original empty visual role.")
            if group["status"] == "invalid":
                asset["validationErrors"] = group["validation"]["errors"]
        else:
            asset["pendingReason"] = "No generated source mapping in available receipts."
        if original.get("derived_from"):
            asset["originalDerivation"] = original["derived_from"]
        if original.get("duplicate_of"):
            asset["originalDuplicateOf"] = original["duplicate_of"]
        assets.append(asset)

    assets_by_source = {asset["sourcePath"]: asset for asset in assets}
    candidates = defaultdict(list)
    for asset in assets:
        if asset["status"] in GENERATED:
            candidates[asset.get("sourcePixelSha256")].append(asset)
    # Exact-pixel aliases may inherit a verified new image. A pending receipt is
    # retained as a plan, but is never itself evidence of completed generation.
    for asset in assets:
        if asset["status"] != "pending":
            continue
        for candidate in candidates.get(asset.get("sourcePixelSha256"), []):
            if true_pixel_duplicate(asset["sourcePath"], candidate["sourcePath"]):
                inherited = {k: candidate[k] for k in (
                    "path", "promptPath", "groupId", "index", "row", "column", "uv", "columns", "rows",
                    "width", "height", "mode", "sha256", "generationMode",
                ) if k in candidate}
                asset.update(inherited, status="derived", derived_from=candidate["sourcePath"])
                asset["derivationReason"] = "Original dimensions and actual RGBA pixels are identical. Reuse the verified new cell."
                asset["limitations"] = list(candidate["limitations"])
                asset.pop("pendingReason", None)
                break
    for asset in assets:
        if asset.get("derived_from") and asset["status"] in GENERATED:
            origin = assets_by_source.get(asset["derived_from"])
            if origin is None or origin["status"] not in GENERATED:
                asset["status"] = "invalid"
                errors.append(f"{asset['sourcePath']}: derived_from has no verified generated origin")
            elif asset.get("path") != origin.get("path") or asset.get("uv") != origin.get("uv"):
                asset["status"] = "invalid"
                errors.append(f"{asset['sourcePath']}: derived cell does not match its declared origin path/UV")

    counts = Counter(asset["status"] for asset in assets)
    required = len(assets) - counts["excluded"]
    covered = counts["generated"] + counts["derived"]
    coverage = {
        "totalOriginal": len(assets), "required": required, "excluded": counts["excluded"],
        "generatedDirect": counts["generated"], "direct_generated": counts["generated"],
        "derived": counts["derived"], "covered": covered,
        "pending": counts["pending"], "invalid": counts["invalid"],
        "coveragePercent": round(100 * covered / required, 2) if required else 100,
        "complete": covered == required and not errors,
        "groupCount": len(groups), "generatedGroupCount": sum(g["status"] == "generated" for g in groups),
        "missingManifests": missing_receipts, "validationErrors": errors, "validationWarnings": warnings,
        "duplicateSourcePaths": sorted(duplicate_claims), "sourceReferenceValidationErrors": source_errors,
        "pendingSourcePaths": [a["sourcePath"] for a in assets if a["status"] == "pending"],
        "excludedSourcePaths": [a["sourcePath"] for a in assets if a["status"] == "excluded"],
        "sourceReferencesAreAnalysisOnly": True,
        "sourceInventory": inventory_path,
        "evidenceScope": "This manifest verifies image files and static source-to-cell mappings. It does not claim runtime or gameplay equivalence.",
    }
    return {"coverage": coverage, "groups": groups, "assets": assets}


def markdown(result):
    coverage = result["coverage"]
    lines = ["# 新视觉素材覆盖清单", "", f"源路径 **{coverage['totalOriginal']}**；范围内 **{coverage['required']}**；已覆盖 **{coverage['covered']}**（{coverage['coveragePercent']}%）。",
             f"新绘图集槽位 {coverage['generatedDirect']}，缩略图复用或重复派生 {coverage['derived']}，待生成 {coverage['pending']}，无效 {coverage['invalid']}，排除非中文本地化 {coverage['excluded']}。", "",
             "所有原路径都保留在 JSON 的 `assets` 数组。`generated` 必须同时满足生成回执与文件校验；`pending` 不是已生成。源原图只用于分析，未进入交付映射。", "", "## 图集", "",
             "| 图集 | 状态 | 网格 | 尺寸 | 源槽位 | 产物 |", "|---|---|---|---|---:|---|"]
    for group in result["groups"]:
        lines.append(f"| {group['id']} | {group['status']} | {group['columns']}×{group['rows']} | {group.get('width', '?')}×{group.get('height', '?')} | {len(group['slots'])} | `{group['path']}` |")
    lines += ["", "## 已知视觉差异", ""]
    limitations = list(dict.fromkeys(item for group in result["groups"] for item in group["limitations"]))
    lines += ["- " + item for item in limitations] or ["无记录。"]
    lines += ["", "## 待生成路径", ""]
    lines += ["- `" + path + "`" for path in coverage["pendingSourcePaths"]] or ["无。"]
    lines += ["", "## 排除路径", ""]
    lines += ["- `" + path + "`" for path in coverage["excludedSourcePaths"]] or ["无。"]
    lines += ["", "## 校验", "", "- 检查输出文件、SHA256、图像尺寸和模式、格索引、UV 范围和源路径唯一性。", "- 原生透明 GUI 状态与未用空白格均允许透明。只读棋盘合成图属于分析资料。"]
    if coverage["missingManifests"]:
        lines.append("- 尚未提交的分清单：" + ", ".join("`" + x + "`" for x in coverage["missingManifests"]))
    lines.extend("- ERROR: " + error for error in coverage["validationErrors"])
    if not coverage["validationErrors"]:
        lines.append("- 当前已提交内容的校验通过。")
    return "\n".join(lines) + "\n"


def qa_overview(root, result, output):
    groups = [g for g in result["groups"] if g["status"] == "generated"]
    if not groups:
        return
    columns, cell_width, cell_height = 4, 400, 300
    canvas = Image.new("RGB", (columns * cell_width, math.ceil(len(groups) / columns) * cell_height), "#ececf3")
    draw = ImageDraw.Draw(canvas)
    try:
        font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 16)
    except OSError:
        font = ImageFont.load_default()
    for number, group in enumerate(groups):
        with Image.open(root / group["path"]) as original:
            image = original.convert("RGBA")
        image.thumbnail((cell_width - 12, cell_height - 35))
        checker = Image.new("RGB", image.size, "white")
        background = ImageDraw.Draw(checker)
        for y in range(0, image.height, 12):
            for x in range(0, image.width, 12):
                if (x // 12 + y // 12) % 2:
                    background.rectangle((x, y, x + 11, y + 11), fill="#c4d2d8")
        checker.paste(image, (0, 0), image)
        x, y = number % columns * cell_width, number // columns * cell_height
        canvas.paste(checker, (x + 6, y + 30))
        draw.text((x + 6, y + 4), f"{group['id']} {group['columns']}x{group['rows']}", fill="#242424", font=font)
    output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--inventory", default="analysis/asset-inventory.json")
    parser.add_argument("--manifest", action="append", help="Override default receipt list; repeat as needed.")
    parser.add_argument("--out-json", default="analysis/generated-assets.json")
    parser.add_argument("--out-md", default="analysis/generated-assets.md")
    parser.add_argument("--require-complete", action="store_true")
    parser.add_argument("--qa-overview", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    result = build(root, args.inventory, args.manifest or DEFAULT_MANIFESTS)
    if args.qa_overview:
        qa_path = "analysis/reference/style/generated-assets-overview.jpg"
        qa_overview(root, result, root / qa_path)
        result["coverage"]["analysisOverview"] = qa_path
    atomic_write(root / args.out_json, json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    atomic_write(root / args.out_md, markdown(result))
    summary = {key: value for key, value in result["coverage"].items()
               if key in {"totalOriginal", "required", "excluded", "covered", "pending", "invalid", "complete"}}
    summary["errorCount"] = len(result["coverage"]["validationErrors"])
    print(json.dumps(summary))
    if result["coverage"]["validationErrors"] or (args.require_complete and not result["coverage"]["complete"]):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
