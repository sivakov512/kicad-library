"""Build the PCM package from the working copy.

Usage: pcm_package.py TAG OUT.zip

In the repository every reference points at the working copy, so the library can be
edited in kicad-library.kicad_pro next to an installed release:

    footprints  LOCAL_SKC_<lib>:<name>
    3D models   ${KIPRJMOD}/3dmodels/<lib>.3dshapes/<name>.step
    datasheets  https://cdn.jsdelivr.net/gh/sivakov512/kicad-library@main/...

The package gets the references PCM users need:

    footprints  PCM_SKC_<lib>:<name>
    3D models   ${KICADnn_3RD_PARTY}/3dmodels/<identifier>/<lib>.3dshapes/<name>.step
    datasheets  ...kicad-library@<TAG>/... (the files this release shipped with)

The package is checked before it is zipped: nothing local may be left and every
footprint and 3D model reference must resolve inside the package.
"""

import json
import os
import re
import shutil
import sys
import tempfile
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = ["symbols", "footprints", "3dmodels", "metadata.json"]
DATASHEETS = "https://cdn.jsdelivr.net/gh/sivakov512/kicad-library@"
LOCAL_LEFTOVERS = ["LOCAL_SKC_", "${KIPRJMOD}", DATASHEETS + "main/"]


def library_files(stage):
    for folder, ext in (("symbols", ".kicad_sym"), ("footprints", ".kicad_mod")):
        for dirpath, _, names in os.walk(os.path.join(stage, folder)):
            for name in sorted(names):
                if name.endswith(ext):
                    yield os.path.join(dirpath, name)


def rewrite(stage, tag):
    meta = json.load(open(os.path.join(stage, "metadata.json")))
    major = meta["versions"][0]["kicad_version"].split(".")[0]
    model_dir = "${KICAD%s_3RD_PARTY}/3dmodels/%s/" % (major, meta["identifier"].replace(".", "_"))
    for path in library_files(stage):
        with open(path, encoding="utf-8") as f:
            text = f.read()
        text = text.replace('"LOCAL_SKC_', '"PCM_SKC_')
        text = text.replace("${KIPRJMOD}/3dmodels/", model_dir)
        text = text.replace(DATASHEETS + "main/", DATASHEETS + tag + "/")
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
    return model_dir


def verify(stage, model_dir, tag):
    errors = []
    footprints = set()
    for path in library_files(stage):
        if path.endswith(".kicad_mod"):
            lib = os.path.basename(os.path.dirname(path))[: -len(".pretty")]
            footprints.add("PCM_%s:%s" % (lib, os.path.basename(path)[: -len(".kicad_mod")]))
    for path in library_files(stage):
        rel = os.path.relpath(path, stage)
        text = open(path, encoding="utf-8").read()
        for leftover in LOCAL_LEFTOVERS if tag != "main" else LOCAL_LEFTOVERS[:2]:
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


def main(tag, out):
    with tempfile.TemporaryDirectory() as stage:
        for item in CONTENT:
            src, dst = os.path.join(ROOT, item), os.path.join(stage, item)
            (shutil.copytree if os.path.isdir(src) else shutil.copy2)(src, dst)
        model_dir = rewrite(stage, tag)
        errors = verify(stage, model_dir, tag)
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
    print("Package: %s (datasheets @%s, models %s)" % (os.path.relpath(out), tag, model_dir))
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1], sys.argv[2]))
