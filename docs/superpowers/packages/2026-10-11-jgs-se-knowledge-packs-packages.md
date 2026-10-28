---
date: 2026-10-11
project: jgs-se-knowledge-packs
mode: full
rounds: 1
input_digest: bbb44c491acbcb457423f79895862f2124e493a80bbbfbbb446c73164ae7b55a
open_objections: []
---

# Work packages - jgs-se-knowledge-packs (2026-10-11, full re-run)

Context: the source-freshness-watch superpowers-process run finished 2026-10-11 (6 commits on unmerged branch source-freshness-watch, EXECUTED, IVL advisory-only): source-watchlist.json seeded for all 64 live packs, check_source_watch.py with validate/record modes, check-18 docstring in check_release.py with the call deliberately not wired (D-06, staged in the plan's post-pipeline notes), SOURCE-FRESHNESS.md, version 1.22.1. That run was picked outside the packages document, so no package status transitions were owed from it. This cut converges round 1, zero critical defects: one wave (value 5, risk 3, cohesion 5), merge reused the five prior growth ids and added three new packages, triage passed all eight. The working tree's only red is the local release gate failing on five untracked duplicate nasa-se-handbook chapters.

## Carry-forward status

| id | name | status |
|----|------|--------|
| P1-P7, P9-P22, P27 | prior cuts | done |
| P8 | phase21-planning-ledger-close | in-flight (frozen) |

## P32 - growth-registration-watchlist-surface

- **id**: P32; **name**: growth-registration-watchlist-surface; **size**: S; **status**: done (2026-10-12; commit ca4507d, EXECUTED, IVL Track 1 clean, capture 2 rows); **corroboration**: 1 (cohesion); **deps**: none; **promoted_ids**: []
- **problem**: every live content pack now participates in two inventories that must stay aligned: catalog.json live set and docs/source-watchlist.json (check_source_watch.py:151-155 fails when a live catalog slug lacks a watchlist row, and the reverse). candidate-packs.md:96-98 "Mechanics of adding a pack" still lists only pack folder, SOURCE-VETTING, SKILLS.md, catalog.json, /se routing, and capability map; the watchlist is missing. The proposed growth packages (P23/P25/P26/P28/P29) inherit that incomplete checklist.
- **evidence**: docs/candidate-packs.md:96-98 ("Adding any pack from this list needs: the pack folder per PACK-SPEC.md, ... and the capability map"); tooling/check_source_watch.py:151-155 (coverage failures both directions); docs/SOURCE-FRESHNESS.md:15-17 (one entry per live catalog pack).
- **in_scope**: extend candidate-packs.md mechanics (and any PACK-SPEC/CONTRIBUTING registration note listing surfaces) to require a docs/source-watchlist.json row for each new live content pack; state the signpost/orchestrator exclusion consistent with EXCLUDED_KINDS; optionally add a one-line registration reminder to growth package scopes.
- **out_scope**: building any growth pack content; calibration run or check-18 wire (P31); coverage algorithm changes; merging growth builds into one package.
- **why_now**: the watchlist coverage check is live in tooling while the published add-a-pack checklist still describes the pre-watch registration set; one surface fix prevents five separate growth builds from re-learning the miss, and P25 depends on it.
- **first_prompt**: `/superpowers-process full add the source-watchlist row to the add-a-pack registration checklist in candidate-packs and PACK-SPEC`

## P30 - nasa-shortname-chapter-dupes

- **id**: P30; **name**: nasa-shortname-chapter-dupes; **size**: S; **status**: done (2026-10-12; five untracked dupes deleted, no commit needed; local gate fully green, both dupe-caused probes green; EXECUTED + IVL Track 1 clean); **corroboration**: 2 (risk, cohesion); **deps**: none; **promoted_ids**: []
- **problem**: five untracked short-basename chapter files under packs/nasa-se-handbook/chapters/ duplicate tracked long-basename siblings for the same section numbers (ch05 HSI, ch11-ch14 phases A-D). check_pack_quality.py:69-77 globs chapters/ on disk and emits [orphan-chapter] for any basename not named in SKILL.md, so the local release gate is red solely from this debris (IVL baseline, 2026-10-11). PACK.yaml claims chapters: 34 and SKILL.md links only the long names; an accidental git add would ship duplicate chapter surfaces. The 2026-10-07 pack-quality plan renamed ch05 short to long, so these are pre-rename leftovers.
- **evidence**: git status (5 untracked chapters/ files); ch05 short vs long basename with identical first line ("# Chapter 5: 2.6 Human Systems Integration (HSI) in the SE Process"); packs/nasa-se-handbook/PACK.yaml:13 ("chapters: 34"); tooling/check_pack_quality.py:69-77 (orphan scan); docs/superpowers/plans/2026-10-11-source-freshness-watch-ivl-triage-log.md:9 (failure set = the 5 untracked chapters); docs/superpowers/plans/2026-10-07-pack-quality-fixes.md:216 (ch05 rename).
- **in_scope**: delete the five untracked short-basename chapter files; confirm no metadata references them and PACK.yaml chapters: 34 / SKILL Topic Index stay aligned with tracked disk; re-run pack-quality and check_release until the five-orphan failure set is gone.
- **out_scope**: renaming or rewriting tracked long-name chapters; SKILL.md Topic Index changes; other pack prose; source-watch work; history rewrite; growth packs.
- **why_now**: sole current red set of the local pre-tag gate; clears first as a pure pack-local cleanup with no shared files with P31 or growth work, and P31's gate-PASS verification needs a green baseline.
- **first_prompt**: `/superpowers-process full delete the five untracked short-basename nasa-se-handbook chapter dupes and clear the local gate red set`

## P23 - fda-med-device-pack

- **id**: P23; **name**: fda-med-device-pack; **size**: L; **status**: done (2026-10-12; ported + adapted from the jgs-med-device-knowledge-packs prototype, D-04 pin 2026-10-12, registered on every gate surface; 65 packs / 70 skills; RELEASE CHECK: PASS; EXECUTED + IVL Track 1 clean); **corroboration**: 1 (value); **deps**: none; **promoted_ids**: []
- **problem**: candidate-packs.md:16 ranks fda-med-device #1: tier-1 US public-domain device guidance (QMSR/21 CFR 820, device software, premarket, cybersecurity), zero open competitor, large audience; no packs/fda-med-device exists. packs/functional-safety-signpost/SKILL.md:49-50 already admits FDA software guidance is absent from the catalogue.
- **evidence**: docs/candidate-packs.md:16, 67 (build-order row and tier-1 source list); packs/functional-safety-signpost/SKILL.md:49-50 ("FDA software guidance is not in this catalogue").
- **in_scope**: vet and build packs/fda-med-device per PACK-SPEC from tier-1 FDA guidance; register in SKILLS.md, catalog.json, /se routing, capability map, and (per P32's checklist) a source-watchlist row; all gates green including check 16.
- **out_scope**: med-device-eu (b-28); landing count copy; P8; distribution submissions; tooling pets.
- **why_now**: standing #1 on the committed build-order table; unlocks a whole regulated sector no existing pack covers and closes the free-path gap a shipped signpost already names.
- **first_prompt**: `/superpowers-process full build fda-med-device pack from tier-1 FDA guidance and register it`

## P25 - faa-8110-49-pack

- **id**: P25; **name**: faa-8110-49-pack; **size**: L; **status**: done (2026-10-12; ported + adapted from the jgs-aviation-knowledge-packs prototype, D-04 four-document pin verified 2026-10-12, registered on every gate surface; 66 packs / 71 skills / notes 675; RELEASE CHECK: PASS; EXECUTED + IVL Track 1 clean); **corroboration**: 2 (value, cohesion); **deps**: [P32]; **promoted_ids**: [b-26]
- **problem**: seven faa-* packs ship but the FAA family lacks FAA Order 8110.49 (software certification guidance for DO-178C usage; tier 1, public domain; candidate-packs.md:70). The avionics free-path story needs this content half; without it the catalogue cannot answer DO-178C-shaped questions from an open primary and P26 has no free path to land on.
- **evidence**: docs/candidate-packs.md:18, 70, 82; docs/superpowers/backlog.md b-26 (promoted into P25).
- **in_scope**: build packs/faa-8110-49 per PACK-SPEC; register across SKILLS.md, catalog.json, /se routing, capability map, and a source-watchlist row (same registration flow); gates green including check 16.
- **out_scope**: avionics-signpost body (P26); easa-rules (b-29); reproducing DO-178C/DO-254/ARP paywalled text; other growth sectors; source-watch calibration of the full 64-pack seed (P31).
- **why_now**: content half of the ranked avionics story; must exist before the signpost's free-path row is honest; extends the shipped faa family with no new tooling. Depends on P32 so the registration flow includes the watchlist row from the start.
- **first_prompt**: `/superpowers-process full build faa-8110-49 pack from FAA Order 8110.49 and register it`

## P28 - uk-defence-jsp-pack

- **id**: P28; **name**: uk-defence-jsp-pack; **size**: L; **status**: done (2026-10-12; ported + adapted from the jgs-uk-defence-knowledge-packs prototype, JSP 815 V1.3 pin verified 2026-10-12, first OGL v3.0 tier-2 pack with Licences row and UK chip; 67 packs / 72 skills / notes 685; RELEASE CHECK: PASS; EXECUTED + IVL Track 1 clean); **corroboration**: 1 (value); **deps**: none; **promoted_ids**: []
- **problem**: defence practice in the catalogue is US-federal only. candidate-packs.md:19 ranks a UK defence JSP family next (OGL v3, no open competitor, matches consultancy identity) and directs starting with one JSP pack on gov.uk; no packs/uk-defence-* exists, so geography expansion and the OGL tier-2 path stay unrealized.
- **evidence**: docs/candidate-packs.md:19, 46, 69 (build-order row, licence table, tier-2/3 vet-per-doc guidance).
- **in_scope**: one packs/uk-defence-jsp-* from a single OGL JSP; tier-2 SOURCE-VETTING record; in-pack OGL licence text and attribution; surface registration including a source-watchlist row; gates green. Family expansion later.
- **out_scope**: any DEF-STAN (including 00-051) until in-document terms are recorded; full JSP library; med-device-eu.
- **why_now**: next full-pack row after FDA/avionics on the published order; first non-US defence geography and proves the OGL packaging path for later EU/UK rows.
- **first_prompt**: `/superpowers-process full build first uk-defence JSP pack under OGL with per-document vetting`

## P29 - nrc-nuclear-pack

- **id**: P29; **name**: nrc-nuclear-pack; **size**: L; **status**: done (2026-10-12; ported + adapted from the jgs-nuclear-knowledge-packs prototype, seven-document NRC pin with ML numbers verified 2026-10-12, NRC Agency row + chip; 68 packs / 73 skills / notes 693; RELEASE CHECK: PASS; EXECUTED + IVL Track 1 clean); **corroboration**: 1 (value); **deps**: none; **promoted_ids**: []
- **problem**: nuclear/energy scored FULL on public-domain NRC guides (candidate-packs.md:72: NUREG-0800 chapters, RG 1.168 siblings) but no nrc-* pack or /se NRC agency row exists, while sibling safety families (nasa-system-safety, DOE) already ship.
- **evidence**: docs/candidate-packs.md:22, 47, 72 (build-order row, licence table, tier-1 source list).
- **in_scope**: one packs/nrc-nuclear tier-1 pack scoped to digital-systems/software-assurance guides; SOURCE-VETTING tier-1 note; catalog/SKILLS//se NRC agency row, capability map, source-watchlist row; gates green.
- **out_scope**: ONR/HSE UK nuclear; whole NUREG library; easa-rules (b-29).
- **why_now**: clean tier-1 growth parallel to FDA/FAA with sibling safety packs already in-tree; extends regulated safety coverage into nuclear without tooling work.
- **first_prompt**: `/superpowers-process full build nrc-nuclear pack from NRC guides and NUREGs and register it`

## P26 - avionics-signpost-pack

- **id**: P26; **name**: avionics-signpost-pack; **size**: S; **status**: done (2026-10-12; ported + adapted from the jgs-aviation-knowledge-packs 2-file prototype, easa-rules claims stripped to named-text-only, signpost surfaces moved 4->5 signposts with packs unchanged at 68; RELEASE CHECK: PASS; EXECUTED + IVL Track 1 clean); **corroboration**: 2 (value, cohesion); **deps**: [P25]; **promoted_ids**: [b-27]
- **problem**: DO-178C/DO-254/ARP4754A/ARP4761 are paywalled; candidate-packs.md:82 defines avionics-signpost mapping them to free paths (faa-8110-49, existing faa-*, EASA AMC). automotive-signpost and functional-safety-signpost already ship at that grain (SKILL.md + PACK.yaml only, kind: signpost, zero reproduced text); packs/avionics-signpost is missing. Kept split from the full pack after the P24 oversized kill.
- **evidence**: docs/candidate-packs.md:82, 63; docs/superpowers/backlog.md b-27 (promoted into P26).
- **in_scope**: packs/avionics-signpost (SKILL.md + PACK.yaml, kind: signpost, zero reproduced normative text); open-path rows to live faa-* and faa-8110-49; signpost inventory surfaces so check 13's M stays true; gates green.
- **out_scope**: faa-8110-49 content (P25); easa-rules; merging with other signposts; source-watchlist row (signposts are excluded kinds).
- **why_now**: cheapest sector close once the FAA free-path pack exists; same one-day signpost grain already proven twice; completes the #3 build-order row.
- **first_prompt**: `/superpowers-process full build avionics-signpost pack mapping DO-178C family to free paths`

## P31 - source-watch-calibrate-and-wire

- **id**: P31; **name**: source-watch-calibrate-and-wire; **size**: L; **status**: done (2026-10-13: 6 unknowns maintainer-resolved via record mode d53fa35 -- 5 match + 1 stated drift mrl-deskbook V2025; check 18 wired 9b415b8; all 68 rows last_checked; standalone watch PASS; ten-command gate sweep green; IVL clean Track 1 Round 1; monthly cron created; report .zcode/source-watch/2026-10-12.md incl. 2026-10-13 maintainer-resolution addendum); **corroboration**: 3 (risk x2, cohesion); **deps**: [P30]; **promoted_ids**: [source-freshness-watch-2]
- **problem**: check_release.py documents check 18 [source-watch] (:60-63) and SOURCE-FRESHNESS.md:51-54 states empty last_checked will fail the gate once wired, but main() never calls check_source_watch (D-06 deferral; staged block in the plan's post-pipeline notes). All 64 watchlist last_checked values are empty and the first calibration run has not happened, so a pre-tag PASS can ship over a never-checked catalogue while the documented freshness gate is hollow. Additionally check_source_watch.py:142-146 treats catalog status null/empty-string as live while check_release.py:586-588 and the spec coverage rule (:70) accept live-or-absent only (backlog source-freshness-watch-2; fail-closed direction unexercised; test_source_watch builds only status "live").
- **evidence**: tooling/check_release.py:60-63, 586-588; tooling/check_source_watch.py:142-146, 151-155; docs/SOURCE-FRESHNESS.md:51-54; docs/source-watchlist.json (64 empty last_checked); docs/superpowers/plans/2026-10-11-source-freshness-watch.md:23, 1050-1066 (calibration then wiring); docs/superpowers/specs/2026-10-11-source-freshness-watch.md:70; tooling/test_source_watch.py:45.
- **in_scope**: align the live-status predicate in check_source_watch with catalog-live-set and the spec (live or absent only; empty string not live) with probe cases for both directions; first calibration run per the post-pipeline notes (web search + --record for all 64 live packs; resolve unknowns by hand); insert the staged check-18 call block into check_release.main after MAP-21-05; confirm check_source_watch validate green, then check_release PASS with a non-empty last_checked set; promote/close source-freshness-watch-2; optionally create the monthly cron only after calibration passes.
- **out_scope**: mirroring check 18 into CI validate.yml; editing pack content or PACK.yaml source_version on drift; rebuilding drifted packs; merging the source-freshness-watch branch (human merge decision); source-freshness-watch-1 stdout capture; catalog.json content edits; nasa chapter cleanup (P30); growth packs.
- **why_now**: without calibration plus wiring every subsequent tag can PASS while the documented freshness gate never runs; the fail-closed coverage fix must land first so the wired coverage set matches the live catalog contract, and the gate-PASS verification needs the P30 red set gone.
- **first_prompt**: `/superpowers-process full calibrate the 64-pack source watchlist, fix live-status fail-closed, and wire check 18 into check_release`

## Dependency order (triage, round 1)

P32, P30 (independent, either first), then P23, P25, P28, P29 (growth; P25 after P32), P26 after P25, P31 after P30. Any single package may start independently except P26 (needs P25) and P31 (needs P30's green gate baseline).

## Human forks

None in this cut. Outside packaging: the source-freshness-watch branch (HEAD 220f580, 6 commits) is unmerged; the merge decision stays with the maintainer. P8 remains frozen outside this cut.

## Backlog

See [backlog.md](../backlog.md). Delta: source-freshness-watch-2 promoted into P31; source-freshness-watch-1 routed needs-info (all three lenses killed it; IVL advisory-skipped); b-26 and b-27 stay promoted (P25/P26 unchanged). No rows added or dropped. Unchanged: b-01, b-02, b-06, b-07, b-09, b-10, b-12, b-14, b-15, b-16, b-18, b-22, b-23, b-28, b-29, b-30, b-31, html-self-contain-scan-1, automotive-packs-2.
