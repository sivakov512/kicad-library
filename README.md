# KiCadX Libraries

A collection of custom libraries for KiCad 9+, including schematic blocks, footprint libraries, and matching 3D models.

### Design blocks
Reusable schematic blocks located in [`design_blocks/power.kicad_blocks/`](design_blocks/power.kicad_blocks/):
- **5V → 3.3V** using LM1117 with filtering
- **AC → 5V** using HLK-5M05 with fuse and varistor

### Footprints
Custom component footprints grouped into `.pretty` folders under [`footprints/`](footprints):

#### Capacitors
- Radial electrolytic capacitor — 5mm diameter, 1.5mm pitch (`CP_Radial_D5.0mm_P1.50mm.kicad_mod`)

#### Fuse holders
- 5x20mm fuse holder — PTF76, 15mm lead spacing (`Fuse_PTF76_5x20mm_RM15mm.kicad_mod`)

#### Relays
- Relpol RM51 — SPDT, 10A mechanical relay (`Relay_SPDT_Relpol-RM51.kicad_mod`, with matching 3D model)

### 3D models
Located in [`3dmodels/`](3dmodels):
- STEP models for fuse holder and relay footprints

## Installation

1. Clone the repository to your local system:
   ```bash
   git clone git@github.com:sivakov512/kicadx-libs.git
   ```
2. In KiCad, go to **Preferences** → **Manage Footprint Libraries** or **Manage Design Block Libraries**
3. Add the relevant subdirectories from the cloned repo to your global or project library list

## Contribution

Contributions are welcome! Please follow the naming conventions outlined in [CONTRIBUTING.md](./CONTRIBUTING.md).

## License

This project is licensed under the terms of the [MIT License](./LICENSE).
