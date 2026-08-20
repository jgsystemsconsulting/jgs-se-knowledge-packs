# Phase 15: Plan Review

**Reviewed:** 2026-08-20T10:10:24Z
**Reviewer:** gsd-code-reviewer (plan review mode)
**Plan:** `.planning/phases/15-source-retries/15-01-PLAN.md`
**Plan check:** `15-PLAN_CHECK.md` — Verdict PASS_WITH_FIXES (0 blockers, 4 warnings) — justified
**Research:** `15-RESEARCH.md` (host-200 for armypubs; plan overrides with ASAFM PDF 403)
**Patterns:** `15-PATTERNS.md` (Vetted-candidates insert is stale analog; plan correctly uses Not-cleared + Phase 16 handoff)
**Requirements SoT:** live `.planning/REQUIREMENTS.md` VET-20-01..03 + ROADMAP Phase 15 SC-1..4

---

## Summary

Single plan `15-01` is docs-only source-retry for VET-20-01 (FUT-04 Army CBA), VET-20-02 (AAF Product Support + Software pathway), VET-20-03 (optional ROSAP vs faa-std-025 Rev F). Three tasks: tracer FUT-04 fetch→store→register, AAF/ROSAP + Phase 16 handoff, REQUIREMENTS/STATE annotations without ticking boxes.

Plan does **not** invent packs/grants, tick VET/PACK as built, put scheme strings in SOURCE-VETTING, or skip evidence. Deferred-with-evidence is ROADMAP-legal default. Honest NO-GO handoff for Phase 16 is the intended done state.

What keeps this off plain APPROVE: Task 1 automated verify is **not executable** (tab IndentationError). Two more verify gates are weak against the pre-phase tree (same class as Phase 10 MJ-* weak gates). Fold MAJORs into executor brief; no redesign.

---

## Blocker gate (hard fails)

| Gate | Result | Evidence |
|------|--------|----------|
| Would invent packs / CBA / AAF pack? | PASS — forbidden | `files_modified` docs+planning only; prohibitions; T-15-03; `git diff --name-only -- packs/` empty required; no extract/build/catalog |
| Would invent redistribution grant? | PASS — forbidden | Grant path only if opened official PDF quote lands in 15-RESEARCH; 200 HTML / copyright footer explicitly not clearance; T-15-02/04 |
| Would tick live VET-20 / PACK-20 as built? | PASS — forbidden | Task 3 forbids; verify asserts three open VET-20 + three open PACK-20; ticks owned by verify / phase.complete |
| Would put `http` in SOURCE-VETTING? | PASS — forbidden | Link Policy in action + whole-file `http` ban in T1/T2/T3 verify; pointer names 15-RESEARCH only; T-15-01 |
| Claim verification present + load-bearing? | PASS | Non-empty `<claim_verification>` with live 2026-08-20 commands; executor told not invent replacements |
| VET-20-01..03 + ROADMAP SC-1..4 covered? | PASS | Frontmatter `requirements:` + Task 1/2/3 map 01 / 02+03 / annotations; SC-4 no-pack fenced all tasks |
| Skip dated evidence? | PASS — forbidden | must_haves require 2026-08-20 stamps; execute-day re-fetch into 15-RESEARCH; T-15-07 |

**BLOCKER count: 0**

---

## Spot-check (plan claims vs disk)

| Claim | Observed (this review) | Match |
|-------|------------------------|-------|
| Branch is main | `main` | Yes |
| `grep -c http docs/SOURCE-VETTING.md` | `0` | Yes |
| No 2026-08-20 stamp in register yet | `0` | Yes |
| Insert point Phase 11 then Def Stan | lines 168 / 179; no v1.19.1 retry heading | Yes |
| FUT-04 still 2026-08-17 DEFERRED | Not-cleared bullet + GP-06 A-94-only row | Yes |
| AAF Excluded-pending + unused sentence | Excluded table + Not-cleared bullet | Yes |
| faa-std-025 pack Rev F | `PACK.yaml` source_version Rev F; ROSAP rev E blocked at build | Yes |
| No army/cba/aaf/rosap pack dirs | none | Yes |
| VET-20-01..03 unchecked | three `- [ ]` | Yes |
| PACK-20-01..03 unchecked (Phase 16) | three `- [ ]` | Yes |
| Task 1 automated python compiles | `IndentationError: unexpected indent` (8 tab-prefixed lines) | Fail — MJ-01 |
| Task 2 / Task 3 automated compile | OK | Yes |
| 15-RESEARCH already has WarU 403 | Fresh Evidence 403 | Yes — weakens T1 `assert '403' in rs` (MJ-02) |

**RESEARCH vs plan (plan wins, correctly):**
1. RESEARCH Fresh Evidence curled armypubs host **200**. Plan claim_verification + Task 1 re-fetch ASAFM **PDF** → 403 Akamai. Plan already forbids treating host-200 as grant.
2. PATTERNS suggests `### Vetted candidates (v1.19.0 retry)` — wrong for uncleared sources. Plan uses Not-cleared + Phase 16 handoff (honest analog). Correct deviation.

---

## Findings

### BLOCKER

None.

### MAJOR (fold into executor brief)

1. **MAJOR — MJ-01: Task 1 automated verify does not compile (IndentationError)**  
   **File:** `15-01-PLAN.md` Task 1 `<verify><automated>` (lines ~186–193)  
   **Issue:** Eight lines after the Path reads are tab-indented. `python -c` payload raises `IndentationError: unexpected indent`. Execute verify cannot go green even when the FUT-04 action succeeded. Confirmed this review via `compile()`. Task 2/3 are clean column-0 style.  
   **Fix (executor brief):** Detab those eight lines to column 0 before or as first execute step. Do not wrap in a block. Same as 15-PLAN_CHECK W1.  
   **Fold:** Pre-execute one-line plan edit **or** executor detab-in-place then run verify.

2. **MAJOR — MJ-02: Task 1 verify `assert '403' in rs` already true; GP-06 dated suffix untested**  
   **File:** `15-01-PLAN.md` Task 1 `<verify><automated>`  
   **Issue:** 15-RESEARCH Fresh Evidence already records WarU PSM **403**. Acceptance also wants GP-06 still A-94-only with 2026-08-20 suffix, plus packs empty. A partial T1 that only touches RESEARCH with any 403 string (or skips GP-06 suffix) can still pass once MJ-01 is fixed. Heading-order + FUT-04 DEFERRED conjuncts do distinguish the register half.  
   **Fix (executor brief):** After detab, assert an ASAFM/FUT-04 execute-day marker in 15-RESEARCH; assert `2026-08-20` on the GP-06 table row; optionally `git diff --name-only -- packs/` empty. Same as W2.  
   **Fold:** Executor must still satisfy acceptance_criteria even if automated gate stays thin; SUMMARY claim transcript should show ASAFM PDF status + GP-06 suffix.

3. **MAJOR — MJ-03: Task 2 verify leans on pre-existing unused sentence; hard `NO-GO` count fights rare GO path**  
   **File:** `15-01-PLAN.md` Task 2 `<verify><automated>`  
   **Issue:** `NOT yet vetted — do not use` and Product Support Manager Guidebook already exist at v1.19.0 Excluded/Not-cleared lines. A skipped AAF bullet inside the new v1.19.1 section can still pass those greps. Phase 16 handoff heading is absent live (distinguishes). `sec16.count('| NO-GO —') == 2` breaks the action’s allowed quoted-grant GO exception (unlikely on planner 403 HEADs, but contract-inconsistent).  
   **Fix (executor brief):** Scope asserts to the v1.19.1 Not-cleared section containing both AAF and ROSAP + 2026-08-20; condition NO-GO vs GO on whether 15-RESEARCH contains a verbatim grant quote. Same as W3.  
   **Fold:** When executing Task 2, ensure new Not-cleared bullets + handoff table rows are real content, not heading-only stubs.

### MINOR

1. **MINOR — MN-01: 15-RESEARCH Army evidence is host-200; plan is PDF-403**  
   **File:** `15-RESEARCH.md` Fresh Evidence vs plan claim_verification  
   **Issue:** Stale on PDF path only; deferral decision unchanged. Plan is authoritative.  
   **Fix:** Optional RESEARCH stamp that publications host 200 ≠ Cost Benefit Analysis PDF clearance (still 403). Do not flip FUT-04. Same as W4. Out of critical path.

2. **MINOR — MN-02: PATTERNS Vetted-candidates / ROADMAP.md rows are stale analogs**  
   **File:** `15-PATTERNS.md`  
   **Issue:** Plan correctly ignores inventing a Vetted-candidates table and does not edit ROADMAP.md. No execute defect.  
   **Fix:** None required for execute.

3. **MINOR — MN-03: Task 3 does not assert STATE YAML frontmatter byte-stability**  
   **File:** `15-01-PLAN.md` Task 3  
   **Issue:** Action forbids touching `current_phase` / progress / completed_plans; automated verify only greps Phase 15 deviations bullet. Acceptance-only.  
   **Fix:** Optional; executor discipline + SUMMARY is enough.

---

## Coverage vs VET-20-01..03 + ROADMAP SC

| ID / SC | Live SoT intent | Plan delivery | Status |
|---------|-----------------|---------------|--------|
| VET-20-01 | Dated FUT-04 retry; grant or deferred; not silent tick | Task 1 tracer: re-fetch ASAFM PDF → 15-RESEARCH → Not-cleared + GP-06 suffix; no pack | COVERED |
| VET-20-02 | Quote grant or keep Excluded-pending / NOT yet vetted — do not use | Task 2: Excluded-pending + Not-cleared AAF bullet dated; no second Excluded row; no AAF pack | COVERED |
| VET-20-03 | Optional ROSAP vs faa-std-025 Rev F; document only; no forced rebuild | Task 2: ROSAP bullet + GP-02 one-liner; PACK.yaml untouched | COVERED |
| SC-4 | No pack this phase | All tasks + threat model + packs diff empty | COVERED |
| Annotate open boxes | VET-20 parentheticals; boxes stay open | Task 3; PACK-20 untouched (Phase 16) | COVERED |

---

## plan_check PASS_WITH_FIXES justification

| Dimension | Assessment |
|-----------|------------|
| Requirement coverage | All three VET-20 IDs in frontmatter + tasks; PACK-20 Phase 16 only annotated open |
| Task completeness | files / action / verify / done / acceptance; exact headings + insert point |
| Scope / prohibitions | No packs; no scheme strings; no VET/PACK ticks; pathspec commits; main only |
| Claim verification | Present, command-backed; file/git rows re-spot-checked true |
| Research conflict | Explicit plan-wins on ASAFM PDF 403 vs host-200 |
| Patterns | Link Policy / pointer / honest-deferral / dated-row / pathspec; correctly skips stale Vetted-candidates |
| Verification derivation | WARN justified — W1 compile break + W2/W3 weak conjuncts = MAJORs below, not blockers |

Checker 0 blockers / 4 warnings map 1:1 onto MJ-01..03 + MN-01. No hidden revision loop. No phase split.

---

## Executor-brief fold list (APPROVE_WITH_NOTES)

Copy into execute brief:

1. **Detab Task 1 automated block** (8 tab lines) so tracer verify can run — do this before relying on the gate.
2. **T1 evidence quality:** Record ASAFM **PDF** status (not just publications host); append GP-06 `v1.19.1 retry 2026-08-20` suffix; keep A-94-only wording.
3. **T2 section scope:** Put AAF + ROSAP bullets inside `### Not cleared this session (v1.19.1 retry)`; write full Phase 16 handoff table (default 2× NO-GO + document-only ROSAP). Do not treat pre-existing v1.19.0 unused sentence as Task 2 done.
4. **Never:** packs/, extract/build/catalog, `http` in SOURCE-VETTING, tick VET-20/PACK-20, invent grant from 200 HTML or copyright footer, `git add -A`.
5. **SUMMARY:** `## Claim verification` transcript + `## Deviations` (empty/None valid).

Optional (non-blocking): stamp 15-RESEARCH host-200 ≠ PDF clearance; tighten T2 asserts if editing the plan anyway.

---

## Execute readiness

- Branch: **main** (required)
- Tasks: 3 (tracer FUT-04 → AAF/ROSAP handoff → REQUIREMENTS/STATE)
- Expected commits (explicit pathspecs): SOURCE-VETTING + 15-RESEARCH (×2); REQUIREMENTS + STATE
- Live VET-20 / PACK-20 boxes stay open until phase.complete / verify
- Default expected verdicts (planner HEAD): ASAFM PDF 403, WarU 403 Cloudflare, AAF 301, ROSAP 403, guessed FAA Rev F 404 — all NO-GO / document-only unless execute-day opens a real PDF grant quote
- OneDrive: `git commit --no-verify` may timeout; check `git log --oneline -1` before retry

---

## Counts

| Severity | Count |
|----------|------:|
| BLOCKER | 0 |
| MAJOR | 3 |
| MINOR | 3 |
| **Total** | **6** |

---

**Verdict:** APPROVE_WITH_NOTES

_Reviewed: 2026-08-20T10:10:24Z_  
_Reviewer: gsd-code-reviewer (plan review mode)_  
_Blockers: 0 · Majors: 3_
