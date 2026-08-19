# Phase 12: Gap Analysis — Map regen + hygiene + gate wiring

**Date:** 2026-08-17
**Inputs:** 12-IMPL_REVIEW, 12-CODE_REVIEW, 12-INTEGRATION_CHECK, 12-SECURITY_AUDIT (all four present, none skipped) + ROADMAP Phase 12 success criteria SC-1..4 + REQUIREMENTS MAP-19-01..05 + HYG-01..04 + 12-01/12-02 SUMMARY + live gate re-verify + analog 11-GAP_ANALYSIS.md
**Method:** Adjudication of all post-execute findings against ROADMAP Phase 12 success criteria and phase goal ("Map reflects new packs; competency-primary floor asserted; hygiene + consumer-contract note"), with independent live re-verification of gates on `main` at HEAD after review artifacts (`55429cd` code_review / prior execute through `828e237`).

**Verdict:** CLOSED

## Review Inventory

| Review | Verdict | Blocker | Major | Minor | Info/Warn/Notes | Post-review state |
|---|---|---|---|---|---|---|
| 12-IMPL_REVIEW | PASS | 0 | 0 | 0 | notes only (version 1.18.0; boxes open; HYG-03 PR open OK) | Map MOVE + floors + wire + hygiene match both plans |
| 12-CODE_REVIEW | PASS_WITH_NOTES | 0 | 0 | 0 | 3 INFO (IN-01..03) | Plan hygiene leftovers; executed tree faithful |
| 12-INTEGRATION_CHECK | PASS_WITH_NOTES | 0 | 0 | — | 7 NOTES | Phase 13 consumption chain COMPLETE; stale map now fails ship gate |
| 12-SECURITY_AUDIT | SECURED | 0 | 0 | 0 | 4 notes (N1–N4) | 10/10 declared threats CLOSED; threats_open = 0 |

No review returned NEEDS_WORK. No blocker or major finding remains open. Phase 13 leftovers (catalog chapter integer, README new-slug rows, version trio / tag) are intentional fences, not Phase 12 defects. MAP-19 / HYG boxes remain open for verify (execute must not silent-tick).

## Live Gate Re-Verification (gap-analysis time)

| Gate | Result | Notes |
|---|---|---|
| `python tooling/check_capability_map.py` | **PASS** | exit 0; `PASS: capability map OK`; TOTAL **644** |
| `python tooling/check_release.py` | **PASS** | exit 0; reprints map cluster-count block; `RELEASE CHECK: PASS` |
| Envelope | schema **2** / `map_version` **1.18.0** / `generated_on` **2026-08-17** / 32 clusters | holds |
| Chapter-set / uniqueness | reviews: `on_disk_only=0`, `map_only=0` (536/536); live pairs **644 unique / 644** | holds |
| MAP-19-03 MOVE / DA | DA **5 entries / 4 packs** exact want-set (`nasa-ceh` ch06, `nasa-se-handbook` ch34-6-8, `federal-bca` ch04+ch06, `dod-vva-rpg` ch06) | MOVE not copy |
| Listed-primary conjunct | DA 5/4; Validation 7/4; Integration 4/4; Interfaces 9/4; Ops 13/5 | none `<4 AND 1 pack` |
| Wire | `check_release.py` in-process `import check_capability_map` + `main()` + `fail()`; no subprocess on map path | holds |
| CONTRACT MAP-19-05 | §6 contains 628 / 644 / 502 / Cybersecurity / Digital Engineering / unbound | holds |
| HYG-01 | CHANGELOG first bytes `3c212d2d…`; BOM **False**; `.gitattributes` exactly `*.md text eol=lf` | holds |
| HYG-03 vendor ban | `tooling/vet_source.py` **absent** | holds |
| Link Policy | `grep -c http docs/SOURCE-VETTING.md` → **0** | holds |
| Version trio / tag | plugin / cursor-plugin / CHANGELOG top / RELEASE-INFO / `map_version` all **1.18.0**; no `v1.19*` tag | holds |
| MAP-19 + HYG boxes | **9 open / 0 checked** | all `- [ ]` |
| Catalog leftover | `dod-vva-rpg.chapters` still **10** | Phase 13 |
| Branch | `main` | HEAD after reviews `55429cd` |

## Success-Criteria Cross-Check (ROADMAP Phase 12)

| Criterion | Requirement | Status | Evidence (reproduced at gap-analysis time) |
|---|---|---|---|
| SC-1: `check_capability_map.py` PASS; MAP-19-02 floor held (no listed primary still at <4 entries AND 1 pack) | MAP-19-01, MAP-19-02, MAP-19-03 | **VERIFIED** | Live map gate exit 0 / TOTAL 644; DA MOVE to 5/4; five listed primaries all clear the conjunct; Integration held 4/4 (no AAF raid). |
| SC-2: `check_release.py` invokes the map gate | MAP-19-04 | **VERIFIED** | In-process `main()` after cursor-manifest; release run prints cluster block then PASS; floors committed before wire. |
| SC-3: CONTRACT.md notes live snapshot (not 502) and unbound Cyber/DE clusters | MAP-19-05 | **VERIFIED** | §6: live 628+ / post-regen 644; 502 residue; Cyber 69/10 + DE 25/4 unbound. |
| SC-4: CHANGELOG BOM gone; `.gitattributes` pin present; topic-index nits fixed; vet_source EXCLUDED sync done or recorded as external-repo PR | HYG-01..04 | **VERIFIED** | BOM gone + LF pin; four SKILL nits landed (reviews + validate_pack PASS ×4); HYG-04 `(c)` enumeration wording; HYG-03 Path A sibling PR #2 recorded (merge not required). |
| Phase goal: map reflects new packs; primary floor asserted; hygiene + consumer-contract note | MAP-19 + HYG | **VERIFIED** | 16 Phase-11 chapters classified; chapter-set empty; floors + CONTRACT + wire + hygiene complete; version unbumped; boxes still open for verify. |

## Thread Adjudication

### Thread 1 — Map regen + MOVE + floors (MAP-19-01..03): closable

Phase 12's job was to apply the Phase 11 remap table, classify the 16 new/leftover chapters, and assert listed-primary floors without inventing packs or raiding Integration.

Live tree shows:
1. DA exactly the five locked rows / 4 packs; old Opportunity/Assurance tuples vacated
2. Stay-put held (federal-bca ch01–ch03/ch05 + support in Opportunity; RPG ch08 Validation; ch10 Risk)
3. 644 entries / 63 packs; uniqueness 644/644; gate PASS
4. THRESHOLDS name-keyed ≥4 for DA/Validation/Integration/Interfaces/Ops; Training/Traceability/Opportunity floors not weakened
5. No generator; no AAF/CBA/DoDM/stakeholder packs; Cyber/DE unbound

Adjudicated **not gaps**. Re-opening execute to re-classify or bump floors would steal Phase 13 / regress T-12-03.

### Thread 2 — Gate wire + CONTRACT (MAP-19-04/05): closable

Wire is in-process after GREEN (THRESHOLDS commit ancestor of import). CONTRACT §4 describes the wire; §6 carries the se-agents consumer paragraph. Both gates PASS together.

Adjudicated **not gaps**. Unwiring or treating the map as optional docs would break the Phase 13 ship invariant.

### Thread 3 — Hygiene (HYG-01..04): closable

HYG-01/02/04 landed in-tree. HYG-03 Path A is authorized: sibling PR https://github.com/jgsystemsconsulting/jgs-reference-skill/pull/2 (OPEN) with keys recorded; `tooling/vet_source.py` not vendored. ROADMAP SC-4 / 12-02-PLAN allow close without sibling merge.

Adjudicated **not gaps**. Merging the sibling PR is an external-repo concern, not a Phase 12 execute re-entry.

### Thread 4 — MAP/HYG boxes still open: verify owns the tick

All nine MAP-19-01..05 and HYG-01..04 lines remain `- [ ]`. Execute must-NOT check boxes; security T-12-10 CLOSED on that boundary. Same class as Phase 11 Thread 3.

**Verify-time:** close MAP-19 and HYG boxes that honestly describe achieved state (live map PASS + MOVE + floors + wire + CONTRACT paragraph + hygiene + Path A PR record). Do **not** claim catalog/README/version 1.19.0 — those are Phase 13. ROADMAP Phase 12 checkbox closes at verify after this gap analysis.

### Thread 5 — Review residuals: ship-able

| Finding | Class | Adjudication |
|---|---|---|
| CODE IN-01: 12-01 T1 `<automated>` still omits MJ-01 chapter-set conjunct | INFO | Reject as gap. Live chapter-set empty; SUMMARY re-ran set-diff + gate. Residual risk is future re-execute only. |
| CODE IN-02: PLAN_REVIEW advisory stamps (VALIDATION task map / RESEARCH Open Questions) still open | INFO | Reject as gap. Advisory at PLAN_REVIEW; decisions followed (Integration floor-held; map_version 1.18.0; Path A; ch11 T&E). |
| CODE IN-03: plan greps still carry MN-01 / MN-04 dead weight | INFO | Reject as gap. Live CONTRACT §5 + Topic Index row correct; optional plan-archive polish only. |
| INT NOTE-1: catalog `dod-vva-rpg.chapters` still 10 | note | Reject as gap. Phase 13 / REL-19-01; plan fence; user instruction: not OPEN_GAPS. |
| INT NOTE-2: README live-pack table omits new-slug rows; RPG still "10 chapters" | note | Reject as gap. Badge/gates green; full surface sync is Phase 13 / REL-19-01. |
| INT NOTE-3: version trio + tag still 1.18.0 | note | Reject as gap. Phase 13 / REL-19-02 by design; T-12-05/T-12-10 hold. |
| INT NOTE-4: ROADMAP Phase 12 + MAP/HYG boxes open | note | Reject as gap. Verify owns ticks (Thread 4). |
| INT NOTE-5: REQUIREMENTS IO-01 still says "Live count leave-2 is Phase 12" | note | Reject as gap. Annotation lag only; live DA is 5/4; remap table + JSON agree. Optional verify parenthetical refresh. |
| INT NOTE-6: HYG-03 sibling PR open/unmerged | note | Reject as gap. SC-4 Path A complete without merge. |
| INT NOTE-7: CI does not exec repo Python / no map step in validate.yml | note | Reject as gap. Intentional local/trusted split; T-12-07 CLOSED; do not add CI repo-Python in Phase 13 leftovers. |
| SEC N1–N4 | note / forward | v1.19 changelog bullet vs trio; historical SUMMARY §4 sentence; PR URL in planning only; Phase 13 forward boundary — not open threats. |

### Thread 6 — Phase 11 analog classes not repeated

Unlike prior contrast cases:
- No copy-not-move remap (uniqueness + old-cluster absence prove MOVE)
- No wire-on-RED map (floors precede import)
- No silent MAP/HYG ticks
- No version/tag steal (1.18.0 throughout; no `v1.19*`)
- No vendored `vet_source.py` / sibling secrets
- No generator; no forbidden packs; SOURCE-VETTING `http`=0
- Catalog/README/version leftovers left for Phase 13 (not stolen)

## Phase 13 Routing (preconditions — not Phase 12 gaps)

| ID | Obligation | Source of record | Consequence if skipped |
|---|---|---|---|
| P13-REG-1 | Bump catalog `dod-vva-rpg.chapters` 10→13; README live-pack rows for `nasa-std-8719-14` + `is-gps-200n`; RPG "10 chapters" → 13 | INT NOTE-1/2; REL-19-01 | Catalog/docs lag only; map/gates already green |
| P13-REL-1 | Version trio 1.19.0 + `## [1.19.0]` + `v1.19.0` tag + GitHub Release; CHANGELOG lists IO-unlocks by competency | INT NOTE-3; REL-19-02; T-12-05/10 fence | Release surface incomplete |
| P13-GATE-1 | Both gates PASS at updated catalog/directory basis; rely on wired map import (do not unwire) | MAP-19-04 live; SC-2 | Stale map or broken ship gate |
| P13-NOGO-1 | Do not build AAF/CBA/DoDM/stakeholder packs; do not bind Cyber/DE here; do not vendor `vet_source.py`; do not add CI repo-Python map step | IO-05/06/07; MAP-19-05; T-12-03/07/08 | Scope / licence / CI elevation regression |
| P13-NOTE | Live map 644 / DA 5/4 / floors / CONTRACT §6 are **frozen inputs** — do not re-classify the 16 chapters or reverse the MOVE | 12-01-SUMMARY; integration handoff | Double-build / wrong clusters |

## Residual Notes That Ship (no execute re-entry)

- Catalog `dod-vva-rpg.chapters` integer still 10; README new-slug rows absent (Phase 13 registration).
- Version trio + `map_version` still 1.18.0; no `## [1.19.0]`; no `v1.19*` tag (Phase 13 release).
- Plan files never rewritten for MJ-01 automated chapter-set conjunct or MN-01/MN-04 greps (IN-01/IN-03); live gates and SUMMARY are authority.
- Advisory PLAN_REVIEW stamps on VALIDATION / RESEARCH Open Questions still open (IN-02).
- REQUIREMENTS IO-01 parenthetical still mentions "Live count leave-2 is Phase 12" while live DA is 5/4 (INT NOTE-5) — optional verify annotation refresh.
- HYG-03 sibling PR #2 remains OPEN externally; merge not required for Phase 12 close.
- MAP-19-01..05 and HYG-01..04 boxes and ROADMAP Phase 12 checkbox still open for verify (Thread 4).
- CI still does not exec repo Python (intentional).
- Working-tree flow bookkeeping (`master_flow_state.json`, etc.) outside execute map/hygiene scope.

## Rejected as Non-Gaps

- **"SC-1 fails until catalog/README match disk chapter counts"** — rejected: map gate + chapter-set are the SC-1 authority; catalog integer and README rows are REL-19-01 / Phase 13. User instruction: Phase 13 leftovers are NOT OPEN_GAPS.
- **"SC-2 incomplete because CI validate.yml does not run the map gate"** — rejected: MAP-19-04 and plans require local/trusted `check_release` in-process wire; CI repo-Python is explicitly forbidden (T-12-07).
- **"SC-4 incomplete because sibling vet_source PR is unmerged"** — rejected: SC-4 allows "done or recorded as external-repo PR"; Path A PR #2 recorded; vendor ban holds.
- **"MAP/HYG boxes still open = phase incomplete"** — rejected: execute must not tick; verify closes after gap analysis.
- **"map_version / plugin still 1.18.0 blocks close"** — rejected: phase required version-unbumped; REL-19-02 is Phase 13; md v1.19 changelog bullet is human history only.
- **"Plan automated blocks missing MJ-01 conjunct block close"** — rejected: INFO only; executed tree independently satisfies MJ-01 (live set-diff empty + gate PASS).
- **"IO-01 REQUIREMENTS text still says leave-2"** — rejected: annotation lag; live JSON + remap table are authority; optional verify wording refresh.
- **"HYG-03 incomplete without vendoring vet_source.py"** — rejected: vendoring is a threat (T-12-08); Path A is the authorized path.
- **"Integration still 4/4 means MAP-19-02 failed"** — rejected: floor is ≥4 held without raid; AAF remains deferred; conjunct `floor_fail=False`.
- **"Must re-open execute to stamp RESEARCH/VALIDATION advisories"** — rejected: advisory INFO; decisions already followed in shipped files.

## Verify-Time Actions (checklist for the closing step)

1. Close MAP-19 / HYG requirement boxes that match achieved state:
   - MAP-19-01: regen 644 / chapter-set empty / gate PASS — tick.
   - MAP-19-02: listed-primary floors ≥4; conjunct held; Integration not raided — tick.
   - MAP-19-03: three-row MOVE applied; DA 5/4 live — tick (and optionally refresh IO-01 parenthetical from "leave-2 is Phase 12" to live 5/4).
   - MAP-19-04: `check_release` in-process wire — tick.
   - MAP-19-05: CONTRACT §6 628+/644 / 502 residue / Cyber+DE unbound — tick.
   - HYG-01..04: BOM/LF pin + four nits + `(c)` wording + Path A PR record — tick.
2. Close ROADMAP Phase 12 checkbox when the above is accepted.
3. Re-run gates: `check_capability_map.py` PASS; `check_release.py` PASS; SOURCE-VETTING `http`=0; no BOM; `.gitattributes` pin; version still 1.18.0; no `v1.19*` tag; MAP/HYG open→checked only via deliberate ticks; no forbidden packs; no `tooling/vet_source.py`.
4. Hand §Phase 13 Routing into Phase 13 planning (catalog/README registration + version/tag release; consume frozen map 644 / DA 5/4 / wired gate; no AAF/Cyber-bind/CI-Python/vendor work).
5. Optional hygiene (non-blocking): stamp RESEARCH Open Questions; fold chapter-set assert into plan archives; refresh IO-01 live-count parenthetical.

**Next commands:** none — no `plan-phase --gaps` / `execute --gaps-only` re-entry is required for Phase 12. Proceed to verify close-out, then Phase 13 planning with the routing table above.

---

_Gap analysis: ZCode (gsd-gap-analyzer) — all four reviews read in full; check_capability_map, check_release, DA membership, CONTRACT markers, wire import, BOM/.gitattributes, version trio/tag, SOURCE-VETTING Link Policy, MAP/HYG boxes, catalog leftover, and vendor ban re-verified live on `main`._
