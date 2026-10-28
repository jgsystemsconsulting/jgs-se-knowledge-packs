# IVL: fhwa-its-se-pack (P42)

Date: 2026-10-28 · Range `e7b1674..eb5b1f8` · Deliverable: `2026-10-27-fhwa-its-se-pack-EXECUTED.md`

## Lens verdicts

- **Behavior** (`ivl-behavior`): NO_CRITICAL_OR_MAJOR. B1 pack loads (shape == faa-8110-49, both manifests resolve); B2 discoverability (chapter/topic indexes resolve, /se Civil-ITS + FHWA rows route, site surfaces present); B3 licence self-contained (PD § 105, zero URLs pack-wide); B4 gates validate/quality/release exit 0, map TOTAL 735.
- **Regression** (`ivl-regression`): NO_CRITICAL_OR_MAJOR. 12/12 test modules + 4/4 checkers exit 0 fresh-run; stale-count grep clean (no "72 packs"/"81 skills"/"728" in live surfaces); neighbor packs untouched (packs/se/SKILL.md +2 routing rows only); generators reproduce byte-identical; plugin versions and signpost count frozen; cursor 79-vs-82 gap pre-existing and unchanged.
- **Contract** (`ivl-contract`): ALL CONTRACTS MET. Cert sha256 matches (`bb36332a…b366`); D1-D8 MET; catalog 9-key row, watchlist 6-key row with version==source_version and last_checked 2026-10-28; generator 4×735; Do-not list clean. One reported MAJOR adjudicated FALSE POSITIVE: the lens looked for `note-overrides`/`map` keys inside `docs/classification-rules.json`; the overrides live in `docs/capability-pack-map-note-overrides.json` (7 fhwa rows, `generated_on` 2026-10-28) and the map in `docs/capability-pack-map.json` (`generated_on` present; `check_capability_map.py` PASS with 1:1 pairing verified).

## Post-fix gate

`python tooling/check_capability_map.py` → `PASS: capability map OK` after adjudication (no code change needed).

## Carry-forward

None new from IVL. Final-review Minor (glued `U.S.C.§`) already fixed pre-IVL in eb5b1f8.
