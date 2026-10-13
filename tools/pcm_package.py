"""Build the PCM package from the working copy.

Usage: pcm_package.py TAG OUT.zip [--pages DIR] [--urls FILE]

In the repository every reference points at the working copy, so the library can be
edited in kicad-library.kicad_pro next to an installed release:

    footprints  LOCAL_SKC_<lib>:<name>
    3D models   ${KIPRJMOD}/3dmodels/<lib>.3dshapes/<name>.step
    datasheets  ${KIPRJMOD}/datasheets/<category>/<file>.pdf

The package gets the references PCM users need:

    footprints  PCM_SKC_<lib>:<name>
    3D models   ${KICADnn_3RD_PARTY}/3dmodels/<identifier>/<lib>.3dshapes/<name>.step
    datasheets  https://sivakov512.github.io/kicad-library/datasheets/<hash>/<file>.pdf

Datasheets are published on GitHub Pages under the hash of their content, so a link
in any release keeps pointing at the exact file that release shipped with, and an
unchanged file is published once. --pages DIR copies the files that need publishing
into a checkout of the site; --urls FILE lists every datasheet URL for checking.

The package is checked before it is zipped: nothing local may be left and every
footprint, 3D model and datasheet reference must resolve.
"""

import hashlib
import json
import os
import re
import shutil
import sys
import tempfile
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = ["symbols", "footprints", "3dmodels", "metadata.json"]
PAGES = "https://sivakov512.github.io/kicad-library/"
LOCAL_DATASHEET = re.compile(r"\$\{KIPRJMOD\}/(datasheets/[^\" ,)]+\.pdf)")
LOCAL_LEFTOVERS = ["LOCAL_SKC_", "${KIPRJMOD}"]


def published_path(rel):
    """datasheets/<hash>/<file>.pdf for a repository datasheet."""
    with open(os.path.join(ROOT, rel), "rb") as f:
        digest = hashlib.sha256(f.read()).hexdigest()[:12]
    return "datasheets/%s/%s" % (digest, os.path.basename(rel))


def library_files(stage):
    for folder, ext in (("symbols", ".kicad_sym"), ("footprints", ".kicad_mod")):
        for dirpath, _, names in os.walk(os.path.join(stage, folder)):
            for name in sorted(names):
                if name.endswith(ext):
                    yield os.path.join(dirpath, name)


def rewrite(stage, datasheets):
    meta = json.load(open(os.path.join(stage, "metadata.json")))
    major = meta["versions"][0]["kicad_version"].split(".")[0]
    model_dir = "${KICAD%s_3RD_PARTY}/3dmodels/%s/" % (major, meta["identifier"].replace(".", "_"))
    for path in library_files(stage):
        with open(path, encoding="utf-8") as f:
            text = f.read()
        text = text.replace('"LOCAL_SKC_', '"PCM_SKC_')
        text = text.replace("${KIPRJMOD}/3dmodels/", model_dir)
        def link(m):
            if not os.path.isfile(os.path.join(ROOT, m.group(1))):
                return m.group(0)  # left local; verify() reports it
            datasheets[m.group(1)] = published_path(m.group(1))
            return PAGES + datasheets[m.group(1)]
        text = LOCAL_DATASHEET.sub(link, text)
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
    return model_dir


def verify(stage, model_dir):
    errors = []
    footprints = set()
    for path in library_files(stage):
        if path.endswith(".kicad_mod"):
            lib = os.path.basename(os.path.dirname(path))[: -len(".pretty")]
            footprints.add("PCM_%s:%s" % (lib, os.path.basename(path)[: -len(".kicad_mod")]))
    for path in library_files(stage):
        rel = os.path.relpath(path, stage)
        text = open(path, encoding="utf-8").read()
        for leftover in LOCAL_LEFTOVERS:
            if leftover in text:
                errors.append("%s: still contains %s" % (rel, leftover))
        for fp in re.findall(r'\(property "Footprint" "(PCM_SKC_[^"]+)"', text):
            if fp not in footprints:
                errors.append("%s: footprint %s is not in the package" % (rel, fp))
        for model in re.findall(r'\(model "([^"]+)"', text):
            if model.startswith(model_dir):
                if not os.path.isfile(os.path.join(stage, "3dmodels", model[len(model_dir):])):
                    errors.append("%s: 3D model %s is not in the package" % (rel, model))
            elif not re.match(r"\$\{KICAD\d+_3DMODEL_DIR\}/", model):
                errors.append("%s: 3D model path %s is neither packaged nor stock" % (rel, model))
    return errors


def main(tag, out, pages=None, urls=None):
    datasheets = {}
    with tempfile.TemporaryDirectory() as stage:
        for item in CONTENT:
            src, dst = os.path.join(ROOT, item), os.path.join(stage, item)
            (shutil.copytree if os.path.isdir(src) else shutil.copy2)(src, dst)
        model_dir = rewrite(stage, datasheets)
        errors = verify(stage, model_dir)
        for line in errors:
            print("ERROR " + line)
        if errors:
            print("\nPackage: %d errors" % len(errors))
            return 1
        os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
            for dirpath, _, names in os.walk(stage):
                for name in sorted(names):
                    if name == ".DS_Store":
                        continue
                    path = os.path.join(dirpath, name)
                    z.write(path, os.path.relpath(path, stage))
    if pages:
        new = 0
        for rel, target in sorted(datasheets.items()):
            dst = os.path.join(pages, target)
            if not os.path.exists(dst):
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                shutil.copy2(os.path.join(ROOT, rel), dst)
                new += 1
        print("Pages: %d datasheets, %d new in %s" % (len(datasheets), new, pages))
    if urls:
        with open(urls, "w") as f:
            f.write("".join(PAGES + target + "\n" for target in sorted(set(datasheets.values()))))
    print("Package %s: %s (models %s, datasheets %s)" % (tag, os.path.relpath(out), model_dir, PAGES))
    return 0


if __name__ == "__main__":
    args = sys.argv[1:]
    opts = {}
    for key in ("--pages", "--urls"):
        if key in args:
            i = args.index(key)
            opts[key[2:]] = args[i + 1]
            del args[i:i + 2]
    if len(args) != 2:
        sys.exit(__doc__)
    sys.exit(main(args[0], args[1], **opts))
