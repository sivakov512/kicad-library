"""Generate a KiCad project that places every library footprint on one board for DRC.

Usage: gen_drc.py OUT_DIR
"""

import json
import os
import sys
import uuid

import kicadlib as kl

GAP = 5.0
ROW_WIDTH = 300.0
MARGIN = 10.0

# Typical fab minimums: anything tighter is a real manufacturability problem
# of the footprint rather than a quirk of KiCad's conservative defaults.
MIN_CLEARANCE = 0.1
MIN_HOLE_CLEARANCE = 0.2
MIN_EDGE_CLEARANCE = 0.2

# Rules about the footprints themselves are errors; rules that only make sense
# on a routed board are dropped.
ERROR_RULES = [
    "missing_courtyard",
    "malformed_courtyard",
    "footprint_type_mismatch",
    "lib_footprint_issues",
    "lib_footprint_mismatch",
    "silk_over_copper",
    "padstack",
    "annular_width",
    "drill_out_of_range",
    "hole_to_hole",
    "holes_co_located",
    "through_hole_pad_without_hole",
    "item_on_disabled_layer",
    "text_height",
    "text_thickness",
    "unresolved_variable",
]
WARNING_RULES = [
    "silk_overlap",
    "silk_edge_clearance",
]
IGNORED_RULES = [
    "unconnected_items",
    "footprint",
    "missing_footprint",
    "extra_footprint",
    "duplicate_footprints",
    "footprint_symbol_mismatch",
    "footprint_symbol_field_mismatch",
    "footprint_filters_mismatch",
    "net_conflict",
    "isolated_copper",
]


def bbox(fp):
    xs, ys = [], []
    for item in fp:
        if not isinstance(item, list):
            continue
        if item[0].startswith("fp_"):
            for key in ("start", "end", "center", "mid"):
                p = kl.child(item, key)
                if p:
                    xs.append(float(p[1]))
                    ys.append(float(p[2]))
            pts = kl.child(item, "pts")
            for xy in kl.children(pts or [], "xy"):
                xs.append(float(xy[1]))
                ys.append(float(xy[2]))
        elif item[0] == "pad":
            at, size = kl.child(item, "at"), kl.child(item, "size")
            r = max(float(size[1]), float(size[2])) / 2
            xs += [float(at[1]) - r, float(at[1]) + r]
            ys += [float(at[2]) - r, float(at[2]) + r]
    return min(xs), max(xs), min(ys), max(ys)


def translate(node, dx, dy):
    for item in node:
        if isinstance(item, list):
            if item[0] == "xy":
                item[1] = round(float(item[1]) + dx, 6)
                item[2] = round(float(item[2]) + dy, 6)
            else:
                translate(item, dx, dy)


def placed(fp, lib_id, ref, x, y):
    out = [fp[0], kl.Q(lib_id)]
    for item in fp[2:]:
        if isinstance(item, list) and item[0] in ("version", "generator", "generator_version"):
            continue
        if isinstance(item, list) and item[0] == "property" and item[1] == "Reference":
            item = item[:2] + [kl.Q(ref)] + item[3:]
        if isinstance(item, list) and item[0] == "zone":
            # Unlike other footprint items, zones are stored in board coordinates.
            translate(item, x, y)
        out.append(item)
        if isinstance(item, list) and item[0] == "layer":
            out += [["uuid", kl.Q(str(uuid.uuid4()))], ["at", round(x, 4), round(y, 4)]]
    return out


def main(out_dir):
    os.makedirs(out_dir, exist_ok=True)
    kl.project_lib_tables(out_dir)

    board = kl.load(os.path.join(kl.ROOT, "kicad-library.kicad_pcb"))
    board = [x for x in board if not (isinstance(x, list) and x[0] in ("footprint", "gr_rect", "gr_line"))]

    footprints = []
    x = y = MARGIN
    row_height = 0.0
    n = 0
    for lib_dir in kl.footprint_libs():
        nickname = kl.PCM_PREFIX + kl.lib_name(lib_dir)
        for path in kl.footprint_files(lib_dir):
            fp = kl.load(path)
            x0, x1, y0, y1 = bbox(fp)
            w, h = x1 - x0, y1 - y0
            if x + w > ROW_WIDTH + MARGIN and x > MARGIN:
                x, y, row_height = MARGIN, y + row_height + GAP, 0.0
            n += 1
            footprints.append(placed(fp, "%s:%s" % (nickname, fp[1]), "FP%d" % n, x - x0, y - y0))
            x += w + GAP
            row_height = max(row_height, h)

    outline = [
        "gr_rect",
        ["start", 0, 0],
        ["end", round(ROW_WIDTH + 2 * MARGIN + GAP, 4), round(y + row_height + MARGIN, 4)],
        ["stroke", ["width", 0.05], ["type", "default"]],
        ["fill", "no"],
        ["layer", kl.Q("Edge.Cuts")],
        ["uuid", kl.Q(str(uuid.uuid4()))],
    ]
    tail = board.index(kl.child(board, "embedded_fonts"))
    board[tail:tail] = footprints + [outline]
    with open(os.path.join(out_dir, "drc.kicad_pcb"), "w", encoding="utf-8") as f:
        f.write(kl.dump(board) + "\n")

    severities = {r: "error" for r in ERROR_RULES}
    severities.update({r: "warning" for r in WARNING_RULES})
    severities.update({r: "ignore" for r in IGNORED_RULES})
    project = {
        "board": {
            "design_settings": {
                "rule_severities": severities,
                "rules": {
                    "min_clearance": MIN_CLEARANCE,
                    "min_hole_clearance": MIN_HOLE_CLEARANCE,
                    "min_copper_edge_clearance": MIN_EDGE_CLEARANCE,
                },
            }
        },
        "net_settings": {"classes": [{"name": "Default", "clearance": MIN_CLEARANCE}]},
        "meta": {"filename": "drc.kicad_pro", "version": 3},
    }
    with open(os.path.join(out_dir, "drc.kicad_pro"), "w") as f:
        json.dump(project, f, indent=2)


if __name__ == "__main__":
    main(sys.argv[1])
