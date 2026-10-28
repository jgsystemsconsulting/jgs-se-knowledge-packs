# Rebuild nasa-risk Handbook v2 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rebuild the existing `packs/nasa-risk` slug from NASA Risk Management Handbook Version 2.0 (November 2024), both volumes, and move every version-bearing registration surface off NASA/SP-2011-3422.

**Architecture:** Re-fetch both NTRS citation records and both PDFs before any chapter prose. Freeze chapter titles from the PDF contents lists (Part 1 chapters 1 through 6, Definitions folded into the glossary, one Part 2 examples chapter). Delete the ten 2011 chapter files and rewrite the pack in place. Delete every `nasa-risk` classification and note row, append the new set, and move the hard-coded 744-row pin in the capability-map generator to `744 - 10 + N`. `nasa-pra` stays untouched.

**Tech Stack:** Markdown pack files, YAML frontmatter, JSON catalogue and map files, Python 3 stdlib tooling (`tooling/validate_pack.py`, `tooling/check_pack_quality.py`, `tooling/check_source_watch.py`, `tooling/generate_capability_map.py`, `tooling/check_capability_map.py`, `tooling/check_classification_rules.py`, `tooling/gen_pack_pages.py`, `tooling/gen_packs_page.py`, `tooling/check_release.py`). PDF text via `pdftotext` if present, else an already-installed reader. No new dependencies.

**Spec:** `docs/superpowers/specs/2026-10-28-rebuild-nasa-risk-handbook-v2.md`

Spec certificate sha256: `d1bf8090b3c2161144e6d44528bde88c110a56998f26a97571784541c05edeff`.

## Global Constraints

- D1: primary pin is NASA Risk Management Handbook Version 2.0, November 2024, two volumes, one pack. Part 1 NASA/SP-20240014019 is the doctrine volume and the volume that supersedes NASA/SP-2011-3422. Part 2 NASA/SP-20240014326 is the examples volume. Both PDFs are in scope. Do not pin Part 2's verso typo `SP-202400114326`. Do not drop Part 2. Do not split into two packs.
- D2: licence stays tier 1 public domain, US Government work, 17 U.S.C. 105. Field values, verbatim: `license: "Public Domain (US Government work, 17 U.S.C. 105)"`, `license_tier: 1`, `commercial_use: true`, `share_alike: false`, `attribution_required: false`. NTRS `PUBLIC_USE_PERMITTED` plus NASA special-publication class is the evidence. Do not invent a copyright legend the PDF does not print. Execution re-fetches both PDFs and both citation APIs. Stop if either PDF URL is dead, either file is not `%PDF`, either NTRS record is no longer `distribution: PUBLIC`, or either record sets `containsThirdPartyMaterial` true.
- D3: `nasa-pra` is out. SP-2011-3421 is the PRA Procedures Guide, not the handbook Part 1 supersedes. Do not edit `packs/nasa-pra/`, its catalog row, its NOTICE block, or its watchlist row. The watchlist `version` on `nasa-pra` is a mis-pin from 2026-10-12. Leave it. Name it in the backlog evidence shrink.
- D4: reconstruction rule stays the live pack's rule. Synthesized reference notes. Short defined terms may be kept. No long verbatim passages. No PDF page images. NPR 8000.4, NPD 1000.0, NPR 7120.5, and NPR 8715.3 are named as the policy the handbook aligns to. They are not quoted and not rebuilt. Domain PRA methods stay a pointer to `nasa-pra`, not a chapter here.
- D5: chapter count is one file per Part 1 numbered chapter, excluding chapter 7 Definitions, plus one file for the Part 2 examples. Expected 7 files: ch01 through ch06 from Part 1 chapters 1 through 6, ch07 from Part 2 chapters 1 through 4 as one examples chapter. Contents lists win over the provisional table. If Part 1 gains or loses a numbered chapter, follow the list and keep Definitions out of `chapters/`. Do not split Part 1 chapter 4's RIDM steps into three files. Do not split Part 2 into four files. Floor 6, ceiling 8. Appendices A through I are not chapters.
- D6: support files stay three: `glossary.md`, `cheatsheet.md`, `patterns.md`. They are not in the 6 to 8 count. Glossary absorbs Part 1 chapter 7 and the acronym list. Cheatsheet absorbs the RIDM six steps and the CRM five steps plus communicate-and-document. Patterns absorbs risk-leadership and graded-approach moves. No fourth support file.
- D7: classification churn is delete-then-append, not a migration. Remove every `nasa-risk` row from `docs/classification-rules.json` `assignments` and from `docs/capability-pack-map-note-overrides.json` `notes` (13 rows each today: 10 chapters + 3 support). Append one `is_support: false` row per new chapter file and one `is_support: true` row per surviving support file. Same keys in both files. Cluster `Risk Management` unless a chapter's best fit is a different name already in `cluster_names`. Do not invent a cluster. Bump the `744` literal in `tooling/generate_capability_map.py` (docstring line 9 and the three comparison sites at lines 195, 203, and 204) to `744 - 10 + N`, where N is the new chapter-file count. Support rows do not change the total: 3 removed, 3 added. Expected total `734 + N`. At the D5 expected N of 7, total is 741. `map_version` stays `1.22.0`. `generated_on` on both JSON files moves to the execution date.
- D8: counts that measure packs or skills do not change. Pack count stays 74. Skill count stays 83. NASA family chip stays 16. `catalog.json` `updated` stays `2026-10-14`. Do not bump `RELEASE-INFO.txt` or either plugin `version`. Do not add a skill path. The slug already exists in both plugin manifests.
- D9: watchlist `nasa-risk` only. Hand-edit `document` to `NASA Risk Management Handbook` (the watch `document` field carries the document title, not the version). Run `--record nasa-risk "<catalog source_version>" <vet-date>` after the catalog row matches, not before. `version` must equal catalog `source_version`. Do not pass a URL. Do not record `nasa-pra`. CAUTION: no gate compares watch `version` to catalog `source_version`. The three-surface byte-match (PACK.yaml, catalog row, watchlist) is a manual Testing step. Record only after the catalog row carries the new `source_version`, so the manual diff has a fixed reference.
- D10: backlog slug `source-watch-calibrate-and-wire-2` stays `open`. Evidence cell drops `nasa-risk` and states the count is 13, not 14. The remaining list keeps `nasa-pra` and states its watch `version` is a mis-pin of the handbook V2.0 onto SP-2011-3421, not a rebuild candidate for this cut. Do not delete the row. Do not mark it `done`.
- Pin string, verbatim, in PACK.yaml `source_version`, the catalog `source_version`, and the watchlist `version` once `--record` runs: `Version 2.0 (November 2024)`. If the re-fetch cover date disagrees, stop. Do not rewrite the pin to match a different issue.
- Title, verbatim: `NASA Risk Management Handbook, Version 2.0 (NASA/SP-20240014019, NASA/SP-20240014326)`. Publisher, verbatim: `NASA`.
- `build.built_on` is the execution date in `YYYY-MM-DD`, not a date copied from this plan's filename. `catalog.json` `"updated"` stays `2026-10-14`.
- `build.source_pages` is 392 (303 + 89) unless a re-fetch returns different page counts. `build.chapters` equals the chapter-file count, not 10 and not 392. `build.method` names the two PDFs, not the 2011 extraction.
- `notes` carries the public-domain line, both SP numbers, both byte sizes, both page counts, the vet date, the NTRS determination fields, the Part 1 supersession sentence, and the named-not-quoted policy list (NPR 8000.4, NPD 1000.0, NPR 7120.5, NPR 8715.3). No URL in `PACK.yaml`.
- `change_indication: "reconstructed as synthesized reference notes"`.
- No `source_url` in PACK.yaml or `catalog.json`. No `http://` or `https://` under `packs/nasa-risk/`.
- Chapter body at least 30 lines (`tooling/check_pack_quality.py` `MIN_CHAPTER_LINES`). Topic Index `chNN` tokens in `SKILL.md` resolve to the new chapter files. Frontmatter `name` stays `nasa-risk`.
- Catalog row keeps the nine live keys, in order: `slug`, `title`, `publisher`, `source_version`, `license`, `license_tier`, `commercial_use`, `chapters`, `status`. `title` matches PACK.yaml `title`. `source_version` matches PACK.yaml `source_version`. `chapters` matches the new file count. `license` stays the shorter catalog form already on the live row and on the nasa-pra row: `Public Domain (US Government work)`. Do not add a key.
- Chapter assignment notes are one sentence each, no em dash, and say the note is from Version 2.0 November 2024. Support-file notes stay short labels, same shape as the three notes being replaced (`Glossary for pack`, `Cheatsheet for pack`, `Patterns for pack`).
- Do not (spec Out and Non-goals, verbatim):
  - Do not edit `packs/nasa-pra/`, its catalog row, its NOTICE block, or its watchlist row.
  - Do not close `source-watch-calibrate-and-wire-2`. Thirteen findings remain.
  - Do not bump a release version. Changelog Unreleased is the record.
  - Do not edit neighbor pack chapters that mention `nasa-risk`.
  - Do not commit the downloaded PDFs. They are vet inputs, not repo content.
  - Do not bump `RELEASE-INFO.txt`, either plugin `version`, or `catalog.json` `updated`.
  - Do not add a skill path. Do not add a slug. Do not hand-edit generated HTML, `docs/capability-pack-map.json`, or `docs/capability-pack-map.md`.
- Also out: the other 12 drift rows (sebok, nasa-se-handbook, nist-ssdf, nist-stat-handbook, dod-rio, nasa-schedule, dodaf, federal-bca, faa-ams-vv, mrl-deskbook, and the two standing-drift rows the backlog still counts inside 14). A second pack for Part 2, or a chapter per Part 2 section. Quoting NPR, NPD, or PRA guide text. Embedding PDF pages. New validators, new page templates, new licence tiers. GitHub release, plugin publish, or commit. This plan does not authorize those.
- A licence failure, a dead PDF, a non-PUBLIC NTRS record, `containsThirdPartyMaterial: true`, or a contents list that will not fit 6 to 8 chapters is a stop-and-report. Do not invent content to fill the gap.
- No task pauses for human input except the D2 stop. Executors do not ask questions. Commit steps are off unless the parent execution mode says commit. Do not push. Do not open a PR.
- Per-task briefs live at `.superpowers/sdd/2026-10-28-rebuild-nasa-risk-handbook-v2/task-N-brief.md`. The controller writes them at dispatch. This plan does not create those files.

## Codebase context

Post-P57 baseline, re-checked on main at `6b0348a` on 2026-10-28. Precedent for the reconstructed-notes rule and the three support files is the live `packs/nasa-risk/` itself. Required content-pack layout is `docs/PACK-SPEC.md`.

- `packs/nasa-risk/` today: `PACK.yaml` (v1.0 November 2011, `source_pages: 256`, `chapters: 10`, `built_on: 2026-06-19`), `SKILL.md`, `LICENSE`, `glossary.md`, `cheatsheet.md`, `patterns.md`, and 10 chapter files under `chapters/`. Support files are not chapters. The ten files to delete: `ch01-introduction-and-rm-overview.md`, `ch02-ridm-crm-integration.md`, `ch03-ridm-part1-identification-of-alternatives.md`, `ch04-ridm-part2-risk-analysis-of-alternatives.md`, `ch05-ridm-part3-risk-informed-selection.md`, `ch06-crm-initialisation-and-planning.md`, `ch07-crm-identify-and-analyze.md`, `ch08-crm-plan-step.md`, `ch09-crm-track-control-communicate.md`, `ch10-enterprise-risks-and-appendices.md`.
- `nasa-risk` assignment rows today: 10 chapter rows plus 3 support rows (`glossary.md`, `cheatsheet.md`, `patterns.md`), all cluster `Risk Management`. Cluster name already exists in `cluster_names`. Do not invent one. Overrides are a parallel list, same `(pack, chapter)` keys, one `note` string each. `tooling/check_classification_rules.py` requires one `is_support: false` row per `packs/<slug>/chapters/*.md` and rejects an assignment whose chapter file is gone. There is no removal API. A rebuild deletes the old `nasa-risk` rows from both JSON files and appends the new ones. Key sets must match after the edit.
- `tooling/generate_capability_map.py` refuses any notes length other than 744 (line 9 docstring, line 195 `len(notes) != 744`, line 203 `if len(notes) != 744`, line 204 error string). Those four literals must move, or the generator rejects the new note file. Do not hand-edit `docs/capability-pack-map.json` or `docs/capability-pack-map.md`. `map_version` on both JSON files is `1.22.0` and stays. `generated_on` on both is `2026-10-28` today and must move to the execution date or the fidelity check fails. Generator invocation: `python tooling/generate_capability_map.py --generated-on YYYY-MM-DD --sync-md`.
- Watchlist today, both rows, `last_checked` 2026-10-12. `nasa-risk` `document` is `v1.0 (November 2011)`. `version` already carries `Version 2.0 (NASA/SP-20240014019 Part 1; NASA/SP-20240014326 Part 2; November 2024)`. `document` is what the pack was built from. `version` is what the watch last saw. After the rebuild, `document` must be hand-edited to `NASA Risk Management Handbook`. `python tooling/check_source_watch.py --record SLUG VERSION DATE` rewrites `version` and `last_checked` on an existing slug. It does not create a row. It does not write `document`. Entry keys, in order: `slug`, `publisher`, `document`, `version`, `last_checked`, `hint`.
- `nasa-pra` watch `version` is `NASA Risk Management Handbook Version 2.0 (November 2024; NASA/SP-20240014019 Part 1, NASA/SP-20240014326 Part 2)`. That string does not describe SP-2011-3421. Record the wrongness in the backlog evidence cell. Do not edit the row.
- Registration surfaces that name the 2011 pin and must move with the pack: `catalog.json` nasa-risk row (nine keys, same shape; do not change top-level `updated`), `README.md` catalogue row (line 131, `live (10 chapters)` must become the new count), `SKILLS.md` nasa-risk description (line 24), `NOTICE` `[pack: nasa-risk]` block (line 3957, ends before `[pack: nasa-system-safety]`), `packs/nasa-risk/LICENSE`, `packs/nasa-risk/SKILL.md`. Generated pages (`docs/packs/nasa-risk/index.html`, `docs/packs.html`, `docs/sitemap.xml`) come from generators. Do not hand-edit them.
- `tooling/gen_pack_pages.py --only nasa-risk` rewrites that pack page and always rewrites `docs/sitemap.xml` from the full live catalog (help text at the `--only` flag). It does not truncate the sitemap. Finish with `python tooling/gen_packs_page.py` for `docs/packs.html`. Do not hand-edit generated HTML.
- Surfaces that count packs, skills, or NASA family size do not move. Pack count stays 74. Skill count stays 83. `SKILLS.md` line 9 stays `74 packs (+8 signposts, +1 orchestrator)`. `docs/index.html` `NASA · 16` chip stays 16. `docs/products/website/01-jgs-se-knowledge-packs.yaml` `NASA (16)` stays 16. `README.md` `packs-74` badge stays. Plugin `version` fields stay. `RELEASE-INFO.txt` stays. Do not edit `.claude-plugin/plugin.json` or `.cursor-plugin/plugin.json`. The slug is already in both.
- `/se` already routes risk to `nasa-risk` and PRA to `nasa-pra` (`packs/se/SKILL.md` lines 87, 93, 124, 145). No new slug. No new routing row. Description text may name Version 2.0. Do not add `nasa-risk` to the system-safety row. Do not remove `nasa-pra` from it. Today those rows do not say 2011 or SP-2011-3422. Leave them.
- `docs/superpowers/backlog.md` line 101, slug `source-watch-calibrate-and-wire-2`, status `open`. Evidence names 14 drift rows, `nasa-pra` and `nasa-risk` among them. This cut removes `nasa-risk` from that evidence list and from the count. It does not close the row.
- `CHANGELOG.md` already has `## [Unreleased]` and `### Added`. Add a `### Changed` bullet under `[Unreleased]`. Do not add an `## [x.y.z]` heading. Do not edit `## [1.23.0]`.
- Neighbors named in other packs (`dod-rio`, `nasa-ms-7009`, `gao-schedule`, `space-signpost`) cite `nasa-risk` as the RIDM/CRM pack. Leave those sentences. They do not pin SP-2011-3422.
- `sources/` is gitignored. The PDFs and the text extracts stay untracked. `git ls-files sources/` must stay empty.
- Catalog `license` on the live nasa-risk row is `Public Domain (US Government work)`. PACK.yaml `license` is the longer `Public Domain (US Government work, 17 U.S.C. 105)`. Keep that split. Do not lengthen the catalog cell to match PACK.yaml.

## Research

research: https://ntrs.nasa.gov/citations/20240014019
research: https://ntrs.nasa.gov/api/citations/20240014019/downloads/SP-20240014019.pdf
research: https://ntrs.nasa.gov/citations/20240014326
research: https://ntrs.nasa.gov/api/citations/20240014326/downloads/SP-20240014326.pdf

Page-level pin from the spec, not re-verified by this plan. Task 1 re-vets it.

| Volume | Title (NTRS, exact) | Report number | PDF | Spec bytes | Spec pages | Cover date |
|---|---|---|---|---|---|---|
| Part 1 | NASA Risk Management Handbook: Version 2.0, Part 1 | NASA/SP-20240014019 | download URL above | 14,471,540 | 303 | Version 2.0, November 2024 |
| Part 2 | NASA Risk Management Handbook: Version 2.0, Part 2 | NASA/SP-20240014326 | download URL above | 6,669,330 | 89 | Version 2.0, November 2024 |

Cover subtitles, not the NTRS title strings: Part 1 "Guidance for an Integrated Framework of Risk Leadership and Management Across the NASA Organization: Concepts and Principles". Part 2 "Guidance for an Integrated Framework of Risk Leadership and Management Across the NASA Organization: Application Examples".

Supersession, quoted from the PDF verso pages:

- Part 1 page 2: "NASA SP-20240014019 Version 2 supersedes NASA SP-2011-3422 Version 1 dated November 2011."
- Part 2 page 2: "NASA SP-202400114326 and NASA SP-20240014019 supersede NASA SP-2011-3422 dated November 2011." The `114326` token is a typo on the verso. NTRS `otherReportNumbers` and the cover both read NASA/SP-20240014326. Pin the NTRS number. Do not copy the typo into `PACK.yaml`.

NTRS `copyright` on 20240014019: `determinationType` `PUBLIC_USE_PERMITTED`, `containsThirdPartyMaterial` false. Neither PDF prints "public domain" or "17 U.S.C." in the front matter. Do not invent a legend the PDF does not print. Spec fetch on 2026-10-28: both citation APIs HTTP 200 JSON, both PDFs HTTP 200 `%PDF-1.7`. Task 1 records the execution-time byte sizes and page counts. The spec numbers are a check, not a lock, except the D2 stop conditions.

Provisional chapter map, discarded where the PDF contents lists disagree:

| File | Draws from | Job |
|---|---|---|
| ch01-introduction-and-scope.md | Part 1 ch 1 | Purpose, policy documents the handbook aligns to, what changed in Version 2.0, how the two parts are meant to be used. |
| ch02-objectives-driven-framework.md | Part 1 ch 2 | Risk and opportunity in the NASA context, objectives flow-down, risk leadership, graded rigor, integration across boundaries. |
| ch03-risk-models-and-posture.md | Part 1 ch 3 | Risk triplet, risk scenario diagram, known vs unknown-unknown, risk posture and tolerance, matrix display. |
| ch04-risk-informed-decision-making.md | Part 1 ch 4 | RIDM six steps in one chapter. Alternatives, analysis, deliberation, selection. Graded application stays here. |
| ch05-continuous-risk-management.md | Part 1 ch 5 | CRM initialize, identify, analyze, plan, track, control, communicate and document. |
| ch06-organizational-integration.md | Part 1 ch 6 | Life-cycle reviews, cross-cutting risk, risk management plan contents. |
| ch07-application-examples.md | Part 2 ch 1-4 | One chapter. Process selection, one activity-planning RIDM example, CRM execution examples. Examples illustrate Part 1. They do not add doctrine. |

Part 1 contents (page iv), top-level only, as the spec recorded them: 1 Introduction, 2 Objectives-Driven Risk Management Framework Foundations and Key Elements, 3 Risk Models, Analysis, and Decision Concepts, 4 Risk-Informed Decision Making, 5 Continuous Risk Management, 6 Organizational and Managerial Aspects of Objectives-Driven Risk Management, 7 Definitions. Appendices A through I. Part 2 contents (page iv): 1 Introduction, 2 Risk Process Selection and Applicability, 3 Example of Activity-Planning RIDM Execution, 4 Examples of CRM Execution. No appendix in Part 2. No chapter 5.

## File map

Create (untracked; do not commit):

- `sources/nasa-risk/SP-20240014019.pdf`
- `sources/nasa-risk/SP-20240014326.pdf`
- `sources/nasa-risk/part1.txt`
- `sources/nasa-risk/part2.txt`
- `sources/nasa-risk/citation-20240014019.json`
- `sources/nasa-risk/citation-20240014326.json`

Create (tracked):

- `packs/nasa-risk/chapters/chNN-<slug>.md` (6, 7, or 8 files, frozen in Task 1; expected 7)

Modify:

- `packs/nasa-risk/PACK.yaml`
- `packs/nasa-risk/LICENSE`
- `packs/nasa-risk/SKILL.md`
- `packs/nasa-risk/glossary.md`
- `packs/nasa-risk/cheatsheet.md`
- `packs/nasa-risk/patterns.md`
- `catalog.json` (nasa-risk row only; `"updated"` untouched)
- `docs/source-watchlist.json` (nasa-risk `document`, then `--record` rewrites `version` and `last_checked`)
- `SKILLS.md` (nasa-risk description only; line 9 count stays)
- `NOTICE` (`[pack: nasa-risk]` block only)
- `README.md` (nasa-risk catalogue row chapter count only)
- `docs/classification-rules.json` (delete 13 nasa-risk rows, append `N + 3`)
- `docs/capability-pack-map-note-overrides.json` (same keys)
- `tooling/generate_capability_map.py` (four `744` literals become `744 - 10 + N`)
- `docs/capability-pack-map.json` and `docs/capability-pack-map.md` (regenerated)
- `docs/packs/nasa-risk/index.html`, `docs/packs.html`, `docs/sitemap.xml` (regenerated)
- `CHANGELOG.md` (one `[Unreleased]` Changed bullet)
- `docs/superpowers/backlog.md` (evidence cell on line 101 only)

Delete:

- the ten chapter files listed in Codebase context

Do not modify: `packs/nasa-pra/`, `packs/se/SKILL.md`, `.claude-plugin/plugin.json`, `.cursor-plugin/plugin.json`, `RELEASE-INFO.txt`, `docs/index.html`, `docs/products/website/01-jgs-se-knowledge-packs.yaml`, `docs/LICENSING.md`, neighbor pack chapters.

---

### Task 1: Vet both PDFs, freeze the chapter map, delete the ten old chapters

**Gate:** gate-enforced (spec D2 stop, contents-list freeze).

**Files:**
- Create: `sources/nasa-risk/SP-20240014019.pdf` (untracked)
- Create: `sources/nasa-risk/SP-20240014326.pdf` (untracked)
- Create: `sources/nasa-risk/part1.txt` (untracked)
- Create: `sources/nasa-risk/part2.txt` (untracked)
- Create: `sources/nasa-risk/citation-20240014019.json` (untracked)
- Create: `sources/nasa-risk/citation-20240014326.json` (untracked)
- Delete: the ten `packs/nasa-risk/chapters/ch*.md` files listed in Codebase context

**Interfaces:**
- Consumes: the four research URLs and the D2 stop conditions.
- Produces: `CHAPTER_COUNT` (integer 6, 7, or 8), `PAGE_COUNT_1`, `PAGE_COUNT_2`, `BYTE_SIZE_1`, `BYTE_SIZE_2` (integers), `VET_DATE` (`YYYY-MM-DD`), the frozen basename list `chNN-kebab-title.md` with the printed page range that feeds each file, and the determination fields from both citation JSON records (`distribution`, `determinationType`, `containsThirdPartyMaterial`). Tasks 2, 3, and 4 copy those values. They do not re-decide them. `SOURCE_PAGES` is `PAGE_COUNT_1 + PAGE_COUNT_2`.

**Model:** standard

Per-task brief: `.superpowers/sdd/2026-10-28-rebuild-nasa-risk-handbook-v2/task-1-brief.md`

- [ ] **Step 1: Record the execution date and re-fetch both records and both PDFs**

```bash
python -c "import datetime; print(datetime.date.today().isoformat())"
```

Call that date `VET_DATE`. It must be `YYYY-MM-DD`. It is `build.built_on`. Do not hard-code `2026-10-28` unless that is the date the command prints.

Download both citation APIs and both PDFs. Do not `pip install` anything.

```bash
mkdir -p sources/nasa-risk
curl -fsSL -o sources/nasa-risk/citation-20240014019.json "https://ntrs.nasa.gov/api/citations/20240014019"
curl -fsSL -o sources/nasa-risk/citation-20240014326.json "https://ntrs.nasa.gov/api/citations/20240014326"
curl -fsSL -o sources/nasa-risk/SP-20240014019.pdf "https://ntrs.nasa.gov/api/citations/20240014019/downloads/SP-20240014019.pdf"
curl -fsSL -o sources/nasa-risk/SP-20240014326.pdf "https://ntrs.nasa.gov/api/citations/20240014326/downloads/SP-20240014326.pdf"
python -c "
import hashlib, json, pathlib
root = pathlib.Path('sources/nasa-risk')
for name in ('SP-20240014019.pdf', 'SP-20240014326.pdf'):
    data = (root / name).read_bytes()
    print(name, 'bytes', len(data), 'head', data[:8], 'sha256', hashlib.sha256(data).hexdigest())
for name in ('citation-20240014019.json', 'citation-20240014326.json'):
    rec = json.loads((root / name).read_text(encoding='utf-8'))
    print(name, 'distribution', rec.get('distribution'), 'copyright', rec.get('copyright'))
"
```

Expected: both heads start with `b'%PDF'`. Record `BYTE_SIZE_1` and `BYTE_SIZE_2`. The spec's 14,471,540 and 6,669,330 are a check, not a lock. A different size is not a stop if the file is a PDF and D2 holds.

Confirm from the citation JSON, not from the spec:

- Both records have `distribution` equal to `PUBLIC`.
- Neither record has `copyright.containsThirdPartyMaterial` true.
- Record `determinationType` from each. Spec expected `PUBLIC_USE_PERMITTED` on 20240014019. A different determination type is a stop. Record the fields; Task 2 copies them into `PACK.yaml` `notes`.

Extract text. Prefer `pdftotext -layout` if `command -v pdftotext` succeeds. Otherwise use an already-installed reader (`pypdf` or `fitz`). Do not `pip install` a PDF library. If no reader is available, stop and report. Write the extracts to `sources/nasa-risk/part1.txt` and `sources/nasa-risk/part2.txt`. Record `PAGE_COUNT_1` and `PAGE_COUNT_2` from the reader, not from the spec. The spec's 303 and 89 are a check, not a lock.

Confirm from the PDF text, not from the spec:

- Part 1 page 2 contains the sentence that NASA SP-20240014019 Version 2 supersedes NASA SP-2011-3422 Version 1 dated November 2011.
- Cover date on both volumes is Version 2.0, November 2024. If the cover date disagrees, stop. Do not rewrite the pin.
- Part 2 verso may print `SP-202400114326`. That token is a typo. Pin NASA/SP-20240014326. Do not copy the typo into any pack file.

Stop and report, without writing chapter prose and without deleting the old chapters, if any of these hold:

- Either PDF URL is dead, or either fetch is not HTTP 200.
- Either file is not a PDF (`%PDF` missing).
- Either NTRS record is no longer `distribution: PUBLIC`.
- Either record sets `containsThirdPartyMaterial` true.
- Either record's `determinationType` is not `PUBLIC_USE_PERMITTED`.
- The Part 1 supersession sentence is absent.
- The November 2024 cover date is absent on either volume.

The 2026-10-28 spec fetch is not a substitute for this re-fetch.

- [ ] **Step 2: Freeze 6 to 8 chapter titles from the contents lists**

Read the contents list in `sources/nasa-risk/part1.txt` (page iv) and `sources/nasa-risk/part2.txt` (page iv). Produce 6, 7, or 8 rows. Each row has a basename `chNN-kebab-title.md` and the printed page range that feeds it, naming which PDF.

Rules:

- The PDF contents lists win over the provisional table in Research.
- One file per Part 1 numbered chapter, excluding chapter 7 Definitions. Definitions fold into `glossary.md` in Task 2. Do not write a chapter whose only job is the definitions list.
- One file for Part 2 chapters 1 through 4. Do not split Part 2 into four files.
- Do not split Part 1 chapter 4's RIDM steps into three files.
- Appendices A through I are not chapters. Fold a defined term an appendix adds into the glossary in Task 2. Do not write an appendix chapter.
- Subsections stay inside the parent chapter.
- Floor 6, ceiling 8. If Part 1 gains or loses a numbered chapter, follow the list and keep Definitions out of `chapters/`.
- If the body cannot be covered in 6 to 8 chapters without inventing a theme, stop and report both contents lists. Do not write a ninth chapter. Do not delete the old chapters.

Basenames must match `^ch[0-9]{2}-[a-z0-9-]+\.md$`. Expected outcome, discarded if the lists disagree:

- `ch01-introduction-and-scope.md` (Part 1 ch 1)
- `ch02-objectives-driven-framework.md` (Part 1 ch 2)
- `ch03-risk-models-and-posture.md` (Part 1 ch 3)
- `ch04-risk-informed-decision-making.md` (Part 1 ch 4)
- `ch05-continuous-risk-management.md` (Part 1 ch 5)
- `ch06-organizational-integration.md` (Part 1 ch 6)
- `ch07-application-examples.md` (Part 2 ch 1-4)

Save the frozen list in the executor notes that Tasks 2, 3, and 4 will read. Call the file count `CHAPTER_COUNT`. Call `SOURCE_PAGES` = `PAGE_COUNT_1 + PAGE_COUNT_2`.

- [ ] **Step 3: Delete the ten old chapter files**

Only after Steps 1 and 2 pass. Do not delete if the vet stopped.

```bash
rm -f \
  packs/nasa-risk/chapters/ch01-introduction-and-rm-overview.md \
  packs/nasa-risk/chapters/ch02-ridm-crm-integration.md \
  packs/nasa-risk/chapters/ch03-ridm-part1-identification-of-alternatives.md \
  packs/nasa-risk/chapters/ch04-ridm-part2-risk-analysis-of-alternatives.md \
  packs/nasa-risk/chapters/ch05-ridm-part3-risk-informed-selection.md \
  packs/nasa-risk/chapters/ch06-crm-initialisation-and-planning.md \
  packs/nasa-risk/chapters/ch07-crm-identify-and-analyze.md \
  packs/nasa-risk/chapters/ch08-crm-plan-step.md \
  packs/nasa-risk/chapters/ch09-crm-track-control-communicate.md \
  packs/nasa-risk/chapters/ch10-enterprise-risks-and-appendices.md
python -c "
import pathlib
left = sorted(p.name for p in pathlib.Path('packs/nasa-risk/chapters').glob('*.md'))
assert left == [], left
print('old chapters gone')
"
git check-ignore -v sources/nasa-risk/SP-20240014019.pdf
git ls-files sources/
```

Expected: `old chapters gone`, the ignore rule matches the PDF, and `git ls-files sources/` is empty. Do not commit the PDFs, the extracts, or the citation JSON.

---

### Task 2: Write the new chapters and rebuild SKILL.md, PACK.yaml, LICENSE, glossary, cheatsheet, patterns

**Gate:** gate-enforced (validate_pack, check_pack_quality, URL scan, 14-gram scan).

**Files:**
- Create: `packs/nasa-risk/chapters/chNN-<slug>.md` (the frozen list from Task 1)
- Modify: `packs/nasa-risk/PACK.yaml`
- Modify: `packs/nasa-risk/LICENSE`
- Modify: `packs/nasa-risk/SKILL.md`
- Modify: `packs/nasa-risk/glossary.md`
- Modify: `packs/nasa-risk/cheatsheet.md`
- Modify: `packs/nasa-risk/patterns.md`
- Read: `sources/nasa-risk/part1.txt`, `sources/nasa-risk/part2.txt` (do not commit)

**Interfaces:**
- Consumes: frozen basenames, page ranges, `CHAPTER_COUNT`, `SOURCE_PAGES`, `BYTE_SIZE_1`, `BYTE_SIZE_2`, `PAGE_COUNT_1`, `PAGE_COUNT_2`, `VET_DATE`, and the NTRS determination fields from Task 1.
- Produces: chapter files whose basenames later tasks copy into classification rows, with the `.md` suffix. SKILL.md Topic Index `chNN` tokens must match those basenames. `PACK.yaml` `source_version` is the string Task 3 copies into the catalog row and Task 3 passes to `--record`: `Version 2.0 (November 2024)`. `PACK.yaml` `title` is the string Task 3 copies into the catalog `title`.

**Model:** standard

Per-task brief: `.superpowers/sdd/2026-10-28-rebuild-nasa-risk-handbook-v2/task-2-brief.md`

- [ ] **Step 1: Write `packs/nasa-risk/PACK.yaml`**

Replace `VET_DATE`, `SOURCE_PAGES`, `CHAPTER_COUNT`, `BYTE_SIZE_1`, `BYTE_SIZE_2`, `PAGE_COUNT_1`, and `PAGE_COUNT_2` with the values from Task 1. `CHAPTER_COUNT` is 6, 7, or 8. `SOURCE_PAGES` is the sum of the two page counts, 392 only if the re-fetch returned 303 and 89.

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
build:
  method: "Synthesized from NASA/SP-20240014019 and NASA/SP-20240014326, vetted on VET_DATE. Not adapted from the 2011 extraction."
  source_pages: SOURCE_PAGES
  chapters: CHAPTER_COUNT
  built_on: "VET_DATE"
notes: >
  US Government work, 17 U.S.C. 105. Public domain in the United States.
  No attribution duty. Courtesy attribution only. NASA does not endorse
  this pack. Part 1 NASA/SP-20240014019, BYTE_SIZE_1 bytes, PAGE_COUNT_1
  pages. Part 2 NASA/SP-20240014326, BYTE_SIZE_2 bytes, PAGE_COUNT_2 pages.
  Vetted on VET_DATE. NTRS distribution PUBLIC. determinationType
  PUBLIC_USE_PERMITTED. containsThirdPartyMaterial false on both records.
  Part 1 states that NASA SP-20240014019 Version 2 supersedes NASA
  SP-2011-3422 Version 1 dated November 2011. Do not pin the Part 2 verso
  typo SP-202400114326. NPR 8000.4, NPD 1000.0, NPR 7120.5, and NPR 8715.3
  are named as the policy the handbook aligns to. They are not quoted and
  not rebuilt. Domain PRA methods are a pointer to nasa-pra
  (NASA/SP-2011-3421), not a chapter here. Source identification and the
  reconstructed-notes statement are in packs/nasa-risk/LICENSE.
change_indication: "reconstructed as synthesized reference notes"
```

No `source_url` key. No URL anywhere in the file. `source_pages` and `chapters` are bare integers. Mandatory fields above `build:` stay column-0 scalars. The YAML parser reads only column-0 `key: value` lines and skips folded `>` blocks. Do not copy the Part 2 verso typo into this file. Do not invent a copyright legend the PDF does not print. The `notes` block is the D2 manifest.

- [ ] **Step 2: Write `packs/nasa-risk/LICENSE`**

Replace the 2011 identification. Keep the existing section order. No download URL, same rule as `docs/LICENSING.md`.

```text
nasa-risk pack: content licence
=================================

This pack is derived from:
NASA Risk Management Handbook, Version 2.0 (November 2024)
Part 1 NASA/SP-20240014019 and Part 2 NASA/SP-20240014326
NASA

Source licence: Public Domain (US Government work, 17 U.S.C. 105) (tier 1, see ../../docs/SOURCE-VETTING.md)
No source-material download link is published (see ../../docs/LICENSING.md).

This source work is a work of the United States Government, prepared by NASA, and
is therefore NOT subject to copyright protection in the United States (17 U.S.C. 105).
It is in the public domain: anyone may reproduce, transform, and redistribute it for
any purpose, including commercially, without permission.

The pin was verified on VET_DATE: Part 1 BYTE_SIZE_1 bytes, PAGE_COUNT_1 pages;
Part 2 BYTE_SIZE_2 bytes, PAGE_COUNT_2 pages. NTRS distribution PUBLIC,
determinationType PUBLIC_USE_PERMITTED, containsThirdPartyMaterial false.
Part 1 states that NASA SP-20240014019 Version 2 supersedes NASA SP-2011-3422
Version 1 dated November 2011. The Part 2 verso typo SP-202400114326 is not the pin.

Attribution to NASA is provided as a courtesy (see the repository NOTICE), not a legal
obligation. NASA does not endorse this pack or its authors.

NPR 8000.4, NPD 1000.0, NPR 7120.5, and NPR 8715.3 are named as the policy the
handbook aligns to. They are not quoted. Domain PRA methods stay a pointer to
nasa-pra (NASA/SP-2011-3421).

NOTE: this file governs the CONTENT of the pack. The repository tooling is licensed
separately under the MIT licence (see ../../LICENSE).
```

Replace `VET_DATE` and the four size tokens with Task 1 values. No `http://` or `https://` in the file.

- [ ] **Step 3: Write one chapter file per frozen row**

For each frozen row, write `packs/nasa-risk/chapters/<basename>`. Open with a `Sources:` line naming the volume and the printed page range. Then an H1 equal to the working title. Then prose of at least 30 lines.

Synthesis rules:

- Synthesize. Do not paste a run of more than one source sentence. A short defined term may be kept and marked as a defined term.
- Do not copy tables as reconstructed shall-lists. Describe the decision rule in prose.
- Name NPR 8000.4, NPD 1000.0, NPR 7120.5, and NPR 8715.3 where the page range names them. Do not quote their clause text. Do not rebuild them.
- Domain PRA methods (fault trees, event trees, Bayesian inference) are a pointer to `nasa-pra` (NASA/SP-2011-3421), not a section here. If Part 1 names a newer PRA document, name that document and still point at `nasa-pra` for the quantitative pack this repo ships. Do not quote PRA guide text.
- Do not embed page images. Do not copy the Part 2 verso typo `SP-202400114326` into any chapter.
- Ground every claim in the page range for that chapter. Do not borrow another chapter's range to fill length.
- Chapter section shape, in order, when the source supports the heading: `Core Idea`, `Frameworks Introduced`, `Key Concepts`, `Mental Models`, `Anti-patterns` (only if the source states a refusal), `Key Takeaways`, `Connects To`. Skip a heading the page range does not support. Do not invent a framework the PDF does not contain.
- The Part 2 examples chapter illustrates Part 1. It does not add doctrine.
- No `http://` or `https://` in any chapter.

If a frozen row's page range has no usable prose, stop and report. Do not write a stub under 30 lines.

- [ ] **Step 4: Rewrite the three support files**

`glossary.md`: absorb Part 1 chapter 7 Definitions and the acronym list. Alphabetical. Each entry names the `chNN` that uses it. No URLs. This file keeps an `is_support: true` row in Task 3. It is not a chapter.

`cheatsheet.md`: absorb the RIDM six steps and the CRM five steps plus communicate-and-document, described in prose, not copied as page images. No URLs. Support row, not a chapter.

`patterns.md`: absorb risk-leadership and graded-approach moves the handbook states. No URLs. Support row, not a chapter.

No fourth support file. Do not write a chapter whose only job is the definitions list.

- [ ] **Step 5: Rewrite `packs/nasa-risk/SKILL.md`**

Frontmatter `name` stays `nasa-risk`. Description names Version 2.0 and both SP numbers, states RIDM and CRM plus risk leadership, and keeps the existing limit.

```yaml
---
name: nasa-risk
description: "Knowledge pack synthesized from NASA Risk Management Handbook, Version 2.0 (November 2024; NASA/SP-20240014019 Part 1, NASA/SP-20240014326 Part 2): RIDM, CRM, and risk leadership. SCOPE LIMITS: single-source (the two November 2024 volumes); domain PRA methods (fault trees, event trees, Bayesian inference) are not this pack, see nasa-pra (NASA/SP-2011-3421); NPR 8000.4, NPD 1000.0, NPR 7120.5, and NPR 8715.3 named, not quoted; reconstructed reference notes, not NASA guidance, and no NASA endorsement."
---
```

If Part 1 names a newer PRA document as the current PRA pointer, name that document in the description and still point the skill at `nasa-pra`. Do not point at a 2002 PRA guide citation unless Part 1 itself names that older guide as the current pointer.

Body order:

1. H1: `NASA Risk Management Handbook, Version 2.0`
2. A `**Source:**` line naming the public-domain status, both SP numbers, November 2024, and a relative link `[LICENSE](LICENSE)`. No absolute URL. No download URL.
3. `## When to use` then, on the next line, `**Prerequisites:**` none, plain Markdown. Then one paragraph: use this skill for questions about NASA risk-informed decision making, continuous risk management, and risk leadership. It does not cover domain PRA methods. Those stay in `nasa-pra`.
4. `## How to use this skill`: four bullets. With no arguments, read Core Frameworks. For a topic, use the Topic Index. For a life-cycle question, use the Chapter Index. For a term, use `glossary.md`. For a decision rule, use `cheatsheet.md`. For a leadership or graded-approach move, use `patterns.md`.
5. `## Core Frameworks & Mental Models`: two to four subsections drawn only from the PDFs (objectives-driven framework, risk leadership, RIDM six steps, CRM steps plus communicate-and-document). Do not invent a framework the PDFs do not contain. Do not keep the 2011 "four mission execution domains" framing unless Part 1 still states it.
6. `## Chapter Index`: one line per frozen chapter, linking `chapters/<basename>`.
7. `## Topic Index`: keyword lines whose `chNN` tokens match the frozen basenames. Cover RIDM, CRM, risk leadership, graded approach, risk posture, and the Part 2 examples, plus any extra top-level section Task 1 kept. Every `chNN` token must resolve to a file `check_pack_quality.py` can see.
8. `## Supporting Files`: `glossary.md`, `cheatsheet.md`, and `patterns.md`, one line each.
9. `## Scope & Limits`: source version and `VET_DATE`; Version 2.0 only; domain PRA methods are `nasa-pra`; policy documents named, not quoted; not official NASA guidance.

No `http://` or `https://` in the file. No `SP-2011-3422` in the file.

- [ ] **Step 6: Run the pack gates and the 14-gram scan**

```bash
python tooling/validate_pack.py packs/nasa-risk
python tooling/check_pack_quality.py packs/nasa-risk
python -c "
import pathlib, re
root = pathlib.Path('packs/nasa-risk')
bad = []
for p in root.rglob('*'):
    if p.is_file():
        text = p.read_text(encoding='utf-8')
        if 'https://' in text or 'http://' in text:
            bad.append(str(p))
        if 'SP-2011-3422' in text or 'SP-202400114326' in text:
            bad.append('old-or-typo ' + str(p))
assert not bad, bad
n = len(list((root / 'chapters').glob('*.md')))
assert 6 <= n <= 8, n
print('pack clean', n, 'chapters')
"
```

Expected: `validate_pack.py` exits 0, `check_pack_quality.py` prints `PASS  nasa-risk` and exits 0, and the scan prints `pack clean` with the Task 1 count.

14-gram scan against both extracts. Zero contiguous runs of 18 or more words. A short defined term is not a run.

```bash
python -c "
import pathlib, re
def words(text):
    return re.findall(r\"[A-Za-z][A-Za-z0-9'-]*\", text.lower())
def grams(seq, n):
    return {' '.join(seq[i:i+n]) for i in range(max(0, len(seq) - n + 1))}
src_seq = words(pathlib.Path('sources/nasa-risk/part1.txt').read_text(encoding='utf-8', errors='replace'))
src_seq += words(pathlib.Path('sources/nasa-risk/part2.txt').read_text(encoding='utf-8', errors='replace'))
src_g = grams(src_seq, 18)
hits = []
for p in sorted(pathlib.Path('packs/nasa-risk/chapters').glob('*.md')):
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
- Modify: `catalog.json` (nasa-risk row only)
- Modify: `docs/classification-rules.json`
- Modify: `docs/capability-pack-map-note-overrides.json`
- Modify: `tooling/generate_capability_map.py` (four `744` literals only)
- Modify: `docs/source-watchlist.json` (nasa-risk `document`, then `--record`)
- Modify: `NOTICE` (`[pack: nasa-risk]` block only)
- Modify: `CHANGELOG.md` (one Changed bullet)
- Modify: `SKILLS.md` (nasa-risk description only)
- Modify: `README.md` (nasa-risk chapter-count cell only)
- Modify: `docs/superpowers/backlog.md` (line 101 evidence cell only)
- Regenerated, do not hand-edit: `docs/capability-pack-map.json`, `docs/capability-pack-map.md`, `docs/packs/nasa-risk/index.html`, `docs/packs.html`, `docs/sitemap.xml`

**Interfaces:**
- Consumes: `CHAPTER_COUNT`, `VET_DATE`, frozen basenames with the `.md` suffix, and the pin strings from Task 2 (`source_version` `Version 2.0 (November 2024)`, `title` as written in PACK.yaml).
- Produces: notes length `744 - 10 + CHAPTER_COUNT` (741 when `CHAPTER_COUNT` is 7), matching assignment length, watchlist `version` equal to catalog `source_version`, and a regenerated map. Later tasks do not hand-edit the generated JSON, Markdown, or HTML.

**Model:** standard

Per-task brief: `.superpowers/sdd/2026-10-28-rebuild-nasa-risk-handbook-v2/task-3-brief.md`

- [ ] **Step 1: Replace the catalog nasa-risk row**

Edit the existing `nasa-risk` object in `catalog.json` `packs`. Do not add a row. Do not change `"updated"` (`2026-10-14`). Do not add `source_url`. Do not touch the `nasa-pra` object. Keys stay in this order:

```json
{
  "slug": "nasa-risk",
  "title": "NASA Risk Management Handbook, Version 2.0 (NASA/SP-20240014019, NASA/SP-20240014326)",
  "publisher": "NASA",
  "source_version": "Version 2.0 (November 2024)",
  "license": "Public Domain (US Government work)",
  "license_tier": 1,
  "commercial_use": true,
  "chapters": CHAPTER_COUNT,
  "status": "live"
}
```

`CHAPTER_COUNT` is the integer from Task 1, not the token. `license` stays the shorter catalog form. Do not lengthen it to the PACK.yaml form. `title` must equal PACK.yaml `title`. `source_version` must equal PACK.yaml `source_version`. Keep JSON valid. Pack count stays 74.

- [ ] **Step 2: Delete every nasa-risk row, then append the new set**

Count before editing. Both files must report 13, and both files must report 744.

```bash
python -c "
import json, pathlib
rules = json.loads(pathlib.Path('docs/classification-rules.json').read_text(encoding='utf-8'))
ov = json.loads(pathlib.Path('docs/capability-pack-map-note-overrides.json').read_text(encoding='utf-8'))
ra = [a for a in rules['assignments'] if a['pack']=='nasa-risk']
rn = [a for a in ov['notes'] if a['pack']=='nasa-risk']
print('assign', len(rules['assignments']), 'nasa-risk', len(ra))
print('notes', len(ov['notes']), 'nasa-risk', len(rn))
assert len(ra)==13 and len(rn)==13
assert len(rules['assignments'])==744 and len(ov['notes'])==744
assert {a['chapter'] for a in ra} == {a['chapter'] for a in rn}
print('pre-edit ok')
"
```

Expected: `pre-edit ok`. If the counts are not 13 and 744, stop. Do not edit. The arithmetic in this step assumes those counts.

Then delete every object whose `pack` is `nasa-risk` from `docs/classification-rules.json` `assignments` and from `docs/capability-pack-map-note-overrides.json` `notes`. Append, in both files, one object per frozen chapter file and one object per surviving support file. Same `pack` and `chapter` in both files. `chapter` is the basename with `.md`.

Assignment object, one per frozen chapter:

```json
{"pack": "nasa-risk", "chapter": "chNN-slug.md", "cluster": "Risk Management", "is_support": false}
```

`cluster` stays `Risk Management` unless that chapter's best fit is a different name already in `cluster_names`. Do not invent a cluster.

Support assignments, all three, `is_support` true, cluster `Risk Management`:

```json
{"pack": "nasa-risk", "chapter": "glossary.md", "cluster": "Risk Management", "is_support": true}
{"pack": "nasa-risk", "chapter": "cheatsheet.md", "cluster": "Risk Management", "is_support": true}
{"pack": "nasa-risk", "chapter": "patterns.md", "cluster": "Risk Management", "is_support": true}
```

Note object, one per frozen chapter. One sentence, no em dash, no spaced double hyphen used as a dash, and the sentence says the note is from Version 2.0 November 2024. No URL.

```json
{"pack": "nasa-risk", "chapter": "chNN-slug.md", "note": "One sentence from Version 2.0 November 2024 naming what this chapter covers."}
```

Support notes stay short labels, same shape as the three being replaced:

```json
{"pack": "nasa-risk", "chapter": "glossary.md", "note": "Glossary for pack"}
{"pack": "nasa-risk", "chapter": "cheatsheet.md", "note": "Cheatsheet for pack"}
{"pack": "nasa-risk", "chapter": "patterns.md", "note": "Patterns for pack"}
```

Set `generated_on` on both files to `VET_DATE`. Leave `map_version` at `1.22.0`. Do not touch any other pack's rows.

After the edit, both lists have length `744 - 10 + CHAPTER_COUNT`. Support rows do not change the total: 3 removed, 3 added. At the expected `CHAPTER_COUNT` of 7, length is 741. Key sets match.

```bash
python -c "
import json, pathlib
rules = json.loads(pathlib.Path('docs/classification-rules.json').read_text(encoding='utf-8'))
ov = json.loads(pathlib.Path('docs/capability-pack-map-note-overrides.json').read_text(encoding='utf-8'))
ra = [a for a in rules['assignments'] if a['pack']=='nasa-risk']
rn = [a for a in ov['notes'] if a['pack']=='nasa-risk']
chapters = sorted(p.name for p in pathlib.Path('packs/nasa-risk/chapters').glob('*.md'))
content = [a for a in ra if not a['is_support']]
support = sorted(a['chapter'] for a in ra if a['is_support'])
assert [a['chapter'] for a in content] or True
assert sorted(a['chapter'] for a in content) == chapters
assert support == ['cheatsheet.md', 'glossary.md', 'patterns.md']
assert { (a['pack'], a['chapter']) for a in ra } == { (a['pack'], a['chapter']) for a in rn }
assert len(rules['assignments']) == len(ov['notes'])
assert len(rules['assignments']) == 744 - 10 + len(chapters)
assert rules['map_version'] == '1.22.0'
assert ov['map_version'] == '1.22.0'
print('rows', len(rules['assignments']), 'chapters', len(chapters))
"
```

Expected: `rows` equals `734 + CHAPTER_COUNT`, and `chapters` equals `CHAPTER_COUNT`.

- [ ] **Step 3: Move the four 744 literals**

`NEW` is `744 - 10 + CHAPTER_COUNT`. At the expected 7, `NEW` is 741. In `tooling/generate_capability_map.py`, replace `744` at the docstring (line 9), the combined comparison (line 195), the length comparison (line 203), and the error string (line 204). Do not change any other number in the file. Do not change `map_version`.

```bash
python -c "
import pathlib
text = pathlib.Path('tooling/generate_capability_map.py').read_text(encoding='utf-8')
print('744 count', text.count('744'))
"
```

Expected: `744 count 0`. If `744` remains, the generator will reject the new note file. Do not edit the generator beyond those four literals.

- [ ] **Step 4: Regenerate the map and check it**

`generated_on` on both JSON files is already `VET_DATE` from Step 2. Then:

```bash
python tooling/generate_capability_map.py --generated-on VET_DATE --sync-md
python tooling/check_capability_map.py
python tooling/check_classification_rules.py
```

Expected: three exit 0. If the generator reports `notes length must be 744`, Step 3 missed a literal. If a check reports an assignment missing a note, the paired rows disagree. Fix the rows. Do not edit the generator beyond the four literals. Do not hand-edit `docs/capability-pack-map.json` or `docs/capability-pack-map.md`.

- [ ] **Step 5: Hand-edit watchlist document, then record**

CAUTION: no gate compares watch `version` to catalog `source_version`. Record only after Step 1, so the manual diff in Step 8 has a fixed reference.

In `docs/source-watchlist.json`, on the `nasa-risk` object only, set `document` to `NASA Risk Management Handbook`. Leave `publisher` as `NASA`. Leave `hint` as `""`. Do not edit the `nasa-pra` object. Do not pass a URL.

Then:

```bash
python tooling/check_source_watch.py --record nasa-risk "Version 2.0 (November 2024)" VET_DATE
python tooling/check_source_watch.py
```

`VET_DATE` is the Task 1 date, not the token. `--record` rewrites `version` and `last_checked`. It does not write `document`. Expected: `recorded nasa-risk` and then `check_source_watch.py` exits 0.

Confirm `nasa-pra` `version` is still the pre-cut mis-pin, byte for byte:

```text
NASA Risk Management Handbook Version 2.0 (November 2024; NASA/SP-20240014019 Part 1, NASA/SP-20240014326 Part 2)
```

If that string changed, restore it. This cut does not repair that row.

- [ ] **Step 6: NOTICE, CHANGELOG, SKILLS.md, README**

`NOTICE`: replace the `[pack: nasa-risk]` block only. Do not edit `[pack: nasa-pra]`. Do not edit `[pack: nasa-system-safety]`. Keep the courtesy-attribution sentence and the no-endorsement sentence.

```text
[pack: nasa-risk]

  Source : NASA Risk Management Handbook, Version 2.0 (November 2024)
           Part 1 NASA/SP-20240014019, Part 2 NASA/SP-20240014326
  Author : NASA
  Licence: Public Domain -- US Government work (17 U.S.C. 105)
  Changes: reconstructed as synthesized reference notes (not a reproduction)
  Terms  : public domain, no copyright. Attribution to NASA is courtesy, not
           obligation; NASA does not endorse this pack. See packs/nasa-risk/LICENSE.
```

The `--` in the Licence line matches the existing NOTICE block shape. It is a field separator, not prose. Do not spread it into other sentences.

`CHANGELOG.md`: under `## [Unreleased]`, add a `### Changed` heading if that heading is absent, then one bullet. Do not add an `## [x.y.z]` heading. Do not edit `## [1.23.0]`. Do not bump a version.

```markdown
### Changed
- `nasa-risk` rebuilt from NASA Risk Management Handbook, Version 2.0 (November 2024): Part 1 NASA/SP-20240014019 and Part 2 NASA/SP-20240014326. The November 2011 pin NASA/SP-2011-3422 is retired.
```

`SKILLS.md` line 24: replace the nasa-risk description so it names Version 2.0, both SP numbers, RIDM, CRM, and risk leadership, and points domain PRA methods at `nasa-pra`. Do not change line 9. Pack count stays `74 packs (+8 signposts, +1 orchestrator)`. Do not change the `nasa-pra` row.

`README.md` line 131: change `live (10 chapters)` to `live (CHAPTER_COUNT chapters)` on the `nasa-risk` row only. `CHAPTER_COUNT` is the integer from Task 1. Do not change the `packs-74` badge. Do not change any other row's chapter count, including rows that also say `(10 chapters)`.

- [ ] **Step 7: Shrink the backlog evidence cell**

`docs/superpowers/backlog.md` line 101, slug `source-watch-calibrate-and-wire-2`. Status stays `open`. Do not delete the row. Do not mark it `done`.

Replace the evidence cell. Drop `nasa-risk` from the parenthetical and from the watchlist-field list. State 13 findings remain. State `nasa-pra` watch `version` still carries the handbook V2.0 string and that string does not describe SP-2011-3421. Leave the other slugs in the list: sebok, nasa-se-handbook, nist-ssdf, nist-stat-handbook, dod-rio, nasa-schedule, dodaf, federal-bca, faa-ams-vv, mrl-deskbook.

Evidence cell, substance required:

```text
docs/source-watchlist.json version fields on the remaining drift rows (nasa-pra, sebok, nasa-se-handbook, nist-ssdf, nist-stat-handbook, dod-rio, nasa-schedule, dodaf, federal-bca, faa-ams-vv, mrl-deskbook); 13 findings remain after nasa-risk left this list on VET_DATE; nasa-pra watch version still carries the handbook Version 2.0 string and that string does not describe NASA/SP-2011-3421, so it is not a rebuild candidate for the nasa-risk cut; .zcode/source-watch/2026-10-12.md drift findings + addendum item 6
```

`VET_DATE` is the Task 1 date, not the token. Also drop `nasa-risk` from the summary cell's implication that 14 findings still stand: the summary should say 13 findings remain, not 14. Do not close the row.

- [ ] **Step 8: Generate pages and run the three-surface diff**

```bash
python tooling/gen_pack_pages.py --only nasa-risk
python tooling/gen_packs_page.py
```

`--only` rewrites `docs/packs/nasa-risk/index.html` and always rewrites `docs/sitemap.xml` from the full live catalog. It does not truncate the sitemap. Do not hand-edit the generated HTML.

Three-surface byte-match. No gate does this. Run it by hand.

```bash
python -c "
import json, pathlib
pack = pathlib.Path('packs/nasa-risk/PACK.yaml').read_text(encoding='utf-8')
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
row = next(p for p in cat['packs'] if p['slug']=='nasa-risk')
watch = json.loads(pathlib.Path('docs/source-watchlist.json').read_text(encoding='utf-8'))
w = next(s for s in watch['sources'] if s['slug']=='nasa-risk')
pra = next(s for s in watch['sources'] if s['slug']=='nasa-pra')
assert row['title'] == title, (row['title'], title)
assert row['source_version'] == ver, (row['source_version'], ver)
assert w['version'] == ver, (w['version'], ver)
assert w['document'] == 'NASA Risk Management Handbook'
assert str(row['chapters']) == field(pack, 'chapters')
assert cat['updated'] == '2026-10-14'
assert pra['version'] == 'NASA Risk Management Handbook Version 2.0 (November 2024; NASA/SP-20240014019 Part 1, NASA/SP-20240014326 Part 2)'
assert 'SP-2011-3422' not in pack
print('three-surface match', ver, 'chapters', row['chapters'])
"
```

Expected: `three-surface match Version 2.0 (November 2024)` and the Task 1 chapter count. If `version` and `source_version` differ, `--record` ran against the wrong string. Re-run Step 5. Do not edit `nasa-pra`.

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

Per-task brief: `.superpowers/sdd/2026-10-28-rebuild-nasa-risk-handbook-v2/task-4-brief.md`

- [ ] **Step 1: 2011-pin grep and the manual README / SKILLS.md check**

```bash
rg -n "SP-2011-3422" packs/nasa-risk catalog.json docs/source-watchlist.json NOTICE
rg -n "nasa-risk" docs/superpowers/backlog.md
rg -n "SP-202400114326" packs/nasa-risk NOTICE catalog.json
```

Expected: the first command prints nothing. The second command prints no hit on the `source-watch-calibrate-and-wire-2` row. Hits on other backlog rows are out of scope. Leave them. The third command prints nothing.

No sentinel test covers README or SKILLS.md. Read them and record the result in the run notes.

- `README.md` nasa-risk row says `live (CHAPTER_COUNT chapters)`, not `(10 chapters)`.
- `SKILLS.md` nasa-risk row names Version 2.0 and does not say 10 chapters.
- `SKILLS.md` line 9 still says `74 packs (+8 signposts, +1 orchestrator)`.

- [ ] **Step 2: Prose check**

```bash
python ~/.zcode/scripts/prose_check.py packs/nasa-risk/SKILL.md packs/nasa-risk/LICENSE packs/nasa-risk/glossary.md packs/nasa-risk/cheatsheet.md packs/nasa-risk/patterns.md packs/nasa-risk/chapters CHANGELOG.md NOTICE
```

Expected: exit 0, or every finding fixed or justified in the run notes. Zero em dashes in headings and body prose of the files this cut wrote. The NOTICE `Licence:` line keeps the existing `--` field separator. That is the block shape, not new prose. Do not spread it.

- [ ] **Step 3: Catalog counts, release gate, and the URL rule**

```bash
python tooling/test_catalog_live_set.py
python tooling/test_catalogue_count.py
python tooling/test_ci_gate.py
python tooling/check_release.py
python -c "
import pathlib
root = pathlib.Path('packs/nasa-risk')
bad = []
for p in root.rglob('*'):
    if p.is_file() and ('https://' in p.read_text(encoding='utf-8') or 'http://' in p.read_text(encoding='utf-8')):
        bad.append(str(p))
assert not bad, bad
cat = pathlib.Path('catalog.json').read_text(encoding='utf-8')
assert '\"updated\": \"2026-10-14\"' in cat or '\"updated\": \"2026-10-14\"' in cat
print('no urls in pack')
"
git ls-files sources/
```

Expected: the three catalog tests exit 0 (counts unchanged at 74/83). `check_release.py` prints `RELEASE CHECK: PASS` and exits 0, or its only new findings are outside this pack and get named in the run notes, not fixed here. `git ls-files sources/` is empty. `catalog.json` `updated` is still `2026-10-14`.

If `check_release.py` fails on a surface this cut owns, fix that surface and re-run. Do not bump `RELEASE-INFO.txt`. Do not bump either plugin `version`. Do not change `catalog.json` `updated`. Do not edit `packs/nasa-pra/`. Do not edit `packs/se/SKILL.md`. Do not commit unless the parent execution mode says commit. Do not push. Do not open a PR.

Chapter-file count is between 6 and 8. `build.chapters` equals that count. Catalog `chapters` equals that count. Notes length equals `744 - 10 + N`.

---

## Testing

All must pass before the cut is done. Commands are gates, not suggestions.

1. `python tooling/validate_pack.py packs/nasa-risk` and `python tooling/check_pack_quality.py packs/nasa-risk` exit 0. Floor is 30 lines per chapter. Topic Index `chNN` tokens resolve to the new chapter set.
2. `python tooling/test_catalog_live_set.py`, `python tooling/test_catalogue_count.py`, and `python tooling/test_ci_gate.py` exit 0. Counts stay 74/83. `catalog.json` `updated` stays `2026-10-14`.
3. `python ~/.zcode/scripts/prose_check.py` on the touched prose exits 0, or findings are fixed or justified.
4. 14-gram scan of the new chapters against both extracts: zero contiguous runs of 18 or more words.
5. `python tooling/check_classification_rules.py` exits 0. A coverage error on `nasa-risk` means a chapter file and an assignment row disagree.
6. `python tooling/check_capability_map.py` exits 0. Notes length equals `744 - 10 + N`.
7. `python tooling/generate_capability_map.py --generated-on <VET_DATE> --sync-md` regenerates without a notes-length refusal. Re-run the capability-map check after generation.
8. `python tooling/check_source_watch.py` exits 0. `nasa-risk` `version` equals catalog `source_version`. `nasa-pra` `version` is unchanged from the pre-cut string. CAUTION: no gate compares watch `version` to catalog `source_version`. The three-surface byte-match in Task 3 Step 8 is the check. Record only after the catalog row carries the new `source_version`.
9. `python tooling/check_release.py` exits 0, or its only new findings are outside this pack and get named, not fixed here.
10. `rg -n "SP-2011-3422" packs/nasa-risk catalog.json docs/source-watchlist.json NOTICE` returns nothing. Separately confirm `README.md` no longer says `(10 chapters)` for nasa-risk and the `SKILLS.md` row shows the new chapter count. No sentinel test covers README or SKILLS.md. Verify by eye and record the result in the run notes.
11. `rg -n "nasa-risk" docs/superpowers/backlog.md` returns no hit on the `source-watch-calibrate-and-wire-2` row. Hits on other rows are out of scope.
12. Chapter-file count is between 6 and 8. `build.chapters` equals that count. Catalog `chapters` equals that count.
13. No URL string in `PACK.yaml` or `catalog.json`. `git ls-files sources/` is empty.

Count formulas, not a hardcoded chapter total: content packs stay 74, skills stay 83, map assignments `744 - 10 + N` where N is the Task 1 chapter count (6, 7, or 8). At the expected N of 7, assignments are 741.

## Self-review

Spec coverage: D1 Task 1 Step 1 (both PDFs, NTRS number, typo not pinned) and Task 2 Step 1 (title and source_version). D2 Task 1 Step 1 (stop conditions) and Task 2 Steps 1 and 2 (tier-1 fields, notes manifest, no invented legend). D3 Global Constraints and Task 3 Step 5 (nasa-pra watch version asserted unchanged). D4 Task 2 Steps 3 and 6 (synthesized notes, 14-gram scan, named-not-quoted policy, PRA pointer). D5 Task 1 Step 2 (contents lists win, 6 to 8, Definitions out, Part 2 one file). D6 Task 2 Step 4 (three support files, no fourth). D7 Task 3 Steps 2, 3, and 4 (delete-then-append, four literals, regenerate). D8 Global Constraints and Task 4 Step 3 (counts stay, no version bump, `updated` stays `2026-10-14`). D9 Task 3 Steps 5 and 8 (hand-edit document, `--record` after catalog, manual three-surface diff). D10 Task 3 Step 7 (evidence shrink, status stays open). Testing items 1 through 13 are the Testing section and Task 4. Registration surfaces in Codebase context are Task 3 Steps 1, 6, and 8. Do not list copied Global Constraints.

Placeholder scan: no open slots, no deferred-work markers, no "similar to Task N" standing in for a step. `CHAPTER_COUNT`, `VET_DATE`, `SOURCE_PAGES`, `PAGE_COUNT_1`, `PAGE_COUNT_2`, `BYTE_SIZE_1`, and `BYTE_SIZE_2` are Task 1 outputs, not blanks. The pin string `Version 2.0 (November 2024)`, the title, and the NTRS numbers are copied from the spec. Catalog row key order matches the live nasa-risk row. Watchlist key order matches `ENTRY_KEYS`.

Type consistency: `source_version` is `Version 2.0 (November 2024)` in PACK.yaml, the catalog row, and the `--record` argument. `document` is `NASA Risk Management Handbook`, not the version string. `CHAPTER_COUNT` is the chapter-file count, used as `build.chapters`, catalog `chapters`, and the README cell. Notes length is `744 - 10 + CHAPTER_COUNT` in Task 3 Steps 2 and 3 and in Testing item 6. Support basenames are `glossary.md`, `cheatsheet.md`, `patterns.md` in Task 2 and Task 3. The nasa-pra watch version string in Task 3 Step 5 matches the live row.

Deviations from spec: none. `gen_pack_pages.py --only` always rewrites `docs/sitemap.xml` from the full live catalog, so the spec's "must not be the last generator run if it truncates" condition does not fire. The plan still finishes with `gen_packs_page.py`, which the spec also requires.
