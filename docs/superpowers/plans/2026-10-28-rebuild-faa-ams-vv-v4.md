# Rebuild faa-ams-vv Guidelines v4 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rebuild the existing `packs/faa-ams-vv` slug from FAA AMS Lifecycle Verification and Validation Guidelines Version 4.0 (January 2023) and move every version-bearing registration surface off Version 3.0 (April 2017).

**Architecture:** Re-fetch the FAST PDF before any chapter prose. Freeze chapter titles from the contents list (sections 1, 2, and 3; SASP gets its own chapter; appendices fold into support files). Delete the seven 2017 chapter files and rewrite the pack in place. Delete every `faa-ams-vv` classification and note row, append the new set, and move the hard-coded 741-row pin in the capability-map generator to `741 - 7 + N`. Other FAA packs stay untouched.

**Tech Stack:** Markdown pack files, YAML frontmatter, JSON catalogue and map files, Python 3 stdlib tooling (`tooling/validate_pack.py`, `tooling/check_pack_quality.py`, `tooling/check_source_watch.py`, `tooling/generate_capability_map.py`, `tooling/check_capability_map.py`, `tooling/check_classification_rules.py`, `tooling/gen_pack_pages.py`, `tooling/gen_packs_page.py`, `tooling/check_release.py`). PDF text via `pdftotext` if present, else an already-installed reader. No new dependencies.

**Spec:** `docs/superpowers/specs/2026-10-28-rebuild-faa-ams-vv-v4.md`

Spec certificate sha256: `9d2b440fc901440eaf71ac8ec9f127e78a65f32daf5376038e3553edd594cb7f`.

## Global Constraints

- D1: primary pin is FAA AMS Lifecycle Verification and Validation Guidelines, Version 4.0, January 2023, one PDF, one pack. URL `https://fast.faa.gov/docs/vandvguidelines.pdf`, 2,700,181 bytes, 63 pages. Cover title is the title string. Do not pin the bare `fast.faa.gov/vandvguidelines.pdf` path (that URL returns an HTML shell). Do not split the appendices into a second pack. Do not quote a supersession sentence the PDF does not print.
- D2: licence stays tier 1 public domain, US Government work, 17 U.S.C. 105. Field values, verbatim: `license: "Public Domain (US Government work, 17 U.S.C. 105)"`, `license_tier: 1`, `commercial_use: true`, `share_alike: false`, `attribution_required: false`. Evidence is FAA authorship plus FAST hosting plus no contractor copyright block in the front matter, the same class as the 3.0 pin. The PDF does not print "public domain", "17 U.S.C.", or a contractor copyright notice. Do not invent a legend the PDF does not print. Execution re-fetches the PDF. Stop if the URL is dead, the file is not `%PDF`, the cover no longer reads Version 4.0 January 2023, or the front matter now carries a contractor copyright notice (Booz Allen, MITRE, or equivalent). PDF `/Author` personal names are not a contractor copyright. Stop only if the front matter itself carries the notice.
- D3: reconstruction rule stays the live pack's rule. Synthesized reference notes. Short defined terms may be kept. No long verbatim passages. No PDF page images. CMMI for Development v1.2 definitions are paraphrased, never copied. The page 3 footnote is named, not reproduced as the definition. Tables 1 through 6 are January 2023 policy snapshots, illustrative, not live authority. AMS policy sections named on the FAST page (Section 2.1.6) are named, not quoted, and not rebuilt.
- D4: other FAA packs are out. Do not edit `packs/faa-sem/`, `packs/faa-req-handbook/`, `packs/faa-system-safety/`, `packs/faa-hf-std/`, `packs/faa-rma/`, `packs/faa-8110-49/`, or `packs/faa-std-025/`. Do not edit their catalog rows, NOTICE blocks, or watchlist rows. `mrl-deskbook` and the other remaining drift rows stay out. `nasa-risk` is already rebuilt. Do not reopen it. `nasa-pra` stays mis-pinned.
- D5: chapter count is one file per numbered section 1, 2, and 3, with SASP (section 3.1) as its own chapter, plus a split of section 3.3 through 3.5 only if one file would bury a decision-point table, plus no file whose only job is an appendix. Expected 4 files: ch01 section 1 (including 1.3.2 shift-left), ch02 section 2, ch03 section 3.1 (SASP), ch04 sections 3.2 through 3.5. Contents list wins over the provisional table. Floor 3, ceiling 6. Appendices A, B, and C are not chapters. Do not keep `ch07-faa-ams-vv-acronyms-checklists-definitions.md`. Do not write one file per table.
- D6: support files stay three: `glossary.md`, `cheatsheet.md`, `patterns.md`. They are not in the 3 to 6 count. Glossary absorbs Appendix A acronyms and Appendix C definitions (paraphrased; CMMI-sourced terms named, not copied). Cheatsheet absorbs the decision-point rules and the plan/perform/report/decide pipeline. Patterns absorbs shift-left and independence moves the guideline states. No fourth support file.
- D7: classification churn is delete-then-append, not a migration. Remove every `faa-ams-vv` row from `docs/classification-rules.json` `assignments` and from `docs/capability-pack-map-note-overrides.json` `notes` (10 rows each today: 7 chapters + 3 support). Append one `is_support: false` row per new chapter file and one `is_support: true` row per surviving support file. Same keys in both files. Cluster `Verification` or `Validation`, both already in `cluster_names`. A chapter that is mostly decision-point tables may use `Governance, Reviews, Gates & Control Points` if that fit is better. Do not invent a cluster. Bump the `741` literal in `tooling/generate_capability_map.py` (docstring line 9 and the three comparison sites at lines 195, 203, and 204) to `741 - 7 + N`, where N is the new chapter-file count. Support rows do not change the total: 3 removed, 3 added. Expected total `734 + N`. At the D5 expected N of 4, total is 738. `map_version` stays `1.22.0`. `generated_on` on both JSON files moves to the execution date.
- D8: counts that measure packs or skills do not change. Pack count stays 74. Skill count stays 83. FAA family chip stays 8. `catalog.json` `updated` stays `2026-10-14`. Do not bump `RELEASE-INFO.txt` or either plugin `version`. Do not add a skill path. The slug already exists in both plugin manifests.
- D9: watchlist `faa-ams-vv` only. Hand-edit `document` to `AMS Lifecycle Verification and Validation Guidelines` (the watch `document` field carries the document title, not the version). Run `python tooling/check_source_watch.py --record faa-ams-vv "<catalog source_version>" <vet-date>` after the catalog row matches, not before. `version` must equal catalog `source_version`. Do not pass a URL. Do not record any other slug. CAUTION: no gate compares watch `version` to catalog `source_version`. The three-surface byte-match (PACK.yaml, catalog row, watchlist) is a manual Testing step. Record only after the catalog row carries the new `source_version`, so the manual diff has a fixed reference.
- D10: backlog slug `source-watch-calibrate-and-wire-2` stays `open`. Evidence cell drops `faa-ams-vv` and states the count is 12, not 13. The remaining list keeps `nasa-pra` and keeps the P58 statement that its watch `version` is a mis-pin of the handbook Version 2.0 onto NASA/SP-2011-3421. Do not delete the row. Do not mark it `done`.
- Pin string, verbatim, in PACK.yaml `source_version`, the catalog `source_version`, and the watchlist `version` once `--record` runs: `Version 4.0 (January 2023)`. If the re-fetch cover date disagrees, stop. Do not rewrite the pin to match a different issue.
- Title, verbatim: `FAA AMS Lifecycle Verification and Validation Guidelines, Version 4.0`. Publisher, verbatim: `FAA`.
- `build.built_on` is the execution date in `YYYY-MM-DD`, not a date copied from this plan's filename. `catalog.json` `"updated"` stays `2026-10-14`.
- `build.source_pages` is 63 unless a re-fetch returns a different page count. `build.chapters` equals the chapter-file count, not 7 and not 63. `build.method` names the 4.0 PDF, not the 2017 extraction.
- `notes` carries the public-domain line, the byte size, the page count, the vet date, the no-copyright-legend finding, the CMMI v1.2 paraphrase-only caution (name the August 2006 footnote, do not copy the definition sentences), the January 2023 snapshot caveat on Tables 1 through 6, and the statement that the PDF does not print a supersession sentence. No URL in `PACK.yaml`.
- `change_indication: "reconstructed as synthesized reference notes"`.
- No `source_url` in PACK.yaml or `catalog.json`. No `http://` or `https://` under `packs/faa-ams-vv/`.
- Chapter body at least 30 lines (`tooling/check_pack_quality.py` `MIN_CHAPTER_LINES`). Topic Index `chNN` tokens in `SKILL.md` resolve to the new chapter files. Frontmatter `name` stays `faa-ams-vv`.
- Catalog row keeps the nine live keys, in order: `slug`, `title`, `publisher`, `source_version`, `license`, `license_tier`, `commercial_use`, `chapters`, `status`. `title` matches PACK.yaml `title`. `source_version` matches PACK.yaml `source_version`. `chapters` matches the new file count. `license` stays the shorter catalog form already on the live row: `Public Domain (US Government work)`. Do not lengthen the catalog cell to the PACK.yaml form. Do not add a key.
- Chapter assignment notes are one sentence each, no em dash, and say the note is from Version 4.0 January 2023. Support-file notes stay short labels, same shape as the three notes being replaced (`Glossary for pack`, `Cheatsheet / quick reference`, `Patterns/practice heuristics`).
- Do not (spec Out and Non-goals, verbatim in substance):
  - Do not edit other FAA packs, their catalog rows, their NOTICE blocks, or their watchlist rows.
  - Do not close `source-watch-calibrate-and-wire-2`. Twelve findings remain.
  - Do not bump a release version. Changelog Unreleased is the record.
  - Do not edit neighbor pack chapters that mention `faa-ams-vv` unless they pin Version 3.0 or April 2017.
  - Do not commit the downloaded PDF. It is a vet input, not repo content.
  - Do not bump `RELEASE-INFO.txt`, either plugin `version`, or `catalog.json` `updated`.
  - Do not add a skill path. Do not add a slug. Do not hand-edit generated HTML, `docs/capability-pack-map.json`, or `docs/capability-pack-map.md`.
- Also out: the other 11 drift rows still on the backlog cell after this shrink (nasa-pra, sebok, nasa-se-handbook, nist-ssdf, nist-stat-handbook, dod-rio, nasa-schedule, dodaf, federal-bca, mrl-deskbook, and the standing-drift row the backlog still counts inside 13). A second pack for the appendices, or a chapter per table. Quoting CMMI definition sentences, AMS policy section text, or PDF page images. New validators, new page templates, new licence tiers. GitHub release, plugin publish, or commit. This plan does not authorize those.
- A licence failure, a dead PDF, a cover date that is not Version 4.0 January 2023, a contractor copyright notice in the front matter, or a contents list that will not fit 3 to 6 chapters is a stop-and-report. Do not invent content to fill the gap.
- No task pauses for human input except the D2 stop. Executors do not ask questions. Commit steps are off unless the parent execution mode says commit. Do not push. Do not open a PR.
- Per-task briefs live at `.superpowers/sdd/2026-10-28-rebuild-faa-ams-vv-v4/task-N-brief.md`. The controller writes them at dispatch. This plan does not create those files.

## Codebase context

Post-P58 baseline, re-checked on main at `b019f9c` on 2026-10-28. Precedent for the reconstructed-notes rule and the three support files is the live `packs/faa-ams-vv/` itself, plus the P58 rebuild shape in `docs/superpowers/plans/2026-10-28-rebuild-nasa-risk-handbook-v2.md`. Required content-pack layout is `docs/PACK-SPEC.md`.

- `packs/faa-ams-vv/` today: `PACK.yaml` (title `FAA AMS Lifecycle V&V Guidelines v3.0`, `source_version` `Version 3.0 (April 2017)`, `license` the shorter `Public Domain (US Government work)`, `source_pages: 54`, `chapters: 7`, `built_on: 2026-06-24`), `SKILL.md`, `LICENSE`, `glossary.md`, `cheatsheet.md`, `patterns.md`, and 7 chapter files under `chapters/`. Support files are not chapters. The seven files to delete: `ch01-faa-ams-vv-introduction-and-vv-philosophy.md`, `ch02-faa-ams-vv-implementation-guidance.md`, `ch03-faa-ams-vv-approach-and-early-lifecycle.md`, `ch04-faa-ams-vv-investment-analysis.md`, `ch05-faa-ams-vv-solution-implementation.md`, `ch06-faa-ams-vv-in-service-management.md`, `ch07-faa-ams-vv-acronyms-checklists-definitions.md`.
- `faa-ams-vv` assignment rows today: 7 chapter rows plus 3 support rows (`glossary.md`, `cheatsheet.md`, `patterns.md`). Clusters in use: `Verification` (ch01, ch02, ch03, ch05, ch07, and all three support files) and `Validation` (ch04, ch06). Both names already exist in `cluster_names`, as does `Governance, Reviews, Gates & Control Points`. Do not invent one. Overrides are a parallel list, same `(pack, chapter)` keys, one `note` string each. Live support notes, which Task 3 keeps as the short-label shape: `Glossary for pack`, `Cheatsheet / quick reference`, `Patterns/practice heuristics`. `tooling/check_classification_rules.py` requires one `is_support: false` row per `packs/<slug>/chapters/*.md` and rejects an assignment whose chapter file is gone. There is no removal API. A rebuild deletes the old `faa-ams-vv` rows from both JSON files and appends the new ones. Key sets must match after the edit.
- `tooling/generate_capability_map.py` refuses any notes length other than 741 (line 9 docstring, line 195 `len(notes) != 741`, line 203 `if len(notes) != 741`, line 204 error string `notes length must be 741`). Those four literals must move, or the generator rejects the new note file. Do not hand-edit `docs/capability-pack-map.json` or `docs/capability-pack-map.md`. `map_version` on both JSON files is `1.22.0` and stays. `generated_on` on both is `2026-10-28` today and must move to the execution date or the fidelity check fails. Generator invocation: `python tooling/generate_capability_map.py --generated-on YYYY-MM-DD --sync-md`.
- Watchlist today, `last_checked` 2026-10-12. `faa-ams-vv` `document` is `Version 3.0 (April 2017)`. `version` already carries `Version 4.0 (January 2023)`. `document` is what the pack was built from. `version` is what the watch last saw. After the rebuild, `document` must be hand-edited to `AMS Lifecycle Verification and Validation Guidelines`. `python tooling/check_source_watch.py --record SLUG VERSION DATE` rewrites `version` and `last_checked` on an existing slug. It does not create a row. It does not write `document`. Entry keys, in order: `slug`, `publisher`, `document`, `version`, `last_checked`, `hint`.
- `nasa-pra` watch `version` is `NASA Risk Management Handbook Version 2.0 (November 2024; NASA/SP-20240014019 Part 1, NASA/SP-20240014326 Part 2)`. That string does not describe SP-2011-3421. P58 recorded the wrongness and left the row. Do not edit it. Record the same sentence in the backlog evidence cell.
- Registration surfaces that name the 2017 pin and must move with the pack: `catalog.json` faa-ams-vv row (nine keys, same shape; do not change top-level `updated`), `README.md` catalogue row (line 164, `live (7 chapters)` must become the new count, title must become the new title), `SKILLS.md` faa-ams-vv description (line 50), `NOTICE` `[pack: faa-ams-vv]` block (starts at the marker, ends before `[pack: gao-agile]`), `packs/faa-ams-vv/LICENSE`, `packs/faa-ams-vv/SKILL.md`. Generated pages (`docs/packs/faa-ams-vv/index.html`, `docs/packs.html`, `docs/sitemap.xml`) come from generators. Do not hand-edit them.
- `tooling/gen_pack_pages.py --only faa-ams-vv` rewrites that pack page and always rewrites `docs/sitemap.xml` from the full live catalog (help text at the `--only` flag: any run leaves pages and sitemap consistent). It does not truncate the sitemap. Finish with `python tooling/gen_packs_page.py` for `docs/packs.html`. Do not hand-edit generated HTML.
- Surfaces that count packs, skills, or FAA family size do not move. Pack count stays 74. Skill count stays 83. `SKILLS.md` line 9 stays `74 packs (+8 signposts, +1 orchestrator)`. `docs/index.html` `FAA · 8` chip stays 8. `docs/products/website/01-jgs-se-knowledge-packs.yaml` `FAA (8)` stays 8. `README.md` `packs-74` badge stays. Plugin `version` fields stay. `RELEASE-INFO.txt` stays. Do not edit `.claude-plugin/plugin.json` or `.cursor-plugin/plugin.json`. The slug is already in both. Do not edit `.github/workflows/validate.yml`.
- `/se` already routes verification and validation to `faa-ams-vv`, and the FAA row already names it (`packs/se/SKILL.md` lines 80, 81, 127, 143, 144, 146). No new slug. No new routing row. Description text may name Version 4.0. Do not add or remove packs on those rows. Today those rows do not say 2017 or Version 3.0. Leave them.
- `docs/superpowers/backlog.md` line 101, slug `source-watch-calibrate-and-wire-2`, status `open`. Evidence names 13 drift findings after the P58 shrink, `faa-ams-vv` among them. This cut removes `faa-ams-vv` from that evidence list and from the count. It does not close the row. Twelve findings remain.
- `CHANGELOG.md` already has `## [Unreleased]`, `### Added`, and `### Changed` (the P58 `nasa-risk` bullet). Add one bullet under the existing `### Changed`. Do not add an `## [x.y.z]` heading. Do not edit `## [1.23.0]`.
- Neighbors (`faa-sem` and the `/se` FAA row) cite this pack as the AMS V&V overlay. Leave those sentences unless they pin "Version 3.0" or "April 2017". A version pin inside another pack is a one-line edit. A doctrine sentence is not.
- `sources/` is gitignored. The PDF and the text extract stay untracked. `git ls-files sources/` must stay empty.
- Catalog `license` on the live faa-ams-vv row is `Public Domain (US Government work)`. PACK.yaml `license` today is the same shorter string. This cut lengthens PACK.yaml to the D2 form `Public Domain (US Government work, 17 U.S.C. 105)`, matching the P58 nasa-risk split. Keep the catalog cell short. Do not lengthen it.

## Research

research: https://fast.faa.gov/AMSBB_Verification_Validation.cfm
research: https://fast.faa.gov/docs/vandvguidelines.pdf

Page-level pin from the spec, not re-verified by this plan. Task 1 re-vets it.

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

Third-party text that is present, and must stay paraphrased. Page 3 footnote on the verification and validation definitions, quoted here so the rebuild does not drop it:

> Note: Capability Maturity Model Integration (CMMI) for Development, Version 1.2, Carnegie Mellon Software Engineering Institute, Pittsburgh, PA, August 2006.

The same page states the definitions are consistent with CMMI and that GAO uses CMMI for quality audits. CMMI and CMMI for Development are marked registered. That is the live pack's paraphrase-only caution. Carry it forward. Do not copy the definition sentences that sit under the footnote.

Contents (page i), top-level numbered sections only. Subsections stay inside the parent chapter except SASP, which the V4 list gives its own chapter. Appendices are not chapters.

1. Introduction (1.1 Scope, 1.2 V&V Terms and Definitions, 1.3 V&V Philosophy, including 1.3.1 V-Model Implementation and 1.3.2 Agile Acquisition/Shift-Left Principles In V&V)
2. V&V Implementation Guidance (2.1 Planning, 2.2 Performing, 2.3 Reporting, 2.4 Decision Support)
3. V&V Approach in the AMS Lifecycle (3.1 Service Analysis & Strategic Planning, 3.2 Concept and Requirements Definition, 3.3 Investment Analysis with 3.3.1 Initial and 3.3.2 Final, 3.4 Solution Implementation, 3.5 In-Service Management)

Appendix A Acronyms. Appendix B Verification and Validation Checklists (PRD, ISPD, PMP, APB). Appendix C Definitions. Figures 1 through 5. Tables 1 through 6, one per lifecycle slice in section 3.

Grouping note versus the 3.0 pack (a pack-grouping difference, not a document novelty: the 3.0 PDF already carries section 1.3.2 Agile Acquisition / shift-left and section 3.1 Service Analysis & Strategic Planning as its own Table 1 slice): the current pack folds early lifecycle into one chapter and starts its Table-1 chapter with SASP and CRD together. The V4 rebuild follows the V4 contents list instead, which gives SASP its own chapter. Contents-list wins. Do not keep the 3.0 grouping where the V4 list disagrees.

Spec fetch on 2026-10-28: FAST page HTTP 200 HTML, PDF HTTP 200 `Content-Type: application/pdf`, `%PDF-1.3`, `Content-Length: 2700181`. Last-Modified `Thu, 17 Apr 2025 15:42:43 GMT` is a host cache stamp, not the cover date. Task 1 records the execution-time byte size and page count. The spec numbers are a check, not a lock, except the D2 stop conditions.

Provisional chapter map, discarded where the PDF contents list disagrees. SASP is its own file because the V4 list gives section 3.1 its own slice:

| File | Draws from | Job |
|---|---|---|
| ch01-introduction-and-vv-philosophy.md | Section 1 | Scope, work-product/component/product terms, verify-vs-validate (paraphrased, CMMI footnote named), V&V vs QA, V-model, agile acquisition and shift-left. |
| ch02-implementation-guidance.md | Section 2 | Plan, perform, report, decide. Work-product methods vs product/component methods. Independence. Report minimum content. Decision support. |
| ch03-service-analysis-and-strategic-planning.md | Section 3.1 | SASP only. Table 1. Front-loaded security and the early management documents that Table 1 binds. |
| ch04-lifecycle-after-sasp.md | Sections 3.2 through 3.5 | Concept and Requirements Definition, initial and final investment analysis, solution implementation, in-service management. Tables 2 through 6. DT/OT/IOA stays here, not a separate chapter. |

If sections 3.2 through 3.5 will not fit one file without burying a table, split into ch04 (CRD and investment analysis) and ch05 (solution implementation and in-service). That split is allowed inside the ceiling. It is not the default.

## File map

Create (untracked; do not commit):

- `sources/faa-ams-vv/vandvguidelines.pdf`
- `sources/faa-ams-vv/body.txt`

Create (tracked):

- `packs/faa-ams-vv/chapters/chNN-<slug>.md` (3, 4, 5, or 6 files, frozen in Task 1; expected 4)

Modify:

- `packs/faa-ams-vv/PACK.yaml`
- `packs/faa-ams-vv/LICENSE`
- `packs/faa-ams-vv/SKILL.md`
- `packs/faa-ams-vv/glossary.md`
- `packs/faa-ams-vv/cheatsheet.md`
- `packs/faa-ams-vv/patterns.md`
- `catalog.json` (faa-ams-vv row only; `"updated"` untouched)
- `docs/source-watchlist.json` (faa-ams-vv `document`, then `--record` rewrites `version` and `last_checked`)
- `SKILLS.md` (faa-ams-vv description only; line 9 count stays)
- `NOTICE` (`[pack: faa-ams-vv]` block only)
- `README.md` (faa-ams-vv catalogue row title and chapter count only)
- `docs/classification-rules.json` (delete 10 faa-ams-vv rows, append `N + 3`)
- `docs/capability-pack-map-note-overrides.json` (same keys)
- `tooling/generate_capability_map.py` (four `741` literals become `741 - 7 + N`)
- `docs/capability-pack-map.json` and `docs/capability-pack-map.md` (regenerated)
- `docs/packs/faa-ams-vv/index.html`, `docs/packs.html`, `docs/sitemap.xml` (regenerated)
- `CHANGELOG.md` (one `[Unreleased]` Changed bullet)
- `docs/superpowers/backlog.md` (evidence cell and summary cell on line 101 only)

Delete:

- the seven chapter files listed in Codebase context

Do not modify: other FAA packs, `packs/nasa-risk/`, `packs/nasa-pra/`, `packs/se/SKILL.md`, `.claude-plugin/plugin.json`, `.cursor-plugin/plugin.json`, `RELEASE-INFO.txt`, `docs/index.html`, `docs/products/website/01-jgs-se-knowledge-packs.yaml`, `docs/LICENSING.md`, `.github/workflows/validate.yml`, neighbor pack chapters.

---

### Task 1: Vet the PDF, freeze the chapter map, delete the seven old chapters

**Gate:** gate-enforced (spec D2 stop, contents-list freeze).

**Files:**
- Create: `sources/faa-ams-vv/vandvguidelines.pdf` (untracked)
- Create: `sources/faa-ams-vv/body.txt` (untracked)
- Delete: the seven `packs/faa-ams-vv/chapters/ch*.md` files listed in Codebase context

**Interfaces:**
- Consumes: the research PDF URL and the D2 stop conditions.
- Produces: `CHAPTER_COUNT` (integer 3, 4, 5, or 6), `PAGE_COUNT` (integer), `BYTE_SIZE` (integer), `VET_DATE` (`YYYY-MM-DD`), the frozen basename list `chNN-kebab-title.md` with the printed page range that feeds each file, and a one-line front-matter finding (`no contractor copyright notice` or the stop). Tasks 2, 3, and 4 copy those values. They do not re-decide them. `SOURCE_PAGES` is `PAGE_COUNT`.

**Model:** standard

Per-task brief: `.superpowers/sdd/2026-10-28-rebuild-faa-ams-vv-v4/task-1-brief.md`

- [ ] **Step 1: Record the execution date and re-fetch the PDF**

```bash
python -c "import datetime; print(datetime.date.today().isoformat())"
```

Call that date `VET_DATE`. It must be `YYYY-MM-DD`. It is `build.built_on`. Do not hard-code `2026-10-28` unless that is the date the command prints.

Download the PDF. Do not `pip install` anything. Do not fetch the bare `https://fast.faa.gov/vandvguidelines.pdf` path. That URL returns HTML.

```bash
mkdir -p sources/faa-ams-vv
curl -fsSL -o sources/faa-ams-vv/vandvguidelines.pdf "https://fast.faa.gov/docs/vandvguidelines.pdf"
python -c "
import hashlib, pathlib
data = pathlib.Path('sources/faa-ams-vv/vandvguidelines.pdf').read_bytes()
print('bytes', len(data), 'head', data[:8], 'sha256', hashlib.sha256(data).hexdigest())
"
```

Expected: head starts with `b'%PDF'`. Record `BYTE_SIZE`. The spec's 2,700,181 is a check, not a lock. A different size is not a stop if the file is a PDF and D2 holds.

Extract text. Prefer `pdftotext -layout` if `command -v pdftotext` succeeds. Otherwise use an already-installed reader (`pypdf` or `fitz`). Do not `pip install` a PDF library. If no reader is available, stop and report. Write the extract to `sources/faa-ams-vv/body.txt`. Record `PAGE_COUNT` from the reader, not from the spec. The spec's 63 is a check, not a lock.

Confirm from the PDF text, not from the spec:

- Cover reads Version 4.0 and January 2023. If the cover date disagrees, stop. Do not rewrite the pin.
- Front matter has no contractor copyright notice (Booz Allen, MITRE, or equivalent). PDF `/Author` personal names are not that notice. Record the finding for Task 2 `notes`.
- The PDF does not print a supersession sentence. Do not invent one. The 2026-10-12 watch line "stated supersedes" stays unverified.
- The page 3 CMMI footnote is present (CMMI for Development, Version 1.2, August 2006). If it is gone, still carry the paraphrase caution. Do not copy definition sentences that sit under the footnote.

Stop and report, without writing chapter prose and without deleting the old chapters, if any of these hold:

- The PDF URL is dead, or the fetch is not HTTP 200.
- The file is not a PDF (`%PDF` missing).
- The cover does not read Version 4.0 January 2023.
- The front matter carries a contractor copyright notice.

The 2026-10-28 spec fetch is not a substitute for this re-fetch.

- [ ] **Step 2: Freeze 3 to 6 chapter titles from the contents list**

Read the contents list in `sources/faa-ams-vv/body.txt` (page i). Produce 3, 4, 5, or 6 rows. Each row has a basename `chNN-kebab-title.md` and the printed page range that feeds it.

Rules:

- The PDF contents list wins over the provisional table in Research.
- One file for section 1, including 1.3.2 shift-left. Do not split shift-left into its own file.
- One file for section 2. Do not split plan, perform, report, and decide into four files.
- Section 3.1 Service Analysis & Strategic Planning (SASP) gets its own chapter. The V4 list gives SASP its own slice. Do not fold SASP back into a CRD chapter the way the 3.0 pack did.
- Sections 3.2 through 3.5 share one file unless that file would bury a decision-point table. The allowed split is ch04 (CRD and investment analysis) and ch05 (solution implementation and in-service). That split is inside the ceiling. It is not the default.
- Appendices A, B, and C are not chapters. Fold acronyms and paraphrased definitions into `glossary.md` in Task 2. Fold checklist use into `cheatsheet.md`. Do not write a chapter whose only job is the acronym, checklist, or definition list.
- Do not write one file per table. Tables 1 through 6 stay inside the chapter that owns their lifecycle slice.
- Subsections stay inside the parent chapter, except the SASP split above.
- Floor 3, ceiling 6. If the body cannot be covered in 3 to 6 chapters without inventing a theme, stop and report the contents list. Do not write a seventh chapter. Do not delete the old chapters.

Basenames must match `^ch[0-9]{2}-[a-z0-9-]+\.md$`. Expected outcome, discarded if the list disagrees:

- `ch01-introduction-and-vv-philosophy.md` (section 1)
- `ch02-implementation-guidance.md` (section 2)
- `ch03-service-analysis-and-strategic-planning.md` (section 3.1, SASP)
- `ch04-lifecycle-after-sasp.md` (sections 3.2 through 3.5)

Save the frozen list in the executor notes that Tasks 2, 3, and 4 will read. Call the file count `CHAPTER_COUNT`. Call `SOURCE_PAGES` = `PAGE_COUNT`.

- [ ] **Step 3: Delete the seven old chapter files**

Only after Steps 1 and 2 pass. Do not delete if the vet stopped.

```bash
rm -f \
  packs/faa-ams-vv/chapters/ch01-faa-ams-vv-introduction-and-vv-philosophy.md \
  packs/faa-ams-vv/chapters/ch02-faa-ams-vv-implementation-guidance.md \
  packs/faa-ams-vv/chapters/ch03-faa-ams-vv-approach-and-early-lifecycle.md \
  packs/faa-ams-vv/chapters/ch04-faa-ams-vv-investment-analysis.md \
  packs/faa-ams-vv/chapters/ch05-faa-ams-vv-solution-implementation.md \
  packs/faa-ams-vv/chapters/ch06-faa-ams-vv-in-service-management.md \
  packs/faa-ams-vv/chapters/ch07-faa-ams-vv-acronyms-checklists-definitions.md
python -c "
import pathlib
left = sorted(p.name for p in pathlib.Path('packs/faa-ams-vv/chapters').glob('*.md'))
assert left == [], left
print('old chapters gone')
"
git check-ignore -v sources/faa-ams-vv/vandvguidelines.pdf
git ls-files sources/
```

Expected: `old chapters gone`, the ignore rule matches the PDF, and `git ls-files sources/` is empty. Do not commit the PDF or the extract.

---

### Task 2: Write the new chapters and rebuild SKILL.md, PACK.yaml, LICENSE, glossary, cheatsheet, patterns

**Gate:** gate-enforced (validate_pack, check_pack_quality, URL scan, 14-gram scan, CMMI-caveat scan).

**Files:**
- Create: `packs/faa-ams-vv/chapters/chNN-<slug>.md` (the frozen list from Task 1)
- Modify: `packs/faa-ams-vv/PACK.yaml`
- Modify: `packs/faa-ams-vv/LICENSE`
- Modify: `packs/faa-ams-vv/SKILL.md`
- Modify: `packs/faa-ams-vv/glossary.md`
- Modify: `packs/faa-ams-vv/cheatsheet.md`
- Modify: `packs/faa-ams-vv/patterns.md`
- Read: `sources/faa-ams-vv/body.txt` (do not commit)

**Interfaces:**
- Consumes: frozen basenames, page ranges, `CHAPTER_COUNT`, `SOURCE_PAGES`, `BYTE_SIZE`, `PAGE_COUNT`, `VET_DATE`, and the front-matter finding from Task 1.
- Produces: chapter files whose basenames later tasks copy into classification rows, with the `.md` suffix. SKILL.md Topic Index `chNN` tokens must match those basenames. `PACK.yaml` `source_version` is the string Task 3 copies into the catalog row and Task 3 passes to `--record`: `Version 4.0 (January 2023)`. `PACK.yaml` `title` is the string Task 3 copies into the catalog `title`.

**Model:** standard

Per-task brief: `.superpowers/sdd/2026-10-28-rebuild-faa-ams-vv-v4/task-2-brief.md`

- [ ] **Step 1: Write `packs/faa-ams-vv/PACK.yaml`**

Replace `VET_DATE`, `SOURCE_PAGES`, `CHAPTER_COUNT`, `BYTE_SIZE`, and `PAGE_COUNT` with the values from Task 1. `CHAPTER_COUNT` is 3, 4, 5, or 6. `SOURCE_PAGES` is the re-fetch page count, 63 only if the reader returned 63.

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
build:
  method: "Synthesized from FAA AMS Lifecycle Verification and Validation Guidelines Version 4.0, vetted on VET_DATE. Not adapted from the 2017 extraction."
  source_pages: SOURCE_PAGES
  chapters: CHAPTER_COUNT
  built_on: "VET_DATE"
notes: >
  US Government work, 17 U.S.C. 105. Public domain in the United States.
  No attribution duty. Courtesy attribution only. FAA does not endorse
  this pack. PDF BYTE_SIZE bytes, PAGE_COUNT pages. Vetted on VET_DATE.
  The PDF prints no copyright legend and no contractor copyright notice.
  The 2026-10-12 watch claim that the PDF states a supersession is
  unverified: the file does not print a supersession sentence. Do not
  quote one. CMMI for Development, Version 1.2 (Carnegie Mellon Software
  Engineering Institute, August 2006) is named on the page 3 footnote.
  Definitions drawn from that model are paraphrased and never copied.
  Tables 1 through 6 are January 2023 policy snapshots, illustrative, not
  live authority. AMS policy sections named on the FAST page are named,
  not quoted, and not rebuilt. Source identification and the
  reconstructed-notes statement are in packs/faa-ams-vv/LICENSE.
change_indication: "reconstructed as synthesized reference notes"
```

No `source_url` key. No URL anywhere in the file. `source_pages` and `chapters` are bare integers. Mandatory fields above `build:` stay column-0 scalars. The YAML parser reads only column-0 `key: value` lines and skips folded `>` blocks. Do not invent a copyright legend the PDF does not print. Do not invent a supersession quote. The `notes` block is the D2 and D3 manifest. The CMMI sentence must survive. A rebuild that drops it fails Task 4.

- [ ] **Step 2: Write `packs/faa-ams-vv/LICENSE`**

Replace the 2017 identification. Keep the existing section order. No download URL, same rule as `docs/LICENSING.md`. Keep both caveats. Move the snapshot date to January 2023.

```text
faa-ams-vv pack: content licence
=================================

This pack is derived from:
FAA AMS Lifecycle Verification and Validation Guidelines
Federal Aviation Administration (FAA), Version 4.0 (January 2023)

Source licence: Public Domain (US Government work, 17 U.S.C. 105) (tier 1, see ../../docs/SOURCE-VETTING.md)
No source-material download link is published (see ../../docs/LICENSING.md).

This source work is a work of the United States Government, prepared by the FAA, and
is therefore NOT subject to copyright protection in the United States (17 U.S.C. 105).
It is in the public domain: anyone may reproduce, transform, and redistribute it for
any purpose, including commercially, without permission.

The pin was verified on VET_DATE: BYTE_SIZE bytes, PAGE_COUNT pages.
The PDF prints no copyright legend and no contractor copyright notice.
The file does not print a supersession sentence. Do not quote one.

Attribution to the FAA is provided as a courtesy (see the repository NOTICE), not a legal
obligation. The FAA does not endorse this pack or its authors.

1. CMMI definitions (third-party copyright). The source guideline draws its
   formal definitions of verification and validation from CMMI for
   Development, Version 1.2 (Carnegie Mellon Software Engineering Institute,
   August 2006), a separately copyrighted process model. This pack PARAPHRASES
   those concepts and reproduces NO verbatim CMMI text. Any CMMI wording
   should be cited to SEI, not copied from this pack.

2. Policy-snapshot caveat. The source's V&V phase tables (Tables 1-6) reflect
   FAA AMS policy as of January 2023. Current FAA phase guidance supersedes
   them. Treat table content as illustrative, not live authority.

3. No third-party material reproduced. This pack contains only synthesized,
   paraphrased reference notes. No source figures, tables, or extended verbatim
   passages.

NOTE: this file governs the CONTENT of the pack. The repository tooling is licensed
separately under the MIT licence (see ../../LICENSE).
```

Replace `VET_DATE`, `BYTE_SIZE`, and `PAGE_COUNT` with Task 1 values. No `http://` or `https://` in the file. No `April 2017` in the file.

- [ ] **Step 3: Write one chapter file per frozen row**

For each frozen row, write `packs/faa-ams-vv/chapters/<basename>`. Open with a `Sources:` line naming the printed page range. Then an H1 equal to the working title. Then prose of at least 30 lines.

Synthesis rules:

- Synthesize. Do not paste a run of more than one source sentence. A short defined term may be kept and marked as a defined term.
- Do not copy tables as reconstructed shall-lists. Describe the decision rule in prose.
- Name the CMMI for Development v1.2 footnote where the page range names it. Do not copy the definition sentences that sit under it. Say the definitions are paraphrased.
- Name AMS policy sections the page range names (including Section 2.1.6 if the range names it). Do not quote their clause text. Do not rebuild them.
- Tables 1 through 6 are January 2023 snapshots. Say so in the chapter that uses them. Do not present a table cell as current FAA authority.
- Do not embed page images. Do not invent a supersession sentence.
- Ground every claim in the page range for that chapter. Do not borrow another chapter's range to fill length.
- Chapter section shape, in order, when the source supports the heading: `Core Idea`, `Frameworks Introduced`, `Key Concepts`, `Mental Models`, `Anti-patterns` (only if the source states a refusal), `Key Takeaways`, `Connects To`. Skip a heading the page range does not support. Do not invent a framework the PDF does not contain.
- The SASP chapter covers section 3.1 only. Do not pull CRD rows into it to fill length.
- No `http://` or `https://` in any chapter.

If a frozen row's page range has no usable prose, stop and report. Do not write a stub under 30 lines.

- [ ] **Step 4: Rewrite the three support files**

`glossary.md`: absorb Appendix A acronyms and Appendix C definitions. Alphabetical. Each entry names the `chNN` that uses it. CMMI-sourced terms are paraphrased and marked as paraphrased. No URLs. This file keeps an `is_support: true` row in Task 3. It is not a chapter.

`cheatsheet.md`: absorb the plan/perform/report/decide pipeline, the decision-point rules, and how Appendix B checklists (PRD, ISPD, PMP, APB) are used. Prose, not copied page images. Mark Tables 1 through 6 as January 2023 snapshots. No URLs. Support row, not a chapter.

`patterns.md`: absorb shift-left and independence moves the guideline states. No URLs. Support row, not a chapter.

No fourth support file. Do not write a chapter whose only job is the acronym, checklist, or definition list.

- [ ] **Step 5: Rewrite `packs/faa-ams-vv/SKILL.md`**

Frontmatter `name` stays `faa-ams-vv`. Description names Version 4.0 January 2023, states the verify-vs-validate split, the three tiers, decision-point-gated V&V across the AMS lifecycle including shift-left, and keeps the existing limit. It is FAA acquisition V&V doctrine, not a general SE process model, not a requirements manual, and not a test-design textbook. CMMI v1.2 stays named and paraphrased. Surrounding AMS lifecycle stays a pointer to `faa-sem`. Phase tables are January 2023 snapshots.

```yaml
---
name: faa-ams-vv
description: "Knowledge pack synthesized from FAA AMS Lifecycle Verification and Validation Guidelines, Version 4.0 (January 2023): verify-vs-validate, the three tiers, decision-point-gated V&V across the AMS lifecycle, and shift-left. SCOPE LIMITS: single-source (the January 2023 guidelines); FAA acquisition V&V doctrine, not a general SE process model, not a requirements manual, and not a test-design textbook; CMMI for Development v1.2 named and paraphrased, never copied; surrounding AMS lifecycle is faa-sem; phase tables are January 2023 snapshots, not live authority; reconstructed reference notes, not FAA guidance, and no FAA endorsement."
---
```

Body order:

1. H1: `FAA AMS Lifecycle Verification and Validation Guidelines, Version 4.0`
2. A `**Source:**` line naming the public-domain status, January 2023, and a relative link `[LICENSE](LICENSE)`. No absolute URL. No download URL.
3. `## When to use` then, on the next line, `**Prerequisites:**` none, plain Markdown. Then one paragraph: use this skill for questions about verification and validation across the FAA AMS lifecycle. It does not cover the surrounding AMS lifecycle. That stays in `faa-sem`.
4. `## How to use this skill`: four bullets. With no arguments, read Core Frameworks. For a topic, use the Topic Index. For a lifecycle question, use the Chapter Index. For a term, use `glossary.md`. For a decision rule, use `cheatsheet.md`. For a shift-left or independence move, use `patterns.md`.
5. `## Core Frameworks & Mental Models`: two to four subsections drawn only from the PDF (verify versus validate, the three tiers, plan/perform/report/decide, decision-point-gated V&V, shift-left). Do not invent a framework the PDF does not contain. Do not keep a 2017-only framing unless Version 4.0 still states it.
6. `## Chapter Index`: one line per frozen chapter, linking `chapters/<basename>`.
7. `## Topic Index`: keyword lines whose `chNN` tokens match the frozen basenames. Cover verify versus validate, the three tiers, shift-left, SASP, and the later lifecycle slices, plus any extra top-level section Task 1 kept. Every `chNN` token must resolve to a file `check_pack_quality.py` can see.
8. `## Supporting Files`: `glossary.md`, `cheatsheet.md`, and `patterns.md`, one line each.
9. `## Scope & Limits`: source version and `VET_DATE`; Version 4.0 only; CMMI v1.2 paraphrased, not copied; phase tables are January 2023 snapshots; surrounding AMS lifecycle is `faa-sem`; not official FAA guidance.

No `http://` or `https://` in the file. No `April 2017` and no `Version 3.0` in the file. The CMMI sentence must survive.

- [ ] **Step 6: Run the pack gates, the CMMI-caveat scan, and the 14-gram scan**

```bash
python tooling/validate_pack.py packs/faa-ams-vv
python tooling/check_pack_quality.py packs/faa-ams-vv
python -c "
import pathlib
root = pathlib.Path('packs/faa-ams-vv')
bad = []
cmmi_files = []
for p in root.rglob('*'):
    if not p.is_file():
        continue
    text = p.read_text(encoding='utf-8')
    if 'https://' in text or 'http://' in text:
        bad.append(str(p))
    if 'April 2017' in text or 'Version 3.0' in text:
        bad.append('old-pin ' + str(p))
    if 'CMMI' in text:
        cmmi_files.append(p.name)
need = {'PACK.yaml', 'LICENSE', 'SKILL.md'}
missing = need - set(cmmi_files)
assert not missing, missing
assert not bad, bad
n = len(list((root / 'chapters').glob('*.md')))
assert 3 <= n <= 6, n
print('pack clean', n, 'chapters')
"
```

Expected: `validate_pack.py` exits 0, `check_pack_quality.py` prints `PASS  faa-ams-vv` and exits 0, and the scan prints `pack clean` with the Task 1 count. `NOTICE` is not in this scan. Task 3 writes that block and Task 4 checks the CMMI caveat there.

14-gram scan against the extract. Zero contiguous runs of 18 or more words. A short defined term is not a run. The CMMI footnote sentence is a named citation, not a passage to copy. If the scan hits that sentence inside a chapter, rewrite it as a paraphrase that names the model and the date.

```bash
python -c "
import pathlib, re
def words(text):
    return re.findall(r\"[A-Za-z][A-Za-z0-9'-]*\", text.lower())
def grams(seq, n):
    return {' '.join(seq[i:i+n]) for i in range(max(0, len(seq) - n + 1))}
src_seq = words(pathlib.Path('sources/faa-ams-vv/body.txt').read_text(encoding='utf-8', errors='replace'))
src_g = grams(src_seq, 18)
hits = []
for p in sorted(pathlib.Path('packs/faa-ams-vv/chapters').glob('*.md')):
    seq = words(p.read_text(encoding='utf-8'))
    for i in range(len(seq) - 17):
        g = ' '.join(seq[i:i+18])
        if g in src_g:
            hits.append((p.name, g[:80]))
            break
assert not hits, hits
print('14-gram scan clean')
"
```

Expected: `14-gram scan clean`. If a hit prints, rewrite that sentence. Do not delete the source sentence from the extract to make the scan pass.

If a chapter is under 30 lines, add synthesis from its own page range. Do not borrow another chapter's range.

---

### Task 3: Version-surface registration

**Gate:** gate-enforced (classification-rules, capability-map, source-watch, catalog row, three-surface byte-match).

**Files:**
- Modify: `catalog.json` (faa-ams-vv row only)
- Modify: `docs/classification-rules.json`
- Modify: `docs/capability-pack-map-note-overrides.json`
- Modify: `tooling/generate_capability_map.py` (four `741` literals only)
- Modify: `docs/source-watchlist.json` (faa-ams-vv `document`, then `--record`)
- Modify: `NOTICE` (`[pack: faa-ams-vv]` block only)
- Modify: `CHANGELOG.md` (one Changed bullet)
- Modify: `SKILLS.md` (faa-ams-vv description only)
- Modify: `README.md` (faa-ams-vv title and chapter-count cells only)
- Modify: `docs/superpowers/backlog.md` (line 101 summary and evidence cells only)
- Regenerated, do not hand-edit: `docs/capability-pack-map.json`, `docs/capability-pack-map.md`, `docs/packs/faa-ams-vv/index.html`, `docs/packs.html`, `docs/sitemap.xml`

**Interfaces:**
- Consumes: `CHAPTER_COUNT`, `VET_DATE`, frozen basenames with the `.md` suffix, and the pin strings from Task 2 (`source_version` `Version 4.0 (January 2023)`, `title` as written in PACK.yaml).
- Produces: notes length `741 - 7 + CHAPTER_COUNT` (738 when `CHAPTER_COUNT` is 4), matching assignment length, watchlist `version` equal to catalog `source_version`, and a regenerated map. Later tasks do not hand-edit the generated JSON, Markdown, or HTML.

**Model:** standard

Per-task brief: `.superpowers/sdd/2026-10-28-rebuild-faa-ams-vv-v4/task-3-brief.md`

- [ ] **Step 1: Replace the catalog faa-ams-vv row**

Edit the existing `faa-ams-vv` object in `catalog.json` `packs`. Do not add a row. Do not change `"updated"` (`2026-10-14`). Do not add `source_url`. Do not touch any other pack object. Keys stay in this order:

```json
{
  "slug": "faa-ams-vv",
  "title": "FAA AMS Lifecycle Verification and Validation Guidelines, Version 4.0",
  "publisher": "FAA",
  "source_version": "Version 4.0 (January 2023)",
  "license": "Public Domain (US Government work)",
  "license_tier": 1,
  "commercial_use": true,
  "chapters": CHAPTER_COUNT,
  "status": "live"
}
```

`CHAPTER_COUNT` is the integer from Task 1, not the token. `license` stays the shorter catalog form. Do not lengthen it to the PACK.yaml form. `title` must equal PACK.yaml `title`. `source_version` must equal PACK.yaml `source_version`. Keep JSON valid. Pack count stays 74.

- [ ] **Step 2: Delete every faa-ams-vv row, then append the new set**

Count before editing. Both files must report 10, and both files must report 741.

```bash
python -c "
import json, pathlib
rules = json.loads(pathlib.Path('docs/classification-rules.json').read_text(encoding='utf-8'))
ov = json.loads(pathlib.Path('docs/capability-pack-map-note-overrides.json').read_text(encoding='utf-8'))
ra = [a for a in rules['assignments'] if a['pack']=='faa-ams-vv']
rn = [a for a in ov['notes'] if a['pack']=='faa-ams-vv']
print('assign', len(rules['assignments']), 'faa-ams-vv', len(ra))
print('notes', len(ov['notes']), 'faa-ams-vv', len(rn))
assert len(ra)==10 and len(rn)==10
assert len(rules['assignments'])==741 and len(ov['notes'])==741
assert {a['chapter'] for a in ra} == {a['chapter'] for a in rn}
print('pre-edit ok')
"
```

Expected: `pre-edit ok`. If the counts are not 10 and 741, stop. Do not edit. The arithmetic in this step assumes those counts.

Then delete every object whose `pack` is `faa-ams-vv` from `docs/classification-rules.json` `assignments` and from `docs/capability-pack-map-note-overrides.json` `notes`. Append, in both files, one object per frozen chapter file and one object per surviving support file. Same `pack` and `chapter` in both files. `chapter` is the basename with `.md`.

Assignment object, one per frozen chapter:

```json
{"pack": "faa-ams-vv", "chapter": "chNN-slug.md", "cluster": "Verification", "is_support": false}
```

`cluster` is `Verification` or `Validation`, both already in `cluster_names`. A chapter that is mostly decision-point tables may use `Governance, Reviews, Gates & Control Points` if that fit is better. Do not invent a cluster. SASP (section 3.1) stays `Verification` unless the page range is a validation-only table.

Support assignments, all three, `is_support` true, cluster `Verification`:

```json
{"pack": "faa-ams-vv", "chapter": "glossary.md", "cluster": "Verification", "is_support": true}
{"pack": "faa-ams-vv", "chapter": "cheatsheet.md", "cluster": "Verification", "is_support": true}
{"pack": "faa-ams-vv", "chapter": "patterns.md", "cluster": "Verification", "is_support": true}
```

Note object, one per frozen chapter. One sentence, no em dash, no spaced double hyphen used as a dash, and the sentence says the note is from Version 4.0 January 2023. No URL.

```json
{"pack": "faa-ams-vv", "chapter": "chNN-slug.md", "note": "One sentence from Version 4.0 January 2023 naming what this chapter covers."}
```

Support notes stay short labels, same shape as the three being replaced:

```json
{"pack": "faa-ams-vv", "chapter": "glossary.md", "note": "Glossary for pack"}
{"pack": "faa-ams-vv", "chapter": "cheatsheet.md", "note": "Cheatsheet / quick reference"}
{"pack": "faa-ams-vv", "chapter": "patterns.md", "note": "Patterns/practice heuristics"}
```

Set `generated_on` on both files to `VET_DATE`. Leave `map_version` at `1.22.0`. Do not touch any other pack's rows.

After the edit, both lists have length `741 - 7 + CHAPTER_COUNT`. Support rows do not change the total: 3 removed, 3 added. At the expected `CHAPTER_COUNT` of 4, length is 738. Key sets match.

```bash
python -c "
import json, pathlib
rules = json.loads(pathlib.Path('docs/classification-rules.json').read_text(encoding='utf-8'))
ov = json.loads(pathlib.Path('docs/capability-pack-map-note-overrides.json').read_text(encoding='utf-8'))
ra = [a for a in rules['assignments'] if a['pack']=='faa-ams-vv']
rn = [a for a in ov['notes'] if a['pack']=='faa-ams-vv']
chapters = sorted(p.name for p in pathlib.Path('packs/faa-ams-vv/chapters').glob('*.md'))
content = [a for a in ra if not a['is_support']]
support = sorted(a['chapter'] for a in ra if a['is_support'])
assert sorted(a['chapter'] for a in content) == chapters
assert support == ['cheatsheet.md', 'glossary.md', 'patterns.md']
assert {(a['pack'], a['chapter']) for a in ra} == {(a['pack'], a['chapter']) for a in rn}
assert len(rules['assignments']) == len(ov['notes'])
assert len(rules['assignments']) == 741 - 7 + len(chapters)
assert rules['map_version'] == '1.22.0'
assert ov['map_version'] == '1.22.0'
allowed = {'Verification', 'Validation', 'Governance, Reviews, Gates & Control Points'}
assert {a['cluster'] for a in ra} <= allowed
print('rows', len(rules['assignments']), 'chapters', len(chapters))
"
```

Expected: `rows` equals `734 + CHAPTER_COUNT`, and `chapters` equals `CHAPTER_COUNT`.

- [ ] **Step 3: Move the four 741 literals**

`NEW` is `741 - 7 + CHAPTER_COUNT`. At the expected 4, `NEW` is 738. In `tooling/generate_capability_map.py`, replace `741` at the docstring (line 9), the combined comparison (line 195), the length comparison (line 203), and the error string (line 204). Do not change any other number in the file. Do not change `map_version`.

```bash
python -c "
import pathlib
text = pathlib.Path('tooling/generate_capability_map.py').read_text(encoding='utf-8')
print('741 count', text.count('741'))
"
```

Expected: `741 count 0`. If `741` remains, the generator will reject the new note file. Do not edit the generator beyond those four literals.

- [ ] **Step 4: Regenerate the map and check it**

`generated_on` on both JSON files is already `VET_DATE` from Step 2. Then:

```bash
python tooling/generate_capability_map.py --generated-on VET_DATE --sync-md
python tooling/check_capability_map.py
python tooling/check_classification_rules.py
```

Expected: three exit 0. If the generator reports `notes length must be 741`, Step 3 missed a literal. If a check reports an assignment missing a note, the paired rows disagree. Fix the rows. Do not edit the generator beyond the four literals. Do not hand-edit `docs/capability-pack-map.json` or `docs/capability-pack-map.md`.

- [ ] **Step 5: Hand-edit watchlist document, then record**

CAUTION: no gate compares watch `version` to catalog `source_version`. Record only after Step 1, so the manual diff in Step 8 has a fixed reference.

In `docs/source-watchlist.json`, on the `faa-ams-vv` object only, set `document` to `AMS Lifecycle Verification and Validation Guidelines`. Leave `publisher` as `FAA`. Leave `hint` as `""`. Do not edit any other object. Do not pass a URL.

Then:

```bash
python tooling/check_source_watch.py --record faa-ams-vv "Version 4.0 (January 2023)" VET_DATE
python tooling/check_source_watch.py
```

`VET_DATE` is the Task 1 date, not the token. `--record` rewrites `version` and `last_checked`. It does not write `document`. Expected: `recorded faa-ams-vv` and then `check_source_watch.py` exits 0.

Confirm `nasa-pra` `version` is still the pre-cut mis-pin, byte for byte:

```text
NASA Risk Management Handbook Version 2.0 (November 2024; NASA/SP-20240014019 Part 1, NASA/SP-20240014326 Part 2)
```

If that string changed, restore it. This cut does not repair that row.

- [ ] **Step 6: NOTICE, CHANGELOG, SKILLS.md, README**

`NOTICE`: replace the `[pack: faa-ams-vv]` block only. The block starts at `[pack: faa-ams-vv]` and ends before `[pack: gao-agile]`. Do not edit `[pack: gao-agile]`. Do not edit any other `[pack:]` block. Keep the courtesy-attribution sentence, the no-endorsement sentence, and the CMMI paraphrase caveat. Move the table-snapshot date from April 2017 to January 2023.

```text
[pack: faa-ams-vv]

  Source : FAA AMS Lifecycle Verification and Validation Guidelines, Version 4.0 (January 2023)
  Author : US Federal Aviation Administration (FAA)
  Licence: Public Domain -- US Government work (17 U.S.C. 105)
  Changes: reconstructed as synthesized reference notes (not a reproduction)
  Terms  : public domain, no copyright. CAVEAT: the source guideline draws its core
           verification/validation definitions from CMMI for Development v1.2 (Carnegie
           Mellon SEI, August 2006), a separately copyrighted model, which this pack
           paraphrases and never reproduces verbatim. CMMI text should be cited to SEI,
           not copied. The source's V&V phase tables (Tables 1-6) are policy snapshots as of
           January 2023 and may be superseded by current FAA phase guidance; treat table
           content as illustrative, not live authority. The PDF does not print a supersession
           sentence. Attribution to the FAA is courtesy, not obligation; the FAA does not
           endorse this pack. See packs/faa-ams-vv/LICENSE.
```

The `--` in the Licence line matches the existing NOTICE block shape. It is a field separator, not prose. Do not spread it into other sentences.

`CHANGELOG.md`: under `## [Unreleased]`, the `### Changed` heading already exists (the P58 `nasa-risk` bullet). Add one bullet under that heading. Do not add a second `### Changed`. Do not add an `## [x.y.z]` heading. Do not edit `## [1.23.0]`. Do not bump a version.

```markdown
- `faa-ams-vv` rebuilt from FAA AMS Lifecycle Verification and Validation Guidelines, Version 4.0 (January 2023). The April 2017 pin Version 3.0 is retired. SASP is its own chapter. CMMI v1.2 definitions stay paraphrased.
```

`SKILLS.md` line 50: replace the faa-ams-vv description so it names Version 4.0 January 2023, the verify-vs-validate split, the three tiers, decision-point-gated V&V, shift-left, the CMMI v1.2 paraphrase, and the pointer to `faa-sem`. Do not say 7 chapters. Do not say April 2017. Do not change line 9. Pack count stays `74 packs (+8 signposts, +1 orchestrator)`. Do not change any other skill row.

`README.md` line 164: on the `faa-ams-vv` row only, change the title cell to `FAA AMS Lifecycle Verification and Validation Guidelines, Version 4.0` and change `live (7 chapters)` to `live (CHAPTER_COUNT chapters)`. `CHAPTER_COUNT` is the integer from Task 1. Do not change the `packs-74` badge. Do not change any other row's chapter count.

- [ ] **Step 7: Shrink the backlog evidence cell**

`docs/superpowers/backlog.md` line 101, slug `source-watch-calibrate-and-wire-2`. Status stays `open`. Do not delete the row. Do not mark it `done`.

Replace the summary cell so it says 12 findings remain, not 13. Replace the evidence cell. Drop `faa-ams-vv` from the parenthetical and from the watchlist-field list. State 12 findings remain. Keep the `nasa-pra` mis-pin sentence. Leave the other slugs in the list: sebok, nasa-se-handbook, nist-ssdf, nist-stat-handbook, dod-rio, nasa-schedule, dodaf, federal-bca, mrl-deskbook.

Summary cell, substance required:

```text
12 drift findings stand recorded as watchlist bookkeeping after the V&V guidelines rebuild left this list: pack content is behind the publisher's observed revisions and no rebuild has been decided for the remaining rows
```

Evidence cell, substance required:

```text
docs/source-watchlist.json version fields on the remaining drift rows (nasa-pra, sebok, nasa-se-handbook, nist-ssdf, nist-stat-handbook, dod-rio, nasa-schedule, dodaf, federal-bca, mrl-deskbook); 12 findings remain after the V&V guidelines rebuild left this list on VET_DATE; nasa-pra watch version still carries the handbook Version 2.0 string and that string does not describe NASA/SP-2011-3421, so it is not a rebuild candidate for this cut; .zcode/source-watch/2026-10-12.md drift findings + addendum item 6
```

`VET_DATE` is the Task 1 date, not the token. Do not close the row. The new evidence cell must not contain the token `faa-ams-vv`.

- [ ] **Step 8: Generate pages and run the three-surface diff**

```bash
python tooling/gen_pack_pages.py --only faa-ams-vv
python tooling/gen_packs_page.py
```

`--only` rewrites `docs/packs/faa-ams-vv/index.html` and always rewrites `docs/sitemap.xml` from the full live catalog. It does not truncate the sitemap. Do not hand-edit the generated HTML.

Three-surface byte-match. No gate does this. Run it by hand.

```bash
python -c "
import json, pathlib
pack = pathlib.Path('packs/faa-ams-vv/PACK.yaml').read_text(encoding='utf-8')
def field(text, key):
    for line in text.splitlines():
        if line.startswith(key + ':'):
            return line.split(':', 1)[1].strip().strip('\"')
    if key == 'chapters':
        for line in text.splitlines():
            s = line.strip()
            if s.startswith('chapters:'):
                return s.split(':', 1)[1].strip()
    raise SystemExit('missing ' + key)
title = field(pack, 'title')
ver = field(pack, 'source_version')
cat = json.loads(pathlib.Path('catalog.json').read_text(encoding='utf-8'))
row = next(p for p in cat['packs'] if p['slug']=='faa-ams-vv')
watch = json.loads(pathlib.Path('docs/source-watchlist.json').read_text(encoding='utf-8'))
w = next(s for s in watch['sources'] if s['slug']=='faa-ams-vv')
pra = next(s for s in watch['sources'] if s['slug']=='nasa-pra')
assert row['title'] == title, (row['title'], title)
assert row['source_version'] == ver, (row['source_version'], ver)
assert w['version'] == ver, (w['version'], ver)
assert w['document'] == 'AMS Lifecycle Verification and Validation Guidelines'
assert str(row['chapters']) == field(pack, 'chapters')
assert cat['updated'] == '2026-10-14'
assert row['license'] == 'Public Domain (US Government work)'
assert pra['version'] == 'NASA Risk Management Handbook Version 2.0 (November 2024; NASA/SP-20240014019 Part 1, NASA/SP-20240014326 Part 2)'
assert 'April 2017' not in pack
assert 'CMMI' in pack
print('three-surface match', ver, 'chapters', row['chapters'])
"
```

Expected: `three-surface match Version 4.0 (January 2023)` and the Task 1 chapter count. If `version` and `source_version` differ, `--record` ran against the wrong string. Re-run Step 5. Do not edit `nasa-pra`.

```bash
python tooling/check_classification_rules.py
python tooling/check_capability_map.py
python tooling/check_source_watch.py
```

Expected: three exit 0.

---

### Task 4: Sweep

**Gate:** gate-enforced (spec Testing bar, including the manual README and SKILLS.md check).

**Files:**
- Read only. Fix only findings this cut introduced, and only inside files Tasks 1 through 3 already own.

**Interfaces:**
- Consumes: the rebuilt pack, the regenerated map, and the registration edits from Tasks 1 through 3.
- Produces: a passing gate transcript. No commit.

**Model:** flash

Per-task brief: `.superpowers/sdd/2026-10-28-rebuild-faa-ams-vv-v4/task-4-brief.md`

- [ ] **Step 1: 2017-pin grep and the manual README / SKILLS.md check**

```bash
rg -n "April 2017" packs/faa-ams-vv
rg -n "Version 3.0" packs/faa-ams-vv
rg -n "faa-ams-vv" docs/superpowers/backlog.md
```

Expected: the the first two commands print nothing (the pack itself is fully off the V3 pin; pre-existing `Version 3.0` hits elsewhere in catalog.json or NOTICE, such as dod-mq-bok July 2025, are out of scope). The third command prints no hit on the `source-watch-calibrate-and-wire-2` row. Hits on other backlog rows are out of scope. Leave them.

No sentinel test covers README or SKILLS.md. Read them and record the result in the run notes.

- `README.md` faa-ams-vv row says `live (CHAPTER_COUNT chapters)`, not `(7 chapters)`, and the title cell names Version 4.0.
- `SKILLS.md` faa-ams-vv row names Version 4.0 and does not say 7 chapters or April 2017.
- `SKILLS.md` line 9 still says `74 packs (+8 signposts, +1 orchestrator)`.

- [ ] **Step 2: Prose check and the CMMI-caveat presence check**

```bash
python ~/.zcode/scripts/prose_check.py packs/faa-ams-vv/SKILL.md packs/faa-ams-vv/LICENSE packs/faa-ams-vv/glossary.md packs/faa-ams-vv/cheatsheet.md packs/faa-ams-vv/patterns.md packs/faa-ams-vv/chapters CHANGELOG.md NOTICE
python -c "
import pathlib
need = {
    pathlib.Path('packs/faa-ams-vv/PACK.yaml'): 'CMMI',
    pathlib.Path('packs/faa-ams-vv/LICENSE'): 'CMMI',
    pathlib.Path('packs/faa-ams-vv/SKILL.md'): 'CMMI',
}
notice = pathlib.Path('NOTICE').read_text(encoding='utf-8')
start = notice.index('[pack: faa-ams-vv]')
end = notice.index('[pack: gao-agile]')
block = notice[start:end]
assert 'CMMI' in block, 'NOTICE faa-ams-vv block dropped the CMMI caveat'
assert 'January 2023' in block
assert 'April 2017' not in block
for path, token in need.items():
    text = path.read_text(encoding='utf-8')
    assert token in text, path
print('cmmi caveat present')
"
```

Expected: `prose_check.py` exits 0, or every finding fixed or justified in the run notes. Zero em dashes in headings and body prose of the files this cut wrote. The NOTICE `Licence:` line keeps the existing `--` field separator. That is the block shape, not new prose. Do not spread it. The second command prints `cmmi caveat present`. A rebuild that drops the CMMI caveat fails.

- [ ] **Step 3: Catalog counts, release gate, and the URL rule**

```bash
python tooling/test_catalog_live_set.py
python tooling/test_catalogue_count.py
python tooling/test_ci_gate.py
python tooling/check_release.py
python -c "
import pathlib
root = pathlib.Path('packs/faa-ams-vv')
bad = []
for p in root.rglob('*'):
    if p.is_file() and ('https://' in p.read_text(encoding='utf-8') or 'http://' in p.read_text(encoding='utf-8')):
        bad.append(str(p))
assert not bad, bad
cat = pathlib.Path('catalog.json').read_text(encoding='utf-8')
assert '\"updated\": \"2026-10-14\"' in cat
print('no urls in pack')
"
git ls-files sources/
```

Expected: the three catalog tests exit 0 (counts unchanged at 74/83). `check_release.py` prints `RELEASE CHECK: PASS` and exits 0, or its only new findings are outside this pack and get named in the run notes, not fixed here. `git ls-files sources/` is empty. `catalog.json` `updated` is still `2026-10-14`.

If `check_release.py` fails on a surface this cut owns, fix that surface and re-run. Do not bump `RELEASE-INFO.txt`. Do not bump either plugin `version`. Do not change `catalog.json` `updated`. Do not edit other FAA packs. Do not edit `packs/se/SKILL.md`. Do not edit `packs/nasa-pra/`. Do not commit unless the parent execution mode says commit. Do not push. Do not open a PR.

Chapter-file count is between 3 and 6. `build.chapters` equals that count. Catalog `chapters` equals that count. Notes length equals `741 - 7 + N`.

---

## Testing

All must pass before the cut is done. Commands are gates, not suggestions.

1. `python tooling/validate_pack.py packs/faa-ams-vv` and `python tooling/check_pack_quality.py packs/faa-ams-vv` exit 0. Floor is 30 lines per chapter. Topic Index `chNN` tokens resolve to the new chapter set.
2. `python tooling/test_catalog_live_set.py`, `python tooling/test_catalogue_count.py`, and `python tooling/test_ci_gate.py` exit 0. Counts stay 74/83. `catalog.json` `updated` stays `2026-10-14`.
3. `python ~/.zcode/scripts/prose_check.py` on the touched prose exits 0, or findings are fixed or justified.
4. 14-gram scan of the new chapters against the extract: zero contiguous runs of 18 or more words. The CMMI footnote sentence is a named citation, not a passage to copy.
5. `python tooling/check_classification_rules.py` exits 0. A coverage error on `faa-ams-vv` means a chapter file and an assignment row disagree.
6. `python tooling/check_capability_map.py` exits 0. Notes length equals `741 - 7 + N`.
7. `python tooling/generate_capability_map.py --generated-on <VET_DATE> --sync-md` regenerates without a notes-length refusal. Re-run the capability-map check after generation.
8. `python tooling/check_source_watch.py` exits 0. `faa-ams-vv` `version` equals catalog `source_version`. No other slug's `version` changed. CAUTION: no gate compares watch `version` to catalog `source_version`. The three-surface byte-match in Task 3 Step 8 is the check. Record only after the catalog row carries the new `source_version`.
9. `python tooling/check_release.py` exits 0, or its only new findings are outside this pack and get named, not fixed here.
10. `rg -n "April 2017" packs/faa-ams-vv` returns nothing. `rg -n "Version 3.0" packs/faa-ams-vv` returns nothing. Separately confirm `README.md` no longer says `v3.0` or `(7 chapters)` for faa-ams-vv and the `SKILLS.md` row shows Version 4.0. No sentinel test covers README or SKILLS.md. Verify by eye and record the result in the run notes.
11. `rg -n "faa-ams-vv" docs/superpowers/backlog.md` returns no hit on the `source-watch-calibrate-and-wire-2` row. Hits on other rows are out of scope.
12. Chapter-file count is between 3 and 6. `build.chapters` equals that count. Catalog `chapters` equals that count.
13. No URL string in `PACK.yaml` or `catalog.json`. `git ls-files sources/` is empty.
14. CMMI caveat still present in `PACK.yaml` `notes`, `LICENSE`, `NOTICE` `[pack: faa-ams-vv]`, and `SKILL.md`. A rebuild that drops it fails.

Count formulas, not a hardcoded chapter total: content packs stay 74, skills stay 83, map assignments `741 - 7 + N` where N is the Task 1 chapter count (3, 4, 5, or 6). At the expected N of 4, assignments are 738.

## Self-review

Spec coverage: D1 Task 1 Step 1 (FAST `/docs/` PDF, cover pin, no invented supersession) and Task 2 Step 1 (title and source_version). D2 Task 1 Step 1 (stop conditions, no contractor notice, personal Author names are not a stop) and Task 2 Steps 1 and 2 (tier-1 fields, notes manifest, no invented legend). D3 Task 2 Steps 3 and 6 (synthesized notes, 14-gram scan, CMMI footnote named not copied, tables as January 2023 snapshots, AMS policy named not quoted). D4 Global Constraints and Task 3 Step 5 (other FAA packs untouched, nasa-pra watch version asserted unchanged). D5 Task 1 Step 2 (contents list wins, 3 to 6, SASP its own chapter, appendices out, no file per table). D6 Task 2 Step 4 (three support files, no fourth). D7 Task 3 Steps 2, 3, and 4 (delete-then-append, four literals, regenerate). D8 Global Constraints and Task 4 Step 3 (counts stay, no version bump, `updated` stays `2026-10-14`). D9 Task 3 Steps 5 and 8 (hand-edit document to `AMS Lifecycle Verification and Validation Guidelines`, `--record` after catalog, manual three-surface diff). D10 Task 3 Step 7 (evidence shrink to 12, no `faa-ams-vv` token in the new cell, status stays open). Testing items 1 through 14 are the Testing section and Task 4. Registration surfaces in Codebase context are Task 3 Steps 1, 6, and 8.

Placeholder scan: no open slots, no deferred-work markers, no "similar to Task N" standing in for a step. `CHAPTER_COUNT`, `VET_DATE`, `SOURCE_PAGES`, `PAGE_COUNT`, and `BYTE_SIZE` are Task 1 outputs, not blanks. The pin string `Version 4.0 (January 2023)`, the title, and the PDF URL are copied from the spec. Catalog row key order matches the live faa-ams-vv row. Watchlist key order matches `ENTRY_KEYS`.

Type consistency: `source_version` is `Version 4.0 (January 2023)` in PACK.yaml, the catalog row, and the `--record` argument. `document` is `AMS Lifecycle Verification and Validation Guidelines`, not the version string. `CHAPTER_COUNT` is the chapter-file count, used as `build.chapters`, catalog `chapters`, and the README cell. Notes length is `741 - 7 + CHAPTER_COUNT` in Task 3 Steps 2 and 3 and in Testing item 6. Support basenames are `glossary.md`, `cheatsheet.md`, `patterns.md` in Task 2 and Task 3. The nasa-pra watch version string in Task 3 Step 5 matches the live row. Support note labels match the live notes being replaced.

Deviations from spec: one, recorded. The spec's D5 sentence names an expected 4-file table that folds SASP with CRD into ch03 and puts sections 3.3 through 3.5 in ch04. The same spec's grouping note, and the parent dispatch, say the V4 contents list gives SASP its own chapter and that the contents list wins. This plan follows the contents-list rule: expected ch03 is SASP only, expected ch04 is sections 3.2 through 3.5, still 4 files, still inside floor 3 and ceiling 6. Task 1 discards that expected table if the re-fetched contents list disagrees. `gen_pack_pages.py --only` always rewrites `docs/sitemap.xml` from the full live catalog, so the spec's "must not be the last generator run if it truncates" condition does not fire. The plan still finishes with `gen_packs_page.py`, which the spec also requires.
