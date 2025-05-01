# KiCadX Libraries

A collection of custom libraries for KiCad 9+, including schematic symbols, footprints, 3D models, and reusable design blocks.

## Design blocks
Custom reusable schematic blocks grouped by function, located in [`design_blocks/`](design_blocks):

### Power supply
- **AC → 5V (HLK-5M05)** — quick prototyping solution
- **AC → 5V (LNK306P)** — standalone switching power supply for production-grade designs
- **5V → 3.3V** using LM1117 with filtering

## Symbols
Custom schematic symbols grouped into `.kicad_sym` libraries under [`symbols/`](symbols):

### ACDC Converters
- **KiCadX_ACDC_Converters.kicad_sym** — contains symbols for all AC-DC converters:
  - **VIPER06** — high-voltage converter for offline power supplies
  - Additional AC-DC converters can be added in the future

## Footprints
Custom component footprints grouped into `.pretty` folders under [`footprints/`](footprints):

### ACDC Converters (SMD)
- **VIPER06** — SSO10 package (`VIPER06_SSO10.kicad_mod`, with assigned 3D model `VIPER06_SSO10.step`)

### Capacitors (THT)
- Radial electrolytic capacitor — 5mm diameter, 1.5mm pitch (`CP_Radial_D5.0mm_P1.50mm.kicad_mod`)

### Fuse Holders (THT)
- 5x20mm fuse holder — PTF76, 15mm lead spacing (`FuseHolder_THT_5x20mm_PTF76_RM15mm.kicad_mod`)

### Relays (THT)
- Relpol RM51 — SPDT, 10A mechanical relay (`Relay_SPDT_Relpol-RM51.kicad_mod`, with assigned 3D model `Relay_SPDT_Relpol-RM51.stp`)

## 3D models
Located in [`3dmodels/`](3dmodels):
- **VIPER06** — SSO10 package (`VIPER06_SSO10.step`)
- **Fuse holder** — PTF76, 5x20mm, 15mm lead spacing (`FuseHolder_THT_5x20mm_PTF76_RM15mm.step`)
- **Relay** — Relpol RM51, SPDT (`Relay_SPDT_Relpol-RM51.stp`)

## Datasheets
Datasheets for components are stored in [`datasheets/`](datasheets):
- **VIPER06** — [`viper06.pdf`](datasheets/viper06.pdf)
- **Relpol RM51** — [`relpol_rm51.pdf`](datasheets/relpol_rm51.pdf)

## Installation

1. Clone the repository to your local system:
   ```bash
   git clone git@github.com:sivakov512/kicadx-libs.git
   ```

2. In KiCad, open **Preferences → Configure Paths** and add a new environment variable:
   - **Name:** `KICADX_LIBS`
   - **Path:** absolute path to the cloned repository

3. Add the needed libraries to KiCad. Depending on the type of library, use one of the following menus:
   - **Preferences → Manage Symbol Libraries** for schematic symbols
   - **Preferences → Manage Footprint Libraries** for footprints
   - **Preferences → Manage Design Block Libraries** for reusable design blocks

   Add only the libraries you need by specifying their paths. Use the `${KICADX_LIBS}` environment variable as a prefix. For example:
   - To add the AC-DC converter symbols: `${KICADX_LIBS}/symbols/KiCadX_ACDC_Converters.kicad_sym`
   - To add the VIPER06 footprint: `${KICADX_LIBS}/footprints/KiCadX_ACDC_Converters_SMD.pretty`
   - To add the power supply design blocks: `${KICADX_LIBS}/design_blocks/power.kicad_blocks/`

## Contribution

Contributions are welcome! Please follow the naming conventions outlined in [CONTRIBUTING.md](./CONTRIBUTING.md).

## License

This project is licensed under the terms of the [MIT License](./LICENSE).
