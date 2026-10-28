# Backlog - jgs-se-knowledge-packs



Created 2026-09-14 by package-loop round 1 (input digest 460acaa9c226881a5467b37f82c92845ea63d0d25eae93999e141a43abf96d72). Groomed 2026-10-08 by package-loop full re-run, 2 rounds (input digest 1eab3cb00e9051b5cafc56c68f33a0a942bf5d3ef35aaa61049d4a91d82e465e): b-11, automotive-packs-1, pack-quality-fixes-1/-2, se-orchestrator-skill-2/-3 promoted into P21/P22/P18/P19/P27/P17; b-13 done (pack-quality-fixes run); se-orchestrator-skill-1 dropped (prior Design disposition); b-12 re-routed needs-info (premise stale: scripts/ holds only configure_repo.sh); b-26/b-27 opened by the P24 oversized split then promoted into P25/P26; b-28..b-31 added needs-info. Groomed by package-loop round 2, full re-run (input digest 7788c2cdde9a730594cf960e526aeec09d422d0fb2017ecad670bf9a29db3b00): b-08 promoted into P8, b-17 dropped, b-03 evidence updated. Groomed 2026-09-15 by package-loop light visual cut (input digest 1199c7861833f155362b1ef98ed7d702d213ab0048c619e2bc29baab5b683158): added b-18..b-25 for rejected visual anti-patterns; no promotion into P9-P14; P8 left frozen; tooling rows b-01..b-16 unchanged. Groomed 2026-09-16 by package-loop light re-run (input digest 3347c22b9ee38b0f0974a13cb3c4aa4d900953d274f918ab3561cb7b9ac746b4): b-03 promoted into P16; b-23 evidence updated (docs/assets images on disk after P9); P8 still frozen. Groomed 2026-10-11 by package-loop full re-run, 1 round (input digest bbb44c491acbcb457423f79895862f2124e493a80bbbfbbb446c73164ae7b55a): source-freshness-watch-2 promoted into P31; source-freshness-watch-1 routed needs-info (killed by all three lenses; IVL advisory-skipped). Groomed 2026-10-13 by package-loop full re-run, round 1 (input digest deefb9e35a58071a900ba6652fce5c3409b343d5c963a8105a6c486b815e2613): growth-registration-watchlist-surface-2 done (both suites green after P30 deleted the five dupes; pack-quality 74/74, ci-gate probe OK). Groomed again at round-2 convergence, same digest: b-28 promoted into P34, b-29 into P33, b-30 across P39/P40/P41, source-watch-calibrate-and-wire-1 into P36, growth-registration-watchlist-surface-1 into P38; b-32 and b-33 added needs-info; se-orchestrator-skill-3 done (grep-verified). Groomed 2026-10-15 by package-loop full re-run, 1 round (input digest 35338db6967e56264c9699fdd67a44c414de18c84068f54463ce3b7271d83b8c): easa-rules-pack-1 promoted into P43, easa-rules-pack-2 into P45, html-self-contain-scan-1 into P46, b-14 into P47, b-32 into P42; space-signpost-1 done (risk lens disproved the plugin.json advisory: check 6b correctly excludes commercial_use:false packs, so 76 entries is the right count); b-34 and b-35 added needs-info. The two mangled med-device rows keep their broken id cells until P44 (superpowers-ledger-hygiene) repairs them. Groomed 2026-10-27 by package-loop full scoped split, 4 cuts (ci-trust/site-gates/growth/doc-truth), one round each (digests in the four 2026-10-27 packages documents): P28/P42 re-promoted (growth), P43/P54/P55/P56 opened (doc-truth), P46/P51/P52/P53 opened (site-gates), P48/P50 opened and P49 conflict-graded under X4 (ci-truth); P45 and P47 routed to backlog (b-43, b-44) and their 2026-10-15 promotions reverted; b-36..b-45 added needs-info. One table for the repository. Rows are never deleted; transitions are status changes. Promotion rule: an item cited by a package's in_scope or evidence becomes `promoted`, keeps its id in that package's `promoted_ids`, and reverts to `open` if the package is later dropped.



| id | title | source | status | evidence |

|----|-------|--------|--------|----------|

| b-01 | Deferred source packs: FUT-04 Army CBA / GP-06 residual, IO-05 Integration, IO-06 Logistics diversity | value+risk kills, round 1 (2026-09-14) | deferred | CHANGELOG.md:35-39; docs/SOURCE-VETTING.md:154; .planning/STATE.md:72-74 |

| b-02 | se-agents consumer refresh (sibling repo, outside this catalogue) | value kill, round 1 (2026-09-14) | deferred | .planning/STATE.md:75 |

| b-03 | catalog.json updated 2026-08-17 vs staged 2026-08-27 metadata drift | value+risk+cohesion kills, round 1 (2026-09-14); promoted 2026-09-16 | promoted | P16 in_scope (catalog live-set parity + metadata); catalog.json:5; RELEASE-INFO.txt:5 |

| b-04 | WR-01 cluster-name pipe/CRLF validation and md escaping | value kill + cohesion P7, round 1 (2026-09-14) | promoted | P7 in_scope; .planning/phases/21-contract-rewrite-release-surfaces/21-IMPL_REVIEW.md:76-80 |

| b-05 | WR-02/WR-03 generated_on cross-check and rendered-md freshness | value kill + cohesion P7, round 1 (2026-09-14) | promoted | P7 in_scope; .planning/phases/21-contract-rewrite-release-surfaces/21-IMPL_REVIEW.md:135 |

| b-06 | Seed .planning/BACKLOG.md (header only, no rows) | value kill, round 1 (2026-09-14) | needs-info | .planning/BACKLOG.md:30 |

| b-07 | Add pytest suite (plans prohibit; verification is release gates) | value+risk kills, round 1 (2026-09-14) | needs-info | .planning/phases/21-contract-rewrite-release-surfaces/21-02-PLAN.md:61 |

| b-08 | GAP.md stale completed-milestone note vs Phase 21 residual | risk kill, round 1 (2026-09-14); promoted round 2 | promoted | P8 in_scope (GAP.md refresh, same ledger sweep as STATE/ROADMAP/MILESTONES/master_flow); .planning/GAP.md:1; .planning/ROADMAP.md:34 |

| b-09 | Restore deleted tooling/eval pytest suite from __pycache__ (speculative) | risk kill, round 1 (2026-09-14) | needs-info | .planning/codebase/TESTING.md:8-9; .planning/phases/21-contract-rewrite-release-surfaces/21-01-PLAN.md:67 |

| b-10 | TODO-sentinel on scaffolded LICENSE/PACK.yaml (no live TODO today) | risk kill, round 1 (2026-09-14) | needs-info | tooling/build_pack.py; packs/**/LICENSE grep empty |

| b-11 | Hardcoded OneDrive paths in build_all_packs.workflow.js | risk kill, round 1 (2026-09-14); promoted 2026-10-08 | done | P21 landed: PACKS derives from the script file, refSkillDir is required, both OneDrive literals removed |

| b-12 | Duplicate root vs scripts/ installers (install.py/sh/ps1) layout cleanup | risk+cohesion kills, round 1 (2026-09-14); re-routed needs-info 2026-10-08 (premise stale: scripts/ holds only configure_repo.sh) | needs-info | tooling/check_release.py:43 REQUIRED_FILES; scripts/configure_repo.sh |

| b-13 | Per-pack content-quality / depth gate | risk kill, round 1 (2026-09-14); done 2026-10-08 by pack-quality-fixes run | done | tooling/check_pack_quality.py + tooling/check_release.py check 16 + CI step "Pack content quality" |

| b-14 | check_release double full-tree read performance | risk kill, round 1 (2026-09-14); promoted 2026-10-15 into P47; reverted needs-info 2026-10-27 (P45/P47 dual-killed by value+risk, routed to backlog b-44) | needs-info | .planning/codebase/CONCERNS.md:61-65; tooling/check_release.py:L966-996; trigger row b-44 |

| b-15 | Entire Phase 21 + ship + tooling WRs as one package (rejected oversized grab) | cohesion kill, round 1 (2026-09-14) | needs-info | .planning/ROADMAP.md:76-93 |

| b-16 | MAP-21-05 tick alone vs REL ticks alone (P8 owns combined tick) | cohesion kill, round 1 (2026-09-14) | needs-info | .planning/phases/21-contract-rewrite-release-surfaces/21-02-SUMMARY.md:148 |

| b-17 | gh release create as standalone package without YAML fix (superseded by X1 fork) | cohesion kill, round 1 (2026-09-14); dropped round 2 | dropped | obsolescence: YAML precondition landed in ffe385a (both website YAMLs 1.20.0, gate block 4a negative-tested); ship ownership lives solely in open fork X1 (P3 vs P8); merged-into P3 rejected because P3's ship claim is the disputed X1 side, not a settled owner; X1 resolved 2026-09-14 to P8 |

| b-18 | Visual-regression CI / Playwright suite for docs HTML | value+risk kills, visual cut 2026-09-15 | needs-info | .planning/codebase/TESTING.md:85; only ad-hoc .playwright-mcp artifacts; not required for image ship |

| b-19 | Publish .playwright-mcp page dumps as public site art | value kill, visual cut 2026-09-15 | dropped | off-kit internal captures; .playwright-mcp/ gitignored; use jgs-image-gen on-brand stills instead |

| b-20 | Reuse sources/*/covers PDF rasters as brand imagery | value kill, visual cut 2026-09-15 | dropped | wrong domain and licence surface for marketing art; sources/ |

| b-21 | Standalone favicon-only package | value kill, visual cut 2026-09-15 | dropped | too small alone; optional fold into P9 og-share-cards asset kit; docs/index.html:15 |

| b-22 | Full packs.html SPA redesign without images | value+cohesion kills, visual cut 2026-09-15 | needs-info | weak image payoff; packs table polish is P14 only if picked; docs/packs.html:5 |

| b-23 | Standalone Git LFS / binary policy with no images on disk yet | risk kill, visual cut 2026-09-15 | needs-info | P9 landed docs/assets/*.png; still no size/clone pain cited; .gitattributes eol-only |

| b-24 | Standalone a11y package for images | risk kill, visual cut 2026-09-15 | dropped | alt text and reduced-motion fold into P10/P11 image insertion, not a separate package |

| b-25 | Merge landing hero stills with dual-page OG meta into one grab | cohesion kill, visual cut 2026-09-15 | dropped | oversized; split is P9 vs P10; docs/index.html:113-124 |

| html-self-contain-scan-1 | ATTR name alternation can match imagesrcset/data-src suffixes (fail-closed over-match) | html-self-contain-scan; promoted 2026-10-15 into P46 | promoted | final review minor; tooling/check_release.py ATTR; P46 in_scope |

| se-orchestrator-skill-1 | Widen /se Agency contexts rows to every same-family pack (today ~6 per family) | se-orchestrator-skill | dropped | prior triage disposition R1 M6 (Design); dropped 2026-10-08 groom, re-propose only with new evidence |

| se-orchestrator-skill-2 | Landing-page /se mention requires a check 13 change first (non-signpost chips add to N) | se-orchestrator-skill; promoted 2026-10-08 | promoted | P27 in_scope; docs/superpowers/specs/2026-09-23-se-orchestrator-skill.md:309 |

| se-orchestrator-skill-3 | Pre-existing drift: website YAML "46 packs" feature title; SKILLS.md header comment names nonexistent tooling/gen_skills_index.py | se-orchestrator-skill; promoted 2026-10-08; done 2026-10-13 (P17 executed; grep-verified: website YAML title reads 68 packs, gen_skills_index claim gone from SKILLS.md:4) | done | P17 in_scope; docs/superpowers/specs/2026-09-23-se-orchestrator-skill.md:314 |

| automotive-packs-1 | Normalize catalog.json string escapes (8 old entries, — vs literal) in a dedicated commit | 2026-09-27-automotive-packs; done 2026-10-08 (obsolescence: catalog.json already single-form) | done | P22 verified no-op: 9 literal em dashes (8 titles + 1 license), zero escaped forms; check 14 + CI parse green |

| automotive-packs-2 | Confirm UNECE R156 document slug at a live (non-403) check; update the signpost row | 2026-09-27-automotive-packs | needs-info | packs/automotive-signpost/SKILL.md R156 row |

| pack-quality-fixes-1 | Kind-detection case sensitivity: validate_pack/check_pack_quality match case-sensitively, check_release.py:338 case-insensitively; align in one commit if ever touched | pack-quality-fixes; promoted 2026-10-08 | promoted | P18 in_scope; tooling/check_pack_quality.py:58-62 vs tooling/check_release.py:338-340 |

| pack-quality-fixes-2 | nasa-se-handbook SKILL.md stale "20 techniques" count (real: 21) at lines 24 and 100 | pack-quality-fixes; promoted into P19; done 2026-10-08 | done | P19 executed (routing skip clause); packs/nasa-se-handbook/SKILL.md:24,100 |

| b-26 | faa-8110-49 full knowledge pack (FAA Order 8110.49, DO-178C software certification guidance; tier 1 public domain); split half of failed P24 cluster | package-loop full 2026-10-08; promoted into P25 | promoted | P25 in_scope; docs/candidate-packs.md:70 |

| b-27 | avionics-signpost (DO-178C / DO-254 / ARP4754A / ARP4761 landing signpost, faa-8110-49 as free path); split half of failed P24 cluster | package-loop full 2026-10-08; promoted into P26 | promoted | P26 in_scope; docs/candidate-packs.md:82 |

| b-28 | med-device-eu full pack (MDCG + MHRA, tier 2/3 vet per document) | value lens round 2, 2026-10-08; promoted 2026-10-13 into P34 | promoted | docs/candidate-packs.md:68; P34 in_scope |

| b-29 | easa-rules full pack (one software/safety volume first, tier 2/3) | value lens round 2, 2026-10-08; promoted 2026-10-13 into P33 | promoted | docs/candidate-packs.md:73; packs/avionics-signpost/SKILL.md:72; P33 in_scope |

| b-30 | rail/space/maritime signpost cluster (split and sequence per domain) | value lens round 2, 2026-10-08; promoted 2026-10-13 across P39/P40/P41 after the round-1 P35 oversized split (one row spans the three signpost packages; closes when P41 lands); done 2026-10-14 (P39/P40/P41 all executed, IVL clean) | done | docs/candidate-packs.md:84-86; P39/P40/P41 in_scope; row 8 carries all three built marks |

| b-31 | telecom-3gpp pack or cheaper signpost first (audience-fit question open) | value lens round 2, 2026-10-08 | needs-info | docs/candidate-packs.md:75 |

| source-freshness-watch-1 | source-watch test suite prints record-mode stdout noise (recorded/FAIL lines) on a passing run; capture or redirect in the record tests | source-freshness-watch; routed needs-info 2026-10-11 (killed by all three lenses: designed print, IVL advisory-skipped, zero catalogue/surface payoff) | needs-info | docs/superpowers/plans/2026-10-11-source-freshness-watch-ivl-triage-log.md Round 1 A1 |

| source-freshness-watch-2 | check_source_watch live-status tolerance accepts null/empty-string status as live; spec coverage rule wording is "live or absent" only (fail-closed direction, unexercised today) | source-freshness-watch; promoted 2026-10-11 | done | P31 in_scope (live-status predicate alignment + probe cases); tooling/check_source_watch.py:142-146; docs/superpowers/plans/2026-10-11-source-freshness-watch-triage-log.md Round 3 A2 |

| growth-registration-watchlist-surface-1 | CONTRIBUTING.md CI-runs-validate_pack.py claim (line 70, was 66) contradicts validate.yml header "CI never executes checked-out repository code"; PACK-SPEC.md:109-110 sides with validate.yml | growth-registration-watchlist-surface; promoted 2026-10-13 into P38 | promoted | CONTRIBUTING.md:70; .github/workflows/validate.yml:26; docs/superpowers/specs/2026-10-12-growth-registration-watchlist-surface.md Non-goals + D-05; P38 in_scope |

| growth-registration-watchlist-surface-2 | tooling/test_pack_quality.py (:142) and test_ci_gate.py (:732) fail on real-tree assertions over packs/ because of the five untracked nasa-se-handbook chapter dupes; dupe-caused, expected green after P30 deletes them (evidence corrected 2026-10-12; earlier VERSION-sentinel attribution wrong: that string is check_source_watch.py:60 probe noise from the passing test_source_watch); done 2026-10-13: P30 deleted the dupes 2026-10-12 and both suites run green on the real tree (pack-quality 74/74, ci-gate probe OK) | growth-registration-watchlist-surface | done | tooling/test_pack_quality.py:142; tooling/test_ci_gate.py:732; docs/superpowers/specs/2026-10-12-nasa-shortname-chapter-dupes.md Codebase context; docs/superpowers/packages/2026-10-11-jgs-se-knowledge-packs-packages.md P30 |

| source-watch-calibrate-and-wire-1 | dod-te-guidebook watchlist row publisher attribution (OUSD R&E, cto.mil) no longer resolves to a hosted copy of the T&E Enterprise Guidebook; recorded 2026-10-13 on cross-pack confirmation (Ruling R1), but monthly runs will keep hitting cto.mil dead paths until the row carries a hint pointing at the surviving publisher home (test-evaluation.osd.mil) | source-watch-calibrate-and-wire; promoted 2026-10-13 into P36 | promoted | docs/source-watchlist.json:301-306 (hint empty); .zcode/source-watch/2026-10-12.md maintainer-resolution addendum (2026-10-13) item 4; P36 in_scope |

| source-watch-calibrate-and-wire-2 | 14 drift findings stand recorded as watchlist bookkeeping (13 from the 2026-10-12 calibration, plus mrl-deskbook V2022 -> V2025 from 2026-10-13): pack content is behind the publisher's observed revisions and no rebuild has been decided (D-04 leaves packs untouched; the watchlist version fields now carry the observed strings) | source-watch-calibrate-and-wire | open | docs/source-watchlist.json version fields on the drift rows (nasa-pra, nasa-risk, sebok, nasa-se-handbook, nist-ssdf, nist-stat-handbook, dod-rio, nasa-schedule, dodaf, federal-bca, faa-ams-vv, mrl-deskbook); .zcode/source-watch/2026-10-12.md drift findings + addendum item 6 |

| b-32 | fhwa-its-se tier-1 candidate pack absent from the numbered build-order table; maintainer ranking decision pending | package-loop full 2026-10-13 (value lens kill routing, round 1); promoted 2026-10-15 into P42 (the pack build carries the ranking question) | done | docs/candidate-packs.md:74 (listed as remaining candidate, not ranked in the numbered table at lines 14-24); P42 in_scope; done 2026-10-28 (P42, candidate-packs row 9). |

| b-33 | Standing-drift blind spot: spot-check the first production catalog_equivalent finding against its source before trusting the predicate | package-loop full 2026-10-13 (risk/cohesion kill routing, round 1); deferred post-pipeline note from source-watch-calibrate-and-wire | needs-info | docs/superpowers/plans/2026-10-12-source-watch-calibrate-and-wire.md:675 (post-pipeline note 2); trigger condition not yet fired |

| easa-rules-pack-1 | Pre-existing website YAML section-06 detail body says "FAA (7)" while the docs/index.html FAA chip counts 8 (chip includes faa-8110-49); invisible to check 4a "N packs" regex | easa-rules-pack; promoted 2026-10-15 into P43 | done | docs/products/website/01-jgs-se-knowledge-packs.yaml detail body (FAA line) vs docs/index.html FAA chip; surfaced by Task 4 implementer 2026-10-13, final review accepted as out-of-scope; P43 in_scope; done 2026-10-27 (P43) |

| easa-rules-pack-2 | check 4a scans a hardcoded two-file tuple of website YAMLs, not a glob; a future third docs/products/website/*.yaml would silently escape the N-packs enforcement | easa-rules-pack; promoted 2026-10-15 into P45; reverted needs-info 2026-10-27 (P45 dual-killed by value+risk: exactly two YAMLs exist, tuple covers both; routed to backlog b-43) | needs-info | tooling/check_release.py:L1026-1028 (two-file tuple); surfaced by ARL spec review round 2 advisory 2026-10-13; trigger row b-43 |

| easa-rules... med-device-eu capture: S6 asset URL embeds a media ID that can change on re-upload; the durable citation is the gov.uk publication page (watchlist/licence citations already use it) | med-device-eu-pack | open | sources/med-device-eu/capture-record.md url row (untracked); Task 1 report note; gitignored capture, so the durable record is this row |

| MDCG PDFs (S1-S5) carry no in-document licence footer; licence basis is the Commission legal-notice page-level grant (Decision 2011/833/EU, CC BY 4.0) plus the in-PDF "not legally binding" disclaimer; monthly watch runs should re-check the endorsed-guidance index for revised editions (S1 is rev.1 June 2025) | med-device-eu-pack | open | sources/med-device-eu/capture-record.md footer rows (FOOTER: silent for S1-S5); docs/source-watchlist.json med-device-eu row |

| uk-defence-next-jsp-pack-1 | jsp-376 chapters carry interior clause-span echoes inside the brief's near-verbatim ceiling (e.g. ch02 DLOD-safety sentence, ch03 CONEMP/CONUSE sentence); a stricter no-near-verbatim rule is a spec change, revisit if a content-quality pass opens | uk-defence-next-jsp-pack | open | packs/jsp-376/chapters/ch02-roles-and-safety-in-the-programme.md and ch03 sentence-level runs vs plan excerpt blocks; SDD final review parked row |

| uk-defence-next-jsp-pack-2 | Generated/derived surfaces (docs/packs.html, capability map, index.html count text) ship with no browser-render check anywhere in the gate story; check_release verifies text and structure only, so a rendering regression would pass every gate | uk-defence-next-jsp-pack | needs-info | tooling/check_release.py check 5c (gen_packs_page pipeline); SDD ruling 2026-10-14 (run transcript): repo-native gate stands in for a Playwright pass, precedent med-device-eu |

| rail-signpost-1 | Fourth+ signpost adds duplicate the count-move checklist by hand (six surfaces + twin lists + cursor + NOTICE); a signpost-add helper or golden-file check would prevent the drift class the plan review caught twice | rail-signpost | needs-info | docs/superpowers/plans/2026-10-14-rail-signpost.md Task 6/7; ARL R1 C1/M1 (hit-count + porcelain expectations needed two fix rounds); run transcript |

| space-signpost-1 | plugin.json skills[] audit claim: an IVL contract pass reported 76 entries vs 79 live dirs (easa-rules, med-device-eu, sebok allegedly absent) while check 6b passes; reconcile the lens parse against the real array once, then close or fix | space-signpost; done 2026-10-15 (false alarm: check 6b excludes commercial_use:false packs, and easa-rules, med-device-eu, sebok all carry commercial_use false in PACK.yaml, so 76 entries is the correct count; verified tooling/check_release.py:1209-1216 against the three PACK.yaml files) | done | .cursor-plugin/plugin.json skills array vs packs/ listing; space-signpost IVL contract advisory (2026-10-14); package-loop full 2026-10-15 risk-lens verification |

| maritime-signpost-1 | bot-gated sources (USCG DCO NVIC/MSC pages, eCFR body) carry research-pass caveats inside the pack Title cells; a future monthly source-watch pass should re-verify those three URLs in a real browser and update the caveat wording if access changed | maritime-signpost | needs-info | packs/maritime-signpost/SKILL.md Title cells (eCFR/NVIC/MSC caveat sentences); research file 2026-10-14 bot-gate records |

| b-34 | Frozen P8 phase21-planning-ledger-close: GitHub Release pending user go; routed here so the frozen in-flight state survives outside the packages document | package-loop full 2026-10-15 (triage routing of the P8 kill, round 1) | needs-info | .planning/STATE.md (stopped_at: GitHub Release pending user go); packages doc carry-forward P8 |

| b-35 | Def Stan 00-051 licence/source status UNVERIFIED; verify per document before any DEF-STAN pack is ranked or built | package-loop full 2026-10-15 (value kill routing, round 1) | needs-info | docs/SOURCE-VETTING.md:198; docs/candidate-packs.md:69 |



| b-36 | X4 signpost counter-gate placement fork: I9 counter-gate inside P48 (risk/cohesion) vs separate P49 (value) | ci-trust triage, scoped split 2026-10-27 | done | Resolved by user default during the 2026-10-27 "until completed" run: folded into P48 (P49 dropped/absorbed); shipped in 6c928d3..bb3468c (validate.yml licence+signpost step, test_ci_gate parity pin) |

| b-37 | I2 ci-local-gate-twin-fork maintainability residual: revisit the inline-heredoc twin doctrine only if parity-pin maintenance cost demonstrably bites | ci-trust triage (value+risk+cohesion kills), 2026-10-27 | needs-info | .zcode/pkg-ci-trust-bundle.md:L2551-2574; tooling/test_ci_gate.py (34KB parity glue) |

| b-38 | Full validate_pack-in-CI blind fork residual: keep local-only unless parser-fork drift controls ever exist (advisory a-06 in 2026-10-26 findings) | ci-trust triage, 2026-10-27 | needs-info | .github/workflows/validate.yml:L26-27; docs/superpowers/reviews/2026-10-26-jgs-se-knowledge-packs-findings.md a-06 |

| b-39 | X5 rider: if the human resolves ATTR grain OUT of P46, the html-self-contain-scan-1 ATTR boundary work needs a home (bounded regex edit + two byte-identical pin updates) | site-gates triage, 2026-10-27 | needs-info | tooling/check_release.py:L157-160; tooling/test_ci_gate.py:L86-88; docs/superpowers/packages/2026-10-27-jgs-se-knowledge-packs-site-gates-packages.md X5 |

| b-40 | gen_packs_page.py and gen_pack_pages.py are live paired generators drifting without a sync note, shared helper, or golden-file check (advisory a-04) | site-gates triage (cohesion kill routing), 2026-10-27 | needs-info | .zcode/pkg-site-gates-bundle.md:L2708; tooling/gen_pack_pages.py vs gen_packs_page.py |

| b-41 | uk-defence JSP tail (912/940/945/816/375/520) unranked in the numbered build order beyond jsp-936; maintainer ranking pending | growth triage (value kill routing), 2026-10-27 | needs-info | docs/candidate-packs.md:L19,L69; b-35 covers the Def Stan verify side |

| b-42 | mit-ocw-se pack build (planned catalog row, CC BY-NC-SA non-commercial) awaits maintainer ranking | growth triage (value kill routing), 2026-10-27 | needs-info | catalog.json planned[]; README planned-pack note; b-32 precedent |

| b-43 | check 4a website-YAML tuple-to-glob deferred until a third docs/products/website/*.yaml exists (ex-P45; carries reverted easa-rules-pack-2) | doc-truth triage (value+risk dual kill), 2026-10-27 | needs-info | tooling/check_release.py:L1026-1028; docs/superpowers/packages/2026-10-27-jgs-se-knowledge-packs-doc-truth-packages.md P45 |

| b-44 | check_release leak/link single-read refactor deferred until the I/O cost actually bites (ex-P47; carries reverted b-14) | doc-truth triage (value+risk dual kill), 2026-10-27 | needs-info | tooling/check_release.py:L966-996; docs/superpowers/packages/2026-10-27-jgs-se-knowledge-packs-doc-truth-packages.md P47 |

| b-45 | X3 rider: side-B stale-token assertion on check 4a (fail on "FAA (7)") runs inside P43 only if the human picks side B; drops entirely on side A | doc-truth triage, 2026-10-27 | needs-info | docs/superpowers/packages/2026-10-27-jgs-se-knowledge-packs-doc-truth-packages.md open_objections X3 |
