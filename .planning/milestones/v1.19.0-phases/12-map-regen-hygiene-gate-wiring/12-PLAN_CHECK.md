# Phase 12 Plan Check

**Phase:** 12-map-regen-hygiene-gate-wiring
**Plans checked:** 2 (`12-01-PLAN.md`, `12-02-PLAN.md`)
**Checked:** 2026-08-17
**Method:** Goal-backward verification against ROADMAP Phase 12 goal + SC-1..SC-4, REQUIREMENTS MAP-19-01..05 + HYG-01..04, `12-RESEARCH.md` (recommended shape + user_constraints), `12-PATTERNS.md`, `12-VALIDATION.md`, `11-02-SUMMARY.md` remap table, and live re-measurement of every `claim_verification` row.

**Verdict:** PASS_WITH_FIXES

The two waves will regenerate the map, apply the locked three-row MOVE, encode the listed-primary floor, land the CONTRACT paragraph, wire the now-green map gate into `check_release.py`, and close the four hygiene nits if the executor follows the actions. Remap is MOVE not copy. Version trio stays 1.18.0. Wire is gated on a GREEN map. HYG-03 may close as an external-repo PR. Several automated blocks do not measure every acceptance line (chapter-set completeness in 12-01 T1; CONTRACT section 5 table; VALIDATION task map; Open Questions unmarked). Fix those before execute if the verifier scores the written commands strictly. Do not treat this as a rewrite.

---

## Goal-backward trace

Phase goal: *Map reflects new packs; competency-primary floor asserted; hygiene + consumer-contract note*

| Success criterion | Required truth | Covering task | Provably delivered? |
|---|---|---|---|
| SC-1 / MAP-19-01 + MAP-19-02 -- `check_capability_map.py` PASS; no listed primary still at `<4 entries AND 1 pack` | Agent-classify 16 unmapped chapters; name-keyed THRESHOLDS >=4; conjunct print | 12-01 T1 (classify + MOVE + md) + 12-01 T2 (THRESHOLDS + gate + conjunct) | **Yes.** T2 runs the live gate to exit 0 and fails if any listed primary is `(count < 4 and n_packs == 1)`. Integration stays 4/4 -- floor encoded, no invented pack. |
| SC-1 / MAP-19-03 -- Decision Analysis leaves 2 via locked remap | Three-row MOVE into cluster 16; DA = 5/4; Opportunity keeps ch01-ch03/ch05 + support | 12-01 T1 | **Yes as MOVE.** Membership asserts delete old cluster rows; uniqueness on `(pack, chapter)` forbids copy. Table matches `11-02-SUMMARY.md:163-171`. |
| SC-2 / MAP-19-04 -- `check_release.py` invokes the map gate | In-process `import check_capability_map; rc = main()`; fail on non-zero | 12-02 T1 | **Yes, after green.** `depends_on: ["12-01"]` + hard STOP if map is still RED. No subprocess. No CI repo-Python step. |
| SC-3 / MAP-19-05 -- CONTRACT notes live snapshot (not 502) and unbound Cyber/DE | One paragraph: 628+ / 502 residue / Cyber+DE unbound | 12-01 T3 | **Yes.** Pack-side only; no ROLE-AGENTS edit; no bindings. |
| SC-4 / HYG-01 -- CHANGELOG BOM gone; `.gitattributes` pin | Strip BOM + LF; `*.md text eol=lf` | 12-02 T2 | **Yes.** No `## [1.19.0]`. No whole-repo EOL rewrite. |
| SC-4 / HYG-02 -- topic-index nits fixed | 881F alpha, dafman AFOTEC-before-Agile, 40051 drop circular Topic Index, federal-bca label; `validate_pack` x4 | 12-02 T2 | **Yes.** Exact live lines + revalidate. |
| SC-4 / HYG-03 -- vet_source EXCLUDED sync **or** recorded external-repo PR | Sibling keys **or** SUMMARY Path B | 12-02 T3 | **Yes.** ROADMAP SC-4 allows either. Do not vendor. Do not block close on sibling merge. |
| SC-4 / HYG-04 -- federal-bca "(c)" wording | PACK.yaml enumeration-markers wording | 12-02 T2 | **Yes.** Cosmetic only. |
| Phase 13 fence | No version/tag/catalog/README steal | both plans + T3 fence | **Yes.** `map_version` stays `1.18.0`; plugin/CHANGELOG/RELEASE-INFO stay 1.18.0; catalog `dod-vva-rpg.chapters` stays 10. |

Requirements frontmatter: 12-01 lists [MAP-19-01, MAP-19-02, MAP-19-03, MAP-19-05]; 12-02 lists [MAP-19-04, HYG-01, HYG-02, HYG-03, HYG-04]. No ROADMAP requirement ID is missing from all plans.

`claim_verification` is present and populated on both plans (not missing/empty). Live re-run matches every current-state row (see below).

---

## First principles / inversion

**Current Assumptions:**
- Assumption 1: MAP-19-02 "must each move" requires an Integration pack or a count delta -- challenged: **false**. RESEARCH Q1 + Pattern 3: Integration already 4/4; encode THRESHOLDS >=4; do not raid. Conjunct is `<4 AND 1 pack`, not "every primary gains rows".
- Assumption 2: Regenerating the map requires bumping `map_version` / plugin to 1.19.0 -- challenged: **false**. RESEARCH discretion: keep `1.18.0` + fresh `generated_on`. Phase 13 owns the version trio.
- Assumption 3: HYG-03 fails unless the sibling merges -- challenged: **false**. ROADMAP SC-4: "done or recorded as external-repo PR".
- Assumption 4: Wiring `check_release` can land in the same wave as regen -- challenged: **false**. RESEARCH Pitfall 2: regen first, wire second, or `check_release` flips RED on `main`.

**Fundamental Truths:**
- Uniqueness is on `(pack, chapter)`. Copy-not-move fails the gate and fails SC-1.
- The map gate must be GREEN before `check_release` imports it.
- Phase 13 owns REL-19. Phase 12 must not invent a version surface.
- FUT-05 generator stays deferred. Agent pass + existing gate is the locked path.

**Guaranteed Failure Modes:**
1. Copy remap rows: Avoid by DA exact-set assert + old-cluster absence + uniqueness.
2. Wire a RED map: Avoid by `depends_on 12-01` + T1 hard STOP.
3. Bump 1.19.0 / tag / catalog 10->13: Avoid by must-NOT + version-trio / catalog asserts.
4. Invent Integration / AAF / CBA / DoDM / stakeholder packs: Avoid by Integration 4/4 assert + must-NOT.
5. Bind Cyber/DE or put URLs in SOURCE-VETTING: Avoid by CONTRACT unbound wording + `grep -c http == 0`.
6. Vendor `vet_source.py` and wait on sibling merge: Avoid by Path B + `test ! -e tooling/vet_source.py`.

**Anti-Goals (Never Do):**
- Write a map generator
- Leave remap as copy
- Bump plugin / CHANGELOG `[1.19.0]` / RELEASE-INFO / `map_version` / tag
- Import the map gate before it is GREEN
- Steal catalog `dod-vva-rpg.chapters` or README new-slug rows

**Remaining Risk:** 12-01 T1 automated verify is pack-level, not chapter-set; a sloppy classify that maps the two new slugs but omits some of the 16 files will only fail at T2 when the live gate runs (W1). CONTRACT section 5 table update is acceptance-only (W2).

---

## Dimension results

| Dim | Result | Notes |
|---|---|---|
| 1 Requirement coverage | PASS | All nine ROADMAP IDs appear in a plan `requirements` field and have a covering task. REL-19 stays Phase 13. |
| 2 Task completeness | PASS | `verify.plan-structure`: 6 auto tasks, all have Files + Action + Verify + Done. Actions name files, locked MOVE rows, THRESHOLDS keys, insertion point, and HYG line fixes. |
| 3 Dependencies | PASS | 12-01 wave 1 `depends_on: []`. 12-02 wave 2 `depends_on: ["12-01"]` (same convention as 11-02 to 11-01). Acyclic. Shared CONTRACT / `check_capability_map.py` are sequential, different sections. |
| 4 Key links | PASS | Gate reads committed JSON; JSON covers every on-disk chapter (T2 gate); `check_release` imports `main()` after GREEN; CONTRACT section 4 flips when the wire lands; `.gitattributes` pins CHANGELOG LF. |
| 5 Scope sanity | PASS with note | 12-01: 3 tasks / 4 files. 12-02: 3 tasks / 10 files (warning threshold, not split -- RESEARCH Wave B shape). estimate-check --calibrated: 80000 (0.80) and 60000 (0.60) of 100000; `over_budget` false. Plan confidence high vs tool confidence low (`sample_count: 0`) -- advisory only. |
| 6 Verification derivation | WARN | Truths are user-observable. T1 does not assert chapter-file staleness (W1). T3 does not assert CONTRACT section 5 floors (W2). |
| 7 Context compliance | SKIPPED (no CONTEXT.md) | Discuss skipped. Locked RESEARCH user_constraints honored: agent pass not generator; MOVE list authoritative; floor is conjunct; wire existing gate; CONTRACT one paragraph; HYG-03 may be external PR; Phase 13 fence; stay on main. |
| 7b Scope reduction | PASS | Integration floor-held is RESEARCH Q1, not a silent v1. `map_version` 1.18.0 is discretion. HYG-03 Path B is ROADMAP-legal. No "static labels" / stub wire. |
| 7c Architectural tier | PASS | Responsibility map is committed map artifacts + two stdlib gates + cosmetic pack/docs. Tasks match those tiers. No client/API/DB misplacement. |
| 8 Nyquist | PASS with VALIDATION drift | `12-VALIDATION.md` exists. All six tasks have `<automated>` (no MISSING, no `--watch`, latency ~15s). Sampling 3/3 and 3/3. Wave 0 N/A (existing gates). VALIDATION per-task map lumps tasks (W3). |
| 9 Cross-plan contracts | PASS | 12-01 produces GREEN map + THRESHOLDS + MAP-19-05 paragraph. 12-02 consumes GREEN map, updates docstring + section 4 only, then hygiene. No conflicting transform. Wire cannot start until 12-01. |
| 10 CLAUDE.md | SKIPPED | No `./CLAUDE.md`. |
| 11 Research resolution | WARN | Open Questions has no `(RESOLVED)` suffix and no inline RESOLVED markers (W4). Each item already has a Recommendation the plans implemented. |
| 12 Pattern compliance | PASS | New/modified files map to PATTERNS.md analogs (Phase 8 agent regen, self gate, `validate_pack` import style, HYG exact lines). Shared "GREEN before wire" + import-not-subprocess + hygiene patterns are in the covering tasks. `.gitattributes` has no in-repo analog; plan copies RESEARCH / PATTERNS content verbatim. |

### Smart-zone estimates

| Plan | estimate.tokens | budget | over_budget | plan confidence | tool confidence |
|---|---|---|---|---|---|
| 12-01 | 80000 | 100000 | false | high | low (sample_count: 0) |
| 12-02 | 60000 | 100000 | false | high | low (sample_count: 0) |

Calibration not yet applied for this project (`sample_count: 0`). Weigh the 3-task / 4-file and 3-task / 10-file counts more heavily than the token figures.

### Dimension 8: Nyquist Compliance

| Task | Plan | Wave | Automated Command | Status |
|------|------|------|-------------------|--------|
| T1 classify 16 + MOVE | 12-01 | 1 | python membership/uniqueness/DA-set + md greps + no generator + catalog chapters==10 + http==0 | PASS (pack-level; W1) |
| T2 THRESHOLDS + conjunct | 12-01 | 1 | `python tooling/check_capability_map.py` + THRESHOLDS body + conjunct print + `check_release` still unwired | PASS |
| T3 CONTRACT paragraph | 12-01 | 1 | CONTRACT 628/502/Cyber/DE/unbound + map gate PASS + plugin 1.18.0 + http==0 | PASS (W2 on section 5) |
| T1 wire map into release | 12-02 | 2 | both gates PASS + import/`main()` + no standalone docstring + version trio 1.18.0 + validate.yml unnamed | PASS |
| T2 HYG-01/02/04 | 12-02 | 2 | CHANGELOG no BOM/CRLF + `.gitattributes` + four SKILL asserts + `validate_pack` x4 + PACK.yaml markers | PASS |
| T3 HYG-03 + fence | 12-02 | 2 | both gates + version trio + catalog 10 + no v1.19 tag + no vendored vet_source + SUMMARY keywords | PASS |

Sampling: Wave 1: 3/3 verified -> PASS. Wave 2: 3/3 verified -> PASS.
Wave 0: none required -> PASS (existing `check_capability_map` / `check_release` / `validate_pack`).
Overall: PASS (VALIDATION.md task-id map is lumped -- W3).

`verify.plan-structure` #429 warning on unquoted `http` in 12-02 is a **false positive** -- the grep is a Link Policy ban, not a required echo (same class as Phase 10/11).

---

## Targeted checks (orchestrator brief)

### Requirement to task mapping

| Req | Planned delivery | Gap |
|---|---|---|
| MAP-19-01 | 12-01 T1 agent-classify 16 chapters + sync md; T2 gate PASS | T1 verify is pack-level; chapter-set completeness waits for T2 (W1) |
| MAP-19-02 | 12-01 T2 name-keyed THRESHOLDS >=4 + conjunct print; Integration 4/4 no raid | None in the action |
| MAP-19-03 | 12-01 T1 three-row MOVE; DA exact five rows; old clusters emptied | None -- MOVE asserted, not copy |
| MAP-19-04 | 12-02 T1 in-process import after GREEN; CONTRACT section 4 + docstring | None |
| MAP-19-05 | 12-01 T3 one CONTRACT paragraph | section 5 threshold table is acceptance-only (W2) |
| HYG-01 | 12-02 T2 BOM/LF + `.gitattributes` | None |
| HYG-02 | 12-02 T2 four SKILL nits + validate_pack x4 | None |
| HYG-03 | 12-02 T3 Path A sibling keys or Path B SUMMARY record | None -- external PR is a valid close |
| HYG-04 | 12-02 T2 PACK.yaml enumeration-markers wording | None |

### Locked prohibitions (confirmed present)

| Prohibition | Where encoded | Live now |
|---|---|---|
| Remap is MOVE not copy | 12-01 T1 action table + DA exact-set + old-cluster absence + uniqueness | ch04/ch06 still Opportunity; rpg ch06 still Assurance |
| No version bump | must-NOT + T1 `map_version==1.18.0` + T3/12-02 version trio | plugin/CHANGELOG/RELEASE-INFO/map_version all 1.18.0; no v1.19* tag |
| Wire AFTER map is GREEN | 12-02 `depends_on: ["12-01"]` + T1 hard STOP | map gate RED (19 issues); `check_release` does not import map |
| HYG-03 may be external PR | 12-02 T3 Path A or B; ROADMAP SC-4 | sibling EXCLUDED still missing afotec / dod-dag / cmu-sei |
| No generator | T1 `test ! -e tooling/generate_capability_map.py` | files absent |
| No catalog 10->13 / README new slugs | T1 catalog assert + commit name-only fence | `dod-vva-rpg.chapters == 10` |
| No Cyber/DE bindings | T3 unbound wording; must-NOT | live 69/10 and 25/4 unbound |

### claim_verification accuracy (live re-run, 2026-08-17)

| Plan | Claim | Live | Status |
|---|---|---|---|
| 12-01 | Branch is main | main | Accurate |
| 12-01 | Map gate RED, 19 issues; `is-gps-200n` + `nasa-std-8719-14` not in map; on_disk_only=16, map_only=0 | exit 1; `FAIL: 19 issue(s)`; same two packs; 16 named chapter files | Accurate |
| 12-01 | Release gate PASS; does not import map | `RELEASE CHECK: PASS`; `check_capability_map` absent | Accurate |
| 12-01 | Envelope Phase 8: schema 2, map_version 1.18.0, generated_on 2026-08-17; 32 clusters; 628 entries; 61 mapped / 63 disk | matches | Accurate |
| 12-01 | Disk not mapped `['is-gps-200n', 'nasa-std-8719-14']`; map-not-disk `[]` | matches | Accurate |
| 12-01 | Chapter files 7 / 6 / 13 | matches | Accurate |
| 12-01 | Listed-primary counts DA 2/2; Validation 5/4; Integration 4/4; Interfaces 4/3; Ops 6/4; Opportunity 10/2; Assurance 9/4 | matches | Accurate |
| 12-01 | MAP-19-03 membership (ch04/ch06 Opportunity; rpg ch06 Assurance; ch08 Validation; ch10 Risk) | matches | Accurate |
| 12-01 | DA today two rows nasa-ceh + nasa-se-handbook | matches | Accurate |
| 12-01 | Cyber 69/10; DE 25/4 | matches | Accurate |
| 12-01 | Version trio 1.18.0; no v1.19* tag | plugin/CHANGELOG/RELEASE-INFO 1.18.0; empty v1.19* tags | Accurate |
| 12-01 | Catalog leftover Phase 13; thin-register already has both new slugs; n_catalog 63 | `dod-vva-rpg chapters 10`; both slugs present | Accurate |
| 12-01 | THRESHOLDS Training 1 / Traceability 3 / Interfaces 3 / Opportunity 2 | lines 34-39 | Accurate |
| 12-01 | CONTRACT standalone sentence :81-82 | present | Accurate |
| 12-01 | SOURCE-VETTING http count 0 | 0 | Accurate |
| 12-01 | CI never execs repo Python | validate.yml:4-6 | Accurate |
| 12-02 | Map RED at plan time (12-01 must flip) | still RED | Accurate |
| 12-02 | Import analog in-process :118-128 | `sys.path.insert` + `import validate_pack` | Accurate |
| 12-02 | Map-gate `main()` returns 0/1 | :238-245 | Accurate |
| 12-02 | CHANGELOG UTF-8 BOM + CRLF | `efbbbf3c212d2d0d`; BOM True; crlf 620 | Accurate |
| 12-02 | `.gitattributes` missing | False | Accurate |
| 12-02 | HYG-02 live nits (881F :89 last; dafman Agile then AFOTEC; 40051 Topic Index; federal-bca Opportunity/Benefit Analysis) | matches | Accurate |
| 12-02 | HYG-04 live wording :20 | no third-party copyright / (c) / all-rights-reserved notices | Accurate |
| 12-02 | Sibling EXCLUDED missing afotec / cmu / sei; `defense acquisition` is US_GOV | confirmed in sibling vet_source.py:41-61 | Accurate |

No missing/empty `claim_verification`. No numeric conflict with RESEARCH that required a prescribed correction. Future-state arithmetic (644 if 16 adds / 0 support) is labeled expected, not asserted as an exact verify equality.

### Verify-command audit

No `2>/dev/null || echo 0`, no `|| true` feeding a comparison, no caret-anchored package-manager grep.

| Task | Distinguishes pre-phase tree? | Residual |
|---|---|---|
| 12-01 T1 | Yes on DA membership (live DA is the two NASA rows; want-set includes the three MOVE chapters). Pack-set fails today (`is-gps-200n`, `nasa-std-8719-14` missing). | Does not walk `packs/*/chapters` vs JSON chapter fields (W1). |
| 12-01 T2 | Yes. THRESHOLDS today lack DA/Validation/Integration/Ops and Interfaces is 3 not 4. Gate is RED until T1+T2. | Gate run covers chapter-set that T1 skipped. |
| 12-01 T3 | Yes. CONTRACT today has no 628 live-snapshot paragraph (502 appears only as residue context after the edit). | Does not grep the section 5 floor table (W2). |
| 12-02 T1 | Yes. `check_capability_map` absent from `check_release.py` today. | subprocess check is a short-window string slice; acceptable. |
| 12-02 T2 | Yes. BOM present; `.gitattributes` absent; four nits live. | None material. |
| 12-02 T3 | Yes. SUMMARY does not exist yet; keywords required. | Path B URL is optional in the action; verify only requires keywords (matches ROADMAP). |

---

## Findings

### Warnings (should fix; execution can proceed)

**W1. [verification_derivation] 12-01 Task 1 verify is pack-level, not chapter-set**
- Plan: 12-01 Task 1
- Action / done require all 16 unmapped chapter files classified. Automated verify asserts disk-vs-map **pack** sets, uniqueness, and the MOVE membership. An executor could add one row per new slug and leave leftover RPG / remaining 8719/200N files unmapped; T1 would still print `MAP_MOVE_OK`.
- T2 `python tooling/check_capability_map.py` would then fail chapter-set staleness -- recoverable, but T1 can be marked done too early.
- Fix: add a chapter-file set-diff to T1 verify (`packs/*/chapters/*.md` vs JSON `(pack, chapter)`), or run the map gate in T1 and treat THRESHOLDS failures as the only expected RED (plan already allows adding THRESHOLDS in-session if the commit stays on T2).

**W2. [verification_derivation] 12-01 Task 3 does not assert the section 5 threshold table**
- Plan: 12-01 Task 3
- Action + acceptance require section 5 to match the new floors (Interfaces >=4; add DA/Validation/Integration/Ops >=4). Automated verify only greps 628 / 502 / Cybersecurity / Digital Engineering / unbound.
- Fix: grep CONTRACT for the four new cluster names (or `Decision Analysis`) alongside the 628/502 paragraph.

**W3. [nyquist] 12-VALIDATION.md Per-Task map lumps the six execute tasks**
- File: 12-VALIDATION.md
- Rows: 12-01-01 (MAP-19-01/02/03), 12-01-02 (MAP-19-05), 12-02-01 (MAP-19-04), 12-02-02 (HYG-01..04). Actual plans are 3+3 tasks; T2 THRESHOLDS and T3 HYG-03 are not named.
- Fix: add rows for 12-01-02 THRESHOLDS/conjunct and 12-02-03 HYG-03, or leave as advisory (Nyquist 8a-8d still pass).

**W4. [research_resolution] Open Questions not marked RESOLVED**
- File: 12-RESEARCH.md Open Questions (no suffix; no inline RESOLVED)
- All four items already have Recommendations the plans followed (Integration floor-held; `map_version` 1.18.0; HYG-03 Path A or B; ch11 not force-fit to Validation).
- Fix: retitle `Open Questions (RESOLVED)` and prefix each item RESOLVED with the plan-chosen path. Do not reopen the decisions.

### Non-issues (checked, not raised)

- `claim_verification` present, non-empty, and live-accurate on both plans.
- Remap is MOVE: delete-from + insert-into table; DA exact five-row set; Opportunity/Assurance absence asserts.
- No version bump: `map_version` stays 1.18.0; version trio asserted; no `## [1.19.0]`; no v1.19* tag.
- Wire happens AFTER map is GREEN: wave 2 + hard STOP + T1 of 12-01 does not touch `check_release.py`.
- HYG-03 may be external PR: Path B is a valid close; vendoring forbidden.
- MAP-19 / HYG boxes left unchecked -- correct; verify owns the ticks.
- Integration "must move" treated as floor-held 4/4 -- RESEARCH Q1, not a reduction.
- FUT-05 generator, AAF/CBA/DoDM/stakeholder packs, Cyber/DE bindings, CI repo-Python, catalog 10->13 all forbidden in must-NOT + verify.
- 12-02 10 files is the warning threshold; RESEARCH Wave B shape stands -- do not split.
- Structure-tool #429 on unquoted `http` is a false positive.
- No CONTEXT.md / CLAUDE.md -- those dimensions skipped, not failed.
- Unclassified `.edge-coverage.json` probes left unresolved by explicit must_haves (`EDGE_ABSENT=1`).
- 12-01 T1 expected 644 is not a hard equality (support-file omit is discretion).

---

## Structured issues

```yaml
issues:
  - plan: "12-01"
    dimension: verification_derivation
    severity: warning
    task: 1
    description: "Task 1 automated verify asserts pack-set coverage and MOVE membership but not chapter-file staleness for the 16 unmapped files. Done can go green before every leftover RPG / 8719 / 200N chapter is classified."
    fix_hint: "Add packs/*/chapters vs JSON (pack, chapter) set-diff to T1 automated, or run check_capability_map.py in T1 and accept only THRESHOLDS as expected remaining failures."

  - plan: "12-01"
    dimension: verification_derivation
    severity: warning
    task: 3
    description: "Task 3 acceptance requires CONTRACT section 5 threshold table to match new floors; automated verify only greps the MAP-19-05 paragraph tokens."
    fix_hint: "Grep CONTRACT for Decision Analysis / Validation / Integration / Operations, Maintenance plus Interfaces >=4 (or the four new cluster names)."

  - plan: null
    dimension: nyquist
    severity: warning
    description: "12-VALIDATION.md Per-Task map has four lumped rows and does not name 12-01 T2 THRESHOLDS or 12-02 T3 HYG-03."
    fix_hint: "Add 12-01-02 (THRESHOLDS + conjunct + gate PASS) and 12-02-03 (HYG-03 Path A/B + both gates) before execute, or leave as advisory."

  - plan: null
    dimension: research_resolution
    severity: warning
    description: "12-RESEARCH.md Open Questions has neither a (RESOLVED) suffix nor inline RESOLVED markers, though each item already has a Recommendation the plans implemented."
    fix_hint: "Mark the section Open Questions (RESOLVED) and stamp each item RESOLVED with the chosen path. Do not change verdicts."
```

---

## Recommendation

blockers: 0. 4 warnings. Verdict **PASS_WITH_FIXES**.

Highest-leverage pre-execute nits (same plans, no split): chapter-set assert on 12-01 T1; CONTRACT section 5 greps on T3; stamp Open Questions resolved; optionally expand VALIDATION.md rows.

Plans reduce 0 locked user decisions (no CONTEXT.md; RESEARCH constraints delivered in full). Remap is MOVE. No version bump. Wire is after GREEN. HYG-03 may be an external PR. No phase split required. Execute can proceed; the warnings are verify-strictness and research-hygiene, not missing coverage of MAP-19 / HYG.

**Verdict:** PASS_WITH_FIXES

## ISSUES FOUND

**Phase:** 12-map-regen-hygiene-gate-wiring
**Plans checked:** 2
**Issues:** blockers: 0, 4 warning(s), 0 info

### Warnings (should fix)

**1. [verification_derivation] 12-01 T1 verify is pack-level, not chapter-set**
- Plan: 12-01
- Task: 1
- Fix: add chapter-file set-diff (or run the map gate) in T1 automated verify

**2. [verification_derivation] 12-01 T3 does not assert CONTRACT section 5 floors**
- Plan: 12-01
- Task: 3
- Fix: grep the new threshold cluster names in CONTRACT

**3. [nyquist] VALIDATION.md lumps execute tasks**
- Plan: null
- Fix: add THRESHOLDS and HYG-03 rows

**4. [research_resolution] Open Questions unmarked**
- Plan: null
- Fix: Open Questions (RESOLVED) + inline RESOLVED stamps

Plans verified with warnings only. Run `/gsd:execute-phase 12` after optional nits, or proceed and treat the extra acceptance greps as executor checklist items.
