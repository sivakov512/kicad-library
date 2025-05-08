# KiCadX Libraries

A collection of custom libraries for KiCad 9+, including schematic symbols, footprints, 3D models, and reusable design blocks.

## Design blocks
Custom reusable schematic blocks grouped by function, located in [`design_blocks/`](design_blocks):

### Power supply
- **AC → 5V (HLK-5M05)** — quick prototyping solution using Hi-Link HLK-5M05 module
- **AC → 5V (LNK306P)** — standalone switching power supply for production-grade designs based on Power Integrations LNK306P
- **5V → 3.3V** — linear regulator circuit using LM1117 with filtering capacitors

## Symbols
Custom schematic symbols grouped into `.kicad_sym` libraries under [`symbols/`](symbols):

### ACDC Converters
- **KiCadX_ACDC_Converters.kicad_sym** — contains symbols for AC-DC converters:
  - **VIPER06** — high-voltage offline converter from STMicroelectronics
  - Additional AC-DC converters can be added in the future

### Microcontrollers
- **KiCadX_MCU_Espressif.kicad_sym** — contains symbols for Espressif microcontrollers:
  - **ESP32-H2** — low-power wireless microcontroller with Zigbee and Thread support

### Transformers
- **KiCadX_Transformers.kicad_sym** — contains symbols for transformers:
  - **Wurth 750370423** — E13 core transformer for isolated DC-DC converters from Würth Elektronik

## Footprints
Custom component footprints grouped into `.pretty` folders under [`footprints/`](footprints):

### ACDC Converters (SMD)
- **VIPER06** — SSO10 package for STMicroelectronics VIPER06 (`VIPER06_SSO10.kicad_mod`, with assigned 3D model `VIPER06_SSO10.step`)

### Antennas (SMD)
- **AH316M245001-T** — compact 2.4 GHz antenna from Taiyo Yuden (`AH316M245001_T.kicad_mod`, with assigned 3D model `AH316M245001_T.step`)

### Capacitors (THT)
- **Radial electrolytic capacitor** — 5mm diameter, 1.5mm pitch (`CP_Radial_D5.0mm_P1.50mm.kicad_mod`)

### Fuse Holders (THT)
- **PTF76** — 5x20mm fuse holder with 15mm lead spacing (`FuseHolder_THT_5x20mm_PTF76_RM15mm.kicad_mod`, with assigned 3D model `FuseHolder_THT_5x20mm_PTF76_RM15mm.step`)

### Fuses (SMD)
- **2410 (6125 Metric)** — 6.1x2.5mm SMD fuse (`Fuse_2410_6125Metric_6.1x2.5mm.kicad_mod`, with assigned 3D model `fuse_2410_6125metric_6.1x2.5mm.step`)

### Relays (THT)
- **Relpol RM51** — SPDT, 10A mechanical relay from Relpol (`Relay_SPDT_Relpol-RM51.kicad_mod`, with assigned 3D model `Relay_SPDT_Relpol-RM51.stp`)
- **OJ-SH-105HM** — SPST relay, 5V coil, from Jingis (`Relay_SPST_OJ_SH_105HM_000.kicad_mod`, with assigned 3D model `Relay_SPST_OJ_SH_105HM_000.step`)

### Thermistors (THT)
- **NTC10D-7** — 10Ω NTC thermistor, 7mm disc, 5mm pitch (`NTC10D_7_Disc_D7.0mm_P5.0mm.kicad_mod`, with assigned 3D model `NTC10D_7_Disc_D7.0mm_P5.0mm.step`)

### Transformers (THT)
- **Wurth 750370423** — E13 core transformer for isolated DC-DC converters from Würth Elektronik (`Wurth_750370423_THT_E13.kicad_mod`, with assigned 3D model `Wurth_750370423_THT_E13.step`)

### Microcontroller Packages (SMD)
- **Espressif TQFN-32** — TQFN-32 package with multiple variants, suitable for Espressif microcontrollers (e.g., ESP32-H2, ESP32-C6, etc.):
  - Compact: `TQFN_32_1EP_4x4mm_P0.4mm_EP2.4x2.4mm_Compact.kicad_mod`
  - Standard: `TQFN_32_1EP_4x4mm_P0.4mm_EP2.6x2.6mm_Standard.kicad_mod`
  - Extended: `TQFN_32_1EP_4x4mm_P0.4mm_EP2.8x2.8mm_Extended.kicad_mod`

## 3D models
Located in [`3dmodels/`](3dmodels):
- **VIPER06** — SSO10 package (`VIPER06_SSO10.step`)
- **Fuse holder** — PTF76, 5x20mm, 15mm lead spacing (`FuseHolder_THT_5x20mm_PTF76_RM15mm.step`)
- **Relay (SPDT)** — Relpol RM51, SPDT (`Relay_SPDT_Relpol-RM51.stp`)
- **Relay (SPST)** — OJ-SH-105HM, SPST (`Relay_SPST_OJ_SH_105HM_000.step`)
- **Espressif TQFN-32** — TQFN-32 package (`TQFN_32_1EP_4x4mm_P0.4mm.step`)
- **Antenna** — AH316M245001-T (`AH316M245001_T.step`)
- **Fuse (SMD)** — 2410 (6125 Metric) (`fuse_2410_6125metric_6.1x2.5mm.step`)
- **Thermistor** — NTC10D-7 (`NTC10D_7_Disc_D7.0mm_P5.0mm.step`)
- **Transformer** — Wurth 750370423 (`Wurth_750370423_THT_E13.step`)

## Datasheets
Datasheets for components are stored in [`datasheets/`](datasheets):
- **VIPER06** — High-voltage offline converter from STMicroelectronics ([`viper06.pdf`](datasheets/viper06.pdf))
- **Relays**:
  - **Relpol RM51** — SPDT, 10A relay from Relpol ([`relpol_rm51.pdf`](datasheets/relpol_rm51.pdf))
  - **OJ-SH-105HM** — SPST, 5V relay from Jingis ([`j-sh-105hm000.pdf`](datasheets/j-sh-105hm000.pdf))
- **Espressif Microcontrollers**:
  - **ESP32-H2** — Zigbee and Thread-enabled microcontroller ([`esp32-h2.pdf`](datasheets/esp32-h2.pdf))
- **Antenna**:
  - **AH316M245001-T** — 2.4 GHz antenna from Taiyo Yuden ([`taiyo_yuden_antennas.pdf`](datasheets/taiyo_yuden_antennas.pdf))
- **Transformer**:
  - **Wurth 750370423** — E13 core transformer for isolated DC-DC converters from Würth Elektronik ([`750370423.pdf`](datasheets/750370423.pdf))

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
