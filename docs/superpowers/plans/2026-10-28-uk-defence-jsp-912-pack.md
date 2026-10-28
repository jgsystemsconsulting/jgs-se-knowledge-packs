# UK Defence JSP 912 Pack Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship `packs/jsp-912` as one live tier-2 Open Government Licence pack synthesized from JSP 912 Parts 1 and 2 (both V3.0 March 2024), and register it on every surface `jsp-936` already uses.

**Architecture:** Re-fetch the gov.uk publication page and both PDFs before any chapter prose. Freeze 6 to 10 chapter titles from the two contents lists, not from the spec's provisional map. Write reconstructed notes under `packs/jsp-912/` using the `jsp-936` licence shape and chapter shape. Register the pack on every surface `tooling/check_release.py` compares, and move the hard-coded 735-row pin in the capability-map generator to 735 plus the frozen chapter count. No new tooling.

**Tech Stack:** Markdown pack files, YAML frontmatter, JSON catalogue and map files, Python 3 stdlib tooling (`tooling/validate_pack.py`, `tooling/check_pack_quality.py`, `tooling/check_source_watch.py`, `tooling/generate_capability_map.py`, `tooling/check_capability_map.py`, `tooling/check_classification_rules.py`, `tooling/gen_pack_pages.py`, `tooling/gen_packs_page.py`, `tooling/check_release.py`). PDF text via `pdftotext` if present, else an already-installed reader. No new dependencies.

**Spec:** `docs/superpowers/specs/2026-10-28-uk-defence-jsp-912-pack.md`

Spec certificate sha256: `75ec38b628fe5bcfcc94dbd529b5b9bcf0fa5351c223924db1f86e7ae80714a3`.

## Global Constraints

- D1: Pin is JSP 912 Parts 1 and 2, both Version 3.0 March 2024, one pack. Do not drop Part 2. Do not split into two packs. Title carries the part. Chapter index orders Part-1-dominant chapters first, then Part-2-dominant chapters, with a both-drawing chapter placed beside its dominant neighbour. `PACK.yaml` `source_version` names both parts and the shared V3.0 (March 2024). The stale "Version 3.0 Oct 2021" line on the Part 1 cover is not the pin.
- D2: Licence class is Open Government Licence v3.0, `license_tier: 2`, `commercial_use: true`, `share_alike: false`, `attribution_required: true`, matching `jsp-936`. Re-fetch the publication page and both PDFs before prose. Record vet date, both byte sizes, both page counts, and the exception-scan result in `PACK.yaml` `notes`. Stop if the footer no longer states Open Government Licence v3.0, either PDF URL is dead, either body is not a PDF, either running footer is not V3.0 Mar 2024, or either PDF states an exception that removes the reuse grant from the body.
- D3: One pack, two parts (one slug, two source PDFs, one `LICENSE`). Chapters are not hard-split by part. A chapter may draw from Part 1, Part 2, or both, and its title names the part it primarily draws from. A both-drawing chapter names both. `SKILL.md` says which part a claim comes from. The chapter index keeps Part-1-dominant chapters before Part-2-dominant ones.
- D4: Reconstruction rule copies `jsp-936`. Synthesized reference notes. Short defined terms may be kept. No long verbatim passages. Name JSP 375, JSP 536, JSP 815, JSP 822, DEF-STANs, and third-party standards. Do not quote them. Do not embed PDF page images. HuFIMS names and URLs stay out of pack files except `LICENSE`.
- D5: Scope is Human Factors Integration in Defence acquisition: the human component of capability. Companion to `jsp-815` and `jsp-376`. Not a second Defence SMS. Not a second acquisition-safety policy. `SKILL.md` scope limits name those siblings and state they are not reproduced. Do not put `jsp-912` on the AI and cyber-physical row. HFI is not dependable-AI direction.
- D6: Chapter count is 6 to 10, files `chapters/chNN-<slug>.md`. Contents lists of both PDFs win over the provisional table. If a provisional theme is absent from both contents lists, do not write that chapter. If the lists force a merge to stay inside 10, merge. Do not exceed 10 files. Do not go under 6.
- D7: Full registration on every surface in Codebase context. Partial registration is the miss this package exists to avoid. `docs/candidate-packs.md` changes only row 4, the unranked-remainder sentence, and the `uk-defence-*` proposed-pack bullet.
- D8: b-41 stays `promoted`. Do not set status to `done`. Do not delete the row. After this plan is EXECUTED, the packages doc marks P57 done. The evidence cell gains the execution date and states that 940, 945, 816, 375, and 520 remain needs-info and are not built. 912 promotion is recorded there, not by closing b-41.
- D9: No new tooling, except the `735` literals in `tooling/generate_capability_map.py`, which become `735 + N` as plain integers where N is the chapter count frozen in Task 1. Do not bump `RELEASE-INFO.txt`, either plugin `version`, or `catalog.json` `updated`.
- Pin string, verbatim, in PACK.yaml `source_version`, catalog `source_version`, and watchlist `document` and `version` once vet confirms both running footers are V3.0 Mar 2024: `JSP 912 Human Factors Integration in Defence Systems, Part 1 Directive and Part 2 Guidance, V3.0 (March 2024)`. If either footer disagrees, stop. Do not rewrite the pin to match a different issue.
- Title, verbatim: `JSP 912: Human Factors Integration in Defence Systems (Parts 1 and 2)`. Publisher, verbatim: `Ministry of Defence`.
- `build.built_on` and watchlist `last_checked` are the execution date in `YYYY-MM-DD`, not a date copied from this plan's filename. `catalog.json` `updated` stays `2026-10-14`.
- No `source_url` in `PACK.yaml` or `catalog.json`. No URL in any file under `packs/jsp-912/` except `packs/jsp-912/LICENSE`.
- `build.chapters` equals the frozen chapter count. `build.method` says synthesized from the two JSP 912 PDFs, not adapted from a sibling prototype. `change_indication` is `reconstructed synthesized reference notes`.
- Chapter body at least 30 lines (`tooling/check_pack_quality.py` `MIN_CHAPTER_LINES`). Basenames match `^ch[0-9]{2}-[a-z0-9-]+\.md$`. SKILL.md frontmatter `name` is `jsp-912`.
- Cluster names come from `docs/classification-rules.json` `cluster_names`. Do not invent a cluster. `Human Systems Integration / Human Factors` is the live name. The spec's shorter "Human Systems Integration" is not in the list. Use the live name. One assignment per chapter file only. `glossary.md` and `cheatsheet.md` get no assignment or note rows. Note-override notes are one sentence, no em dash, and say the note is from JSP 912 V3.0 March 2024.
- Count move, live inventory before this cut (main, post-1.23.0): 73 content packs, 8 signposts, 1 orchestrator, 82 skills, 735 classification assignments. After this cut: content packs 74, skills 83, assignments `735 + N` where N is the chapter count frozen in Task 1 (6 to 10). Signposts stay 8. Orchestrator stays 1. `tooling/generate_capability_map.py` hard-codes `735` on lines 9, 195, 203, and 204. Those four literals must move, or the generator rejects the new note file. Do not hand-edit `docs/capability-pack-map.json` or `docs/capability-pack-map.md`.
- OGL packs are required on the `/se` Licences table. `tooling/check_release.py` errors if a non-Public-Domain content pack lacks a Licences row. Add one row for `jsp-912`. Do not add `jsp-912` to the AI and cyber-physical row.
- Defence safety management Topics row currently holds three packs (`jsp-815`, `jsp-376`, `jsp-936`). Adding `jsp-912` makes four, inside the six-pack cap stated in `packs/se/SKILL.md` line 190. Do not create a second Defence row. Do not edit neighbour pack keywords to make room.
- Do not (spec D9 and Non-goals, verbatim):
  - Do not bump `RELEASE-INFO.txt`.
  - Do not edit neighbour packs' chapter files.
  - Do not commit anything under `sources/`.
  - Do not bump plugin `version` or any release version file.
  - Do not change `catalog.json` `updated`. It stays `2026-10-14`.
- Also out: JSP 940, JSP 945, JSP 816, JSP 375, JSP 520, JSP 939, JSP 600, and any DEF-STAN. Changes to `jsp-815`, `jsp-376`, or `jsp-936` chapter prose. A second pack for Part 2, or a Part-1-only pack. New validators, new page templates, new licence tiers. Quoting JSP 375, JSP 536, JSP 815, JSP 822, or third-party standard text. Embedding PDF page images. `source_url` in `PACK.yaml` or `catalog.json`. GitHub release, plugin publish, or a commit this plan does not authorize.
- Stop-and-report, do not write chapters, if the gov.uk footer no longer says Open Government Licence v3.0, either PDF URL returns non-200, either body is not a PDF, either running footer is not V3.0 Mar 2024, or either PDF carves its body out of the OGL reuse grant. The 2026-10-28 fetch in the spec is not a substitute for the execution-time re-fetch.
- Commit steps are off unless the parent execution mode says commit. Do not push. Do not open a PR.
- Per-task briefs live at `.superpowers/sdd/uk-defence-jsp-912-pack/task-N-brief.md`. The controller writes them at dispatch. This plan does not create those files.

## Codebase context

Ad-hoc context, re-checked on the tree on 2026-10-28. Precedent for licence fields, chapter shape, glossary, cheatsheet, and SKILL.md is `packs/jsp-936/`. No sibling ships two PDFs. `jsp-815` is a single-PDF pack. This cut defines the two-PDF convention itself. Required content-pack layout is `docs/PACK-SPEC.md`.

- Pack contract: `packs/<slug>/{SKILL.md, PACK.yaml, LICENSE, chapters/chNN-*.md}`. Quality gate: chapter body at least 30 lines, no orphan chapter files, Topic Index `chNN` tokens resolve. `validate_pack.py` checks required files, frontmatter `name` equals folder slug, chapter links resolve, and mandatory PACK.yaml fields. The YAML parser reads only column-0 `key: value` lines and skips folded `>` blocks, so mandatory fields must be column-0 scalars.
- `packs/jsp-936/LICENSE` is the OGL template. Model the new LICENSE on it: attribution statement, source identification, publication URL, deed URL, reconstructed-notes statement, non-endorsement, excluded-material section, then the full OGL v3.0 text already in that file. Do not invent a shorter deed.
- Watchlist record mode rewrites an existing row. Usage:

  ```bash
  python tooling/check_source_watch.py --record SLUG VERSION DATE
  ```

  `record_entry` returns 1 when the slug is absent from the watchlist, and refuses when the watchlist and the live catalog disagree. Hand-insert the watchlist row and the catalog live row before that command. Coverage checks the live catalog against the watchlist in both directions. A planned catalog entry must not carry a URL.
- Routing map (`packs/se/SKILL.md`, markers `ROUTING-MAP:BEGIN` / `ROUTING-MAP:END`): Defence safety management row is line 118 and currently names `jsp-815`, `jsp-376`, `jsp-936`. Licences table rows for those three are lines 159 to 161. AI and cyber-physical row is line 107 and stays on `jsp-936`.
- Cursor plugin skills are `./packs/<slug>/SKILL.md`. Claude plugin skills are `./packs/<slug>`. Cursor check fails if an eligible pack (`commercial_use` not false) is missing. Claude plugin skills array is not count-gated. Spec D7 still requires the insert. Do not change either file's `version`. Cursor stays 1.22.0 (79 skills; the three `commercial_use: false` packs are absent on purpose). Claude stays 1.23.0 (82 skills). The cursor version gap is P60, not this cut.
- Catalogue count loci `check_catalogue_count` and `[pack-count]` compare: `docs/index.html` section 06 h2 `73 packs · 8 signposts`; chip COUNT sums to 73 (the chip parser adds every chip whose label does not contain `signpost` or `orchestrator`); `docs/assets/still-catalogue.svg` subtitle `73 packs · 8 signposts · open sources only` and footer `73 PACKS · 8 SIGNPOSTS · FILTER ON packs.html`; `docs/products/website/01-jgs-se-knowledge-packs.yaml` line 47 `73 packs across the SE catalogue`. The skills sentence in `docs/index.html` (`82 skills in all`: 73 knowledge packs) is not parsed by the chip regex, but it states the same inventory and must move with it. README badge `packs-73`.
- `SKILLS.md` line 9 says `73 packs (+8 signposts, +1 orchestrator)`. The new table row goes after the `jsp-936` row (line 80) and before the `fhwa-its-se` row (line 81).
- `NOTICE` OGL shape is the `[pack: jsp-936]` block. Insert the new block after that block and before `[pack: fhwa-its-se]`.
- `catalog.json` live row keys, in order, match `jsp-936`: `slug`, `title`, `publisher`, `source_version`, `license`, `license_tier`, `commercial_use`, `chapters`, `status`. `"updated"` is `2026-10-14` and must stay that string. Insert the new object after the `jsp-936` object. `fhwa-its-se` is the last live row. Do not append after it if that would split the UK family. After `jsp-936` is the insertion point.
- `docs/source-watchlist.json` keys, in order: `slug`, `publisher`, `document`, `version`, `last_checked`, `hint`. `hint` is `""`. No URL in any value. Insert after the `jsp-936` source, same position rule as the catalog.
- `docs/candidate-packs.md` row 4 is line 19. The unranked-remainder sentence is line 26. The catalogue-count sentence is line 30 (`82 packs: 73 full reconstructed content packs`). The `uk-defence-*` proposed-pack bullet is line 70.
- `docs/superpowers/backlog.md` b-41 is line 141. Status cell is `promoted`. Do not change that status word. Evidence cell already names P57 and says 940/945/816/375/520 remain needs-info. Append the execution date. Do not delete the row.
- `CHANGELOG.md` `## [Unreleased]` is empty. `## [1.23.0]` already shipped on 2026-10-28 and contains the `fhwa-its-se` and `jsp-936` bullets. Add the new bullet under `## [Unreleased]`. Do not add a version heading. Do not edit `## [1.23.0]`. The Changed bullet that says the plugin declares 82 skill paths is a historical release note. Do not rewrite it.
- UK chip in `docs/index.html` line 202 is `UK · 3` and already names JSP 815, JSP 376, JSP 936, plus a parenthetical that MHRA device software guidance is counted under EU / academic / JGS. Keep that parenthetical. Add JSP 912 to the span. Change the count to 4. Do not move MHRA into the UK count. The EU / academic / JGS chip stays 5.
- `docs/classification-rules.json` and `docs/capability-pack-map-note-overrides.json` both have `generated_on` `2026-10-28` and 735 rows. Hand-add one assignment and one note per frozen chapter. Do not hand-edit the generated map.
- PDF downloads and text extracts go under `sources/jsp-912/`. `sources/` is gitignored. `tooling/check_release.py` fails tracked extracts. `git ls-files sources/` must stay empty.

## Research

section-url (2026-10-28 research gate already pinned and licence-cleared both PDFs at page level; no new external research needed to write this plan. The build re-fetches the publication page and both PDFs at execution time.)

Page-level pin from the spec, not re-verified by this plan. Task 1 re-vets it:

- Publication page: https://www.gov.uk/government/publications/human-factors-integration-in-defence-systems-jsp-912
- Part 1 PDF: https://assets.publishing.service.gov.uk/media/6634dc9ccf3b5081b14f314b/JSP_912_Part_1_V3.0.pdf
- Part 2 PDF: https://assets.publishing.service.gov.uk/media/6634dcae1834d96a0aa6d0da/JSP_912_Part_2_V3.0.pdf
- OGL deed: https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- Publisher: Ministry of Defence. Published 3 February 2014. Page last updated 3 May 2024. Update note names Parts 1 and 2.
- Spec fetch on 2026-10-28: both PDFs HTTP 200, `%PDF-1.7`. Part 1: 360,991 bytes, 16 pages, running footer `JSP 912 Pt 1 (V3.0 Mar 24)`. Part 2: 1,326,830 bytes, 65 pages, running footer `JSP 912 Pt 2 (V3.0 Mar 24)`. Cover line "Version 3.0 Oct 2021" on Part 1 is stale and is not the pin. Page footer states Open Government Licence v3.0 except where otherwise stated, and Crown copyright. No withdrawn notice (grep the page HTML for `Withdrawn`: zero hits required). No login wall. "Reproduced" appears only as ordinary prose, not as a licence restriction.
- Task 1 records the execution-time byte sizes and page counts. The spec numbers are a check, not a lock, except the V3.0 Mar 2024 footer sentence, which is a stop condition.

Provisional chapter map, discarded wherever either contents list disagrees:

| Ch | Working title | Draws from |
|---|---|---|
| 01 | What HFI is and why Defence mandates it | Part 1 §1 and Part 2 §1 |
| 02 | HFI and systems engineering | Part 2 §1 and Part 2 §2 |
| 03 | HFI process goals, activities, tailoring | Part 1 §2 and Part 2 §2 and §4 |
| 04 | User need and system requirements (HFI-1.0, HFI-2.0) | Part 2 §3 |
| 05 | Tenders and detailed design (HFI-3.0, HFI-4.0) | Part 2 §3 |
| 06 | Test, acceptance, in-service feedback (HFI-5.0, HFI-6.0) | Part 2 §3 |
| 07 | Roles and responsibilities | Part 1 §3 and Part 2 §5 |
| 08 | Competencies, ethics, conduct | Part 1 §4 and Part 2 §6 |

References, acronym lists, and the Part 2 glossary do not become chapters. Fold defined terms into `glossary.md`. If HFI-4.0 is too large for one chapter with HFI-3.0, split provisional chapter 05 into two and drop nothing else: that is 9, still inside D6. If a contents heading above is absent on the execution-time extract, delete that chapter and merge its neighbour. Do not write a chapter neither contents list contains. Expected outcome is 6, 7, 8, 9, or 10 files. Eight is the provisional count, not a lock.

## File map

Create:

- `packs/jsp-912/PACK.yaml`
- `packs/jsp-912/LICENSE`
- `packs/jsp-912/SKILL.md`
- `packs/jsp-912/chapters/chNN-<slug>.md` (6 to 10 files, frozen in Task 1)
- `packs/jsp-912/glossary.md`
- `packs/jsp-912/cheatsheet.md`
- `sources/jsp-912/part1.pdf` (untracked; do not commit)
- `sources/jsp-912/part2.pdf` (untracked; do not commit)
- `sources/jsp-912/part1.txt` (untracked; do not commit)
- `sources/jsp-912/part2.txt` (untracked; do not commit)
- `docs/packs/jsp-912/index.html` (generator output; do not hand-write)

Modify:

- `catalog.json` (one live row; `"updated"` untouched)
- `docs/source-watchlist.json` (one source row)
- `SKILLS.md` (count line, one table row)
- `packs/se/SKILL.md` (Defence row keywords and pack cell, one Licences row)
- `.claude-plugin/plugin.json` (one skills entry; `version` untouched)
- `.cursor-plugin/plugin.json` (one skills entry; `version` untouched)
- `NOTICE` (one OGL block)
- `README.md` (badge, one table row)
- `docs/index.html` (section 06 h2, UK chip, skills sentence)
- `docs/assets/still-catalogue.svg` (subtitle, footer)
- `docs/products/website/01-jgs-se-knowledge-packs.yaml` (pack-count claim, UK MOD sentence)
- `docs/candidate-packs.md` (row 4, unranked-remainder sentence, catalogue-count sentence, `uk-defence-*` bullet)
- `docs/superpowers/backlog.md` (b-41 evidence cell only; status stays `promoted`)
- `docs/classification-rules.json` (N assignment rows)
- `docs/capability-pack-map-note-overrides.json` (N note rows)
- `tooling/generate_capability_map.py` (four `735` literals become `735 + N`)
- `docs/capability-pack-map.json` and `docs/capability-pack-map.md` (generator output only)
- `docs/packs.html` and `docs/sitemap.xml` (generator output only)
- `CHANGELOG.md` (one Unreleased bullet)

Do not touch: `docs/LICENSING.md`, `RELEASE-INFO.txt`, `tooling/validate_pack.py`, `tooling/check_release.py`, `tooling/check_pack_quality.py`, `.github/workflows/validate.yml`, `docs/products/website/catalog.yaml`, `packs/jsp-936/`, `packs/jsp-815/`, `packs/jsp-376/`, `packs/fhwa-its-se/`, `.claude-plugin/marketplace.json`.

---

### Task 1: Vet both PDFs, freeze the chapter map, write PACK.yaml and LICENSE

**Gate:** gate-enforced (skeleton assert, ignore check).

**Files:**
- Create: `packs/jsp-912/PACK.yaml`
- Create: `packs/jsp-912/LICENSE`
- Create: `sources/jsp-912/part1.pdf` (untracked)
- Create: `sources/jsp-912/part2.pdf` (untracked)
- Create: `sources/jsp-912/part1.txt` (untracked)
- Create: `sources/jsp-912/part2.txt` (untracked)
- Read: `packs/jsp-936/LICENSE` (structure only; do not edit)

**Interfaces:**
- Consumes: publication URL and both PDF URLs in Research. Stop conditions in Global Constraints D2.
- Produces: `CHAPTER_COUNT` (integer 6 to 10), `PAGE_COUNT_P1`, `PAGE_COUNT_P2`, `BYTE_SIZE_P1`, `BYTE_SIZE_P2`, `VET_DATE` (`YYYY-MM-DD`), frozen basenames `chNN-kebab-title.md` with part-dominance tags, and the pin string `JSP 912 Human Factors Integration in Defence Systems, Part 1 Directive and Part 2 Guidance, V3.0 (March 2024)`. Tasks 2, 3, 4, and 5 consume these. They do not re-decide them.

**Model:** standard

Per-task brief: `.superpowers/sdd/uk-defence-jsp-912-pack/task-1-brief.md`

- [ ] **Step 1: Record the execution date and re-fetch both PDFs**

```bash
python -c "import datetime; print(datetime.date.today().isoformat())"
```

Save the printed date as `VET_DATE`. It must be `YYYY-MM-DD`. It becomes `build.built_on` and watchlist `last_checked`. Do not hard-code `2026-10-28` unless the date command prints that.

Download both PDFs. Do not `pip install` anything.

```bash
mkdir -p sources/jsp-912
curl -fsSL -o sources/jsp-912/part1.pdf "https://assets.publishing.service.gov.uk/media/6634dc9ccf3b5081b14f314b/JSP_912_Part_1_V3.0.pdf"
curl -fsSL -o sources/jsp-912/part2.pdf "https://assets.publishing.service.gov.uk/media/6634dcae1834d96a0aa6d0da/JSP_912_Part_2_V3.0.pdf"
curl -fsSL -o sources/jsp-912/page.html "https://www.gov.uk/government/publications/human-factors-integration-in-defence-systems-jsp-912"
python -c "
import hashlib, pathlib
for name in ('part1.pdf', 'part2.pdf'):
    p = pathlib.Path('sources/jsp-912') / name
    data = p.read_bytes()
    print(name, 'bytes', len(data))
    print(name, 'sha256', hashlib.sha256(data).hexdigest())
    print(name, 'head', data[:5])
"
```

Expected: exit 0, both `head` values start with `b'%PDF'`. Record `BYTE_SIZE_P1` and `BYTE_SIZE_P2`. Spec checks, not locks: 360991 and 1326830. A different size is not a stop if the footer sentence in Step 1's confirm list is present.

Fetch the publication page the same way. Confirm, in `sources/jsp-912/page.html`:

- HTTP body contains `Open Government Licence v3.0` (the footer sense "All content is available under the Open Government Licence v3.0, except where otherwise stated").
- Body contains `Crown copyright`.
- Body does not contain a withdrawn notice.
- Both PDF filenames appear: `JSP_912_Part_1_V3.0.pdf` and `JSP_912_Part_2_V3.0.pdf`.

Extract text. Prefer `pdftotext -layout` if `command -v pdftotext` succeeds. Otherwise use an already-installed reader (`pypdf` or `fitz`). Do not `pip install` a PDF library. If no reader is available, stop and report. Write extracts to `sources/jsp-912/part1.txt` and `sources/jsp-912/part2.txt`.

Confirm from the extracts, not from the spec:

- Part 1 running footer contains `JSP 912 Pt 1 (V3.0 Mar 24)`.
- Part 2 running footer contains `JSP 912 Pt 2 (V3.0 Mar 24)`.
- Page counts recorded as `PAGE_COUNT_P1` and `PAGE_COUNT_P2`. Spec's 16 and 65 are a check, not a lock. A different count is not a stop if the Mar 2024 footer sentence is present.
- Neither PDF states an exception that removes the body from the Open Government Licence reuse grant. "Reproduced" as ordinary prose is not an exception. A line that reserves all rights, or that carves the body out of OGL, is an exception. Stop if you find one.
- The Part 1 cover line "Version 3.0 Oct 2021", if present, is recorded as stale and is not written into `source_version`.

Stop and report, without writing PACK.yaml, if the page footer no longer states Open Government Licence v3.0, either curl fails, either file does not start with `%PDF`, either running footer is not V3.0 Mar 2024, or either PDF carves its body out of the reuse grant. Do not treat the spec's 2026-10-28 fetch as this re-fetch.

- [ ] **Step 2: Freeze 6 to 10 chapter titles from both contents lists**

Read both contents lists in `sources/jsp-912/part1.txt` and `sources/jsp-912/part2.txt`. Write a frozen map of 6 to 10 rows. Each row has a basename `chNN-kebab-title.md`, a dominance tag (`part-1`, `part-2`, or `both`), and the printed page ranges that feed it.

Rules:

- Both contents lists win over the provisional table in Research.
- One file per frozen theme, not one file per PDF section number. Part 1 sections 5 (References) and 6 (Acronyms) do not become chapters. Part 2 glossary, references, and acronym lists do not become chapters. Fold defined terms into `glossary.md` in Task 2.
- Order: Part-1-dominant chapters first, then Part-2-dominant chapters. A both-drawing chapter sits beside its dominant neighbour. Provisional chapters 01, 03, 07, and 08 draw from both parts. Place each with the part it primarily draws from. Provisional 01 and 07 are Part-1-dominant. Provisional 03 and 08 are Part-2-dominant unless the extract shows otherwise. Say which, in the frozen map, in one line per chapter.
- If HFI-4.0 is too large to share a chapter with HFI-3.0, split provisional 05 into two files and drop nothing else.
- If a provisional theme is absent from both contents lists, delete that chapter and merge its neighbour. Do not write a chapter neither list contains.
- Do not exceed 10 files. Do not go under 6. If the body cannot be covered in 6 to 10 chapters without inventing a theme, stop and report both contents lists. Do not write an 11th chapter.
- Six named roles in Part 1 section 3 stay six. Do not invent a seventh role. Those roles land in the roles chapter and in the cheatsheet, not in six separate chapters.

Basenames must match `^ch[0-9]{2}-[a-z0-9-]+\.md$`. Save the frozen list to `.superpowers/sdd/2026-10-28-uk-defence-jsp-912-pack/executor-notes.md` (create the directory). Tasks 2, 3, and 4 read that file. Call the file count `CHAPTER_COUNT`.

- [ ] **Step 3: Write `packs/jsp-912/PACK.yaml`**

Replace `VET_DATE`, `PAGE_COUNT_P1`, `PAGE_COUNT_P2`, `BYTE_SIZE_P1`, `BYTE_SIZE_P2`, and `CHAPTER_COUNT` with the values from Steps 1 and 2. `CHAPTER_COUNT` is an integer from 6 to 10. `source_pages` is the sum of the two page counts, a bare integer.

```yaml
slug: jsp-912
title: "JSP 912: Human Factors Integration in Defence Systems (Parts 1 and 2)"
publisher: "Ministry of Defence"
source_version: "JSP 912 Human Factors Integration in Defence Systems, Part 1 Directive and Part 2 Guidance, V3.0 (March 2024)"
license: "Open Government Licence v3.0"
license_tier: 2
commercial_use: true
share_alike: false
attribution_required: true
build:
  method: "Synthesized from the JSP 912 Part 1 and Part 2 PDFs pinned on VET_DATE. Not adapted from a sibling prototype."
  source_pages: PAGE_SUM
  chapters: CHAPTER_COUNT
  built_on: "VET_DATE"
  notes: >
    Contains public sector information licensed under the Open Government
    Licence v3.0. Source: JSP 912 Human Factors Integration in Defence
    Systems, Part 1 Directive and Part 2 Guidance, V3.0 (March 2024).
    Ministry of Defence, Crown copyright. Reconstructed reference notes,
    not reproductions. No MOD endorsement implied. Vetted VET_DATE:
    publication page carried OGL v3.0 and Crown copyright; Part 1
    BYTE_SIZE_P1 bytes, PAGE_COUNT_P1 pages; Part 2 BYTE_SIZE_P2 bytes,
    PAGE_COUNT_P2 pages; PDF exception scan found no carve-out of the body
    from the reuse grant. Running footers V3.0 Mar 2024. The Part 1 cover
    line Version 3.0 Oct 2021, if present, is stale and is not the pin.
    JSP 375, JSP 536, JSP 815, JSP 822, DEF-STANs, and third-party
    standards are named and not quoted. Source links and full licence
    text are in packs/jsp-912/LICENSE.
change_indication: "reconstructed synthesized reference notes"
```

No `source_url` key. No URL anywhere in this file. `source_pages` and `chapters` are bare integers. Mandatory fields above `build:` stay column-0 scalars. The `notes` block is the D2 manifest. Do not keep a second list of vet facts.

- [ ] **Step 4: Write `packs/jsp-912/LICENSE`**

Model the file on `packs/jsp-936/LICENSE`. Copy the full OGL v3.0 text from that file (the block that starts `Open Government Licence v3.0 (full text, copied from the National Archives on 2026-09-25)` through the last line). Do not shorten the deed. Do not re-fetch the deed unless the copied text is missing a section that `jsp-936/LICENSE` has.

Section order above the deed:

1. Heading `JSP 912 pack: content licence`.
2. Attribution statement: `Contains public sector information licensed under the Open Government Licence v3.0.`
3. Source identification: JSP 912 Human Factors Integration in Defence Systems, Part 1 Directive and Part 2 Guidance, Version 3.0, March 2024, Ministry of Defence, Crown copyright. State the pin was verified on `VET_DATE` against the publication page and both PDFs (byte sizes, page counts, running footers `JSP 912 Pt 1 (V3.0 Mar 24)` and `JSP 912 Pt 2 (V3.0 Mar 24)`). State the exception scan found no carve-out of either PDF body from the Open Government Licence reuse grant. State both parts are in this pack.
4. Source link: `https://www.gov.uk/government/publications/human-factors-integration-in-defence-systems-jsp-912`
5. Licence deed link: `https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/`
6. Nature: reconstructed reference notes, not a reproduction, not official MOD guidance. Passages paraphrased except short defined terms.
7. Non-endorsement: the Ministry of Defence does not endorse this pack.
8. Excluded material, named and not quoted: JSP 375, JSP 536, JSP 815, JSP 822, other JSPs the two PDFs cite, DEF-STANs, and third-party standards. No clause text. No PDF figures. No HuFIMS URL.
9. Scope: this licence governs the content pack (`SKILL.md`, `chapters/`, `glossary.md`, `cheatsheet.md`). The repository's MIT licence covers tooling and scaffolding only.

URLs appear in this file only. They do not appear in PACK.yaml, SKILL.md, chapters, glossary, or cheatsheet.

- [ ] **Step 5: Verify the skeleton**

```bash
python -c "
import pathlib
p = pathlib.Path('packs/jsp-912/PACK.yaml').read_text(encoding='utf-8')
assert 'source_url' not in p
assert 'http://' not in p and 'https://' not in p
assert 'license: \"Open Government Licence v3.0\"' in p
assert 'JSP 912 Human Factors Integration in Defence Systems, Part 1 Directive and Part 2 Guidance, V3.0 (March 2024)' in p
assert 'slug: jsp-912' in p
assert 'Ministry of Defence' in p
assert 'license_tier: 2' in p
assert 'commercial_use: true' in p
assert 'share_alike: false' in p
assert 'attribution_required: true' in p
assert 'change_indication: \"reconstructed synthesized reference notes\"' in p
assert 'Oct 2021' in p
assert 'not the pin' in p
lic = pathlib.Path('packs/jsp-912/LICENSE').read_text(encoding='utf-8')
assert 'Open Government Licence v3.0' in lic
assert 'does not endorse' in lic
assert 'https://www.gov.uk/government/publications/human-factors-integration-in-defence-systems-jsp-912' in lic
assert 'https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/' in lic
assert 'JSP 375' in lic and 'JSP 536' in lic
print('skeleton ok')
"
git check-ignore -v sources/jsp-912/part1.pdf
git ls-files sources/
```

Expected: `skeleton ok`, the ignore rule matches the PDF, and `git ls-files sources/` is empty.

---

### Task 2: Write chapters, glossary, cheatsheet, and SKILL.md

**Gate:** gate-enforced (validate_pack, check_pack_quality, URL scan).

**Files:**
- Create: `packs/jsp-912/chapters/chNN-<slug>.md` (frozen list from Task 1)
- Create: `packs/jsp-912/glossary.md`
- Create: `packs/jsp-912/cheatsheet.md`
- Create: `packs/jsp-912/SKILL.md`
- Read: `sources/jsp-912/part1.txt` and `sources/jsp-912/part2.txt` (do not commit)
- Read: `packs/jsp-936/chapters/ch01-introduction.md` (section order only; do not edit)

**Interfaces:**
- Consumes: frozen basenames, dominance tags, page ranges, `CHAPTER_COUNT`, and `VET_DATE` from Task 1.
- Produces: chapter files whose basenames later tasks copy into classification rows, including the `.md` suffix. SKILL.md Topic Index `chNN` tokens must match those basenames. `check_pack_quality.py` requires each chapter body to be at least 30 lines.

**Model:** standard

Per-task brief: `.superpowers/sdd/uk-defence-jsp-912-pack/task-2-brief.md`

- [ ] **Step 1: Write each frozen chapter from its page range**

For each frozen row, write `packs/jsp-912/chapters/<basename>`. Each file is at least 30 lines of prose.

Rules:

- Synthesized reference notes. Short defined terms may be kept verbatim. No long verbatim passages. No shall-lists copied as clauses.
- Name JSP 375, JSP 536, JSP 815, JSP 822, DEF-STANs, and third-party standards when the page range names them. Do not quote them. Do not embed page images. Do not write a HuFIMS URL.
- Ground every claim in the page range for that chapter. Do not borrow another chapter's range to fill length.
- First line of each chapter names the source part and the printed page range, in the `jsp-936` shape: `Sources: JSP 912 Part 1 V3.0, printed body pp. N-M` or both parts when the chapter draws from both.
- Chapter section shape, in order, when the source supports the heading: `Core Idea`, `Frameworks Introduced`, `Key Concepts`, `Mental Models`, `Anti-patterns` (only if the source states a refusal), `Key Takeaways`, `Connects To`. Skip a heading the page range does not support. Do not invent a framework neither PDF contains.
- Stay inside D5. Do not write a Defence SMS chapter. Do not write an acquisition-safety policy chapter. Do not write dependable-AI direction. Point at `jsp-815` and `jsp-376` when the source names those JSPs, and state they are not reproduced.
- Roles chapter: the six named roles from Part 1 section 3 (Project Team Leader, HFI Focus, Requirements Manager, Capability Sponsor, Capability Integration Working Group, HFI Support Function). Do not invent a seventh. Confirm the six names against the extract. If the extract uses a different official name, use the extract's name and say so in the chapter.
- No `http://` or `https://` in any chapter.

If a frozen row's page range has no usable prose, stop and report. Do not write a stub under 30 lines.

- [ ] **Step 2: Write `glossary.md` and `cheatsheet.md`**

`glossary.md`: terms either PDF defines, alphabetical. Each entry names the `chNN` that uses it. Fold acronyms and the Part 2 glossary here. No URLs. No assignment row is created for this file.

`cheatsheet.md`: the six HFI stage gates (HFI-1.0 through HFI-6.0) and the six roles, described in prose, not copied as page images. No URLs. No assignment row is created for this file.

- [ ] **Step 3: Write `packs/jsp-912/SKILL.md`**

Frontmatter:

```yaml
---
name: jsp-912
description: "Knowledge pack synthesized from JSP 912 Human Factors Integration in Defence Systems, Part 1 Directive and Part 2 Guidance, V3.0 (March 2024, Ministry of Defence, Open Government Licence v3.0): Human Factors Integration in Defence acquisition. SCOPE LIMITS: both parts, one pack; MOD policy, not statute; not Defence SMS (use jsp-815) and not acquisition-safety policy (use jsp-376); not dependable-AI direction (use jsp-936); JSP 375, JSP 536, JSP 815, JSP 822, and DEF-STANs named, not quoted; reconstructed reference notes, not MOD guidance, and no official status."
---
```

Body order, matching PACK-SPEC and `packs/jsp-936/SKILL.md`:

1. Heading: `# JSP 912: Human Factors Integration in Defence Systems (Parts 1 and 2)`
2. `## When to use`, then a `**Prerequisites:**` line (`none required; plain Markdown`). State the skill answers questions about Human Factors Integration in UK Defence acquisition: what HFI is, how it sits in systems engineering, the six stage gates, and the six roles. It does not cover Defence SMS, acquisition-safety policy, or dependable AI.
3. A `**Source:**` line naming the OGL attribution statement, both parts, V3.0 (March 2024), Ministry of Defence, Crown copyright, the reconstructed-notes statement, and a relative link `[LICENSE](LICENSE)`. No absolute URL in this file. The licence file holds the URLs.
4. `## How to use this skill`: four bullets. With no arguments, read Core Frameworks. With a topic, use the Topic Index. With a role or stage-gate question, use the Chapter Index. For a term, use `glossary.md`. For a stage gate or a role, use `cheatsheet.md`.
5. `## Core Frameworks & Mental Models`: two to four subsections drawn only from the two PDFs (what HFI is, the six stage gates, how tailoring works, the six roles). Do not invent a framework neither PDF contains. Say which part each claim comes from.
6. `## Chapter Index`: one line per frozen chapter, linking `chapters/<basename>`. Part-1-dominant chapters before Part-2-dominant chapters, matching the frozen map. A both-drawing line names both parts.
7. `## Topic Index`: keyword lines whose `chNN` tokens match the frozen basenames. Cover HFI, human component of capability, HFI domains, systems engineering, stage gates HFI-1.0 through HFI-6.0, roles, competencies, and tailoring.
8. `## Supporting Files`: `glossary.md` and `cheatsheet.md`, one line each.
9. `## Scope & Limits`: source version and `VET_DATE`; HFI in Defence acquisition only; not Defence SMS (`jsp-815`); not acquisition-safety policy (`jsp-376`); not dependable-AI direction (`jsp-936`); other JSPs and third-party standards named, not quoted; not official MOD guidance.

No `http://` or `https://` in this file.

- [ ] **Step 4: Run the pack gates**

```bash
python tooling/validate_pack.py packs/jsp-912
python tooling/check_pack_quality.py packs/jsp-912
python -c "
import pathlib
root = pathlib.Path('packs/jsp-912')
bad = []
for p in root.rglob('*'):
    if p.is_file() and p.name != 'LICENSE':
        text = p.read_text(encoding='utf-8')
        if 'https://' in text or 'http://' in text:
            bad.append(str(p))
assert not bad, bad
print('no urls outside LICENSE')
"
```

Expected: `validate_pack.py` exits 0, `check_pack_quality.py` prints a pass for `jsp-912` and exits 0, and the URL scan prints `no urls outside LICENSE`.

If a chapter is under 30 lines, extend it from its own page range. Do not borrow another chapter's range.

---

### Task 3: Catalogue, watchlist, indexes, routing, and count sentences

**Gate:** gate-enforced (catalog live set, source-watch coverage, routing-map Topics coverage, routing-map Licences row, SKILLS.md row, cursor manifest).

**Files:**
- Modify: `catalog.json`
- Modify: `docs/source-watchlist.json`
- Modify: `SKILLS.md`
- Modify: `packs/se/SKILL.md`
- Modify: `.claude-plugin/plugin.json`
- Modify: `.cursor-plugin/plugin.json`
- Modify: `NOTICE`
- Modify: `README.md`
- Modify: `docs/index.html`
- Modify: `docs/assets/still-catalogue.svg`
- Modify: `docs/products/website/01-jgs-se-knowledge-packs.yaml`
- Modify: `docs/candidate-packs.md`
- Modify: `docs/superpowers/backlog.md`
- Modify: `CHANGELOG.md`

**Interfaces:**
- Consumes: `CHAPTER_COUNT` and `VET_DATE` from Task 1, and the pin string `JSP 912 Human Factors Integration in Defence Systems, Part 1 Directive and Part 2 Guidance, V3.0 (March 2024)`.
- Produces: a live catalog row and a watchlist row that Task 4's generator and Task 5's release gate both require. Cursor path is `./packs/jsp-912/SKILL.md`. Claude path is `./packs/jsp-912`.

**Model:** standard

Per-task brief: `.superpowers/sdd/uk-defence-jsp-912-pack/task-3-brief.md`

- [ ] **Step 1: Add the catalog row**

Insert one object in `catalog.json` `packs`, after the `jsp-936` object and before the `fhwa-its-se` object. Do not change `"updated"` (`2026-10-14`). Do not add `source_url`. Keys in this order, matching `jsp-936`:

```json
{
  "slug": "jsp-912",
  "title": "JSP 912: Human Factors Integration in Defence Systems (Parts 1 and 2)",
  "publisher": "Ministry of Defence",
  "source_version": "JSP 912 Human Factors Integration in Defence Systems, Part 1 Directive and Part 2 Guidance, V3.0 (March 2024)",
  "license": "Open Government Licence v3.0",
  "license_tier": 2,
  "commercial_use": true,
  "chapters": CHAPTER_COUNT,
  "status": "live"
}
```

`CHAPTER_COUNT` is the integer from Task 1, not the token. Keep JSON valid. Live pack count becomes 74.

- [ ] **Step 2: Add the watchlist row, then record**

The record command refuses a slug that is not already in the file, and also refuses when the watchlist and the live catalog disagree. The catalog row from Step 1 must exist first. Insert one object in `docs/source-watchlist.json` `sources`, after the `jsp-936` source and before the `fhwa-its-se` source. Keys in this order:

```json
{
  "slug": "jsp-912",
  "publisher": "Ministry of Defence",
  "document": "JSP 912 Human Factors Integration in Defence Systems, Part 1 Directive and Part 2 Guidance, V3.0 (March 2024)",
  "version": "JSP 912 Human Factors Integration in Defence Systems, Part 1 Directive and Part 2 Guidance, V3.0 (March 2024)",
  "last_checked": "VET_DATE",
  "hint": ""
}
```

`document` and `version` are byte-equal to PACK.yaml `source_version` and to the catalog `source_version`. No URL in any value. `hint` stays an empty string.

```bash
python tooling/check_source_watch.py --record jsp-912 "JSP 912 Human Factors Integration in Defence Systems, Part 1 Directive and Part 2 Guidance, V3.0 (March 2024)" VET_DATE
python tooling/check_source_watch.py
```

Expected: both exit 0. If the record command returns 1, the slug was missing or the catalog row disagrees. Fix the row. Do not add a URL.

- [ ] **Step 3: SKILLS.md, NOTICE, README, plugins, CHANGELOG**

`SKILLS.md` line 9: change `73 packs (+8 signposts, +1 orchestrator)` to `74 packs (+8 signposts, +1 orchestrator)`. After the `jsp-936` table row (line 80) and before the `fhwa-its-se` row, insert:

```markdown
| [`jsp-912`](packs/jsp-912/SKILL.md) | Open Government Licence v3.0 | Synthesized reference notes from JSP 912 Human Factors Integration in Defence Systems, Part 1 Directive and Part 2 Guidance, V3.0 (March 2024); Human Factors Integration in Defence acquisition; JSP 375, JSP 536, and DEF-STANs named, not quoted. |
```

`NOTICE`: after the `[pack: jsp-936]` block and before `[pack: fhwa-its-se]`, insert one block in the `jsp-936` shape.

```text
[pack: jsp-912]

Source : JSP 912 Human Factors Integration in Defence Systems, Part 1
         Directive and Part 2 Guidance, V3.0 (March 2024). Ministry of
         Defence, Crown copyright.
Author : Ministry of Defence
Licence: Open Government Licence v3.0
Changes: reconstructed synthesized reference notes (not a reproduction)
Terms  : attribution required. Contains public sector information licensed
         under the Open Government Licence v3.0. The Ministry of Defence does
         not endorse this pack. Other JSPs and third-party standards the
         two parts cite are named and not reproduced. Both parts are in
         this pack. See packs/jsp-912/LICENSE.
```

`.claude-plugin/plugin.json`: insert `"./packs/jsp-912"` in the `skills` array, beside the existing `./packs/jsp-936` entry. Do not change `version` (stays `1.23.0`). Keep JSON valid.

`.cursor-plugin/plugin.json`: insert `"./packs/jsp-912/SKILL.md"` in the `skills` array, beside the existing `./packs/jsp-936/SKILL.md` entry. Do not change `version` (stays `1.22.0`). Keep JSON valid. Cursor skill count becomes 80. That is expected. The three `commercial_use: false` packs stay absent. Do not add them.

`README.md`: change `packs-73` to `packs-74` in the shields.io URL and the alt text (`https://img.shields.io/badge/packs-74-blueviolet`, alt `74 packs`). After the `jsp-936` catalogue row and before the `fhwa-its-se` row, insert a row in the same cell shape as `jsp-936`:

```markdown
| `jsp-912` | JSP 912 Human Factors Integration in Defence Systems, Parts 1 and 2, V3.0 (March 2024) | OGL v3.0 (UK MoD) | 🟡 2 | ✅ live (CHAPTER_COUNT chapters) |
```

`CHAPTER_COUNT` is the integer from Task 1. If a README catalogue-count sentence states 73 or 82, move it to 74 or 83. Do not invent a sentence that is not there. The badge line is the count the release gate parses.

`CHANGELOG.md`: under `## [Unreleased]`, add a `### Added` heading if that heading is absent, then one bullet. Do not add a version heading. Do not edit `## [1.23.0]`. Do not edit the Changed bullet that says the plugin declares 82 skill paths. That sentence is a historical release note, not a count the release gate parses.

```markdown
- `jsp-912` content pack from JSP 912 Parts 1 and 2, V3.0 (March 2024), reconstructed notes, registered on the catalogue surfaces.
```

- [ ] **Step 4: Routing map**

In `packs/se/SKILL.md`, inside `ROUTING-MAP:BEGIN` / `ROUTING-MAP:END`:

Edit the Defence safety management row (line 118). Add keywords `human factors`, `HFI`, `human component`. Do not remove existing safety keywords. Add `jsp-912` to the pack cell. Do not create a second Defence row. Four packs, inside the six-pack cap.

Current row:

```markdown
| Defence safety management | JSP 815, JSP 376, acquisition safety, defence safety, SMS, safety case, assurance, dependable AI, AI assurance | `jsp-815`, `jsp-376`, `jsp-936` |
```

Replacement:

```markdown
| Defence safety management | JSP 815, JSP 376, JSP 912, acquisition safety, defence safety, SMS, safety case, assurance, dependable AI, AI assurance, human factors, HFI, human component | `jsp-815`, `jsp-376`, `jsp-936`, `jsp-912` |
```

Do not add `jsp-912` to the AI and cyber-physical row (line 107). That row stays on `jsp-936`.

Add a Licences row after the `jsp-936` row (line 161) and before the `easa-rules` row. OGL packs are required. The routing-map check errors if this row is missing.

```markdown
| `jsp-912` | Open Government Licence v3.0 |
```

- [ ] **Step 5: Count loci the release gate parses**

These claims must move together. Signpost count stays 8. Orchestrator stays 1. Do not renumber NASA, DoD, NIST, FAA, or any other family chip.

`docs/index.html` section 06 h2 (line 189): `73 packs` becomes `74 packs`. The skills sentence (line 209) `82 skills in all` becomes `83 skills in all`, and `73 knowledge packs` becomes `74 knowledge packs`.

UK chip (line 202): `UK · 3` becomes `UK · 4`. Add JSP 912 to the span. Keep the MHRA parenthetical. Do not move MHRA into the UK count. The EU / academic / JGS chip stays 5.

Current:

```html
<div class="pk"><b>UK &middot; 3</b><span>JSP 815 Defence Safety Management System; JSP 376 Defence Acquisition Safety Policy; JSP 936 Dependable Artificial Intelligence (AI) in Defence, Part 1: Directive; MHRA device software guidance (counted under EU / academic / JGS)</span></div>
```

Replacement:

```html
<div class="pk"><b>UK &middot; 4</b><span>JSP 815 Defence Safety Management System; JSP 376 Defence Acquisition Safety Policy; JSP 936 Dependable Artificial Intelligence (AI) in Defence, Part 1: Directive; JSP 912 Human Factors Integration in Defence Systems, Parts 1 and 2; MHRA device software guidance (counted under EU / academic / JGS)</span></div>
```

Chip COUNT sum must equal 74. Signposts chip stays 8. Orchestrator chip stays 1 and is exempt from the content sum.

`docs/assets/still-catalogue.svg`: subtitle `73 packs` becomes `74 packs` (line 12). Footer `73 PACKS` becomes `74 PACKS` (line 24). Leave the signpost strings alone.

`docs/products/website/01-jgs-se-knowledge-packs.yaml` line 47: `73 packs across the SE catalogue` becomes `74 packs across the SE catalogue`. Line 70: `UK MOD (3)` becomes `UK MOD (4)`, and the sentence names JSP 912 after JSP 936. Do not change the YAML `version:` field. Do not renumber NASA, DoD, NIST, FAA, or other family counts.

Current line 70:

```yaml
UK MOD (3): JSP 815 Defence Safety Management System; JSP 376 Defence Acquisition Safety Policy; JSP 936 Dependable Artificial Intelligence (AI) in Defence, Part 1: Directive.
```

Replacement:

```yaml
UK MOD (4): JSP 815 Defence Safety Management System; JSP 376 Defence Acquisition Safety Policy; JSP 936 Dependable Artificial Intelligence (AI) in Defence, Part 1: Directive; JSP 912 Human Factors Integration in Defence Systems, Parts 1 and 2.
```

- [ ] **Step 6: Candidate packs and b-41 (D7, D8)**

`docs/candidate-packs.md` changes only these four strings. Do not edit any other row.

Row 4 (line 19). Current status cell starts `partially built 2026-10-27 (jsp-815, jsp-376, and jsp-936 done, other JSPs and DEF-STANs pending)`. Replace that status cell with:

```markdown
partially built VET_DATE (jsp-815, jsp-376, jsp-936, and jsp-912 done, other JSPs and DEF-STANs pending). OGL-licensed, no open competitor, and UK sourcing matches the consultancy's identity
```

`VET_DATE` is the date from Task 1, not the token. Keep the row number `4` and the family name `` `uk-defence` family (JSP series first) ``.

Unranked-remainder sentence (line 26). The live line reads `the unranked remainder of the uk-defence family (JSP 912, JSP 940, DEF-STANs) and telecom-3gpp need a new ranking pass.` (note: no "and the" before DEF-STANs; re-grep at execution). Anchor by substring `unranked remainder of the uk-defence family (JSP 912, JSP 940, DEF-STANs)` and replace with `unranked remainder of the uk-defence family (JSP 940, DEF-STANs)` — delete `JSP 912, ` only. Keep JSP 940 and the DEF-STANs. Do not mark JSP 940 built.

Catalogue-count sentence (line 30). Current: `The catalogue holds 82 packs: 73 full reconstructed content packs`. Replacement: `The catalogue holds 83 packs: 74 full reconstructed content packs`. Leave the eight signpost names and the `/se` orchestrator clause as they are.

`uk-defence-*` proposed-pack bullet (line 70). Current: `Built 2026-10-27 (jsp-815, jsp-376, and jsp-936).` Replacement: `Built VET_DATE (jsp-815, jsp-376, jsp-936, and jsp-912).` Do not edit any other proposed-pack bullet.

`docs/superpowers/backlog.md` b-41 (line 141): leave the status cell as `promoted`. Do not write `done`. Do not delete the row. Append to the evidence cell, after the existing P57 sentence: `Execution VET_DATE: jsp-912 shipped. JSP 940, JSP 945, JSP 816, JSP 375, and JSP 520 remain needs-info and are not built.` The packages doc marks P57 done after this plan is EXECUTED. That is not this file's job.

- [ ] **Step 7: Verify the registration text**

```bash
python -c "
import json, pathlib
cat = json.loads(pathlib.Path('catalog.json').read_text(encoding='utf-8'))
assert cat['updated'] == '2026-10-14'
row = next(p for p in cat['packs'] if p['slug'] == 'jsp-912')
assert list(row.keys()) == ['slug', 'title', 'publisher', 'source_version', 'license', 'license_tier', 'commercial_use', 'chapters', 'status']
assert row['license'] == 'Open Government Licence v3.0'
assert row['source_version'] == 'JSP 912 Human Factors Integration in Defence Systems, Part 1 Directive and Part 2 Guidance, V3.0 (March 2024)'
assert row['license_tier'] == 2
assert row['commercial_use'] is True
assert row['status'] == 'live'
assert 'source_url' not in row
assert len(cat['packs']) == 74
watch = json.loads(pathlib.Path('docs/source-watchlist.json').read_text(encoding='utf-8'))
w = next(s for s in watch['sources'] if s['slug'] == 'jsp-912')
assert list(w.keys()) == ['slug', 'publisher', 'document', 'version', 'last_checked', 'hint']
assert w['document'] == row['source_version']
assert w['version'] == row['source_version']
assert w['hint'] == ''
assert 'http' not in json.dumps(w)
claude = json.loads(pathlib.Path('.claude-plugin/plugin.json').read_text(encoding='utf-8'))
assert claude['version'] == '1.23.0'
assert './packs/jsp-912' in claude['skills']
cursor = json.loads(pathlib.Path('.cursor-plugin/plugin.json').read_text(encoding='utf-8'))
assert cursor['version'] == '1.22.0'
assert './packs/jsp-912/SKILL.md' in cursor['skills']
se = pathlib.Path('packs/se/SKILL.md').read_text(encoding='utf-8')
assert '\`jsp-912\`' in se
lic = se.split('### Licences')[1].split('ROUTING-MAP:END')[0]
assert '\`jsp-912\`' in lic
ai = [ln for ln in se.splitlines() if ln.startswith('| AI & cyber-physical')][0]
assert 'jsp-912' not in ai
backlog = pathlib.Path('docs/superpowers/backlog.md').read_text(encoding='utf-8')
b41 = [ln for ln in backlog.splitlines() if ln.startswith('| b-41 |')][0]
assert '| promoted |' in b41
assert 'done' not in b41.split('|')[4]
print('registration ok')
"
python tooling/check_source_watch.py
```

Expected: `registration ok`, and `check_source_watch.py` exits 0.

---

### Task 4: Classification rows, generator literals, regenerate map and pages

**Gate:** gate-enforced (classification-rules, capability-map, generated HTML).

**Files:**
- Modify: `docs/classification-rules.json`
- Modify: `docs/capability-pack-map-note-overrides.json`
- Modify: `tooling/generate_capability_map.py` (four literals only)
- Generate: `docs/capability-pack-map.json`
- Generate: `docs/capability-pack-map.md`
- Generate: `docs/packs/jsp-912/index.html`
- Generate: `docs/sitemap.xml`
- Generate: `docs/packs.html`

**Interfaces:**
- Consumes: frozen chapter basenames from Task 2, including the `.md` suffix, plus `VET_DATE` and `CHAPTER_COUNT` from Task 1. Consumes the live `cluster_names` list. `Human Systems Integration / Human Factors` is in that list. The spec's shorter name is not.
- Produces: N assignment rows and N note rows, with N equal to `CHAPTER_COUNT`. Four generator literals become the plain integer `735 + N`. The generator then writes the map. Later tasks do not hand-edit generated JSON, Markdown, or HTML.

**Model:** standard

Per-task brief: `.superpowers/sdd/uk-defence-jsp-912-pack/task-4-brief.md`

- [ ] **Step 1: Hand-add N assignments and N notes**

N is `CHAPTER_COUNT` from Task 1. For each frozen chapter file, append one object to `docs/classification-rules.json` `assignments` and one object to `docs/capability-pack-map-note-overrides.json` `notes`. Same `pack` and `chapter` in both files. `chapter` is the basename including `.md`, matching Task 2.

Assignment object:

```json
{"pack": "jsp-912", "chapter": "chNN-slug.md", "cluster": "CLUSTER", "is_support": false}
```

`cluster` must be a name already in `cluster_names`. Pick from the vocabulary the chapter actually supports. Likely fits, and only if the chapter supports the name:

- `Human Systems Integration / Human Factors` (the live name; do not write the shorter spec form)
- `Requirements Engineering`
- `Supplier, Procurement & Acquisition`
- `Verification`
- `Validation`
- `Governance, Reviews, Gates & Control Points`
- `Standards, Tailoring & Process Models`

Do not invent a cluster. Do not add glossary or cheatsheet rows. `is_support` stays false. This pack has no pointer-only chapter.

Note object:

```json
{"pack": "jsp-912", "chapter": "chNN-slug.md", "note": "One sentence on what the chapter covers, from JSP 912 V3.0 March 2024."}
```

Note rules: one sentence, no em dash, no spaced double hyphen used as a dash, and the sentence says the note is from JSP 912 V3.0 March 2024. No URL.

Set `generated_on` on both files to `VET_DATE` before the generator run. Do not change any other envelope field by hand.

- [ ] **Step 2: Replace the four 735 literals**

In `tooling/generate_capability_map.py`, replace `735` on lines 9, 195, 203, and 204 with the plain integer `735 + N` (735 plus Task 1's chapter count). If N is 8, the integer is `743`. Write the integer, not the expression `735 + N`. Do not change any other number in the file.

The four sites, current text:

- Line 9: `the mandatory 735-row overrides file (H-01).`
- Line 195: `if only_a or only_n or len(notes) != 735:`
- Line 203: `if len(notes) != 735:`
- Line 204: `parts.append(f"notes length must be 735, got {len(notes)}")`

```bash
python -c "
import pathlib
text = pathlib.Path('tooling/generate_capability_map.py').read_text(encoding='utf-8')
print('735 count', text.count('735'))
"
```

Expected: `735 count 0`. If `735` remains, the generator will reject the new note file. Do not edit the generator beyond those four literals.

- [ ] **Step 3: Regenerate the map and check it**

```bash
python tooling/generate_capability_map.py --generated-on VET_DATE --sync-md
python tooling/check_capability_map.py
python tooling/check_classification_rules.py
```

Expected: all three exit 0. Map total is `735 + N`. If the generator reports `notes length must be 735`, Step 2 missed a literal. If a check reports an assignment missing a note, the paired rows disagree. Fix the rows. Do not edit the generator beyond the four literals. Do not hand-edit `docs/capability-pack-map.json` or `docs/capability-pack-map.md`.

- [ ] **Step 4: Generate pack pages**

`gen_pack_pages.py` with the only-slug flag reads the live catalog. The catalog row from Task 3 must exist, or the command exits 1 with `unknown pack slugs`.

```bash
python tooling/gen_pack_pages.py --only jsp-912
python tooling/gen_packs_page.py
```

The only-slug flag is an execution command. Do not write that flag into a committed comment as the generator's default. A later full regen is `python tooling/gen_pack_pages.py` with no flag. This task uses the flag because the spec names it, and a full regen rewrites every pack page.

Expected: both exit 0. `docs/packs/jsp-912/index.html` exists. `docs/sitemap.xml` contains a jsp-912 URL. `docs/packs.html` names jsp-912 because the generator wrote it. Do not hand-edit those three files.

```bash
python -c "
import pathlib
assert pathlib.Path('docs/packs/jsp-912/index.html').is_file()
site = pathlib.Path('docs/sitemap.xml').read_text(encoding='utf-8')
assert 'jsp-912' in site
page = pathlib.Path('docs/packs.html').read_text(encoding='utf-8')
assert 'jsp-912' in page
print('pages ok')
"
```

Expected: `pages ok`.

---

### Task 5: Sweep

**Gate:** gate-enforced (surface scan, prose check, release gate, catalog tests).

**Files:**
- Read only. Fix only findings this pack introduced. Do not open a new surface.

**Interfaces:**
- Consumes: every file Tasks 1, 2, 3, and 4 wrote or generated.
- Produces: a passing `python tooling/check_release.py` transcript. No commit.

**Model:** flash

Per-task brief: `.superpowers/sdd/uk-defence-jsp-912-pack/task-5-brief.md`

- [ ] **Step 1: D7 surfaces and the URL rule**

```bash
python -c "
import pathlib
surfaces = [
    'catalog.json',
    'docs/source-watchlist.json',
    'SKILLS.md',
    'packs/se/SKILL.md',
    'NOTICE',
    '.claude-plugin/plugin.json',
    '.cursor-plugin/plugin.json',
    'docs/classification-rules.json',
    'docs/capability-pack-map-note-overrides.json',
    'docs/capability-pack-map.json',
    'docs/packs.html',
    'docs/packs/jsp-912/index.html',
    'docs/sitemap.xml',
    'docs/candidate-packs.md',
    'docs/superpowers/backlog.md',
    'README.md',
    'CHANGELOG.md',
]
# jsp-936 precedent: docs/index.html, docs/assets/still-catalogue.svg, and
# docs/products/website/01-jgs-se-knowledge-packs.yaml carry human-form text
# ("JSP 912 Human Factors Integration in Defence Systems, Parts 1 and 2"),
# not the slug. Their 74/8 counts are asserted by check_release's own
# catalogue-count gate; exclude them from the slug-assert loop.
count_surfaces = [
    'docs/index.html',
    'docs/assets/still-catalogue.svg',
    'docs/products/website/01-jgs-se-knowledge-packs.yaml',
]
for s in count_surfaces:
    text = pathlib.Path(s).read_text(encoding='utf-8')
    assert '74' in text, s
for s in surfaces:
    text = pathlib.Path(s).read_text(encoding='utf-8')
    assert 'jsp-912' in text, s
print('surfaces name jsp-912')
root = pathlib.Path('packs/jsp-912')
for p in root.rglob('*'):
    if p.is_file() and p.name != 'LICENSE':
        text = p.read_text(encoding='utf-8')
        assert 'https://' not in text and 'http://' not in text, p
print('pack has no urls outside LICENSE')
"
```

Expected: both prints, exit 0.

- [ ] **Step 2: Prose check on the new pack**

```bash
python ~/.zcode/scripts/prose_check.py packs/jsp-912/SKILL.md packs/jsp-912/glossary.md packs/jsp-912/cheatsheet.md packs/jsp-912/LICENSE packs/jsp-912/chapters
```

Expected: exit 0. Zero em dashes in headings and body prose. If a finding is inside a fenced code block, the script already skips those. Fix body prose. Do not edit `packs/jsp-936` to make this pass.

- [ ] **Step 3: Release gate and the catalog tests**

```bash
python tooling/check_release.py
python tooling/test_catalog_live_set.py
python tooling/test_catalogue_count.py
python tooling/test_ci_gate.py
git ls-files sources/
```

Expected: `RELEASE CHECK: PASS` from `check_release.py`. The three tests exit 0. `git ls-files sources/` is empty.

`test_catalog_live_set.py` locks `catalog.json` `"updated"` at `2026-10-14`. Do not change that field to make a test pass.

Fix only findings this pack introduced. Common misses and the fix:

- `[catalogue-count]` or `[pack-count]`: a `73` left in `docs/index.html` section 06, a chip COUNT, `still-catalogue.svg`, or the YAML pack-count line. Do not change signpost counts. Chip COUNT sum must equal 74. UK chip must be 4. EU / academic / JGS chip stays 5.
- `[index] SKILLS.md lists`: line 9 still says 73, or the new table row is missing.
- `[cursor]`: `.cursor-plugin/plugin.json` lacks `./packs/jsp-912/SKILL.md`, or `version` is no longer `1.22.0`.
- `[routing-map]`: Topics Packs column lacks `jsp-912`, or the Licences row is missing. Add the Licences row. Do not add `jsp-912` to the AI row. Four packs on the Defence row is inside the six-pack cap.
- `[classification-rules]` or `[map-replay]`: assignment count, note count, and the four generator literals disagree, or `generated_on` differs across the rules file and the live map. Re-run Task 4 Step 3.
- `[source-watch]`: watchlist row missing, a URL in a value, or `last_checked` is not `YYYY-MM-DD`.
- `[sitemap]` or `[pack-rev]`: re-run Task 4 Step 4 (pack pages, then the packs index).

Do not bump `RELEASE-INFO.txt`. Do not bump either plugin `version`. Do not change `catalog.json` `updated`. Do not commit unless the parent execution mode says commit. Do not push. Do not open a PR.

CONTRIBUTING pre-tag checks are not required. This cut is not a release. The next release catches them.

---

## Testing

All must pass before the cut is done. Commands are gates, not suggestions.

1. `python tooling/validate_pack.py packs/jsp-912` exits 0.
2. `python tooling/check_pack_quality.py packs/jsp-912` exits 0. The script accepts a pack path. Floor is 30 lines per chapter. Topic Index `chNN` tokens resolve.
3. Record, then coverage. Record only after the catalog live row and the hand-added watchlist row exist. Both exit 0.

   ```bash
   python tooling/check_source_watch.py --record jsp-912 "JSP 912 Human Factors Integration in Defence Systems, Part 1 Directive and Part 2 Guidance, V3.0 (March 2024)" <YYYY-MM-DD vet>
   python tooling/check_source_watch.py
   ```

4. Regenerate the map, then both checkers. Override row count must match rules row count. Map total is `735 + N`. The four `735` literals in `tooling/generate_capability_map.py` must already be the plain integer `735 + N`. All three exit 0.

   ```bash
   python tooling/generate_capability_map.py --generated-on <YYYY-MM-DD> --sync-md
   python tooling/check_capability_map.py
   python tooling/check_classification_rules.py
   ```

5. Pack pages, then the packs index. Both exit 0. `docs/packs/jsp-912/index.html` exists. `docs/sitemap.xml` contains a jsp-912 URL. Do not hand-edit generated HTML.

   ```bash
   python tooling/gen_pack_pages.py --only jsp-912
   python tooling/gen_packs_page.py
   ```
6. A scan of registration surfaces finds `jsp-912`, and a scan of `packs/jsp-912` finds no URL except in `LICENSE`.
7. `python tooling/check_release.py` exits 0. `[routing-map]` must see `jsp-912` on the Defence row and on the Licences table. `[catalogue-count]` must see 74, and the chip sum must equal 74. Fix only findings this pack introduced.
8. `python tooling/test_catalog_live_set.py`, `python tooling/test_catalogue_count.py`, and `python tooling/test_ci_gate.py` exit 0. `test_catalog_live_set.py` locks `"updated"` at `2026-10-14`.
9. `python ~/.zcode/scripts/prose_check.py` on the new pack's prose files. Zero em dashes in headings and body prose.
10. `git ls-files sources/` is empty.

Count formulas, not a hardcoded chapter total: content packs 74, skills 83 (74 content + 8 signposts + 1 orchestrator), map assignments `735 + N` where N is the Task 1 chapter count (6, 7, 8, 9, or 10).

CONTRIBUTING pre-tag checks are not required. No release in this cut. The next release catches them.

## Self-review

Spec coverage: D1 is Task 1 Step 1 (re-fetch both PDFs, Mar 2024 footer is the pin, Oct 2021 cover line is stale, Part 2 is not dropped). D2 is Task 1 Steps 1, 3, and 4 (tier-2 fields, stop conditions, notes manifest, OGL deed copied from `jsp-936`). D3 is Task 1 Step 2 and Task 2 Step 3 (one slug, dominance order, SKILL.md says which part). D4 is Task 2 Step 1 (synthesized notes, named-not-quoted, no figures, no HuFIMS URL). D5 is Task 2 Steps 1 and 3 and Task 3 Step 4 (scope limits, not on the AI row, companions named). D6 is Task 1 Step 2 (contents lists win, 6 to 10, references and acronyms are not chapters). D7 is Task 3 (every registration surface) and Task 4 (rules, overrides, generated map and HTML). D8 is Task 3 Step 6 (b-41 stays `promoted`, evidence cell names the five remaining JSPs as needs-info and not built, row not deleted). D9 is Global Constraints and Task 4 Step 2 (four `735` literals only, no version bump, `updated` stays `2026-10-14`). Testing items 1 through 9 are the Testing section and Task 5. The Do-not list is copied into Global Constraints.

Placeholder scan: no open slots, no deferred-work markers, no "similar to Task N" standing in for a step. `CHAPTER_COUNT`, `VET_DATE`, `PAGE_COUNT_P1`, `PAGE_COUNT_P2`, `BYTE_SIZE_P1`, `BYTE_SIZE_P2`, and `PAGE_SUM` are recorded in Task 1 because the PDFs are re-fetched then. They are not invented here.

Type consistency: pin string `JSP 912 Human Factors Integration in Defence Systems, Part 1 Directive and Part 2 Guidance, V3.0 (March 2024)` is the same in Tasks 1, 3, and 4. Title `JSP 912: Human Factors Integration in Defence Systems (Parts 1 and 2)` matches. Publisher `Ministry of Defence` matches. Cluster name used in Task 4 is `Human Systems Integration / Human Factors`, the live `cluster_names` entry, not the spec's shorter form. Catalog row key order matches `jsp-936`. Watchlist key order matches the live file. Cursor path is `./packs/jsp-912/SKILL.md`. Claude path is `./packs/jsp-912`. Generator literal count is four, on lines 9, 195, 203, and 204.

Deviations from the spec text, recorded so an executor does not "correct" them back:

- D8 in the spec says status becomes `done` for the 912 promotion. Parent dispatch for this plan overrides that: b-41 stays `promoted`, because 940, 945, 816, 375, and 520 remain. The packages doc marks P57 done after EXECUTED. The evidence cell still records the 912 ship date and the five remaining needs-info items. The row is not deleted.
- Spec cluster hint "Human Systems Integration" is not in `cluster_names`. The live name is `Human Systems Integration / Human Factors`. Task 4 uses the live name. The spec already says to use the nearest existing name and say so in the override note.
- Spec says insert catalog and watchlist rows the way `jsp-936` was inserted (after the previous family member). `fhwa-its-se` is now the last live row. Insertion point is after `jsp-936` and before `fhwa-its-se`, not after the last row.
- UK chip already carries an MHRA parenthetical that points at the EU / academic / JGS count. The plan keeps that parenthetical and adds JSP 912. It does not invent a chip that drops MHRA.
