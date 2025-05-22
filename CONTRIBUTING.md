## Contribution Guidelines

Contributions are welcome and appreciated.  
To maintain consistency, please follow the naming and structure conventions outlined below.

### Repository Structure

The repository is organized as follows:

```
.
├── 3dmodels/                  # 3D model files organized by category
│   ├── Sivakov_ACDC_Converters_SMD.3dshapes/
│   ├── Sivakov_Antennas_SMD.3dshapes/
│   └── ...
├── datasheets/                # Datasheets organized by category
│   ├── ACDC_Converters/
│   ├── MCU/
│   └── ...
├── footprints/                # Footprint libraries (.pretty folders)
│   ├── Sivakov_ACDC_Converters_SMD.pretty/
│   ├── Sivakov_MCU_Espressif.pretty/
│   └── ...
├── symbols/                   # Symbol libraries (.kicad_sym files)
│   ├── Sivakov_ACDC_Converters.kicad_sym
│   ├── Sivakov_MCU_Espressif.kicad_sym
│   └── ...
├── metadata.json              # Library metadata
└── README.md                  # Documentation
```

When adding new components, ensure they are placed in the correct directory and follow the naming conventions described below.

### Naming Convention

All library items must start with the `Sivakov_` prefix.  
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

#### 3D Models Libraries:
```
Sivakov_[CategoryName]_[MountingType].3dshapes
Sivakov_[CategoryName]_[Manufacturer].3dshapes
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

#### Datasheets:
Organized in category folders:
```
datasheets/[CategoryName]/[Manufacturer]_[PartNumber].pdf
```

### Footprints

- Place footprints in the appropriate `.pretty` folder under `footprints/`.
- Include a matching STEP model in the `3dmodels/` directory, following the same naming structure.
- Ensure the following layers are properly defined:
  - **Silkscreen**: For component outlines and labels.
  - **Courtyard**: For placement and clearance checks.
  - **Fab**: For assembly and manufacturing details.
- Use correct pin numbering as specified in the component's datasheet.
- Assign the 3D model to the footprint using relative paths or the `${KISYS3DMOD}` environment variable.

### Schematic Symbols

- Place schematic symbols in `.kicad_sym` libraries under `symbols/`.
- Group related symbols into a single library (e.g., `Sivakov_ACDC_Converters.kicad_sym` for all AC-DC converters).
- Use clear and descriptive names for symbols.
- Include the following metadata fields:
  - **Description**: Short, searchable phrases describing the component.
  - **Keywords**: Relevant keywords for searchability.
  - **Datasheet**: Link to the datasheet file.

### 3D Models

- Place 3D models in the appropriate `.3dshapes` directory under `3dmodels/`.
- Use the STEP format (`.step` or `.stp`) for compatibility.
- Ensure the 3D model matches the footprint dimensions and orientation.
- Name the 3D model file to match the associated footprint.

### Datasheets

- Place datasheets in the appropriate subdirectory under `datasheets/` following the category structure.
- Use descriptive filenames that include the manufacturer and part number (e.g., `STMicroelectronics_VIPER06.pdf`).
- Reference the datasheet in the `datasheet` field of symbols.



### Mounting Types

Use the following suffixes to indicate mounting type:

- `SMD` - Surface-mount devices
- `THT` - Through-hole technology components

### Metadata

- Use the `description`, `keywords`, and `datasheet` fields in symbols and footprints.
- Write descriptions in short, searchable phrases.
- Format dimensions consistently (e.g., `D5.0mm`, `P2.54mm`).

### General Guidelines

- Follow the existing structure and conventions in the repository.
- Test your contributions in KiCad to ensure compatibility and correctness.
- If you're unsure about something, open an issue or start a discussion — we're happy to help!

Thank you for contributing to the Sivakov Component Library!