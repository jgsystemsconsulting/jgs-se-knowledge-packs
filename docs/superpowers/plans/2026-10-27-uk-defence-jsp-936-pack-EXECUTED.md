# EXECUTED: uk-defence-jsp-936-pack (P28)

Date: 2026-10-27
Plan: `docs/superpowers/plans/2026-10-27-uk-defence-jsp-936-pack.md`
Spec: `docs/superpowers/specs/2026-10-27-uk-defence-jsp-936-pack.md`
Range: `352137a..04f8f0e` (branch `packages-2026-10-27`)

## What shipped

- New pack `packs/jsp-936/`: tier-2, OGL v3.0, JSP 936 Part 1: Directive V1.1 (November 2024) only. 8 chapters (PDF-wins chapter map), glossary, cheatsheet, references, LICENSE (full OGL deed, gov.uk attribution), PACK.yaml, SKILL.md.
- Full D6 registration: `catalog.json`, `docs/source-watchlist.json` (`--record`), `SKILLS.md` (72 packs), `packs/se/SKILL.md` (Defence row + Licences row + AI row), `NOTICE`, `.claude-plugin/plugin.json`, `.cursor-plugin/plugin.json`, classification assignments (8) + paired note overrides + regenerated capability map (720→728), README badge+row, `docs/index.html`/`still-catalogue.svg`/website YAML (72/81, UK 3), `docs/candidate-packs.md` row 4, CHANGELOG Unreleased entry, generated pack page + sitemap.
- Generator count literals in `tooling/generate_capability_map.py`: 720→728 (four loci).
- Prose fix in `ch07-suppliers.md` ("leverage" → "bargaining power") from Task 5 prose_check.

## Execution notes

- Task 1 brief garbled mid-flight (OCR-mangled steps): scope reduced to vetting; pack scaffold + chapters absorbed into Task 2. Controller committed pack content (`14af68f`) after Task 2 implementer left it untracked.
- Tasks 3+4 combined into one implementer dispatch (registration surfaces), reviewed in one pass: all ✅, Approved.
- Task 5 (flash): surface grep clean, prose_check 3 findings → 1 fixed (named surface), 2 justified keeps (directive vocabulary "robust/Robustness" — verbatim source triad). `RELEASE CHECK: PASS (v1.22.1 @ 9d0cd0d)`; `git ls-files sources/` empty.

## Review trail

- Task 3+4 reviewer (`sdd-reviewer-task`): all requirements ✅, minor stale line-loc in brief only. Approved.
- Final whole-branch review (`sdd-reviewer-final`): **Approved-with-deferred-minors**. No Critical, no Important.
  - M1 (Minor): `docs/index.html:108` title-card img alt still says "71 packs" — decorative alt, not a `[pack-count]` gate surface; fix next catalogue-count pass.
  - M2 (Minor): `packs/jsp-936/glossary.md:37` "Robustness" slop advisory — directive vocabulary, keep.

## Gates at close

`python tooling/check_release.py` → `RELEASE CHECK: PASS (v1.22.1 @ 04f8f0e)`. `validate_pack.py packs/jsp-936` PASS. `check_pack_quality.py packs/jsp-936` PASS. Capability map TOTAL: 728.
