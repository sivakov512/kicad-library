# KiCadX Libraries

A collection of custom libraries for KiCad 9+, including schematic blocks, footprint libraries, and matching 3D models.

## Design blocks
Custom reusable schematic blocks grouped by function, located in [`design_blocks/`](design_blocks):

### Power supply
- **AC → 5V (HLK-5M05)** — quick prototyping solution
- **AC → 5V (LNK306P)** — standalone switching power supply for production-grade designsy
- **5V → 3.3V** using LM1117 with filtering

## Footprints
Custom component footprints grouped into `.pretty` folders under [`footprints/`](footprints):

### Capacitors
- Radial electrolytic capacitor — 5mm diameter, 1.5mm pitch (`CP_Radial_D5.0mm_P1.50mm.kicad_mod`)

### Fuse holders
- 5x20mm fuse holder — PTF76, 15mm lead spacing (`Fuse_PTF76_5x20mm_RM15mm.kicad_mod`)

### Relays
- Relpol RM51 — SPDT, 10A mechanical relay (`Relay_SPDT_Relpol-RM51.kicad_mod`, with matching 3D model)

## 3D models
Located in [`3dmodels/`](3dmodels):
- STEP models for fuse holder and relay footprints

## Installation

1. Clone the repository to your local system:
   ```bash
   git clone git@github.com:sivakov512/kicadx-libs.git
   ```

2. In KiCad, open **Preferences → Configure Paths** and add a new environment variable:
   - **Name:** `KICADX_LIBS`
   - **Path:** absolute path to the cloned repository

3. Add the needed libraries through **Preferences → Manage Footprint Libraries** or **Manage Design Block Libraries**, using paths like:
   - `${KICADX_LIBS}/footprints/KiCadX_FuseHolders_THT.pretty`
   - `${KICADX_LIBS}/design_blocks/power.kicad_blocks/`

## Contribution

Contributions are welcome! Please follow the naming conventions outlined in [CONTRIBUTING.md](./CONTRIBUTING.md).

## License

This project is licensed under the terms of the [MIT License](./LICENSE).
