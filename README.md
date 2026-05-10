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

**Legend:** ✅ available · ❌ not available · —  not applicable

### Symbols (`SKC_*`.kicad_sym)

| Symbol                     | Datasheet |
| -------------------------- | --------- |
| **Converter ACDC**         |           |
| STMicroelectronics VIPER06 | ✅        |
| **DevKit**                 |           |
| WaveShare ESP32-C6-Zero    | ✅        |
| **LED SMD**                |           |
| Worldsemi SK6812-EC20      | ✅        |
| **MCU Espressif**          |           |
| Espressif ESP32-C3         | ✅        |
| Espressif ESP32-H2         | ✅        |
| **Regulator Linear**       |           |
| Rohm BDXXKA5WF             | ✅        |
| **Switch Power**           |           |
| Texas TPS2121              | ✅        |
| **Transformer**            |           |
| Wurth 750370423            | ✅        |

### Footprints (`SKC_*`.pretty)

| Footprint                                  | 3D Model | Datasheet |
| ------------------------------------------ | -------- | --------- |
| **Antenna SMD**                            |          |           |
| TaiyoYuden AH316M245001-T                  | ✅       | ✅        |
| Quectel YC0010AA                           | ✅       | ✅        |
| PCB Antenna Espressif 2.4GHz Left          | —        | —         |
| PCB Antenna Espressif 2.4GHz Right         | —        | —         |
| **Button THT**                             |          |           |
| SW Push SPST 6mm                           | ❌       | —         |
| **Capacitor THT**                          |          |           |
| CP Radial D5.0mm P1.50mm                   | —        | ❌        |
| CP Radial D6.0mm P2.50mm                   | —        | ❌        |
| CP Radial D16.0mm P10.0mm                  | —        | ❌        |
| **Connector PinHeader 2.54mm**             |          |           |
| PinHeader 1x02 Vertical NoSilk             | —        | —         |
| PinHeader 1x04 Vertical NoSilk             | —        | —         |
| PinHeader 1x06 Vertical NoSilk             | —        | —         |
| PinHeader 1x07 Vertical NoSilk             | —        | —         |
| **Connector USB**                          |          |           |
| Cvilux CU3216SASBLR004-NH (USB-C SMD)      | ❌       | ✅        |
| NoName USB-C Receptacle (Hybrid SMD/THT)   | —        | ❌        |
| **Converter ACDC SMD**                     |          |           |
| STMicroelectronics VIPER06 SSO-10          | ✅       | ✅        |
| **Crystal**                                |          |           |
| Crystal SMD 1612 4-Pin 1.6x1.2mm           | ✅       | —         |
| **DevKit**                                 |          |           |
| WaveShare ESP32-C6-Zero                    | ✅       | ✅        |
| **Diode THT**                              |          |           |
| SOD-64                                     | ❌       | ❌        |
| **FuseHolder THT**                         |          |           |
| PTF76 Cartridge 5x20mm 15mm pitch          | ✅       | ❌        |
| **Fuse SMD**                               |          |           |
| Fuse 2410 6125Metric 6.1x2.5mm             | ✅       | ❌        |
| **Inductor THT**                           |          |           |
| TDK B82720K Vertical 13x9.5mm              | ❌       | ✅        |
| **LED SMD**                                |          |           |
| Worldsemi SK6812-EC20 2.0x2.0mm            | ❌       | ✅        |
| **NetTie**                                 |          |           |
| NetTie 2-pad D0.5mm P4.0mm                 | —        | —         |
| **Package QFN**                            |          |           |
| TQFN-32 4x4mm P0.4mm EP2.4x2.4mm Compact   | ✅       | —         |
| TQFN-32 4x4mm P0.4mm EP2.6x2.6mm Standard  | ✅       | —         |
| TQFN-32 4x4mm P0.4mm EP2.8x2.8mm Extended  | ✅       | —         |
| VFQFN-32 5x5mm P0.5mm EP3.2x3.2mm Compact  | ✅       | —         |
| Texas VQFN-HR-12 2x2.5mm P0.5mm            | ✅       | —         |
| **Package SO**                             |          |           |
| SOP-8 4.4x5.35mm P1.27mm                   | —        | —         |
| **Relay THT**                              |          |           |
| Relpol RM51 SPDT                           | ✅       | ✅        |
| TE Connectivity OJ-SH-105HM SPST           | ✅       | ✅        |
| **TestPoint**                              |          |           |
| TestPoint 2-Pad RM2.54mm D1.4mm            | —        | —         |
| **Thermistor THT**                         |          |           |
| NTC10D-7 Disc D7.0mm P5.0mm                | ✅       | ❌        |
| **Transformer THT**                        |          |           |
| Wurth 750370423 THT E13                    | ✅       | ✅        |


## Structure

```
.
├── 3dmodels/       # SKC_[Category].3dshapes/
├── datasheets/     # [CategoryName]/[Manufacturer]_[PartNumber].pdf
├── footprints/     # SKC_[Category].pretty/
└── symbols/        # SKC_[Category].kicad_sym
```

Naming follows [KiCad Library Conventions (KLC) v3.0](https://klc.kicad.org). All manufacturer-specific symbols and footprints include the vendor prefix (e.g. `Espressif_ESP32-C3`, `STMicroelectronics_VIPER06_SSO-10`).

## Contribution

Contributions are welcome! Follow the repository structure above and [KLC naming conventions](https://klc.kicad.org).

## License

This project is licensed under the terms of the [MIT License](./LICENSE).
