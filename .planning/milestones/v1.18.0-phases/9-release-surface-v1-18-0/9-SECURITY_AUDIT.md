# Phase 9 Security Audit — Release Surface v1.18.0

**Range audited:** release commit `d19be1a` (11 files), tag object `cae0145` → `d19be1a`, GitHub Release `v1.18.0`, plus a whole-range sweep `v1.17.0..v1.18.0` (90 commits) for secrets and pack-content licence drift.
**Date:** 2026-08-17
**Method:** `git show` full-diff pattern scans (credential regexes `ghp_`, `AKIA…`, `github_pat_`, `sk-`, `BEGIN PRIVATE KEY`, api_key/password/secret/token/Bearer; email regex; URL extraction), `gh release view --json body` URL count, name-status reconciliation of every file in the commit and range, licence-file diffs for the renamed pack, tag-object inspection local vs `git ls-remote`.

**Verdict:** SECURED

## Findings

| # | Check | Status | Evidence |
|---|---|---|---|
| 1 | Release-commit diff scan: secrets / PII / URLs | SECURED | URLs in `git show d19be1a` (9 unique): own repo URL, 5 shields.io badges (incl. the 1.17.0→1.18.0 badge swap, so both versions legitimately appear), `keepachangelog.com/en/1.1.0/`, `semver.org` — all expected changelog/badge furniture; **zero source-material URLs**. Credential-pattern scan: 1 hit, false positive ("ri**sk-i**nformed accreditation" matching `sk-`); no token/key/password values. PII: sole email is the author's GitHub `noreply` address (245595077+…@users.noreply.github.com) in commit metadata only. |
| 2 | GitHub Release notes: no source-material URLs | SECURED | `gh release view v1.18.0 --json body` → `grep -cE "https?://"` = **0**. Notes describe the 7 packs, the rename (+catalog alias), capability map v2, and fixes — all by name, no document/mirror/download URLs. |
| 3 | No untracked strays committed | SECURED | `git show --name-status d19be1a` = exactly 11 `M` files, all intentional release surfaces (.claude-plugin/plugin.json, .cursor-plugin/plugin.json, CHANGELOG.md, README.md, RELEASE-INFO.txt, docs/SOURCE-VETTING.md, docs/capability-map-CONTRACT.md, docs/index.html, docs/packs.html, docs/products/website/01-jgs-se-knowledge-packs.yaml, docs/products/website/catalog.yaml). No adds, no temp/local/OS-junk files. Working tree clean. Range sweep `v1.17.0..v1.18.0`: adds are only 7 new `packs/*` trees, 3 docs files (ROLE-AGENTS-REQUIREMENTS-V2, capability-map-CONTRACT, capability-pack-map.{json,md}), `tooling/check_capability_map.py`, and `.planning/` records — every add accounted for by a phase artifact. |
| 4 | Licence compliance unchanged (content edits = docs/metadata only) | SECURED | Release commit touches zero `packs/` files — docs/metadata/version surfaces only. Range-level pack-content deltas all benign: (a) `doe-413-3b` → `doe-o-413-3` rename with chapters R100 (byte-identical moves); LICENSE diff = slug header line only ("…(formerly doe-413-3b)"), PACK.yaml = slug + alias note, licence terms untouched; (b) `packs/doe-sem/chapters/ch03-planning-stage.md` = one cross-reference line updated to the new slug (commit c9d5e7e); (c) 7 new packs all Tier-1 US-gov public domain (catalog `license_tier: 1`, release notes, SOURCE-VETTING rows). `sebok` remains CC BY-NC-SA 3.0 `commercial_use: false` and is correctly excluded from the Cursor manifest by the §6b gate. Root LICENSE/COPYRIGHT/NOTICE terms unchanged (NOTICE +72 lines = new-pack attributions only). |
| 5 | Tag is the tamper-evidence anchor | SECURED | `v1.18.0` is an **annotated** tag (`git cat-file -t cae0145` = `tag`; tagger jgsystemsconsulting + timestamp 1786928604 +0100 + message matching the release subject). Present on origin: `git ls-remote --tags origin` shows `refs/tags/v1.18.0` = `cae0145` with `^{}` peel = `d19be1a` — byte-identical to the local tag object, so any history rewrite/re-tag on either side is detectable. No competing 1.18-prefixed tags; `gh release list` shows a single, Latest release on the tag. |

## Additional sweep (beyond brief)

- **Whole-range credential scan** (`git diff v1.17.0 v1.18.0`): all pattern hits are prose inside `.planning/` audit/plan documents describing prior scans or listing regex names — no credential values anywhere in the release range.
- **Release metadata**: `isDraft: false`, `isPrerelease: false`; published 2026-08-17T01:03:47Z, consistent with the release-commit timestamp (02:03:23 +0100).

## Threat notes (informational, no action)

1. Release notes disclose that the Cursor manifest's 7-pack addition landed post-v1.17.0-tag in `e00ac7d` and is surfaced here for completeness — transparency handled correctly; no exposure.
2. Source-material URLs remain confined to their designated stores (e.g. 6-RESEARCH.md §2, PACK.yaml provenance) per Link Policy; the public release surfaces (notes, README, SOURCE-VETTING) stay URL-free where required (SOURCE-VETTING plan action explicitly enforces "no http/https URLs in added text").

**Escalations:** none.
