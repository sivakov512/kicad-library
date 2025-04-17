## Contribution Guidelines

Contributions are welcome and appreciated.
To maintain consistency, please follow the naming and structure conventions below.

### Naming convention

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

Recommended component prefixes:
- `CP_` – Polarized capacitors
- `Fuse_` – Fuses and holders
- `Relay_` – Mechanical relays
- `LDO_`, `MCU_`, `Connector_`, etc. – As needed

### Footprints

- Place in matching `.pretty` folder
- Include STEP model if possible (same base name)
- Define silkscreen, courtyard, and fab layers
- Use correct pin numbering from datasheets

### Schematic blocks

- Keep compact and single-purpose
- Prefer named inputs/outputs
- Avoid mixing unrelated functionality in one block

### Metadata

- Use `description`, `keywords`, and `datasheet` fields
- Write descriptions in short, searchable phrases
- Format dimensions consistently (e.g., `D5.0mm`, `P2.54mm`)

Not sure about something? Open an issue — happy to help.
