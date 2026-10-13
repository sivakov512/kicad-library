"""Run the official KLC checkers (kicad-library-utils) over the library.

Usage: klc.py KLU_DIR BUILD_DIR {symbols|footprints} [--warnings]

Messages that only make sense for the official KiCad libraries are dropped;
everything else is reported. Exits non-zero when errors remain.
"""

import os
import re
import subprocess
import sys
import xml.etree.ElementTree as ET

import kicadlib as kl

# Some rules list every offending item; keep the report readable.
MAX_DETAILS = 10

# In the repository models are referenced from the working copy as
# ${KIPRJMOD}/3dmodels/<lib>.3dshapes/...; tools/pcm_package.py rewrites them to
# ${KICADn_3RD_PARTY}/... for a release. The checker only knows KiCad's bundled
# model directory, so these F9.3 messages are dropped when the folder matches.
IGNORED_MESSAGES = [
    re.compile(r"^Model path should start with '\$\{KICAD\d+_3DMODEL_DIR\}/'"),
    re.compile(r"^3D model directory is different from footprint directory "
               r"\(found '\$\{KIPRJMOD\}/3dmodels/(?P<dir>[^']+)', should be '(?P=dir)'\)"),
]


STOCK_FOOTPRINT_DIRS = [
    os.environ.get("KICAD10_FOOTPRINT_DIR", ""),
    "/Applications/KiCad/KiCad.app/Contents/SharedSupport/footprints",
    "/usr/share/kicad/footprints",
]


def footprint_aliases(build_dir):
    """Expose footprint libraries under the nicknames the symbols use: this
    library under its local nicknames, KiCad's stock libraries as they are."""
    alias_dir = os.path.join(build_dir, "fp-aliases")
    os.makedirs(alias_dir, exist_ok=True)
    libs = [(kl.LOCAL_PREFIX + os.path.basename(d), d) for d in kl.footprint_libs()]
    stock_dir = next((d for d in STOCK_FOOTPRINT_DIRS if d and os.path.isdir(d)), None)
    if stock_dir:
        libs += [(name, os.path.join(stock_dir, name)) for name in os.listdir(stock_dir) if name.endswith(".pretty")]
    for name, lib_dir in libs:
        link = os.path.join(alias_dir, name)
        if not os.path.islink(link):
            os.symlink(os.path.abspath(lib_dir), link)
    return alias_dir


def run_checker(klu_dir, build_dir, kind):
    junit = os.path.join(build_dir, "klc-%s.xml" % kind)
    if os.path.exists(junit):
        os.remove(junit)  # the checker appends to an existing report
    if kind == "symbols":
        script = "check_symbol.py"
        args = ["--footprints", footprint_aliases(build_dir)] + kl.symbol_libs()
    else:
        script = "check_footprint.py"
        args = [f for lib in kl.footprint_libs() for f in kl.footprint_files(lib)]
    cmd = [sys.executable, os.path.join(klu_dir, "klc-check", script), "--nocolor", "-s", "--junit", junit]
    proc = subprocess.run(cmd + args, capture_output=True, text=True)
    if not os.path.exists(junit):
        sys.stderr.write(proc.stdout + proc.stderr)
        sys.exit("KLC checker failed to run")
    # The checker reports unparsable files on stdout only.
    unparsable = [line for line in proc.stdout.splitlines() if line.startswith("Could not parse")]
    return ET.parse(junit).getroot(), unparsable


def filtered(text):
    """Drop ignored messages (with their indented detail lines)."""
    lines = text.splitlines()
    out, skipping = [], False
    for line in lines[2:]:  # first two lines are the rule title and URL
        stripped = line.strip()
        if any(p.search(stripped) for p in IGNORED_MESSAGES):
            skipping = True
            continue
        if skipping and stripped.startswith("- "):
            continue
        skipping = False
        out.append(line)
    if len(out) > MAX_DETAILS:
        out = out[:MAX_DETAILS] + ["       ... and %d more lines" % (len(out) - MAX_DETAILS)]
    return lines[:1], out


def rule_exceptions(kind):
    """Rules waived per item by `KLC_<rule>` or `KLC_<rule>_<pin>` properties.

    The checker honours them in its own counts but still lists the violations in
    the JUnit report. A property without a pin waives the whole rule for the item;
    `KLC_S4.4_5V` waives it only for messages about pin 5V.
    """
    waived = {}
    klc = re.compile(r"^KLC_([^_]+)_*(.*)$")
    if kind == "symbols":
        items = [("%s:%s" % (kl.lib_name(path), sym[1]), sym) for path in kl.symbol_libs()
                 for sym in kl.children(kl.load(path), "symbol")]
    else:
        items = [(kl.lib_name(f), kl.load(f)) for lib in kl.footprint_libs() for f in kl.footprint_files(lib)]
    for item, node in items:
        for prop in kl.children(node, "property"):
            key = prop[2] if prop[1] == "private" else prop[1]
            m = klc.match(key)
            if m:
                pins = waived.setdefault(item, {}).setdefault(m.group(1), set())
                pins.add(m.group(2) or "*")
    return waived


def is_waived(rule, details, waived_rules):
    pins = waived_rules.get(rule)
    if not pins:
        return False
    if "*" in pins:
        return True
    # only waive when every pin the message is about is a waived one
    named = re.findall(r"Pin (\S+) \(", "\n".join(details))
    return bool(named) and all(n in pins for n in named)


def main():
    klu_dir, build_dir, kind = sys.argv[1:4]
    show_warnings = "--warnings" in sys.argv
    os.makedirs(build_dir, exist_ok=True)
    root, unparsable = run_checker(klu_dir, build_dir, kind)

    waived = rule_exceptions(kind)
    counts = {"FAILURE": 0, "WARNING": 0}
    report = {}
    for case in root.iter("testcase"):
        item = case.get("name").rsplit(" - ", 1)[0]
        for failure in case.iter("failure"):
            severity = failure.get("type")
            title, details = filtered(failure.text or "")
            if not details or is_waived(title[0].split(":")[0], details, waived.get(item, {})):
                continue
            counts[severity] = counts.get(severity, 0) + 1
            if severity == "FAILURE" or show_warnings:
                tag = "ERROR" if severity == "FAILURE" else "WARN "
                report.setdefault(item, []).append("  [%s] %s\n%s" % (tag, title[0], "\n".join(details)))

    for item in sorted(report):
        print("%s:" % item)
        print("\n".join(report[item]))
    for line in unparsable:
        print(line)
    print(
        "\nKLC %s: %d errors, %d warnings%s"
        % (kind, counts["FAILURE"] + len(unparsable), counts["WARNING"], "" if show_warnings else " (use KLC_WARNINGS=1 to list)")
    )
    sys.exit(1 if counts["FAILURE"] or unparsable else 0)


if __name__ == "__main__":
    main()
