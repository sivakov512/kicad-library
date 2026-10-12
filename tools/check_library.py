"""Library integrity checks that KLC, ERC and DRC do not cover.

Usage: check_library.py

- symbol pin numbers match the pad numbers of the default footprint
- 3D models exist and are STEP files
- datasheets hosted in this repository exist and are PDFs
- every 3D model and datasheet in the repository is referenced

Files are read with the parsers of kicad-library-utils (git submodule).
"""

import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools", "kicad-library-utils", "common"))

from kicad_mod import KicadMod  # noqa: E402
from kicad_sym import KicadLibrary  # noqa: E402

PCM_PREFIX = "PCM_"
DATASHEET_URL = "https://cdn.jsdelivr.net/gh/sivakov512/kicad-library@main/"
OWN_MODEL = re.compile(r"^\$\{KICAD\d*_3RD_PARTY\}/3dmodels/com_github_sivakov512_kicad-library/(.*)$")
STOCK_MODEL = re.compile(r"^\$\{KICAD\d*_3DMODEL_DIR\}/(.*)$")
STOCK_MODEL_DIRS = [
    os.environ.get("KICAD10_3DMODEL_DIR", ""),
    "/Applications/KiCad/KiCad.app/Contents/SharedSupport/3dmodels",
    "/usr/share/kicad/3dmodels",
]

errors = []
used_files = set()


def error(where, msg):
    errors.append("%s: %s" % (where, msg))


def check_file(where, path, magic, kind, fmt):
    used_files.add(os.path.normpath(path))
    if not os.path.isfile(path):
        error(where, "%s %s does not exist" % (kind, os.path.relpath(path, ROOT)))
        return
    with open(path, "rb") as f:
        if f.read(len(magic)) != magic:
            error(where, "%s %s is not a %s file" % (kind, os.path.relpath(path, ROOT), fmt))


def check_datasheet(where, url):
    if url and url.startswith(DATASHEET_URL):
        check_file(where, os.path.join(ROOT, url[len(DATASHEET_URL):]), b"%PDF", "datasheet", "PDF")


def pin_numbers(number):
    """Expand KiCad 10 pin stacks written as "[1,2,5-7]"."""
    m = re.fullmatch(r"\[(.*)\]", number)
    if not m:
        return [number]
    out = []
    for part in m.group(1).split(","):
        a, _, b = part.strip().partition("-")
        out += [str(i) for i in range(int(a), int(b) + 1)] if b else [a]
    return out


def load_footprints():
    footprints = {}
    for path in sorted(glob.glob(os.path.join(ROOT, "footprints", "*.pretty", "*.kicad_mod"))):
        lib = os.path.basename(os.path.dirname(path))[: -len(".pretty")]
        footprints["%s%s:%s" % (PCM_PREFIX, lib, os.path.basename(path)[: -len(".kicad_mod")])] = KicadMod(path)
    return footprints


def check_footprints(footprints):
    stock_dir = next((d for d in STOCK_MODEL_DIRS if d and os.path.isdir(d)), None)
    if not stock_dir:
        print("WARN  KiCad 3D model directory not found, stock models are not checked")
    for fp_id, fp in footprints.items():
        where = fp_id[len(PCM_PREFIX):]
        # KLC F9.1: footprints carry the datasheet URL in their description
        for url in re.findall(re.escape(DATASHEET_URL) + r"\S+\.pdf", fp.description):
            check_datasheet(where, url)
        for model in fp.models:
            own, stock = OWN_MODEL.match(model["file"]), STOCK_MODEL.match(model["file"])
            if own:
                check_file(where, os.path.join(ROOT, "3dmodels", own.group(1)), b"ISO-10303", "3D model", "STEP")
            elif stock and stock_dir and not os.path.isfile(os.path.join(stock_dir, stock.group(1))):
                error(where, "stock 3D model %s does not exist" % stock.group(1))
            elif not own and not stock:
                error(where, "3D model path %s uses an unknown variable" % model["file"])


def symbol_property(sym, name):
    """Property value, falling back to the parent of a derived symbol."""
    p = sym.get_property(name) or sym.get_root_symbol().get_property(name)
    return p.value if p else ""


def check_symbols(footprints):
    for path in sorted(glob.glob(os.path.join(ROOT, "symbols", "*.kicad_sym"))):
        for sym in KicadLibrary.from_path(path).symbols:
            where = "%s:%s" % (sym.libname, sym.name)
            root = sym.get_root_symbol()
            check_datasheet(where, symbol_property(sym, "Datasheet"))
            fp_id = symbol_property(sym, "Footprint")
            if not fp_id.startswith(PCM_PREFIX):
                continue  # stock footprints are checked by ERC
            if fp_id not in footprints:
                error(where, "default footprint %s does not exist" % fp_id)
                continue
            pins = {n for pin in root.pins for n in pin_numbers(pin.number)}
            pads = {pad["number"] for pad in footprints[fp_id].pads if pad["number"]}
            if pins - pads:
                error(where, "pins without pads in the footprint: %s" % ", ".join(sorted(pins - pads)))
            if pads - pins:
                error(where, "footprint pads without pins: %s" % ", ".join(sorted(pads - pins)))


def check_unreferenced():
    for folder in ("3dmodels", "datasheets"):
        for path in sorted(glob.glob(os.path.join(ROOT, folder, "*", "*"))):
            if os.path.normpath(path) not in used_files:
                error(os.path.relpath(path, ROOT), "not referenced by any symbol or footprint")


def main():
    footprints = load_footprints()
    check_footprints(footprints)
    check_symbols(footprints)
    check_unreferenced()
    for line in errors:
        print("ERROR " + line)
    print("\nIntegrity: %d errors" % len(errors))
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
