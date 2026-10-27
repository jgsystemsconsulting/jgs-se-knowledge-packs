# IVL: uk-defence-jsp-936-pack (P28)

Date: 2026-10-27 · Range `352137a..04f8f0e` (+ fix commit) · Deliverable: `2026-10-27-uk-defence-jsp-936-pack-EXECUTED.md`

## Lens verdicts

- **Behavior** (`ivl-behavior`): NO_CRITICAL_OR_MAJOR. Pack loads as skill (shape == jsp-376, both manifests resolve); discoverable via SKILL.md index, se Defence/Licences/AI rows, catalog, site surfaces; licence self-contained in LICENSE; gates validate/quality/release all exit 0.
- **Regression** (`ivl-regression`): ISSUES_FOUND → fixed in-loop. 17/17 test+gate suite exit 0; neighbor packs untouched (only `packs/se/SKILL.md` routing rows +jsp-936); signposts stay 8; plugin versions 1.22.1/1.22.0 untouched; generated surfaces regenerate zero-diff.
  - M1 fixed: `docs/candidate-packs.md:29` stale "80 packs: 71 full" → "81 packs: 72 full".
  - A1 fixed: `docs/DISTRIBUTION.md:11` "all 80" manifest paths → "all 81" (both loci).
- **Contract** (`ivl-contract`): ALL CONTRACTS MET, PASS. Spec cert sha256 matches disk (`1cadc041…454e`); all 16 contract rows MET (tier-2 shape, Part 1 V1.1 only, OGL URLs LICENSE-only, 8 chapters, no fabricated quotes/URLs, pin exact, D1–D7 covered, 9-field catalog row, 6-key watchlist, 1:1 notes, 728 literals, `updated` 2026-10-14, no RELEASE-INFO bump, no jsp-376/sources edits).

## Post-fix gate

`python tooling/check_release.py` → `RELEASE CHECK: PASS (v1.22.1 @ 04f8f0e)` after the two doc fixes.

## Carry-forward

None new. Pre-existing M1/M2 from final review (index.html alt "71", glossary "Robustness") stay deferred as recorded in EXECUTED doc.
