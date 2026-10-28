---
date: 2026-10-27
project: jgs-se-knowledge-packs-doc-truth
mode: full
rounds: 1
input_digest: c64fe3d3131022345762dba59cd2891d24d2e29eeebd071f2ac0e01bed0bd21e
open_objections: ["X3"]
---

Picked 2026-10-27 (user: run all four cuts to completion). X3 default: content-only baseline (side A); side-B stale-token assertion stays parked on backlog b-45.

# Work packages - jgs-se-knowledge-packs-doc-truth (2026-10-27, full scoped re-run)

Scope of this cut: public-surface and maintainer-surface truth. P43 FAA family sync
(reused id, fork X3), P54 PACK-SPEC install path, P55 catalog stamp, P56 build
orchestrator META. P45 and P47 were demoted to backlog by triage (no current bite;
1-lens re-proposals dual-killed by value and risk). Converged in one round (value 4,
risk 2, cohesion 6 candidates; merge produced 6 packages; triage zero_critical).
Open fork X3 travels in `open_objections`.

## P43 - website-faa-family-inventory-sync

- **id**: P43; **name**: website-faa-family-inventory-sync; **size**: M; **status**: done; **corroboration**: 3 (value, risk, cohesion); **deps**: none; **promoted_ids**: [easa-rules-pack-1]
- **problem**: Website product YAML section-06 still teaches FAA (7) plus a separate FAA-airborne (1) line while the live FAA set and the docs/index.html chip are eight packs (faa-8110-49 folded in); freeform family bullets also lag the live catalogue (missing easa-rules and med-device-eu; families under-sum 71). check 4a only gates bare "N packs" integers, so RELEASE CHECK stays green while the published family inventory is wrong (prior-cut fork, renumbered X3 this run).
- **evidence**: docs/products/website/01-jgs-se-knowledge-packs.yaml:L57-59 ("FAA (7): RMA Handbook, ..."), L68 ("FAA airborne software and AEH approval (1): Order 8110.49A and ACs ..."); docs/index.html:L194 ("FAA &middot; 8" chip with the folded description); tooling/check_release.py:L1037-1041 (pack-count regex matches only "N packs" integers).
- **in_scope**: rewrite the FAA family count/list to the live eight-pack set; reconcile section-06 family detail with live packs/ and index chips (easa-rules, med-device-eu; re-sum to 71); grep residual FAA (7) and split-pattern claims; resolve X3 (side A content-only vs side B content plus a hard stale-token assertion on check 4a failing on "FAA (7)"); promote/close easa-rules-pack-1; confirm check_release PASS.
- **out_scope**: check 4a tuple-to-glob discovery (routed to backlog b-43 this run); leak/link single-read (backlog b-44); pack content rebuilds; index.html redesign; catalog stamp (P55); version bump.
- **why_now**: public family inventory wrong under a green gate; the next growth pack only deepens the mismatch unless the family body is fixed and X3 answered.
- **triage notes**: PASS with fork noted, size M. The content-only baseline is fully evidenced and startable; the side-B delta is one bounded stale-token assertion in check 4a, so either human pick still fits one run. X3 goes to the human fork, not a startability blocker.
- **first_prompt**: `/superpowers-process full sync website FAA family inventory to the live catalogue`

## P54 - pack-spec-install-path-drift

- **id**: P54; **name**: pack-spec-install-path-drift; **size**: M; **status**: done; **corroboration**: 3 (value, risk, cohesion); **deps**: none; **promoted_ids**: []
- **problem**: docs/PACK-SPEC.md install section teaches a manual flat copy into ~/.claude/skills/\<slug\> and promises a future tooling/install.py, while root install.py/install.sh/install.ps1 and README already ship the namespaced default plus multi-agent targets (--dry-run, --flat, --agent, --list-agents). The pack contract is the first doc contributors and users read; it points at a path that does not exist (finding I3, MEDIUM).
- **evidence**: docs/PACK-SPEC.md:L84-91 ("cp -r jgs-se-knowledge-packs/packs/sebok ~/.claude/skills/sebok" and "(A future `tooling/install.py <slug>` will automate per-pack install across hosts.)"); README install.py flow.
- **in_scope**: rewrite the Installing a pack section to root installer truth (namespaced default, --flat, --agent/--list-agents pointers); delete or replace the dead future-tooling promise; grep PACK-SPEC for other install-path residue; one-line cross-link to README.
- **out_scope**: installer behavior changes; CONTRIBUTING runbooks (P53 in the site-gates cut); catalog stamp (P55); version bump.
- **why_now**: the contract doc lies about install path today; every new reader inherits the wrong default.
- **triage notes**: PASS, size M.
- **first_prompt**: `/superpowers-process full rewrite PACK-SPEC install section to the shipped installer`

## P55 - catalog-updated-field-stale

- **id**: P55; **name**: catalog-updated-field-stale; **size**: S; **status**: done; **corroboration**: 2 (value, cohesion); **deps**: none; **promoted_ids**: []
- **problem**: catalog.json top-level updated stays 2026-08-27 while the catalogue moved through 1.22.1 (2026-10-11); machine consumers and humans read it as freshness metadata (finding I4, MEDIUM). Risk lens judged the bite advisory-class; value and cohesion carried it as a one-field truth fix.
- **evidence**: catalog.json:L5 (`"updated": "2026-08-27",`); tooling/check_release.py:L47 ("updated is review-only after the b-03 bump."); CHANGELOG 1.22.1 dated 2026-10-11.
- **in_scope**: define and apply the updated stamp policy (current release date, last pack-set change, or document the review-only rule); set the field consistently; align the check_release comment if the policy hardens.
- **out_scope**: live pack row edits; live-set schema changes; planned[] edits; version bump machinery.
- **why_now**: named public truth surface; a one-field fix stops freshness misreads by any consumer keying the field.
- **triage notes**: PASS, size S.
- **first_prompt**: `/superpowers-process full set catalog.json updated stamp policy and truthful value`

## P56 - stale-build-orchestrator-backlog

- **id**: P56; **name**: stale-build-orchestrator-backlog; **size**: S; **status**: done; **corroboration**: 2 (value, cohesion); **deps**: none; **promoted_ids**: []
- **problem**: tooling/build_all_packs.workflow.js META is frozen on already-shipped packs and points agents at docs/PACK-BACKLOG.md, absent from docs/; META also names unshipped slugs (nasa-swehb, grcse, dau-glossary) with no candidate-packs or catalog row (finding I1, MEDIUM). Risk lens judged it maintainer-only; value and cohesion carried it as a single-file rot fix.
- **evidence**: tooling/build_all_packs.workflow.js:L40-41 (dead PACK-BACKLOG.md pointer), L112 (prepare prompt reads the missing file), L57 (unshipped META row).
- **in_scope**: retarget or remove the dead docs/PACK-BACKLOG.md pointers (live surfaces are docs/candidate-packs.md and docs/PACK-SPEC.md); reconcile META with live packs/ and candidate-packs (drop shipped noise; park or justify unshipped slugs); keep the bulk-build path usable for remaining unshipped rows only.
- **out_scope**: building those unshipped packs; PACK-SPEC install rewrite (P54); catalog stamp (P55); check_release changes; version bump.
- **why_now**: the bulk-build path lies about its backlog file and staged set; single-file fix, cheap and contained.
- **triage notes**: PASS, size S.
- **first_prompt**: `/superpowers-process full retarget build orchestrator META and dead backlog pointers`

## P45 - website-yaml-check-glob (routed to backlog)

- **id**: P45; **name**: website-yaml-check-glob; **size**: S; **status**: proposed; **corroboration**: 1 (cohesion); **deps**: none; **promoted_ids**: []
- **problem**: check 4a hardcodes a two-file website_yamls tuple, so a future third docs/products/website/*.yaml would escape version and N-packs scans. Carried over proposed from the 2026-10-15 cut.
- **evidence**: tooling/check_release.py:L1013-1027 (two-file tuple covers both existing YAMLs: 01-jgs-se-knowledge-packs.yaml and catalog.yaml).
- **triage notes**: grade routed-to-backlog. Value and risk both killed it this round and the verification confirmed exactly two YAML files exist, so no current silent escape. The easa-rules-pack-2 promotion (2026-10-15) reverts; backlog row b-43 carries the trigger condition. No first_prompt; not startable; re-cut via /package-loop full jgs-se-knowledge-packs-doc-truth if a third YAML ever lands.

## P47 - check-release-single-read (routed to backlog)

- **id**: P47; **name**: check-release-single-read; **size**: S; **status**: proposed; **corroboration**: 1 (cohesion); **deps**: none; **promoted_ids**: []
- **problem**: check_release runs the leak-sentinel and source-link loops as two passes, each calling read_text on every text file; CONCERNS and backlog b-14 name the double-read. Carried over proposed from the 2026-10-15 cut.
- **evidence**: tooling/check_release.py:L966-996 (text_files list plus two re-reading loops).
- **triage notes**: grade routed-to-backlog. Value and risk both killed it: I/O cost only, no correctness, security, or licence bite. The b-14 promotion (2026-10-15) reverts; backlog row b-44 carries the trigger condition. No first_prompt; not startable; re-cut via /package-loop full jgs-se-knowledge-packs-doc-truth if the I/O cost ever bites.
