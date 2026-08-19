# Phase 6 Plan Review — 6-01-PLAN.md

**Reviewed:** 2026-08-14
**Depth:** deep (plan vs live tree: ROADMAP, REQUIREMENTS, STATE, SOURCE-VETTING, 6-RESEARCH, capability-gap-report, MILESTONES; live re-run of every verify command)
**Plan:** `.planning/phases/6-source-vetting-unverified-resolution/6-01-PLAN.md`
**Plan check:** 6-PLAN_CHECK.md — PASS_WITH_FIXES (0 blockers, 6 warnings)
**Files reviewed:** 6-01-PLAN.md against 7 live surfaces

**Verdict:** NEEDS_WORK

The edit actions are substantively correct: every verdict in Tasks 1-4 traces faithfully to
6-RESEARCH.md §1-§5 (40051-2C image-cover caveat, SP-7084 NTRS licence, VV&A chapter-wise
rescope, 881F access path, AFOTEC/DAG/SEI exclusions, GP-08 descope with NPR 7150.2 +
NASA-STD-8739.8 alternatives), the 56 + 7 = 63 arithmetic is right, and the Link Policy is
safe (live `grep -c http docs/SOURCE-VETTING.md` = 0; actions forbid URLs; pointer paragraph
routes to 6-RESEARCH.md as the URL store). What blocks approval is executability and
coverage: one automated gate is a bash syntax error that can never pass in an
`autonomous: true` plan, one phase success criterion (SC3, GP-06) is not delivered and is
then falsely certified as satisfied inside Task 5, and two stale 8-pack surfaces survive
with no verify able to catch them. All fixes are small, single-file plan revisions — no
redesign, no split.

---

## Findings

### BL-01 [BLOCKER] Task 1 `<automated>` verify is invalid bash — gate can never pass

**File:** 6-01-PLAN.md, Task 1 `<verify><automated>` (plan line 77)
**Issue:** The pipeline `... && grep -c "Verified 2026-08-14" docs/SOURCE-VETTING.md (expect ≥ 7 new v1.18 rows; total count = pre-existing count + 7) && ...` carries an unquoted parenthetical. Live `bash -c` re-run: `syntax error near unexpected token '('`. The plan is `autonomous: true` and `estimate.tasks: 5`; the executor hits a parse-failing gate on the first task — it either stalls or silently improvises a weaker check, defeating the automated gate.
**Fix:** Drop the parenthetical; assert a numeric floor plus the distinctive strings (plan_check W1):
```bash
! grep -n "http" docs/SOURCE-VETTING.md && test "$(grep -c 'Verified 2026-08-14' docs/SOURCE-VETTING.md)" -ge 14 && grep -n "Vetted candidates (v1.18.0)" docs/SOURCE-VETTING.md && grep -n "6-RESEARCH.md" docs/SOURCE-VETTING.md
```

### MJ-01 [MAJOR] GP-06 (`federal-bca`) gets no verdict, yet Task 5 certifies SC3 satisfied

**File:** 6-01-PLAN.md, Task 1 action ("7 rows covering the confirmed GP packs") and Task 5 action item (6)
**Issue:** Task 1's 7 rows are 40051-2C (GP-07), SP-7084 (not a GP pack — it is a VET-01 item), VV&A (GP-01), 881F (GP-05), FAA-STD-025 (GP-02), DOT&E (GP-03), DAFMAN (GP-04). GP-06 (OMB A-94 + Army CBA Guide) has no 6-RESEARCH.md section, no spot-check, and no SOURCE-VETTING row — the gap report (capability-gap-report.md line 157) marked it Tier 1 live, but Phase 6 never records that on the integrity surface. ROADMAP Phase 6 SC3 says "Each GP pack candidate confirmed or dropped" — GP-06 is neither. Worse, Task 5 item (6) asserts the SC "is now satisfied by artifacts (GP-01..07 confirmed in SOURCE-VETTING...)" — a false claim about the plan's own output. A fresh executor will either believe it or discover the contradiction mid-run.
**Fix:** Add an 8th vetted row (or a one-line "already-ranked Tier 1 in gap report §shortlist item 5; not re-opened" note) for OMB Circular A-94 + Army CBA Guide dated `(Verified 2026-08-14.)`, and correct the Task 5 claim. Adjust the Task 5 stamp arithmetic accordingly (see MJ-03).

### MJ-02 [MAJOR] Stale 8-pack surfaces survive — ROADMAP overview bullet and MILESTONES.md not tasked

**File:** 6-01-PLAN.md, Task 4 action/verify; live `.planning/ROADMAP.md:77`, `.planning/MILESTONES.md:18`
**Issue:** Task 4 edits only the Phase 7 Details Goal/Requirements. ROADMAP line 77 (v1.18 phase list) still reads "Build GP-01..GP-08 packs", and MILESTONES.md line 18 still reads "7-8 Tier-1 packs" (hyphenated, outside `files_modified`). After a faithful execution the roadmap contradicts itself (overview says 8, details say 7) and the milestone surface advertises a range the descope kills. Task 5's leftover-guard `! grep -n "63-64\|7–8 packs"` catches none of this — verified live: en-dash `7–8 packs` matches neither `7–8 public-domain packs` (ROADMAP Goal) nor `7-8 Tier-1 packs` (MILESTONES, plain hyphen); `GP-01..GP-08` is not grepped at all.
**Fix:** Task 4 also rewrites the ROADMAP overview bullet to "Build GP-01..GP-07 packs (GP-08 descoped)". Either add `.planning/MILESTONES.md` to `files_modified` and set it to 7 packs / 63 total, or explicitly record it as accepted drift. Task 5 greps for `GP-01..GP-08`, `7-8`/`7–8`, and `63-64` across all touched surfaces.

### MJ-03 [MAJOR] Verify gates false-pass and false-fail beyond the syntax error

**File:** 6-01-PLAN.md, Task 2 verify (line 87), Task 5 verify (line 117)
**Issue:** Four weak gates: (a) Task 2 uses one OR-grep (`AFOTEC|Defense Acquisition Guidebook|CMU SEI`) — a single name passes; (b) `grep -c "Verified 2026-08-14"` appears in Tasks 1, 2, and 5 with no numeric assertion, and the pre-phase tree already has 7 stamps (live count confirmed), so it exits 0 today; (c) Task 5 greps `GP-07` in docs/SOURCE-VETTING.md, but Task 1 writes document names (`MIL-STD-40051-2C`), never GP tokens — faithful execution false-fails; (d) `git diff --stat` always exits 0, proving nothing. The `must_haves` truths (dated rows, exclusions, URL-free) are therefore not provable by the plan's own automation.
**Fix:** Task 2: three conjunct greps. Task 5: `test "$(grep -c 'Verified 2026-08-14' docs/SOURCE-VETTING.md)" -eq <N>` where N = 7 pre-existing + new rows (10 as written, 11 if MJ-01's GP-06 row is added); grep document short names (`40051-2C`, `SP-7084`, `VV&A`, `881F`, `FAA-STD-025`, `DOT&E`, `DAFMAN`, `A-94`) instead of `GP-07`; replace bare `git diff --stat` with a file-count assertion (exactly 4 modified files, or 5 with MILESTONES).

### MN-01 [MINOR] claim_verification: wrong path and overstated house-style claim

**File:** 6-01-PLAN.md, claim_verification rows 2 and 7 (lines 62, 67)
**Issue:** Row 7 runs `sed -n '/1c/,/1d/p' 6-RESEARCH.md` against the repo root — the file lives at `.planning/phases/6-source-vetting-unverified-resolution/6-RESEARCH.md`; the command fails as written (quoted verdict text is real). Row 2 claims SOURCE-VETTING "rows carry '(Verified 2026-08-14.)' convention" — true only for the 7 Excluded rows; the v1.17 Vetted table has no date stamps (live-verified).
**Fix:** Correct the sed path. Reword row 2 to "Excluded rows carry the date-stamp convention; v1.17 Vetted rows are undated" (matches MN-05).

### MN-02 [MINOR] Task 2 trailing instruction is self-contradictory and mistypes the SEI address

**File:** 6-01-PLAN.md, Task 2 action (line 85)
**Issue:** "Do not name permission@sei.cmu.eu or any URL — the email address is fine (it is not a URL), but no http links." The row text itself correctly uses `permission@sei.cmu.edu` (matching 6-RESEARCH §3b); this trailing sentence mistypes the domain (.eu) and simultaneously forbids and permits the email. A literal executor may strip the email from the row or propagate the typo.
**Fix:** "No http/https URLs anywhere in the row; the bare email address `permission@sei.cmu.edu` (no mailto:) is permitted."

### MN-03 [MINOR] DOT&E row drops the research conditional and the PACK.yaml edition label

**File:** 6-01-PLAN.md, Task 1 row (6) and Task 3 GP-03 note (lines 75, 95)
**Issue:** 6-RESEARCH §2b says build against Aug 2022 (8.02) from dote.osd.mil "if a direct PDF is obtainable in-browser", with the afacpo single-encoded mirror (which is v3 June 2022, a different edition) as fallback, labelled in PACK.yaml. The plan records an unconditional "build against Aug 2022 edition (8.02)" and — unlike the FAA-STD-025 row — omits "record chosen edition/revision in PACK.yaml". Phase 7 may be forced to deviate from REQUIREMENTS as written if 8.02 has no direct PDF.
**Fix:** Carry the conditional and add "record the edition actually used (8.02 or mirror v3-June) in PACK.yaml" to both the SOURCE-VETTING row and the GP-03 note.

### MN-04 [MINOR] GP-04 REQUIREMENTS description left stale despite the MOTRC title correction

**File:** 6-01-PLAN.md, Task 3 (line 95); live `.planning/REQUIREMENTS.md:83`
**Issue:** 6-RESEARCH §2c corrects DAFMAN 63-119's title to "Mission-Oriented Test Readiness Certification" ("not a general 'AF T&E enterprise manual'"). Task 3 appends notes to GP-01 and GP-03 only; GP-04 keeps the pre-correction description "DAF Test & Evaluation manual", against must_haves key_links ("REQUIREMENTS GP rows must match the verdicts in 6-RESEARCH.md §5").
**Fix:** Append to GP-04: "(title correction: MOTRC compliance manual, 15 Apr 2021 — per 6-RESEARCH.md §2c)".

### MN-05 [MINOR] Date-stamping Vetted rows contradicts the convention the plan says it follows

**File:** 6-01-PLAN.md, Task 1 action (line 75)
**Issue:** Task 1 instructs "following its exact table format ... and prose conventions" of the v1.17 section, then "Every row ends with a date stamp '(Verified 2026-08-14.)' matching house convention" — but the v1.17 Vetted table carries no stamps (the convention is Excluded-table-only). Executable, but self-contradictory, and the Task 5 "+10 stamps" arithmetic depends on the deviation. must_haves truth 1 does require stamps, so keep them — just stop describing them as the existing Vetted convention.
**Fix:** "Rows carry `(Verified 2026-08-14.)` — deliberate extension of the Excluded-table stamp convention to the new Vetted rows (v1.17 Vetted rows are undated)."

---

## Plan-check incorporation (orchestrator question)

All six 6-PLAN_CHECK warnings are incorporable in-scope, as small edits to 6-01-PLAN.md only:

| Check finding | In-scope? | Covered by |
|---|---|---|
| W1 Task 1 verify syntax error | Yes — rewrite one command | BL-01 |
| W2 unasserted stamp counts / OR-grep | Yes — rewrite two commands | MJ-03 |
| W3 overview bullet + MILESTONES leftovers | Yes — one extra Task 4 edit (+ optional files_modified addition) | MJ-02 |
| W4 GP-07 token false-fail | Yes — retarget greps | MJ-03 |
| W5 claim_verification sed path | Yes — fix path | MN-01 |
| W6 GP-06 no verdict | Yes — one added row/note | MJ-01 |
| W7 estimate confidence med vs low | No action (check says "do not split") | none |

No plan_check finding requires a scope change, a new file outside `files_modified` (except the optional MILESTONES.md line), or renegotiating any verdict.

## Confirmed correct (checked, not raised)

- Verdict fidelity: all 11 rows of 6-RESEARCH §5 map 1:1 onto Task 1/2 row specs, including the 40051-2C scanned-image DIST-A caveat, SP-7084 NTRS "Work of the US Gov. Public Use Permitted" evidence, VV&A chapter-wise build with per-chapter provenance, and the 881F QuickSearch/GovTribe path.
- AFOTEC exclusion wording (DTIC maintenance shells, 1989 AD-A205 489, revisit condition) matches §1e exactly; DAG (retired, AFCAPO 2022-08-15) and SEI (© CMU, gov-purpose carve-out, DIST-A ≠ copyright grant) match §3a/§3b.
- GP-08 descope is explicit and reversible: strike + Out-of-Scope row + NPR 7150.2 / NASA-STD-8739.8 alternatives as v1.19/stretch — not a silent cut.
- Arithmetic: 56 shipped (54 catalog + 2 signposts) + 7 GP = 63; REL-1x and Phase 9 do not hard-code 64.
- Link Policy: live http count 0; tasks forbid URLs; URL store stays in 6-RESEARCH.md; T-6-01 mitigation matches the grep gate. The bare `swehb.nasa.gov` host in the GP-08 note is scheme-less and passes the Phase-2 reading (acceptable; "NASA SWEHB wiki" is cleaner).
- Insertion points match the live file (v1.18 section after the v1.17 section; Excluded rows after the DAU/WARU row, which is the table's last row).
- VET-01/VET-02 rows correctly left unchecked (verification phase ticks them); no pack builds; Task ordering acyclic; single plan, `depends_on: []` valid.
- Date-stamp baseline live-verified: 7 pre-existing stamps, so the plan's "+10 = 17" arithmetic is correct as written (becomes 18 with MJ-01's GP-06 row).

## Recommendation

Revise 6-01-PLAN.md before execute — the fix list is mechanical: (1) repair the four verify commands (BL-01, MJ-03); (2) add the GP-06 row/note and delete the false SC3-satisfied claim (MJ-01); (3) task the ROADMAP overview bullet and decide MILESTONES.md (MJ-02); (4) the four one-line wording/accuracy nits (MN-01..MN-04). No verdict changes, no scope changes, no re-plan. A quick re-check of the edited verify blocks is sufficient after revision; a full re-review is not.

---

**Verdict:** NEEDS_WORK
