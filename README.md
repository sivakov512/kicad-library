# Sivakov KiCad Component Library

Symbols, footprints and 3D models for parts that are missing from the stock KiCad libraries. Datasheets are linked from every symbol and footprint. The library follows the [KiCad Library Conventions (KLC)](https://klc.kicad.org) and is checked against them on every change.

Everything is prefixed with **SKC** (Sivakov KiCad Components): type `SKC` in a library browser to see only this library.

## Requirements

KiCad 10.0 or newer is required since version 3.0. Older KiCad installations are offered the last 2.x release by the Plugin and Content Manager.

## Installation

1. In KiCad open **Plugin and Content Manager** → **Manage**.
2. Click **Add Repository** and paste:
   ```
   https://raw.githubusercontent.com/sivakov512/kicad-pcm-index/main/repository.json
   ```
3. Select the repository, find **Sivakov KiCad Component Library** and click **Install**, then **Apply Pending Changes**.

Updates arrive through the same manager.

## Usage

- Libraries appear as `PCM_SKC_<Category>`, for example `PCM_SKC_Regulator_Linear`.
- Symbols come with their footprint assigned and footprint filters set.
- **Datasheet** on a symbol or footprint opens the PDF of the exact library version you have installed.

### Sharing a project with someone who doesn't have the library

- **Schematics and boards** keep their own copy of every symbol and footprint, so they open without the library.
- **3D models** are only referenced. Run **Collect And Embed 3D Models** in the PCB editor to store them inside the board file.
- **The recipient will keep adding these parts:** ask them to install the library as above, or copy the parts the project uses into a project library.

## Components

<!-- components:start -->

**Legend:** ✅ available · ❌ not available · — not applicable

### Symbols

| Symbol                      | Footprint                                             | Datasheet |
| --------------------------- | ----------------------------------------------------- | --------- |
| **SKC_Converter_ACDC**      |                                                       |           |
| `VIPER06XS`                 | `STMicroelectronics_SSO-10_3.9x4.9mm_P1.00mm`         | ✅         |
| `VIPER06HS`                 | `STMicroelectronics_SSO-10_3.9x4.9mm_P1.00mm`         | ✅         |
| `VIPER06LS`                 | `STMicroelectronics_SSO-10_3.9x4.9mm_P1.00mm`         | ✅         |
| **SKC_DevKit**              |                                                       |           |
| `Waveshare_ESP32-C6-Zero`   | `Waveshare_ESP32-C6-Zero`                             | ✅         |
| **SKC_Driver_LED**          |                                                       |           |
| `LP5009RUK`                 | `Texas_RUK0020B_WQFN-20-1EP_3x3mm_P0.4mm_EP1.7x1.7mm` | ✅         |
| `TPS92512HVDGQ`             | `HVSSOP-10-1EP_3x3mm_P0.5mm_EP1.83x1.89mm`            | ✅         |
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
| **SKC_RF_Module**           |                                                       |           |
| `MGM240PB22VNA3`            | `SiliconLabs_MGM240P`                                 | ✅         |
| **SKC_Regulator_Linear**    |                                                       |           |
| `BD10KA5WF`                 | `ROHM_SOP-8_4.4x5mm_P1.27mm`                          | ✅         |
| `TPS70933DBV`               | `SOT-23-5`                                            | ✅         |
| `BD12KA5WF`                 | `ROHM_SOP-8_4.4x5mm_P1.27mm`                          | ✅         |
| `BD15KA5WF`                 | `ROHM_SOP-8_4.4x5mm_P1.27mm`                          | ✅         |
| `BD18KA5WF`                 | `ROHM_SOP-8_4.4x5mm_P1.27mm`                          | ✅         |
| `BD25KA5WF`                 | `ROHM_SOP-8_4.4x5mm_P1.27mm`                          | ✅         |
| `BD30KA5WF`                 | `ROHM_SOP-8_4.4x5mm_P1.27mm`                          | ✅         |
| `BD33KA5WF`                 | `ROHM_SOP-8_4.4x5mm_P1.27mm`                          | ✅         |
| **SKC_Regulator_Switching** |                                                       |           |
| `TPS564242DRL`              | `SOT-563`                                             | ✅         |
| `TPS564247DRL`              | `SOT-563`                                             | ✅         |
| **SKC_Switch**              |                                                       |           |
| `SW_SP3T_SS13D07VG4`        | `SW_SP3T_SHOUHAN_SS13D07VG4`                          | ✅         |
| **SKC_Switch_Power**        |                                                       |           |
| `TPS2121RUX`                | `Texas_RUX0012A_VQFN-HR-12_2x2.5mm_P0.5mm`            | ✅         |
| **SKC_Transformer**         |                                                       |           |
| `Wurth_750370423`           | `Transformer_Wurth_750370423`                         | ✅         |
| `ZMPT101B`                  | `Transformer_Zeming_ZMPT101B`                         | ✅         |

### Footprints

| Footprint                                                    | 3D model | Datasheet |
| ------------------------------------------------------------ | -------- | --------- |
| **SKC_Antenna_SMD**                                          |          |           |
| `Antenna_PCB_Espressif_2.4GHz_Left`                          | —        | ✅         |
| `Antenna_PCB_Espressif_2.4GHz_Right`                         | —        | ✅         |
| `Quectel_YC0010AA`                                           | ✅        | ✅         |
| `TaiyoYuden_AH316M245001-T`                                  | ✅        | ✅         |
| **SKC_BatteryHolder_THT**                                    |          |           |
| `BatteryHolder_Myoung_BH-18650-A5BJ001-2D`                   | ✅        | ✅         |
| **SKC_Button_SMD**                                           |          |           |
| `SW_SPST_Omron_B3FS-40xxP`                                   | ✅        | ✅         |
| **SKC_Button_THT**                                           |          |           |
| `SW_PUSH_6mm_2Pins`                                          | ✅        | —         |
| `SW_SP3T_SHOUHAN_SS13D07VG4`                                 | ✅        | ✅         |
| **SKC_Buzzer_SMD**                                           |          |           |
| `Buzzer_INGHAi_GSD9605YB`                                    | ✅        | ✅         |
| `MagneticBuzzer_KELIKING_KLJ-5020`                           | ✅        | ✅         |
| **SKC_Capacitor_THT**                                        |          |           |
| `CP_Radial_D6.0mm_P2.50mm`                                   | ✅        | —         |
| **SKC_Connector_Audio**                                      |          |           |
| `Jack_3.5mm_BOOMELE_PJ-307C_Horizontal`                      | ✅        | ✅         |
| `Jack_3.5mm_HRO_PJ-3126-5A_Horizontal`                       | ✅        | ✅         |
| **SKC_Connector_Card**                                       |          |           |
| `miniSIM_Molex_47553-2001`                                   | ✅        | ✅         |
| **SKC_Connector_FFC-FPC**                                    |          |           |
| `GUOCONN_1.0K-FX-10PWB-RL_1x10-1MP_P1.0mm_Horizontal`        | ✅        | ✅         |
| `GUOCONN_1.0K-N-10PB-RXW_1x10-1MP_P1.0mm_Vertical`           | ✅        | ✅         |
| **SKC_Connector_USB**                                        |          |           |
| `USB_C_Receptacle_Cvilux_CU3216SASBLR004-NH`                 | ❌        | ✅         |
| `USB_C_Receptacle_SHOUHAN_TYPE-C-14PLC-H10.0_Vertical`       | ✅        | ✅         |
| **SKC_Converter_ACDC_SMD**                                   |          |           |
| `STMicroelectronics_SSO-10_3.9x4.9mm_P1.00mm`                | ✅        | ✅         |
| **SKC_Crystal**                                              |          |           |
| `Crystal_SMD_1612-4Pin_1.6x1.2mm`                            | ✅        | —         |
| **SKC_DevKit**                                               |          |           |
| `Waveshare_ESP32-C6-Zero`                                    | ✅        | ✅         |
| **SKC_Diode_THT**                                            |          |           |
| `D_SOD-64_P10.16mm_Horizontal`                               | ✅        | —         |
| **SKC_FuseHolder_THT**                                       |          |           |
| `Fuseholder_Cylinder-5x20mm_PTF76_Horizontal`                | ✅        | —         |
| **SKC_Fuse_SMD**                                             |          |           |
| `Fuse_2410_6125Metric`                                       | ✅        | —         |
| **SKC_Inductor_SMD**                                         |          |           |
| `L_MetalLions_MMPC0402`                                      | ✅        | ✅         |
| **SKC_Inductor_THT**                                         |          |           |
| `Choke_EPCOS_B82720K`                                        | ✅        | ✅         |
| **SKC_LED_SMD**                                              |          |           |
| `LED_SK6812_EC20_2.0x2.0mm`                                  | ✅        | ✅         |
| `LED_XINGLIGHT_XL-2835WWC-02`                                | ✅        | ✅         |
| **SKC_Module_Cellular**                                      |          |           |
| `SIMCom_A7672x_A7670x`                                       | ✅        | ✅         |
| **SKC_Package_DFN**                                          |          |           |
| `Maxim_TDFN-8-1EP_2x2mm_P0.5mm_EP0.9x1.3mm`                  | ✅        | ✅         |
| **SKC_Package_QFN**                                          |          |           |
| `Texas_RGF0040E_VQFN-40-1EP_5x7mm_P0.5mm_EP3.8x5.8mm`        | ✅        | ✅         |
| `Texas_RUX0012A_VQFN-HR-12_2x2.5mm_P0.5mm`                   | ✅        | ✅         |
| **SKC_Package_SO**                                           |          |           |
| `ROHM_SOP-8_4.4x5mm_P1.27mm`                                 | ✅        | ✅         |
| **SKC_RF_Module**                                            |          |           |
| `SiliconLabs_MGM240P`                                        | ✅        | ✅         |
| **SKC_Relay_THT**                                            |          |           |
| `Relay_SPDT_Relpol_RM51`                                     | ✅        | ✅         |
| `Relay_SPST_TE_OJ-SH-105HM`                                  | ✅        | ✅         |
| **SKC_TerminalBlock**                                        |          |           |
| `TerminalBlock_DORABO_DB125-2.54-2P_1x02_P2.54mm_Horizontal` | ✅        | ✅         |
| **SKC_TestPoint**                                            |          |           |
| `TestPoint_2Pads_Pitch2.54mm_D1.4mm`                         | —        | —         |
| **SKC_Thermistor_THT**                                       |          |           |
| `RT_Disc_D7mm_W2.8mm_P5mm`                                   | ✅        | —         |
| **SKC_Transformer_THT**                                      |          |           |
| `Transformer_Wurth_750370423`                                | ✅        | ✅         |
| `Transformer_Zeming_ZMPT101B`                                | ✅        | ✅         |

<!-- components:end -->

## Contributing

Contributions are welcome. See [CONTRIBUTING.md](./CONTRIBUTING.md) for the rules and the development setup.

## License

- **Library (symbols, footprints and tooling):** [MIT License](./LICENSE).
- **Datasheets:** belong to their manufacturers and are redistributed for convenience.
- **3D models:** come from the part manufacturers or from LCSC/EasyEDA and remain subject to their terms.
