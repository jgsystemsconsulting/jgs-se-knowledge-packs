---
phase: 9-release-surface-v1-18-0
reviewed: 2026-08-17T01:12:30Z
depth: deep
scope: impl (release commit d19be1a; tag v1.18.0; post-tag 7081649, 7e0de75, 98bd340)
files_reviewed: 12
files_reviewed_list:
  - .claude-plugin/plugin.json
  - .cursor-plugin/plugin.json
  - CHANGELOG.md
  - RELEASE-INFO.txt
  - README.md
  - docs/index.html
  - docs/packs.html
  - docs/products/website/01-jgs-se-knowledge-packs.yaml
  - docs/products/website/catalog.yaml
  - docs/capability-map-CONTRACT.md
  - docs/SOURCE-VETTING.md
  - .planning/phases/9-release-surface-v1-18-0/9-01-SUMMARY.md
findings:
  critical: 0
  blocker: 0
  major: 0
  minor: 1
  info: 1
  total: 2
status: issues_found
verdict: PASS_WITH_NOTES
---

# Phase 9 Impl Review (diff scope: release commit d19be1a + tag v1.18.0 + post-tag 7081649, 7e0de75)

**Verdict:** PASS_WITH_NOTES

No blockers, no majors. The release commit, annotated tag, GitHub Release, and
post-tag planning commits were each independently re-verified against the plan's
must_haves and Task 5/6 file lists. Every adversarial check below was executed
live against the working tree and the tag tree; none rely on SUMMARY assertions.

## What Was Adversarially Verified (evidence, not assertions)

### Release commit d19be1a — file set exactness

`git show --stat d19be1a` lists exactly the 11 files the plan's Task 5 mandates,
nothing more, no deletions:

| # | File | Delta |
|---|------|-------|
| 1 | .claude-plugin/plugin.json | 2 +1 -1 |
| 2 | .cursor-plugin/plugin.json | 2 +1 -1 |
| 3 | CHANGELOG.md | 68 pure insertions (numstat 68/0 — history untouched) |
| 4 | RELEASE-INFO.txt | 6 |
| 5 | README.md | 6 |
| 6 | docs/SOURCE-VETTING.md | 2 (OUSW → OUSD) |
| 7 | docs/capability-map-CONTRACT.md | 2 ("cluster 30" → cluster name) |
| 8 | docs/index.html | 4 (both REV spans) |
| 9 | docs/packs.html | 2 (REV span, generator-produced) |
| 10 | docs/products/website/01-jgs-se-knowledge-packs.yaml | 2 |
| 11 | docs/products/website/catalog.yaml | 2 |

No untracked strays crossed into the commit (T-9-01 mitigated as planned).

### 11 surfaces at 1.18.0 — working tree AND tag tree

Spot-checked `git show v1.18.0:<file>` against the working tree; both read
identically: plugin.json:4, cursor plugin.json:5, RELEASE-INFO.txt:3-4
(Version 1.18.0 / Tag v1.18.0 / Staged 2026-08-17T00:59:27Z), README.md:10
(badge version-1.18.0-green + alt text) / 58 / 224, docs/index.html:110 and 226
(both REV spans), docs/packs.html:86, catalog.yaml:13,
01-jgs-se-knowledge-packs.yaml:15.

Residual `1.17.0` sweep (excluding .planning/.git/sources) returns ONLY CHANGELOG
history (lines 66, 80, 106) plus exactly the 5 whitelisted historical doc lines:
capability-map-CONTRACT.md:54, capability-pack-map.md:16, SOURCE-VETTING.md:93,
144, 149. The 5 historical references were correctly left untouched.

### CHANGELOG 1.18.0 entry correctness

- `## [1.18.0]: 2026-08-17` sits above `## [1.17.0]: 2026-08-15`; exactly one occurrence.
- The doe-413-3b → doe-o-413-3 rename paragraph precedes the first `###` heading (leads, per REL-1x-02).
- Chapter counts re-read live from each packs/<slug>/PACK.yaml line 13:
  dote-te-guidebook=8, faa-std-025=6, federal-bca=6, dafman-63-119=7,
  mil-std-881f=7, mil-std-40051=8, dod-vva-rpg=10 — all seven "(N ch)" values in
  the entry match; intentionally non-uniform, so no copy error.
- Caveats present on exactly the three mandated packs: vva (~2011 internal dates
  in undated container), faa-std-025 (Rev F mirror vs ROSAP Rev E),
  mil-std-40051 (counters 1168 vs metadata 584).
- v1.17.0 wording fix present in Fixed (docs/index.html is a version surface,
  not a registration surface). Cursor manifest e00ac7d item present so the
  release notes are complete.
- Em dashes in entry: 0. En dashes: 0. `http` occurrences: 0 (link policy clean).
- No duplication of the 1.17.0 Changed `.planning/` scan-skip item; the 1.18.0
  Changed item ("Registered the 7 packs on every registered surface") correctly
  drops docs/index.html and does not restate any 1.17.0 Changed line.
- "Catalogue now 61 packs (+2 signposts)." closes the Added section.

### Carry-forward doc fixes (IN-01, OUSD)

- d19be1a diff for capability-map-CONTRACT.md shows exactly the one-clause change
  "cluster 30)." → "the Standards, Tailoring & Process Models cluster)." — zero
  `cluster 30` references remain in the CONTRACT.
- d19be1a diff for SOURCE-VETTING.md shows OUSW(R&E) → OUSD(R&E) in the GP-01 row
  only; zero `OUSW` occurrences remain in the file.

### Tag + release provenance

- Tag object cae0145 is a real annotated tag (type `tag`, tagger set), peels via
  `v1.18.0^{}` to d19be1a74635aa858ee0563029c7645892cf3bab; `git diff v1.18.0
  d19be1a` is empty (tag tree == release commit tree).
- Tag message is colon-style matching the v1.17.0 convention verbatim:
  `v1.18.0: 7 gap-driven Tier-1 packs (61 +2 signposts), capability map v2`.
- `git ls-remote --tags origin` shows both refs/tags/v1.18.0 and its peeled
  commit — the tag is on origin (REL-1x-02).
- Release commit is the last CONTENT commit on main: post-tag commits 7081649,
  7e0de75, 98bd340 each touch only `.planning/` files (verified via per-commit
  stats).
- Working tree has zero content drift vs the tag (`git diff v1.18.0 -- .
  ':!.planning'` empty) and `git status --short` is clean.

## Findings

### MI-01: Task 6 commit scope exceeded the plan's declared file list

**File:** `.planning/phases/9-release-surface-v1-18-0/9-01-SUMMARY.md:125`; commit 7081649
**Class:** MINOR
**Issue:** Plan Task 6 `files_modified` lists STATE.md, MILESTONES.md, ROADMAP.md only;
commit 7081649 also modified `.planning/REQUIREMENTS.md` (ticking REL-1x-01/02) and
added the SUMMARY itself. Both additions are correct and GSD-standard (REQUIREMENTS
ticking is the normal completion act; the SUMMARY is the plan's `<output>`), and the
SUMMARY's task table discloses the 5-file set honestly — but the Deviations table does
not list the file-set expansion, and "Files modified: 11 content (release) + 3
planning" undercounts the actual Task 6 commit (5 planning-scope files).
**Fix:** No code change. For future release phases, either include REQUIREMENTS.md and
the SUMMARY path in Task 6's `files_modified`, or add a one-row deviation noting the
planning-commit file set so the count reconciles.

### MI-02: Soft-reset provenance is unverifiable from history (observation)

**File:** `.planning/phases/9-release-surface-v1-18-0/9-01-SUMMARY.md:221-227`
**Class:** INFO
**Issue:** Deviation 1 / Auto-fixed Issue 1 describe intermediate Task 1-3 commits
soft-reset into the single release commit. The intermediate SHAs no longer exist on
main, so this cannot be independently re-verified — however the end state fully
matches the Phase 5 template invariant it was protecting (release commit is the sole
content delta before the tag), which IS verified above.
**Fix:** None needed; recorded as an accepted trust-the-SUMMARY item typical of the
squash-release pattern.

## Requirement Coverage Verdict

| Requirement | Check | Result |
|---|---|---|
| REL-1x-01 (SC1) | 11 surfaces version-consistent at 1.18.0 (tree + tag); dual gate PASS at 61/63 basis | VERIFIED (gate detail in 9-CODE_REVIEW.md) |
| REL-1x-02 (SC2) | annotated tag v1.18.0 on origin; GitHub Release with CHANGELOG-derived notes leading with the rename; wording fix present | VERIFIED |

**Verdict: PASS_WITH_NOTES** — ship the release as-is; both findings are
planning-record hygiene, not public-surface defects.

---
*Reviewed: 2026-08-17T01:12:30Z*
*Reviewer: gsd-code-reviewer (adversarial)*
*Depth: deep (diff scope)*
