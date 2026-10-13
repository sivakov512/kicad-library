"""Regenerate the component list in README.md from the libraries.

Usage: readme_tables.py [--check]

The list lives between the <!-- components:start --> and <!-- components:end -->
markers: one row per part, grouped by category. A part is a symbol with its
footprint, or a footprint that is used with a stock KiCad symbol. With --check
nothing is written; the exit code is 1 when README.md is out of date.
"""

import collections
import os
import re
import sys

import kicadlib as kl

README = os.path.join(kl.ROOT, "README.md")
START, END = "<!-- components:start -->", "<!-- components:end -->"
LOCAL_URL = "${KIPRJMOD}/"
YES, NO, NA = "✅", "❌", "—"
# Footprints that are copper only and have no physical body to model.
VIRTUAL = re.compile(r"^(Antenna_PCB_|TestPoint_)")


def category(lib):
    return re.sub(r"_(SMD|THT)$", "", lib[len("SKC_"):]).replace("_", " ")


def anchor(title):
    return re.sub(r"[^a-z0-9 -]", "", title.lower()).replace(" ", "-")


def maker(url):
    """Manufacturer from a repository datasheet name: <Manufacturer>_<PartNumber>.pdf."""
    if url.startswith(LOCAL_URL):
        return os.path.basename(url).split("_", 1)[0]
    return ""


def human_part(url, fallback):
    """'Manufacturer PartNumber' from a repository datasheet name, else the fallback."""
    if url.startswith(LOCAL_URL):
        return os.path.basename(url)[: -len(".pdf")].replace("_", " ", 1)
    return fallback


def datasheet_link(url):
    if not url or url == "~":
        return NA
    if url.startswith(LOCAL_URL):
        return "[PDF](%s)" % url[len(LOCAL_URL):]
    return "[link](%s)" % url


def footprints():
    """name -> (category, model, datasheet url, description) for this library's footprints."""
    out = {}
    for lib_dir in kl.footprint_libs():
        lib = kl.lib_name(lib_dir)
        for path in kl.footprint_files(lib_dir):
            fp = kl.load(path)
            name = os.path.basename(path)[: -len(".kicad_mod")]
            descr = (kl.child(fp, "descr") or ["", ""])[1]
            url = (re.search(r"(https?://|\$\{KIPRJMOD\}/)\S+", descr) or [""])[0].rstrip(",")
            model = YES if kl.children(fp, "model") else (NA if VIRTUAL.match(name) else NO)
            out["%s:%s" % (lib, name)] = (category(lib), model, url, re.sub(r",?\s*(https?://|\$\{KIPRJMOD\}/)\S+", "", descr).strip())
    return out


def rows():
    fps = footprints()
    used = set()
    groups = collections.defaultdict(list)
    for path in kl.symbol_libs():
        lib = kl.lib_name(path)
        by_name = {s[1]: s for s in kl.children(kl.load(path), "symbol")}
        merged = collections.OrderedDict()  # derived variants with the same footprint share a row
        for name, sym in by_name.items():
            flat = kl.flatten_symbol(sym, by_name)
            fp = kl.prop(flat, "Footprint", "")
            nick, _, fp_name = fp.partition(":")
            if nick.startswith(kl.LOCAL_PREFIX):
                key = "%s:%s" % (nick[len(kl.LOCAL_PREFIX):], fp_name)
                used.add(key)
                fp_cell, model = "`%s`" % fp_name, fps[key][1]
            else:
                fp_cell, model = ("`%s` (KiCad)" % fp_name if fp_name else NA), "KiCad"
            parent = kl.child(sym, "extends")
            group_key = (parent[1] if parent is not None else name, fp)
            url = kl.prop(flat, "Datasheet", "")
            row = merged.setdefault(group_key, {"names": [], "desc": kl.prop(flat, "Description", ""),
                                                "fp": fp_cell, "model": model, "maker": maker(url), "url": url,
                                                "ds": datasheet_link(url)})
            row["names"].append(name)
        for row in merged.values():
            names = row["names"]
            label = names[0] if len(names) == 1 else "%s … %s" % (names[0], names[-1])
            if row["maker"] and label.startswith(row["maker"] + "_"):
                label = label[len(row["maker"]) + 1:]
            part_number = human_part(row["url"], "").partition(" ")[2]
            if len(names) == 1 and part_number and label != part_number and label.endswith(part_number):
                label = part_number  # e.g. SW_SP3T_SS13D07VG4 -> SS13D07VG4
            if not row["maker"] and "_" in label:
                label = label.replace("_", " ", 1)  # Manufacturer_Part symbols with an external datasheet
            part = ("%s %s" % (row["maker"], label)).strip()
            symbols = "`%s`" % names[0] if len(names) == 1 else "`%s` … `%s` (%d)" % (names[0], names[-1], len(names))
            groups[category(lib)].append([part, row["desc"], symbols, row["fp"], row["model"], row["ds"]])
    for key, (cat, model, url, descr) in fps.items():
        if key not in used:
            name = key.split(":", 1)[1]
            groups[cat].append([human_part(url, name), descr, "KiCad", "`%s`" % name, model, datasheet_link(url)])
    return groups


def table(header, body):
    out = ["| " + " | ".join(header) + " |", "|" + "|".join(" --- " for _ in header) + "|"]
    out += ["| " + " | ".join(c.replace("|", "\\|") for c in r) + " |" for r in body]
    return "\n".join(out)


def render():
    groups = rows()
    cats = sorted(groups)
    parts = [START,
             "\n".join("- [%s](#%s) — %d" % (c, anchor(c), len(groups[c])) for c in cats),
             "\n".join([
                 "Legend:",
                 "",
                 "- **Symbol** `KiCad`: no own symbol, use a stock KiCad one",
                 "- **Footprint** `(KiCad)`: stock KiCad footprint",
                 "- **3D model** ✅ included · ❌ not available · — copper only, no body · KiCad: stock model",
             ])]
    for c in cats:
        body = sorted(groups[c], key=lambda r: r[0].lower())
        parts += ["### %s" % c, table(["Part", "Description", "Symbol", "Footprint", "3D model", "Datasheet"], body)]
    parts.append(END)
    return "\n\n".join(parts)


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
