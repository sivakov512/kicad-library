# KiCad Component Library

A comprehensive collection of custom libraries for KiCad, including schematic symbols, footprints, 3D models, and datasheets. Organized by component categories and mounting types for easy navigation.

All library components are prefixed with **SKC** (Sivakov KiCad Components) to make them easily searchable in KiCad. When looking for symbols, footprints, or 3D models from this library, simply type "SKC" in the KiCad search field to quickly filter all components from this collection.

## Installation

### Using Plugin and Content Manager (Recommended)

The easiest way to install this library is through KiCad's Plugin and Content Manager:

1. Open KiCad
2. Go to **Plugin and Content Manager** → **Manage**
3. Click **Add Repository**
4. Add this repository URL:
   ```
   https://raw.githubusercontent.com/sivakov512/kicad-pcm-index/main/repository.json
   ```
5. Click **OK**
6. Find "Sivakov KiCad Component Library" in the list and click **Install**
7. Restart KiCad to ensure all components are properly loaded

## Component List

The table below shows the available components in the library and indicates which resources are available for each component.

**Legend:**
- ✅ — Available in the library
- ❌ — Not available
- 〰️ — Not applicable or available in standard KiCad libraries

| Component | Symbol | Footprint | 3D Model | Datasheet |
|-----------|:------:|:---------:|:--------:|:---------:|
| **AC-DC Converters** |
| STMicroelectronics VIPER06 (SSO10) | ✅ | ✅ | ✅ | ✅ |
| **Antennas** |
| TaiyoYuden AH316M245001-T chip (2.4GHz) | 〰️ | ✅ | ✅ | ✅ |
| Quectel TaiyoYuden chip (2.4GHz) | 〰️ | ✅ | ✅ | ✅ |
| PCB Antenna Espressif 2.4GHz (left/right) | 〰️ | ✅ | 〰️ | 〰️ |
| **Capacitors** |
| Radial Electrolytic (THT, D5.0mm/P1.5mm) | 〰️ | ✅ | ✅ | ❌ |
| Radial Electrolytic (THT, D6.0mm/P2.5mm) | 〰️ | ✅ | ✅ | ❌ |
| Radial Electrolytic (THT, D16.0mm/P10.0mm) | 〰️ | ✅ | ✅ | ❌ |
| **Fuses and Fuse Holders** |
| PTF76 (5x20mm, 15mm lead spacing) | 〰️ | ✅ | ✅ | ❌ |
| 2410 (6125 Metric) SMD Fuse | 〰️ | ✅ | ✅ | ❌ |
| **Inductors** |
| TDK B82720K (THT, 13x9.5mm) | 〰️ | ✅ | ❌ | ✅ |
| **Microcontrollers** |
| ESP32-H2 | ✅ | 〰️ | 〰️ | ✅ |
| ESP32-C3 | ✅ | 〰️ | ✅ | ✅ |
| **Development Boards** |
| ESP32-C6-Zero Waveshare | ✅ | ✅ | ✅ | ✅ |
| **Packages** |
| QFN-32 (4x4mm, P0.4mm, Compact EP) | 〰️ | ✅ | ✅ | 〰️ |
| QFN-32 (4x4mm, P0.4mm, Standard EP) | 〰️ | ✅ | ✅ | 〰️ |
| QFN-32 (4x4mm, P0.4mm, Extended EP) | 〰️ | ✅ | ✅ | 〰️ |
| VFQFN-32 (5x5mm, P0.5mm, Compact EP) | 〰️ | ✅ | ✅ | 〰️ |
| **Relays** |
| Relpol RM51 (SPDT, 10A) | 〰️ | ✅ | ✅ | ✅ |
| OJ SH-105HM (SPST, 5V coil) | 〰️ | ✅ | ✅ | ✅ |
| **Thermistors** |
| NTC10D-7 (10Ω NTC, 7mm disc) | 〰️ | ✅ | ✅ | ❌ |
| **Transformers** |
| Wurth 750370423 (E13 core) | ✅ | ✅ | ✅ | ✅ |
| **Connectors** |
| Pin Headers 1x02, 1x04, 1x06, 1x07 (2.54mm, NoSilk) | 〰️ | ✅ | 〰️ | 〰️ |
| Cvilux CU3216SASBLR004-NH (USB Type-C Receptacle, SMD) | 〰️ | ✅ | ❌ | ✅ |
| **PCB Design Elements** |
| Net Ties (Various sizes) | 〰️ | ✅ | 〰️ | 〰️ |
| **Crystals** |
| Crystal SMD 1612 (4-Pin, 1.6x1.2mm) | 〰️ | ✅ | ✅ | 〰️ |
| **Diodes** |
| SOD-64 (MELF DO-213AB, THT) | 〰️ | ✅ | ❌ | ❌ |
| **Buttons** |
| SW_Push_SPST_6mm (Tactile button) | 〰️ | ✅ | ❌ | 〰️ |
| **Test Points** |
| TestPoint_2Pads_RM2.54mm_D1.4 | 〰️ | ✅ | 〰️ | 〰️ |


## Contribution

Contributions are welcome! Please follow the naming conventions outlined above and in [CONTRIBUTING.md](./CONTRIBUTING.md).

## License

This project is licensed under the terms of the [MIT License](./LICENSE).
