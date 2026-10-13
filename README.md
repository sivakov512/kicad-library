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

- [Antenna](#antenna) — 4
- [BatteryHolder](#batteryholder) — 1
- [Button](#button) — 2
- [Buzzer](#buzzer) — 2
- [Capacitor](#capacitor) — 1
- [Connector Audio](#connector-audio) — 2
- [Connector Card](#connector-card) — 1
- [Connector FFC-FPC](#connector-ffc-fpc) — 2
- [Connector USB](#connector-usb) — 2
- [Converter ACDC](#converter-acdc) — 1
- [Crystal](#crystal) — 1
- [DevKit](#devkit) — 1
- [Diode](#diode) — 1
- [Driver LED](#driver-led) — 2
- [Fuse](#fuse) — 1
- [FuseHolder](#fuseholder) — 1
- [Inductor](#inductor) — 2
- [LED](#led) — 2
- [MCU Espressif](#mcu-espressif) — 2
- [Module Cellular](#module-cellular) — 1
- [Motor Driver](#motor-driver) — 1
- [Power Monitor](#power-monitor) — 1
- [RF Module](#rf-module) — 1
- [Regulator Linear](#regulator-linear) — 2
- [Regulator Switching](#regulator-switching) — 1
- [Relay](#relay) — 2
- [Switch](#switch) — 1
- [Switch Power](#switch-power) — 1
- [TerminalBlock](#terminalblock) — 1
- [TestPoint](#testpoint) — 1
- [Thermistor](#thermistor) — 1
- [Transformer](#transformer) — 2

Legend:

- **Symbol** `KiCad`: no own symbol, use a stock KiCad one
- **Footprint** `(KiCad)`: stock KiCad footprint
- **3D model** ✅ included · ❌ not available · — copper only, no body · KiCad: stock model

### Antenna

| Part | Description | Symbol | Footprint | 3D model | Datasheet |
| --- | --- | --- | --- | --- | --- |
| Antenna_PCB_Espressif_2.4GHz_Left | PCB trace antenna for 2.4 GHz, as used on Espressif DevKitC and ESP32-MINI modules, left direction | KiCad | `Antenna_PCB_Espressif_2.4GHz_Left` | — | [link](https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32c3/pcb-layout-design.html) |
| Antenna_PCB_Espressif_2.4GHz_Right | PCB trace antenna for 2.4 GHz, as used on Espressif DevKitC and ESP32-MINI modules, right direction | KiCad | `Antenna_PCB_Espressif_2.4GHz_Right` | — | [link](https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32c3/pcb-layout-design.html) |
| Quectel YC0010AA | Quectel YC0010AA chip antenna, 2.4Ghz, 5.2x2.0 mm | KiCad | `Quectel_YC0010AA` | ✅ | [PDF](datasheets/Antenna_SMD/Quectel_YC0010AA.pdf) |
| TaiyoYuden AH316M245001-T | Taiyo Yuden AH316M245001-T chip antenna, 2.4 GHz, 3.2×1.6 mm, SMT | KiCad | `TaiyoYuden_AH316M245001-T` | ✅ | [PDF](datasheets/Antenna_SMD/TaiyoYuden_AH316M245001-T.pdf) |

### BatteryHolder

| Part | Description | Symbol | Footprint | 3D model | Datasheet |
| --- | --- | --- | --- | --- | --- |
| Myoung BH-18650-A5BJ001-2D | Battery holder, BH-18650-A5BJ001-2D, battery type 1x18650 | KiCad | `BatteryHolder_Myoung_BH-18650-A5BJ001-2D` | ✅ | [PDF](datasheets/BatteryHolder_THT/Myoung_BH-18650-A5BJ001-2D.pdf) |

### Button

| Part | Description | Symbol | Footprint | 3D model | Datasheet |
| --- | --- | --- | --- | --- | --- |
| Omron B3FS-40xxP | Omron B3FS-4000 series SMD tactile switch, 12x12mm, land pattern per datasheet | KiCad | `SW_SPST_Omron_B3FS-40xxP` | ✅ | [PDF](datasheets/Button_SMD/Omron_B3FS-40xxP.pdf) |
| SW_PUSH_6mm_2Pins | Generic 6mm SW tactile push button SPST | KiCad | `SW_PUSH_6mm_2Pins` | ✅ | — |

### Buzzer

| Part | Description | Symbol | Footprint | 3D model | Datasheet |
| --- | --- | --- | --- | --- | --- |
| INGHAi GSD9605YB | INGHAi GSD9605YB SMD piezo buzzer, 9.6x9.6x5.0mm | KiCad | `Buzzer_INGHAi_GSD9605YB` | ✅ | [PDF](datasheets/Buzzer_SMD/INGHAi_GSD9605YB.pdf) |
| KELIKING KLJ-5020 | Magnetic buzzer, KELIKING KLJ-5020, 5.0x5.0x2.0mm, SMD, land pattern per datasheet | KiCad | `MagneticBuzzer_KELIKING_KLJ-5020` | ✅ | [PDF](datasheets/Buzzer_SMD/KELIKING_KLJ-5020.pdf) |

### Capacitor

| Part | Description | Symbol | Footprint | 3D model | Datasheet |
| --- | --- | --- | --- | --- | --- |
| CP_Radial_D6.0mm_P2.50mm | CP, Radial series, Radial, pin pitch=2.50mm, diameter=6mm, Electrolytic Capacitor | KiCad | `CP_Radial_D6.0mm_P2.50mm` | ✅ | — |

### Connector Audio

| Part | Description | Symbol | Footprint | 3D model | Datasheet |
| --- | --- | --- | --- | --- | --- |
| BOOMELE PJ-307C | 3.5mm stereo audio jack, switched tip and ring, horizontal, BOOMELE PJ-307C | KiCad | `Jack_3.5mm_BOOMELE_PJ-307C_Horizontal` | ✅ | [PDF](datasheets/Connector_Audio/BOOMELE_PJ-307C.pdf) |
| HRO PJ-3126-5A | TRS 3.5mm, horizontal, through-hole | KiCad | `Jack_3.5mm_HRO_PJ-3126-5A_Horizontal` | ✅ | [PDF](datasheets/Connector_Audio/HRO_PJ-3126-5A.pdf) |

### Connector Card

| Part | Description | Symbol | Footprint | 3D model | Datasheet |
| --- | --- | --- | --- | --- | --- |
| Molex 47553-2001 | miniSIM slot MOLEX 475532001 8pin | KiCad | `miniSIM_Molex_47553-2001` | ✅ | [PDF](datasheets/Connector_Card/Molex_47553-2001.pdf) |

### Connector FFC-FPC

| Part | Description | Symbol | Footprint | 3D model | Datasheet |
| --- | --- | --- | --- | --- | --- |
| GUOCONN 1.0K-FX-10PWB-RL | GUOCONN FFC/FPC connector, horizontal, bottom contacts, 10 contacts, 1.0mm pitch, 3D model of the pin-compatible TE 1-84952-0 | KiCad | `GUOCONN_1.0K-FX-10PWB-RL_1x10-1MP_P1.0mm_Horizontal` | ✅ | [PDF](datasheets/Connector_FFC-FPC/GUOCONN_1.0K-FX-10PWB-RL.pdf) |
| GUOCONN 1.0K-N-10PB-RXW | GUOCONN FFC/FPC connector, vertical, 10 contacts, 1.0mm pitch, 4.5mm high | KiCad | `GUOCONN_1.0K-N-10PB-RXW_1x10-1MP_P1.0mm_Vertical` | ✅ | [PDF](datasheets/Connector_FFC-FPC/GUOCONN_1.0K-N-10PB-RXW.pdf) |

### Connector USB

| Part | Description | Symbol | Footprint | 3D model | Datasheet |
| --- | --- | --- | --- | --- | --- |
| Cvilux CU3216SASBLR004-NH | Cvilux CU3216SASBLR004-NH USB 2.0 Type-C Receptacle 16 ways | KiCad | `USB_C_Receptacle_Cvilux_CU3216SASBLR004-NH` | ❌ | [PDF](datasheets/Connector_USB/Cvilux_CU3216SASBLR004-NH.pdf) |
| SHOUHAN TYPE-C-14PLC-H10.0 | USB 2.0 Type-C receptacle, SHOU HAN TYPE-C 14PLC-H10.0, 14 pins, through-hole, vertical, 10mm high | KiCad | `USB_C_Receptacle_SHOUHAN_TYPE-C-14PLC-H10.0_Vertical` | ✅ | [PDF](datasheets/Connector_USB/SHOUHAN_TYPE-C-14PLC-H10.0.pdf) |

### Converter ACDC

| Part | Description | Symbol | Footprint | 3D model | Datasheet |
| --- | --- | --- | --- | --- | --- |
| STMicroelectronics VIPER06XS … VIPER06LS | Offline high-voltage converter, 800V avalanche rugged power section, PWM controller, 30kHz with frequency jittering, direct feedback, SSO-10 | `VIPER06XS` … `VIPER06LS` (3) | `STMicroelectronics_SSO-10_3.9x4.9mm_P1.00mm` | ✅ | [PDF](datasheets/Converter_ACDC/STMicroelectronics_VIPER06.pdf) |

### Crystal

| Part | Description | Symbol | Footprint | 3D model | Datasheet |
| --- | --- | --- | --- | --- | --- |
| Crystal_SMD_1612-4Pin_1.6x1.2mm | SMD1612/4, Crystal, 1.6x1.2mm package, SMD | KiCad | `Crystal_SMD_1612-4Pin_1.6x1.2mm` | ✅ | — |

### DevKit

| Part | Description | Symbol | Footprint | 3D model | Datasheet |
| --- | --- | --- | --- | --- | --- |
| Waveshare ESP32-C6-Zero | Development board, ESP32-C6 Wi-Fi 6 BLE 5 Zigbee Thread module, castellated and through-hole pins | `Waveshare_ESP32-C6-Zero` | `Waveshare_ESP32-C6-Zero` | ✅ | [link](https://www.waveshare.com/wiki/ESP32-C6-Zero) |

### Diode

| Part | Description | Symbol | Footprint | 3D model | Datasheet |
| --- | --- | --- | --- | --- | --- |
| D_SOD-64_P10.16mm_Horizontal | SOD-64 MELF DO-213AB diode | KiCad | `D_SOD-64_P10.16mm_Horizontal` | ✅ | — |

### Driver LED

| Part | Description | Symbol | Footprint | 3D model | Datasheet |
| --- | --- | --- | --- | --- | --- |
| Texas LP5009RUK | 9-channel 12-bit PWM I2C RGB LED driver, ultra-low quiescent current, WQFN-20 | `LP5009RUK` | `Texas_RUK0020B_WQFN-20-1EP_3x3mm_P0.4mm_EP1.7x1.7mm` (KiCad) | KiCad | [PDF](datasheets/Driver_LED/Texas_LP5009.pdf) |
| Texas TPS92512HVDGQ | 2.5A buck LED driver with integrated MOSFET and analog current adjust, 4.5-60V input, HVSSOP-10 | `TPS92512HVDGQ` | `HVSSOP-10-1EP_3x3mm_P0.5mm_EP1.83x1.89mm` (KiCad) | KiCad | [PDF](datasheets/Driver_LED/Texas_TPS92512.pdf) |

### Fuse

| Part | Description | Symbol | Footprint | 3D model | Datasheet |
| --- | --- | --- | --- | --- | --- |
| Fuse_2410_6125Metric | SMD fuse, 2410 (6125 Metric), 6.1×2.5 mm body, IPC 7351 nominal | KiCad | `Fuse_2410_6125Metric` | ✅ | — |

### FuseHolder

| Part | Description | Symbol | Footprint | 3D model | Datasheet |
| --- | --- | --- | --- | --- | --- |
| Fuseholder_Cylinder-5x20mm_PTF76_Horizontal | Fuse holder, THT, 5x20mm cartridge, PTF76, 15mm pitch | KiCad | `Fuseholder_Cylinder-5x20mm_PTF76_Horizontal` | ✅ | — |

### Inductor

| Part | Description | Symbol | Footprint | 3D model | Datasheet |
| --- | --- | --- | --- | --- | --- |
| EPCOS B82720K | THT B82720K common mode choke, 4-pin, vertical, 13×9.5 mm body, 10x7.5mm pitch | KiCad | `Choke_EPCOS_B82720K` | ✅ | [PDF](datasheets/Inductor_THT/EPCOS_B82720K.pdf) |
| MetalLions MMPC0402 | Choke, SMD, 4.5x4mm | KiCad | `L_MetalLions_MMPC0402` | ✅ | [PDF](datasheets/Inductor_SMD/MetalLions_MMPC0402.pdf) |

### LED

| Part | Description | Symbol | Footprint | 3D model | Datasheet |
| --- | --- | --- | --- | --- | --- |
| Worldsemi SK6812-EC20 | Addressable RGB LED, integrated controller, single-wire serial interface, 2.0x2.0mm | `SK6812-EC20` | `LED_SK6812_EC20_2.0x2.0mm` | ✅ | [PDF](datasheets/LED_SMD/Worldsemi_SK6812-EC20.pdf) |
| XINGLIGHT XL-2835WWC-02 | XINGLIGHT XL-2835WWC-02 white LED, PLCC-2 3.5x2.8mm | KiCad | `LED_XINGLIGHT_XL-2835WWC-02` | ✅ | [PDF](datasheets/LED_SMD/XINGLIGHT_XL-2835WWC-02.pdf) |

### MCU Espressif

| Part | Description | Symbol | Footprint | 3D model | Datasheet |
| --- | --- | --- | --- | --- | --- |
| Espressif ESP32-C3 | 2.4GHz Wi-Fi and BLE 5 SoC, 32-bit RISC-V microcontroller, 22 GPIO, QFN-32 | `ESP32-C3` | `QFN-32-1EP_5x5mm_P0.5mm_EP3.7x3.7mm` (KiCad) | KiCad | [PDF](datasheets/MCU_Espressif/Espressif_ESP32-C3.pdf) |
| Espressif ESP32-H2 | IEEE 802.15.4 and BLE 5 SoC, Thread and Zigbee, 32-bit RISC-V microcontroller, 19 GPIO, QFN-32 | `ESP32-H2` | `VQFN-32-1EP_4x4mm_P0.4mm_EP2.8x2.8mm` (KiCad) | KiCad | [PDF](datasheets/MCU_Espressif/Espressif_ESP32-H2.pdf) |

### Module Cellular

| Part | Description | Symbol | Footprint | 3D model | Datasheet |
| --- | --- | --- | --- | --- | --- |
| SIMCom A7672x … A7670x | LTE Cat 1 and GSM/EDGE module, 10Mbps downlink, 5Mbps uplink, optional GNSS and Bluetooth, 3.4-4.2V supply, LCC+LGA-124 24x24mm | `A7672x` … `A7670x` (2) | `SIMCom_A7672x_A7670x` | ✅ | [PDF](datasheets/Module_Cellular/SIMCom_A7672x_A7670x.pdf) |

### Motor Driver

| Part | Description | Symbol | Footprint | 3D model | Datasheet |
| --- | --- | --- | --- | --- | --- |
| Texas DRV8316CRRGF | Three-phase BLDC motor driver, integrated FETs, 4.5-35V, 8A peak, SPI configuration, built-in current sensing, VQFN-40 | `DRV8316CRRGF` | `Texas_RGF0040E_VQFN-40-1EP_5x7mm_P0.5mm_EP3.8x5.8mm` | ✅ | [PDF](datasheets/Motor_Driver/Texas_DRV8316C.pdf) |

### Power Monitor

| Part | Description | Symbol | Footprint | 3D model | Datasheet |
| --- | --- | --- | --- | --- | --- |
| Maxim MAX17048G | Single-cell Li+ fuel gauge, ModelGauge, I2C, TDFN-8 | `MAX17048G` | `Maxim_TDFN-8-1EP_2x2mm_P0.5mm_EP0.9x1.3mm` | ✅ | [PDF](datasheets/Power_Monitor/Maxim_MAX1704x.pdf) |

### RF Module

| Part | Description | Symbol | Footprint | 3D model | Datasheet |
| --- | --- | --- | --- | --- | --- |
| SiliconLabs MGM240PB22VNA3 | Multi-protocol wireless module, EFR32MG24 SoC, 2.4 GHz Bluetooth LE / Zigbee / Thread / Matter, built-in antenna | `MGM240PB22VNA3` | `SiliconLabs_MGM240P` | ✅ | [PDF](datasheets/RF_Module/SiliconLabs_MGM240P.pdf) |

### Regulator Linear

| Part | Description | Symbol | Footprint | 3D model | Datasheet |
| --- | --- | --- | --- | --- | --- |
| ROHM BD10KA5WF … BD33KA5WF | 500mA 1.0V fixed positive voltage output, with enable, overcurrent and thermal shutdown protection, SOP-8 | `BD10KA5WF` … `BD33KA5WF` (7) | `ROHM_SOP-8_4.4x5mm_P1.27mm` | ✅ | [PDF](datasheets/Regulator_Linear/ROHM_BDxxKA5WF.pdf) |
| Texas TPS70933DBV | 150mA 30V 1uA quiescent current LDO with enable, fixed 3.3V output, SOT-23-5 | `TPS70933DBV` | `SOT-23-5` (KiCad) | KiCad | [PDF](datasheets/Regulator_Linear/Texas_TPS709.pdf) |

### Regulator Switching

| Part | Description | Symbol | Footprint | 3D model | Datasheet |
| --- | --- | --- | --- | --- | --- |
| Texas TPS564242DRL … TPS564247DRL | 4A synchronous buck converter, Eco-mode at light load, 3-16V input, 0.6-7V adjustable output, 1.2MHz, D-CAP3, SOT-563 | `TPS564242DRL` … `TPS564247DRL` (2) | `SOT-563` (KiCad) | KiCad | [PDF](datasheets/Regulator_Switching/Texas_TPS56424x.pdf) |

### Relay

| Part | Description | Symbol | Footprint | 3D model | Datasheet |
| --- | --- | --- | --- | --- | --- |
| Relpol RM51 | Relpol Relay SPDT RM51 | KiCad | `Relay_SPDT_Relpol_RM51` | ✅ | [PDF](datasheets/Relay_THT/Relpol_RM51.pdf) |
| TE OJ-SH-105HM | TE Connectivity OJ-SH-105HM,000 relay, SPST, THT package | KiCad | `Relay_SPST_TE_OJ-SH-105HM` | ✅ | [PDF](datasheets/Relay_THT/TE_OJ-SH-105HM.pdf) |

### Switch

| Part | Description | Symbol | Footprint | 3D model | Datasheet |
| --- | --- | --- | --- | --- | --- |
| SHOUHAN SS13D07VG4 | SP3T slide switch, common on pin 2, SHOUHAN SS13D07VG4 | `SW_SP3T_SS13D07VG4` | `SW_SP3T_SHOUHAN_SS13D07VG4` | ✅ | [PDF](datasheets/Switch/SHOUHAN_SS13D07VG4.pdf) |

### Switch Power

| Part | Description | Symbol | Footprint | 3D model | Datasheet |
| --- | --- | --- | --- | --- | --- |
| Texas TPS2121RUX | Priority power multiplexer, 2.8-22V, 4.5A, 56mOhm, seamless switchover, VQFN-HR-12 | `TPS2121RUX` | `Texas_RUX0012A_VQFN-HR-12_2x2.5mm_P0.5mm` | ✅ | [PDF](datasheets/Switch_Power/Texas_TPS212x.pdf) |

### TerminalBlock

| Part | Description | Symbol | Footprint | 3D model | Datasheet |
| --- | --- | --- | --- | --- | --- |
| DORABO DB125-2.54 | Terminal block, DORABO DB125-2.54-2P, 2 pins, pitch 2.54mm, horizontal wire entry | KiCad | `TerminalBlock_DORABO_DB125-2.54-2P_1x02_P2.54mm_Horizontal` | ✅ | [PDF](datasheets/TerminalBlock/DORABO_DB125-2.54.pdf) |

### TestPoint

| Part | Description | Symbol | Footprint | 3D model | Datasheet |
| --- | --- | --- | --- | --- | --- |
| TestPoint_2Pads_Pitch2.54mm_D1.4mm | Test point with 2 pins, pitch 2.54mm, diameter 1.4mm | KiCad | `TestPoint_2Pads_Pitch2.54mm_D1.4mm` | — | — |

### Thermistor

| Part | Description | Symbol | Footprint | 3D model | Datasheet |
| --- | --- | --- | --- | --- | --- |
| RT_Disc_D7mm_W2.8mm_P5mm | THT NTC thermistor, 10 Ω, 7 mm disc, 5.0 mm lead spacing (RM) | KiCad | `RT_Disc_D7mm_W2.8mm_P5mm` | ✅ | — |

### Transformer

| Part | Description | Symbol | Footprint | 3D model | Datasheet |
| --- | --- | --- | --- | --- | --- |
| Wurth 750370423 | Offline flyback transformer, EE13/7/6, 13.33:1:2.78 turns ratio, 1.5mH primary, THT | `Wurth_750370423` | `Transformer_Wurth_750370423` | ✅ | [PDF](datasheets/Transformer/Wurth_750370423.pdf) |
| Zeming ZMPT101B | Current-type voltage transformer, 1000:1000 turns ratio, 2mA rated, 4kV isolation, voltage and power measurement, THT | `ZMPT101B` | `Transformer_Zeming_ZMPT101B` | ✅ | [PDF](datasheets/Transformer/Zeming_ZMPT101B.pdf) |

<!-- components:end -->

## Contributing

Contributions are welcome. See [CONTRIBUTING.md](./CONTRIBUTING.md) for the rules and the development setup.

## License

- **Library (symbols, footprints and tooling):** [MIT License](./LICENSE).
- **Datasheets:** belong to their manufacturers and are redistributed for convenience.
- **3D models:** come from the part manufacturers or from LCSC/EasyEDA and remain subject to their terms.
