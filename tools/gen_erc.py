"""Generate a KiCad project that places every library symbol on one schematic for ERC.

Usage: gen_erc.py OUT_DIR
"""

import json
import os
import sys
import uuid

import kicadlib as kl

SCH_VERSION = "20260306"
GRID = 2.54
ROW_WIDTH = 400 * GRID

# Unconnected test placement makes these checks meaningless; everything else
# (symbol/footprint links, filters, stacked pins, off-grid pins...) is kept.
IGNORED_RULES = [
    "pin_not_connected",
    "pin_not_driven",
    "power_pin_not_driven",
    "missing_power_pin",
    "missing_input_pin",
    "missing_bidi_pin",
    "no_connect_dangling",
    "simulation_model_issue",
]
ERROR_RULES = [
    "lib_symbol_issues",
    "lib_symbol_mismatch",
    "footprint_link_issues",
    "footprint_filter",
    "stacked_pin_name",
    "endpoint_off_grid",
    "no_connect_connected",
    "pin_to_pin",
    "different_unit_footprint",
    "different_unit_net",
    "missing_unit",
    "duplicate_reference",
    "unannotated",
    "unresolved_variable",
    "field_name_whitespace",
]


def new_uuid():
    return kl.Q(str(uuid.uuid4()))


def snap(v):
    return round(round(v / GRID) * GRID, 4)


def bbox(sym):
    xs, ys = [0.0], [0.0]

    def walk(node):
        for item in node:
            if not isinstance(item, list):
                continue
            if item[0] in ("at", "start", "end", "center", "mid", "xy") and len(item) >= 3:
                try:
                    xs.append(float(item[1]))
                    ys.append(float(item[2]))
                except ValueError:
                    pass
            if item[0] != "property":
                walk(item)

    walk(sym)
    return min(xs), max(xs), min(ys), max(ys)


def instance(lib_id, sym, unit, ref, x, y, root_uuid):
    props = kl.properties(sym)
    node = [
        "symbol",
        ["lib_id", kl.Q(lib_id)],
        ["at", x, y, 0],
        ["unit", unit],
        ["exclude_from_sim", "no"],
        ["in_bom", "yes"],
        ["on_board", "yes"],
        ["dnp", "no"],
        ["uuid", new_uuid()],
    ]
    for name, p in props.items():
        if name.startswith("ki_") or name == "private":  # private: KLC exception notes
            continue
        value = kl.Q(ref) if name == "Reference" else p[2]
        at = kl.child(p, "at") or ["at", 0, 0, 0]
        placed = ["at", round(float(at[1]) + x, 4), round(y - float(at[2]), 4)] + at[3:]
        field = ["property", kl.Q(name), value, placed]
        field += [c for c in p[3:] if isinstance(c, list) and c[0] not in ("at", "id")]
        node.append(field)
    node.append(
        ["instances", ["project", kl.Q("erc"), ["path", kl.Q("/" + root_uuid), ["reference", kl.Q(ref)], ["unit", unit]]]]
    )
    return node


def main(out_dir):
    os.makedirs(out_dir, exist_ok=True)
    kl.project_lib_tables(out_dir)
    root_uuid = str(uuid.uuid4())

    lib_symbols = ["lib_symbols"]
    placed = []
    refs = {}
    x = y = 0.0
    row_height = 0.0
    for path in kl.symbol_libs():
        nickname = kl.LOCAL_PREFIX + kl.lib_name(path)
        lib = kl.load(path)
        by_name = {s[1]: s for s in kl.children(lib, "symbol")}
        for name, sym in by_name.items():
            flat = kl.flatten_symbol(sym, by_name)
            lib_id = "%s:%s" % (nickname, name)
            embedded = [flat[0], kl.Q(lib_id)] + flat[2:]
            lib_symbols.append(embedded)

            prefix = kl.prop(flat, "Reference", "U")
            refs[prefix] = refs.get(prefix, 0) + 1
            ref = "%s%d" % (prefix, refs[prefix])
            for unit in kl.symbol_units(flat):
                x0, x1, y0, y1 = bbox(flat)
                width, height = x1 - x0 + 20 * GRID, y1 - y0 + 20 * GRID
                if x + width > ROW_WIDTH:
                    x, y, row_height = 0.0, y + row_height, 0.0
                px, py = snap(x - x0 + 10 * GRID), snap(y + y1 + 10 * GRID)
                placed.append(instance(lib_id, flat, unit, ref, px, py, root_uuid))
                x += width
                row_height = max(row_height, height)

    sch = [
        "kicad_sch",
        ["version", SCH_VERSION],
        ["generator", kl.Q("kicad-library-check")],
        ["generator_version", kl.Q("10.0")],
        ["uuid", kl.Q(root_uuid)],
        ["paper", kl.Q("User"), snap(ROW_WIDTH + 40 * GRID), snap(y + row_height + 40 * GRID)],
        lib_symbols,
    ] + placed + [["sheet_instances", ["path", kl.Q("/"), ["page", kl.Q("1")]]], ["embedded_fonts", "no"]]

    with open(os.path.join(out_dir, "erc.kicad_sch"), "w", encoding="utf-8") as f:
        f.write(kl.dump(sch) + "\n")

    severities = {r: "ignore" for r in IGNORED_RULES}
    severities.update({r: "error" for r in ERROR_RULES})
    project = {"erc": {"rule_severities": severities}, "meta": {"filename": "erc.kicad_pro", "version": 3}}
    with open(os.path.join(out_dir, "erc.kicad_pro"), "w") as f:
        json.dump(project, f, indent=2)


if __name__ == "__main__":
    main(sys.argv[1])
