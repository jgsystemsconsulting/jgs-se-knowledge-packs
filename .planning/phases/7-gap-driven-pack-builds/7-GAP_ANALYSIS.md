# Phase 7 Gap Analysis — Gap-Driven Pack Builds

**Analyzed:** 2026-08-14 (post-execute, post-fix `e4699c4`)
**Inputs read:** 7-RESEARCH, 7-01/02/03-PLAN + SUMMARY, 7-PLAN_CHECK (round 2 PASS), 7-PLAN_REVIEW, 7-IMPL_REVIEW, 7-CODE_REVIEW, 7-INTEGRATION_CHECK, 7-SECURITY_AUDIT, ROADMAP Phase 7 (SCs + plan list), REQUIREMENTS GP section (post-`e4699c4`), live repo state.
**Fresh re-verification by this analysis:** `check_release.py` PASS on the post-`e4699c4` tree; `validate_pack.py` PASS on dod-vva-rpg / mil-std-40051 / federal-bca (packs touched by or adjacent to the fix commit); repo-wide `OUSW` grep; `debok_meta_summary.json` empty + gitignored; ROADMAP/STATE bookkeeping state.

**Verdict:** CLOSED

All four post-execute reviews are PASS_WITH_NOTES / SECURED_WITH_NOTES with zero open blockers. The single MAJOR (GP-06 partial delivery untracked at milestone level) was resolved by `e4699c4` before this analysis. Every remaining finding is a ship-able residual with routing; no execute re-entry (`--gaps-only`) is required. Phase 7 can proceed to `phase.complete`.

## Roadmap success-criteria cross-check

| SC | Requirement | Status | Evidence |
|----|-------------|--------|----------|
| SC-1 | Packs conform to PACK-SPEC; validate + scan + overlap all pass | **MET** | IMPL/CODE reviews: validate 7/7, scan + overlap exit 0 (overlap freshly re-run by security auditor incl. 10 vva chapter fulltexts); re-confirmed post-fix by this analysis |
| SC-2 | PACK.yaml provenance complete; no sources/ leaked; SKILL.md When-to-use + Prerequisites | **MET** | Security audit: 15/15 threats CLOSED, range-wide leak check clean, RR-S-13 in all 7; provenance adversarially verified against local build evidence |
| SC-3 | Target clusters actually fattened | **MET AT PHASE 7 SCOPE — deferred to Phase 8 by design** | ROADMAP SC-3 wording: "verified post-map-regeneration in Phase 8". Phase 7's obligation (target packs carry cluster vocabulary + baseline handoff) verified by integration check: 40051 carries cluster-25 vocabulary (4 SKILL.md hits), federal-bca carries cluster-15 content; baseline table (7-03-SUMMARY, cross-checked live against capability-pack-map.json: 570 entries / 32 clusters, cluster 25 = 0/0, cluster 15 = 1/1) is accurate |

GP-01..GP-07: all 7 packs built, validated, registered at exact counts (catalog 61 / cursor 62 / packs 63 / SKILLS "61 (+2 signposts)" / badge packs-61 / NOTICE x7; data-level catalog diff = 7 added, 0 mutated). GP-06 partial (A-94 only) is honestly tracked — see thread 1. GP-08 descoped pre-phase with recorded rationale (no consolidated NASA-HDBK-2203 PDF).

## Thread adjudication

### 1. MA-01 — GP-06 partial delivery (federal-bca A-94 only) → **CLOSED at `e4699c4`**

- The rescope itself was plan-sanctioned, not a deviation: 7-01-PLAN Task 4 step 3 (P7-PRE-2 hard gate) explicitly instructs "If EITHER fails the in-source check: STOP — drop the failing document and rescope". Army CBA fetch genuinely failed (489-byte "Access Denied" stub on disk, verified by code review + security audit).
- What both reviews actually flagged as MAJOR was the missing milestone-level tracking of the unmet Army half. `e4699c4` delivers exactly the requested fix: REQUIREMENTS GP-06 now reads `[x] ... single-source (dual-source as scoped was NOT fully met: Army CBA Guide unobtainable — 403/503, honestly excluded at build per P7-PRE-2...)` and a new **FUT-04** register entry tracks the retry ("federal-bca Army CBA Guide second source... v1.19 candidate if the ASAFM PDF becomes reachable").
- Post-fix integrity: check_release PASS; validate PASS; ROADMAP plan list already said "federal-bca A-94-only (GP-06 rescoped)". Closable.

### 2. MINOR provenance findings → **1 fixed, 1 resolved-as-recorded, 1 routed to Phase 9**

- **MI-01 (code review) — "OUSW(R&E)" typo: FIXED at `e4699c4`** on all 4 shipped attribution surfaces (dod-vva-rpg PACK.yaml x2, LICENSE x2, catalog.json publisher, NOTICE Author line). Residual: `docs/SOURCE-VETTING.md:130` (GP-01 row, living doc) still reads OUSW → routed to Phase 9 one-liner (below). Occurrences in 6-RESEARCH / 7-RESEARCH / 7-03-PLAN / 6-SECURITY_AUDIT are immutable phase records — do not edit.
- **MI-02 (code review) — vva internal chapter dates ~2011 vs "no dated rev": ACCEPT with note, routed to Phase 9.** `source_version: "RPG web edition (no dated rev; retrieved 2026-08-16)"` is true of the container; the gap is consumer-facing currency completeness, not an untruth. Editing a shipped PACK.yaml now for one note line would force pack re-validation for marginal gain; Phase 9 owns the consumer-facing release surface, so the ~2011 chapter-currency caveat goes into the v1.18.0 CHANGELOG wording. Optional PACK.yaml note line rides the v1.19 backlog.
- **MI-03 (code review) / MI-01 (impl review) — 40051 page objects 1168 vs 584: RESOLVED-AS-RECORDED, no action needed.** PACK.yaml notes record both numbers, attribute 1168 to "some counters", and anchor authority on pdftotext/metadata.pages = 584; 7-02-SUMMARY deviation 4 records the same decision ("pdftotext/metadata.json is build authority"). This is the "accepted ambiguity" disposition the code review explicitly listed as acceptable. Selection ratios are internally consistent (151/584; cpp 2939.9) and the floor gate ran on selected stats — no gate bypassed.
- **MI-02 (impl review) — faa Rev F (everyspec) not ROSAP Rev E: ACCEPT with note.** Plan-permitted fallback (Task 1 step 1), fully attributed per P7-PRE-3. Content-currency caveat for consumers → same Phase 9 CHANGELOG caveat line; ROSAP rev E retry → v1.19 backlog.
- **MI-03 (impl) / IN-03 (code) — build dates 2026-08-16 vs reviewer clock 2026-08-14: CONFIRMED CLOCK ARTIFACT.** The recorded dates are internally self-consistent across all 7 PACK.yaml files, catalog `updated`, NOTICE, the three SUMMARYs, STATE last_activity, and git author dates (Aug 16-17) — the review headers' "2026-08-14" stamp is the outlier against all repository evidence. P7-PRE-3 repudiation control hereby gets its one explicit confirmation: 2026-08-16 was the actual build day. No change.

### 3. Security notes → **ACCEPTED (all three recorded, none blocking)**

- **Note 1 — DIST-A metadata evidence class (881F QuickSearch Dist Stmt column; vva DEBoK PD + OSD/OUSD authorship):** honest, recorded in PACK.yaml, self-flagged in plan SUMMARYs, adversarially verified. A defensible T-6-03 disposition and a weaker-but-documented evidence class. Accept; if the licence basis is ever challenged these records ride with the packs. v1.19 backlog: revisit if in-PDF DIST-A editions of 881F/RPG surface.
- **Note 2 — empty `sources/dod-vva-rpg/debok_meta_summary.json` ({} per chapter):** confirmed by this analysis (file exists locally, all values empty, gitignored). Raw OTMM capture failed but the per-chapter evidence chain rests on the executor-written provenance headers, which the security auditor verified individually (10/10 chapters). Local-only either way. Accept.
- **Note 3 — federal-bca "(c)" wording imprecision:** substance verified clean (8 literal "(c)" hits are enumeration markers; zero actual copyright notices). Wording tweak only → v1.19 backlog, folded into any future PACK.yaml touch.

### 4. Integration warnings → **NOTE ONLY (phase.complete bookkeeping)**

- ROADMAP line 77 Phase-7 checkbox unchecked while all three plans are `[x]` — ticked at phase close (Phase 6 precedent line 76).
- STATE.md `current_phase: 6` stale while Phase 7 P01-P03 rows exist — phase.close step updates it.
- capability-pack-map.json lacks schema/version/generator — by design, AE-01..03 are Phase 8 scope; baseline numbers inherited from 7-RESEARCH verified accurate against the live map.

### 5. IN-02 — check_overlap / scan_generated_skill not CI-reproducible → **BACKLOG**

Pre-existing Phase 3 model (scripts live in the gitignored jgs-reference-skill; sources/ excluded by design), not a Phase 7 regression. INFO class. The no-long-verbatim rule currently rests on build-session attestations plus adversarial re-verification. Route to v1.19 backlog: commit a minimal overlap checker under `tooling/` so the rule is mechanically enforceable post-hoc. Not Phase 8 (map/generator scope) and not Phase 9 (release surface scope) — new tooling needs its own validation.

### 6. GP-01..GP-07 delivery — **CONFIRMED**

7/7 packs validated and registered (see SC cross-check). GP-06 partial honestly tracked via FUT-04. Plan-phase blockers (7-PLAN_REVIEW BL-01/BL-02, MA-01 gate sequencing) were remediated pre-execute and confirmed by 7-PLAN_CHECK round 2 PASS (`bea75b7`).

## Residual list (ship-able)

| # | Residual | Class | Owner |
|---|----------|-------|-------|
| R1 | vva chapter PDFs ~2011 internal dates not in PACK.yaml; container "no dated rev" is true but incomplete for currency assessment | Minor, provenance completeness | Phase 9 (CHANGELOG caveat); optional PACK.yaml note v1.19 |
| R2 | faa-std-025 documents Rev F (2007) where ROSAP canonical is Rev E (2002) | Minor, content currency | Phase 9 (CHANGELOG caveat); ROSAP retry v1.19 |
| R3 | `docs/SOURCE-VETTING.md:130` GP-01 row still reads OUSW(R&E) | Minor, doc consistency | Phase 9 one-liner |
| R4 | DIST-A evidence for 881F/vva is metadata-class, not in-PDF | Accepted security note | Rides with packs; v1.19 revisit |
| R5 | federal-bca "(c)" wording imprecise (substance clean) | Cosmetic | v1.19 |
| R6 | IN-01 topic-index nits: 881F/dafman index ordering; 40051 circular "Topic Index" routing; federal-bca "Opportunity/Benefit Analysis" label matches no chapter term | Cosmetic, INFO | v1.19 polish (touches 4 shipped SKILL.md → revalidate) |
| R7 | IN-02 overlap/scan gates not CI-reproducible from committed repo | Pre-existing model debt | v1.19 backlog (minimal committed checker) |
| R8 | ROADMAP Phase-7 checkbox + STATE current_phase stale | Bookkeeping | phase.complete (automatic) |
| R9 | Army CBA Guide second source unobtainable | Tracked gap | FUT-04 (v1.19 candidate) |

## Rejected as non-gaps

- **GP-06 "incomplete requirement" as a Phase 7 blocker** — the rescope followed the plan's own hard-gate instruction; REQUIREMENTS now records the honest single-source state with FUT-04 tracking the residual. Within v1.18 scope this is closed.
- **40051 1168-vs-584 as an open provenance question** — both counters recorded, authority anchored (metadata.pages=584), selection math consistent; accepted-ambiguity disposition is the code review's own sanctioned option.
- **catalog.json ~1305-line textual churn in `e00ac7d`** — re-serialization only; data-level diff = 7 entries added, 0 modified, 0 removed.
- **Build-date "future" stamp** — clock artifact of the review context, disproven by git author dates, file mtimes, and cross-surface consistency.
- **Map lacking generator/schema** — explicitly Phase 8 scope (AE-01..03); Phase 7 handoff (baseline + vocabulary) verified.

## Routing

**Phase 8 (proceed, no re-entry):** regenerate capability-pack-map including the 7 new packs; assert cluster 25 non-empty and clusters 3/5/15 above thresholds (SC-2 / AE-02) against the inherited baseline table. Map currently covers only the 54 pre-Phase-7 packs — expected.

**Phase 9 (fold into release surface):**
1. CHANGELOG v1.18.0 caveat line(s): dod-vva-rpg chapter PDFs carry internal dates circa 2011 (web-edition container undated); faa-std-025 built from Rev F mirror (ROSAP canonical is Rev E); optionally the 40051 counter note.
2. One-line OUSD(R&E) correction in `docs/SOURCE-VETTING.md:130`.
3. Usual version bumps (plugin.json / CHANGELOG / RELEASE-INFO) already owned by Phase 9.

**v1.19 backlog:** FUT-04 Army CBA retry; IN-02 minimal committed overlap checker; IN-01 index polish; optional PACK.yaml note additions (R1, R5); ROSAP rev E retry; 881F/vva DIST-A in-PDF edition revisit.

## Next commands

Phase 7 requires no execute re-entry. Proceed:

```
phase.complete (ticks ROADMAP line 77, advances STATE) → Phase 8 plan-phase
```
