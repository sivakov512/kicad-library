"""Library integrity checks that KLC, ERC and DRC do not cover.

Usage: check_library.py

- symbol pin numbers match the pad numbers of the default footprint
- 3D models exist and are STEP files
- datasheets hosted in this repository exist and are PDFs
- every 3D model and datasheet in the repository is referenced
- the courtyard keeps the KLC F5.3 clearance around every pad

Files are read with the parsers of kicad-library-utils (git submodule).
"""

import contextlib
import glob
import io
import math
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools", "kicad-library-utils", "common"))
sys.path.insert(0, os.path.join(ROOT, "tools", "kicad-library-utils", "klc-check"))

from kicad_mod import KicadMod  # noqa: E402
from kicad_sym import KicadLibrary  # noqa: E402
from rules_footprint import F5_3  # noqa: E402

# In the repository everything points at the working copy; tools/pcm_package.py
# rewrites nicknames, model paths and datasheet links for a release.
LOCAL_PREFIX = "LOCAL_"
DATASHEET_URL = "${KIPRJMOD}/"  # repository datasheets; pcm_package.py publishes and links them
OWN_MODEL = re.compile(r"^\$\{KIPRJMOD\}/3dmodels/(.*)$")
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


def xy(p):
    return (p["x"], p["y"])


def circle_points(cx, cy, r, a0, sweep):
    """Polyline along an arc, with a chord error far below the courtyard grid."""
    n = max(8, int(abs(sweep) / (2 * math.acos(max(-1.0, 1 - 1e-4 / r))) + 1)) if r > 0 else 1
    return [(cx + r * math.cos(a0 + sweep * i / n), cy + r * math.sin(a0 + sweep * i / n)) for i in range(n + 1)]


def arc_points(s, m, e):
    (x1, y1), (x2, y2), (x3, y3) = s, m, e
    d = 2 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    if abs(d) < 1e-12:
        return [s, e]
    cx = ((x1**2 + y1**2) * (y2 - y3) + (x2**2 + y2**2) * (y3 - y1) + (x3**2 + y3**2) * (y1 - y2)) / d
    cy = ((x1**2 + y1**2) * (x3 - x2) + (x2**2 + y2**2) * (x1 - x3) + (x3**2 + y3**2) * (x2 - x1)) / d
    a1, a2, a3 = (math.atan2(y - cy, x - cx) for x, y in (s, m, e))
    sweep = (a3 - a1) % (2 * math.pi)
    if (a2 - a1) % (2 * math.pi) > sweep:  # mid is on the other side: go clockwise
        sweep -= 2 * math.pi
    return circle_points(cx, cy, math.hypot(x1 - cx, y1 - cy), a1, sweep)


def courtyard_segments(fp):
    """F.CrtYd outline as straight segments; arcs and circles are approximated."""
    layer = "F.CrtYd"
    chains = [[xy(ln["start"]), xy(ln["end"])] for ln in fp.filterLines(layer)]
    for r in fp.filterRects(layer):
        (x0, y0), (x1, y1) = xy(r["start"]), xy(r["end"])
        chains.append([(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)])
    for p in fp.filterPolys(layer):
        pts = [xy(q) for q in p["points"]]
        chains.append(pts + pts[:1])
    for c in fp.filterCircles(layer):
        (cx, cy), (ex, ey) = xy(c["center"]), xy(c["end"])
        chains.append(circle_points(cx, cy, math.hypot(ex - cx, ey - cy), 0, 2 * math.pi))
    for a in fp.filterArcs(layer):
        chains.append(arc_points(xy(a["start"]), xy(a["mid"]), xy(a["end"])))
    return [(c[i], c[i + 1]) for c in chains for i in range(len(c) - 1)]


def inside(point, segments):
    """Even-odd test: is the point inside the area enclosed by the segments?"""
    x, y = point
    crossings = 0
    for (x1, y1), (x2, y2) in segments:
        if (y1 > y) != (y2 > y) and x < x1 + (y - y1) * (x2 - x1) / (y2 - y1):
            crossings += 1
    return crossings % 2 == 1


def point_segment_distance(p, a, b):
    (px, py), (ax, ay), (bx, by) = p, a, b
    dx, dy = bx - ax, by - ay
    t = ((px - ax) * dx + (py - ay) * dy) / (dx * dx + dy * dy) if dx or dy else 0
    t = min(1, max(0, t))
    return math.hypot(px - ax - t * dx, py - ay - t * dy)


def segments_cross(a, b, c, d):
    def side(p, q, r):
        return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])
    return side(a, b, c) * side(a, b, d) < 0 and side(c, d, a) * side(c, d, b) < 0


def segment_rect_distance(a, b, hw, hh):
    """Distance between a segment and the rectangle |x| <= hw, |y| <= hh."""
    if any(abs(x) <= hw and abs(y) <= hh for x, y in (a, b)):
        return 0.0
    corners = [(-hw, -hh), (hw, -hh), (hw, hh), (-hw, hh)]
    edges = [(corners[i], corners[(i + 1) % 4]) for i in range(4)]
    if any(segments_cross(a, b, c, d) for c, d in edges):
        return 0.0
    return min([point_segment_distance(p, c, d) for c, d in edges for p in (a, b)]
               + [point_segment_distance(c, a, b) for c in corners])


def pad_outline(pad):
    """A pad as a rectangle (half sizes) grown by a radius: covers rect, roundrect, oval and circle."""
    w, h = pad["size"]["x"], pad["size"]["y"]
    shape = pad["shape"]
    if shape == "circle":
        r = w / 2
    elif shape == "oval":
        r = min(w, h) / 2
    elif shape == "roundrect":
        r = min(w, h) * float(pad["roundrect_rratio"] or 0)
    else:  # rect; custom and other shapes are checked by their anchor size
        r = 0.0
    return w / 2 - r, h / 2 - r, r


def courtyard_clearance(fp):
    """KLC F5.3 clearance for this footprint: 0.25 mm, 0.5 mm for connectors, buttons
    and switches, 0.15 mm for parts under 2x2 mm. Taken from the KLC checker, which
    only uses it to draw a courtyard and doesn't check it."""
    with contextlib.redirect_stdout(io.StringIO()):
        return F5_3.Rule(fp, None).defaultOffset()


def check_courtyard(where, fp):
    """Every pad lies inside the courtyard and no courtyard edge comes closer than the clearance."""
    if "KLC_F5.3" in exceptions(fp):
        return
    segments = courtyard_segments(fp)
    if not segments:
        return  # a missing courtyard is reported by the KLC checker
    clearance = courtyard_clearance(fp)
    for pad in fp.pads:
        px, py = pad["pos"]["x"], pad["pos"]["y"]
        name = pad["number"] or "unnamed"
        if not inside((px, py), segments):
            error(where, "pad %s at (%g, %g) is outside the courtyard" % (name, px, py))
            continue
        hw, hh, r = pad_outline(pad)
        angle = math.radians(pad["pos"]["orientation"])
        cos, sin = math.cos(angle), math.sin(angle)

        def local(p):
            x, y = p[0] - px, p[1] - py
            return (x * cos - y * sin, x * sin + y * cos)

        gap = min(segment_rect_distance(local(a), local(b), hw, hh) for a, b in segments) - r
        if gap < clearance - 1e-3:
            error(where, "pad %s at (%g, %g) is %.3f mm from the courtyard, needs %g mm"
                  % (name, px, py, gap, clearance))


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
