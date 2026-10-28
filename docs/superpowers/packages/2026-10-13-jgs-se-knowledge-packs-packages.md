---
date: 2026-10-13
project: jgs-se-knowledge-packs
mode: full
rounds: 2
input_digest: deefb9e35a58071a900ba6652fce5c3409b343d5c963a8105a6c486b815e2613
open_objections: []
---

# Work packages - jgs-se-knowledge-packs (2026-10-13, full re-run)

Context: the 2026-10-11 cut (P23, P25, P26, P28, P29, P30, P31, P32) fully executed 2026-10-12/13: five growth packs + avionics-signpost landed (catalogue now 68 content packs, 5 signposts, 1 orchestrator = 74 skills), the nasa chapter dupes are gone, and the source watch is calibrated (68 rows last_checked) with check 18 wired and a monthly cron created outside the repo. This cut is two rounds: round 1 converged six packages and failed the rail/space/maritime signpost cluster as Oversized; round 2 re-cut it into three single-domain signpost packages per triage direction and converged zero critical defects. One wave per round (round 1: value 5, risk 3, cohesion 3; round 2: value 9, risk 3, cohesion 6). Groom closed growth-registration-watchlist-surface-2 (both test suites green after P30) and se-orchestrator-skill-3 (grep-verified fixed).

## Carry-forward status

| id | name | status |
|----|------|--------|
| P1-P7, P9-P27, P29-P32 | prior cuts | done |
| P28 | uk-defence-jsp-pack (jsp-815, first pack) | done (2026-10-12) — id reused below for the second-JSP package |
| P8 | phase21-planning-ledger-close | in-flight (frozen; GitHub Release pending user go) |

## P33 - easa-rules-pack

- **id**: P33; **name**: easa-rules-pack; **size**: L; **status**: done (2026-10-13; ported from the jgs-aviation-knowledge-packs sibling prototype, pin re-verified 2026-10-13, registered on every gate surface incl. watchlist row; 69 packs / 75 skills; RELEASE CHECK: PASS v1.22.1 @ 0c9d76e; EXECUTED + IVL clean Track 1 Round 1); **corroboration**: 1 (value); **deps**: none; **promoted_ids**: [b-29]
- **problem**: build-order row 7 is only half done: nrc-nuclear shipped 2026-10-12, easa-rules is still pending. The avionics free-path story is asymmetric: faa-8110-49 and avionics-signpost are live, but the signpost's EASA AMC 20-115D/20-152A row is Open with the explicit limit "No EASA pack in this catalogue", so European software/safety regulator content has no installable landing.
- **evidence**: docs/candidate-packs.md:23 ("partially built 2026-10-12 (nrc-nuclear done, easa-rules pending). NRC guides are public domain; EASA Easy Access Rules are free downloads"); docs/candidate-packs.md:73 ("`easa-rules` (tier 2/3, vet per doc) ... Start with one volume relevant to software and systems (for example the rules covering 1309 safety objectives) rather than the whole library"); packs/avionics-signpost/SKILL.md:72 ("No EASA pack in this catalogue. The AMC row carries the free URL and nothing more"); docs/superpowers/backlog.md b-29.
- **in_scope**: vet and pin one EASA Easy Access Rules software/safety volume (or AMC-20 slice covering 20-115D/20-152A / 1309-class safety objectives); build packs/easa-rules per PACK-SPEC with tier 2/3 per-document licence statement; register on every live gate surface (SKILLS.md, /se routing, capability map, catalog.json, source-watchlist row); gates green.
- **out_scope**: whole EASA library dump; rebuilding avionics-signpost beyond naming the new pack as open path; paywalled RTCA/SAE content; other growth packs; version bump/release tag.
- **why_now**: the ranked remaining full-pack gap on the free regulator path; the shipped avionics signpost already points at the empty EASA landing, so this closes the named asymmetry before further aviation/EU growth.
- **first_prompt**: `/superpowers-process full build easa-rules pack from one EASA Easy Access Rules software/safety volume and register it`

## P34 - med-device-eu-pack

- **id**: P34; **name**: med-device-eu-pack; **size**: L; **status**: done (2026-10-13; built from scratch from six captured MDCG + MHRA sources, 8 chapters, tier 2 per-document Commission-reuse + OGL v3; registered on every gate surface; 70 packs / 76 skills; RELEASE CHECK: PASS v1.22.1 @ e1881a1; EXECUTED + IVL clean Track 1 Round 1); **corroboration**: 1 (value); **deps**: none; **promoted_ids**: [b-28]
- **problem**: build-order row 5 is untouched: med-device-eu (MDCG + MHRA) has no pack folder while fda-med-device landed 2026-10-12. Medical-device sector coverage is US-only, so EU/UK device software, PMS, and clinical-evaluation questions have no catalogue answer despite FULL sector feasibility and named tier-2/3 sources.
- **evidence**: docs/candidate-packs.md:20 ("`med-device-eu` | full | MDCG guidance is free to reuse with attribution; MHRA is OGL"); docs/candidate-packs.md:68 ("Chapter candidates: clinical evaluation, post-market surveillance, software as a medical device"); docs/candidate-packs.md:45 (sector table FULL); docs/superpowers/backlog.md b-28.
- **in_scope**: per-document vet of selected MDCG + MHRA sources; build packs/med-device-eu with chapters for SaMD / clinical evaluation / PMS as the source set allows; full registration (catalog, watchlist row, /se, capability map, SKILLS.md); gates green.
- **out_scope**: IEC 62304 / ISO 13485 clause reproduction (name only); re-opening fda-med-device content; functional-safety-signpost edits beyond an optional open-path cross-link; version bump.
- **why_now**: completes the medical-device geography axis immediately after the FDA half landed; ranked full pack with open sources and no on-disk pack.
- **first_prompt**: `/superpowers-process full build med-device-eu pack from MDCG and MHRA guidance and register it`

## P28 - uk-defence-next-jsp-pack

- **id**: P28; **name**: uk-defence-next-jsp-pack; **size**: L; **status**: done (2026-10-14; built packs/jsp-376 from JSP 376 Defence Acquisition Safety Policy V1.1 (April 2024), 8 chapters + glossary + cheatsheet, OGL v3 tier 2, atomic registration across all 17 surfaces; 71 packs / 5 signposts / 77 skills / 720 notes; RELEASE CHECK: PASS v1.22.1 @ 5f4b805; EXECUTED + IVL clean Track 1 Round 1); **corroboration**: 1 (value); **deps**: none; **promoted_ids**: []
- **problem**: cross-run re-proposal on the done uk-defence id: jsp-815 (first OGL pack, done 2026-10-12) is the family's only member and its build spec explicitly scoped it alone ("No other JSP. No `jsp-375`, no `jsp-376`, no `jsp-520`. No DEF-STAN"). candidate-packs row 4 remains "partially built ... other JSPs and DEF-STANs pending", so the UK defence line is a single-pack stub.
- **evidence**: docs/candidate-packs.md:19 ("partially built 2026-10-12 (jsp-815 done, other JSPs and DEF-STANs pending). OGL-licensed, no open competitor"); docs/candidate-packs.md:69 ("Built 2026-10-12 (jsp-815 only)"); docs/superpowers/specs/2026-10-12-uk-defence-jsp-pack.md:24-25; CHANGELOG.md:28 (jsp-815 V1.3 entry); prior packages doc P28 done entry.
- **in_scope**: pick and build exactly one next JSP (safety/assurance/requirements practice) under OGL v3.0 with per-document vetting; register on every gate surface including Licences/NOTICE attribution and a source-watchlist row; update /se UK family routing; update candidate-packs row 4 for the chosen slug only.
- **out_scope**: DEF-STANs (including unvetted Def Stan 00-051); multiple JSPs in one package; jsp-815 rework; non-OGL crown sources without per-document licence proof; version bump.
- **why_now**: jsp-815 proved the OGL path and the ranked family row is explicitly partial; one more JSP turns a beachhead into a line with known mechanics.
- **first_prompt**: `/superpowers-process full build the second uk-defence JSP pack under OGL and register it`

## P39 - rail-signpost

- **id**: P39; **name**: rail-signpost; **size**: S; **status**: done (2026-10-14; built packs/rail-signpost (SKILL.md + PACK.yaml, kind signpost, MIT, six-column tables: EN 50126-1/-2 2017+A1:2024, EN 50128:2011+A1/A2:2020, EN 50129:2018+2026, EN 50159:2010, twelve-row CSM/ORR free-path table, RSSB summaries-only; sixth signpost, M 5→6, skills 77→78, N stays 71; RELEASE CHECK: PASS v1.22.1 @ e6fb9b5; EXECUTED + IVL clean Track 1 Round 1); **corroboration**: 2 (value, cohesion); **deps**: none; **promoted_ids**: [b-30]
- **problem**: rail is a distinct paywalled-core sector (EN 50126/50128/50129) already scored SIGNPOST with named free paths (CSM regulations on EUR-Lex, RSSB standard summaries), and no packs/rail-signpost exists. First cut of the round-1 P35 cluster that failed Oversized; b-30 directs split-and-sequence per domain.
- **evidence**: docs/candidate-packs.md:23 ("`rail-signpost`, `space-signpost`, `maritime-signpost` | signpost | Cheap to build, each takes a day, and together they close the sector map"); docs/candidate-packs.md:84 ("`rail-signpost`: EN 50126/50128/50129. Free paths: CSM regulations on EUR-Lex, RSSB standard summaries"); docs/candidate-packs.md:55 (sector row SIGNPOST); docs/candidate-packs.md:63 (signpost grain: SKILL.md + PACK.yaml, no reproduced content); docs/superpowers/backlog.md b-30.
- **in_scope**: build packs/rail-signpost (SKILL.md + PACK.yaml only, kind signpost) mapping EN 5012x to its free paths; register signpost inventory surfaces (skill index, /se routing as applicable, capability map, check 13 M); no catalog.json or watchlist rows per mechanics; gates green.
- **out_scope**: space-signpost and maritime-signpost bodies; full EN 5012x knowledge pack; reproducing paywalled text; version bump.
- **why_now**: first domain in the triage-ordered rail, space, maritime sequence; establishes the post-P35 one-signpost-per-package grain (P26 precedent) before the siblings.
- **first_prompt**: `/superpowers-process full build rail-signpost pack mapping EN 5012x to free paths`

## P40 - space-signpost

- **id**: P40; **name**: space-signpost; **size**: S; **status**: done (2026-10-14; built packs/space-signpost (SKILL.md + PACK.yaml, kind signpost, MIT; six tables: ECSS E/M/Q/U rows Excluded with catalogue URLs incl. the two known-wrong slugs copied as fetched, 13-row Open NASA free-path table; seventh signpost, M 6-7, skills 78-79, N stays 71; RELEASE CHECK: PASS v1.22.1 @ 43250a4; EXECUTED + IVL clean Track 1 Round 1); **corroboration**: 2 (value, cohesion); **deps**: [P39]; **promoted_ids**: [b-30]
- **problem**: the ECSS family is scored SIGNPOST only (free after registration under ECSS licence; repo vetting already excludes ECSS from packaging) with free-path coverage via the existing NASA packs, and no packs/space-signpost exists. Second single-domain cut of the failed P35 cluster.
- **evidence**: docs/candidate-packs.md:85 ("`space-signpost`: ECSS family. Free paths: the existing NASA packs cover most ECSS-equivalent ground; the signpost names the ECSS document for each need and links to the ECSS catalogue"); docs/candidate-packs.md:56 ("repo vetting already excludes ECSS from packaging | SIGNPOST"); docs/candidate-packs.md:23; docs/superpowers/backlog.md b-30.
- **in_scope**: build packs/space-signpost (SKILL.md + PACK.yaml only, kind signpost) naming ECSS documents with catalogue links and pointing free paths at the existing NASA packs; register signpost surfaces only; no reproduced ECSS text; gates green.
- **out_scope**: packaging ECSS content (vetting-excluded); rail-signpost and maritime-signpost; NASA pack rebuilds; version bump.
- **why_now**: second step of the ordered sequence; disjoint standards family and free-path set from rail, so it stays its own package.
- **first_prompt**: `/superpowers-process full build space-signpost pack mapping ECSS to NASA free paths`

## P41 - maritime-signpost

- **id**: P41; **name**: maritime-signpost; **size**: S; **status**: done (2026-10-14; built packs/maritime-signpost (SKILL.md + PACK.yaml, kind signpost, MIT; five tables: SOLAS Consolidated Edition 2024 (IH110E) / ISM 2018 / ISPS 2003 + 2021 guide / COLREGS 2026 as Excluded IMO sales rows, US flag rows (eCFR Title 46, USCG NVICs, MSC) and UK MCA MSN/MGN/MIN rows Open, DNV/ABS/BV class portals Excluded free-to-read, IMO orientation rows Open; bot-gate caveats verbatim; eighth signpost, M 7-8, skills 79-80, N stays 71; candidate-packs row 8 fully built, b-30 closes; RELEASE CHECK: PASS v1.22.1 @ 4d26688; EXECUTED + IVL clean Track 1 Round 1); **corroboration**: 2 (value, cohesion); **deps**: [P40]; **promoted_ids**: [b-30]
- **problem**: maritime is a third disjoint SIGNPOST sector (SOLAS and class rules paywalled or unclear; USCG material public domain) with no packs/maritime-signpost. Final single-domain cut; landing it closes build-order row 8 and b-30 entirely.
- **evidence**: docs/candidate-packs.md:86 ("`maritime-signpost`: SOLAS, class rules. Free path: USCG material"); docs/candidate-packs.md:57 (sector row SIGNPOST); docs/candidate-packs.md:23; docs/superpowers/backlog.md b-30.
- **in_scope**: build packs/maritime-signpost (SKILL.md + PACK.yaml only, kind signpost) mapping SOLAS/class rules to USCG free paths; register signpost surfaces only; no IMO/class reproduced content; gates green.
- **out_scope**: full maritime/USCG content pack; rail-signpost and space-signpost; re-bundling the three domains; version bump.
- **why_now**: last step of the sequence; completes the cheap sector-map closure row 8 promised.
- **first_prompt**: `/superpowers-process full build maritime-signpost pack mapping SOLAS class rules to the USCG free path`

## P36 - dod-te-watchlist-publisher-hint

- **id**: P36; **name**: dod-te-watchlist-publisher-hint; **size**: S; **status**: done (2026-10-14; dod-te-guidebook hint filled per Ruling R1 (names test-evaluation.osd.mil + T- **id**: P36; **name**: dod-te-watchlist-publisher-hint; **size**: S; **status**: ready;E Enterprise Guidebook, no URL); publisher string kept; check_source_watch PASS; EXECUTED + IVL clean Track 1 Round 1); **corroboration**: 3 (value, risk, cohesion); **deps**: none; **promoted_ids**: [source-watch-calibrate-and-wire-1]
- **problem**: the dod-te-guidebook watchlist row still attributes the T&E Enterprise Guidebook to OUSD R&E (cto.mil) with an empty hint, after the 2026-10-13 maintainer resolution (Ruling R1) found no hosted copy on cto.mil at any revision and confirmed the same edition on the surviving publisher home (test-evaluation.osd.mil, already the recorded home for dote-te-guidebook). The monthly cron now runs against this row, so every future run keeps hitting the dead path until the hint field is filled.
- **evidence**: docs/source-watchlist.json:301-306 ("\"slug\": \"dod-te-guidebook\", \"publisher\": \"US Department of Defense, Office of the Under Secretary of Defense for Research and Engineering (OUSD R&E)\", ... \"last_checked\": \"2026-10-13\", \"hint\": \"\""); .zcode/source-watch/2026-10-12.md:67-71 ("A hint fix for this row is a backlog candidate"); .zcode/source-watch/2026-10-12.md:58-61 (dote-te confirmed on test-evaluation.osd.mil); docs/SOURCE-FRESHNESS.md:15-19 (hint is a first-class optional field; watchlist carries no URLs); docs/superpowers/backlog.md source-watch-calibrate-and-wire-1.
- **in_scope**: set the dod-te-guidebook hint to a non-URL search hint naming the surviving publisher home (test-evaluation.osd.mil / T&E Enterprise Guidebook) per Ruling R1; align the publisher string if needed for the same row; re-run check_source_watch validate and confirm the row still passes.
- **out_scope**: rebuilding dod-te-guidebook or dote-te-guidebook pack content; merging the two rows or deleting a slug; deciding any of the 14 recorded drift rebuilds; mirroring check 18 into CI; cron or orchestrator changes.
- **why_now**: P31 closed last_checked and wired check 18; this is the one concrete watchlist repair the calibration addendum already named, and it keeps every future monthly run cheap before more growth packs add rows.
- **first_prompt**: `/superpowers-process full fill the dod-te-guidebook source-watchlist hint per Ruling R1`

## P38 - contributing-ci-validate-truth

- **id**: P38; **name**: contributing-ci-validate-truth; **size**: S; **status**: done (2026-10-14; CONTRIBUTING.md:70 CI bullet rewritten to match validate.yml reality (CI does not run validate_pack; inline data-invariant checks named; step 6 local command pointed at; maintainer tier-review kept); validate.yml and PACK-SPEC untouched; EXECUTED + IVL clean Track 1 Round 1); **corroboration**: 3 (value, risk, cohesion); **deps**: none; **promoted_ids**: [growth-registration-watchlist-surface-1]
- **problem**: CONTRIBUTING.md tells contributors CI runs validate_pack.py on every pack and blocks invalid licence tiers and broken chapter links, but validate.yml's header and PACK-SPEC both state the opposite: CI never executes checked-out repository code and full validate_pack is deliberately kept local-only to avoid parser fork drift. Every new pack PR is opened under a false gate story; P32 deferred exactly this residual to the backlog.
- **evidence**: CONTRIBUTING.md:70-71 ("CI runs `validate_pack.py` on every pack and blocks invalid licence tiers and broken chapter links"); .github/workflows/validate.yml:4-5 ("never executes checked-out repository code") and :26-32 ("CI does not cover, and why: full validate_pack (non-trivial parser; a fork invites permanent drift)"); docs/PACK-SPEC.md:108-111 ("deliberately kept out of CI to avoid parser fork drift; CI runs inline data-invariant heredocs instead"); docs/superpowers/backlog.md growth-registration-watchlist-surface-1; docs/superpowers/specs/2026-10-12-growth-registration-watchlist-surface.md:30 (deferred as backlog capture).
- **in_scope**: rewrite the CONTRIBUTING.md Open-a-PR CI bullet to match validate.yml + PACK-SPEC reality (local validate_pack via check_release check 5; CI inline data-invariant subsets only); name the real local commands contributors must run before a PR; grep-confirm no other contributor doc still claims CI executes validate_pack.py; leave validate.yml behavior unchanged.
- **out_scope**: adding validate_pack.py execution to CI; parser or gate behavior changes; PACK-SPEC structural redesign; pack builds; watchlist or inventory prose.
- **why_now**: the candidate build order still has multiple growth rows, so every future pack PR re-reads CONTRIBUTING; the false claim is the last open growth-registration residual after P32.
- **first_prompt**: `/superpowers-process full align the CONTRIBUTING CI validate_pack claim with validate.yml and PACK-SPEC`

## P37 - catalogue-inventory-prose-sync

- **id**: P37; **name**: catalogue-inventory-prose-sync; **size**: M; **status**: done (2026-10-14; SOURCE-FRESHNESS.md 64->71 live packs + check-18 prose present tense with check_release cites; candidate-packs.md 66->80 packs (71 content + 8 signpost + 1 orch), eight signpost slugs named, rows 2/5/6/7 + Proposed bullets med-device-eu/nhtsa-vehicle/easa-rules + free-path bullets built-marked; PACK-SPEC verified already current, untouched; CHANGELOG Changed bullet; residual grep clean; EXECUTED + IVL clean Track 1 Round 1); **corroboration**: 3 (value, risk, cohesion); **deps**: none; **promoted_ids**: []
- **problem**: gate-enforced surfaces and badges already read 68 packs / 5 signposts, but three unenforced inventory prose surfaces still teach pre-growth state: docs/SOURCE-FRESHNESS.md opens with "The catalogue's 64 live packs" and describes check-18 failure as "once that check is wired" although check 18 is already called from check_release; docs/PACK-SPEC.md's kind table says content packs are "the 64 catalogue packs"; docs/candidate-packs.md says the catalogue "holds 66 packs" with only two signpost packs and still presents functional-safety-signpost, automotive-signpost, and nhtsa-vehicle as unbuilt or proposed even though they ship. Maintainerrs and growth agents reading these surfaces inherit a wrong inventory.
- **evidence**: docs/SOURCE-FRESHNESS.md:8-9 ("The catalogue's 64 live packs were each built from one upstream document"); docs/SOURCE-FRESHNESS.md:51-54 ("keeps the release gate's source-watch check failing once that check is wired (the wiring lands after the first calibration run...)"); docs/PACK-SPEC.md:103 ("| content pack (default) | the 64 catalogue packs |"); docs/candidate-packs.md:29 ("The catalogue holds 66 packs ... two signpost packs (`se-standards-signpost`, `omg-signpost`)"); docs/candidate-packs.md:17, 21, 81 (shipped packs presented as unbuilt/proposed); tooling/check_release.py:60-63 (check 18 wired, local-only); SKILLS.md:9 ("68 packs (+5 signposts, +1 orchestrator)").
- **in_scope**: update SOURCE-FRESHNESS.md live-pack count prose to the current live count and rewrite the check-18 wiring prose to present tense; update PACK-SPEC.md kind-table member counts/lists; update candidate-packs.md standing count, signpost inventory, build-order built markers, and free-path wording so shipped packs match packs/ + SKILLS.md; grep pass for residual frozen "64" claims on live-path surfaces; leave gate-enforced surfaces (already at 68) and historical CHANGELOG/milestone narratives alone.
- **out_scope**: building or re-registering any pack; watchlist drift rebuilds or the dod-te hint (P36); CONTRIBUTING CI claim (P38); website YAML / README / index badges (already current); se-orchestrator-skill-3 re-litigation (grep-verified done); version bump.
- **why_now**: every future growth or monthly-watch run reads these intake surfaces first; syncing them once now prevents the next pack wave from compounding the stale 64/66 baselines, and the signpost packages (P39-P41) will change check 13's M again right after.
- **first_prompt**: `/superpowers-process full sync inventory prose counts in SOURCE-FRESHNESS, PACK-SPEC, and candidate-packs to the 68-pack catalogue`

## Dependency order (triage, round 2)

P33, P34, P28 are independent growth packages (any may start first). P39 before P40 before P41 (sequence adopted from the b-30 split; each passes alone). P36, P38, P37 are independent small packages; run them whenever a gap opens between growth runs. Recommended order: P33, P34, P28, P39, P40, P41, P36, P38, P37.

## Human forks

Unchanged from the prior cut, plus branch state: packages-2026-10-12 is 34 commits ahead of main and origin/main (merge/push decision is the maintainer's); source-freshness-watch (6 commits) remains unmerged into both. P8 phase21-planning-ledger-close stays frozen in-flight (STATE.md: GitHub Release pending user go). The 14 recorded drift findings stay bookkeeping-only (source-watch-calibrate-and-wire-2 open); rebuild decisions are maintainer calls under D-04. The monthly watch cron exists outside the repo and is orchestrator-owned.

## Backlog

See [backlog.md](../backlog.md). Delta: promoted b-28 into P34, b-29 into P33, b-30 into P39/P40/P41 (one row spanning the three signpost packages; closes when P41 lands), source-watch-calibrate-and-wire-1 into P36, growth-registration-watchlist-surface-1 into P38; added b-32 (fhwa-its-se absent from the numbered build-order table) and b-33 (standing-drift first-production catalog_equivalent spot-check), both needs-info; closed growth-registration-watchlist-surface-2 (both test suites green after P30) and se-orchestrator-skill-3 (grep-verified: the "46 packs" title and gen_skills_index header claims are gone) as done. Unchanged: b-01, b-02, b-06, b-07, b-09, b-10, b-12, b-14, b-15, b-16, b-18, b-22, b-23, b-31, automotive-packs-2, html-self-contain-scan-1, source-freshness-watch-1, source-watch-calibrate-and-wire-2.
