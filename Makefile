# Library checks. `make check` runs everything; each target also runs alone.
#
#   make integrity   pins vs pads, 3D models, datasheets, unreferenced files
#   make klc         KiCad Library Convention (official kicad-library-utils)
#   make erc         ERC on a generated schematic with every symbol
#   make drc         DRC on a generated board with every footprint
#   make package     PCM package as a release builds it (TAG=v1.2.3, default main)
#
# KLC_WARNINGS=1 also lists KLC warnings. Reports are written to build/.

KICAD_CLI ?= kicad-cli
# kicad-library-utils needs Python 3.10+; uv provides one when the system is older.
PYTHON ?= $(shell command -v uv >/dev/null 2>&1 && echo "uv run --no-project --python 3.12 python" || echo python3)

# Official KLC checker and KiCad file parsers, pinned as a git submodule.
KLU_DIR := tools/kicad-library-utils

BUILD := build
KLC_FLAGS := $(if $(KLC_WARNINGS),--warnings)
TAG ?= main

.PHONY: check integrity klc klc-symbols klc-footprints erc drc package tools clean

# Run every listed target even when an earlier one fails.
run_all = status=0; for t in $(1); do $(MAKE) --no-print-directory $$t || status=1; done; exit $$status

check:
	@$(call run_all,integrity klc-symbols klc-footprints erc drc package)

integrity: tools
	@echo "==> integrity"
	@$(PYTHON) tools/check_library.py

klc:
	@$(call run_all,klc-symbols klc-footprints)

klc-symbols: tools
	@echo "==> KLC symbols"
	@$(PYTHON) tools/klc.py $(KLU_DIR) $(BUILD)/klc symbols $(KLC_FLAGS)

klc-footprints: tools
	@echo "==> KLC footprints"
	@$(PYTHON) tools/klc.py $(KLU_DIR) $(BUILD)/klc footprints $(KLC_FLAGS)

erc:
	@echo "==> ERC"
	@$(PYTHON) tools/gen_erc.py $(BUILD)/erc
	@$(KICAD_CLI) sch erc --severity-error --severity-warning --exit-code-violations \
		-o $(BUILD)/erc/erc.rpt $(BUILD)/erc/erc.kicad_sch > $(BUILD)/erc/cli.log 2>&1; \
		status=$$?; \
		grep -E '^\[|^    @' $(BUILD)/erc/erc.rpt; \
		grep -E '^Found' $(BUILD)/erc/cli.log || cat $(BUILD)/erc/cli.log; \
		exit $$status

drc:
	@echo "==> DRC"
	@$(PYTHON) tools/gen_drc.py $(BUILD)/drc
	@$(KICAD_CLI) pcb drc --severity-error --severity-warning --exit-code-violations \
		-o $(BUILD)/drc/drc.rpt $(BUILD)/drc/drc.kicad_pcb > $(BUILD)/drc/cli.log 2>&1; \
		status=$$?; \
		grep -E '^\[|^    @' $(BUILD)/drc/drc.rpt; \
		grep -E '^Found' $(BUILD)/drc/cli.log || cat $(BUILD)/drc/cli.log; \
		exit $$status

package:
	@echo "==> PCM package"
	@$(PYTHON) tools/pcm_package.py $(TAG) $(BUILD)/package/skc-$(TAG).zip

tools: $(KLU_DIR)/klc-check/check_symbol.py

$(KLU_DIR)/klc-check/check_symbol.py:
	git submodule update --init $(KLU_DIR)

clean:
	rm -rf $(BUILD)
