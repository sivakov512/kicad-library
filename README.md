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

**Legend:** ✅ available · ❌ not available · — not applicable

### Symbols (`SKC_*.kicad_sym`)

| Symbol                      | Footprint                                             | Datasheet |
| --------------------------- | ----------------------------------------------------- | --------- |
| **SKC_Converter_ACDC**      |                                                       |           |
| `VIPER06XS`                 | `STMicroelectronics_SSO-10_3.9x4.9mm_P1.00mm`         | ✅         |
| `VIPER06HS`                 | `STMicroelectronics_SSO-10_3.9x4.9mm_P1.00mm`         | ✅         |
| `VIPER06LS`                 | `STMicroelectronics_SSO-10_3.9x4.9mm_P1.00mm`         | ✅         |
| **SKC_DevKit**              |                                                       |           |
| `Waveshare_ESP32-C6-Zero`   | `Waveshare_ESP32-C6-Zero`                             | ✅         |
| **SKC_LED_SMD**             |                                                       |           |
| `SK6812-EC20`               | `LED_SK6812_EC20_2.0x2.0mm`                           | ✅         |
| **SKC_MCU_Espressif**       |                                                       |           |
| `ESP32-C3`                  | `QFN-32-1EP_5x5mm_P0.5mm_EP3.7x3.7mm`                 | ✅         |
| `ESP32-H2`                  | `VQFN-32-1EP_4x4mm_P0.4mm_EP2.8x2.8mm`                | ✅         |
| **SKC_Module_Cellular**     |                                                       |           |
| `A7672x`                    | `SIMCom_A7672x_A7670x`                                | ✅         |
| `A7670x`                    | `SIMCom_A7672x_A7670x`                                | ✅         |
| **SKC_Motor_Driver**        |                                                       |           |
| `DRV8316CRRGF`              | `Texas_RGF0040E_VQFN-40-1EP_5x7mm_P0.5mm_EP3.8x5.8mm` | ✅         |
| **SKC_Power_Monitor**       |                                                       |           |
| `MAX17048G`                 | `Maxim_TDFN-8-1EP_2x2mm_P0.5mm_EP0.9x1.3mm`           | ✅         |
| **SKC_Regulator_Linear**    |                                                       |           |
| `BD10KA5WF`                 | `ROHM_SOP-8_4.4x5mm_P1.27mm`                          | ✅         |
| `BD12KA5WF`                 | `ROHM_SOP-8_4.4x5mm_P1.27mm`                          | ✅         |
| `BD15KA5WF`                 | `ROHM_SOP-8_4.4x5mm_P1.27mm`                          | ✅         |
| `BD18KA5WF`                 | `ROHM_SOP-8_4.4x5mm_P1.27mm`                          | ✅         |
| `BD25KA5WF`                 | `ROHM_SOP-8_4.4x5mm_P1.27mm`                          | ✅         |
| `BD30KA5WF`                 | `ROHM_SOP-8_4.4x5mm_P1.27mm`                          | ✅         |
| `BD33KA5WF`                 | `ROHM_SOP-8_4.4x5mm_P1.27mm`                          | ✅         |
| **SKC_Regulator_Switching** |                                                       |           |
| `TPS564242DRL`              | `SOT-563`                                             | ✅         |
| `TPS564247DRL`              | `SOT-563`                                             | ✅         |
| **SKC_Switch_Power**        |                                                       |           |
| `TPS2121RUX`                | `Texas_RUX0012A_VQFN-HR-12_2x2.5mm_P0.5mm`            | ✅         |
| **SKC_Transformer**         |                                                       |           |
| `Wurth_750370423`           | `Transformer_Wurth_750370423`                         | ✅         |
| `ZMPT101B`                  | `Transformer_Zeming_ZMPT101B`                         | ✅         |

### Footprints (`SKC_*.pretty`)

| Footprint                                             | 3D Model | Datasheet |
| ----------------------------------------------------- | -------- | --------- |
| **SKC_Antenna_SMD**                                   |          |           |
| `Antenna_PCB_Espressif_2.4GHz_Left`                   | —        | ✅         |
| `Antenna_PCB_Espressif_2.4GHz_Right`                  | —        | ✅         |
| `Quectel_YC0010AA`                                    | ✅        | ✅         |
| `TaiyoYuden_AH316M245001-T`                           | ✅        | ✅         |
| **SKC_BatteryHolder_THT**                             |          |           |
| `BatteryHolder_Myoung_BH-18650-A5BJ001-2D`            | ✅        | ✅         |
| **SKC_Button_THT**                                    |          |           |
| `SW_PUSH_6mm_2Pins`                                   | ✅        | —         |
| **SKC_Buzzer_SMD**                                    |          |           |
| `MagneticBuzzer_KELIKING_KLJ-5020`                    | ✅        | ✅         |
| **SKC_Capacitor_THT**                                 |          |           |
| `CP_Radial_D6.0mm_P2.50mm`                            | ✅        | —         |
| **SKC_Connector_Audio**                               |          |           |
| `Jack_3.5mm_HRO_PJ-3126-5A_Horizontal`                | ✅        | ✅         |
| **SKC_Connector_Card**                                |          |           |
| `miniSIM_Molex_47553-2001`                            | ✅        | ✅         |
| **SKC_Connector_USB**                                 |          |           |
| `USB_C_Receptacle_Cvilux_CU3216SASBLR004-NH`          | ❌        | ✅         |
| **SKC_Converter_ACDC_SMD**                            |          |           |
| `STMicroelectronics_SSO-10_3.9x4.9mm_P1.00mm`         | ✅        | ✅         |
| **SKC_Crystal**                                       |          |           |
| `Crystal_SMD_1612-4Pin_1.6x1.2mm`                     | ✅        | —         |
| **SKC_DevKit**                                        |          |           |
| `Waveshare_ESP32-C6-Zero`                             | ✅        | ✅         |
| **SKC_Diode_THT**                                     |          |           |
| `D_SOD-64_P10.16mm_Horizontal`                        | ✅        | —         |
| **SKC_FuseHolder_THT**                                |          |           |
| `Fuseholder_Cylinder-5x20mm_PTF76_Horizontal`         | ✅        | —         |
| **SKC_Fuse_SMD**                                      |          |           |
| `Fuse_2410_6125Metric`                                | ✅        | —         |
| **SKC_Inductor_SMD**                                  |          |           |
| `L_MetalLions_MMPC0402`                               | ✅        | ✅         |
| **SKC_Inductor_THT**                                  |          |           |
| `Choke_EPCOS_B82720K`                                 | ✅        | ✅         |
| **SKC_LED_SMD**                                       |          |           |
| `LED_SK6812_EC20_2.0x2.0mm`                           | ✅        | ✅         |
| **SKC_Module_Cellular**                               |          |           |
| `SIMCom_A7672x_A7670x`                                | ✅        | ✅         |
| **SKC_Package_DFN**                                   |          |           |
| `Maxim_TDFN-8-1EP_2x2mm_P0.5mm_EP0.9x1.3mm`           | ✅        | ✅         |
| **SKC_Package_QFN**                                   |          |           |
| `Texas_RGF0040E_VQFN-40-1EP_5x7mm_P0.5mm_EP3.8x5.8mm` | ✅        | ✅         |
| `Texas_RUX0012A_VQFN-HR-12_2x2.5mm_P0.5mm`            | ✅        | ✅         |
| **SKC_Package_SO**                                    |          |           |
| `ROHM_SOP-8_4.4x5mm_P1.27mm`                          | ✅        | ✅         |
| **SKC_Relay_THT**                                     |          |           |
| `Relay_SPDT_Relpol_RM51`                              | ✅        | ✅         |
| `Relay_SPST_TE_OJ-SH-105HM`                           | ✅        | ✅         |
| **SKC_TestPoint**                                     |          |           |
| `TestPoint_2Pads_Pitch2.54mm_D1.4mm`                  | —        | —         |
| **SKC_Thermistor_THT**                                |          |           |
| `RT_Disc_D7mm_W2.8mm_P5mm`                            | ✅        | —         |
| **SKC_Transformer_THT**                               |          |           |
| `Transformer_Wurth_750370423`                         | ✅        | ✅         |
| `Transformer_Zeming_ZMPT101B`                         | ✅        | ✅         |

## Structure

```
.
├── 3dmodels/       # SKC_[Category].3dshapes/
├── datasheets/     # [CategoryName]/[Manufacturer]_[PartNumber].pdf
├── footprints/     # SKC_[Category].pretty/
└── symbols/        # SKC_[Category].kicad_sym
```

Naming follows the [KiCad Library Conventions (KLC)](https://klc.kicad.org) and the stock KiCad libraries: symbols are named by part number (e.g. `ESP32-C3`, `TPS2121RUX`), footprints by package or by manufacturer and part (e.g. `ROHM_SOP-8_4.4x5mm_P1.27mm`, `Relay_SPDT_Relpol_RM51`). Run `make check` to validate the libraries against KLC, ERC and DRC.

## Contribution

Contributions are welcome! Follow the repository structure above and [KLC naming conventions](https://klc.kicad.org).

## License

This project is licensed under the terms of the [MIT License](./LICENSE).
