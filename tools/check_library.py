"""Library integrity checks that KLC, ERC and DRC do not cover.

Usage: check_library.py

- symbol pin numbers match the pad numbers of the default footprint
- 3D models exist and are STEP files
- datasheets hosted in this repository exist and are PDFs
- every 3D model and datasheet in the repository is referenced
- the courtyard keeps COURTYARD_CLEARANCE around the pads and the F.Fab body

Files are read with the parsers of kicad-library-utils (git submodule).
"""

import glob
import math
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools", "kicad-library-utils", "common"))

from kicad_mod import KicadMod  # noqa: E402
from kicad_sym import KicadLibrary  # noqa: E402

# In the repository everything points at the working copy; tools/pcm_package.py
# rewrites nicknames, model paths and datasheet links for a release.
LOCAL_PREFIX = "LOCAL_"
DATASHEET_URL = "${KIPRJMOD}/"  # repository datasheets; pcm_package.py publishes and links them
OWN_MODEL = re.compile(r"^\$\{KIPRJMOD\}/3dmodels/(.*)$")
STOCK_MODEL = re.compile(r"^\$\{KICAD\d*_3DMODEL_DIR\}/(.*)$")
COURTYARD_CLEARANCE = 0.25  # KLC F5.3; the KLC checker only checks the grid and line width
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
        footprints["%s%s:%s" % (LOCAL_PREFIX, lib, os.path.basename(path)[: -len(".kicad_mod")])] = KicadMod(path)
    return footprints


def check_footprints(footprints):
    stock_dir = next((d for d in STOCK_MODEL_DIRS if d and os.path.isdir(d)), None)
    if not stock_dir:
        print("WARN  KiCad 3D model directory not found, stock models are not checked")
    for fp_id, fp in footprints.items():
        where = fp_id[len(LOCAL_PREFIX):]
        # KLC F9.1: footprints carry the datasheet in their description. In the
        # repository it is a local path (the package gets a URL), so the KLC
        # wrapper can't see it; check here that every footprint has one.
        local = re.findall(re.escape(DATASHEET_URL) + r"\S+?\.pdf", fp.description)
        for url in local:
            check_datasheet(where, url)
        if not local and not re.search(r"https?://", fp.description) and "KLC_F9.1" not in exceptions(fp):
            error(where, "description has no datasheet and there is no KLC_F9.1 exception")
        if "cdn.jsdelivr.net" in fp.description:
            error(where, "datasheet should be written as %sdatasheets/..." % DATASHEET_URL)
        check_courtyard(where, fp)
        for model in fp.models:
            own, stock = OWN_MODEL.match(model["file"]), STOCK_MODEL.match(model["file"])
            if own:
                expected = "%s.3dshapes/%s.step" % tuple(where.split(":"))
                if own.group(1) != expected:
                    error(where, "3D model %s should be %s" % (own.group(1), expected))
                check_file(where, os.path.join(ROOT, "3dmodels", own.group(1)), b"ISO-10303", "3D model", "STEP")
            elif stock and stock_dir and not os.path.isfile(os.path.join(stock_dir, stock.group(1))):
                error(where, "stock 3D model %s does not exist" % stock.group(1))
            elif not own and not stock:
                error(where, "3D model path %s uses an unknown variable" % model["file"])


def outline(fp, layer):
    bb = fp.geometricBoundingBox(layer)
    # BoundingBox.addPoint drops the radius of a circle centred on x or y = 0.
    for c in fp.filterCircles(layer):
        r = math.hypot(c["end"]["x"] - c["center"]["x"], c["end"]["y"] - c["center"]["y"])
        bb.addPoint(c["center"]["x"] - r, c["center"]["y"] - r)
        bb.addPoint(c["center"]["x"] + r, c["center"]["y"] + r)
    return bb


def check_courtyard(where, fp):
    if "KLC_F5.3" in exceptions(fp):
        return
    courtyard = outline(fp, "F.CrtYd")
    need = fp.overpadsBounds()
    body = outline(fp, "F.Fab")
    if body.valid:
        need.addBoundingBox(body)
    if not courtyard.valid or not need.valid:
        return  # a missing courtyard is reported by the KLC checker
    need.expand(COURTYARD_CLEARANCE - 1e-6)
    if (courtyard.xmin > need.xmin or courtyard.ymin > need.ymin
            or courtyard.xmax < need.xmax or courtyard.ymax < need.ymax):
        error(where, "courtyard (%.2f, %.2f)..(%.2f, %.2f) should cover pads and body with %g mm: (%.2f, %.2f)..(%.2f, %.2f)"
              % (courtyard.xmin, courtyard.ymin, courtyard.xmax, courtyard.ymax, COURTYARD_CLEARANCE,
                 need.xmin, need.ymin, need.xmax, need.ymax))


def exceptions(fp):
    """KLC_* exception property names of a footprint."""
    return {p.get("name", "") for p in getattr(fp, "properties", [])} | set(re.findall(r'"(KLC_[^"]+)"', open(fp.filename).read()))


def symbol_property(sym, name):
    """Property value, falling back to the parent of a derived symbol."""
    p = sym.get_property(name) or sym.get_root_symbol().get_property(name)
    return p.value if p else ""


def check_symbols(footprints):
    for path in sorted(glob.glob(os.path.join(ROOT, "symbols", "*.kicad_sym"))):
        for sym in KicadLibrary.from_path(path).symbols:
            where = "%s:%s" % (sym.libname, sym.name)
            root = sym.get_root_symbol()
            ds = symbol_property(sym, "Datasheet")
            check_datasheet(where, ds)
            if "cdn.jsdelivr.net" in ds:
                error(where, "datasheet should be written as %sdatasheets/..." % DATASHEET_URL)
            fp_id = symbol_property(sym, "Footprint")
            if fp_id.startswith("PCM_SKC_"):
                error(where, "footprint %s should use the local nickname %s" % (fp_id, LOCAL_PREFIX + fp_id[4:]))
                continue
            if not fp_id.startswith(LOCAL_PREFIX):
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
