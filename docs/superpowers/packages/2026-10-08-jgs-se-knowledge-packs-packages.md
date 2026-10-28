---
date: 2026-10-08
project: jgs-se-knowledge-packs
mode: full
rounds: 2
input_digest: 1eab3cb00e9051b5cafc56c68f33a0a942bf5d3ef35aaa61049d4a91d82e465e
open_objections: []
---

# Work packages - jgs-se-knowledge-packs (2026-10-08, full re-run)

Context: pack-quality-fixes executed 2026-10-08 (11 commits, EXECUTED, IVL clean) landed the per-pack content gate (check 16 + ninth CI step), EARS repairs, dodaf routing, five nasa renames, six chapter deepens. P1-P16 done; P8 frozen in-flight. Landing counts verified true (69 = 64 content + 4 signposts + 1 orchestrator); survey's "65 content" was a miscount. Round 1 triaged 8 candidates, FAILed the oversized avionics cluster (split b-26/b-27); round 2 re-proposed the halves standalone and added four growth packages. Converged round 2, zero critical defects.

## Carry-forward status

| id | name | status |
|----|------|--------|
| P1-P7, P9-P16 | prior cuts | done |
| P8 | phase21-planning-ledger-close | in-flight (frozen) |

## P17 - surface-truth-drift

- **id**: P17; **name**: surface-truth-drift; **size**: S; **status**: done; **corroboration**: 3 (value, risk, cohesion); **deps**: none; **promoted_ids**: [se-orchestrator-skill-3]
- **problem**: docs/products/website/01-jgs-se-knowledge-packs.yaml:47 feature title still says "46 packs across the SE landscape" (live: 64/4/1); SKILLS.md:4 names tooling/gen_skills_index.py which does not exist. check 4a pins YAML versions, not titles, so RELEASE CHECK PASS ships the lie.
- **in_scope**: rewrite the YAML feature title/detail to live inventory (or gate it); fix the SKILLS.md regen pointer to the real path (hand-maintained + gen_packs_page.py) without inventing the script; optional thin count-claim gate if cheap; promote se-orchestrator-skill-3.
- **out_scope**: landing §06/still-catalogue (counts true); catalog.json; se-orchestrator-skill-1/2; building gen_skills_index.py.
- **why_now**: last published-surface lie after P15/P16; every release can ship PASS with a 46-pack product claim.
- **first_prompt**: `/superpowers-process full fix website YAML 46-packs title and SKILLS.md dead gen_skills_index pointer to live inventory`

## P18 - kind-detection-align

- **id**: P18; **name**: kind-detection-align; **size**: M; **status**: done; **corroboration**: 1 (cohesion); **deps**: none; **promoted_ids**: [pack-quality-fixes-1]
- **problem**: pack-kind regexes split across tools: check_release inventory_pack_slugs is case-insensitive (:343-346) while its own signpost_dirs helper (:932-933), validate_pack (:69-70), and check_pack_quality (:58-61) are case-sensitive. Check 16 just joined the consumers; a non-canonical kind line fails one gate and passes another.
- **in_scope**: one shared kind-match policy (or identical flags) across the three tools and both check_release sites; probe coverage for mixed-case kind lines; docs that claim parity.
- **out_scope**: new kind values; routing-map content; nasa prose fix.
- **why_now**: small shared-subsystem align while the third consumer is fresh; prevents split live-set classification.
- **first_prompt**: `/superpowers-process full unify pack-kind detection across validate_pack, check_pack_quality, and check_release`

## P19 - nasa-techniques-count-truth

- **id**: P19; **name**: nasa-techniques-count-truth; **size**: S; **status**: done; **corroboration**: 1 (value); **deps**: none; **promoted_ids**: [pack-quality-fixes-2]
- **problem**: packs/nasa-se-handbook/SKILL.md:24,100 advertise "20 techniques"; patterns.md holds 21 technique sections. Deferred by the pack-quality run as a non-goal; still a counted falsehood on the flagship pack surface.
- **in_scope**: correct both counts to 21; promote pack-quality-fixes-2.
- **out_scope**: patterns.md content; kind-align; other packs' counts unless same bug evidenced.
- **why_now**: smallest remaining pack-faithfulness lie; two-line fix protecting the highest-traffic pack claim.
- **first_prompt**: `/superpowers-process full correct nasa-se-handbook SKILL.md techniques count to actual 21`

## P20 - committed-source-build-extracts

- **id**: P20; **name**: committed-source-build-extracts; **size**: S; **status**: done (premise corrected: nothing tracked under sources/ across all refs; shipped check 17 invariant + CI residual); **corroboration**: 1 (risk); **deps**: none; **promoted_ids**: []
- **problem**: sources/*/.build trees for five packs (dod-digital-engineering, dod-mosa, dod-mq-bok, dod-rio, dod-te-guidebook) are tracked in git despite .gitignore:10-17 banning sources/, **/.build/, and *.full_text.txt. The extracts carry licence-bearing source prose and absolute OneDrive paths; every clone redistributes what the product refuses to publish.
- **in_scope**: confirm tracked paths (git ls-files); git rm --cached all sources//**/.build paths (keep working-tree extracts local); verify ignore coverage + force-add trap note; small release/CI invariant that tracked sources/ paths stay empty; confirm scanners still skip sources/.
- **out_scope**: deleting local PDFs; history rewrite/BFG (nothing pushed since the commits, decide at execution if needed); moving sources/ out of the repo root.
- **why_now**: licence/redistribution exposure compounds on every clone and tag; ignore rules already state the policy, so this is a broken window, not a design debate. Surface work should not outrank shipping banned source text.
- **first_prompt**: `/superpowers-process full untrack committed sources .build extracts and gate against re-tracking`

## P21 - build-orchestrator-onedrive-defaults

- **id**: P21; **name**: build-orchestrator-onedrive-defaults; **size**: S; **status**: done; **corroboration**: 1 (risk); **deps**: none; **promoted_ids**: [b-11]
- **problem**: tooling/build_all_packs.workflow.js:24-25 defaults PACKS/REF to absolute OneDrive paths on one machine; the documented "one go" build entrypoint fails anywhere else, blocking future pack intake by non-owner contributors.
- **in_scope**: derive PACKS from repo root by default; require refSkillDir via args/env with fail-closed error; remove the literals; document launch args; mark b-11 done.
- **out_scope**: vendoring jgs-reference-skill; CI running the full orchestrator; installer layout (b-12).
- **why_now**: next staged pack batch (P23/P25/P28/P29) hits this first if built via the orchestrator.
- **first_prompt**: `/superpowers-process full make build_all_packs workflow paths repo-relative and fail-closed`

## P22 - catalog-title-dash-normalize

- **id**: P22; **name**: catalog-title-dash-normalize; **size**: S; **status**: done (verified no-op: catalog.json already single-form); **corroboration**: 1 (cohesion); **deps**: none; **promoted_ids**: [automotive-packs-1]
- **problem**: catalog.json carries a mixed title-encoding pocket (em dash vs escaped forms, ~8 old rows across :64-273 plus stragglers): a second truth dialect beside the corrected landing/SKILLS counts.
- **in_scope**: one-policy dash normalization across affected live rows; confirm check 14/catalog-live-set stays green; no slug/status churn.
- **out_scope**: automotive-packs-2 live URL check; P17 surfaces; adding orchestrator/signpost rows to catalog.packs.
- **why_now**: bounded, ticketed, single-file; keeps the machine catalogue in one dialect before growth packs add rows.
- **first_prompt**: `/superpowers-process full normalize catalog.json title dash escapes in one dedicated commit`

## P27 - se-landing-orchestrator-chip

- **id**: P27; **name**: se-landing-orchestrator-chip; **size**: M; **status**: done; **corroboration**: 1 (cohesion); **deps**: none; **promoted_ids**: [se-orchestrator-skill-2]
- **problem**: advertising /se on landing §06 is not copy-only: every non-signpost chip adds to content N in check 13 (check_release.py:372-399 chip parser), and /se is kind: orchestrator. Needs the chip-taxonomy change first (backlog se-orchestrator-skill-2).
- **in_scope**: check 13 orchestrator-chip exemption mirroring the signpost grain; landing /se chip mention + still-catalogue copy consistency; probe coverage for the new chip class; catalog live-set keeps excluding orchestrators.
- **out_scope**: P17 strings; se-orchestrator-skill-1 (dropped); routing-map content; ATTR residual.
- **why_now**: only open se-* row coupling HTML UX to the count gate; distinct from P17 (taxonomy vs strings).
- **first_prompt**: `/superpowers-process full add check 13 orchestrator-chip exemption and land the /se landing mention`

## P23 - fda-med-device-pack

- **id**: P23; **name**: fda-med-device-pack; **size**: L; **status**: proposed; **corroboration**: 1 (value); **deps**: none; **promoted_ids**: []
- **problem**: candidate-packs.md ranks fda-med-device #1: tier-1 US public-domain device guidance (QMSR/21 CFR 820, device software, premarket, cybersecurity), zero open competitor, large audience; no packs/fda-med-device exists. functional-safety-signpost's free-path story names it as proposed.
- **in_scope**: vet + build packs/fda-med-device per PACK-SPEC from tier-1 FDA guidance; register in SKILLS.md, catalog.json, /se routing, capability map; all gates green incl. check 16.
- **out_scope**: med-device-eu (backlog b-28); landing counts; P8; distribution submissions; tooling pets.
- **why_now**: standing #1 growth item; highest-payoff new sector on the published growth ledger.
- **first_prompt**: `/superpowers-process full build fda-med-device pack from tier-1 FDA guidance and register it`

## P25 - faa-8110-49-pack

- **id**: P25; **name**: faa-8110-49-pack; **size**: L; **status**: proposed; **corroboration**: 2 (value, cohesion); **deps**: none; **promoted_ids**: [b-26]
- **problem**: seven faa-* packs ship but the FAA family lacks FAA Order 8110.49 (software certification guidance for DO-178C usage; tier 1, public domain; candidate-packs.md:70). The avionics free-path story needs this content half (round-1 split b-26).
- **in_scope**: build packs/faa-8110-49 per PACK-SPEC; register across surfaces; gates green.
- **out_scope**: avionics-signpost (P26); easa-rules; reproducing DO-178C/DO-254/ARP text.
- **why_now**: the split half two lenses re-proposed; unlocks the avionics sector alongside P26.
- **first_prompt**: `/superpowers-process full build faa-8110-49 pack from FAA Order 8110.49 and register it`

## P26 - avionics-signpost-pack

- **id**: P26; **name**: avionics-signpost-pack; **size**: S; **status**: proposed; **corroboration**: 2 (value, cohesion); **deps**: [P25]; **promoted_ids**: [b-27]
- **problem**: DO-178C/DO-254/ARP4754A/ARP4761 are paywalled; candidate-packs.md:82 defines avionics-signpost mapping them to free paths (faa-8110-49, existing faa-*, EASA AMC). Same grain as the shipped automotive/functional-safety signposts; none exists.
- **in_scope**: packs/avionics-signpost (SKILL.md + PACK.yaml, kind: signpost, zero reproduced text); open-path rows to faa-* and P25; signpost inventory surfaces so check 13's M stays true; gates green.
- **out_scope**: faa-8110-49 content (P25); easa-rules; merging with other signposts.
- **why_now**: cheapest sector close; dep on P25 is soft (pointer works either way) but order honors the complete avionics story.
- **first_prompt**: `/superpowers-process full build avionics-signpost pack mapping DO-178C family to free paths`

## P28 - uk-defence-jsp-pack

- **id**: P28; **name**: uk-defence-jsp-pack; **size**: L; **status**: proposed; **corroboration**: 1 (value); **deps**: none; **promoted_ids**: []
- **problem**: candidate-packs.md ranks a UK defence family next (OGL v3, no open competitor, matches consultancy identity); catalogue is US-federal-only on defence practice. One starter JSP pack on gov.uk, vet per document (SOURCE-VETTING already excludes unvetted DEF-STANs).
- **in_scope**: one packs/uk-defence-jsp-* from a single OGL JSP; tier-2 SOURCE-VETTING record; in-pack OGL licence text + attribution; surface registration; gates green. Family expansion later.
- **out_scope**: any DEF-STAN (incl. 00-051) until in-document terms recorded; full JSP library; med-device-eu.
- **why_now**: next full-pack row in the published build order; unique geography payoff.
- **first_prompt**: `/superpowers-process full build first uk-defence JSP pack under OGL with per-document vetting`

## P29 - nrc-nuclear-pack

- **id**: P29; **name**: nrc-nuclear-pack; **size**: L; **status**: proposed; **corroboration**: 1 (value); **deps**: none; **promoted_ids**: []
- **problem**: nuclear/energy scored FULL on public-domain NRC guides (candidate-packs.md:72: NUREG-0800 chapters, RG 1.168 siblings); no nrc-* pack or /se NRC row; sibling families (nasa-system-safety, DOE) already ship.
- **in_scope**: one packs/nrc-nuclear tier-1 pack scoped to digital-systems/software-assurance guides; SOURCE-VETTING tier-1 note; catalog/SKILLS//se NRC agency row + capability map; gates green.
- **out_scope**: ONR/HSE UK nuclear; whole NUREG library; easa-rules (b-29).
- **why_now**: clean tier-1 growth parallel to FDA/FAA paths; extends safety coverage into nuclear without new tooling.
- **first_prompt**: `/superpowers-process full build nrc-nuclear pack from NRC guides and NUREGs and register it`

## Dependency order (triage, full round 2)

P17, P18, P19, P20, P21, P22, P27 (fixes and gate work first), then P23, P25, P26, P28, P29 (growth; P26 after P25). Any single package may start independently except P26.

## Human forks

None. P8 remains frozen outside this cut.

## Backlog

See [backlog.md](../backlog.md). Delta: se-orchestrator-skill-3, se-orchestrator-skill-2, pack-quality-fixes-1, pack-quality-fixes-2, b-11, automotive-packs-1, b-26, b-27 promoted into P17/P27/P18/P19/P21/P22/P25/P26; b-13 done (pack-quality run); se-orchestrator-skill-1 dropped (prior Design disposition); b-12 re-routed needs-info (premise stale: scripts/ holds only configure_repo.sh); b-28..b-31 added needs-info (later candidate-packs rows); b-10/b-14/b-18/automotive-packs-2/html-self-contain-scan-1 unchanged.
