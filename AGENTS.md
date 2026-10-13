# Notes for agents

Read [CONTRIBUTING.md](./CONTRIBUTING.md) first: it holds the repository rules, the layout and the checks. The notes below add what matters when an agent does the work.

- Run `make check` before calling a change done. It must end with 0 errors.
- Run heavy commands (renders, `make check`, STEP processing) one at a time and with `nice`; the maintainer works on the same machine.
- After editing `.kicad_sym` or `.kicad_mod` files with a script, run `kicad-cli sym upgrade --force` or `kicad-cli fp upgrade --force` on them to restore KiCad's own formatting, then check the diff.
- Never draw 3D models yourself. Download them, e.g. `uvx easyeda2kicad --3d --lcsc_id=C123456`. Align them to the pads and bake the placement into the STEP. Verify against a render with `kicad-cli pcb render`: pins in holes, body on the board, polarity.
- Work in the repository's local form (`LOCAL_SKC_`, `${KIPRJMOD}`, `@main`); never write `PCM_SKC_` or `${KICAD10_3RD_PARTY}` paths.
- The default shell is zsh, where `$VAR` does not split into words. Write loops over lists as `bash -c` or pass the list through `xargs`.
- macOS file systems are case-insensitive. Do a rename that only changes case in two steps through a temporary name (`git mv a tmp && git mv tmp A`).
- Commit messages: one subject line in Conventional Commits form, no body, no co-author trailers.
