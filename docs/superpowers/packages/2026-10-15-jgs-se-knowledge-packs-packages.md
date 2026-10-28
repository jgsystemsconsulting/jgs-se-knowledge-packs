---
date: 2026-10-15
project: jgs-se-knowledge-packs
mode: full
rounds: 1
input_digest: 35338db6967e56264c9699fdd67a44c414de18c84068f54463ce3b7271d83b8c
open_objections: []
---

# Work packages - jgs-se-knowledge-packs (2026-10-15, full re-run)

Context: the 2026-10-13 cut (P33, P34, P28-second, P39, P40, P41, P36, P38, P37) fully executed 2026-10-14; all nine EXECUTED records are on disk and the release gate reads RELEASE CHECK: PASS (v1.22.1 @ bb90288). The catalogue stands at 80 pack directories (71 content packs, 8 signposts, 1 orchestrator), branch packages-2026-10-12 is 84 commits ahead of main and origin/main. This cut converged in one round (value 3, risk 3, cohesion 5 candidates; merge produced 7 packages; triage zero_critical). Two scope contradictions survived merge as human forks X1 and X2 (open-fork list below). Run deviation: pkg-merge and pkg-triage ran in general-purpose carriers carrying their role and JSON contracts verbatim, because the cached GLM pin (builtin:zai-coding-plan) was unspawnable in this session; the pin is fixed on disk (model-profiles.json, account:zai-individual-coding-plan) for future chats.

## Carry-forward status

| id | name | status |
|----|------|--------|
| P1-P27, P29-P32, P33, P34, P36-P41 | prior cuts | done |
| P28 | uk-defence-next-jsp-pack (jsp-376) | done (2026-10-14); id reused below for the JSP 936 package |
| P8 | phase21-planning-ledger-close | in-flight (frozen; GitHub Release pending user go) |

## P28 - uk-defence-jsp-936-pack

- **id**: P28; **name**: uk-defence-jsp-936-pack; **size**: L; **status**: proposed; **corroboration**: 1 (value); **deps**: none; **promoted_ids**: []
- **problem**: Build-order row 4 is still the only unfinished ranked full-pack line: jsp-815 and jsp-376 shipped, but candidate-packs still marks the uk-defence family partially built with other JSPs pending, and the intake surface states the remaining full-pack work on the list is that unfinished family. The 2026-10-14 research gate already ranked JSP 936 Part 1 (Dependable AI in Defence, OGL v3, single ~41-page directive) as the first alternate after the chosen second pack (376), so the next family member is named, licence-cleared at page level, and absent from packs/ and /se routing.
- **evidence**: docs/candidate-packs.md:19 ("| 4 | `uk-defence` family (JSP series first) | full | partially built 2026-10-14 (jsp-815 and jsp-376 done, other JSPs and DEF-STANs pending). OGL-licensed, no open competitor, and UK sourcing matches the consultancy's identity |"); docs/candidate-packs.md:25 ("The remaining full-pack work on this list is the unfinished part of the uk-defence family."); docs/superpowers/research/2026-10-14-uk-defence-next-jsp-pack-research.md:9 (ranked alternates: JSP 936 Part 1 first, JSP 912 second); packs/se/SKILL.md:117 (Defence safety management row routes jsp-815, jsp-376 only); docs/candidate-packs.md:69 ("Built 2026-10-14 (jsp-815 and jsp-376)").
- **in_scope**: per-document OGL v3 vet of JSP 936 Part 1 (Dependable AI in Defence V1.1) on gov.uk; build packs/jsp-936 per PACK-SPEC (SKILL.md, PACK.yaml, LICENSE with OGL text, chapters, cheatsheet/glossary as source allows); register on every live gate surface (SKILLS.md, /se UK family routing, capability map, catalog.json, source-watchlist row, NOTICE attribution); update candidate-packs row 4 / uk-defence bullet for the jsp-936 slug only; gates green.
- **out_scope**: JSP 912/940/945/816/375/520 and DEF-STANs; jsp-815 or jsp-376 rework; paywalled third-party standard clause reproduction; version bump / GitHub Release / frozen P8.
- **why_now**: only remaining ranked full-pack gap on the intake build order; research already named 936 as the next OGL member after 376, and prior JSP packs proved the registration mechanics, so this is the highest-payoff growth step before unranked sectors open.
- **first_prompt**: `/superpowers-process full build jsp-936 Dependable AI in Defence pack under OGL and register it`

## P42 - fhwa-its-se-pack

- **id**: P42; **name**: fhwa-its-se-pack; **size**: L; **status**: proposed; **corroboration**: 1 (value); **deps**: none; **promoted_ids**: [b-32]
- **problem**: fhwa-its-se is the only remaining named full pack in candidate-packs Proposed packs that is tier 1 public domain, scored FULL for civil infrastructure, and still has no packs/ folder (80 pack directories on disk, none named fhwa). The expansion axes call out civil infrastructure as a sector the current US-federal core cannot reach with ITS SE-shaped content, yet the pack was never placed on the numbered build-order table (backlog b-32 needs-info on ranking only).
- **evidence**: docs/candidate-packs.md:74 ("`fhwa-its-se` (tier 1). FHWA/USDOT systems-engineering guidance for intelligent transportation systems. Public domain, extends the catalogue into civil infrastructure with genuinely SE-shaped content rather than construction codes."); docs/candidate-packs.md:51 ("| Civil infrastructure | FHWA guidance incl. ITS systems-engineering material, FEMA docs | US public domain | FULL |"); docs/candidate-packs.md:31 (expansion axes name civil infrastructure); docs/superpowers/backlog.md b-32 (ranking decision pending); bundle survey ("pack dirs total: 80", no fhwa dir).
- **in_scope**: select and pin one FHWA/USDOT ITS systems-engineering primary source set (public domain); build packs/fhwa-its-se per PACK-SPEC with tier 1 licence statement; full registration (catalog.json, source-watchlist, SKILLS.md, /se routing, capability map); mark the candidate-packs fhwa bullet built and add a numbered build-order row if the maintainer wants the ranking recorded; gates green.
- **out_scope**: construction codes / non-SE FHWA material dumps; FEMA-only packs; telecom-3gpp; UK defence JSPs; version bump.
- **why_now**: opens the last named tier-1 FULL sector still missing a pack folder once the ranked uk-defence work is no longer the only growth story; needs no new tooling and is independent of the UK line.
- **first_prompt**: `/superpowers-process full build fhwa-its-se pack from FHWA ITS systems-engineering guidance and register it`

## P43 - website-faa-family-inventory-sync

- **id**: P43; **name**: website-faa-family-inventory-sync; **size**: M; **status**: proposed; **corroboration**: 3 (value, risk, cohesion); **deps**: none; **promoted_ids**: [easa-rules-pack-1]; **open fork**: X1 (see Human forks)
- **problem**: the published website product YAML section-06 family detail body is stale and gate-invisible: it teaches "FAA (7)" plus a separate "FAA airborne software and AEH approval (1)" line while docs/index.html's FAA chip reads "FAA · 8" (includes faa-8110-49), and the freeform family bullets omit easa-rules and med-device-eu, so the named family packs undersum the live catalogue. check 4a only regex-matches "N packs" integers against the live inventory, so RELEASE CHECK stays green while the public family inventory drifts under every growth wave.
- **evidence**: docs/products/website/01-jgs-se-knowledge-packs.yaml:57-59 ("FAA (7): RMA Handbook, Systems Engineering Manual, System Safety, Human Factors Design Std, AMS V&V, Requirements Engineering Management, STD-025 interface documentation."); docs/products/website/01-jgs-se-knowledge-packs.yaml:68 ("FAA airborne software and AEH approval (1): Order 8110.49A and ACs 20-115D, 20-152A, 00-69."); docs/index.html:194 (FAA · 8 chip); tooling/check_release.py:1037-1041 (pack-count regex checks only "N packs" integers); docs/superpowers/backlog.md easa-rules-pack-1 (open).
- **in_scope**: rewrite the website YAML FAA family count/list so it matches the live eight-pack FAA set (fold faa-8110-49 in, or equivalent honest wording); reconcile the section-06 family detail body with live packs/ and docs/index.html chips (add easa-rules and med-device-eu, re-sum families to 71); grep other product/prose surfaces and publisher chips for residual "FAA (7)" claims or the same split pattern; resolve fork X1 (either leave check 4a enforcement as-is with an optional comment, or add the stale-token assertion); promote/close easa-rules-pack-1; confirm check_release still PASS.
- **out_scope**: building or rebuilding pack content; changing live pack count N or signpost M; the check 4a tuple/glob question (P45); index.html redesign; SKILLS.md, catalog.json, version bump, GitHub Release; Playwright/browser-render gate.
- **why_now**: the release gate already passes while the public family inventory is wrong; the next growth pack bumps only the gated N-packs title again and deepens the mismatch unless the detail body is fixed first.
- **first_prompt**: `/superpowers-process full sync website YAML section-06 family inventory with the live FAA-8 catalogue`

## P44 - superpowers-ledger-hygiene

- **id**: P44; **name**: superpowers-ledger-hygiene; **size**: S; **status**: proposed; **corroboration**: 2 (risk, cohesion); **deps**: none; **promoted_ids**: []; **open fork**: X2 (see Human forks)
- **problem**: two package-loop ledger artifacts from the completed 2026-10-13/14 wave are corrupted on disk. The 2026-10-13 packages document's P36 status line is splice-corrupted (done text interrupted mid-word by a second full id/status stub). The backlog table has two open rows whose id cells were mangled into title prose ("easa-rules... med-device-eu capture: ..." and a bare "MDCG PDFs (S1-S5)..." title with no id), so groom, promoted_ids, and status transitions cannot key them.
- **evidence**: docs/superpowers/packages/2026-10-13-jgs-se-knowledge-packs-packages.md:84 (splice-corrupted P36 line); docs/superpowers/backlog.md:56-57 (the two mangled rows); docs/superpowers/backlog.md header (promotion rule keys on the id column).
- **in_scope**: rewrite the P36 status line to a single clean done status (per fork X2); assign stable backlog ids and restore the id|title columns for the two mangled med-device-eu-pack rows without changing their substance; grep the backlog for any other id-less or splice-fused rows and fix them the same way; leave row statuses open/needs-info as appropriate after id repair.
- **out_scope**: acting on the med-device-eu capture/licence substance of those rows; rebuilding med-device-eu pack content; promoting unrelated open backlog rows; re-opening done P36/P33/P34 work; editing packs/, check_release, or capture-record content; P8 / STATE.md ship.
- **why_now**: this cut's candidate space is defined as backlog open/needs-info rows; two open rows are unaddressable by id and a done package line mis-states status, so every later groom and promotion pass mis-counts or re-mints them until the ledger is repaired.
- **first_prompt**: `/superpowers-process full repair the corrupted package-loop ledger lines (P36 status splice and mangled backlog ids)`

## P45 - website-yaml-check-glob

- **id**: P45; **name**: website-yaml-check-glob; **size**: S; **status**: proposed; **corroboration**: 1 (cohesion); **deps**: none; **promoted_ids**: [easa-rules-pack-2]
- **problem**: check 4a hardcodes a two-file tuple of website product YAMLs; version and "N packs" enforcement cover only those two paths, so a future third docs/products/website/*.yaml would silently escape both checks.
- **evidence**: tooling/check_release.py:1013-1027 (comment names "the two website product YAMLs"; website_yamls two-file tuple); docs/superpowers/backlog.md easa-rules-pack-2 (open, surfaced by ARL spec review round 2 advisory 2026-10-13).
- **in_scope**: replace the hardcoded two-file website_yamls tuple with a directory-scoped discovery of docs/products/website/*.yaml (or equivalent explicit enumeration that fails closed on extras); keep version + N-packs scans on every discovered website YAML; update any CI-twin/docs comment that still says "exactly these two paths"; promote/close easa-rules-pack-2.
- **out_scope**: FAA (7) vs (8) prose fix (P43); ATTR regex / html-assets changes (P46); leak/link full-tree read merge (P47); adding new website YAML product files.
- **why_now**: isolated gate-scope fix on the website-YAML check path; independent of the FAA content sync and of the other check_release subsystems, which stay their own packages.
- **first_prompt**: `/superpowers-process full convert check 4a website YAML tuple to directory-scoped discovery`

## P46 - html-attr-name-boundary

- **id**: P46; **name**: html-attr-name-boundary; **size**: S; **status**: proposed; **corroboration**: 1 (cohesion); **deps**: none; **promoted_ids**: [html-self-contain-scan-1]
- **problem**: the html-assets ATTR regex alternates bare attribute names (href|src|data|srcset|...) without name boundaries, so a longer attribute whose suffix matches a short name (imagesrcset, data-src) can be treated as an asset attribute. The scan is shared by check_release and the CI twin that pins ATTR pattern text byte-identically.
- **evidence**: tooling/check_release.py:157-160 (ATTR regex); tooling/check_release.py:177-182 (scan_html_external_assets docstring on byte-identical pinning with the CI twin); tooling/test_ci_gate.py:86-88 (ATTR name groups pin); docs/superpowers/backlog.md html-self-contain-scan-1 (open).
- **in_scope**: tighten ATTR name matching so only whole attribute names match (boundary/non-name char guards); keep check_release ATTR and test_ci_gate ATTR pattern pins byte-identical; add or adjust the twin's ATTR name-group assertion for the suffix cases; promote/close html-self-contain-scan-1.
- **out_scope**: website YAML tuple/glob (P45); leak/link single-pass read (P47); docs HTML content edits; expanding FIRST_PARTY_HOSTS.
- **why_now**: self-contained html-assets subsystem fix with no dependency on the other check_release open rows; should land alone so the twin pin stays reviewable.
- **first_prompt**: `/superpowers-process full bound the ATTR attribute-name regex against suffix over-match with the CI twin pin`

## P47 - check-release-single-read

- **id**: P47; **name**: check-release-single-read; **size**: S; **status**: proposed; **corroboration**: 1 (cohesion); **deps**: none; **promoted_ids**: [b-14]
- **problem**: check_release builds one text_files list then runs the leak sentinels and the source-link scan as two separate loops, each calling read_text on every text file. CONCERNS already names the double-read and the fix (read once, run both checks per body); the live loops still double-read the same list.
- **evidence**: tooling/check_release.py:966-975 (text_files list + leak loop); tooling/check_release.py:992-999 (links loop re-reads every file); .planning/codebase/CONCERNS.md:61-65 (double-read concern and improvement path); docs/superpowers/backlog.md b-14 (open).
- **in_scope**: collapse the leak + link full-tree loops to one read per text file (signpost skip still applies to links only); refresh the CONCERNS.md line cites for the new locus; promote/close b-14.
- **out_scope**: ATTR/html-assets changes (P46); website YAML discovery changes (P45); changing the leak sentinel set or banned-host policy; CI workflow rewrite.
- **why_now**: independent I/O-path cleanup inside check_release; keeping it separate from the html-assets and 4a packages means each gate subsystem stays a single review unit.
- **first_prompt**: `/superpowers-process full collapse check_release leak and link scans to a single read per file`

## Dependency order (triage, round 1)

No dependency edges; all seven packages are independent. Triage order: P44, P45, P46, P47 (four small repairs first, each a single gate or ledger subsystem), then P43 (needs the X1 fork answered), then P28 and P42 (the two L growth packs, runnable in either order).

## Human forks

- **X1** (P43): value out_scope keeps check 4a unchanged beyond an optional comment; risk in_scope extends check 4a (or a sibling assertion) so family-count drift cannot pass silently. Choose one: (A) content-only family inventory sync with check 4a left as-is, or (B) the same content sync plus a hard assertion that fails on known stale tokens such as "FAA (7)". Unresolved at the proposal stop.
- **X2** (P44): risk out_scope excludes touching the historical P36 status-line splice; cohesion in_scope rewrites it. Choose one: (A) backlog-id repair only, leave the 2026-10-13 document untouched, or (B) full ledger hygiene including the P36 line rewrite. Unresolved at the proposal stop.

Unchanged from the prior cut, plus branch state: packages-2026-10-12 is 84 commits ahead of main and origin/main (merge/push decision is the maintainer's). P8 phase21-planning-ledger-close stays frozen in-flight (STATE.md: GitHub Release pending user go; routed to the backlog as b-34 so the frozen state survives outside this document). The 14 recorded drift findings stay bookkeeping-only (source-watch-calibrate-and-wire-2 open); rebuild decisions are maintainer calls under D-04. The monthly watch cron exists outside the repo and is orchestrator-owned.

## Backlog

See [backlog.md](../backlog.md). Delta: promoted easa-rules-pack-1 into P43, easa-rules-pack-2 into P45, html-self-contain-scan-1 into P46, b-14 into P47, b-32 into P42; closed space-signpost-1 as done (risk lens disproved the advisory: check 6b excludes commercial_use:false packs, so 76 plugin entries is the correct count); added b-34 (frozen P8 tracker note) and b-35 (Def Stan 00-051 licence verification) both needs-info. Unchanged: b-01, b-02, b-06, b-07, b-09, b-10, b-12, b-15, b-16, b-18, b-22, b-23, b-31, b-33, automotive-packs-2, source-freshness-watch-1, source-watch-calibrate-and-wire-2, uk-defence-next-jsp-pack-1/-2, rail-signpost-1, maritime-signpost-1, and the two mangled med-device rows (P44 owns the id repair).
