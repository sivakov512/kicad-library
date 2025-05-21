# Sivakov Component Library

A comprehensive collection of custom libraries for KiCad, including schematic symbols, footprints, 3D models, and reusable design blocks. Organized by component categories and mounting types for easy navigation.

## Library Structure

The library is organized using the following structure:

### Design Blocks
Custom reusable schematic blocks grouped by function, located in [`design_blocks/`](design_blocks):

- **Power Block** — includes various power supply solutions, DC-DC converters, etc.

### Symbols
Schematic symbols grouped by component category in `.kicad_sym` files under [`symbols/`](symbols):

- **`Sivakov_ACDC_Converters.kicad_sym`** — symbols for AC-DC converters
- **`Sivakov_MCU_Espressif.kicad_sym`** — symbols for Espressif microcontrollers
- **`Sivakov_Transformers.kicad_sym`** — symbols for transformers

### Footprints
Component footprints grouped by category and mounting type in `.pretty` folders under [`footprints/`](footprints):

- **`Sivakov_ACDC_Converters_SMD.pretty`** — footprints for SMD AC-DC converters
- **`Sivakov_Antennas_SMD.pretty`** — footprints for SMD antennas
- **`Sivakov_Capacitors_THT.pretty`** — footprints for through-hole capacitors
- **`Sivakov_FuseHolders_THT.pretty`** — footprints for through-hole fuse holders
- **`Sivakov_Fuse_SMD.pretty`** — footprints for SMD fuses
- **`Sivakov_Inductors_THT.pretty`** — footprints for through-hole inductors
- **`Sivakov_MCU_Espressif.pretty`** — footprints for Espressif microcontrollers
- **`Sivakov_NetTies.pretty`** — footprints for PCB net ties
- **`Sivakov_Relays_THT.pretty`** — footprints for through-hole relays
- **`Sivakov_Thermistors_THT.pretty`** — footprints for through-hole thermistors
- **`Sivakov_Transformers_THT.pretty`** — footprints for through-hole transformers

### 3D Models
3D models organized by component category and mounting type under [`3dmodels/`](3dmodels):

- **`ACDC_Converters/SMD/`** — 3D models for SMD AC-DC converters
- **`Antennas/SMD/`** — 3D models for SMD antennas
- **`FuseHolders/THT/`** — 3D models for through-hole fuse holders
- **`Fuses/SMD/`** — 3D models for SMD fuses
- **`MCU/Espressif/`** — 3D models for Espressif microcontrollers
- **`Relays/THT/`** — 3D models for through-hole relays
- **`Thermistors/THT/`** — 3D models for through-hole thermistors
- **`Transformers/THT/`** — 3D models for through-hole transformers

### Datasheets
Component datasheets organized by category under [`datasheets/`](datasheets):

- **`ACDC_Converters/`** — datasheets for AC-DC converters
- **`Antennas/`** — datasheets for antennas
- **`Inductors/`** — datasheets for inductors
- **`MCU/Espressif/`** — datasheets for Espressif microcontrollers
- **`Relays/`** — datasheets for relays
- **`Transformers/`** — datasheets for transformers

## Component List

### AC-DC Converters
- **STMicroelectronics VIPER06** — High-voltage offline converter in SSO10 package

### Antennas
- **TaiyoYuden AH316M245001-T** — Compact 2.4GHz antenna
- **PCB Antenna** — Espressif reference 2.4GHz antenna design (left and right variants)

### Capacitors
- **Radial Electrolytic Capacitors** — Various sizes for through-hole mounting

### Fuses and Fuse Holders
- **PTF76** — 5x20mm fuse holder with 15mm lead spacing
- **2410 (6125 Metric)** — 6.1x2.5mm SMD fuse

### Inductors
- **TDK B82720K** — Vertical through-hole inductor, 13x9.5mm body

### Microcontrollers
- **ESP32-H2** — Low-power wireless microcontroller with Zigbee and Thread support
- **TQFN-32 Package** — For Espressif microcontrollers, with multiple thermal pad variants

### Relays
- **Relpol RM51** — SPDT, 10A mechanical relay
- **OJ SH-105HM** — SPST relay, 5V coil

### Thermistors
- **NTC10D-7** — 10Ω NTC thermistor, 7mm disc, 5mm pitch

### Transformers
- **Wurth 750370423** — E13 core transformer for isolated DC-DC converters

## Installation

### As a Plugin (Recommended)
1. Download the release archive or clone the repository
2. Extract the contents to a directory of your choice
3. In KiCad, go to **Plugin and Content Manager**
4. Click **Install from File** and select the directory containing this library
5. The libraries will automatically be available in your KiCad installation

### Manual Installation
1. Clone the repository to your local system:
   ```bash
   git clone git@github.com:sivakov512/kicad-components.git
   ```

2. In KiCad, open **Preferences → Configure Paths** and add a new environment variable:
   - **Name:** `KICADX_LIBS`
   - **Path:** absolute path to the cloned repository

3. Add the libraries to KiCad using the appropriate menu:
   - **Preferences → Manage Symbol Libraries** for schematic symbols
   - **Preferences → Manage Footprint Libraries** for footprints
   - **Preferences → Manage Design Block Libraries** for design blocks

   Add the libraries by specifying their paths using the `${KICADX_LIBS}` environment variable. For example:
   - For symbols: `${KICADX_LIBS}/symbols/Sivakov_ACDC_Converters.kicad_sym`
   - For footprints: `${KICADX_LIBS}/footprints/Sivakov_ACDC_Converters_SMD.pretty`
   - For design blocks: `${KICADX_LIBS}/design_blocks/power.kicad_blocks/`

4. 3D models are automatically linked from the footprints using the `${KISYS3DMOD}` path

## Naming Conventions

This library follows consistent naming conventions to make components easy to find and use:

### Symbol Libraries
```
Sivakov_[CategoryName].kicad_sym
Sivakov_[CategoryName]_[Manufacturer].kicad_sym
```

### Footprint Libraries
```
Sivakov_[CategoryName]_[MountingType].pretty
Sivakov_[CategoryName]_[Manufacturer].pretty
```

### 3D Models
```
[CategoryName]/[MountingType]/[ModelName].step
[CategoryName]/[Manufacturer]/[ModelName].step
```

### Datasheets
```
[CategoryName]/[Manufacturer]_[PartNumber].pdf
[CategoryName]/[Manufacturer]/[PartNumber].pdf
```

## Contribution

Contributions are welcome! Please follow the naming conventions outlined above and in [CONTRIBUTING.md](./CONTRIBUTING.md).

## License

This project is licensed under the terms of the [MIT License](./LICENSE).
