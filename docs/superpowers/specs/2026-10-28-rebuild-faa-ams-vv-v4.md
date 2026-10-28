# rebuild-faa-ams-vv-v4

Rebuild `packs/faa-ams-vv` from FAA AMS Lifecycle Verification and Validation Guidelines Version 4.0 (January 2023). The live pack pins Version 3.0 (April 2017). The V4 PDF does not print a supersession sentence. The version jump comes from the cover and the watch observation. Do not quote a sentence the file does not contain.

## Research

Spec fetch on 2026-10-28. FAST toolkit page HTTP 200 HTML. PDF HTTP 200, `Content-Type: application/pdf`, `%PDF-1.3`, `Content-Length: 2700181`. Bytes 2,700,181 and 63 pages are author-observed. Re-verify both at execution vet. They are a check, not a lock, except the D2 stop conditions. `Last-Modified: Thu, 17 Apr 2025 15:42:43 GMT` is a host cache stamp, not the cover date.

research: https://fast.faa.gov/AMSBB_Verification_Validation.cfm
research: https://fast.faa.gov/docs/vandvguidelines.pdf

| Field | Observed |
|---|---|
| Cover title | FAA AMS LIFECYCLE VERIFICATION AND VALIDATION GUIDELINES |
| Running head | AMS Lifecycle Verification and Validation Guidelines |
| Version | Version 4.0 |
| Cover date | January 2023 |
| PDF URL | https://fast.faa.gov/docs/vandvguidelines.pdf |
| Bytes | 2,700,181 |
| Pages | 63 (pypdf; printed body runs to page 61, plus cover and contents) |
| PDF metadata | Title `VV Guidelines Version 4 (Clean)`; Author `Rose and Howard Shectman`; Creator `Word`; Producer `macOS Version 13.4 (Build 22F66) Quartz PDFContext`; CreationDate `D:20230605193321Z` |

The official page is the FAST AMS "Verification & Validation" toolkit page, not a faa.gov AIR library page. That older path 404s. The toolkit button is labeled "Verification & Validation Guidelines" and points at `docs/vandvguidelines.pdf`. Bare `https://fast.faa.gov/vandvguidelines.pdf` returns a FAST HTML shell, not the PDF. Pin the `/docs/` URL.

Supersession is not printed in the PDF. Cover, contents, and a full-text scan for "supersede", "version 3", "copyright", "Booz", and "MITRE" returned no replacement sentence and no copyright page. The 2026-10-12 watch report says "stated supersedes". That sentence is not in the file. What is true: FAST hosts this PDF as the current guidelines, the cover reads Version 4.0 January 2023, and the live pack pins Version 3.0 April 2017. Do not invent a supersession quote. `PACK.yaml` `notes` records the watch claim as unverified against the PDF, not as a quoted line.

Copyright determination is from absence plus publisher class, not from a printed legend. The PDF does not print "public domain", "17 U.S.C.", or a contractor copyright notice. Front matter has no Booz Allen or MITRE copyright block. PDF `/Author` metadata lists personal names. That is not a contractor copyright claim. Do not invent a legend the PDF does not print.

Third-party text that is present, and must stay paraphrased. Page 3 footnote on the verification and validation definitions:

> Note: Capability Maturity Model Integration (CMMI) for Development, Version 1.2, Carnegie Mellon Software Engineering Institute, Pittsburgh, PA, August 2006.

The same page states the definitions are consistent with CMMI and that GAO uses CMMI for quality audits. CMMI and CMMI for Development are marked registered. That is the live pack's paraphrase-only caution. Carry it forward. Do not copy the definition sentences that sit under the footnote.

Contents (page i), top-level numbered sections only. Subsections stay inside the parent chapter except SASP, which the V4 list gives its own chapter. Appendices are not chapters.

1. Introduction (1.1 Scope, 1.2 V&V Terms and Definitions, 1.3 V&V Philosophy, including 1.3.1 V-Model Implementation and 1.3.2 Agile Acquisition/Shift-Left Principles In V&V)
2. V&V Implementation Guidance (2.1 Planning, 2.2 Performing, 2.3 Reporting, 2.4 Decision Support)
3. V&V Approach in the AMS Lifecycle (3.1 Service Analysis & Strategic Planning, 3.2 Concept and Requirements Definition, 3.3 Investment Analysis with 3.3.1 Initial and 3.3.2 Final, 3.4 Solution Implementation, 3.5 In-Service Management)

Appendix A Acronyms. Appendix B Verification and Validation Checklists (PRD, ISPD, PMP, APB). Appendix C Definitions. Figures 1 through 5. Tables 1 through 6, one per lifecycle slice in section 3.

Grouping note versus the 3.0 pack. This is a pack-grouping difference, not a document novelty. The 3.0 PDF already carries section 1.3.2 Agile Acquisition / shift-left and section 3.1 Service Analysis & Strategic Planning as its own Table 1 slice. The current pack folds early lifecycle into one chapter and starts its Table-1 chapter with SASP and CRD together. The V4 rebuild follows the V4 contents list instead, which gives SASP its own chapter. Contents list wins. Do not keep the 3.0 grouping where the V4 list disagrees.

Provisional chapter map, discarded where the PDF contents list disagrees. SASP is its own file because the V4 list gives section 3.1 its own slice. Expected 4 files. Floor 3, ceiling 6.

| File | Draws from | Job |
|---|---|---|
| ch01-introduction-and-vv-philosophy.md | Section 1 | Scope, work-product/component/product terms, verify-vs-validate (paraphrased, CMMI footnote named), V&V vs QA, V-model, agile acquisition and shift-left. |
| ch02-implementation-guidance.md | Section 2 | Plan, perform, report, decide. Work-product methods vs product/component methods. Independence. Report minimum content. Decision support. |
| ch03-service-analysis-and-strategic-planning.md | Section 3.1 | SASP only. Table 1. Front-loaded security and the early management documents that Table 1 binds. |
| ch04-lifecycle-after-sasp.md | Sections 3.2 through 3.5 | Concept and Requirements Definition, initial and final investment analysis, solution implementation, in-service management. Tables 2 through 6. DT/OT/IOA stays here, not a separate chapter. |

If sections 3.2 through 3.5 will not fit one file without burying a decision-point table, split into ch04 (CRD and investment analysis) and ch05 (solution implementation and in-service). That split is allowed inside the ceiling. It is not the default.

## Codebase context

Post-P58 baseline, re-checked on main at `b019f9c` on 2026-10-28. Precedent for the reconstructed-notes rule and the three support files is the live `packs/faa-ams-vv/` itself, plus the P58 rebuild shape in `docs/superpowers/specs/2026-10-28-rebuild-nasa-risk-handbook-v2.md`. Required content-pack layout is `docs/PACK-SPEC.md`.

`packs/faa-ams-vv/` today: `PACK.yaml` (title `FAA AMS Lifecycle V&V Guidelines v3.0`, `source_version` `Version 3.0 (April 2017)`, `license` the shorter `Public Domain (US Government work)`, `source_pages: 54`, `chapters: 7`, `built_on: 2026-06-24`), `SKILL.md`, `LICENSE`, `glossary.md`, `cheatsheet.md`, `patterns.md`, and 7 chapter files under `chapters/`. Support files are not chapters. The seven files to delete: `ch01-faa-ams-vv-introduction-and-vv-philosophy.md`, `ch02-faa-ams-vv-implementation-guidance.md`, `ch03-faa-ams-vv-approach-and-early-lifecycle.md`, `ch04-faa-ams-vv-investment-analysis.md`, `ch05-faa-ams-vv-solution-implementation.md`, `ch06-faa-ams-vv-in-service-management.md`, `ch07-faa-ams-vv-acronyms-checklists-definitions.md`.

`faa-ams-vv` assignment rows today: 7 chapter rows plus 3 support rows (`glossary.md`, `cheatsheet.md`, `patterns.md`). Clusters in use: `Verification` (ch01, ch02, ch03, ch05, ch07, and all three support files) and `Validation` (ch04, ch06). Both names already exist in `cluster_names`, as does `Governance, Reviews, Gates & Control Points`. Do not invent one. Overrides are a parallel list, same `(pack, chapter)` keys, one `note` string each. Live support notes, which the rebuild keeps as the short-label shape: `Glossary for pack`, `Cheatsheet / quick reference`, `Patterns/practice heuristics`. `tooling/check_classification_rules.py` requires one `is_support: false` row per `packs/<slug>/chapters/*.md` and rejects an assignment whose chapter file is gone. There is no removal API. A rebuild deletes the old `faa-ams-vv` rows from both JSON files and appends the new ones. Key sets must match after the edit.

`tooling/generate_capability_map.py` refuses any notes length other than 741 (line 9 docstring, line 195 `len(notes) != 741`, line 203 `if len(notes) != 741`, line 204 error string `notes length must be 741`). Those four literals must move, or the generator rejects the new note file. Do not hand-edit `docs/capability-pack-map.json` or `docs/capability-pack-map.md`. `map_version` on both JSON files is `1.22.0` and stays. `generated_on` on both is `2026-10-28` today and must move to the execution date or the fidelity check fails. Generator invocation:

```text
python tooling/generate_capability_map.py --generated-on YYYY-MM-DD --sync-md
```

Watchlist today, `last_checked` 2026-10-12. `faa-ams-vv` `document` is `Version 3.0 (April 2017)`. `version` already carries `Version 4.0 (January 2023)` from the 2026-10-12 calibration write-through. `document` is what the pack was built from. `version` is what the watch last saw. After the rebuild, `document` must be hand-edited to `AMS Lifecycle Verification and Validation Guidelines`. The record command rewrites `version` and `last_checked` on an existing slug:

```text
python tooling/check_source_watch.py --record SLUG VERSION DATE
``` It does not create a row. It does not write `document`. Entry keys, in order: `slug`, `publisher`, `document`, `version`, `last_checked`, `hint`. CAUTION: no gate compares watch `version` to catalog `source_version`. The three-surface byte-match (PACK.yaml, catalog row, watchlist) is a manual Testing step. Record only after the catalog row carries the new `source_version`, so the manual diff has a fixed reference.

`nasa-pra` watch `version` is `NASA Risk Management Handbook Version 2.0 (November 2024; NASA/SP-20240014019 Part 1, NASA/SP-20240014326 Part 2)`. That string does not describe SP-2011-3421. P58 recorded the wrongness and left the row. Do not edit it. Record the same sentence in the backlog evidence cell.

Registration surfaces that name the 2017 pin and must move with the pack: `catalog.json` faa-ams-vv row (nine keys, same shape; do not change top-level `updated`), `README.md` catalogue row (line 164, `live (7 chapters)` must become the new count, title must become the new title), `SKILLS.md` faa-ams-vv description (line 50), `NOTICE` `[pack: faa-ams-vv]` block (starts at the marker, ends before `[pack: gao-agile]`), `packs/faa-ams-vv/LICENSE`, `packs/faa-ams-vv/SKILL.md`. Generated pages (`docs/packs/faa-ams-vv/index.html`, `docs/packs.html`, `docs/sitemap.xml`) come from generators. Do not hand-edit them.

The pack-page generator rewrites that pack page and always rewrites `docs/sitemap.xml` from the full live catalog:

```text
python tooling/gen_pack_pages.py --only faa-ams-vv
``` It does not truncate the sitemap. Finish with `python tooling/gen_packs_page.py` for `docs/packs.html`. Do not hand-edit generated HTML.

Surfaces that count packs, skills, or FAA family size do not move. Pack count stays 74. Skill count stays 83. `SKILLS.md` line 9 stays `74 packs (+8 signposts, +1 orchestrator)`. `docs/index.html` `FAA · 8` chip stays 8. `docs/products/website/01-jgs-se-knowledge-packs.yaml` `FAA (8)` stays 8. `README.md` `packs-74` badge stays. Plugin `version` fields stay. `RELEASE-INFO.txt` stays. Do not edit `.claude-plugin/plugin.json` or `.cursor-plugin/plugin.json`. The slug is already in both. Do not edit `.github/workflows/validate.yml`.

`/se` already routes verification and validation to `faa-ams-vv`, and the FAA row already names it (`packs/se/SKILL.md` lines 80, 81, 127, 143, 144, 146). No new slug. No new routing row. Description text may name Version 4.0. Do not add or remove packs on those rows. Today those rows do not say 2017 or Version 3.0. Leave them.

`docs/superpowers/backlog.md` line 101, slug `source-watch-calibrate-and-wire-2`, status `open`. Evidence names 13 drift findings after the P58 shrink, `faa-ams-vv` among them. This cut removes `faa-ams-vv` from that evidence list and from the count. It does not close the row. Twelve findings remain.

`CHANGELOG.md` already has `## [Unreleased]`, `### Added`, and `### Changed` (the P58 `nasa-risk` bullet). Add one bullet under the existing `### Changed`. Do not add an `## [x.y.z]` heading. Do not edit `## [1.23.0]`.

Neighbors (`faa-sem` and the `/se` FAA row) cite this pack as the AMS V&V overlay. Leave those sentences unless they pin "Version 3.0" or "April 2017". A version pin inside another pack is a one-line edit. A doctrine sentence is not.

`sources/` is gitignored. The PDF and the text extract stay untracked. `git ls-files sources/` must stay empty.

Catalog `license` on the live faa-ams-vv row is `Public Domain (US Government work)`. PACK.yaml `license` today is the same shorter string. This cut lengthens PACK.yaml to the D2 form `Public Domain (US Government work, 17 U.S.C. 105)`, matching the P58 nasa-risk split. Keep the catalog cell short. Do not lengthen it.

## Decision register

- D1: Primary pin is FAA AMS Lifecycle Verification and Validation Guidelines, Version 4.0, January 2023, one PDF, one pack. URL `https://fast.faa.gov/docs/vandvguidelines.pdf`, 2,700,181 bytes, 63 pages (author-observed; re-verify at execution vet). Cover title is the title string. Do not pin the bare `fast.faa.gov/vandvguidelines.pdf` path (that URL returns an HTML shell). Do not split the appendices into a second pack. Do not quote a supersession sentence the PDF does not print.
- D2: Licence stays tier 1 public domain, US Government work, 17 U.S.C. 105. Field values, verbatim: `license: "Public Domain (US Government work, 17 U.S.C. 105)"`, `license_tier: 1`, `commercial_use: true`, `share_alike: false`, `attribution_required: false`. Evidence is FAA authorship plus FAST hosting plus no contractor copyright block in the front matter, the same class as the 3.0 pin. Those three strings are absent from the file. Do not invent a legend. Execution re-fetches the PDF. Stop if the URL is dead, the file is not `%PDF`, the cover no longer reads Version 4.0 January 2023, or the front matter now carries a contractor copyright notice (Booz Allen, MITRE, or equivalent). PDF `/Author` personal names are not a contractor copyright. Stop only if the front matter itself carries the notice.
- D3: Reconstruction rule stays the live pack's rule. Synthesized reference notes. Short defined terms may be kept. No long verbatim passages. No PDF page images. CMMI for Development v1.2 definitions are paraphrased, never copied. The page 3 footnote is named, not reproduced as the definition. Tables 1 through 6 are January 2023 policy snapshots, illustrative, not live authority. AMS policy sections named on the FAST page (Section 2.1.6) are named, not quoted, and not rebuilt.
- D4: Other FAA packs are out. Do not edit `packs/faa-sem/`, `packs/faa-req-handbook/`, `packs/faa-system-safety/`, `packs/faa-hf-std/`, `packs/faa-rma/`, `packs/faa-8110-49/`, or `packs/faa-std-025/`. Do not edit their catalog rows, NOTICE blocks, or watchlist rows. `mrl-deskbook` and the other remaining drift rows stay out. `nasa-risk` is already rebuilt. Do not reopen it. `nasa-pra` stays mis-pinned.
- D5: Chapter count is one file per numbered section 1, 2, and 3, with SASP (section 3.1) as its own chapter, plus a split of section 3.3 through 3.5 only if one file would bury a decision-point table, plus no file whose only job is an appendix. Expected 4 files: ch01 section 1 (including 1.3.2 shift-left), ch02 section 2, ch03 section 3.1 (SASP), ch04 sections 3.2 through 3.5. Contents list wins over the provisional table. Floor 3, ceiling 6. Appendices A, B, and C are not chapters. Do not keep `ch07-faa-ams-vv-acronyms-checklists-definitions.md`. Do not write one file per table.
- D6: Support files stay three: `glossary.md`, `cheatsheet.md`, `patterns.md`. They are not in the 3 to 6 count. Glossary absorbs Appendix A acronyms and Appendix C definitions (paraphrased; CMMI-sourced terms named, not copied). Cheatsheet absorbs the decision-point rules and the plan/perform/report/decide pipeline. Patterns absorbs shift-left and independence moves the guideline states. No fourth support file.
- D7: Classification churn is delete-then-append, not a migration. Remove every `faa-ams-vv` row from `docs/classification-rules.json` `assignments` and from `docs/capability-pack-map-note-overrides.json` `notes` (10 rows each today: 7 chapters + 3 support). Append one `is_support: false` row per new chapter file and one `is_support: true` row per surviving support file. Same keys in both files. Cluster `Verification` or `Validation`, both already in `cluster_names`. A chapter that is mostly decision-point tables may use `Governance, Reviews, Gates & Control Points` if that fit is better. Do not invent a cluster. Bump the `741` literal in `tooling/generate_capability_map.py` (docstring line 9 and the three comparison sites at lines 195, 203, and 204) to `741 - 7 + N`, where N is the new chapter-file count. Support rows do not change the total: 3 removed, 3 added. Expected total `734 + N`. At the D5 expected N of 4, total is 738. `map_version` stays `1.22.0`. `generated_on` on both JSON files moves to the execution date.
- D8: Counts that measure packs or skills do not change. Pack count stays 74. Skill count stays 83. FAA family chip stays 8. `catalog.json` `updated` stays `2026-10-14`. Do not bump `RELEASE-INFO.txt` or either plugin `version`. Do not add a skill path. The slug already exists in both plugin manifests.
- D9: Watchlist `faa-ams-vv` only. Hand-edit `document` to `AMS Lifecycle Verification and Validation Guidelines` (the watch `document` field carries the document title, not the version). Run the record command after the catalog row matches, not before:

```text
python tooling/check_source_watch.py --record faa-ams-vv "<catalog source_version>" <vet-date>
``` `version` must equal catalog `source_version`. Do not pass a URL. Do not record any other slug. Same caution as Codebase context: no automated gate does that comparison, and the byte-match stays a manual Testing step. Watch `version` already reads `Version 4.0 (January 2023)` from the 2026-10-12 calibration write-through. The record command still rewrites `version` and `last_checked` so the date matches the vet.
- D10: Backlog slug `source-watch-calibrate-and-wire-2` stays `open`. Evidence cell drops `faa-ams-vv` and states the count is 12, not 13. The remaining list keeps `nasa-pra` and keeps the P58 statement that its watch `version` is a mis-pin of the handbook Version 2.0 onto NASA/SP-2011-3421. That cell also drops the slug token itself. Do not delete the row. Do not mark it `done`.

## Problem

`packs/faa-ams-vv` still teaches the April 2017 guidelines (Version 3.0, 54 pages, 7 chapters). FAST now hosts Version 4.0 (January 2023, one PDF, 63 pages) as the current AMS Lifecycle Verification and Validation Guidelines. The watch already recorded that drift on 2026-10-12 and left the pack untouched, which is what the watch is for. Leaving the pack there means `/faa-ams-vv` answers from a document the publisher no longer hosts as current. Because the file prints no supersession sentence, the rebuild uses the cover date and the watch observation. It does not invent a quote.

The 3.0 pack also groups the body differently from the V4 contents list. It folds early lifecycle into one chapter and starts its Table-1 chapter with SASP and CRD together. The V4 list gives SASP (section 3.1) its own slice. That grouping difference is a pack choice, not a document novelty: the 3.0 PDF already carries sections 1.3.2 and 3.1. Contents list wins.

## Approach

Rebuild the existing slug. Do not add a slug. Do not open other FAA packs. Do not reopen `nasa-risk`. Do not repair `nasa-pra`.

1. Re-fetch the FAST PDF at `https://fast.faa.gov/docs/vandvguidelines.pdf`. Confirm D2. Record vet date, byte size, page count, and the front-matter finding in `PACK.yaml` `notes`. Stop if D2 fails. The 2026-10-28 spec fetch is not a substitute for this re-fetch. Bytes 2,700,181 and 63 pages are a check, not a lock.
2. Extract the contents list (page i). Freeze chapter titles from that list under D5. Expected 4 files, SASP its own chapter. Discard the provisional table if the re-fetched list disagrees. Floor 3, ceiling 6. Appendices do not become chapters. Delete the seven old chapter files only after the vet and the freeze both pass.
3. Replace `packs/faa-ams-vv/` content. Keep the slug, the directory, and the three support filenames. Write the new chapter files. Rewrite `SKILL.md`, `PACK.yaml`, `LICENSE`, `glossary.md`, `cheatsheet.md`, and `patterns.md` against Version 4.0. `built_on` is the execution date, not a date copied from this spec's filename. `build.method` names the 4.0 PDF, not the 2017 extraction. `change_indication` stays `reconstructed as synthesized reference notes`.
4. Apply D7. Hand-edit rules and overrides. Delete the 10 `faa-ams-vv` rows, then append `N + 3`. Bump the four `741` literals to `741 - 7 + N`. Regenerate `docs/capability-pack-map.json` and `docs/capability-pack-map.md` with `tooling/generate_capability_map.py`. Do not hand-edit those two generated files.
5. Update the version-bearing registration surfaces in Codebase context. Regenerate `docs/packs/faa-ams-vv/index.html` with the pack-page generator restricted to `faa-ams-vv`, then `docs/packs.html` with `tooling/gen_packs_page.py`. Do not hand-edit generated HTML. The restricted run always rewrites `docs/sitemap.xml` from the full live catalog, so it does not truncate the sitemap. Finish with `gen_packs_page.py` anyway.
6. Hand-edit watchlist `document` to `AMS Lifecycle Verification and Validation Guidelines`, then the record command per D9, and only once the catalog row already carries the new pin.
7. Shrink the backlog evidence cell per D10. Count becomes 12. The new cell has no `faa-ams-vv` token. Status stays `open`.
8. Add one bullet under the existing `## [Unreleased]` `### Changed` heading in `CHANGELOG.md`. Name the faa-ams-vv rebuild, the retired April 2017 pin, SASP as its own chapter, and the CMMI v1.2 paraphrase. Do not add an `## [x.y.z]` heading. Do not bump a version.
9. Run the gates in Testing. Fix only this pack's findings.

Pin string, verbatim, in PACK.yaml `source_version`, the catalog `source_version`, and the watchlist `version` once the record command runs: `Version 4.0 (January 2023)`. If the re-fetch cover date disagrees, stop. Do not rewrite the pin to match a different issue.

Title, verbatim: `FAA AMS Lifecycle Verification and Validation Guidelines, Version 4.0`. Publisher, verbatim: `FAA`.

`PACK.yaml` field values once the vet passes:

```yaml
slug: faa-ams-vv
title: "FAA AMS Lifecycle Verification and Validation Guidelines, Version 4.0"
publisher: "FAA"
source_version: "Version 4.0 (January 2023)"
license: "Public Domain (US Government work, 17 U.S.C. 105)"
license_tier: 1
commercial_use: true
share_alike: false
attribution_required: false
```

`build.source_pages` is 63 unless a re-fetch returns a different page count. `build.chapters` equals the chapter-file count, not 7 and not 63. `notes` carries the public-domain line, the byte size, the page count, the vet date, the no-copyright-legend finding, the CMMI v1.2 paraphrase-only caution (name the August 2006 footnote, do not copy the definition sentences), the January 2023 snapshot caveat on Tables 1 through 6, and the statement that the PDF does not print a supersession sentence. No URL in `PACK.yaml`.

`SKILL.md` frontmatter `name` stays `faa-ams-vv`. Description names Version 4.0 January 2023, states the verify-vs-validate split, the three tiers, decision-point-gated V&V across the AMS lifecycle including shift-left, and keeps the existing limit. It is FAA acquisition V&V doctrine, not a general SE process model, not a requirements manual, and not a test-design textbook. CMMI v1.2 stays named and paraphrased. Surrounding AMS lifecycle stays a pointer to `faa-sem`. Phase tables are January 2023 snapshots. No source URL in the skill body. A `**Source:**` line may name the public-domain status and January 2023 and must point at `LICENSE` for the legal text.

Catalog row keeps the nine live keys, in order: `slug`, `title`, `publisher`, `source_version`, `license`, `license_tier`, `commercial_use`, `chapters`, `status`. `title` matches PACK.yaml `title`. `source_version` matches PACK.yaml `source_version`. `chapters` matches the new file count. `license` stays the shorter catalog form already on the live row: `Public Domain (US Government work)`. Do not lengthen the catalog cell to the PACK.yaml form. Do not add a key. Do not change top-level `updated` (`2026-10-14`).

`NOTICE` `[pack: faa-ams-vv]` replaces the April 2017 lines with Version 4.0 January 2023. Keep the courtesy-attribution sentence, the no-endorsement sentence, and the CMMI paraphrase caveat. Move the table-snapshot date from April 2017 to January 2023. State that the PDF does not print a supersession sentence. The double hyphen in the Licence line matches the existing NOTICE block shape. It is a field separator, not prose. Do not spread it into other sentences. Do not edit `[pack: gao-agile]`.

`LICENSE` replaces the 2017 identification with Version 4.0, January 2023, and the same 17 U.S.C. 105 paragraph. Keep both caveats: CMMI definitions paraphrased, and Tables 1 through 6 as a January 2023 policy snapshot. No download URL, same rule as `docs/LICENSING.md`.

Chapter assignment notes are one sentence each, no em dash, and say the note is from Version 4.0 January 2023. Support-file notes stay short labels, same shape as the three notes being replaced (`Glossary for pack`, `Cheatsheet / quick reference`, `Patterns/practice heuristics`).

Backlog evidence edit, substance required, wording not frozen: drop `faa-ams-vv` from the parenthetical and from the watchlist-field list; state 12 findings remain; keep the `nasa-pra` mis-pin sentence (watch `version` still carries the handbook Version 2.0 string and that string does not describe NASA/SP-2011-3421); the new cell names no slug token for this pack; leave status `open`.

## Scope

In:

- Re-fetch of the FAST `/docs/` PDF, D2 stop conditions. Bytes and page count re-verified at execution. The spec numbers are a check, not a lock.
- Replacement of `packs/faa-ams-vv/` content against Version 4.0, D5 chapter rule (contents list wins, SASP its own chapter), D6 support files.
- Delete-then-append of the 10 `faa-ams-vv` rows in the rules file and the overrides file, plus the four `741` literal bumps to `741 - 7 + N` (738 at N=4).
- Regeneration of the capability map, the faa-ams-vv pack page, `docs/packs.html`, and a full-catalog sitemap.
- Catalog row, README catalogue row, SKILLS.md faa-ams-vv blurb, NOTICE faa-ams-vv block, watchlist `document` plus the record command.
- One Unreleased changelog bullet.
- Evidence shrink on `source-watch-calibrate-and-wire-2` from 13 to 12, with no `faa-ams-vv` token in the new cell. `/se` description text only if it still says 2017 or Version 3.0. It does not, today. Leave the routing rows.

Out:

- Any edit under `packs/faa-sem/`, `packs/faa-req-handbook/`, `packs/faa-system-safety/`, `packs/faa-hf-std/`, `packs/faa-rma/`, `packs/faa-8110-49/`, or `packs/faa-std-025/`, their catalog rows, their NOTICE blocks, or their watchlist rows.
- Any edit under `packs/nasa-risk/` or `packs/nasa-pra/`, their catalog rows, their NOTICE blocks, or their watchlist rows. `nasa-pra` stays mis-pinned.
- The other 11 drift rows still on the backlog cell after this shrink (nasa-pra, sebok, nasa-se-handbook, nist-ssdf, nist-stat-handbook, dod-rio, nasa-schedule, dodaf, federal-bca, mrl-deskbook, and the standing-drift row the backlog still counts inside 13).
- A second pack for the appendices, or a chapter per table.
- Quoting CMMI definition sentences, AMS policy section text, or PDF page images. Inventing a supersession sentence the PDF does not print.
- `source_url` in `PACK.yaml` or `catalog.json`. Any `http://` or `https://` under `packs/faa-ams-vv/`.
- New validators, new page templates, new licence tiers.
- `RELEASE-INFO.txt`, plugin `version`, `catalog.json` `updated`, pack-count badges, the FAA family chip, `.github/workflows/validate.yml`.
- A new skill path or a new slug. Hand-edits to generated HTML, `docs/capability-pack-map.json`, or `docs/capability-pack-map.md`.
- GitHub release, plugin publish, or commit. This spec does not authorize those.

## Testing

- `python tooling/validate_pack.py packs/faa-ams-vv` and `python tooling/check_pack_quality.py packs/faa-ams-vv` exit 0 (30-line chapter floor; SKILL.md Topic Index `chNN` tokens must resolve to the new chapter set).
- `python tooling/test_catalog_live_set.py`, `test_catalogue_count.py`, and `test_ci_gate.py` exit 0 (counts unchanged at 74/83). `catalog.json` `updated` stays `2026-10-14`.
- `python ~/.zcode/scripts/prose_check.py` on all touched prose exits 0 or findings fixed/justified. Zero em dashes in headings and body prose of the files this cut wrote. The NOTICE `Licence:` line keeps the existing double-hyphen field separator.
- 14-gram verbatim scan of the new chapters against the extract: zero contiguous runs of 18 or more words (D3 no-long-verbatim). The CMMI footnote sentence is a named citation, not a passage to copy.
- `python tooling/check_classification_rules.py` exits 0. Coverage errors on `faa-ams-vv` mean a chapter file and an assignment row disagree.
- `python tooling/check_capability_map.py` exits 0. Notes length equals `741 - 7 + N`. At the expected N of 4, length is 738.
- The capability-map generator, invoked with the execution date and the markdown sync flag, regenerates without a notes-length refusal. Re-run the capability-map check after generation.

```text
python tooling/generate_capability_map.py --generated-on <vet-date> --sync-md
```
- `python tooling/check_source_watch.py` exits 0. `faa-ams-vv` `version` equals catalog `source_version`. No other slug's `version` changed. `nasa-pra` `version` is unchanged from the pre-cut mis-pin. No automated gate compares those two version fields. The three-surface byte-match (PACK.yaml pin, catalog pin, watchlist pin) is a manual step, and the record command runs only after the catalog row already carries the new pin.
- `python tooling/check_release.py` exits 0, or its only new findings are outside this pack and get named, not fixed here.
- `rg -n "April 2017" packs/faa-ams-vv catalog.json NOTICE` returns nothing. `rg -n "Version 3.0" packs/faa-ams-vv catalog.json NOTICE` returns nothing. Separately confirm `README.md` no longer says `v3.0` or `(7 chapters)` for faa-ams-vv and the `SKILLS.md` row shows Version 4.0. No sentinel test covers README or SKILLS.md. Verify by eye and record the result in the run notes.
- `rg -n "faa-ams-vv" docs/superpowers/backlog.md` returns no hit on the `source-watch-calibrate-and-wire-2` row. Hits on other rows are out of scope. The new evidence cell must not name this pack's slug.
- Chapter-file count is between 3 and 6. `build.chapters` equals that count. Catalog `chapters` equals that count.
- No URL string in `PACK.yaml` or `catalog.json`. `git ls-files sources/` is empty.
- CMMI caveat still present in `PACK.yaml` `notes`, `LICENSE`, `NOTICE` `[pack: faa-ams-vv]`, and `SKILL.md`. A rebuild that drops it fails.

Count formulas, not a hardcoded chapter total: content packs stay 74, skills stay 83, map assignments `741 - 7 + N` where N is the frozen chapter count (3, 4, 5, or 6). At the expected N of 4, assignments are 738.

## Non-goals

- Do not treat the 2026-10-28 fetch as a substitute for the execution-time re-fetch. The vet in step 1 is mandatory. Bytes 2,700,181 and 63 pages are a check, not a lock, except the D2 stop conditions.
- Do not invent a supersession sentence. The file does not print one. The 2026-10-12 watch line "stated supersedes" stays unverified. Use the cover date and the watch observation.
- Do not "correct" the `nasa-pra` watchlist row inside this cut. The mis-pin is recorded so it is not forgotten. Repair is a later cut. This spec does not claim SP-2011-3421 has a successor.
- Do not reopen `nasa-risk`. P58 already rebuilt it.
- Do not close `source-watch-calibrate-and-wire-2` from Non-goals either. Twelve findings remain.
- Do not bump a release version to mark the rebuild. Changelog Unreleased is the record until a release cut says otherwise.
- Do not edit neighbor pack chapters that mention this slug unless they pin Version 3.0 or April 2017.
- Do not commit the downloaded PDF. It is a vet input, not repo content. Leave it out of git.
- Do not edit `RELEASE-INFO.txt`, either plugin `version`, `catalog.json` `updated`, or `.github/workflows/validate.yml`.

## Do not

- Do not edit other FAA packs, their catalog rows, their NOTICE blocks, or their watchlist rows.
- Do not close `source-watch-calibrate-and-wire-2`. Twelve findings remain after this shrink.
- Do not bump a release version. Changelog Unreleased is the record.
- Do not edit neighbor pack chapters that mention `faa-ams-vv` unless they pin Version 3.0 or April 2017.
- Do not commit the downloaded PDF. It is a vet input, not repo content.
- Do not bump `RELEASE-INFO.txt`, either plugin `version`, or `catalog.json` `updated`.
- Do not add a skill path. Do not add a slug. Do not hand-edit generated HTML, `docs/capability-pack-map.json`, or `docs/capability-pack-map.md`.
