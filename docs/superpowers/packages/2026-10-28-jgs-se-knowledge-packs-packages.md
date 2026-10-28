---
date: 2026-10-28
project: jgs-se-knowledge-packs
mode: light
rounds: 1
input_digest: de55ef14804318932f28783a8d83c20fac816cf82ea2cd8ab90b63682f7021ca
open_objections: []
---

# Packages: jgs-se-knowledge-packs, 2026-10-28 (light re-run, groom)

Re-run after the four 2026-10-27 scoped cuts all reached done. Wave: value 3, risk 1, cohesion 0. Merge unioned to four packages, no conflicts; triage zero_critical true. Order below is execution order.

## P57 - uk-defence-jsp-912-pack

- **id**: P57; **name**: uk-defence-jsp-912-pack; **size**: L; **status**: proposed; **corroboration**: 1 (value); **deps**: none; **promoted_ids**: [b-41]
- **problem**: UK defence growth path open after jsp-815/376/936. The 2026-10-14 research gate ranked JSP 912 (Human Factors Integration in defence systems, Parts 1+2, V3.0 Mar 2024, OGL v3, two free gov.uk PDFs ~16pp + ~65pp) next after 936, but candidate-packs row 4 still shows the family partially built and the 2026-10-28 remaining-work sentence lumps 912 into the "unranked remainder".
- **evidence**: docs/candidate-packs.md:L19 (row 4 partially built), :L26 (unranked-remainder sentence names JSP 912); docs/superpowers/research/2026-10-14-uk-defence-next-jsp-pack-research.md:L79 (rank order), :L17 (912 source row: OGL v3, page footer licence, two free PDFs).
- **in_scope**: pin and vet JSP 912 Parts 1+2 on gov.uk (OGL v3); build packs/jsp-912 per docs/PACK-SPEC.md (multi-part precedent: jsp-815; decide one-pack-two-parts per the research note "fits one pack if both parts in scope"); full D6 registration identical to jsp-936/fhwa-its-se (counts 73→74, 82→83, map 735→735+N, `updated` frozen, no Licences-row change needed since OGL row already carries the family cell pattern); candidate-packs row 4 update + drop JSP 912 from the unranked-remainder sentence in the same run.
- **out_scope**: JSP 940/945/816/375/520; DEF-STANs and b-35 verify side; telecom-3gpp; nasa-risk/faa-ams-vv drift rebuilds (P58/P59); CI/gate work; version bump.
- **why_now**: research already names 912; the registration path is proven twice over (P28, P42); row 4 is the last partially-built family.
- **triage notes**: PASS, size L. Two-PDF sizing settled by research doc L17 ("fits one pack if both parts in scope") plus jsp-815 multi-file precedent. The run must also rewrite candidate-packs.md:L26 so the unranked remainder stops naming JSP 912 (rank already exists at research L79) — same run, not a fork.
- **first_prompt**: `/superpowers-process full build jsp-912 pack and resolve its candidate-packs row`

## P58 - rebuild-nasa-risk-handbook-v2

- **id**: P58; **name**: rebuild-nasa-risk-handbook-v2; **size**: M; **status**: proposed; **corroboration**: 1 (value); **deps**: none; **promoted_ids**: []
- **problem**: packs/nasa-risk pins v1.0 (November 2011); source-watch recorded the publisher's V2.0 (Nov 2024, SP-20240014019/14326) superseding it, and SOURCE-FRESHNESS.md leaves the rebuild as a maintainer decision. The pack is now two major versions behind on a high-traffic NASA SE reference.
- **evidence**: packs/nasa-risk/PACK.yaml:L1-4 (v1.0 November 2011); .zcode/source-watch/2026-10-12.md:L15-16 (V2.0 finding on the nasa-risk row); docs/superpowers/backlog.md:L101 (source-watch-calibrate-and-wire-2 open: 14 drift rows, rebuilds undecided); docs/SOURCE-FRESHNESS.md:L35-40.
- **in_scope**: confirm the V2.0 primary pin (SP-20240014019/14326; tier-1 public domain); rebuild packs/nasa-risk chapters + SKILL.md + PACK.yaml + LICENSE to V2.0; refresh every version-bearing registration surface (catalog row, watchlist `--record`, NOTICE if wording changes); close or shrink this slug's drift row on source-watch-calibrate-and-wire-2.
- **out_scope**: nasa-pra blind rebuild (SP-2011-3421 is a different document; the calibration row may conflate the two — verify, don't assume); the other 12 drift rows; CI/gate work; version bump.
- **why_now**: highest-traffic open drift; discovery already done by the calibration run; rebuild restores the trusted-current claim.
- **triage notes**: PASS, size M. Watchlist row is nasa-risk only; the sibling nasa-pra drift row stays explicitly out of scope.
- **first_prompt**: `/superpowers-process full rebuild nasa-risk pack to handbook V2.0`

## P59 - rebuild-faa-ams-vv-v4

- **id**: P59; **name**: rebuild-faa-ams-vv-v4; **size**: M; **status**: proposed; **corroboration**: 1 (value); **deps**: none; **promoted_ids**: []
- **problem**: packs/faa-ams-vv ships AMS Lifecycle V&V Guidelines v3.0 (April 2017); the FAA published 4.0 (January 2023), recorded by source-watch. README positions the catalogue as trusted-current; this live FAA pack is a major version behind.
- **evidence**: packs/faa-ams-vv/PACK.yaml:L1-4 (Version 3.0 April 2017); .zcode/source-watch/2026-10-12.md:L25 (4.0 2023 observed); README.md:L17-20.
- **in_scope**: pin FAA AMS Lifecycle V&V Guidelines 4.0 as primary source (tier-1 public domain); rebuild packs/faa-ams-vv to 4.0 with full PACK-SPEC surfaces; update catalog/watchlist/version-bearing rows; close the faa-ams-vv drift row.
- **out_scope**: other FAA packs; nasa-risk rebuild (P58); mrl-deskbook and standing-drift rows; CI/gate work; website family inventory (P43 done).
- **why_now**: clean major-version supersede on a live pack; discovery done; carries the CMMI-v1.2 paraphrase-only caution in PACK.yaml notes forward into the rebuild.
- **triage notes**: PASS, size M.
- **first_prompt**: `/superpowers-process full rebuild faa-ams-vv pack to guidelines 4.0`

## P60 - cursor-plugin-ssot-gates

- **id**: P60; **name**: cursor-plugin-ssot-gates; **size**: M; **status**: proposed; **corroboration**: 1 (risk); **deps**: none; **promoted_ids**: []
- **problem**: `.cursor-plugin/plugin.json` is a live install surface outside both version single-source and CI: its `version` is 1.22.0 while RELEASE-INFO, CHANGELOG, and `.claude-plugin/plugin.json` carry 1.22.1; `tooling/check_release.py:L1167` and the validate.yml version-SSOT heredoc read only the claude manifest; check 6b (Cursor skills list, `check_release.py:L1363-1365`) runs local-only. A tag or marketplace publish can ship a stale Cursor version and uncaught skill-list drift under green CI.
- **evidence**: .cursor-plugin/plugin.json:L5 (`"version": "1.22.0"`); .claude-plugin/plugin.json:L4 (`"version": "1.22.1"`); RELEASE-INFO.txt:L3 (`Version: 1.22.1`); tooling/check_release.py:L1167; .github/workflows/validate.yml:L1183-1187; tooling/check_release.py:L1363-1365.
- **in_scope**: bump `.cursor-plugin/plugin.json` to 1.22.1; extend the version SSOT (check_release.py, validate.yml heredoc, test_ci_gate parity pin) to cover the cursor manifest; mirror check 6b into the CI pure-data twin with a parity pin; document the pre-tag local-check path in the release runbook.
- **out_scope**: full validate_pack-in-CI (b-38); CI twin rewrite (b-37); gen_packs_page probe (b-40); visual suite (b-18); commercial_use:false policy changes; product version bump.
- **why_now**: Cursor is a live install surface; the stale version ships under green CI until the SSOT extends.
- **triage notes**: PASS, size M. All four loci verified by triage against current bytes.
- **first_prompt**: `/superpowers-process full extend version and skill-list SSOT gates to the cursor plugin manifest`

## Execution order

P57 → P58 → P59 → P60 (no deps; triage order). Each is one `/superpowers-process full` run.
