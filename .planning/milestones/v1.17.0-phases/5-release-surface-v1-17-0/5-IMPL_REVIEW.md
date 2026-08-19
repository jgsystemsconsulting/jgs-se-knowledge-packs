# Phase 5: Implementation Review — Release Surface v1.17.0

**Reviewed:** 2026-08-14
**Scope:** release commit bcd32af + planning commits fab28bd, d99c348 vs 5-01-PLAN.md
**Verdict:** PASS_WITH_NOTES

## Verification Performed (live, not commit-message trust)

| Check | Result |
|---|---|
| 11 version surfaces bumped 1.16.3 → 1.17.0 | VERIFIED — plugin.json:4, .cursor-plugin/plugin.json, RELEASE-INFO.txt (Version/Tag/Staged 2026-08-15T05:46:56Z), README badge/line 58/line 207, docs/index.html REV x2, docs/packs.html, both website YAMLs; `grep 1\.16\.3` outside .planning/packs/ returns only CHANGELOG history heading `## [1.16.3]: 2026-06-26` |
| CHANGELOG chapter counts 8/6/5/7/9/8/7/6 | VERIFIED against live `packs/<slug>/PACK.yaml chapters:` for all 8 packs — exact match (nist-800-171=8, nist-800-61=6, cisa-cpg=5, doe-sem=7, mil-hdbk-338=9, mil-hdbk-516=8, nasa-ms-7009=7, doe-413-3b=6); MA-01 research-draft correction applied |
| Entry hard constraints | VERIFIED — zero em dashes, zero URLs in the `## [1.17.0]: 2026-08-15` entry; entry sits above the 1.16.3 heading; structure matches research §2 (Added/Fixed/Changed + "Catalogue now 54 packs (+2 signposts).") |
| PACK-SPEC addendum | VERIFIED — body-order list now leads with `## When to use` + `**Prerequisites:**` naming RR-S-13 and check_release.py enforcement; remaining items and order untouched (2-line diff) |
| README +8 table rows | VERIFIED — 8 new live rows inserted between `faa-rma` and planned `mit-ocw-se`, chapter counts in rows match PACK.yaml; resolves the badge/table mismatch (MI-02) |
| README doe-413-3b framing line | VERIFIED — em-dash-free prose line adjacent to the table; slug unchanged everywhere (`catalog.json` untouched) |
| No untracked user files committed | VERIFIED — bcd32af touches exactly 10 intended files; docs/ROLE-AGENTS-REQUIREMENTS-V2.md and capability-pack-map.{md,json} absent from all three commits |
| Gate + idempotency | VERIFIED — live run: `check_release.py` exit 0 printing `RELEASE CHECK: PASS`; `gen_packs_page.py` re-run leaves docs/packs.html with empty diff (byte-identical) |
| Tag / release / commit ordering | VERIFIED — annotated tag v1.17.0 (`v1.17.0: 8 Tier-1 public-domain packs (54 +2 signposts)`, colon style) points at bcd32af; pushed to origin (ls-remote shows tag + `^{}` deref); GitHub Release v1.17.0 exists with the CHANGELOG-derived body; bcd32af is the last content commit — fab28bd/d99c348 touch only `.planning/` |
| Task 7 records | VERIFIED — STATE/MILESTONES/ROADMAP updated, 5-01-SUMMARY.md created |

## Findings

### MINOR-01: plugin.json gained an unrelated trailing-newline-at-EOF change

**File:** `.claude-plugin/plugin.json` (bcd32af)
**Issue:** Beyond the version line, the commit also adds a missing final newline to the file (old blob ended `-}` with "No newline at end of file"). Cosmetic and harmless, but it is an out-of-plan edit inside the release commit.
**Fix:** None required; note for history.

### MINOR-02: planning commit expanded scope beyond Task 7 file list

**File:** `.planning/REQUIREMENTS.md` (fab28bd)
**Issue:** Task 7 lists STATE.md, MILESTONES.md, ROADMAP.md (plus the SUMMARY output). fab28bd additionally edits REQUIREMENTS.md. Content-wise consistent with the shipped record and still `.planning/`-only, so the "last content commit" invariant holds — but it is undeclared scope in the plan.
**Fix:** None required; record in retro.

### MINOR-03: README framing-line placement deviates from plan letter

**File:** `README.md` (bcd32af)
**Issue:** Plan specified the doe-413-3b line "immediately after the last live row (~155), before the planned `mit-ocw-se` row"; it landed after the mit-ocw-se row instead. Still adjacent to the table and functionally correct.
**Fix:** None required.

## Summary

The diff matches the plan faithfully: all 11 version surfaces at 1.17.0, CHANGELOG entry with correct PACK.yaml-sourced chapter counts (the MA-01 correction applied, not the research draft's wrong uniform "(8 ch)"), PACK-SPEC addendum, README +8 rows plus the framing line, gate PASS with byte-identical packs.html regeneration, annotated tag and GitHub Release published, and no untracked user files crossed into any commit. Only three MINOR notes, none blocking.

_Reviewer: adversarial implementation review (diff-scope)_
