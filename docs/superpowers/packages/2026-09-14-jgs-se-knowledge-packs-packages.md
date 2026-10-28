---
date: 2026-09-14
project: jgs-se-knowledge-packs
mode: full
rounds: 2
input_digest: 7788c2cdde9a730594cf960e526aeec09d422d0fb2017ecad670bf9a29db3b00
open_objections: []
---

# Work packages — jgs-se-knowledge-packs (2026-09-14, full re-run, round 2)

Context: re-run after P1 landed. Commit ffe385a aligned both website product YAMLs to 1.20.0, extended check_release check 4 with the scoped website-YAML consistency check (4a), and the local annotated tag v1.20.0 was recreated on it (IVL Track 1 clean). CR-01 is closed on disk; the GSD ledger still cites it. Round 2 re-cut with cross-run id matching: P1 done (out of space), P2 done by absorption (its scope landed inside P1), P3-P8 re-confirmed with corroboration. X1 (P3 vs P8 ship-step ownership) remains an open human fork, re-escalated unresolved.

## P1 — align-website-yaml-versions

- **id**: P1
- **name**: align-website-yaml-versions
- **size**: S
- **status**: done
- **promoted_ids**: []
- **corroboration**: 2 (value, cohesion)

**problem**: (round 1) Phase 21 shipped the 1.20.0 version trio and public REV strings and created local annotated tag v1.20.0, but the two RR-B-19 public-website product YAMLs under docs/products/website/ still claimed 1.19.1. Impl review blocked the phase on CR-01.

**outcome**: Done in commit ffe385a (2026-09-14). Both YAMLs at `version: "1.20.0"`; gate PASS; tag v1.20.0 retagged onto the fix commit; optional gate hardening landed (see P2). Dropped from the round-2 candidate space per re-run rules.

## P2 — gate-website-yaml-versions

- **id**: P2
- **name**: gate-website-yaml-versions
- **size**: S
- **status**: done
- **promoted_ids**: []
- **corroboration**: 1 (value)

**problem**: (round 1) check_release version single-source only compared plugin.json, CHANGELOG top heading, and RELEASE-INFO; the website product YAMLs sat outside the gate, so the CR-01 drift class was invisible.

**outcome**: Done by absorption into P1 (2026-09-14). The contract-optional consistency check landed in commit ffe385a as check_release.py block 4a: scoped to exactly the two website YAML paths, regex first-match per file, compared against the RELEASE-INFO version already parsed into `versions`, failing through the existing `[version]` idiom; docstring updated to name the two YAMLs. Negative test proved exit 1 naming the drifted file and no fire on a `packs/*/PACK.yaml` source_version change. All three round-2 lenses independently killed P2 as already landed (tooling/check_release.py:121-132). No remaining delta; P4/P5 carry the broader gate-coverage work.

## P3 — close-phase21-ship-surface

- **id**: P3
- **name**: close-phase21-ship-surface
- **size**: M
- **status**: done
- **promoted_ids**: []
- **corroboration**: 3 (value, risk, cohesion)

**problem**: v1.20.0 product work and the CR-01 website YAML fix are on disk (local tag retagged on ffe385a), but Phase 21 sits at a stale impl_review verdict that still cites the fixed 1.19.1 drift, ROADMAP still shows Phase 21 0/2 Not started, REL-21-01/REL-21-02 remain unchecked with no GitHub Release, and master_flow still carries pre-fix needs_work markers. Operators read a lying blocker and could re-open fixed work or ship without clearing the honest release path.

**evidence**:
- .planning/phases/21-contract-rewrite-release-surfaces/master_flow_state.json:9 `"current_gate": "impl_review"`
- .planning/phases/21-contract-rewrite-release-surfaces/master_flow_state.json:55 `"impl_review": "needs_work:cr_01:_docs/products/website/01_jgs_se_knowledge_packs.yaml_still_version_1.19.1;_retag_after_bump"` (STALE — fix landed in ffe385a)
- .planning/ROADMAP.md:103 `| 21. CONTRACT rewrite + release surfaces | 0/2 | Not started | - |`
- .planning/phases/21-contract-rewrite-release-surfaces/21-02-SUMMARY.md:149 `- /gsd-ship: create GitHub Release for v1.20.0 when ready. Local annotated tag already exists; do not recreate as lightweight.`

**in_scope**: re-gate impl_review after the CR-01 fix (clear the stale needs_work:cr_01 markers); repair stale master_flow Phase 21 fields so the verdict no longer cites fixed drift; finish remaining Phase 21 product gates needed to mark MAP-21-05 / REL-21-01 / REL-21-02 complete.

**out_scope**: website YAML bump (P1 done); check_release 4a gate (landed in ffe385a); new packs or sibling se-agents refresh; WR-01/WR-02/WR-03 residuals (P7); CI host-list or coverage redesign (P4/P5); creating the GitHub Release (X1 resolved 2026-09-14: P8 owns /gsd-ship).

**why_now**: CR-01 and the local retag are done; the re-gate clears the stale blocker so P8 can close the ledger and ship. Every honest-ship dependent waits on the re-gate.

**deps**: none

**first_prompt**: `/superpowers-process full re-gate Phase 21 impl_review after the CR-01 fix`

**outcome**: Done 2026-09-14, ledger-only (zero commits; .planning gitignored by policy). Fresh re-gate evidence run (six probes, EVIDENCE_OK): check_release PASS (v1.20.0 @ 5b2183c), map TOTAL: 644, rules PASS, generator replay PASS, tag v1.20.0 peels to ffe385a, all WR/CR-01 guard greps hit. 21-IMPL_REVIEW.md re-gated in place (PASS_WITH_NOTES, CR-01/WR-01/02/03 CLOSED with evidence, original preserved below). master_flow transitioned: current_gate gap_analysis, four review gates completed, blocked_by null, regate 2, gap/verify honestly open. REQUIREMENTS MAP-21-05 (required-override wording fix) / REL-21-01 / REL-21-02 ticked; ROADMAP Phase 21 boxes + 2/2 Executed. GitHub Release remains P8's.

## P4 — ci-link-policy-parity

- **id**: P4
- **name**: ci-link-policy-parity
- **size**: M
- **status**: done
- **promoted_ids**: []
- **corroboration**: 3 (value, risk, cohesion)

**problem**: The PR CI link-policy HOSTS regex is a weaker copy of the local release gate: tooling/check_release.py bans cisa.gov, energy.gov, nde-ed.org, and everyspec.com while validate.yml omits those four. A PR can introduce banned source-material URLs, pass GitHub Actions, and only fail later on a human-run local check. Link policy is the licence-compliance mechanism; silent CI/local drift worsens every time one list is extended without the other.

**evidence**:
- .github/workflows/validate.yml:43-45 `HOSTS = re.compile(r"https?://[^\s)\\"']*(sebokwiki|nasa\.gov|ntrs|nist\.gov|"` (ends at dau.edu)
- tooling/check_release.py:54 `SOURCE_HOSTS = re.compile(...|dau\.edu|cisa\.gov|energy\.gov|nde-ed\.org|everyspec\.com)`
- .planning/codebase/CONCERNS.md:14 `The duplication is deliberate (CI must not execute repo code), but nothing verifies the copies stay in sync.`

**in_scope**: make CI and local SOURCE_HOSTS/HOSTS lists identical for current banned hosts; prefer a plain data file both gates read as data, or an explicit parity check that fails on divergence; keep the CI trust boundary (workflow never executes checked-out tooling/*.py).

**out_scope**: leak-sentinel rewrites; third-party CI actions or PyYAML; pack content edits; release-gate CI expansion beyond host-list parity (P5).

**why_now**: Every PR already runs the weaker gate; fix before any CI expansion (P5) re-bakes the weaker link policy.

**deps**: none

**first_prompt**: `/superpowers-process full align CI link-policy host list with check_release SOURCE_HOSTS`

**outcome**: Done 2026-09-14, commits 1e47bb0/f3fff72/e025f79/89464a1/a42e3d9 on main. Spec D5 evidence: kept test `link-policy tests: OK` exit 0; `RELEASE CHECK: PASS`; CI parity probes both directions + missing-file fail-closed exit 1 each. CI enforces from trusted inline 18-token frozenset with parity assert vs `tooling/link-policy-hosts.txt`; local gate loads the data file fail-closed; kept assert script `tooling/test_link_policy.py`. Hosted Actions smoke defers to next push (validate.yml runs on main push). Note: `.planning/codebase` doc sync is on-disk only (`.planning` gitignored by policy); CHANGELOG carries the committed doc surface.

## P5 — ci-local-gate-coverage-gap

- **id**: P5
- **name**: ci-local-gate-coverage-gap
- **size**: M
- **status**: done
- **promoted_ids**: []
- **corroboration**: 2 (risk, cohesion)
- **triage notes (round 2)**: non-critical — corroboration 2 with the value lens absent; risk and cohesion carry it.

**problem**: PR CI mirrors only four shallow checks (leak sentinels, link policy, pack frontmatter, catalog.json parse). The local gate enforces eleven checks including version single-source (now covering the website YAMLs), full pack validation, SKILLS.md count, packs.html freshness, chapter-basename overlap, capability-map freshness, classification-rules completeness, and generator replay. Phases 19-20 map/overlap/classification/replay work is invisible to CI; PRs stay green while the repo is not release-ready.

**evidence**:
- tooling/check_release.py:10-23 eleven-check docstring (check 4 now names the two website YAMLs)
- .github/workflows/validate.yml:24-88 four CI steps only
- .planning/codebase/TESTING.md:80 `docs/packs.html`, `catalog.json`, `SKILLS.md` counts are only caught by `check_release.py`, not by CI

**in_scope**: close the highest-value CI-blind gaps without executing untrusted repo Python (at minimum version trio agreement including website YAMLs, SKILLS.md vs packs count, and map/overlap invariants expressible as inline stdlib or pure data reads); document remaining local-only checks and fail closed if a required local gate is skipped pre-tag; preserve the read-all, no-checkout-code-execution permission posture.

**out_scope**: host-list parity itself (P4); running check_release.py directly in CI; content-quality evals; Phase 21 CONTRACT prose; restoring the deleted tooling/eval pytest suite.

**why_now**: Phases 19-20 put map, classification, overlap, and replay on the local gate only; without CI coverage the next merge drifts those surfaces while Actions stays green. Depends on P4 so expansion does not re-bake the weaker link policy.

**deps**: P4

**first_prompt**: `/superpowers-process full close CI-blind release-gate gaps without executing repo code`

**outcome**: Done 2026-09-14, commits 39a4265/79547ca/4a4e69e/e9c1d12/5b2183c on main. Four inline-stdlib CI steps twinning checks 4+4a/6/8 and the pure-data subset of 9/10; overlap whitelist moved to shared fail-closed tooling/overlap-whitelist.txt; drift control via tooling/test_ci_gate.py (heredoc extraction by pinned step names, 10 negative demos incl. signpost-unmarked index, literal-parity asserts vs check_release/check_capability_map/check_classification_rules); docstring CI-covered vs local-only split; sha-stamped PASS banner `RELEASE CHECK: PASS (v<version> @ <sha>)` with distinct `@ no-git` form. Full validate_pack, packs.html, thresholds/notes, replay stay local-only (documented in workflow header + docstring). Push to origin deferred (origin/main 28 behind; outward publish is user/P8 call); GitHub Actions smoke lands at next push.

## P6 — validate-pack-signpost-parity

- **id**: P6
- **name**: validate-pack-signpost-parity
- **size**: S
- **status**: done
- **promoted_ids**: []
- **corroboration**: 2 (risk, cohesion)
- **triage notes (round 2)**: non-critical — corroboration 2; the value lens killed it as contributor broken-window rather than ship-path value, risk and cohesion carry it.

**problem**: tooling/validate_pack.py `--all` iterates every packs/ dir as a full content pack and requires LICENSE plus chapters/; the two signpost packs intentionally lack both, so the documented standalone command exits 1 on a healthy release-ready tree while check_release (which pre-filters signpost dirs) passes. The two tools disagree on what valid means.

**evidence**:
- tooling/validate_pack.py:117-118 `--all` iterates every packs dir
- tooling/validate_pack.py:67-70 LICENSE/chapters required per pack
- tooling/check_release.py:141 `packs = sorted(p for p in ... if p.is_dir() and p not in signpost_dirs)`
- .planning/codebase/CONCERNS.md:39-40 `Standalone validator exits non-zero on a release-ready repo`

**in_scope**: detect `kind: signpost` in SKILL.md frontmatter inside validate_pack.check_pack / --all; relax LICENSE and chapters/ requirements for signposts only; align documented run commands so --all and check_release agree on a clean tree.

**out_scope**: signpost pack body or citation edits; CI workflow edits (P4/P5); pytest; new pack content rules.

**why_now**: Broken-window validator: the command contributors are told to run already fails on mainline; fix before more automation depends on --all exit codes. Cheap alignment while tooling is open for P4/P5.

**deps**: none

**first_prompt**: `/superpowers-process full teach validate_pack.py the signpost pack kind`

**outcome**: Done 2026-09-14, commits 9f40cc4/35c5e3a on main. check_pack detects `kind: signpost` via check_release's exact regex (SKILL.md read once, errors="ignore"), guards only LICENSE+chapters; --all exits 0 at 65/65 with signposts as plain PASS; kept probe tooling/test_validate_pack.py (7 cases) green; PACK-SPEC sentence added; check_release untouched.

## P7 — map-tooling-residual-harden

- **id**: P7
- **name**: map-tooling-residual-harden
- **size**: M
- **status**: done
- **promoted_ids**: [b-04, b-05]
- **corroboration**: 2 (risk, cohesion)

**problem**: Phase 21 closed the pack/chapter/note path and md-cell guards and folded generator --check into check_release, but three residual holes sit on the same generator, md render, and release-replay flow: cluster_names are neither pipe/CR/LF-validated nor escaped in render_md (WR-01); map-replay feeds the map's own generated_on so rules-vs-map date drift never fails (WR-02); --check compares JSON only so capability-pack-map.md can go stale while all gates stay green (WR-03). One slice closes them together.

**evidence**:
- tooling/generate_capability_map.py:260 unescaped f-string md cell for cluster name
- tooling/generate_capability_map.py:332-339 `--check` compares JSON only
- tooling/check_release.py:284-285 replay feeds the map's own `disk_on`
- .planning/phases/21-contract-rewrite-release-surfaces/21-IMPL_REVIEW.md:76-92 WR-01/WR-02/WR-03 headings

**in_scope**: reject |/CR/LF in cluster_names in generate_map and check_rules and escape names in render_md; cross-check rules generated_on vs live map (or feed the rules date into map-replay); extend --check (or check_release) to compare rendered md to on-disk capability-pack-map.md; keep stdlib-only, no validate.yml repo-Python step.

**out_scope**: website YAML bump (P1 done); version trio / CHANGELOG / tag / gh release; CONTRACT rewrite (done); GAP.md ledger refresh (P8); pack content or new packs; CI changes (P4/P5).

**why_now**: Same files and data flow Phase 21 already owns; residuals leave silent md/date corruption paths beside the new release replay. Close before treating FUT-05 tooling as finished.

**deps**: none

**first_prompt**: `/superpowers-process full close WR-01 WR-02 WR-03 map tooling residuals`

**outcome**: Done 2026-09-14, commits 73adda3/a9bfae4/1b037b4 on main. WR-01: `|`/CR/LF/tab reject set in generate_map + check_rules (exact spec messages), render_md `\|` escape defense-in-depth. WR-02: rules-vs-map generated_on fidelity check in check_rules. WR-03: --check full-text md freshness gate with actionable stale message. Kept probe tooling/test_generate_capability_map.py (probes a-e) green; byte-stable replay preserved; check_release.py zero edits. Note: spec rationale claimed header edits fail the freshness gate; corrected during plan review — gate detects body drift only (header preserved verbatim by design).

## P8 — phase21-planning-ledger-close

- **id**: P8
- **name**: phase21-planning-ledger-close
- **size**: M
- **status**: in-flight
- **promoted_ids**: [b-08]
- **corroboration**: 3 (value, risk, cohesion)

**problem**: Phase 21 product surfaces are at 1.20.0 and CR-01 is fixed, but the shared .planning ledger still advertises planning / Phase 20 stop / Phase 21 not started: STATE status planning and stopped_at Phase 20, ROADMAP overview still map_version 1.19.1 with Phase 21 unchecked, REQUIREMENTS MAP-21-05 / REL-21-01 / REL-21-02 unchecked, master_flow still carries the stale CR-01 needs_work marker, MAP-21-05 still describes optional note overrides while the generator fails closed without them, and GAP.md still frames FUT-05 as unfinished follow-up. An honest milestone close cannot certify a ledger that contradicts the shipped catalogue.

**evidence**:
- .planning/STATE.md:7-8 `"status: planning"` / `"stopped_at: Phase 20 complete, ready to plan Phase 21"`
- .planning/ROADMAP.md:5 `map_version **1.19.1** / 644 entries / 32 clusters`; ROADMAP.md:34 Phase 21 unchecked
- .planning/REQUIREMENTS.md:18,22-23 MAP-21-05 / REL-21-01 / REL-21-02 unchecked
- .planning/phases/21-contract-rewrite-release-surfaces/master_flow_state.json:55 stale `"impl_review": "needs_work:cr_01:..."`
- .planning/GAP.md:1 `Follow-up: Finish FUT-05 byte-stable capability-map generator`
- .planning/phases/21-contract-rewrite-release-surfaces/21-02-SUMMARY.md:148 `phase.complete: tick REL-21-01 / REL-21-02 (and MAP-21-05 from 21-01). When ticking MAP-21-05, fix REQUIREMENTS wording that still says "optional" note overrides`

**in_scope**: tick MAP-21-05 / REL-21-01 / REL-21-02 together and fix the MAP-21-05 optional-to-mandatory overrides wording; update STATE/ROADMAP/MILESTONES/master_flow for Phase 21 complete and v1.20.0 ship posture; record the website YAML fix (P1) and remaining /gsd-ship tail in planning notes; refresh the GAP.md stale FUT-05 follow-up note against the Phase 21 residual (same ledger subsystem, b-08); run /gsd-ship for the v1.20.0 GitHub Release as the payoff step (X1 resolved 2026-09-14: P8 owns ship).

**out_scope**: product code under docs/products, tooling/, or the version trio files; WR-01/02/03 residuals (P7); deferred FUT-04 / IO-05 / IO-06 pack work; CI or validate_pack changes.

**why_now**: Planning pointers disagree with shipped product and block an honest milestone close; CR-01 product truth already landed so the ledger can certify without lying. With X1 resolved to P8, this package is the single Phase 21 close-out: ticks, ledger truth, and the GitHub Release in one honest pass.

**deps**: P3

**first_prompt**: `/superpowers-process full close Phase 21 ledger and ship: tick requirements, refresh STATE/ROADMAP/master_flow/GAP.md, run /gsd-ship`

## Human fork

- **X1 (RESOLVED 2026-09-14 by user ruling: P8 owns /gsd-ship)**: was P3 vs P8 ship-step ownership. Resolution: P8 (phase21-planning-ledger-close) carries the GitHub Release creation as its payoff step after the ledger close; P3 (close-phase21-ship-surface) narrows to the impl_review re-gate and the remaining Phase 21 product gates. The P8-after-P3 ordering holds: P8's honest ticks and ship both depend on P3's cleared gates.

## Dependency order (triage, round 2)

P4, P6, P7, P5, P3, P8

## Backlog

See [backlog.md](../backlog.md). Round 2 delta: b-08 promoted into P8 (GAP.md refresh, same ledger sweep); b-17 dropped (obsolescence — the YAML precondition landed in ffe385a and ship ownership lives solely in X1); b-03 evidence updated (P1 did not touch catalog.json); 14 rows otherwise unchanged. No new ids.
