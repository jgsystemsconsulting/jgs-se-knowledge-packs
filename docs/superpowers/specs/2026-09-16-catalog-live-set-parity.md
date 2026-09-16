# Catalog live-set parity (P16): design spec

Date: 2026-09-16. Status: drafted for planning. Package: P16. Promoted backlog: b-03.

## Problem

`catalog.json` is a required release artifact but is only existence- and JSON-parse-checked. The live `packs` array is already set-equal to content pack dirs (63 slugs, no signposts), yet nothing fails when that set drifts. The top-level `updated` field is still `2026-08-17` while `RELEASE-INFO.txt` stages `2026-08-27T00:00:00Z` (backlog b-03). Same honesty class as P15 landing counts, on the machine-readable catalogue.

## Codebase context

Verified 2026-09-16 against the working tree:

- `packs/` holds 65 dirs with `SKILL.md`. Exactly 2 carry frontmatter `kind: signpost` (`omg-signpost`, `se-standards-signpost`); 63 are content packs.
- `catalog.json` has `packs` (63 entries, all `status: live`) set-equal to content dirs, `planned` (1 entry, free), and stale `"updated": "2026-08-17"`.
- Signposts are not catalog entries and must stay out of `catalog.packs`.
- `tooling/check_release.py` lists `catalog.json` in `REQUIRED_FILES` and stops there for the file. Check 13 covers landing counts only.
- `.github/workflows/validate.yml` step `Catalog JSON valid` is parse-only (`json.load`).

## Decision: live slug set equality

Live content pack slug set equals the set of `catalog.packs[].slug` where `status` is `live`, or every entry when `status` is absent. Equality is both directions. Signpost dirs (frontmatter `kind: signpost`, same rule as P15) must not appear in `catalog.packs` under any status. `planned[]` is free and is not compared to `packs/`.

Live slugs always come from the filesystem. Missing `SKILL.md` or unparseable frontmatter fails closed.

## Decision: updated date (b-03)

Set `catalog.json` `"updated"` to `2026-08-27` (date portion of `RELEASE-INFO.txt` `Staged: 2026-08-27T00:00:00Z`).

Rationale: backlog b-03 is specifically catalog metadata lagging the staged release stamp. Aligning to the staged date closes that item without inventing a second clock. Product meaning of `updated` here is "catalogue metadata aligned to the current staged release inventory", not "any calendar day an agent touched the file".

The fail-closed gate does **not** pin `updated` to `RELEASE-INFO` forever. Release stage and inventory can diverge after a freeze; continuous equality would force a catalog touch on every stage bump with no inventory change. The gate pins slug-set honesty. `updated` is corrected in this package and remains a review surface for future inventory edits.

## Changes

### 1. catalog.json

- Bump `"updated"` from `2026-08-17` to `2026-08-27`.
- No slug list rewrite required if the live set already matches (verified). If a recount finds drift, fix `packs[]` to match content dirs and keep signposts out.

### 2. tooling/check_release.py: new check 14 [catalog-live-set]

- Inventory content vs signpost slug sets from `packs/*/SKILL.md` (reuse the P15 signpost frontmatter rule).
- Load `catalog.json`. Require `packs` to be a list of objects with non-empty string `slug`.
- Live catalog set = slugs with `status == "live"` or missing `status`.
- Fail if live catalog set != content slug set (message lists only-in-packs and only-in-catalog).
- Fail if any signpost slug appears in `catalog.packs`.
- Fail on duplicate live slugs.
- Tag every failure `[catalog-live-set]`.
- Update the module docstring numbering and CI-covered line.

### 3. CI twin in .github/workflows/validate.yml

Add step `Catalog live-set parity` (stdlib heredoc, never executes repo code) after `Catalog JSON valid`. Coverage map line: twins check_release 14. Keep parse-only `Catalog JSON valid` as the cheap syntax gate.

### 4. Tests

- `tooling/test_catalog_live_set.py`: assert-based probe for inventory slugs, live-set equality, signpost exclusion, and the real tree.
- Extend `tooling/test_ci_gate.py`: pin the new step, shared literals, negative demo (stale extra catalog slug fails), positive real-tree run.

## Out of scope

- Landing HTML, still assets, packs.html (P15 / generators).
- P8 ledger.
- Expanding `planned[]` into live packs.
- Version bump, CHANGELOG, plugin.json, RELEASE-INFO edits.

## Success criteria

- `catalog.json` `updated` is `2026-08-27`; live `packs[]` slugs remain set-equal to content dirs; signposts absent from `packs[]`.
- `python tooling/check_release.py` PASS with check 14 present.
- CI twin step green; coverage map names check 14.
- Negative demo: inject a phantom catalog slug and confirm `[catalog-live-set]` failure; restore PASS.
- `tooling/test_catalog_live_set.py` and `tooling/test_ci_gate.py` pass.
- Packages doc marks P16 done; b-03 stays `promoted`.

## Research

research: skipped (in-repo catalogue honesty; no external API)
