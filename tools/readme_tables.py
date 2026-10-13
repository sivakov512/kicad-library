"""Regenerate the component tables in README.md from the libraries.

Usage: readme_tables.py [--check]

The tables live between the <!-- components:start --> and <!-- components:end -->
markers. With --check nothing is written; the exit code is 1 when README.md is out
of date.
"""

import os
import re
import sys

import kicadlib as kl

README = os.path.join(kl.ROOT, "README.md")
START, END = "<!-- components:start -->", "<!-- components:end -->"
YES, NO, NA = "✅", "❌", "—"
# Footprints that are copper only and have no physical body to model.
VIRTUAL = re.compile(r"^(Antenna_PCB_|TestPoint_)")


def table(header, rows):
    widths = [max(len(r[i]) for r in [header] + rows) for i in range(len(header))]
    line = lambda r: "| " + " | ".join(c.ljust(w) for c, w in zip(r, widths)) + " |"  # noqa: E731
    return "\n".join([line(header), "| " + " | ".join("-" * w for w in widths) + " |"] + [line(r) for r in rows])


def symbol_rows():
    rows = []
    for path in kl.symbol_libs():
        lib = kl.load(path)
        by_name = {s[1]: s for s in kl.children(lib, "symbol")}
        rows.append(["**%s**" % kl.lib_name(path), "", ""])
        for name, sym in by_name.items():
            flat = kl.flatten_symbol(sym, by_name)
            fp = kl.prop(flat, "Footprint", "").split(":")[-1]
            ds = kl.prop(flat, "Datasheet", "")
            rows.append(["`%s`" % name, "`%s`" % fp if fp else NA, YES if ds not in ("", "~") else NO])
    return rows


def footprint_rows():
    rows = []
    for lib_dir in kl.footprint_libs():
        rows.append(["**%s**" % kl.lib_name(lib_dir), "", ""])
        for path in kl.footprint_files(lib_dir):
            fp = kl.load(path)
            name = os.path.basename(path)[: -len(".kicad_mod")]
            descr = kl.child(fp, "descr")
            model = YES if kl.children(fp, "model") else (NA if VIRTUAL.match(name) else NO)
            datasheet = YES if descr and re.search(r"https?://", descr[1]) else NA
            rows.append(["`%s`" % name, model, datasheet])
    return rows


def render():
    return "\n\n".join([
        START,
        "**Legend:** ✅ available · ❌ not available · — not applicable",
        "### Symbols",
        table(["Symbol", "Footprint", "Datasheet"], symbol_rows()),
        "### Footprints",
        table(["Footprint", "3D model", "Datasheet"], footprint_rows()),
        END,
    ])


def main(check):
    text = open(README, encoding="utf-8").read()
    if START not in text or END not in text:
        sys.exit("README.md has no %s / %s markers" % (START, END))
    head, rest = text.split(START, 1)
    tail = rest.split(END, 1)[1]
    new = head + render() + tail
    if check:
        if new != text:
            print("README.md component tables are out of date, run `make readme`")
            return 1
        print("README.md component tables are up to date")
        return 0
    with open(README, "w", encoding="utf-8") as f:
        f.write(new)
    return 0


if __name__ == "__main__":
    sys.exit(main("--check" in sys.argv))
