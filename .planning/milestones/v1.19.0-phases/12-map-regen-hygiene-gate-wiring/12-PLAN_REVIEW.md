# Phase 12 Plan Review — 12-01-PLAN.md + 12-02-PLAN.md

**Reviewed:** 2026-08-17
**Depth:** deep (plan vs live tree: ROADMAP Phase 12 SC-1..SC-4, REQUIREMENTS MAP-19-01..05 + HYG-01..04, 12-RESEARCH recommended shape + Patterns 1–5 + user_constraints, 12-PLAN_CHECK, 12-VALIDATION, analog 11-PLAN_REVIEW; live re-run of every `claim_verification` row; `bash -n` + pre-phase execute of every `<automated>` block)
**Plans:** `.planning/phases/12-map-regen-hygiene-gate-wiring/12-01-PLAN.md`, `12-02-PLAN.md`
**Plan check:** 12-PLAN_CHECK.md — PASS_WITH_FIXES (blockers: 0, 4 warnings)
**Files reviewed:** both plans against locked RESEARCH constraints + live map/release/hygiene surfaces

**Verdict:** PASS_WITH_FIXES

The two waves will regenerate the map, apply the locked three-row MOVE, encode the listed-primary floor, land the CONTRACT paragraph, wire the now-green map gate into `check_release.py`, and close the four hygiene nits if the executor follows the actions. Remap is MOVE not copy. Version trio stays 1.18.0. Wire is gated on a GREEN map. HYG-03 may close as an external-repo PR. No success criterion is missing and no automated block is invalid bash. What keeps this off APPROVE is the same class as Phase 11 MJ-01 / Phase 10 MJ-01..03: 12-01 Task 1's automated verify can green-light an incomplete classify that the acceptance lines already require. T2's live gate recovers before the plan is done — one-line verify rewrite, no redesign, no split, no verdict changes.

---

## Findings

### MJ-01 [MAJOR] 12-01 Task 1 verify is pack-level, not chapter-set

**File:** 12-01-PLAN.md, Task 1 `<verify><automated>`
**Issue:** Action / done / acceptance require all 16 unmapped chapter files classified (7 `nasa-std-8719-14` + 6 `is-gps-200n` + leftover RPG ch11–ch13). Automated verify asserts disk-vs-map **pack** sets, uniqueness, the locked DA five-row set, old-cluster absence, Integration 4/4, md slug greps, no generator, catalog `chapters == 10`, and SOURCE-VETTING `http == 0`.

An executor can add one row per new slug (so `disk-packs` is empty), apply the three-row MOVE, mention both slugs in `capability-pack-map.md`, and leave leftover RPG / remaining 8719/200N files unmapped. T1 still prints `MAP_MOVE_OK`. Pre-phase execute this session died on `{'is-gps-200n', 'nasa-std-8719-14'}` — distinctive for the two missing *packs*, not for the 16 *files*.

T2 `python tooling/check_capability_map.py` would then fail chapter-set staleness (`on_disk_only=16` today). Recoverable, but T1 can be marked done and the json+md commit can land incomplete. Same class as 11-PLAN_REVIEW MJ-01 / 12-PLAN_CHECK W1.

**Fix:** add a `packs/*/chapters/*.md` vs JSON `(pack, chapter)` set-diff to T1 automated (exclude support-file suffix), **or** run `python tooling/check_capability_map.py` in T1 and treat THRESHOLDS-only failures as the only expected RED (plan already allows adding THRESHOLDS in-session if the commit stays on T2).

### MN-01 [MINOR] 12-01 Task 3 does not assert the section 5 threshold table

**File:** 12-01-PLAN.md, Task 3 `<verify><automated>`
**Issue:** Action + acceptance require §5 to match the new floors (Interfaces ≥4; add DA / Validation / Integration / Ops ≥4). Automated verify only greps `628` / `502` / `Cybersecurity` / `Digital Engineering` / unbound. Live CONTRACT has none of those tokens today (502 lives only in `docs/ROLE-AGENTS-REQUIREMENTS-V2.md`) — the paragraph greps *are* distinctive. The table update is acceptance-only.

**Fix:** grep CONTRACT for `Decision Analysis` / `Validation` / `Integration` / `Operations, Maintenance` plus Interfaces ≥4. 12-PLAN_CHECK W2.

### MN-02 [MINOR] 12-VALIDATION.md Per-Task map lumps the six execute tasks

**File:** 12-VALIDATION.md
**Issue:** Rows: 12-01-01 (MAP-19-01/02/03), 12-01-02 (MAP-19-05), 12-02-01 (MAP-19-04), 12-02-02 (HYG-01..04). Actual plans are 3+3 tasks; T2 THRESHOLDS and T3 HYG-03 are not named. Frontmatter still `nyquist_compliant: false`. Nyquist 8a–8d still pass (every task has `<automated>`).

**Fix:** add rows for 12-01-02 THRESHOLDS/conjunct and 12-02-03 HYG-03, or leave as advisory. 12-PLAN_CHECK W3.

### MN-03 [MINOR] 12-RESEARCH.md Open Questions not marked RESOLVED

**File:** 12-RESEARCH.md Open Questions
**Issue:** No `(RESOLVED)` suffix and no inline RESOLVED markers. All four items already have Recommendations the plans implemented (Integration floor-held 4/4; `map_version` 1.18.0; HYG-03 Path A or B; ch11 not force-fit to Validation).

**Fix:** retitle `Open Questions (RESOLVED)` and prefix each item RESOLVED with the chosen path. Do not reopen. 12-PLAN_CHECK W4.

### MN-04 [MINOR] 12-02 Task 2 40051 `[0]` line is frontmatter, not the Topic Index row

**File:** 12-02-PLAN.md, Task 2 `<verify><automated>`
**Issue:** `assert 'Topic Index' not in [ln for ln in s400.splitlines() if 'Training & Documentation' in ln][0]` takes the **first** matching line. Live that is `SKILL.md:3` frontmatter `description:` (never contained `Topic Index`). The circular target is `:77`. The preceding `assert 'ch08, Topic Index' not in s400` *does* distinguish the pre-phase tree (fails today). The `[0]` check is dead weight, not a false green.

**Fix:** bind the assert to the Topic Index bullet (`ln.startswith('- **Training & Documentation**')` or the `:77` line), or drop `[0]` and keep the `ch08, Topic Index` substring.

---

## Verify-command re-run (this session)

All six `<automated>` blocks extracted verbatim. `bash -n` via `/usr/bin/bash` 5.3.15 (Git Bash / Cygwin):

| Task | `bash -n` | Pre-phase execute | Distinguishes live tree? |
|---|---|---|---|
| 12-01 T1 | SYNTAX_OK | rc=1 (`disk-packs` = `{is-gps-200n, nasa-std-8719-14}`) | Yes on missing packs + DA want-set (live DA is the two NASA rows). Does not walk chapter files (MJ-01) |
| 12-01 T2 | SYNTAX_OK | rc=1 (`FAIL: 19 issue(s)` before THRESHOLDS body) | Yes. THRESHOLDS today lack DA/Validation/Integration/Ops; Interfaces is 3 not 4. Gate RED until T1+T2 |
| 12-01 T3 | SYNTAX_OK | rc=1 (`628` absent from CONTRACT) | Yes on the MAP-19-05 paragraph tokens. Does not grep §5 floors (MN-01) |
| 12-02 T1 | SYNTAX_OK | rc=1 (map gate RED; `&&` stops before import asserts) | Yes. `check_capability_map` absent from `check_release.py` today. Cannot green a RED-map wire |
| 12-02 T2 | SYNTAX_OK | rc=1 (CHANGELOG BOM `ef bb bf`) | Yes. `.gitattributes` absent; 881F PM after Program Element; dafman Agile before AFOTEC; `ch08, Topic Index` present; federal-bca label unfixed |
| 12-02 T3 | SYNTAX_OK | rc=1 (map gate RED; SUMMARY does not exist) | Yes. Keywords required in 12-02-SUMMARY; Path B URL optional (matches ROADMAP SC-4) |

No `2>/dev/null || echo 0`. No `|| true` feeding a comparison. No caret-anchored package-manager grep. `grep -c http docs/SOURCE-VETTING.md | grep -qx 0` is the Link Policy ban (count is 0; pipe form exits 0 on the ban, 1 if a URL appears) — not a required echo. Same false-positive class as Phase 10/11 structure-tool #429.

---

## claim_verification live re-run (cwd repo root, 2026-08-17)

No missing/empty `claim_verification`. No invented replacements. Every current-state row matches:

| Plan | Claim | Live | Status |
|---|---|---|---|
| 12-01 | Branch is main | `main` | Accurate |
| 12-01 | Map gate RED, 19 issues; packs `is-gps-200n` + `nasa-std-8719-14`; `on_disk_only=16, map_only=0`; 16 named chapter files | exit 1; `FAIL: 19 issue(s)`; same two packs; 16 named files | Accurate |
| 12-01 | Release gate PASS; does not import map | `RELEASE CHECK: PASS`; `check_capability_map` absent | Accurate |
| 12-01 | Envelope Phase 8: schema 2, `map_version` `1.18.0`, `generated_on` `2026-08-17`; 32 clusters; 628 entries; 61 mapped / 63 disk | matches | Accurate |
| 12-01 | Disk-not-map `['is-gps-200n', 'nasa-std-8719-14']`; map-not-disk `[]` | matches | Accurate |
| 12-01 | Chapter files 7 / 6 / 13 | matches | Accurate |
| 12-01 | Listed-primary counts DA 2/2; Validation 5/4; Integration 4/4; Interfaces 4/3; Ops 6/4; Opportunity 10/2; Assurance 9/4 | matches | Accurate |
| 12-01 | MAP-19-03 membership (ch04/ch06 Opportunity; rpg ch06 Assurance; ch08 Validation; ch10 Risk) | matches | Accurate |
| 12-01 | DA today two rows `nasa-ceh` + `nasa-se-handbook` | matches | Accurate |
| 12-01 | Cyber 69/10; DE 25/4 | matches | Accurate |
| 12-01 | Version trio 1.18.0; no `v1.19*` tag | plugin/CHANGELOG/RELEASE-INFO 1.18.0; empty `v1.19*` | Accurate |
| 12-01 | Catalog leftover Phase 13; both new slugs thin-registered; `n_catalog` 63; `dod-vva-rpg.chapters == 10` | matches | Accurate |
| 12-01 | THRESHOLDS Training 1 / Traceability 3 / Interfaces 3 / Opportunity 2 | `tooling/check_capability_map.py:34-39` | Accurate |
| 12-01 | CONTRACT standalone sentence :81-82 | present (backticks around `check_release.py`) | Accurate |
| 12-01 | SOURCE-VETTING `http` count 0 | 0 | Accurate |
| 12-01 | CI never execs repo Python | `validate.yml:4-6` | Accurate |
| 12-02 | Map RED at plan time (12-01 must flip) | still RED | Accurate |
| 12-02 | Import analog in-process :118-128 | `sys.path.insert` + `import validate_pack` | Accurate |
| 12-02 | Map-gate `main()` returns 0/1 | :238-245 | Accurate |
| 12-02 | Map-gate docstring still standalone | :16-17 | Accurate |
| 12-02 | CHANGELOG UTF-8 BOM + CRLF | `efbbbf3c212d2d0d`; BOM True; crlf 620 | Accurate |
| 12-02 | `.gitattributes` missing | False | Accurate |
| 12-02 | Version trio 1.18.0; CHANGELOG top `## [1.18.0]: 2026-08-17` | matches | Accurate |
| 12-02 | HYG-02 live nits (881F :89 last; dafman Agile then AFOTEC; 40051 Topic Index; federal-bca Opportunity/Benefit Analysis) | matches | Accurate |
| 12-02 | HYG-04 live wording :20 | `no third-party copyright / (c) / all-rights-reserved notices` | Accurate |
| 12-02 | Sibling EXCLUDED missing afotec / cmu / sei; `defense acquisition` is US_GOV | confirmed `$REF/tools/vet_source.py` | Accurate |
| 12-02 | CI never execs repo Python; no v1.19 tag; SOURCE-VETTING 0; catalog chapters 10 | matches | Accurate |

Future-state arithmetic (644 if 16 adds / 0 support) is labeled expected, not asserted as an exact verify equality.

---

## Plan-check incorporation

All four 12-PLAN_CHECK warnings are in-scope as small edits (verify lines + two advisory stamps). No check finding requires a scope change, a new file outside `files_modified`, or renegotiating any locked RESEARCH decision.

| Check finding | In-scope? | Covered by |
|---|---|---|
| W1 T1 verify is pack-level, not chapter-set | Yes — T1 commit can land incomplete; T2 recovers | MJ-01 |
| W2 T3 does not assert CONTRACT §5 floors | Yes — paragraph greps are the SC; table is acceptance-only | MN-01 |
| W3 VALIDATION.md lumps execute tasks | Yes — advisory row | MN-02 |
| W4 Open Questions unmarked | Yes — stamp only | MN-03 |

---

## Confirmed correct (checked, not raised)

- ROADMAP SC-1..SC-4 and REQUIREMENTS MAP-19-01..05 + HYG-01..04 are all tasked. Frontmatter IDs: 12-01 = MAP-19-01/02/03/05; 12-02 = MAP-19-04 + HYG-01..04. REL-19 stays Phase 13.
- Remap is MOVE: delete-from + insert-into table matches `11-02-SUMMARY.md:163-171`; DA exact five-row set; Opportunity/Assurance absence asserts; uniqueness on `(pack, chapter)` forbids copy.
- No version bump: `map_version` stays `1.18.0`; version trio asserted; no `## [1.19.0]`; no `v1.19*` tag. md changelog may add a v1.19 *bullet* (RESEARCH recommended shape) without touching version surfaces.
- Wire happens AFTER map is GREEN: `depends_on: ["12-01"]` + T1 hard STOP + 12-01 does not touch `check_release.py`. T1 verify is `check_capability_map && check_release` — a RED map cannot green the wire.
- HYG-03 may be external PR: Path B is a valid close (ROADMAP SC-4); vendoring forbidden (`test ! -e tooling/vet_source.py`).
- Integration "must move" treated as floor-held 4/4 — RESEARCH Q1, not a silent reduction. T1 hard-locks `len(integ)==4` so leftover RPG cannot be dumped there.
- FUT-05 generator, AAF/CBA/DoDM/stakeholder packs, Cyber/DE bindings, CI repo-Python, catalog 10→13, README new-slug rows all forbidden in must-NOT + verify.
- MAP-19 / HYG boxes left unchecked — correct; verify owns the ticks.
- 12-02 10 files is the warning threshold; RESEARCH Wave B shape stands — do not split.
- 12-01 80000 and 12-02 60000 are under the 100k smart-zone.
- Unclassified `.edge-coverage.json` probes left unresolved — no invented `check_kind` / `check_target`.
- Import is in-process (`import check_capability_map; rc = main()`), copying the live `validate_pack` analog at `check_release.py:118-128`. No subprocess. Insertion point (after cursor-manifest ~213, before authored-file headers ~214) matches live.
- HYG-02 881F / dafman first-occurrence greps are safe: those strings appear only on the Topic Index rows being moved.
- 12-02 `depends_on: ["12-01"]` is acyclic; shared CONTRACT / `check_capability_map.py` are sequential, different sections (12-01 owns THRESHOLDS + MAP-19-05 paragraph; 12-02 owns docstring + §4 sentence).
- Stay on `main`. No branches / worktrees. EDGE_ABSENT=1 honored.

---

## Recommendation

Add the chapter-set (or live-gate) assert to 12-01 T1 before execute so a two-slug stub cannot go green. Stamp Open Questions / VALIDATION.md and tighten the 40051 / §5 greps if convenient — not execute-blocking. No verdict changes, no scope changes, no re-plan. A quick re-check of the edited T1 verify line is sufficient after revision; a full re-review is not.

---

**Verdict:** PASS_WITH_FIXES

blockers: 0
**majors:** 1
**minors:** 4

Path: `.planning/phases/12-map-regen-hygiene-gate-wiring/12-PLAN_REVIEW.md`

Two-wave plan covers every Phase 12 success criterion and every MAP-19 / HYG ID. Actions match 12-RESEARCH. All six verify scripts are valid bash and fail closed on **this** tree. Remap is MOVE. No version bump. Wire is after GREEN. HYG-03 may be an external PR. Advance after adding the chapter-file set-diff (or map-gate run) to 12-01 T1.
