---
phase: 5-release-surface-v1-17-0
reviewed: 2026-08-15T05:59:05Z
depth: deep
files_reviewed: 10
files_reviewed_list:
  - .claude-plugin/plugin.json
  - .cursor-plugin/plugin.json
  - CHANGELOG.md
  - README.md
  - RELEASE-INFO.txt
  - docs/PACK-SPEC.md
  - docs/index.html
  - docs/packs.html
  - docs/products/website/01-jgs-se-knowledge-packs.yaml
  - docs/products/website/catalog.yaml
findings:
  critical: 0
  warning: 0
  info: 3
  total: 3
status: issues_found
verdict: PASS_WITH_NOTES
---

# Phase 5: Code Review Report — Release surface v1.17.0

**Reviewed:** 2026-08-15T05:59:05Z
**Depth:** deep (release-commit full scope: bcd32af + tag v1.17.0 + GitHub Release)
**Files Reviewed:** 10 (release commit contents)
**Status:** issues_found (3 MINOR, 0 BLOCKER, 0 MAJOR)
**Verdict:** PASS_WITH_NOTES

## Summary

Phase 5 shipped v1.17.0 as release commit `bcd32af` (10 files, +76/-14), annotated tag
`v1.17.0`, and GitHub Release `v1.17.0`. Every contract in scope was independently
re-verified — not by trusting the implementer's summary, but by re-running the gate and
re-deriving each claim from the working tree and git history.

### Verification evidence (all independently reproduced)

| # | Check | Result |
|---|-------|--------|
| 1 | `python tooling/check_release.py` | PASS, exit 0 (re-run at review time) |
| 2 | Version single-source, 11 surfaces | plugin.json x2, RELEASE-INFO, README badge+prose x2, docs/index.html REV x2, docs/packs.html REV, website YAMLs x2, CHANGELOG top — all 1.17.0; only 1.16.3 remnant is the CHANGELOG history heading `## [1.16.3]: 2026-06-26` (legitimate) |
| 3 | CHANGELOG format | `## [1.17.0]: 2026-08-15`, Added/Fixed/Changed sections, 0 em dashes, 0 URLs in entry, no link-ref defs (matches house style — none exist for any version) |
| 4 | Chapter counts vs PACK.yaml | 8/6/5/7/9/8/7/6 (nist-800-171, nist-800-61, cisa-cpg, doe-sem, mil-hdbk-338, mil-hdbk-516, nasa-ms-7009, doe-413-3b) — each matches its `packs/<slug>/PACK.yaml` `chapters:` field exactly |
| 5 | README badge/table | Badge `packs-54`; table has 54 live rows + 1 planned (`mit-ocw-se`); 8 new rows present with chapter counts matching PACK.yaml |
| 6 | PACK-SPEC addendum | `docs/PACK-SPEC.md:33` — `## When to use` + `**Prerequisites:**` is now the first body-order item (RR-S-13) |
| 7 | docs/packs.html freshness (§5c) | Gate regenerates from SKILLS.md and byte-compares — PASS; new pack slugs present in the generated catalogue |
| 8 | No source URLs introduced | `git show bcd32af` added URLs are only `github.com/jgsystemsconsulting/...` and the shields.io version badge — zero SOURCE_HOSTS matches |
| 9 | Untracked user files excluded | `git show --name-only bcd32af` = exactly the 10 release-surface files; pptx files, `docs/capability-pack-map.*`, `docs/ROLE-AGENTS-REQUIREMENTS-V2.md` remain untracked |
| 10 | Tag | `git tag -l -n3 v1.17.0` → annotated (cat-file type `tag`), message `v1.17.0: 8 Tier-1 public-domain packs (54 +2 signposts)` (colon style matching v1.16.3), points at `bcd32af`, pushed to origin (`git ls-remote` confirms) |
| 11 | GitHub Release | `gh release view v1.17.0 --json name,tagName` → `{"name":"v1.17.0 — 8 Tier-1 public-domain packs","tagName":"v1.17.0"}`; notes are CHANGELOG-derived with intro prose, URL-free |
| 12 | Catalog basis (SC-1) | `catalog.json` packs = 54; `packs/` dirs = 56; SKILLS.md entries = 54 (gate); cursor manifest 55 = 56 dirs − 1 non-commercial (`packs/sebok` commercial_use: false) — CHANGELOG's "55 eligible skills" is arithmetically correct |
| 13 | 8 packs on surfaces | catalog.json:1, SKILLS.md:1, NOTICE:2, packs.html present, cursor manifest present per pack |

### Structural Findings (fallow)

None supplied for this phase.

## Narrative Findings (AI reviewer)

### BLOCKER

None.

### MAJOR

None.

### MINOR

#### MI-01: CHANGELOG overstates index.html as a pack "registration" surface

**File:** `CHANGELOG.md` (1.17.0 entry, Changed section — "Registered the 8 packs on every
surface: catalog.json, SKILLS.md, docs/packs.html, NOTICE, README badge, docs/index.html,
Cursor manifest")
**Issue:** `docs/index.html` is a landing page with no pack enumeration (no pack slugs
appear in it; it links to packs.html as "Browse the catalogue"). The release commit only
bumped its two REV spans 1.16.3 → 1.17.0. Listing index.html among surfaces where packs
were "registered" is factually imprecise in a shipped public artifact and could mislead
anyone auditing release completeness.
**Fix:** In the next CHANGELOG entry (do not rewrite published history for this), or via
the release notes if ever regenerated, drop `docs/index.html` from the registered-surfaces
list or reword to "version surfaces bumped (incl. docs/index.html REV)".

#### MI-02: Post-release working tree carries uncommitted workflow state

**File:** `.planning/master_flow_state.json`, `.planning/phases/5-release-surface-v1-17-0/master_flow_state.json`
**Issue:** Both files are modified-uncommitted, plus 3 untracked user files under `docs/`.
These were correctly kept out of the release commit (verified), and the untracked docs/
files are recorded as accepted residuals in STATE.md. Noted so the next phase does not
accidentally sweep them into a commit via `git add docs/` or `-A` — the summary itself
established the explicit-path-only staging rule for exactly this reason.
**Fix:** No release action. Keep explicit-path staging; commit or discard the two state
files with the next planning commit as usual.

#### MI-03: GitHub Release title em dash is a documented exception, not a defect

**File:** GitHub Release v1.17.0 title (`v1.17.0 — 8 Tier-1 public-domain packs`)
**Issue:** The repo enforces em-dash-free CHANGELOG and packs.html, and the annotated tag
uses colon style — but the release title carries an em dash. This matches the v1.16.3
release title convention (`v1.16.3 — RR-S-13 compliance + browsable pack reference`) and is
recorded as house style in STATE.md ("GitHub Release title keeps em-dash house style").
Recorded here only so future reviewers do not re-flag it; no action required.
**Fix:** None (intentional, consistent with v1.16.3).

## Verdict

**PASS_WITH_NOTES** — REL-01 and REL-02 are satisfied and mechanically verified: gate
PASS at 54/56 basis, all 11 version surfaces at 1.17.0, chapter counts live from PACK.yaml,
README badge/table agreement restored, PACK-SPEC addendum present, packs.html
gate-identical, no source URLs, no user files leaked into the release commit, annotated
tag on origin, GitHub Release published. The three findings are MINOR record-keeping
notes; none affects release correctness or requires a patch release.

---

_Reviewed: 2026-08-15T05:59:05Z_
_Reviewer: ZCode (gsd-code-reviewer, deep mode)_
_Depth: deep_
