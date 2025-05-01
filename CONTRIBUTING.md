## Contribution Guidelines

Contributions are welcome and appreciated.  
To maintain consistency, please follow the naming and structure conventions outlined below.

### Repository Structure

The repository is organized as follows:

```
.
├── 3dmodels/          # STEP files for 3D models
├── datasheets/        # Datasheets for components
├── design_blocks/     # Reusable schematic blocks
├── footprints/        # Footprint libraries (.pretty folders)
├── symbols/           # Schematic symbol libraries (.kicad_sym files)
└── README.md          # Documentation
```

When adding new components or blocks, ensure they are placed in the correct directory and follow the naming conventions described below.

### Naming Convention

All items must start with the `KiCadX_` prefix.  
Use clear, structured names in `PascalCase_With_Underscores`.

**Example:**

```
KiCadX_CP_Radial_D5.0mm_P1.50mm
│       │   │      │         │
│       │   │      │         └ Pin pitch (P)
│       │   │      └ Diameter (D)
│       │   └ Mounting style / type
│       └ Component class (CP = polarized capacitor)
└ Repository prefix
```

#### Recommended Component Prefixes:
- `CP_` – Polarized capacitors
- `Fuse_` – Fuses and holders
- `Relay_` – Mechanical relays
- `LDO_`, `MCU_`, `Connector_`, etc. – As needed

### Footprints

- Place footprints in the appropriate `.pretty` folder under `footprints/`.
- Include a matching STEP model in the `3dmodels/` directory, if possible. The 3D model should have the same base name as the footprint.
- Ensure the following layers are properly defined:
  - **Silkscreen**: For component outlines and labels.
  - **Courtyard**: For placement and clearance checks.
  - **Fab**: For assembly and manufacturing details.
- Use correct pin numbering as specified in the component's datasheet.
- Assign the 3D model to the footprint in the `.kicad_mod` file.

### Schematic Symbols

- Place schematic symbols in `.kicad_sym` libraries under `symbols/`.
- Group related symbols into a single library (e.g., `KiCadX_ACDC_Converters.kicad_sym` for all AC-DC converters).
- Use clear and descriptive names for symbols.
- Include the following metadata fields:
  - **Description**: Short, searchable phrases describing the component.
  - **Keywords**: Relevant keywords for searchability.
  - **Datasheet**: Path to the datasheet file using the `${KICADX_LIBS}` environment variable (e.g., `${KICADX_LIBS}/datasheets/viper06.pdf`).

### 3D Models

- Place 3D models in the `3dmodels/` directory.
- Use the STEP format (`.step` or `.stp`) for compatibility.
- Ensure the 3D model matches the footprint dimensions and orientation.
- Name the 3D model file to match the associated footprint (e.g., `VIPER06_SSO10.step` for `VIPER06_SSO10.kicad_mod`).

### Datasheets

- Place datasheets in the `datasheets/` directory.
- Use descriptive filenames that match the component name (e.g., `viper06.pdf` for the VIPER06 component).
- Reference the datasheet in the `datasheet` field of the schematic symbol or footprint using the `${KICADX_LIBS}` environment variable.  
  **Example:** `${KICADX_LIBS}/datasheets/viper06.pdf`

### Design Blocks

- Place reusable schematic blocks in the `design_blocks/` directory.
- Keep blocks compact and focused on a single purpose.
- Use named inputs and outputs for clarity.
- Avoid mixing unrelated functionality in a single block.
- Use descriptive names for blocks and their files.

### Metadata

- Use the `description`, `keywords`, and `datasheet` fields in symbols and footprints.
- Write descriptions in short, searchable phrases.
- Format dimensions consistently (e.g., `D5.0mm`, `P2.54mm`).

### General Guidelines

- Follow the existing structure and conventions in the repository.
- Test your contributions in KiCad to ensure compatibility and correctness.
- If you're unsure about something, open an issue or start a discussion — we're happy to help!

Thank you for contributing to the KiCadX Libraries!