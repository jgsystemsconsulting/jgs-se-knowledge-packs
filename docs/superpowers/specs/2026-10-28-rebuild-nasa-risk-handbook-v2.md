# rebuild-nasa-risk-handbook-v2

Package P58. Rebuild `packs/nasa-risk` from NASA Risk Management Handbook Version 2.0 (November 2024). The live pack pins v1.0, NASA/SP-2011-3422, November 2011. Part 1 of the new set states that it supersedes that document. `nasa-pra` stays on NASA/SP-2011-3421. That is a different document. This cut does not touch it.

## Research

Live pin, fetched 2026-10-28. Both NTRS citation APIs HTTP 200 JSON. Both PDFs HTTP 200, `%PDF-1.7`.

research: https://ntrs.nasa.gov/citations/20240014019
research: https://ntrs.nasa.gov/api/citations/20240014019/downloads/SP-20240014019.pdf
research: https://ntrs.nasa.gov/citations/20240014326
research: https://ntrs.nasa.gov/api/citations/20240014326/downloads/SP-20240014326.pdf

| Volume | Title (NTRS, exact) | Report number | PDF | Bytes | Pages | Cover date |
|---|---|---|---|---|---|---|
| Part 1 | NASA Risk Management Handbook: Version 2.0, Part 1 | NASA/SP-20240014019 | download URL above | 14,471,540 | 303 | Version 2.0, November 2024 |
| Part 2 | NASA Risk Management Handbook: Version 2.0, Part 2 | NASA/SP-20240014326 | download URL above | 6,669,330 | 89 | Version 2.0, November 2024 |

Cover subtitles, not the NTRS title strings: Part 1 "Guidance for an Integrated Framework of Risk Leadership and Management Across the NASA Organization: Concepts and Principles". Part 2 "Guidance for an Integrated Framework of Risk Leadership and Management Across the NASA Organization: Application Examples".

Supersession, quoted from the PDF verso pages, not from the watch report:

- Part 1 page 2: "NASA SP-20240014019 Version 2 supersedes NASA SP-2011-3422 Version 1 dated November 2011."
- Part 2 page 2: "NASA SP-202400114326 and NASA SP-20240014019 supersede NASA SP-2011-3422 dated November 2011." The `114326` token is a typo on the verso. NTRS `otherReportNumbers` and the cover both read NASA/SP-20240014326. Pin the NTRS number. Do not copy the typo into `PACK.yaml`.

NTRS `related` on 20240014019: id 20120000033, type `SUPERSEDES`, title "NASA Risk Management Handbook" (the 2011 handbook); id 20240014326, type `SEE_ALSO`, title "NASA Risk Management Handbook: Version 2.0, Part 2". Publication date on both records: 2024-11-01. Distribution `PUBLIC`. `downloadsAvailable` true. Export control ITAR/EAR `NO`.

Copyright determination, API field, not a PDF legend. Neither PDF prints "public domain" or "17 U.S.C." in the front matter. NTRS `copyright` on 20240014019: `determinationType` `PUBLIC_USE_PERMITTED`, `containsThirdPartyMaterial` false, `belongsToPublisher` false, `belongsToContractor` false, `belongsToAuthors` false. `belongsToUsGov` is also false on this record. That flag is not a copyright claim. NASA special publications are US Government works. The existing pack already classifies SP-2011-3422 as public domain under 17 U.S.C. 105, and V2.0 is the same publisher class. Keep tier 1. Do not invent a copyright legend the PDF does not print.

Part 1 contents (page iv), top-level only. Subsections stay inside the parent chapter. Appendices are not chapters.

1. Introduction
2. Objectives-Driven Risk Management Framework Foundations and Key Elements
3. Risk Models, Analysis, and Decision Concepts
4. Risk-Informed Decision Making
5. Continuous Risk Management
6. Organizational and Managerial Aspects of Objectives-Driven Risk Management
7. Definitions

Appendices A through I (roadmap, leading indicators, technical considerations, aggregate risk, stepwise recap, technical-basis content guide, risk-informed selection report, performance-measure margins, taxonomies). Fold defined terms from chapter 7 and the acronym list into `glossary.md`. Do not write a chapter whose only job is the definitions list.

Part 2 contents (page iv), top-level only. Worked examples, not a second doctrine.

1. Introduction
2. Risk Process Selection and Applicability
3. Example of Activity-Planning RIDM Execution
4. Examples of CRM Execution

No appendix in Part 2. No chapter 5.

Distinction from `nasa-pra`, verified against the live catalog and `packs/nasa-pra/PACK.yaml`, not assumed from the watch row. `nasa-pra` pins NASA PRA Procedures Guide, 2nd ed., NASA/SP-2011-3421, December 2011, 8 chapters. `nasa-risk` pins NASA Risk Management Handbook, NASA/SP-2011-3422, v1.0 November 2011, 10 chapters. Adjacent SP numbers. Different titles, different dates, different contents. The 2026-10-12 watch report line 15 attached the V2.0 handbook finding to the `nasa-pra` row. That attachment is wrong. SP-2011-3421 is not the document Part 1 says it supersedes. SP-2011-3422 is.

## Codebase context

Post-P57 baseline, read 2026-10-28 on main after `jsp-912`: `catalog.json` `packs` 74, `docs/source-watchlist.json` `sources` 74, `docs/classification-rules.json` `assignments` 744, `SKILLS.md` line 9 "74 packs (+8 signposts, +1 orchestrator)". `catalog.json` `updated` is `2026-10-14`. `docs/classification-rules.json` `generated_on` and `docs/capability-pack-map-note-overrides.json` `generated_on` are `2026-10-28`. `map_version` on both is `1.22.0`.

`packs/nasa-risk/` today: `PACK.yaml` (v1.0 November 2011, `source_pages: 256`, `chapters: 10`, `built_on: 2026-06-19`), `SKILL.md`, `LICENSE`, `glossary.md`, `cheatsheet.md`, `patterns.md`, and 10 chapter files under `chapters/`. Support files are not chapters. The checker requires one `is_support: false` row per `packs/<slug>/chapters/*.md` and rejects an assignment whose chapter file is gone (`tooling/check_classification_rules.py` coverage errors). Overrides are a parallel list, same `(pack, chapter)` keys, one `note` string each. `tooling/generate_capability_map.py` refuses any notes length other than 744 (lines 9, 195, 203, 204). There is no removal API. A rebuild deletes the old `nasa-risk` rows from both JSON files and appends the new ones. Key sets must match after the edit. `generated_on` on both files moves to the execution date or the fidelity check fails. `map_version` stays `1.22.0`.

`nasa-risk` assignment rows today: 10 chapter rows plus 3 support rows (`glossary.md`, `cheatsheet.md`, `patterns.md`), all cluster `Risk Management`. Cluster name already exists. Do not invent one.

Watchlist today, both rows, `last_checked` 2026-10-12:

- `nasa-risk` `document` is still `v1.0 (November 2011)`. `version` already carries the observed V2.0 string from the calibration record. `document` is what the pack was built from. `version` is what the watch last saw.
- `nasa-pra` `document` is `Second Edition (December 2011)`. Its `version` field was overwritten with the same V2.0 handbook string. That string does not describe SP-2011-3421. Repair is out of scope here. Record the wrongness. Do not edit the row.

`python tooling/check_source_watch.py --record SLUG VERSION DATE` rewrites `version` and `last_checked` on an existing slug. It does not create a row. It does not write `document`. After the rebuild, `document` must be hand-edited to `NASA Risk Management Handbook` (the watch `document` field carries the document title, not the version). `--record nasa-risk "<new source_version>" <vet-date>` then rewrites `version` and `last_checked`. CAUTION: no gate compares watch `version` to catalog `source_version` — the three-surface byte-match (PACK.yaml, catalog row, watchlist) is a manual Testing step below. Record only after the catalog row carries the new `source_version`, so the manual diff has a fixed reference.

Registration surfaces that name the 2011 pin and must move with the pack: `catalog.json` nasa-risk row (nine keys, same shape; do not change top-level `updated`), `README.md` catalogue row, `SKILLS.md` nasa-risk description, `NOTICE` `[pack: nasa-risk]` block, `packs/nasa-risk/LICENSE`, `packs/nasa-risk/SKILL.md`. Generated pages (`docs/packs/nasa-risk/index.html`, `docs/packs.html`, `docs/sitemap.xml`) come from generators. Do not hand-edit them.

Surfaces that count packs, skills, or NASA family size do not move. Pack count stays 74. Skill count stays 83. `docs/index.html` `NASA · 16` chip stays 16. `docs/products/website/01-jgs-se-knowledge-packs.yaml` `NASA (16)` stays 16. `README.md` `packs-74` badge stays. Plugin `version` fields stay. `RELEASE-INFO.txt` stays.

`/se` already routes risk to `nasa-risk` and PRA to `nasa-pra` (`packs/se/SKILL.md` lines 87, 93, 124, 145). No new slug. No new routing row. Description text may name Version 2.0. Do not add `nasa-risk` to the system-safety row. Do not remove `nasa-pra` from it.

`docs/superpowers/backlog.md` line 101, slug `source-watch-calibrate-and-wire-2`, status `open`. Evidence names 14 drift rows, `nasa-pra` and `nasa-risk` among them. This cut removes `nasa-risk` from that evidence list and from the count. It does not close the row. Thirteen findings remain, including the mis-pinned `nasa-pra` watch `version`.

Neighbors named in other packs (`dod-rio`, `nasa-ms-7009`, `gao-schedule`, `space-signpost`) cite `nasa-risk` as the RIDM/CRM pack. Leave those sentences. They do not pin SP-2011-3422.

## Decision register

- D1: Primary pin is NASA Risk Management Handbook Version 2.0, November 2024, two volumes, one pack. Part 1 NASA/SP-20240014019 (14,471,540 bytes, 303 pages) is the doctrine volume and the volume that supersedes NASA/SP-2011-3422. Part 2 NASA/SP-20240014326 (6,669,330 bytes, 89 pages) is the examples volume. Both PDFs are in scope. Do not pin Part 2's verso typo `SP-202400114326`. Do not drop Part 2. Do not split into two packs.
- D2: Licence stays tier 1 public domain, US Government work, 17 U.S.C. 105. `license_tier: 1`, `commercial_use: true`, `share_alike: false`, `attribution_required: false`. NTRS `PUBLIC_USE_PERMITTED` plus NASA special-publication class is the evidence. Execution re-fetches both PDFs and both citation APIs. Stop if either PDF URL is dead, either file is not `%PDF`, either NTRS record is no longer `distribution: PUBLIC`, or either record sets `containsThirdPartyMaterial` true. Record vet date, both byte sizes, both page counts, and the determination fields in `PACK.yaml` `notes`.
- D3: `nasa-pra` is out. SP-2011-3421 is the PRA Procedures Guide, not the handbook Part 1 supersedes. Do not edit `packs/nasa-pra/`, its catalog row, its NOTICE block, or its watchlist row. The watchlist `version` on `nasa-pra` is a mis-pin from 2026-10-12. Leave it. Name it in the backlog evidence shrink so the next reader does not "fix" it inside this cut.
- D4: Reconstruction rule stays the live pack's rule. Synthesized reference notes. Short defined terms may be kept. No long verbatim passages. No PDF page images. NPR 8000.4, NPD 1000.0, NPR 7120.5, and NPR 8715.3 are named as the policy the handbook aligns to. They are not quoted and not rebuilt. Domain PRA methods stay a pointer to `nasa-pra`, not a chapter here.
- D5: Chapter count is one file per Part 1 numbered chapter, excluding chapter 7 Definitions, plus one file for the Part 2 examples. Expected 7 files: ch01 through ch06 from Part 1 chapters 1 through 6, ch07 from Part 2 chapters 1 through 4 as one examples chapter. Contents lists win over this table. If Part 1 gains or loses a numbered chapter, follow the list and keep Definitions out of `chapters/`. Do not split Part 1 chapter 4's RIDM steps into three files. Do not split Part 2 into four files. Floor 6, ceiling 8. Appendices A through I are not chapters.
- D6: Support files stay three: `glossary.md`, `cheatsheet.md`, `patterns.md`. They are not in the 6 to 8 count. Glossary absorbs Part 1 chapter 7 and the acronym list. Cheatsheet absorbs the RIDM six steps and the CRM five steps plus communicate-and-document. Patterns absorbs risk-leadership and graded-approach moves. No fourth support file.
- D7: Classification churn is delete-then-append, not a migration. Remove every `nasa-risk` row from `docs/classification-rules.json` `assignments` and from `docs/capability-pack-map-note-overrides.json` `notes` (13 rows each today: 10 chapters + 3 support). Append one `is_support: false` row per new chapter file and one `is_support: true` row per surviving support file. Same keys in both files. Cluster `Risk Management` unless a chapter's best fit is a different name already in `cluster_names`. Do not invent a cluster. Bump the `744` literal in `tooling/generate_capability_map.py` (docstring and the three comparison sites) to `744 - 10 + N`, where N is the new chapter-file count. Support rows do not change the total: 3 removed, 3 added. Expected total `734 + N`. At the D5 expected N of 7, total is 741. `map_version` stays `1.22.0`. `generated_on` on both JSON files moves to the execution date.
- D8: Counts that measure packs or skills do not change. Pack count stays 74. Skill count stays 83. NASA family chip stays 16. `catalog.json` `updated` stays `2026-10-14`. Do not bump `RELEASE-INFO.txt` or either plugin `version`. Do not add a skill path. The slug already exists in both plugin manifests.
- D9: Watchlist `nasa-risk` only. Hand-edit `document` to the new pin. Run `--record nasa-risk "<catalog source_version>" <vet-date>` after the catalog row matches, not before. `version` must equal catalog `source_version`. Do not pass a URL. Do not record `nasa-pra`.
- D10: Backlog slug `source-watch-calibrate-and-wire-2` stays `open`. Evidence cell drops `nasa-risk` and states the count is 13, not 14. The remaining list keeps `nasa-pra` and states its watch `version` is a mis-pin of the handbook V2.0 onto SP-2011-3421, not a rebuild candidate for this cut. Do not delete the row. Do not mark it `done`.

## Problem

`packs/nasa-risk` still teaches the November 2011 handbook. The publisher's Version 2.0 (November 2024) says it supersedes that document, adds risk leadership as a named pillar, and splits doctrine from worked examples. The watch already recorded the drift on 2026-10-12 and left the pack untouched, which is what the watch is for. Leaving the pack there means `/nasa-risk` answers from a document the publisher has withdrawn. The same watch row was copied onto `nasa-pra`. Rebuilding both from that copy would replace a PRA procedures guide with a risk-management handbook.

## Approach

Rebuild the existing slug. Do not add a slug. Do not open `nasa-pra`.

1. Re-fetch both citation APIs and both PDFs. Confirm D2. Record vet date, byte sizes, page counts, and copyright determination fields in `PACK.yaml` `notes`. Stop if D2 fails.
2. Extract both contents lists. Freeze chapter titles from Part 1 chapters 1 through 6 plus one Part 2 examples chapter, unless the lists contradict D5. Definitions and appendices do not become chapters.
3. Replace `packs/nasa-risk/` content. Keep the slug, the directory, and the three support filenames. Delete the ten old chapter files. Write the new chapter files. Rewrite `SKILL.md`, `PACK.yaml`, `LICENSE`, `glossary.md`, `cheatsheet.md`, and `patterns.md` against V2.0. `built_on` is the execution date. `build.method` names the two PDFs, not the 2011 extraction. `change_indication` stays `reconstructed as synthesized reference notes`.
4. Apply D7. Hand-edit rules and overrides. Bump the `744` literal. Regenerate `docs/capability-pack-map.json` and `docs/capability-pack-map.md` with `tooling/generate_capability_map.py`. Do not hand-edit those two generated files.
5. Update the version-bearing registration surfaces in Codebase context. Regenerate `docs/packs/nasa-risk/index.html` with `tooling/gen_pack_pages.py --only nasa-risk`, then `docs/packs.html` with `tooling/gen_packs_page.py`. Do not hand-edit generated HTML. `--only` must not be the last generator run if it truncates `docs/sitemap.xml`. Finish with a generator invocation that rewrites the sitemap from the full catalog.
6. Hand-edit watchlist `document`, then `--record` per D9.
7. Shrink the backlog evidence cell per D10.
8. Add an `## [Unreleased]` `### Changed` bullet in `CHANGELOG.md` naming the nasa-risk rebuild and the two SP numbers. Do not add an `## [x.y.z]` heading. Do not bump a version.
9. Run the gates in Testing. Fix only this pack's findings.

`PACK.yaml` field values once the vet passes:

```yaml
slug: nasa-risk
title: "NASA Risk Management Handbook, Version 2.0 (NASA/SP-20240014019, NASA/SP-20240014326)"
publisher: "NASA"
source_version: "Version 2.0 (November 2024)"
license: "Public Domain (US Government work, 17 U.S.C. 105)"
license_tier: 1
commercial_use: true
share_alike: false
attribution_required: false
```

`build.source_pages` is 392 (303 + 89) unless a re-fetch returns different page counts. `build.chapters` equals the chapter-file count, not 10 and not 392. `notes` carries the public-domain line, both SP numbers, both byte sizes, both page counts, the vet date, the NTRS determination fields, the Part 1 supersession sentence, and the named-not-quoted policy list (NPR 8000.4, NPD 1000.0, NPR 7120.5, NPR 8715.3). No URL in `PACK.yaml`.

Provisional chapters. D5 wins if the PDFs disagree.

| File | Draws from | Job |
|---|---|---|
| ch01-introduction-and-scope.md | Part 1 ch 1 | Purpose, policy documents the handbook aligns to, what changed in Version 2.0, how the two parts are meant to be used. |
| ch02-objectives-driven-framework.md | Part 1 ch 2 | Risk and opportunity in the NASA context, objectives flow-down, risk leadership, graded rigor, integration across boundaries. |
| ch03-risk-models-and-posture.md | Part 1 ch 3 | Risk triplet, risk scenario diagram, known vs unknown-unknown, risk posture and tolerance, matrix display. |
| ch04-risk-informed-decision-making.md | Part 1 ch 4 | RIDM six steps in one chapter. Alternatives, analysis, deliberation, selection. Graded application stays here. |
| ch05-continuous-risk-management.md | Part 1 ch 5 | CRM initialize, identify, analyze, plan, track, control, communicate and document. |
| ch06-organizational-integration.md | Part 1 ch 6 | Life-cycle reviews, cross-cutting risk, risk management plan contents. |
| ch07-application-examples.md | Part 2 ch 1-4 | One chapter. Process selection, one activity-planning RIDM example, CRM execution examples. Examples illustrate Part 1. They do not add doctrine. |

`SKILL.md` frontmatter `name` stays `nasa-risk`. Description names Version 2.0 and both SP numbers, states RIDM and CRM plus risk leadership, and keeps the existing limit: domain PRA methods (fault trees, event trees, Bayesian inference) are not this pack. Point that limit at `nasa-pra` (NASA/SP-2011-3421), not at a 2002 PRA guide citation the 2011 skill still carries, unless Part 1 itself names the older guide as the current PRA pointer. If Part 1 names a newer PRA document, name that document and still point the skill at `nasa-pra` for the quantitative pack this repo ships. No source URL in the skill body. A `**Source:**` line may name the public-domain status and both SP numbers and must point at `LICENSE` for the legal text.

Catalog row keeps the nine live keys. `title` matches `PACK.yaml` `title`. `source_version` matches `PACK.yaml` `source_version`. `chapters` matches the new file count. `license` may stay the shorter catalog form `Public Domain (US Government work)` already used on the nasa-pra row, or match `PACK.yaml`. Pick one and use it. Do not add a key.

`NOTICE` `[pack: nasa-risk]` replaces the SP-2011-3422 lines with Version 2.0 and both SP numbers. Keep the courtesy-attribution sentence and the no-endorsement sentence. Do not edit `[pack: nasa-pra]`.

`LICENSE` replaces the 2011 identification with Version 2.0, both SP numbers, November 2024, and the same 17 U.S.C. 105 paragraph. No download URL, same rule as `docs/LICENSING.md`.

Chapter assignment notes are one sentence each, no em dash, and say the note is from Version 2.0 November 2024. Support-file notes stay short labels, same shape as the three notes being replaced.

Backlog evidence edit, substance required, wording not frozen: drop `nasa-risk` from the parenthetical and from the watchlist-field list; state 13 findings remain; state `nasa-pra` watch `version` still carries the handbook V2.0 string and that string does not describe SP-2011-3421; leave status `open`.

## Scope

In:

- Re-fetch of both NTRS records and both PDFs, D2 stop conditions.
- Replacement of `packs/nasa-risk/` content against Version 2.0, D5 chapter rule, D6 support files.
- Delete-then-append of `nasa-risk` rows in the rules file and the overrides file, plus the `744` literal bump.
- Regeneration of the capability map, the nasa-risk pack page, `docs/packs.html`, and a full-catalog sitemap.
- Catalog row, README catalogue row, SKILLS.md nasa-risk blurb, NOTICE nasa-risk block, watchlist `document` plus `--record`.
- One Unreleased changelog bullet.
- Evidence shrink on `source-watch-calibrate-and-wire-2`. `/se` description text only if it still says 2011 or SP-2011-3422. It does not, today. Leave the routing rows.

Out:

- Any edit under `packs/nasa-pra/`, its catalog row, its NOTICE block, or its watchlist row.
- The other 12 drift rows (sebok, nasa-se-handbook, nist-ssdf, nist-stat-handbook, dod-rio, nasa-schedule, dodaf, federal-bca, faa-ams-vv, mrl-deskbook, and the two standing-drift rows the backlog still counts inside 14).
- A new slug, a second pack for Part 2, or a chapter per Part 2 section.
- Quoting NPR, NPD, or PRA guide text. Embedding PDF pages.
- `source_url` in `PACK.yaml` or `catalog.json`.
- New validators, new page templates, new licence tiers.
- `RELEASE-INFO.txt`, plugin `version`, `catalog.json` `updated`, pack-count badges, the NASA family chip.
- GitHub release, plugin publish, or commit. This spec does not authorize those.

## Testing

- `python tooling/validate_pack.py packs/nasa-risk` and `python tooling/check_pack_quality.py packs/nasa-risk` exit 0 (30-line chapter floor; SKILL.md Topic Index chNN tokens must resolve to the new chapter set).
- `python tooling/test_catalog_live_set.py`, `test_catalogue_count.py`, `test_ci_gate.py` exit 0 (counts unchanged at 74/83).
- `python ~/.zcode/scripts/prose_check.py` on all touched prose exits 0 or findings fixed/justified.
- 14-gram verbatim scan of the new chapters vs both extracted PDF texts: zero contiguous runs of 18+ words (D4 no-long-verbatim).
- `python tooling/check_classification_rules.py` exits 0. Coverage errors on `nasa-risk` mean a chapter file and an assignment row disagree.
- `python tooling/check_capability_map.py` exits 0. Notes length equals `744 - 10 + N`.
- `python tooling/generate_capability_map.py` regenerates without a notes-length refusal. Re-run the capability-map check after generation.
- `python tooling/check_source_watch.py` exits 0. `nasa-risk` `version` equals catalog `source_version`. `nasa-pra` `version` is unchanged from the pre-cut string.
- `python tooling/check_release.py` exits 0, or its only new findings are outside this pack and get named, not fixed here.
- `grep -rn "SP-2011-3422" packs/nasa-risk/ catalog.json docs/source-watchlist.json NOTICE` returns nothing (2011 pin fully replaced). Separately confirm README.md no longer says `(10 chapters)` for nasa-risk and SKILLS.md row shows the new chapter count — no sentinel test covers README/SKILLS.md; verify by eye and record in the run report.
- `rg "nasa-risk" docs/superpowers/backlog.md` returns no hit on the `source-watch-calibrate-and-wire-2` row. Hits on other rows are out of scope.
- Chapter-file count is between 6 and 8. `build.chapters` equals that count. Catalog `chapters` equals that count.
- No URL string in `PACK.yaml` or `catalog.json`.

## Non-goals

- Do not treat the 2026-10-28 fetch as a substitute for the execution-time re-fetch. The vet in step 1 is mandatory.
- Do not "correct" the `nasa-pra` watchlist row inside this cut. The mis-pin is recorded so it is not forgotten. Repair is a later cut, and only after someone confirms whether SP-2011-3421 itself has a successor. This spec does not claim that it has one.
- Do not close `source-watch-calibrate-and-wire-2`. Thirteen findings remain.
- Do not bump a release version to mark the rebuild. Changelog Unreleased is the record until a release cut says otherwise.
- Do not edit neighbor pack chapters that mention `nasa-risk`.
- Do not commit the downloaded PDFs. They are vet inputs, not repo content.
