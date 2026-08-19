# Phase 11: Gap Analysis — IO-unlocking packs + Decision Analysis remap

**Date:** 2026-08-17
**Inputs:** 11-IMPL_REVIEW, 11-CODE_REVIEW, 11-INTEGRATION_CHECK, 11-SECURITY_AUDIT (all four present, none skipped) + ROADMAP Phase 11 success criteria SC-1..5 + REQUIREMENTS IO-01..07 + 11-01/11-02 SUMMARY + live gate re-verify + analog 10-GAP_ANALYSIS.md
**Method:** Adjudication of all post-execute findings against ROADMAP Phase 11 success criteria and phase goal ("Poorest competency primaries move; no silent ticks"), with independent live re-verification of gates on `main` at HEAD after review artifacts (`c41565f` code_review / prior execute through `2309329`).

**Verdict:** CLOSED

## Review Inventory

| Review | Verdict | Blocker | Major | Minor | Info/Warn/Notes | Post-review state |
|---|---|---|---|---|---|---|
| 11-IMPL_REVIEW | PASS_WITH_NOTES | 0 | 0 | 1 (MN-01) | — | Plan-authorized catalog `dod-vva-rpg.chapters` lag (10 vs 13); packs/gates green |
| 11-CODE_REVIEW | PASS_WITH_NOTES | 0 | 0 | 0 | 3 INFO (IN-01..03) | Plan hygiene + advisory stamps + stale close-out arithmetic; packs faithful |
| 11-INTEGRATION_CHECK | PASS_WITH_NOTES | 0 | 0 | — | 5 NOTES | Phase 12 consumption chain COMPLETE; map RED is intentional start state |
| 11-SECURITY_AUDIT | SECURED | 0 | 0 | 0 | 4 notes (N1–N4) | 10/10 declared threats CLOSED; threats_open = 0 |

No review returned NEEDS_WORK. No blocker or major finding remains open. Honest deferral (IO-05/06) and ACCEPT (IO-07) with dated evidence, plus remap-table-not-applied (MAP-19-03 / Phase 12), are valid close paths per plan and ROADMAP SC wording.

## Live Gate Re-Verification (gap-analysis time)

| Gate | Result | Notes |
|---|---|---|
| `python tooling/validate_pack.py packs/nasa-std-8719-14` | **PASS** | exit 0 |
| `python tooling/validate_pack.py packs/is-gps-200n` | **PASS** | exit 0 |
| `python tooling/validate_pack.py packs/dod-vva-rpg` | **PASS** | exit 0; 13 chapter files on disk |
| `python tooling/check_release.py` | **PASS** | plugin still **1.18.0** |
| Forbidden packs (`aaf-*`, `army-cba`, stakeholder, `nasa-sp-7084`, `dodm-5000-102`, 705J/800J/ICD-GPS-153, …) | **none** | `ls packs \| grep -Ei …` empty |
| IO-01..07 boxes open / checked | **7 / 0** | all `- [ ]`; no silent ticks |
| `grep IO-05 \| DEFERRED` / `IO-06 \| DEFERRED` / `IO-07 \| ACCEPT` | **all hit** | REQUIREMENTS parentheticals dated 2026-08-17 |
| `git diff -- docs/capability-pack-map.json` | **empty (0 bytes)** | last touch still `dc35907` (Phase 8) |
| `grep -c http docs/SOURCE-VETTING.md` | **0** | Link Policy holds |
| `grep -RInE 'https?://'` on three pack trees | **empty** | pack Link Policy holds |
| Thin-register arithmetic | catalog **63** / dirs **65** / cursor skills **64** | both GO slugs present; `dod-vva-rpg.chapters` still **10** (Phase 13) |
| Remap source files on disk | **present** | `federal-bca` ch04 + ch06; `dod-vva-rpg` ch06-accreditation-agent-role |
| Branch | `main` | — |

## Success-Criteria Cross-Check (ROADMAP Phase 11)

| Criterion | Requirement | Status | Evidence (reproduced at gap-analysis time) |
|---|---|---|---|
| SC-1: Decision Analysis cluster count leaves 2 (new pack and/or MAP-19-03 remap of A-94 / VV&A decision chapters) | IO-01 | **VERIFIED (spec path)** | Remap **specified** in 11-02-SUMMARY three-row table + REQUIREMENTS names three chapters. Live JSON leave-2 / map apply is **Phase 12** (Pattern 4 / EDGE_ABSENT). No CBA pack. Map blob untouched. |
| SC-2: Validation, Ops/Maint/Disposal, Interface Management each gained at least one new pack *or* documented deferral | IO-02, IO-03, IO-04 | **VERIFIED** | Ops: `nasa-std-8719-14` (7 ch). Interfaces: `is-gps-200n` (6 ch). Validation: chapters-not-a-pack — leftover RPG ch11–ch13 in `dod-vva-rpg` (10→13); no `dodm-5000-102`. |
| SC-3: Integration + Logistics built only if AAF cleared; otherwise deferred-recorded | IO-05, IO-06 | **VERIFIED (deferral path)** | Dated DEFERRED parentheticals; no AAF pack; VET-19-03 still "NOT yet vetted — do not use". |
| SC-4: Stakeholder Engagement outcome recorded (SEBoK expansion or accept) — no invented pack | IO-07 | **VERIFIED (accept path)** | Dated ACCEPT; no stakeholder pack; SEBoK rematch explicitly not a substitute. |
| SC-5: Each built pack: PACK-SPEC + validate_pack + scan + overlap + When-to-use/Prerequisites | IO-03/04 + extended RPG | **VERIFIED** | Live validate_pack PASS ×3; reviews re-ran scan + overlap exit 0; When-to-use + Prerequisites present (analog adjacency accepted). |
| Phase goal: poorest competency primaries move; no silent ticks | IO-01..07 | **VERIFIED** | Two GO packs built; Validation depth via chapters; remap specified; AAF deferred; stakeholder accepted; all seven IO boxes still `- [ ]`. |

## Thread Adjudication

### Thread 1 — Honest deferrals / accept (IO-05/06/07): closable, not OPEN_GAPS

Phase 11's job for AAF and stakeholder was **recording**, not inventing packs. SC-3 requires deferred-recorded when AAF is not cleared; SC-4 requires a recorded accept/expansion outcome with no invented pack.

All three dispositions are:
1. Dated 2026-08-17 in REQUIREMENTS with source / why / not-built / unblock
2. Bound greps (`IO-05|DEFERRED`, `IO-06|DEFERRED`, `IO-07|ACCEPT`) hit at gap-analysis time
3. Explicitly non-build (no `packs/aaf-*`, no stakeholder pack)
4. Mirrored in 11-02-SUMMARY and security T-11-03 / T-11-07 tick boundaries

Adjudicated **not gaps**. Re-opening execute to invent AAF or stakeholder packs would violate Phase 10 NO-GO and VET-19-03.

### Thread 2 — Remap table specified, map JSON not applied: closable, not OPEN_GAPS

IO-01 / SC-1 allow "new pack **and/or** MAP-19-03 remap". Phase 11 plan intentionally ships the **table only**; MAP-19-03 apply + live leave-2 count are Phase 12. Integration check confirms:

- Three named chapter files exist on disk
- Live map "From" still matches the table
- `check_capability_map.py` RED (new slugs + ch11–ch13) is the correct Phase 12 start state
- `git diff` on `docs/capability-pack-map.json` is empty

Adjudicated **not a gap**. Editing the map in Phase 11 leftovers would steal Phase 12 and reopen T-11-06 (map).

### Thread 3 — IO boxes still open: verify owns the tick

All seven IO-01..07 lines remain `- [ ]` with Phase 11 (and Phase 10 handoff) parentheticals. Execute must-NOT check boxes; security T-11-07 (tick) CLOSED on that boundary. Unlike Phase 7 MA-01, no IO box was silently ticked while a dual-source half stayed open.

**Verify-time:** close IO boxes that honestly describe achieved state (built packs + chapters-not-a-pack + dated DEFERRED/ACCEPT + remap **spec**). Do **not** claim live map leave-2 until Phase 12 apply. ROADMAP Phase 11 checkbox closes at verify after this gap analysis.

### Thread 4 — Review residuals: ship-able

| Finding | Class | Adjudication |
|---|---|---|
| IMPL MN-01: catalog `dod-vva-rpg.chapters` still 10 after pack grew to 13 | minor / plan-authorized | Reject as gap. 11-02-PLAN explicitly deferred integer bump to Phase 13; `check_release` does not read it; PACK.yaml/disk are 13. |
| CODE IN-01: plan `<automated>` blocks still omit MJ-01/MJ-02 conjuncts | INFO | Reject as gap. Executed content satisfies majors; SUMMARIES re-ran bound greps + new-chapter-only overlap. Residual risk is future re-execute only. |
| CODE IN-02: VALIDATION task map / RESEARCH Open Questions unstamped | INFO | Reject as gap. Advisory at PLAN_REVIEW; decisions followed (thin-register, chapters-not-a-pack, Checklist+2, UCO skip). |
| CODE IN-03: STATE metrics / ROADMAP Plans TBD / IO-03/04 notes still Phase-10-flavored | INFO | Reject as gap. Consume path is packs + 11-02-SUMMARY table + REQUIREMENTS IO-01/02/05/06/07 annotations. Optional close-out hygiene. |
| INT NOTE-1: README live-pack table omits new rows; `dod-vva-rpg` still "10 chapters" | note | Reject as gap. Badge `packs-63` + `check_release` PASS; full surface sync is Phase 13 / REL-19-01. |
| INT NOTE-2: catalog chapter integer lag | note | Same as IMPL MN-01 → Phase 13. |
| INT NOTE-3: ROADMAP `**Plans**: TBD` | note | Reject as gap. 11-01/11-02 PLAN files exist; Phase 12 does not read that line. |
| INT NOTE-4: STATE YAML still `status: planning` / stale progress | note | Reject as gap. Same class as Phase 10 NOTE-1; body Deviations carry Phase 11 bullet. |
| INT NOTE-5: map gate RED | note | Expected Phase 12 start state; do not "fix" map here. |
| SEC N1: bare hostnames (`gps.gov`, `cto.mil`, `de-bok.org`) | note | In-policy (no scheme); Link Policy gate passes. |
| SEC N2–N3: packs.html / pre-existing NOTICE URLs | note | Outside pack/SOURCE-VETTING boundary; T-11-01 holds. |
| SEC N4: forward map apply / ticks / REL-19-02 | forward | Route to Phase 12/13/verify (below); not a Phase 11 open threat. |

### Thread 5 — Phase 10 / 7 analog classes not repeated

Unlike Phase 6/7 defects and Phase 10 contrast cases:
- No silent AAF Tier-1 substitute or AAF pack (Phase 6 MA-01 class avoided)
- No IO box ticked while dual-source half open (Phase 7 MA-01 class avoided)
- No map JSON edit this phase (T-11-06 map CLOSED)
- No version/tag steal (plugin 1.18.0; no `v1.19*`)
- No `sources/` / `full_text.txt` leak; overlap re-run exit 0 on both extracts + ch11–ch13

## Phase 12 / 13 Routing (preconditions — not Phase 11 gaps)

| ID | Obligation | Source of record | Consequence if skipped |
|---|---|---|---|
| P12-MAP-1 | MAP-19-01 regen: include `nasa-std-8719-14` (7 ch) + `is-gps-200n` (6 ch) + `dod-vva-rpg` ch11–ch13 | built packs; integration handoff | Map gate stays RED / wrong clusters |
| P12-MAP-2 | MAP-19-03 apply IO-01 table only: three named files → Decision Analysis & Trade Studies; leave federal-bca ch01–ch03/ch05 in Opportunity; leave dod-vva-rpg ch08 Validation + ch10 Risk | 11-02-SUMMARY remap table; REQUIREMENTS IO-01 | Re-guess chapters; double-build IO-01 |
| P12-NOGO-1 | Do not build Army CBA / AAF / stakeholder / `dodm-5000-102`; do not treat `dod-rio` AAF chapters as guidebook licence | IO-05/06 DEFERRED; IO-07 ACCEPT; Phase 10 NO-GO | Licence / scope regression |
| P12-NOTE | Live Decision Analysis leave-2 count is a **Phase 12** success check after apply — not a Phase 11 residual defect | SC-1 Pattern 4 | False OPEN_GAPS on Phase 11 |
| P13-REG-1 | Bump catalog `dod-vva-rpg.chapters` 10→13; README catalogue rows for new slugs; REL-19-01/02 version/tag surface | IMPL MN-01; INT NOTE-1/2 | Catalog lag only; not map-apply input |

## Residual Notes That Ship (no execute re-entry)

- Catalog `dod-vva-rpg.chapters` integer still 10 (Phase 13 registration).
- Plan files never rewritten for MJ-01/MJ-02 automated conjuncts (IN-01); live gates pass with bound greps + new-chapter overlap.
- Advisory PLAN_REVIEW stamps on VALIDATION / RESEARCH Open Questions still open (IN-02).
- STATE frontmatter progress / ROADMAP `Plans: TBD` / README table rows / IO-03/04 parentheticals still Phase-10-flavored in places (IN-03, INT NOTE-1/3/4) — body annotations and packs are authority.
- Map JSON intentionally stale; `check_capability_map.py` RED is Phase 12 start state (INT NOTE-5).
- Bare hostnames in provenance (SEC N1); generator/site HTTPS outside pack boundary (N2–N3).
- IO-01..07 boxes and ROADMAP Phase 11 checkbox still open for verify (Thread 3).
- Working-tree flow bookkeeping (`master_flow_state.json`, `.edge-coverage.json`) outside execute pack scope.

## Rejected as Non-Gaps

- **"SC-1 fails because Decision Analysis live count is still 2/2"** — rejected: Phase 11 contract is remap **specification**; live leave-2 after apply is Phase 12 / MAP-19-03. User instruction: remap-table-not-applied is NOT OPEN_GAPS if recorded.
- **"IO-05/06 incomplete because Integration/Logistics packs were not built"** — rejected: SC-3 explicit deferred-recorded path; dated DEFERRED present; AAF still unused.
- **"IO-07 incomplete because no stakeholder pack / no SEBoK expansion"** — rejected: SC-4 allows accept; dated ACCEPT; inventing a pack is forbidden.
- **"IO boxes still open = phase incomplete"** — rejected: execute must not tick; verify closes after gap analysis.
- **"Map gate RED / capability-pack-map.json untouched = gap"** — rejected: intentional; Phase 12 owns regen+apply; touching map now is scope theft.
- **"catalog dod-vva-rpg.chapters=10 blocks close"** — rejected: plan-authorized Phase 13 lag; validate_pack/check_release green on disk reality.
- **"Plan automated blocks missing MJ conjuncts block close"** — rejected: INFO only; executed tree independently satisfies MJ-01/MJ-02.
- **"STATE YAML still says planning / ROADMAP Plans TBD"** — rejected: intentional or cosmetic hygiene; consume path is packs + SUMMARY table + REQUIREMENTS.
- **"AAF unused / DoDM not built means SC-2 Validation failed"** — rejected: Validation satisfied via chapters-not-a-pack (IO-02); DoDM remains deferred without a new slug.
- **"check_release must see v1.19.0"** — rejected: thin-register keeps 1.18.0 by design; REL-19-02 is Phase 13.

## Verify-Time Actions (checklist for the closing step)

1. Close IO requirement boxes that match achieved state:
   - IO-01: remap **specified** (not live leave-2) — tick only if verify accepts "spec complete; apply is Phase 12" wording already in the parenthetical.
   - IO-02: chapters-not-a-pack (13 chapters) — tick.
   - IO-03 / IO-04: packs built and validate_pack PASS — tick (optional parenthetical refresh to name built slugs).
   - IO-05 / IO-06: dated DEFERRED — tick as deferred-complete.
   - IO-07: dated ACCEPT — tick as accept-complete.
2. Close ROADMAP Phase 11 checkbox when the above is accepted.
3. Re-run gates: validate_pack ×3; check_release PASS; no forbidden packs; map diff empty; SOURCE-VETTING `http`=0; DEFERRED/ACCEPT greps; IO open→checked transition only via deliberate ticks.
4. Hand §Phase 12 / 13 Routing into Phase 12 planning (MAP-19-01 regen + MAP-19-03 apply table; no AAF/CBA/DoDM/stakeholder builds).
5. Optional hygiene (non-blocking): stamp RESEARCH Open Questions; fold MJ conjuncts into plan archives; ROADMAP Plans links; STATE metrics arithmetic; README catalogue rows deferred to Phase 13 with catalog chapter bump.

**Next commands:** none — no `plan-phase --gaps` / `execute --gaps-only` re-entry is required for Phase 11. Proceed to verify close-out, then Phase 12 planning with the routing table above.

---

_Gap analysis: ZCode (gsd-gap-analyzer) — all four reviews read in full; validate_pack ×3, check_release, forbidden-pack scan, IO boxes, DEFERRED/ACCEPT greps, map JSON diff, and SOURCE-VETTING Link Policy re-verified live on `main`._
