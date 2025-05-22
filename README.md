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
   https://raw.githubusercontent.com/sivakov512/kicad-pcm-index/master/repository.json
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
| TaiyoYuden AH316M245001-T (2.4GHz) | 〰️ | ✅ | ✅ | ✅ |
| PCB Antenna Espressif 2.4GHz (left/right) | 〰️ | ✅ | 〰️ | 〰️ |
| **Capacitors** |
| Radial Electrolytic (THT, Various sizes) | 〰️ | ✅ | ❌ | ❌ |
| **Fuses and Fuse Holders** |
| PTF76 (5x20mm, 15mm lead spacing) | 〰️ | ✅ | ✅ | ❌ |
| 2410 (6125 Metric) SMD Fuse | 〰️ | ✅ | ✅ | ❌ |
| **Inductors** |
| TDK B82720K (THT, 13x9.5mm) | 〰️ | ✅ | ❌ | ✅ |
| **Microcontrollers** |
| ESP32-H2 (QFN-32) | ✅ | ✅ | ✅ | ✅ |
| **Relays** |
| Relpol RM51 (SPDT, 10A) | 〰️ | ✅ | ✅ | ✅ |
| OJ SH-105HM (SPST, 5V coil) | 〰️ | ✅ | ✅ | ✅ |
| **Thermistors** |
| NTC10D-7 (10Ω NTC, 7mm disc) | 〰️ | ✅ | ✅ | ❌ |
| **Transformers** |
| Wurth 750370423 (E13 core) | ✅ | ✅ | ✅ | ✅ |
| **PCB Design Elements** |
| Net Ties (Various sizes) | 〰️ | ✅ | 〰️ | 〰️ |


## Contribution

Contributions are welcome! Please follow the naming conventions outlined above and in [CONTRIBUTING.md](./CONTRIBUTING.md).

## License

This project is licensed under the terms of the [MIT License](./LICENSE).
