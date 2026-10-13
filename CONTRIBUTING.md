# Contributing

The [KiCad Library Conventions (KLC)](https://klc.kicad.org) are the baseline. This file lists only what KLC leaves open or what is specific to this repository. `make check` enforces most of it.

## Setup

Requirements:

- KiCad 10 with `kicad-cli` on `PATH`.
- Python 3.10 or newer. [uv](https://docs.astral.sh/uv/) is used automatically when installed.
- `make`.

Then:

```bash
git clone --recursive https://github.com/sivakov512/kicad-library.git
make check
```

Open `kicad-library.kicad_pro` to edit the library. Its project library tables load the working copy, so you can keep a released version installed through the Plugin and Content Manager without the two getting mixed up.

| Check | What it covers |
| --- | --- |
| `make integrity` | Symbol pins match footprint pads; 3D models and datasheets exist and are STEP/PDF; no unreferenced files. |
| `make klc` | Official KLC checker from [kicad-library-utils](https://gitlab.com/kicad/libraries/kicad-library-utils) (git submodule). `KLC_WARNINGS=1` lists warnings. |
| `make erc` / `make drc` | ERC on a schematic and DRC on a board generated with every symbol and footprint. |
| `make package` | Builds the PCM package the way a release does and checks it. |
| `make readme` | Regenerates the component tables in `README.md` (`make check` fails when they are stale). |

CI runs the same checks on every pull request.

## Layout and naming

```
symbols/     SKC_<Category>.kicad_sym
footprints/  SKC_<Category>.pretty/<footprint>.kicad_mod
3dmodels/    SKC_<Category>.3dshapes/<footprint>.step
datasheets/  <Category>/<Manufacturer>_<PartNumber>.pdf
```

- **Categories** mirror the stock KiCad library names. Footprint libraries add `_SMD`/`_THT` where the stock ones do.
- **Names** follow KLC and the stock libraries:
  - Symbols are named by part number (`TPS2121RUX`).
  - Footprints are named by package, or by type, manufacturer and part (`ROHM_SOP-8_4.4x5mm_P1.27mm`, `Relay_SPDT_Relpol_RM51`).
- **Wildcards** for part families use a lowercase `x` (`A7672x`, `Maxim_MAX1704x.pdf`).
- **Datasheets** sit in the category of the symbol, or of the footprint when there is no symbol. The manufacturer is spelled as in the footprint name.

## References inside the repository

Everything points at the working copy. `tools/pcm_package.py` rewrites the references when a release is built.

| Reference | Write it as | Released as |
| --- | --- | --- |
| Footprint of a symbol | `LOCAL_SKC_<Category>:<name>` | `PCM_SKC_<Category>:<name>` |
| 3D model of a footprint | `${KIPRJMOD}/3dmodels/SKC_<Category>.3dshapes/<name>.step` | `${KICAD10_3RD_PARTY}/3dmodels/com_github_sivakov512_kicad-library/...` |
| Datasheet | `https://cdn.jsdelivr.net/gh/sivakov512/kicad-library@main/datasheets/...` | `...@<release tag>/datasheets/...` |

- **Symbols** keep the datasheet URL in the **Datasheet** field.
- **Footprints** keep it at the end of the **Description**: KLC F9.1 forbids a Datasheet field on footprints.

## Symbols

- **Pins:** 100 mil long. Use 150 mil when pin numbers have three digits; all pins of a symbol share one length.
- **Pin stacks:** stack power and ground pins with KiCad 10 native stacks. Write the numbers as a comma list, `[6,7,8,9,10]`, not as ranges, so they fit a 100 mil pin. Split very long stacks into several pins.
- **Never stack no-connect pins.** Hide them inside the body as separate `no_connect` pins.
- **Reference and Value** go on one line just above the body, like in the stock library. When top pins are in the way, put them under the body or stack them in a free gap.

## Footprints and 3D models

- **Source of 3D models.** Don't draw models yourself. Take them from the manufacturer; otherwise from LCSC/EasyEDA, for the same part or for a part with the same land pattern and body.
- **Placement** is baked into the STEP file: the footprint keeps offset and rotation at 0 and scale at 1. Check the model against pads, holes and the board surface, including polarity.
- **Footprints without a model** are fine when there is a reason; record it as a KLC exception (see below).

## KLC exceptions

When a rule can't be met on purpose, add a private property to the symbol or footprint. Name it `KLC_<rule>` and put the reason in the value, e.g. `KLC_F9.3` = "Manufacturer publishes no 3D model". The checks honour it.

For symbols, `KLC_<rule>_<pin>` waives the rule for one pin only, e.g. `KLC_S4.4_5V`.

## Commits and releases

- **Commits** follow [Conventional Commits](https://www.conventionalcommits.org). [release-please](https://github.com/googleapis/release-please) builds the changelog and the version from them.
- **Breaking changes** are marked with `!` (`fix!:`, `refactor!:`). This covers anything that changes existing designs:
  - renamed symbols, footprints or datasheets;
  - moved pins, pads or anchors;
  - removed parts.
- **Releasing** is automatic: merging the release pull request publishes the GitHub release, builds the package and adds it to the [PCM index](https://github.com/sivakov512/kicad-pcm-index).
