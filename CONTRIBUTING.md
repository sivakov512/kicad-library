## Contribution Guidelines

Contributions are welcome and appreciated.  
To maintain consistency, please follow the naming and structure conventions outlined below.

### Repository Structure

The repository is organized as follows:

```
.
├── 3dmodels/                  # 3D model files organized by category
│   ├── ACDC_Converters/       # Organized by component category
│   │   ├── SMD/               # Further organized by mounting type
│   │   └── THT/
│   ├── Antennas/
│   └── ...
├── datasheets/                # Datasheets organized by category
│   ├── ACDC_Converters/
│   ├── MCU/
│   │   └── Espressif/         # Manufacturer-specific subcategories
│   └── ...
├── design_blocks/             # Reusable schematic blocks
├── footprints/                # Footprint libraries (.pretty folders)
│   ├── Sivakov_ACDC_Converters_SMD.pretty/
│   ├── Sivakov_MCU_Espressif.pretty/
│   └── ...
├── symbols/                   # Symbol libraries (.kicad_sym files)
│   ├── Sivakov_ACDC_Converters.kicad_sym
│   ├── Sivakov_MCU_Espressif.kicad_sym
│   └── ...
└── README.md                  # Documentation
```

When adding new components or blocks, ensure they are placed in the correct directory and follow the naming conventions described below.

### Naming Convention

All items must start with the `Sivakov_` prefix.  
Use clear, structured names with underscores to separate sections.

#### Symbol Libraries:
```
Sivakov_[CategoryName].kicad_sym
Sivakov_[CategoryName]_[Manufacturer].kicad_sym
```

#### Footprint Libraries:
```
Sivakov_[CategoryName]_[MountingType].pretty
Sivakov_[CategoryName]_[Manufacturer].pretty
```

#### Example Footprint Name:
```
Capacitor_THT_Radial_D5.0mm_P1.50mm
│         │   │      │         │
│         │   │      │         └ Pin pitch (P)
│         │   │      └ Diameter (D)
│         │   └ Mounting style / type
│         └ Mounting technology (THT/SMD)
└ Component category
```

For manufacturer-specific components:
```
[Manufacturer]_[PartNumber]_[PackageInfo].kicad_mod
```
Example: `STMicroelectronics_VIPER06_SSO10.kicad_mod`

#### 3D Models and Datasheets:
Organized in category and mounting type folders:
```
3dmodels/[CategoryName]/[MountingType]/[ModelName].step
datasheets/[CategoryName]/[Manufacturer]_[PartNumber].pdf
```

### Footprints

- Place footprints in the appropriate `.pretty` folder under `footprints/`.
- Include a matching STEP model in the `3dmodels/` directory, following the category structure.
- Ensure the following layers are properly defined:
  - **Silkscreen**: For component outlines and labels.
  - **Courtyard**: For placement and clearance checks.
  - **Fab**: For assembly and manufacturing details.
- Use correct pin numbering as specified in the component's datasheet.
- Assign the 3D model to the footprint using `${KISYS3DMOD}/[Category]/[MountingType]/[ModelName].step`.

### Schematic Symbols

- Place schematic symbols in `.kicad_sym` libraries under `symbols/`.
- Group related symbols into a single library (e.g., `Sivakov_ACDC_Converters.kicad_sym` for all AC-DC converters).
- Use clear and descriptive names for symbols.
- Include the following metadata fields:
  - **Description**: Short, searchable phrases describing the component.
  - **Keywords**: Relevant keywords for searchability.
  - **Datasheet**: Path to the datasheet file using the `${KICADX_LIBS}` environment variable (e.g., `${KICADX_LIBS}/datasheets/ACDC_Converters/STMicroelectronics_VIPER06.pdf`).

### 3D Models

- Place 3D models in the appropriate subdirectory under `3dmodels/` following the category structure.
- Use the STEP format (`.step` or `.stp`) for compatibility.
- Ensure the 3D model matches the footprint dimensions and orientation.
- Name the 3D model file to match the associated footprint.

### Datasheets

- Place datasheets in the appropriate subdirectory under `datasheets/` following the category structure.
- Use descriptive filenames that include the manufacturer and part number (e.g., `STMicroelectronics_VIPER06.pdf`).
- Reference the datasheet in the `datasheet` field of symbols or footprints using the `${KICADX_LIBS}` environment variable.  
  **Example:** `${KICADX_LIBS}/datasheets/ACDC_Converters/STMicroelectronics_VIPER06.pdf`

### Design Blocks

- Place reusable schematic blocks in the `design_blocks/` directory.
- Keep blocks compact and focused on a single purpose.
- Use named inputs and outputs for clarity.
- Avoid mixing unrelated functionality in a single block.
- Use descriptive names for blocks and their files.

### Component Categories

Use the following categories for organizing components:

- `ACDC_Converters` - AC to DC converter ICs and modules
- `Amplifiers` - Operational amplifiers, instrumentation amplifiers, etc.
- `Antennas` - RF and wireless antennas
- `Capacitors` - All types of capacitors
- `Connectors` - Electrical connectors of all types
- `Converters_DCDC` - DC to DC converter ICs and modules
- `Diodes` - Diodes, TVS, rectifiers
- `Fuses` - Fuses and related components
- `FuseHolders` - Holders for fuses
- `Inductors` - Inductors and chokes
- `MCU` - Microcontrollers (with subcategories by manufacturer)
- `NetTies` - PCB network tie components
- `Power_Management` - Power management ICs
- `Relays` - Electromechanical relays
- `Resistors` - All types of resistors
- `Sensors` - Various sensor components
- `Switches` - Mechanical and electronic switches
- `Thermistors` - Temperature-dependent resistors
- `Transformers` - Electrical transformers
- `Transistors` - BJTs, MOSFETs, and other transistors

### Mounting Types

Use the following suffixes to indicate mounting type:

- `SMD` - Surface-mount devices
- `THT` - Through-hole technology components
- `Hybrid` - Components with both SMD and THT elements

### Metadata

- Use the `description`, `keywords`, and `datasheet` fields in symbols and footprints.
- Write descriptions in short, searchable phrases.
- Format dimensions consistently (e.g., `D5.0mm`, `P2.54mm`).

### General Guidelines

- Follow the existing structure and conventions in the repository.
- Test your contributions in KiCad to ensure compatibility and correctness.
- If you're unsure about something, open an issue or start a discussion — we're happy to help!

Thank you for contributing to the Sivakov Component Library!