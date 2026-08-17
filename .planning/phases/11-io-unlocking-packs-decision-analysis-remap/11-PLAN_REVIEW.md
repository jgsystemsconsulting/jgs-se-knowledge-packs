# Phase 11 Plan Review — 11-01-PLAN.md + 11-02-PLAN.md

**Reviewed:** 2026-08-17
**Depth:** deep (plan vs live tree: ROADMAP Phase 11 SC-1..SC-5, REQUIREMENTS IO-01..07, SOURCE-VETTING Phase 11 handoff, 11-RESEARCH recommended shape + Patterns 1–6, 11-PLAN_CHECK, 11-VALIDATION, analog 10-PLAN_REVIEW / 7-PLAN_REVIEW; live re-run of every claim_verification row; `bash -n` + pre-phase execute of every `<automated>` block)
**Plans:** `.planning/phases/11-io-unlocking-packs-decision-analysis-remap/11-01-PLAN.md`, `11-02-PLAN.md`
**Plan check:** 11-PLAN_CHECK.md — PASS_WITH_FIXES (0 blockers, 5 warnings)
**Files reviewed:** both plans against locked GO/NO-GO + live pack/catalog/map surfaces

**Verdict:** PASS_WITH_FIXES

The two waves will move the poorest primaries without silent ticks if the executor follows the actions: build `nasa-std-8719-14` + `is-gps-200n`, extend `dod-vva-rpg` (or honestly defer), write the IO-01 remap table only, record AAF deferrals and stakeholder accept, thin-register the two new slugs. No map JSON edit, no Army CBA / AAF / stakeholder / SP-7084 must-build, no IS-300, no URL/source leak. Unlike Phase 7, no automated gate is invalid bash and no success criterion is missing. What keeps this off APPROVE is the same class as Phase 10 MJ-01..03: two automated blocks can green-light incomplete work that the acceptance lines already require. Fixes are one-line verify rewrites — no redesign, no split, no verdict changes.

---

## Findings

### MJ-01 [MAJOR] 11-02 Task 1 verify is not one `&&` chain; leftover `ch1*.txt` hides new-chapter overlap

**File:** 11-02-PLAN.md, Task 1 `<verify><automated>`
**Issue:** The block is `validate && chapters>10 && … && python chapters>10 && REF="…"; for f in sources/dod-vva-rpg/chapter_fulltexts/ch1*.txt; do …; done && leak && map`. The semicolon after `REF=` starts a new command. Chapter-count failure therefore does **not** stop the `for` / leak / map tail.

Live this session:

- `ls packs/dod-vva-rpg/chapters | wc -l` = 10; PACK.yaml `chapters: 10` → both `> 10` asserts fail (good, distinctive).
- `sources/dod-vva-rpg/chapter_fulltexts/ch01.txt`–`ch10.txt` already exist (Phase 7 leftovers). Glob `ch1*.txt` matches those ten files, not “new chapters only”.
- Exact pre-phase run: validate_pack PASS, then `REF` is skipped, the loop invokes `"$REF/tools/check_overlap.py"` as `/tools/check_overlap.py` → `C:\Program Files\Git\tools\check_overlap.py` missing. This tree fail-closes by accident.
- On a tree **without** leftover extracts, the glob is a literal non-file, `[ -f ] || continue` no-ops, leak/map are empty, **overall exit 0** despite chapters still 10. That is a false green on a sloppy no-extend **and** on the authorized IO-02 deferral path (action + acceptance already allow count 10 + DEFERRED).

Even on the happy path, leftover `ch01`–`ch10` make overlap succeed without a new `ch11.txt`. Stub `ch11` with no extract / no P7-PRE-4 notes still passes the mechanical block.

**Fix:** (1) `REF=…;` **first**, then one `&&` chain — no semicolon mid-gate. (2) Either-or the `>10` asserts with `grep IO-02 … DEFERRED` and `test ! -d packs/dodm-5000-102` (11-PLAN_CHECK W1). (3) Overlap only `ch11.txt` / `ch12.txt` / `ch13.txt` (or require at least one `ch1[1-9].txt` when not deferred). (4) Grep new-chapter P7-PRE-4 provenance (title + date / Checklist / TEVV), not just `! TODO`.

### MJ-02 [MAJOR] 11-02 Task 2 DEFERRED/ACCEPT greps are single-hit

**File:** 11-02-PLAN.md, Task 2 `<verify><automated>`
**Issue:** Acceptance requires dated DEFERRED on **both** IO-05 and IO-06, and dated ACCEPT on IO-07. The automated block is `grep -n "DEFERRED"` and `grep -n "ACCEPT"` — exit 0 on one match. One IO-05 parenthetical greens IO-06; an ACCEPT anywhere greens IO-07. Checkbox tests (`grep -c '^- \[ \] **IO-0X**' = 1`) correctly keep boxes open. Chapter-name tokens (`ch04-uncertainty-and-sensitivity` / `ch06-reporting-and-decision-use` / `ch06-accreditation-agent-role`) are absent today and do distinguish the remap pointer. Same class as 10-PLAN_REVIEW MJ-03 / 11-PLAN_CHECK W2.

**Fix:** bind per ID: `grep IO-05 | grep DEFERRED`, `grep IO-06 | grep DEFERRED`, `grep IO-07 | grep ACCEPT` (and keep the open-box counts).

### MN-01 [MINOR] map-untouched check is working-tree `git diff`, not commit-scoped

**Files:** 11-01 T1/T2, 11-02 T1/T2/T3
**Issue:** After a commit that included `docs/capability-pack-map.json`, `git diff --name-only -- docs/capability-pack-map.json` is empty. `files_modified` already excludes the map, so this is a backstop hole, not a planned steal.
**Fix:** also `test -z "$(git show --name-only --pretty=format: HEAD | grep capability-pack-map.json)"` on each scoped commit (same shape as the `sources/` leak check). 11-PLAN_CHECK W3.

### MN-02 [MINOR] When-to-use / Prerequisites are count-only

**Files:** 11-01 T1/T2, 11-02 T1
**Issue:** `grep -c '^## When to use'` and `grep -c '^\*\*Prerequisites:\*\*'` do not assert adjacency. Live analogs (`nasa-ms-7009`, `faa-std-025`, `dod-vva-rpg`) put body text between the heading and `**Prerequisites:**`. Action requires “immediately followed”. `check_release.py` RR-S-13 also accepts a non-adjacent Prerequisites marker.
**Fix:** python/awk: heading line + next non-empty line is `**Prerequisites:**`.

### MN-03 [MINOR] 11-VALIDATION.md Per-Task map omits thin-register

**File:** 11-VALIDATION.md
**Issue:** Rows cover 11-01-01/02 and 11-02-01..03. 11-02 Task 3 (`check_release` / catalog 63 / plugin 1.18.0) is missing. Nyquist 8a–8d still pass (every task has automated verify).
**Fix:** add 11-02-04. 11-PLAN_CHECK W4.

### MN-04 [MINOR] 11-RESEARCH.md Open Questions not marked RESOLVED

**File:** 11-RESEARCH.md Open Questions
**Issue:** No `(RESOLVED)` suffix and no inline RESOLVED markers. All four items already have Recommendations the plans implemented (thin-register; chapters-not-a-pack + DoDM deferral; Checklist + ≤2 at execute; fetch-fail → partial deferral).
**Fix:** retitle Open Questions (RESOLVED) and prefix each item RESOLVED with the chosen path. Do not reopen. 11-PLAN_CHECK W5.

### MN-05 [MINOR] 11-01 verify does not pin chapter-count bands

**Files:** 11-01 T1/T2
**Issue:** Acceptance wants 6–7 (8719) and 5–6 (GPS exemplar). `validate_pack.py` only requires ≥1 `ch*.md`. A one-chapter stub still exits 0.
**Fix:** `test "$(ls packs/<slug>/chapters | wc -l)"` inside the documented band.

### MN-06 [MINOR] 11-02 T1 does not measure chars/page on new RPG chapters

**File:** 11-02 T1
**Issue:** Action + must_haves require ≥300 per new PDF. 11-01 automates the floor; 11-02 T1 does not. Phase 7 leftover extracts already exist for ch01–ch10 only — a thin Checklist extract would not be caught.
**Fix:** same python chars/page line against each new `work_dir_ch1[1-9].txt` / `chapter_fulltexts/ch1[1-9].txt` when not deferred.

### MN-07 [MINOR] write `work_dir.txt` as the copied `sources/<slug>` path

**Files:** 11-01 T1/T2 python chars/page
**Issue:** `python -c "…Path('$WRK'.replace(…))"` is double-quoted. A `%TEMP%` path with backslashes (`C:\Users\…`) becomes a Python `\U` escape and SyntaxError. Action already says copy `book_skill_work` under `sources/<slug>/` and `printf` that root.
**Fix:** executor writes the forward-slash `sources/<slug>` path (as the action implies). Optional: read the file inside python instead of interpolating.

---

## Verify-command re-run (this session)

All five `<automated>` blocks extracted verbatim. `bash -n` via `C:\Program Files\Git\bin\bash.exe` 5.3.15 (not WSL `/bin/bash`, which is missing here):

| Task | `bash -n` | Pre-phase execute | Distinguishes live tree? |
|---|---|---|---|
| 11-01 T1 | SYNTAX_OK | rc=1 (`sources/nasa-std-8719-14/work_dir.txt` missing) | Yes — pack absent; Internet Public / 8719.14C greps are new |
| 11-01 T2 | SYNTAX_OK | rc=1 (`sources/is-gps-200n/work_dir.txt` missing) | Yes — same plus faa-std-025 / DIST-A / SAIC / forbidden GPS slugs absent |
| 11-02 T1 | SYNTAX_OK | rc=1 (chapters=10, then leftover glob + unset `$REF`) | Yes on `>10` **if** the `&&` chain is kept intact. Tail after `;` is not gated (MJ-01) |
| 11-02 T2 | SYNTAX_OK | rc=1 (chapter-filename tokens absent; no DEFERRED/ACCEPT) | Yes on remap filenames + dated records; DEFERRED/ACCEPT not bound per ID (MJ-02) |
| 11-02 T3 | SYNTAX_OK | rc=1 (catalog assert: slugs missing, len 61≠63) | Yes. plugin `1.18.0` + packs-63 + `check_release` are distinctive |

No `2>/dev/null || echo 0`. No `|| true` feeding a comparison. No unquoted parenthetical (Phase 7 BL-01 class). `grep -c http docs/SOURCE-VETTING.md` as a bare command exits 1 on count 0; both plans correctly wrap it in `test "$(…)" = "0"`.

claim_verification live re-run (cwd repo root, 2026-08-17): branch `main`; 63 pack dirs; neither new slug; catalog 61; SKILLS `61 packs (+2 signposts)`; cursor 62 / version `1.18.0`; README `packs-61`; NOTICE 0/0 new blocks; analog trees have SKILL/PACK/LICENSE/chapters/glossary/patterns/cheatsheet; REF vet/outline/build_pack/scan/overlap + extract.py present; repo tooling present; `check_release.py` PASS; `grep -c http` SOURCE-VETTING = 0; `.gitignore:17` `sources/`; Phase 11 handoff heading line 168; map schema 2 / `1.18.0`; Decision Analysis 2/2, Interfaces 4/3, Ops/Maint 6/4, Validation 5/4, Opportunity 10/2; IO-01..07 all `- [ ]` with Phase 10 notes only; `dod-vva-rpg` 10 chapters / `source_pages: 283`; TEVV named as selection drop at PACK.yaml:42; no dodm/aaf/army-cba/sp-7084/is-gps dirs; federal-bca ch04+ch06 present, no Decision Analysis Topic Index row; dod-vva-rpg Decision analysis row line 76. Matches both plans. No invented replacements.

---

## Plan-check incorporation

All five 11-PLAN_CHECK warnings are in-scope as small edits (verify lines + two advisory stamps). No check finding requires a scope change, a new file outside `files_modified`, or renegotiating any verdict.

| Check finding | In-scope? | Covered by |
|---|---|---|
| W1 T1 verify cannot pass authorized IO-02 deferral | Yes — and worse: `;` + leftover `ch1*.txt` can false-pass on a clean sources/ tree | MJ-01 |
| W2 T2 DEFERRED/ACCEPT single-hit | Yes — rewrite greps | MJ-02 |
| W3 map-untouched is working-tree only | Yes — add `git show HEAD` | MN-01 |
| W4 VALIDATION.md omits thin-register | Yes — advisory row | MN-03 |
| W5 Open Questions unmarked | Yes — stamp only | MN-04 |

---

## Confirmed correct (checked, not raised)

- Verdict fidelity: 11-RESEARCH decision table maps 1:1 (IO-03/04 GO builds; IO-02 extend-or-defer; IO-01 table-only; IO-05/06 DEFERRED; IO-07 ACCEPT; SP-7084 skip). Wave A/B split matches recommended shape.
- ROADMAP SC-1..SC-5 and REQUIREMENTS IO-01..07 are all tasked. SC-1 live count leave-2 is correctly **not** a Phase 11 JSON contract (Pattern 4 / EDGE_ABSENT=1 / user brief). SC-2 Validation “new pack” was DoDM and stays deferred; depth moves via chapters.
- Locked prohibitions encoded in `files_modified`, must-NOT, and `test ! -d`: no Army CBA / AAF / stakeholder / `dodm-5000-102` / SP-7084 / IS-300 / ICD-GPS-153 / 705J / 800J / `gps-is-200n`. Map JSON never listed.
- P11-PRE-1 / P11-PRE-2 / P7-PRE-4 are hard gates before GENERATE. Tier 1 leaning is not skip-confirm.
- IO-01..07 boxes stay `- [ ]`. Thin-register does not bump plugin version, CHANGELOG, or tag REL-19-02. Version stays `1.18.0`.
- Link Policy: live `grep -c http docs/SOURCE-VETTING.md` = 0; URLs are research-store only; pack-tree `https?://` greps on both new packs + extended RPG.
- `sources/` gitignored; per-pack `git show` leak check on 11-01; Checklist PDF already present under gitignored `sources/dod-vva-rpg/pdfs/TEVVchecklist-pr.PDF` (and `extracts/ch11/`) so IO-02 need not block on a fresh DEBoK browser session.
- 11-02 `depends_on: ["11-01"]` is acyclic; thin-register waits for both new dirs. 11-01 stays on `main`. Idempotency: do not re-scaffold existing slugs (`build_pack.py` refuses).
- Registration arithmetic is correct against `check_release.py:160-210`: post-thin-register dirs 65 / catalog 63 / SKILLS 63(+2) / cursor 64 (sebok `commercial_use: false`) / README packs-63. Analog catalog keys match live objects (no invented `share_alike` on catalog rows).
- 11-01 90000 and 11-02 70000 are under the 100k smart-zone. Unclassified `.edge-coverage.json` probes left unresolved — no invented `check_kind` / `check_target`.
- 11-01 T2 extract-level DIST-A grep + SAIC watch-item mitigate the scaffold licence-string tautology (Phase 7 MA-02 class) for GPS.

---

## Recommendation

Tighten the two automated verify blocks (MJ-01, MJ-02) before execute so a no-extend `dod-vva-rpg` or a single DEFERRED parenthetical cannot go green. Stamp Open Questions / VALIDATION.md if convenient (MN-03/04) — not execute-blocking. No verdict changes, no scope changes, no re-plan. A quick re-check of the edited verify lines is sufficient after revision; a full re-review is not.

---

**Verdict:** PASS_WITH_FIXES

**blockers:** 0
**majors:** 2
**minors:** 7

Path: `.planning/phases/11-io-unlocking-packs-decision-analysis-remap/11-PLAN_REVIEW.md`

Two-wave plan covers every Phase 11 success criterion and every IO-01..07 ID. Actions match 11-RESEARCH. All five verify scripts are valid bash and fail closed on **this** tree. Advance after rewriting the 11-02 T1 chain (either-or deferral + new-chapter overlap only) and binding DEFERRED/ACCEPT to IO-05/06/07.
