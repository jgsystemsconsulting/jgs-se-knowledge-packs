---
phase: 3-tier-1-packs-public-domain
reviewed: 2026-08-14T23:39:17Z
depth: deep
files_reviewed: 8
files_reviewed_list:
  - .planning/phases/3-tier-1-packs-public-domain/3-01-PLAN.md
  - .planning/phases/3-tier-1-packs-public-domain/3-02-PLAN.md
  - .planning/phases/3-tier-1-packs-public-domain/3-03-PLAN.md
  - .planning/phases/3-tier-1-packs-public-domain/3-RESEARCH.md
  - .planning/phases/3-tier-1-packs-public-domain/3-PLAN_CHECK.md
  - .planning/ROADMAP.md
  - docs/PACK-SPEC.md
  - catalog.json
findings:
  critical: 0
  blocker: 0
  major: 3
  warning: 8
  info: 0
  total: 11
status: issues_found
---

# Phase 3: Plan Review (pre-execute, plans as of ffc3caf)

**Verdict:** APPROVE_WITH_NOTES

**Reviewed:** 2026-08-14T23:39:17Z
**Depth:** deep (plans cross-checked against live tooling code, live catalog/SKILLS/NOTICE, and the external jgs-reference-skill repo)
**Plans:** 3-01 (Batch A: nist-800-171, nist-800-61, cisa-cpg, doe-sem), 3-02 (Batch B: mil-hdbk-338, mil-hdbk-516), 3-03 (Batch C: nasa-ms-7009, doe-413-3b + consolidated registration sweep)

## Summary

The remediated plans are executable and their closing gate is wired correctly. Every
load-bearing mechanical claim was re-verified against live code, not just docs:

- **Licence strings / P3-PRE-1:** ran `vet_source.classify()` live on all 8 build-sheet
  title/publisher/licence triples — all 8 return `excluded: False, tier: 1`. The cisa
  statute-bearing string works because `PD_LICENSE` matches on the licence string
  regardless of publisher (`US_GOV` indeed lacks `cisa`). The DoD Distribution Statement A
  variant and the DOE `"department of "`/NASA signals also classify tier 1. No planned
  title/publisher accidentally trips an `EXCLUDED` substring.
- **Registration sweep (post-B1 remediation):** catalog is repo-root `catalog.json`
  (46 entries, 42 tier-1 measured) → plan's `==54` / `==50` assertions are arithmetically
  correct; no slug collisions with the 48 live pack dirs. The prescribed backtick-slug
  SKILLS.md row parses in both `gen_packs_page.parse_skills` and check_release's
  `\[`([^`]+)`\]\(packs/` index regex; header bump 46→54 matches live SKILLS.md:9.
  `gen_skills_index.py` is confirmed absent (hand-edit claim correct).
- **rr-s-13 contract:** check_release.py 5b requires `^##\s*When to use\s*$` + a
  Prerequisites/Requirements marker; every generate step now mandates
  `## When to use` + `**Prerequisites:**`, matching live `packs/nist-csf/SKILL.md:11-14`.
- **Pipeline flags:** extract.py (via `book_to_skill.utils`) accepts
  `--mode technical|text --install-missing ask|yes|no`; outline.py has
  `--source/--out`; REF build_pack.py has `--slug/--title/--publisher/--version/--license/--out-dir`.
  check_overlap exits 3 on verbatim runs / 0 clean, so the `&&` verify chains fail correctly.
- **OCR contingency:** matches real tool behavior — `looks_image_only()` raises
  ExtractionError with the exact `ocrmypdf` hint the plan's fallback prescribes.
- **Leak safety:** `.gitignore` lines 12/13/17 ignore `**/.build/`, `*.full_text.txt`,
  `sources/`; NOTICE `[pack: ...]` block format confirmed (46 live blocks).
- **Em dash:** `gen_packs_page.deslop()` strips em dashes from SKILLS rows, so the DoD
  licence string's em dash cannot break rr-b-30 (which checks packs.html only).
- **Plugin manifests** don't enumerate packs — the 4-file sweep is the right registration
  surface for catalog/SKILLS/packs.html/NOTICE.

No blockers. Three majors are containment/surface gaps that do not turn any gate red but
should be patched into the plans (small edits) before or during execute. Batches A and C
may start immediately; the Batch B majors should be folded in before 3-02 runs.

## Blockers

None.

## Major

### MJ-01: Registration sweep misses two shipped surfaces that hardcode the pack count — README badge and docs/index.html

**File:** `3-03-PLAN.md:7-14` (files_modified), `3-03-PLAN.md:148-184` (Task 3); live `README.md:11`, `docs/index.html:196`
**Issue:** The sweep covers catalog.json / SKILLS.md / docs/packs.html / NOTICE, but two
shipped surfaces also hardcode counts: README.md:11 carries a `packs-46` badge, and
docs/index.html §06 hardcodes `46 packs · 2 signposts` plus per-publisher group counts
(NASA 14, DoD 11, NIST 7, FAA 6, GAO 4, EU/academic 4). After +8 (NASA +1, DoD +2, NIST +2,
plus new DOE and CISA groups) both go stale. Neither is in files_modified, `check_release.py`
does not verify either count (README: header/SPDX only; index.html: not checked at all), and
nothing in Phase 5's SCs names these two paths — so no mechanical gate ever catches the drift.
**Fix:** Add `README.md` (badge 46→54) and `docs/index.html` (§06 counts and groups) to
3-03 Task 3 files/action/verify — or record an explicit named deferral to Phase 5 for exactly
these two paths with a grep assertion there (`grep -c "packs-54" README.md`,
`grep -c "54 packs" docs/index.html`).

### MJ-02: T-3B-01 (high, mirror tampering) mitigation is only half-tasked — mirror provenance never recorded

**File:** `3-02-PLAN.md:147` (threat register) vs `3-02-PLAN.md:77-84, 103-106` (Task 1 action/verify/done)
**Issue:** The STRIDE register promises "record mirror used in PACK.yaml notes" for the
untrusted-mirror trust boundary (nde-ed.org fallback for a token-gated DLA original), but no
task action, done criterion, or verify instructs or checks that record. The only in-copy
verification tasked is "a Distribution Statement A page appears" — a weak provenance
heuristic for a HIGH-severity tamper threat. There is also no page-count cross-check of the
mirrored copy against the DLA record (~716 pp for 338B) that the research cites.
**Fix:** In both 3-02 task actions add: "record the download source actually used
(DLA vs mirror URL name — URL itself stays out of pack files) and the metadata.json page
count cross-checked against the DLA-record page count in PACK.yaml notes"; add
`grep -c "mirror\|DLA" packs/mil-hdbk-338/PACK.yaml` (and 516) to the verifies.

### MJ-03: OCR trigger is abort-only — a partially scanned DoD PDF passes silently and makes the overlap gate vacuous

**File:** `3-02-PLAN.md:80-83` (Task 1 OCR contingency); reference behavior `jgs-reference-skill/book_to_skill/utils.py:664-668`
**Issue:** The OCR fallback fires only "if extraction aborts as image-only". The tool's
`looks_image_only()` inspects only the *first pages*; a mixed PDF (born-digital front
matter, scanned body — plausible for a 1998 handbook fetched from a third-party mirror)
does not abort and yields partial text. `count_pages()` then reports full page count for
PACK.yaml regardless of extracted text, so provenance looks fine, and `check_overlap` runs
against a truncated full_text.txt — an empty/garbage source cannot overlap anything, so the
licence-safety gate passes vacuously while chapter content is built from a holey text.
**Fix:** For both 3-02 packs, add a post-extract sanity check before outline:
chars-per-page (or metadata tokens) floor, e.g. mean extracted characters per counted page
≥ ~1,000 (typical born-digital handbook density); below it, treat as scanned → run the OCR
fallback and record it. One python one-liner against full_text.txt + metadata.json.

## Minor

### MN-01: (carried W5) 3-01 Task 1 leak check assumes the pack commit is HEAD, and is the only leak check in the phase

**File:** `3-01-PLAN.md:96`
**Issue:** `git show --name-only --pretty=format: HEAD` is meaningless if verify runs
before the step-8 commit or another commit lands in between; the other seven pack tasks
have no sources/ leak check at all (threats T-3A-03/T-3B-02/T-3C-03 all rely on it).
**Fix:** Check the named commit (`git show --name-only --pretty=format: <pack-commit>`)
after commit, or verify the working tree + `git status --porcelain sources/` emptiness in
every pack task.

### MN-02: (carried W1 residual) SC3 provenance (source_pages / chapters / built_on) is never mechanically verified

**File:** all pack verifies (e.g. `3-01-PLAN.md:96,109,135,163`); cause: `tooling/validate_pack.py` `parse_simple_yaml` deliberately skips nested `build:` keys (verified in code)
**Issue:** Only `! grep -q "TODO" PACK.yaml` checks provenance; ROADMAP Phase 3 SC3 rests
entirely on done-criteria prose.
**Fix:** Add one YAML-key grep per pack verify (e.g. `grep -q "source_pages: [0-9]"` and
`grep -q "built_on:"`), or a 3-line python check of the nested keys.

### MN-03: (carried W4) Estimates over the 100k smart-zone; 3-01 at 4 tasks; confidence low

**File:** `3-01-PLAN.md:14-18` (140k/1.40x), `3-02-PLAN.md:12-17` and `3-03-PLAN.md:12-17` (120k/1.20x)
**Issue:** Advisory only; the research-justified 3-batch split is the right shape.
**Fix:** None required; if Batch A blows context, split 2+2 after the nist-800-171
reference run (as both PLAN_CHECK and the plans' own contingency note).

### MN-04: cisa-cpg dual-source outline/merge step is underspecified relative to nasa-ms-7009

**File:** `3-01-PLAN.md:124-131`
**Issue:** Task 3 says "extract each, sum pages" and gives chapter topics, but unlike
3-03 Task 1 (which says "OUTLINE each; build ONE pack; primary spine = STD, second doc =
depth chapters"), it never says to outline both PDFs or how the two documents map onto the
4-6 chapter spine. A fresh agent may outline only the main report and never slice the
controls-list PDF.
**Fix:** Add one sentence mirroring the nasa variation: "OUTLINE both; main report is the
primary spine, controls-list slices feed the IT/OT goals and defining-objectives chapters."

### MN-05: work_dir.txt write mechanism unpinned — a PowerShell-redirected file breaks every later verify

**File:** `3-01-PLAN.md:87` (convention definition, reused by all plans)
**Issue:** The research suggests PowerShell for downloads; a `powershell ... > work_dir.txt`
redirect emits UTF-16/CRLF on Windows, and `$(cat sources/<slug>/work_dir.txt)` then yields a
garbled path so outline/overlap/verify all fail (or worse, quietly test the wrong path).
The plan says "one line, no trailing newline needed" but not how to write it.
**Fix:** Pin the write: `printf '%s' "<work-root>" > sources/<slug>/work_dir.txt` from bash,
and/or read with `WRK=$(tr -d '\r\n' < sources/<slug>/work_dir.txt)` in the verifies.

### MN-06: 3-02 claim_verification row "pipeline order identical to Plan A" contradicts Task 1's deliberate reorder

**File:** `3-02-PLAN.md:64` (claim VERIFIED) vs `3-02-PLAN.md:77-84` (extract precedes vet)
**Issue:** Task 1 intentionally runs EXTRACT before VET to surface the OCR risk early — a
justified deviation (build_pack re-runs the vet gate; nothing is generated pre-vet), but
the claim table asserts identity, which misinforms a future auditor re-verifying claims.
**Fix:** Reword the claim row to "pipeline steps identical; Batch B intentionally extracts
before vet (OCR-risk-first), vet still gates scaffold via build_pack."

### MN-07: Task 3's 8-slug SKILLS grep asserts any-match, not count==8

**File:** `3-03-PLAN.md:181`
**Issue:** `grep -cE '^\| \[`(…|…)`\]'` exits 0 on one match. Backstopped by
check_release §6 (SKILLS entry count == shipped pack count), so not gate-breaking.
**Fix:** `N=$(grep -cE …); [ "$N" -eq 8 ]` for a direct proof.

### MN-08: docs/PACK-SPEC.md omits the `## When to use` + Prerequisites body contract that rr-s-13 enforces

**File:** `docs/PACK-SPEC.md:28-40` (body-order list) vs `tooling/check_release.py` §5b; bridged per-task at `3-01-PLAN.md:90` et al.
**Issue:** ROADMAP SC1 says packs "conform to docs/PACK-SPEC.md", but the spec's SKILL.md
body order has no When-to-use/Prerequisites section while the release gate requires one on
every content pack. The plans bridge this by restating the contract in every generate step
(and pointing at packs/nist-csf as exemplar), so Phase 3 is covered — but the spec/gate
divergence remains a trap for any future pack built from the spec alone.
**Fix:** Add a one-line spec addendum task to 3-03 Task 3 or Phase 5 docs sync: PACK-SPEC
body order gains `## When to use` (+ Prerequisites line) as the first body section.

---

_Reviewed: 2026-08-14T23:39:17Z_
_Reviewer: ZCode (gsd plan reviewer)_
_Depth: deep_
