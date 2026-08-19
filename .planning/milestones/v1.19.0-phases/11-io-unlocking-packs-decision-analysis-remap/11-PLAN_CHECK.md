# Phase 11 Plan Check

**Phase:** 11-io-unlocking-packs-decision-analysis-remap
**Plans checked:** 2 (`11-01-PLAN.md`, `11-02-PLAN.md`)
**Checked:** 2026-08-17
**Method:** Goal-backward verification against ROADMAP Phase 11 goal + SC-1..SC-5, REQUIREMENTS IO-01..07, `11-RESEARCH.md` (GO/NO-GO + recommended shape), `11-PATTERNS.md`, `11-VALIDATION.md`, `docs/SOURCE-VETTING.md` Phase 11 handoff, and live re-measurement of every `claim_verification` row.

**Verdict:** PASS_WITH_FIXES

The two waves will move the poorest primaries without silent ticks if the executor follows the actions: build 8719.14C + IS-GPS-200N, extend `dod-vva-rpg` (or honestly defer), write the IO-01 remap table only, record AAF deferrals and stakeholder accept, thin-register the two new slugs. No map JSON edit, no Army CBA / AAF / stakeholder / SP-7084 must-build. Several automated gates do not cover the authorized IO-02 fetch-failure path or every acceptance line. Fix those before execute if the verifier scores the written commands strictly. Do not treat this as a rewrite.

---


## Goal-backward trace

Phase goal: *Poorest competency primaries move; no silent ticks (consumes Phase 10: build 8719.14C + IS-GPS-200N; remap/defer Army CBA, DoDM 5000.102, AAF; SP-7084 optional)*

| Success criterion | Required truth | Covering task | Provably delivered? |
|---|---|---|---|
| SC-1 / IO-01 -- Decision Analysis leaves 2 (new pack **or** MAP-19-03 remap) | Apply-ready remap table; no CBA pack; no live map edit this phase | 11-02 T2 (table in SUMMARY + REQUIREMENTS pointer) | **Yes as specified.** RESEARCH Pattern 4: Phase 11 writes the table; Phase 12 MAP-19-03 applies it. Live count leave-2 is **not** a Phase 11 JSON contract. User brief: IO-01 is table-only. |
| SC-2 / IO-02 -- Validation gained a new pack **or** documented deferral | Leftover RPG chapters in `dod-vva-rpg` **or** dated DEFERRED; no `dodm-5000-102` | 11-02 T1 | **Yes in the action.** DoDM was the new-pack path and stays deferred; depth moves via chapters. Alternate fetch-failure path is written. Verify on the happy path requires chapters > 10 (see W1). |
| SC-2 / IO-03 -- Ops/Maint/Disposal gained a new pack | `packs/nasa-std-8719-14` gated | 11-01 T1 | **Yes.** Pattern 1 + P11-PRE-1 hard gate + analog nasa-ms-7009. |
| SC-2 / IO-04 -- Interface Management gained a new pack | `packs/is-gps-200n` ICD exemplar gated | 11-01 T2 | **Yes.** 200N only; Apps II-IV not transcribed; no 705J/800J/IS-300/ICD-GPS-153. |
| SC-3 / IO-05 + IO-06 -- Integration + Logistics only if AAF cleared; else deferred-recorded | Dated DEFERRED; no `packs/aaf-*` | 11-02 T2 | **Yes.** Pattern 5 template. Boxes stay open. |
| SC-4 / IO-07 -- Stakeholder outcome recorded; no invented pack | Dated ACCEPT; no stakeholder pack | 11-02 T2 | **Yes.** Discretion chose accept (not SEBoK rematch-as-substitute). |
| SC-5 -- each built pack: PACK-SPEC + validate + scan + overlap + When-to-use/Prerequisites | Gate chain on both new packs + extended RPG | 11-01 T1/T2, 11-02 T1 | **Yes in the actions.** Shared PATTERNS validation chain is copied into each pack task. |
| No silent ticks / no Phase 12-13 steal | Boxes open; map JSON untouched; no REL-19-02 / version bump | both plans + 11-02 T3 thin-register exception | **Yes.** Thin-register is RESEARCH-recommended so `check_release.py` stays green on `main`. Version stays 1.18.0. |

Requirements frontmatter: 11-01 lists [IO-03, IO-04]; 11-02 lists [IO-01, IO-02, IO-05, IO-06, IO-07]. No ROADMAP requirement ID is missing from all plans.

claim_verification is present and populated on both plans (not missing/empty). Live re-run matches every current-state row (see below).


---

## First principles / inversion

**Current Assumptions:**
- Assumption 1: SC-1 requires a live Decision Analysis count change in Phase 11 -- challenged: **false**. REQUIREMENTS puts IO-01 here and MAP-19-03 in Phase 12. RESEARCH Pattern 4 + user brief lock table-only.
- Assumption 2: SC-2 "new pack" forces a Validation slug -- challenged: **false**. ROADMAP allows documented deferral; IO-02 is additional VV&A chapters; inventing `dodm-5000-102` is forbidden.
- Assumption 3: Thin-register steals REL-19-01 -- challenged: **partially**. Full registration + tag is Phase 13; catalog/SKILLS/cursor rows are the mechanical exception so new dirs can exist on `main`.
- Assumption 4: Two full pack builds in 11-01 exceed the phase contract -- challenged: **false**. RESEARCH recommended Wave A shape; estimate 90000 < 100000 smart-zone.

**Fundamental Truths:**
- Phase 10 GO/NO-GO is authoritative. Build only 8719.14C + IS-GPS-200N. Remap/defer the rest.
- A dated DEFERRED/ACCEPT parenthetical with an open checkbox is a valid close. A silent tick is not.
- `docs/capability-pack-map.json` is Phase 12-owned. Editing it here double-builds MAP-19-03.

**Guaranteed Failure Modes:**
1. Build Army CBA / DoDM / AAF / stakeholder / SP-7084: Avoid by files_modified + must-NOT + verify test ! -d.
2. Apply remap to live JSON: Avoid by excluding the map from files_modified; every task checks `git diff --name-only -- docs/capability-pack-map.json`.
3. Treat Tier 1 leaning as skip-confirm: Avoid by P11-PRE-1 / P11-PRE-2 / P7-PRE-4 hard gates before GENERATE.
4. Silent-tick IO-05/06/07: Avoid by boxes stay open + dated parentheticals.
5. GPS appendix dump / IS-300 hunt: Avoid by exemplar chapter table + forbidden-slug asserts.
6. URL / source leak: Avoid by tree grep + git show leak check + sources/ gitignored.

**Anti-Goals (Never Do):**
- Invent a pack to satisfy a noun in ROADMAP SC-2
- Tick an IO box in execute
- Tag v1.19.0 / bump plugin to 1.19.0
- Copy research-store URLs into packs/ or `docs/SOURCE-VETTING.md`

**Remaining Risk:** A fetch failure on the T&E/V&V Checklist still fails 11-02 T1 automated even though the action authorizes partial deferral (W1). Single-hit greps can miss a missing IO-05 or IO-07 sentence (W2).


---

## Dimension results

| Dim | Result | Notes |
|---|---|---|
| 1 Requirement coverage | PASS | All seven IO IDs appear in a plan requirements field and have a covering task. MAP/HYG/REL IDs correctly stay Phase 12/13. |
| 2 Task completeness | PASS with verify defects | verify.plan-structure: 5 auto tasks, all have Files + Action + Verify + Done. 11-02 T1 verify contradicts the authorized deferral path (W1). |
| 3 Dependencies | PASS | 11-01 wave 1 depends_on []. 11-02 wave 2 depends_on ["11-01"] (same convention as 10-02 to 10-01). Acyclic. Thin-register waits for both new dirs. |
| 4 Key links | PASS | SKILL.md to chapters/; is-gps-200n to faa-std-025; remap table to Phase 12 MAP-19-03; catalog to new slugs; PACK.yaml notes to P11-PRE quotes (no URL). |
| 5 Scope sanity | PASS with note | 11-01: 2 tasks / two pack trees. 11-02: 3 tasks / 10 listed paths. estimate-check --calibrated: 90000 (0.90) and 70000 (0.70) of 100000; over_budget false. Plan confidence medium vs tool confidence low (sample_count: 0) -- advisory only. Do not split Wave A. |
| 6 Verification derivation | WARN | must_haves truths are user-observable. T1 happy-path vs deferral-path conflict (W1). T2 DEFERRED/ACCEPT greps are single-hit (W2). Map-untouched check is working-tree git diff, not git show (W3). |
| 7 Context compliance | SKIPPED (no CONTEXT.md) | Discuss skipped. Locked RESEARCH user_constraints honored: GO names only, no CBA/DoDM/AAF/stakeholder packs, no URLs, leaning is not skip-confirm, stay on main. |
| 7b Scope reduction | PASS | IO-01 table-only is the locked path, not a silent v1. SP-7084 skip is YAGNI discretion. IO-02 chapters-not-a-pack is RESEARCH Q2, with DoDM deferral documented so SC-2 still holds. |
| 7c Architectural tier | PASS | Responsibility map is pack trees + planning records + optional thin-register. Tasks match those tiers. No client/API/DB misplacement. |
| 8 Nyquist | PASS with VALIDATION drift | 11-VALIDATION.md exists. All five tasks have automated verify (no MISSING, no --watch, latency ~30s). Sampling 2/2 and 3/3. Wave 0 N/A (existing tooling). VALIDATION map omits 11-02 T3 (W4). |
| 9 Cross-plan contracts | PASS | 11-01 produces dirs and leaves catalog at 61. 11-02 consumes dirs and thin-registers to 63. No conflicting transform on the same stream. Map JSON untouched in both. |
| 10 CLAUDE.md | SKIPPED | No ./CLAUDE.md. |
| 11 Research resolution | WARN | Open Questions has no (RESOLVED) suffix and no inline RESOLVED markers (W5). Each item already has a Recommendation the plans implemented. |
| 12 Pattern compliance | PASS | New/modified files map to PATTERNS.md analogs (nasa-ms-7009, faa-std-025, self+federal-bca, remap table). Shared licence / provenance / gate-chain / When-to-use patterns are in the covering tasks. |

### Smart-zone estimates

| Plan | estimate.tokens | budget | over_budget | plan confidence | tool confidence |
|---|---|---|---|---|---|
| 11-01 | 90000 | 100000 | false | medium | low (sample_count: 0) |
| 11-02 | 70000 | 100000 | false | medium | low (sample_count: 0) |


### Dimension 8: Nyquist Compliance

| Task | Plan | Wave | Automated Command | Status |
|------|------|------|-------------------|--------|
| T1 nasa-std-8719-14 | 11-01 | 1 | validate_pack + overlap + scan + When-to-use/Prerequisites + Internet Public + no URL + chars/page >= 300 + leak/map | PASS |
| T2 is-gps-200n | 11-01 | 1 | same gates + faa-std-025 + DIST-A + SAIC watch-item + forbidden GPS slugs | PASS |
| T1 extend dod-vva-rpg | 11-02 | 2 | validate_pack + chapters > 10 + no dodm-5000-102 + overlap loop + no URL + leak/map | PASS (happy path only; W1) |
| T2 remap + defer/accept | 11-02 | 2 | IO-01 chapter names + DEFERRED + ACCEPT + open boxes + no aaf/cba/stakeholder/sp-7084 + map/http | PASS (single-hit greps; W2) |
| T3 thin-register | 11-02 | 2 | catalog 63 + SKILLS 63(+2) + NOTICE blocks + cursor 1.18.0 + packs-63 + check_release PASS | PASS |

Sampling: Wave 1: 2/2 verified -> PASS. Wave 2: 3/3 verified -> PASS.
Wave 0: none required -> PASS (existing validate_pack / REF scan-overlap / grep).
Overall: PASS (VALIDATION.md omits thin-register row -- W4).

verify.plan-structure #429 warning on unquoted http in 11-02 is a **false positive** -- the grep is a Link Policy ban, not a required echo (same class as Phase 10).


---

## Targeted checks (orchestrator brief)

### Requirement to task mapping

| Req | Planned delivery | Gap |
|---|---|---|
| IO-01 | 11-02 T2 remap table (federal-bca ch04 + ch06, dod-vva-rpg ch06) in SUMMARY; REQUIREMENTS pointer; no `docs/capability-pack-map.json` edit; no CBA pack | Table-only confirmed. Live leave-2 is Phase 12. |
| IO-02 | 11-02 T1 Checklist + <=2 topics in dod-vva-rpg; no dodm-5000-102; fetch-fail -> DEFERRED | Verify does not implement the alternate pass (W1). |
| IO-03 | 11-01 T1 nasa-std-8719-14; P11-PRE-1 quote | None in the action. |
| IO-04 | 11-01 T2 is-gps-200n exemplar; P11-PRE-2 DIST-A; no Apps II-IV dump | Optional +705J/+800J correctly not required. |
| IO-05 | 11-02 T2 dated DEFERRED; no AAF pack | Verify is single-hit DEFERRED (W2). |
| IO-06 | 11-02 T2 dated DEFERRED; no AAF pack | Same as IO-05. |
| IO-07 | 11-02 T2 dated ACCEPT; no invented pack | Verify is single-hit ACCEPT (W2). |

### Locked prohibitions (confirmed present)

| Prohibition | Where encoded | Live now |
|---|---|---|
| No map JSON edit | files_modified excludes it; every task verify; must_haves | `git diff --name-only -- docs/capability-pack-map.json` empty |
| No AAF / Army CBA / stakeholder packs | 11-02 T2 test ! -d + must-NOT | dirs absent |
| No SP-7084 must-build | skip / test ! -d packs/nasa-sp-7084 | dir absent |
| IO-01 table-only | 11-02 T2 Pattern 4; EDGE_ABSENT=1 on numeric leave-2 | map Decision Analysis still 2/2 |
| No silent ticks | boxes stay open; verify counts open IO lines | all IO-01..07 still open |


### claim_verification accuracy (live re-run, 2026-08-17)

| Plan | Claim | Live | Status |
|---|---|---|---|
| 11-01 | Branch is main | main | Accurate |
| 11-01 | 63 pack dirs; neither new slug exists | 63; grep empty | Accurate |
| 11-01 | Catalog 61; SKILLS 61(+2); cursor 62; README packs-61 | 61 / 61 packs (+2 signposts) / 62 / packs-61 | Accurate |
| 11-01 | New slugs absent from catalog / SKILLS / NOTICE | False/False; SKILLS 0/0; NOTICE 0/0 | Accurate |
| 11-01 | Analog trees have full PACK-SPEC file list | both have SKILL/PACK/LICENSE/chapters/glossary/patterns/cheatsheet | Accurate |
| 11-01 | Sibling REF pipeline tools exist | all six paths present | Accurate |
| 11-01 | Repo tooling present | build_pack, check_capability_map, check_release, gen_packs_page, validate_pack | Accurate |
| 11-01 | check_release PASS | RELEASE CHECK: PASS | Accurate |
| 11-01 | grep -c http SOURCE-VETTING | 0 | Accurate |
| 11-01 | sources/ gitignored | .gitignore:17 | Accurate |
| 11-01 | Phase 11 handoff heading | line 168 | Accurate |
| 11-01 | Map schema 2 / 1.18.0; DA 2/2; Interfaces 4/3; Ops/Maint 6/4 | schema 2, map_version 1.18.0; DA 2/2; IM 4/3; Ops 6/4 | Accurate |
| 11-01 | IO-03/IO-04 boxes open | both open with Phase 10 GO notes | Accurate |
| 11-02 | dod-vva-rpg 10 chapters; source_pages 283 | 10 files; source_pages: 283 / chapters: 10 | Accurate |
| 11-02 | TEVV checklist named as selection drop | PACK.yaml line 42 | Accurate |
| 11-02 | No dodm/aaf/army-cba/sp-7084/is-gps slugs | empty | Accurate |
| 11-02 | federal-bca ch04 + ch06; no Decision Analysis Topic Index row | both chapter files present; Decision only in body/ch06 title | Accurate |
| 11-02 | dod-vva-rpg Decision analysis row | line 76 ch06, ch08, ch10 | Accurate |
| 11-02 | Live map DA 2/2; Opportunity 10/2; Validation 5/4 | 2/2, 10/2, 5/4 | Accurate |
| 11-02 | Registration basis 63/61/61(+2)/62/packs-61/1.18.0 | matches | Accurate |
| 11-02 | Analog catalog object keys | slug, title, publisher, source_version, license, license_tier, commercial_use, chapters, status live | Accurate |
| 11-02 | IO boxes open; no Phase 11 DEFERRED/ACCEPT yet | all open; grep DEFERRED/ACCEPT empty | Accurate |

No missing/empty claim_verification. No numeric conflict with RESEARCH that required a prescribed correction. Future-state rows (post-11-01 dirs 65 / catalog still 61) are labeled expected, not current.


### Verify-command audit

No 2>/dev/null || echo 0, no || true feeding a comparison, no caret-anchored package-manager grep.

| Task | Distinguishes pre-phase tree? | Residual |
|---|---|---|
| 11-01 T1 | Yes. Pack dir absent today; validate_pack would fail. Internet Public / 8719.14C greps are new. | Does not assert heading adjacency of When-to-use then Prerequisites (count-only). |
| 11-01 T2 | Yes. Same plus faa-std-025 / DIST-A / SAIC / forbidden slugs absent today. | Same adjacency gap. |
| 11-02 T1 | Yes on chapters > 10 (live = 10). | Authorized fetch-failure path cannot pass this block (W1). Overlap loop no-ops if extracts missing. |
| 11-02 T2 | Yes on DEFERRED/ACCEPT (live empty) and the three chapter-name tokens in REQUIREMENTS (live absent as a remap list). | Single-hit greps (W2). Does not assert SUMMARY heading (plan output does). Map check is working-tree only (W3). |
| 11-02 T3 | Yes. Catalog 61 today; 63 + new slugs will fail until T3 runs. plugin version assert is distinctive. | Hard-coded 63 has claim_verification provenance (61+2). |

---

## Findings

### Warnings (should fix; execution can proceed)

**W1. [verification_derivation] 11-02 Task 1 verify cannot pass the authorized IO-02 deferral path**
- Plan: 11-02 Task 1
- Action + acceptance allow Checklist fetch failure -> IO-02 DEFERRED, chapter count stays 10, no DoDM substitute. Automated verify requires ls chapters | wc -l > 10 and PACK.yaml chapters > 10.
- Fix: wrap the >10 asserts in an either-or: chapters > 10 **or** (grep IO-02 parenthetical DEFERRED and still no packs/dodm-5000-102). Keep overlap loop only when chapter_fulltexts/ch1*.txt exist.

**W2. [verification_derivation] 11-02 Task 2 DEFERRED/ACCEPT greps are single-hit**
- Plan: 11-02 Task 2
- IO-05 and IO-06 both need dated DEFERRED; IO-07 needs dated ACCEPT. grep -n DEFERRED / ACCEPT exit 0 on one match.
- Fix: bind greps per ID: grep IO-05 | grep DEFERRED, grep IO-06 | grep DEFERRED, grep IO-07 | grep ACCEPT.

**W3. [verification_derivation] map-untouched check is working-tree git diff, not commit-scoped**
- Plans: 11-01 T1/T2, 11-02 T1/T2/T3
- After a commit that included docs/capability-pack-map.json, git diff --name-only -- docs/capability-pack-map.json is empty.
- Fix: also test -z "$(git show --name-only --pretty=format: HEAD | grep capability-pack-map.json)" on each scoped commit (same shape as the sources/ leak check).

**W4. [nyquist] 11-VALIDATION.md Per-Task map omits thin-register**
- File: 11-VALIDATION.md
- Rows cover 11-01-01, 11-01-02, 11-02-01 (IO-02), 11-02-02 (IO-01), 11-02-03 (IO-05/06/07). 11-02 Task 3 (check_release / catalog 63) is missing.
- Fix: add a 11-02-04 row for thin-register before execute, or leave as advisory (Nyquist 8a-8d still pass).

**W5. [research_resolution] Open Questions not marked RESOLVED**
- File: 11-RESEARCH.md Open Questions (no suffix; no inline RESOLVED)
- All four items already have Recommendations the plans followed (thin-register; chapters-not-a-pack + DoDM deferral reading; Checklist + <=2 at execute; fetch-fail -> partial deferral).
- Fix: retitle Open Questions (RESOLVED) and prefix each item RESOLVED with the plan-chosen path. Do not reopen the decisions.


### Non-issues (checked, not raised)

- claim_verification present, non-empty, and live-accurate on both plans.
- IO-01..07 boxes left unchecked -- correct; verify owns the ticks.
- IO-01 is table-only -- locked, not a reduction. Decision Analysis live count stays 2/2 until Phase 12.
- No docs/capability-pack-map.json in any files_modified.
- No AAF / Army CBA / stakeholder / dodm-5000-102 / SP-7084 build task.
- Optional +705J/+800J correctly declined (YAGNI; one exemplar).
- Thin-register does not bump plugin version, CHANGELOG, or tag REL-19-02.
- 11-01 90000-token estimate is under budget; RESEARCH Wave A shape stands.
- Structure-tool #429 on unquoted http is a false positive.
- No CONTEXT.md / CLAUDE.md -- those dimensions skipped, not failed.
- Unclassified .edge-coverage.json probes left unresolved by explicit must_haves (EDGE_ABSENT=1) -- do not invent check_kind / check_target.
- 11-02 T3 hard-coded catalog/SKILLS 63 is measured (61+2) in this plan claim_verification.

---

## Structured issues

```yaml
issues:
  - plan: "11-02"
    dimension: verification_derivation
    severity: warning
    task: 1
    description: "Task 1 automated verify requires dod-vva-rpg chapter count > 10, but the action/acceptance authorize IO-02 partial deferral at count 10 if Checklist cannot be fetched."
    fix_hint: "Either-or the >10 asserts with IO-02 DEFERRED + no packs/dodm-5000-102. Run overlap only when chapter_fulltexts exist."

  - plan: "11-02"
    dimension: verification_derivation
    severity: warning
    task: 2
    description: "grep DEFERRED and ACCEPT are single-hit gates; one parenthetical satisfies both IO-05 and IO-06, and ACCEPT is not bound to IO-07."
    fix_hint: "Per-ID greps: IO-05+DEFERRED, IO-06+DEFERRED, IO-07+ACCEPT."

  - plan: "11-01"
    dimension: verification_derivation
    severity: warning
    task: 1
    description: "Map-untouched check is working-tree git diff; a commit that added capability-pack-map.json would still pass."
    fix_hint: "Add git show --name-only HEAD grep for capability-pack-map.json on each scoped commit (same as sources/ leak check). Apply to 11-01 T2 and all 11-02 tasks as well."

  - plan: null
    dimension: nyquist
    severity: warning
    description: "11-VALIDATION.md Per-Task map has no row for 11-02 Task 3 thin-register / check_release."
    fix_hint: "Add 11-02-04 covering catalog 63 + check_release PASS + plugin version 1.18.0."

  - plan: null
    dimension: research_resolution
    severity: warning
    description: "11-RESEARCH.md Open Questions has neither a (RESOLVED) suffix nor inline RESOLVED markers, though each item already has a Recommendation the plans implemented."
    fix_hint: "Mark the section Open Questions (RESOLVED) and stamp each item RESOLVED with the chosen path. Do not change verdicts."
```

---

## Recommendation

0 blockers. 5 warnings. Verdict **PASS_WITH_FIXES**.

Highest-leverage pre-execute nits (same plans, no split): either-or the 11-02 T1 chapter-count gate with the written deferral path; bind DEFERRED/ACCEPT greps to IO-05/06/07; optionally git show the map file on each commit; stamp Open Questions resolved; add the thin-register row to VALIDATION.md.

Plans reduce 0 locked user decisions (no CONTEXT.md; RESEARCH constraints delivered in full). No phase split required. Execute can proceed; the warnings are verify-strictness and research-hygiene, not missing coverage of IO-01..07.

**Verdict:** PASS_WITH_FIXES

## ISSUES FOUND

**Phase:** 11-io-unlocking-packs-decision-analysis-remap
**Plans checked:** 2
**Issues:** 0 blocker(s), 5 warning(s), 0 info

### Warnings (should fix)

**1. [verification_derivation] 11-02 T1 verify cannot pass authorized IO-02 deferral**
- Plan: 11-02
- Task: 1
- Fix: either-or chapters > 10 with IO-02 DEFERRED + no dodm-5000-102

**2. [verification_derivation] 11-02 T2 DEFERRED/ACCEPT greps are single-hit**
- Plan: 11-02
- Task: 2
- Fix: per-ID greps for IO-05/06 DEFERRED and IO-07 ACCEPT

**3. [verification_derivation] map-untouched check is working-tree only**
- Plan: 11-01 / 11-02
- Fix: also git show HEAD for capability-pack-map.json on each scoped commit

**4. [nyquist] VALIDATION.md omits thin-register task**
- Plan: null
- Fix: add 11-02-04 row for catalog 63 + check_release

**5. [research_resolution] Open Questions unmarked**
- Plan: null
- Fix: Open Questions (RESOLVED) + inline RESOLVED stamps

Plans verified with warnings only. Run /gsd:execute-phase 11 after optional nits, or proceed and treat the extra acceptance greps as executor checklist items.

