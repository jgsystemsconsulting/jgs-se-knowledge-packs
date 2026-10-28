# FHWA ITS SE Pack Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship `packs/fhwa-its-se` as a live tier-1 public-domain content pack synthesized from Systems Engineering for ITS, fourth generation (December 2022), and register it on every surface `jsp-936` already uses.

**Architecture:** Re-fetch the pinned FHWA PDF before any chapter prose. Freeze 6 to 8 chapter titles from the PDF contents list, not from the spec's provisional map. Write reconstructed notes under `packs/fhwa-its-se/` using the `faa-8110-49` licence shape and the `jsp-936` chapter shape. Register the pack on every surface `tooling/check_release.py` compares, and move the hard-coded 728-row pin in the capability-map generator to 728 plus the frozen chapter count. No new tooling.

**Tech Stack:** Markdown pack files, YAML frontmatter, JSON catalogue and map files, Python 3 stdlib tooling (`tooling/validate_pack.py`, `tooling/check_pack_quality.py`, `tooling/check_source_watch.py`, `tooling/generate_capability_map.py`, `tooling/check_capability_map.py`, `tooling/check_classification_rules.py`, `tooling/gen_pack_pages.py`, `tooling/gen_packs_page.py`, `tooling/check_release.py`). PDF text via `pdftotext` if present, else an already-installed reader. No new dependencies.

**Spec:** `docs/superpowers/specs/2026-10-27-fhwa-its-se-pack.md`

Spec certificate sha256: `bb36332a6b05de5a73eda2740454371664e6a219bcb0d4f43d59a7794049b366`.

## Global Constraints

- D1: source pin is Systems Engineering for ITS, fourth generation, December 2022, FHWA Office of Operations, one PDF at `https://ops.fhwa.dot.gov/seits/files/segbv4rem.pdf`. No report number exists in the file. Do not invent one. November 2009 SEGB, FHWA-OP-02-046, device model documents, and the Caltrans website edition stay out.
- D2: licence class is tier 1 public domain. Field values, verbatim: `license: "Public Domain (US Government work, 17 U.S.C. § 105)"`, `license_tier: 1`, `commercial_use: true`, `share_alike: false`, `attribution_required: false`. Not OGL. Not tier 2. Re-fetch the PDF before chapter prose. Stop if the December 2022 fourth-generation sentence is gone, the file is no longer a US Government work, or a contractor copyright line reserves copyright.
- D3: synthesized reference notes. Short defined terms may be kept. No long verbatim passages. Name INCOSE, ISO/IEC/IEEE 15288, NTCIP, IEEE, SAE, and other third-party standards. Do not quote their clause text. Do not embed PDF figures.
- D4: scope is ITS project systems engineering for transportation agencies: V process, ConOps, requirements, design, implementation, integration, verification, validation, operations, retirement, cross-cutting processes, tailoring, and ITS procurement. Not construction specifications, not FEMA, not device model-document libraries, not a general SE textbook.
- D5: chapter count is one file per numbered top-level section in the PDF contents list, inside 6 to 8. The contents list wins over the provisional table. Expected outcome is six or seven files. Subsections stay inside the parent chapter. Do not split 3.3.1 through 3.3.13 into thirteen chapters. Basenames are `chNN-kebab-title.md`, frozen in Task 1.
- D6: full registration on every surface in Codebase context. Partial registration is the miss this package exists to avoid. `docs/candidate-packs.md` changes only the new numbered row, the `fhwa-its-se` bullet, the remaining-full-pack sentence, and the catalogue-count sentence.
- D7: b-32 resolves inside this build. Add numbered build-order row 9 for `fhwa-its-se`, status built on the execution date. Mark the proposed-pack bullet built. Set backlog b-32 status to `done`. Do not rank `telecom-3gpp` or any other candidate.
- D8: no new tooling. Do not bump `RELEASE-INFO.txt`, either plugin `version`, or `catalog.json` `updated`.
- Pin string, verbatim, in PACK.yaml `source_version`, the catalog `source_version`, and the watchlist `document` and `version` once vet confirms the December 2022 sentence: `Systems Engineering for ITS, fourth generation (December 2022)`. If the PDF date disagrees, stop. Do not rewrite the pin to match a different issue.
- Title, verbatim: `Systems Engineering for ITS`. Publisher, verbatim: `Federal Highway Administration`.
- `build.built_on` and watchlist `last_checked` are the execution date in `YYYY-MM-DD`, not a date copied from this plan's filename. `catalog.json` `"updated"` stays `2026-10-14`.
- No `source_url` in PACK.yaml or `catalog.json`. No `http://` or `https://` under `packs/fhwa-its-se/` except in `packs/fhwa-its-se/LICENSE`.
- `change_indication: "reconstructed as synthesized reference notes"`.
- `build.chapters` equals the chapter file count. `build.method` states synthesized from the pinned PDF, not adapted from a sibling prototype.
- Chapter body at least 30 lines (`tooling/check_pack_quality.py` `MIN_CHAPTER_LINES`). Topic Index `chNN` tokens in `SKILL.md` resolve to chapter files. Frontmatter `name` is `fhwa-its-se`.
- Cluster names come from `docs/classification-rules.json` `cluster_names`. Do not invent a cluster. One assignment per chapter file only. `glossary.md` and `cheatsheet.md` get no assignment or note rows. Note-override notes are one sentence, no em dash, and say the note is from Systems Engineering for ITS, December 2022.
- Count move, live inventory before this cut: 72 content packs, 8 signposts, 1 orchestrator, 81 skills, 728 classification assignments. After the cut: content packs 73, skills 82, assignments `728 + N` where N is the chapter count frozen in Task 1 (6, 7, or 8). Signposts stay 8. Orchestrator stays 1. `tooling/generate_capability_map.py` hard-codes `728` at lines 9, 195, 203, and 204, and those four literals must move, or the generator rejects the new note file. Do not hand-edit `docs/capability-pack-map.json` or `docs/capability-pack-map.md`.
- Public Domain packs are exempt from the `/se` Licences table. `tooling/check_release.py` errors on an extra Licences row. Do not add one. Do not put `fhwa-its-se` on the Defence row or the CISA / DHS row.
- Do not (spec D8 and Non-goals, verbatim):
  - Do not bump `RELEASE-INFO`.
  - Do not edit neighbor packs' chapter files.
  - Do not commit anything under `sources/`.
  - Do not bump plugin `version` or any release version file.
  - Do not change `catalog.json` `updated`. It stays `2026-10-14`.
- Also out: November 2009 SEGB, FHWA-OP-02-046, FHWA-HOP device model documents, Caltrans Local Assistance SE handbook, FEMA publications, construction specifications. Changes to `jsp-936`, `nhtsa-vehicle`, `cisa-cpg`, or any other pack's chapter prose. New validators, new page templates, new licence tiers. Quoting INCOSE, ISO, IEEE, SAE, or NTCIP clause text, or embedding PDF page images. `source_url` in `PACK.yaml` or `catalog.json`. Ranking or building `telecom-3gpp` or any other candidate. GitHub release, plugin publish, or commit. This plan does not authorize those.
- A licence failure, a missing December 2022 sentence, a contractor copyright reservation, or a contents list that will not fit 6 to 8 chapters is a stop-and-report. Do not invent content to fill the gap.
- No task pauses for human input except the D2 stop. Executors do not ask questions. Commit steps are off unless the parent execution mode says commit. Do not push. Do not open a PR.
- Per-task briefs live at `.superpowers/sdd/2026-10-27-fhwa-its-se-pack/task-N-brief.md`. The controller writes them at dispatch. This plan does not create those files.

## Codebase context

Ad-hoc context, re-checked on the tree on 2026-10-27. Precedent for licence fields is `packs/faa-8110-49/` (tier 1 public domain). Precedent for chapter, glossary, cheatsheet, and SKILL.md shape is `packs/jsp-936/` (registration file list and reconstructed-notes rule). Required content-pack layout is `docs/PACK-SPEC.md`.

- Pack contract: `packs/<slug>/{SKILL.md, PACK.yaml, LICENSE, chapters/chNN-*.md}`. Quality gate: chapter body at least 30 lines, no orphan chapter files, Topic Index `chNN` tokens resolve. `validate_pack.py` checks required files, frontmatter `name` equals folder slug, chapter links resolve, and mandatory PACK.yaml fields. The YAML parser reads only column-0 `key: value` lines and skips folded `>` blocks, so mandatory fields must be column-0 scalars.
- `packs/faa-8110-49/LICENSE` is the public-domain template. Model the new LICENSE on it: no download URL, source identified by title, publisher, and date only. Do not copy the OGL deed from `packs/jsp-936/LICENSE`.
- Watchlist `--record` rewrites an existing row. `tooling/check_source_watch.py` `record_entry` returns 1 when the slug is absent from the watchlist, and also refuses when the watchlist and the live catalog disagree. Hand-insert the watchlist row and the catalog live row before `--record`. Coverage checks the live catalog against the watchlist in both directions. The planned catalog entry must not carry a URL.
- Routing map (`packs/se/SKILL.md`, markers `ROUTING-MAP:BEGIN` / `ROUTING-MAP:END`): Topics Packs column must list every content slug. Non-Public-Domain packs need a Licences row whose cell equals PACK.yaml `license`. Public Domain packs are exempt, and an extra Licences row fails the routing-map check. Cap is six packs per Topics row. This pack gets its own Topics row (`Civil infrastructure & ITS`, one pack) and its own Agency row (`FHWA / USDOT ITS`). Leave the existing `NHTSA / USDOT` row on `nhtsa-vehicle`. Do not merge them. Do not put `fhwa-its-se` on the CISA / DHS row (line 129, pack `cisa-cpg`).
- Cursor manifest paths are `./packs/<slug>/SKILL.md`. Claude plugin paths are `./packs/<slug>`. Cursor check fails if an eligible pack (`commercial_use` not false) is missing. Claude plugin skills array is not count-gated; spec D6 still requires the insert. Do not change either file's `version`.
- Catalogue count loci that `check_catalogue_count` and `[pack-count]` compare: `docs/index.html` section 06 h2 `72 packs · 8 signposts`; chip labels whose COUNT sums to 72 (the chip parser adds every chip whose label does not contain `signpost` or `orchestrator`); `docs/assets/still-catalogue.svg` subtitle `72 packs  ·  8 signposts  ·  open sources only` and footer `72 PACKS · 8 SIGNPOSTS · FILTER ON packs.html`; `docs/products/website/01-jgs-se-knowledge-packs.yaml` line 47 `72 packs across the SE catalogue`. The skills sentence in `docs/index.html` (`81 skills in all`: 72 knowledge packs) is not parsed by the chip regex, but it states the same inventory and must move with it. README badge is `packs-72`.
- `SKILLS.md` line 9 says `72 packs (+8 signposts, +1 orchestrator)`. The new table row goes after the `jsp-936` row (line 80).
- `NOTICE` public-domain shape is the `[pack: faa-8110-49]` block (line 757). Insert the new block after the `[pack: jsp-936]` block (line 799) and before `[pack: nrc-nuclear]` (line 812).
- `catalog.json` live row keys, in order, match `faa-8110-49`: `slug`, `title`, `publisher`, `source_version`, `license`, `license_tier`, `commercial_use`, `chapters`, `status`. `"updated"` is `2026-10-14` and must stay that string. Insert the new object after the `jsp-936` object, which is the last live row.
- `docs/candidate-packs.md` numbered table ends at row 8. Insert row 9 only. The sentence at line 25 says the remaining full-pack work is the unfinished part of the uk-defence family, and that sentence must stop hiding this pack. The catalogue-count sentence at line 29 says 81 packs / 72 full content packs and must become 82 / 73. The `fhwa-its-se` proposed-pack bullet is line 74. No other candidate row changes.
- `docs/superpowers/backlog.md` b-32 is line 52, status `promoted`. Change status to `done`. Do not delete the row.
- `sources/` is gitignored (`.gitignore` line 17). The PDF and the text extract stay untracked. `git ls-files sources/` must stay empty.

## Research

research: skipped (2026-10-27 research gate already pinned and licence-cleared the December 2022 PDF at page level; no new external research needed. The build re-fetches the FHWA PDF at execution time.)

Page-level pin from the spec, not re-verified by this plan. Task 1 re-vets it:

- PDF: https://ops.fhwa.dot.gov/seits/files/segbv4rem.pdf
- Landing page that names the same file: https://ops.fhwa.dot.gov/seits/
- Parent page that states the federal systems-engineering analysis rule: https://ops.fhwa.dot.gov/int_its_deployment/sys_eng.htm
- Identity expected from the PDF body, not from a cover sheet: title Systems Engineering for ITS; publisher Federal Highway Administration, U.S. Department of Transportation; fourth generation, published December 2022; 223 numbered pages; no title page and no report number. Alignment claim names the 4th Edition INCOSE Systems Engineering Handbook and ISO/IEC/IEEE 15288:2015. Those standards are named, not reproduced.
- Spec fetch on 2026-10-27: HTTP 200, `application/pdf`, 5,801,248 bytes, 223 pages. Task 1 records the execution-time byte size and page count. The spec numbers are a check, not a lock, except the December 2022 sentence, which is a stop condition.

Provisional chapter map, discarded where the PDF contents list disagrees:

| Ch | PDF sections | Working title |
|---|---|---|
| 01 | 1 | Introduction, purpose, audience |
| 02 | 2 | What systems engineering is, life-cycle models, USDOT rules |
| 03 | 3.1-3.3.7 | V process through requirements and design |
| 04 | 3.3.8-3.3.13 | Implementation through operations and retirement |
| 05 | 3.4 | Cross-cutting processes: project management, configuration, traceability, risk, trade studies |
| 06 | 4 | Managing SE projects: agency view, tailoring, ITS procurement |
| 07 | 5-6 | Implementing SE in the agency, templates and checklists |

If the contents list has no section 5 or 6, drop chapter 07 and keep six. If a top-level section is only a template appendix, fold it into chapter 07 or drop it. Do not exceed eight files. Do not write a chapter the PDF does not contain.

## File map

Create:

- `packs/fhwa-its-se/PACK.yaml`
- `packs/fhwa-its-se/LICENSE`
- `packs/fhwa-its-se/SKILL.md`
- `packs/fhwa-its-se/chapters/chNN-<slug>.md` (6, 7, or 8 files, frozen in Task 1)
- `packs/fhwa-its-se/glossary.md`
- `packs/fhwa-its-se/cheatsheet.md`
- `sources/fhwa-its-se/segbv4rem.pdf` (untracked; do not commit)
- `sources/fhwa-its-se/body.txt` (untracked; do not commit)
- `docs/packs/fhwa-its-se/index.html` (generator output; do not hand-write)

Modify:

- `catalog.json` (one live row; `"updated"` untouched)
- `docs/source-watchlist.json` (one source row)
- `SKILLS.md` (count line, one table row)
- `packs/se/SKILL.md` (one Topics row, one Agency row; no Licences row)
- `.claude-plugin/plugin.json` (one skills entry; `version` untouched)
- `.cursor-plugin/plugin.json` (one skills entry; `version` untouched)
- `NOTICE` (one public-domain block)
- `README.md` (badge, one table row, catalogue-count sentence if present)
- `docs/index.html` (section 06 h2, one new chip, skills sentence)
- `docs/assets/still-catalogue.svg` (subtitle, footer)
- `docs/products/website/01-jgs-se-knowledge-packs.yaml` (pack-count claim, one FHWA line)
- `docs/candidate-packs.md` (row 9, remaining-full-pack sentence, catalogue-count sentence, `fhwa-its-se` bullet)
- `docs/superpowers/backlog.md` (b-32 status and evidence only)
- `docs/classification-rules.json` (N assignments)
- `docs/capability-pack-map-note-overrides.json` (N notes)
- `tooling/generate_capability_map.py` (four `728` literals become `728 + N`)
- `docs/capability-pack-map.json` and `docs/capability-pack-map.md` (regenerated)
- `docs/packs.html` and `docs/sitemap.xml` (regenerated)
- `CHANGELOG.md` (one `[Unreleased]` Added bullet)

Do not modify: `docs/LICENSING.md`, `RELEASE-INFO.txt`, `tooling/validate_pack.py`, `docs/products/website/catalog.yaml`, `packs/jsp-936/`, `packs/faa-8110-49/`, `packs/nhtsa-vehicle/`, `packs/cisa-cpg/`, `.claude-plugin/marketplace.json`.

---

### Task 1: Vet the PDF, freeze the chapter map, write LICENSE and PACK.yaml

**Gate:** gate-enforced (spec D2 stop, pack skeleton).

**Files:**
- Create: `packs/fhwa-its-se/PACK.yaml`
- Create: `packs/fhwa-its-se/LICENSE`
- Create: `sources/fhwa-its-se/segbv4rem.pdf` (untracked)
- Create: `sources/fhwa-its-se/body.txt` (untracked)
- Read: `packs/faa-8110-49/LICENSE` (shape only; do not edit)

**Interfaces:**
- Consumes: the spec pin URL and the December 2022 sentence.
- Produces: `CHAPTER_COUNT` (integer 6, 7, or 8), `PAGE_COUNT` (integer), `BYTE_SIZE` (integer), `VET_DATE` (`YYYY-MM-DD`), the frozen basename list `chNN-kebab-title.md`, and the pin string `Systems Engineering for ITS, fourth generation (December 2022)`. Tasks 2, 3, 4, and 5 copy those values. They do not re-decide them.

**Model:** standard

Per-task brief: `.superpowers/sdd/2026-10-27-fhwa-its-se-pack/task-1-brief.md`

- [ ] **Step 1: Record the execution date and re-fetch the PDF**

```bash
python -c "import datetime; print(datetime.date.today().isoformat())"
```

Call that date `VET_DATE`. It must be `YYYY-MM-DD`. It is `build.built_on` and the watchlist `last_checked`. Do not hard-code `2026-10-27` unless that is the date the command prints.

Download the PDF. Do not `pip install` anything.

```bash
mkdir -p sources/fhwa-its-se
curl -fsSL -o sources/fhwa-its-se/segbv4rem.pdf "https://ops.fhwa.dot.gov/seits/files/segbv4rem.pdf"
python -c "
import hashlib, pathlib
p = pathlib.Path('sources/fhwa-its-se/segbv4rem.pdf')
data = p.read_bytes()
print('bytes', len(data))
print('sha256', hashlib.sha256(data).hexdigest())
print('head', data[:5])
"
```

Expected: exit 0, `head` starts with `b'%PDF'`. Record `BYTE_SIZE`.

Extract text. Prefer `pdftotext -layout` if `command -v pdftotext` succeeds. Otherwise use an already-installed reader (`pypdf` or `fitz`). Do not `pip install` a PDF library. If no reader is available, stop and report. Write the extract to `sources/fhwa-its-se/body.txt`.

Confirm from the PDF, not from the spec:

- The introduction page contains the sentence that this is fourth generation Systems Engineering for ITS content, published December 2022, combining and updating the FHWA Systems Engineering Guidebook (SEGB) and Systems Engineering Handbook (SEHB).
- Page count is recorded as `PAGE_COUNT`. The spec's 223 is a check, not a lock. A different count is not a stop if the December 2022 sentence is present.
- Cover and front matter contain no line that reserves copyright to a contractor.
- No report number appears. Record the absence. Do not invent one.

Stop and report, without writing chapter prose, if any of these hold:

- The December 2022 fourth-generation sentence is absent.
- A contractor copyright line reserves copyright.
- The file is not a PDF, or the fetch is not HTTP 200.

The 2026-10-27 spec fetch is not a substitute for this re-fetch.

- [ ] **Step 2: Freeze 6 to 8 chapter titles from the contents list**

Read the contents list in `sources/fhwa-its-se/body.txt`. Produce 6, 7, or 8 rows. Each row has a basename `chNN-kebab-title.md` and the printed page range that feeds it.

Rules:

- The PDF contents list wins over the provisional table in Research.
- One file per numbered top-level section. Subsections stay inside the parent chapter.
- Do not split 3.3.1 through 3.3.13 into thirteen chapters.
- If the contents list has no section 5 or 6, drop provisional chapter 07 and keep six.
- If a top-level section is only a template appendix, fold it into the last chapter or drop it.
- Do not exceed eight files. Do not write a chapter the PDF does not contain.
- If the body cannot be covered in 6 to 8 chapters without inventing a theme, stop and report the contents list. Do not write a ninth chapter.

Basenames must match `^ch[0-9]{2}-[a-z0-9-]+\.md$`. Save the frozen list in the executor notes that Tasks 2, 3, and 4 will read. Call the file count `CHAPTER_COUNT`.

- [ ] **Step 3: Write `packs/fhwa-its-se/PACK.yaml`**

Replace `VET_DATE`, `PAGE_COUNT`, `BYTE_SIZE`, and `CHAPTER_COUNT` with the values from Steps 1 and 2. `CHAPTER_COUNT` is 6, 7, or 8.

```yaml
slug: fhwa-its-se
title: "Systems Engineering for ITS"
publisher: "Federal Highway Administration"
source_version: "Systems Engineering for ITS, fourth generation (December 2022)"
license: "Public Domain (US Government work, 17 U.S.C. § 105)"
license_tier: 1
commercial_use: true
share_alike: false
attribution_required: false
build:
  method: "Synthesized from the Systems Engineering for ITS PDF pinned on VET_DATE. Not adapted from a sibling prototype."
  source_pages: PAGE_COUNT
  chapters: CHAPTER_COUNT
  built_on: "VET_DATE"
notes: >
  US Government work, 17 U.S.C. § 105. Public domain in the United States.
  No attribution duty. Courtesy attribution only. FHWA does not endorse
  this pack. Vetted on VET_DATE: BYTE_SIZE bytes, PAGE_COUNT pages, no
  report number in the file, December 2022 fourth-generation sentence
  present, no contractor copyright reservation. INCOSE, ISO/IEC/IEEE
  15288, NTCIP, IEEE, SAE, and other third-party standards are named
  and not quoted. Source identification and the reconstructed-notes
  statement are in packs/fhwa-its-se/LICENSE.
change_indication: "reconstructed as synthesized reference notes"
```

No `source_url` key. No URL anywhere in the file. `source_pages` and `chapters` are bare integers. Mandatory fields above `build:` stay column-0 scalars. The `notes` block is the D2 manifest. Do not keep a second list of vet facts.

- [ ] **Step 4: Write `packs/fhwa-its-se/LICENSE`**

Model the file on `packs/faa-8110-49/LICENSE`. Do not copy the OGL deed. Section order:

1. Heading `fhwa-its-se pack: content licence`.
2. Statute line: work of the United States Government, 17 U.S.C. § 105. Public domain in the United States. No attribution duty. Courtesy attribution only.
3. Source identification, by title, publisher, and date only: Federal Highway Administration, U.S. Department of Transportation, Systems Engineering for ITS, fourth generation, published December 2022. State the pin was verified on `VET_DATE` (byte size, page count, no report number). State the contractor-copyright scan found no reservation. No download URL.
4. Non-endorsement: FHWA does not endorse this pack.
5. Nature: reconstructed reference notes, not a reproduction, not official FHWA guidance.
6. Named-not-quoted: INCOSE Systems Engineering Handbook, ISO/IEC/IEEE 15288, NTCIP, IEEE, SAE, and other third-party standards the PDF names are identified and not quoted. No clause text. No PDF figures.
7. Repo MIT licence covers tooling and scaffolding only. Pack content is the source's public-domain terms.

No `http://` or `https://` in the file. The sibling rule omitted the download URL, so URLs appear nowhere in the pack, including LICENSE.

- [ ] **Step 5: Verify the skeleton**

```bash
python -c "
import pathlib
p = pathlib.Path('packs/fhwa-its-se/PACK.yaml').read_text(encoding='utf-8')
assert 'source_url' not in p
assert 'https://' not in p and 'http://' not in p
assert 'license: \"Public Domain (US Government work, 17 U.S.C. § 105)\"' in p
assert 'source_version: \"Systems Engineering for ITS, fourth generation (December 2022)\"' in p
assert 'slug: fhwa-its-se' in p
assert 'title: \"Systems Engineering for ITS\"' in p
assert 'publisher: \"Federal Highway Administration\"' in p
assert 'license_tier: 1' in p
assert 'commercial_use: true' in p
assert 'share_alike: false' in p
assert 'attribution_required: false' in p
assert 'change_indication: \"reconstructed as synthesized reference notes\"' in p
assert '17 U.S.C.' in p
assert 'no report number' in p
lic = pathlib.Path('packs/fhwa-its-se/LICENSE').read_text(encoding='utf-8')
assert '17 U.S.C.' in lic
assert 'does not endorse' in lic
assert 'https://' not in lic and 'http://' not in lic
assert 'Open Government Licence' not in lic
print('skeleton ok')
"
git check-ignore -v sources/fhwa-its-se/segbv4rem.pdf
git ls-files sources/
```

Expected: `skeleton ok`, the ignore rule matches the PDF, and `git ls-files sources/` is empty.

---

### Task 2: Write chapters, glossary, cheatsheet, and SKILL.md

**Gate:** gate-enforced (validate_pack, check_pack_quality, URL scan).

**Files:**
- Create: `packs/fhwa-its-se/chapters/chNN-<slug>.md` (the frozen list from Task 1)
- Create: `packs/fhwa-its-se/glossary.md`
- Create: `packs/fhwa-its-se/cheatsheet.md`
- Create: `packs/fhwa-its-se/SKILL.md`
- Read: `sources/fhwa-its-se/body.txt` (do not commit)

**Interfaces:**
- Consumes: frozen basenames, page ranges, `CHAPTER_COUNT`, and `VET_DATE` from Task 1.
- Produces: chapter files whose basenames later tasks copy into classification rows, with the `.md` suffix. SKILL.md Topic Index `chNN` tokens must match those basenames. `check_pack_quality.py` resolves them against the files.

**Model:** deep

Per-task brief: `.superpowers/sdd/2026-10-27-fhwa-its-se-pack/task-2-brief.md`

- [ ] **Step 1: Write one chapter file per frozen row**

For each frozen row, write `packs/fhwa-its-se/chapters/<basename>`. Open with a `Sources:` line naming the printed page range. Then an H1 equal to the working title. Then prose of at least 30 lines.

Synthesis rules:

- Synthesize. Do not paste a run of more than one source sentence. A short defined term may be kept and marked as a defined term.
- Do not copy tables as reconstructed shall-lists. Describe the decision rule in prose.
- Name INCOSE, ISO/IEC/IEEE 15288, NTCIP, IEEE, SAE, and other third-party standards the page range names. Do not quote clause text. Do not embed page images.
- Ground every claim in the page range for that chapter. Do not borrow another chapter's range to fill length.
- Chapter section shape, in order, when the source supports the heading: `Core Idea`, `Frameworks Introduced`, `Key Concepts`, `Mental Models`, `Anti-patterns` (only if the source states a refusal), `Key Takeaways`, `Connects To`. Skip a heading the page range does not support. Do not invent a framework the PDF does not contain.
- Stay inside D4. Do not write construction specifications, FEMA content, or a general SE textbook chapter.
- No `http://` or `https://` in any chapter.

If a frozen row's page range has no usable prose, stop and report. Do not write a stub under 30 lines.

- [ ] **Step 2: Write `glossary.md` and `cheatsheet.md`**

`glossary.md`: terms the document defines, alphabetical. Each entry names the `chNN` that uses it. No URLs. No assignment row will be created for this file.

`cheatsheet.md`: decision rules and tailoring or procurement tables, described in prose, not copied as page images. No URLs. No assignment row will be created for this file.

- [ ] **Step 3: Write `packs/fhwa-its-se/SKILL.md`**

Frontmatter:

```yaml
---
name: fhwa-its-se
description: "Knowledge pack synthesized from Systems Engineering for ITS, fourth generation (December 2022, Federal Highway Administration, US Government work, 17 U.S.C. § 105): ITS project systems engineering for transportation agencies. SCOPE LIMITS: single-source (December 2022 FHWA PDF); not construction specifications, not FEMA, not device model-document libraries, not a general SE textbook; INCOSE, ISO/IEC/IEEE 15288, NTCIP, IEEE, and SAE named, not quoted; reconstructed reference notes, not FHWA guidance, and no FHWA endorsement."
---
```

Body order, matching PACK-SPEC:

1. H1: `Systems Engineering for ITS`
2. `## When to use` then, on the next line, `**Prerequisites:**` naming what the reader should already know (plain Markdown; familiarity with a project life cycle helps; the glossary defines ITS-specific terms). Then one paragraph: use this skill for questions about how a transportation agency runs systems engineering on an ITS project. It does not cover construction specifications, FEMA publications, or device model-document libraries.
3. A `**Source:**` line with the pin, Federal Highway Administration, public-domain statement, reconstructed-notes statement, and a relative link `[LICENSE](LICENSE)`. No absolute URL.
4. `## How to use this skill`: four bullets. With no arguments, read Core Frameworks. For a topic, use the Topic Index. For a life-cycle question, use the Chapter Index. For a term, use `glossary.md`. For a decision rule, use `cheatsheet.md`.
5. `## Core Frameworks & Mental Models`: two to four subsections drawn only from the PDF (what the V process is in this document, what the USDOT systems-engineering analysis rule requires, how tailoring works). Do not invent a framework the PDF does not contain.
6. `## Chapter Index`: one line per frozen chapter, linking `chapters/<basename>`.
7. `## Topic Index`: keyword lines whose `chNN` tokens match the frozen basenames. Cover V process, ConOps, requirements, design, implementation, integration, verification, validation, operations, retirement, cross-cutting processes, tailoring, and ITS procurement, plus any extra top-level section Task 1 kept.
8. `## Supporting Files`: `glossary.md` and `cheatsheet.md`, one line each.
9. `## Scope & Limits`: source version and `VET_DATE`; ITS project systems engineering only; not construction specifications; not FEMA; not device model documents; not a general SE textbook; third-party standards named, not quoted; not official FHWA guidance.

No `http://` or `https://` in the file.

- [ ] **Step 4: Run the pack gates**

```bash
python tooling/validate_pack.py packs/fhwa-its-se
python tooling/check_pack_quality.py packs/fhwa-its-se
python -c "
import pathlib
root = pathlib.Path('packs/fhwa-its-se')
bad = []
for p in root.rglob('*'):
    if p.is_file():
        text = p.read_text(encoding='utf-8')
        if 'https://' in text or 'http://' in text:
            bad.append(str(p))
assert not bad, bad
print('no urls in pack')
"
```

Expected: `validate_pack.py` exits 0, `check_pack_quality.py` prints `PASS  fhwa-its-se` and exits 0, and the URL scan prints `no urls in pack`.

If a chapter is under 30 lines, add synthesis from its own page range. Do not borrow another chapter's range.

---

### Task 3: Catalogue, watchlist, indexes, routing, and count sentences

**Gate:** gate-enforced (catalog live set, source-watch coverage, routing-map Topics coverage, routing-map licence exemption, SKILLS.md row, cursor manifest).

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
- Consumes: `CHAPTER_COUNT` and `VET_DATE` from Task 1, and the pin string `Systems Engineering for ITS, fourth generation (December 2022)`.
- Produces: a live catalog row and a watchlist row that Task 4's `--record` and Task 5's release gate both require. Cursor path is `./packs/fhwa-its-se/SKILL.md`. Claude path is `./packs/fhwa-its-se`.

**Model:** standard

Per-task brief: `.superpowers/sdd/2026-10-27-fhwa-its-se-pack/task-3-brief.md`

- [ ] **Step 1: Add the catalog row**

Insert one object in `catalog.json` `packs`, after the `jsp-936` object (the last live row). Do not change `"updated"` (`2026-10-14`). Do not add `source_url`. Keys in this order, matching `faa-8110-49`:

```json
{
  "slug": "fhwa-its-se",
  "title": "Systems Engineering for ITS",
  "publisher": "Federal Highway Administration",
  "source_version": "Systems Engineering for ITS, fourth generation (December 2022)",
  "license": "Public Domain (US Government work, 17 U.S.C. § 105)",
  "license_tier": 1,
  "commercial_use": true,
  "chapters": CHAPTER_COUNT,
  "status": "live"
}
```

`CHAPTER_COUNT` is the integer from Task 1, not the token. Keep JSON valid.

- [ ] **Step 2: Add the watchlist row, then record**

`--record` refuses a slug that is not already in the file, and also refuses when the watchlist and the live catalog disagree. The catalog row from Step 1 must exist first. Insert one object in `docs/source-watchlist.json` `sources`, after the `jsp-936` source. Keys in this order:

```json
{
  "slug": "fhwa-its-se",
  "publisher": "Federal Highway Administration",
  "document": "Systems Engineering for ITS, fourth generation (December 2022)",
  "version": "Systems Engineering for ITS, fourth generation (December 2022)",
  "last_checked": "VET_DATE",
  "hint": ""
}
```

`document` and `version` must equal PACK.yaml `source_version`. No URL in any value. Then run:

```bash
python tooling/check_source_watch.py --record fhwa-its-se "Systems Engineering for ITS, fourth generation (December 2022)" VET_DATE
python tooling/check_source_watch.py
```

Expected: both exit 0. The record line names `fhwa-its-se`. A refusal that says the slug is absent means Step 2's insert was skipped. A coverage failure means the catalog row or the watchlist row is missing. Fix the row. Do not add a URL.

- [ ] **Step 3: SKILLS.md, NOTICE, README, plugins, CHANGELOG**

`SKILLS.md` line 9: change `72 packs (+8 signposts, +1 orchestrator)` to `73 packs (+8 signposts, +1 orchestrator)`. After the `jsp-936` table row, insert:

```markdown
| [`fhwa-its-se`](packs/fhwa-its-se/SKILL.md) | Public Domain (US Government work, 17 U.S.C. § 105) | Synthesized reference notes from Systems Engineering for ITS, fourth generation (December 2022); ITS project systems engineering for transportation agencies; INCOSE, ISO/IEC/IEEE 15288, and NTCIP named, not quoted. |
```

`NOTICE`: after the `[pack: jsp-936]` block and before `[pack: nrc-nuclear]`, insert one block in the `faa-8110-49` shape. No OGL deed lines.

```text
[pack: fhwa-its-se]

Source  : Systems Engineering for ITS, fourth generation (December 2022).
          Federal Highway Administration, U.S. Department of Transportation.
Author  : Federal Highway Administration
Licence : Public Domain (US Government work, 17 U.S.C. § 105)
Changes : reconstructed as synthesized reference notes (not a reproduction)
Terms   : no attribution duty. Courtesy attribution only. FHWA does not
          endorse this pack. INCOSE, ISO/IEC/IEEE 15288, NTCIP, IEEE, SAE,
          and other third-party standards are named and not quoted.
          See packs/fhwa-its-se/LICENSE.
```

`.claude-plugin/plugin.json`: insert `"./packs/fhwa-its-se"` in the `skills` array, beside the existing `./packs/jsp-936` entry. Do not change `version`. Keep JSON valid.

`.cursor-plugin/plugin.json`: insert `"./packs/fhwa-its-se/SKILL.md"` in the `skills` array, beside the existing jsp entry. Do not change `version`. Keep JSON valid. The cursor gate matches `packs/<slug>/SKILL.md` and fails if the path is missing.

`README.md`: change the badge from `packs-72` to `packs-73` in both the shields.io URL and the alt text (`https://img.shields.io/badge/packs-73-blueviolet`, alt `73 packs`). Add one table row after the `jsp-936` row, same column shape as the surrounding rows:

```markdown
| `fhwa-its-se` | Systems Engineering for ITS, fourth generation (December 2022), FHWA | Public domain (US gov) | 🟢 1 | ✅ live (CHAPTER_COUNT chapters) |
```

The table has five columns: slug, source/title, licence, tier, status+chapters. Copy the `fda-med-device` row's licence/tier/status cell shapes exactly.

If README has a catalogue-count sentence that states 72 or 81, move it to 73 or 82. Do not invent a sentence that is not there.

`CHANGELOG.md`: under `## [Unreleased]` / `### Added`, add one bullet. Do not add a version heading. Do not edit `## [1.22.1]`. Do not edit the existing Changed bullet that says the plugin declares 80 skill paths. That sentence is a historical crawl note, not a count the release gate parses.

```markdown
- `fhwa-its-se` content pack from Systems Engineering for ITS, fourth generation (December 2022), reconstructed notes, registered on the catalogue surfaces.
```

- [ ] **Step 4: Routing map**

In `packs/se/SKILL.md`, inside `ROUTING-MAP:BEGIN` / `ROUTING-MAP:END`:

Add a Topics row. One pack, inside the six-pack cap. Do not add `fhwa-its-se` to any existing Topics row. Do not edit a neighbor pack's keywords to make room.

```markdown
| Civil infrastructure & ITS | intelligent transportation, ITS, systems engineering analysis, 23 CFR 940, ConOps | `fhwa-its-se` |
```

Add an Agency row. Leave the existing `NHTSA / USDOT` row on `nhtsa-vehicle`. Do not merge them. Do not put `fhwa-its-se` on the CISA / DHS row.

```markdown
| FHWA / USDOT ITS | FHWA, ITS, systems engineering analysis | `fhwa-its-se` |
```

Do not add a Licences row. Public Domain packs are exempt, and the routing-map check errors on an extra row.

- [ ] **Step 5: Count loci the release gate parses**

These claims must move together. Signpost count stays 8. Orchestrator stays 1.

`docs/index.html` section 06 h2: `72 packs` becomes `73 packs`. The skills sentence `81 skills in all` becomes `82 skills in all`, and `72 knowledge packs` becomes `73 knowledge packs`.

Add one chip inside the section 06 pack grid, after the `NHTSA / USDOT · 1` chip. The chip parser adds every chip whose label does not contain `signpost` or `orchestrator` to the content sum, so this chip's COUNT must be 1 and no other chip COUNT changes. Chip sum must equal 73.

```html
    <div class="pk"><b>FHWA / USDOT · 1</b><span>Systems Engineering for ITS, fourth generation (December 2022)</span></div>
```

`docs/assets/still-catalogue.svg`: subtitle `72 packs` becomes `73 packs`. Footer `72 PACKS` becomes `73 PACKS`. Leave the signpost strings alone.

`docs/products/website/01-jgs-se-knowledge-packs.yaml` line 47: `72 packs across the SE catalogue` becomes `73 packs across the SE catalogue`. In the same detail block, after the `NHTSA / USDOT (1)` sentence, add one sentence: `FHWA / USDOT (1): Systems Engineering for ITS, fourth generation (December 2022).` Do not change the YAML `version:` field. Do not change the UK MOD `(3)` line.

- [ ] **Step 6: Resolve b-32 (D7)**

`docs/candidate-packs.md`:

Insert build-order row 9 after row 8. Do not edit rows 1 through 8.

```markdown
| 9 | `fhwa-its-se` | full | built VET_DATE. Tier-1 civil infrastructure, pinned to Systems Engineering for ITS, fourth generation (December 2022) |
```

`VET_DATE` is the date from Task 1, not the token.

Replace the sentence that says the remaining full-pack work on this list is the unfinished part of the uk-defence family. New sentence: `The remaining full-pack work on this list is the unfinished part of the uk-defence family. Civil infrastructure is no longer on that list: fhwa-its-se is built.`

Replace the catalogue-count sentence. Old: `The catalogue holds 81 packs: 72 full reconstructed content packs`. New: `The catalogue holds 82 packs: 73 full reconstructed content packs`. Leave the eight signpost names and the `/se` orchestrator clause as they are.

Mark the proposed-pack bullet built. Old start: `- \`fhwa-its-se\` (tier 1).` New start: `- \`fhwa-its-se\` (built VET_DATE) (tier 1).` Keep the rest of that bullet. Do not edit any other proposed-pack bullet. Do not rank `telecom-3gpp`.

`docs/superpowers/backlog.md` b-32 row: change status `promoted` to `done`. Append to the evidence cell: `done VET_DATE (P42, candidate-packs row 9).` Do not delete the row.

- [ ] **Step 7: Verify the registration text**

```bash
python -c "
import json, pathlib
cat = json.loads(pathlib.Path('catalog.json').read_text(encoding='utf-8'))
assert cat['updated'] == '2026-10-14'
row = next(p for p in cat['packs'] if p['slug'] == 'fhwa-its-se')
assert list(row.keys()) == ['slug', 'title', 'publisher', 'source_version', 'license', 'license_tier', 'commercial_use', 'chapters', 'status']
assert row['license'] == 'Public Domain (US Government work, 17 U.S.C. § 105)'
assert row['source_version'] == 'Systems Engineering for ITS, fourth generation (December 2022)'
assert row['license_tier'] == 1
assert row['status'] == 'live'
assert 'source_url' not in row
watch = json.loads(pathlib.Path('docs/source-watchlist.json').read_text(encoding='utf-8'))
w = next(s for s in watch['sources'] if s['slug'] == 'fhwa-its-se')
assert list(w.keys()) == ['slug', 'publisher', 'document', 'version', 'last_checked', 'hint']
assert w['document'] == row['source_version']
assert w['version'] == row['source_version']
assert 'http' not in json.dumps(w)
claude = json.loads(pathlib.Path('.claude-plugin/plugin.json').read_text(encoding='utf-8'))
assert './packs/fhwa-its-se' in claude['skills']
cursor = json.loads(pathlib.Path('.cursor-plugin/plugin.json').read_text(encoding='utf-8'))
assert './packs/fhwa-its-se/SKILL.md' in cursor['skills']
se = pathlib.Path('packs/se/SKILL.md').read_text(encoding='utf-8')
assert 'Civil infrastructure & ITS' in se
assert 'FHWA / USDOT ITS' in se
assert '\`fhwa-its-se\`' in se
# Licences table must not gain a row for this pack.
lic_start = se.index('### Licences')
lic_end = se.index('<!-- ROUTING-MAP:END -->')
assert 'fhwa-its-se' not in se[lic_start:lic_end]
notice = pathlib.Path('NOTICE').read_text(encoding='utf-8')
assert '[pack: fhwa-its-se]' in notice
assert 'Open Government Licence' not in notice.split('[pack: fhwa-its-se]')[1].split('[pack:')[0]
print('registration ok')
"
python tooling/check_source_watch.py
```

Expected: `registration ok`, and `check_source_watch.py` exits 0.

---

### Task 4: Classification rows, capability map, and generated pages

**Gate:** gate-enforced (classification-rules, capability-map, pack pages).

**Files:**
- Modify: `docs/classification-rules.json`
- Modify: `docs/capability-pack-map-note-overrides.json`
- Modify: `tooling/generate_capability_map.py` (four literals only)
- Generate: `docs/capability-pack-map.json`
- Generate: `docs/capability-pack-map.md`
- Generate: `docs/packs/fhwa-its-se/index.html`
- Generate: `docs/sitemap.xml`
- Generate: `docs/packs.html`

**Interfaces:**
- Consumes: frozen basenames from Task 2, including the `.md` suffix, and `VET_DATE` from Task 1. `CHAPTER_COUNT` is N. Map total after the cut is `728 + N`.
- Produces: N assignment rows and N note rows with identical `pack` and `chapter` pairs. The generator writes the map. Later tasks do not hand-edit the generated JSON or Markdown.

**Model:** standard

Per-task brief: `.superpowers/sdd/2026-10-27-fhwa-its-se-pack/task-4-brief.md`

- [ ] **Step 1: Hand-add N assignments and N notes**

N is `CHAPTER_COUNT` from Task 1. For each frozen chapter file, append one object to `docs/classification-rules.json` `assignments` and one object to `docs/capability-pack-map-note-overrides.json` `notes`. Same `pack` and `chapter` in both files. `chapter` is the basename with `.md`, matching Task 2.

Assignment object:

```json
{"pack": "fhwa-its-se", "chapter": "chNN-slug.md", "cluster": "CLUSTER", "is_support": false}
```

`cluster` must be a name already in `cluster_names`. Pick from the vocabulary the chapter actually supports. Likely fits, and only if the chapter supports the name: `Standards, Tailoring & Process Models`, `Requirements Engineering`, `Verification`, `Validation`, `Governance, Reviews, Gates & Control Points`, `Supplier, Procurement & Acquisition`, `Operations, Maintenance & Disposal`. Do not invent a cluster. Do not add glossary or cheatsheet rows. `is_support` stays false unless the chapter is only a pointer chapter, which this pack does not have.

Note object:

```json
{"pack": "fhwa-its-se", "chapter": "chNN-slug.md", "note": "One sentence from Systems Engineering for ITS, December 2022, naming what the chapter covers."}
```

Note rules: one sentence, no em dash, no spaced double hyphen used as a dash, and the sentence says the note is from Systems Engineering for ITS, December 2022. No URL.

Do not change `generated_on` by hand in either file before the generator run except to set both source envelopes to `VET_DATE`. The generator writes the map date from `--generated-on`. After generation, rules `generated_on` and overrides `generated_on` must equal that date, because `check_classification_rules.py` compares rules `generated_on` to the live map. Set all three to `VET_DATE`.

- [ ] **Step 2: Move the 728 pin**

In `tooling/generate_capability_map.py`, replace the four `728` literals (lines 9, 195, 203, and 204) with the computed total `728 + N` written as a single decimal number (for example `735` when N is 7), not an arithmetic expression — the file must contain plain integer literals. Do not change any other number in that file.

```bash
python -c "
import pathlib
text = pathlib.Path('tooling/generate_capability_map.py').read_text(encoding='utf-8')
print('728 count', text.count('728'))
"
```

Expected: `728 count 0`. If a `728` remains, the generator will reject the new note file. Do not edit the generator beyond those four literals.

- [ ] **Step 3: Regenerate the map and check it**

Set `generated_on` on the rules file and the overrides file to `VET_DATE` if Step 1 did not already. Then:

```bash
python tooling/generate_capability_map.py --generated-on VET_DATE --sync-md
python tooling/check_capability_map.py
python tooling/check_classification_rules.py
```

Expected: all three exit 0. If the generator reports `notes length must be 728`, Step 2 was missed. If the check reports an assignment missing a note, the paired rows disagree. Fix the rows. Do not edit the generator beyond the four literals. Do not hand-edit `docs/capability-pack-map.json` or `docs/capability-pack-map.md`.

- [ ] **Step 4: Generate pack pages**

```bash
python tooling/gen_pack_pages.py --only fhwa-its-se
python tooling/gen_packs_page.py
```

`--only` is the execution command. Do not write `--only` into a committed comment as if it were the generator's default. A later full regen is `python tooling/gen_pack_pages.py` with no flag. This task uses `--only` because the spec names it and a full regen rewrites every pack page.

Expected: both exit 0. `docs/packs/fhwa-its-se/index.html` exists. `docs/sitemap.xml` contains the fhwa-its-se URL.

```bash
python -c "
import pathlib
assert pathlib.Path('docs/packs/fhwa-its-se/index.html').is_file()
sm = pathlib.Path('docs/sitemap.xml').read_text(encoding='utf-8')
assert 'fhwa-its-se' in sm
print('pages ok')
"
```

Expected: `pages ok`.

---

### Task 5: Repo search, prose check, and the release gate

**Gate:** gate-enforced (spec testing items 5 through 8, `check_release.py`).

**Files:**
- Test only. Edit a file from an earlier task only to fix a failure this task's commands print.

**Interfaces:**
- Consumes: the pack tree from Tasks 1 and 2 and the registration from Tasks 3 and 4.
- Produces: a passing `python tooling/check_release.py` transcript. No commit.

**Model:** flash

Per-task brief: `.superpowers/sdd/2026-10-27-fhwa-its-se-pack/task-5-brief.md`

- [ ] **Step 1: Search the D6 surfaces and the URL rule**

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
    'docs/packs/fhwa-its-se/index.html',
    'docs/sitemap.xml',
    'docs/candidate-packs.md',
    'docs/superpowers/backlog.md',
    'README.md',
    'CHANGELOG.md',
]
for s in surfaces:
    text = pathlib.Path(s).read_text(encoding='utf-8')
    assert 'fhwa-its-se' in text, s
print('surfaces name fhwa-its-se')
root = pathlib.Path('packs/fhwa-its-se')
for p in root.rglob('*'):
    if p.is_file():
        text = p.read_text(encoding='utf-8')
        assert 'https://' not in text and 'http://' not in text, p
print('pack has no urls')
"
```

Expected: both prints, exit 0.

- [ ] **Step 2: Prose check on the new pack**

```bash
python ~/.zcode/scripts/prose_check.py packs/fhwa-its-se/SKILL.md packs/fhwa-its-se/glossary.md packs/fhwa-its-se/cheatsheet.md packs/fhwa-its-se/chapters
```

Expected: exit 0, or only findings you fix in the same files before continuing. Zero em dashes in headings and body prose. Do not edit `packs/faa-8110-49` or `packs/jsp-936`. Do not edit the spec unless execution changed it. If execution changed the spec, run the same script on `docs/superpowers/specs/2026-10-27-fhwa-its-se-pack.md` and fix only findings this cut introduced.

- [ ] **Step 3: Release gate and the catalog tests**

```bash
python tooling/check_release.py
python tooling/test_catalog_live_set.py
python tooling/test_catalogue_count.py
python tooling/test_ci_gate.py
git ls-files sources/
```

Expected: `RELEASE CHECK: PASS` from `check_release.py`. The three test modules exit 0. `git ls-files sources/` is empty.

`test_catalog_live_set.py` asserts `catalog.json` `"updated"` is `2026-10-14`. If it fails on that string, revert the bump. Do not update the test.

If the gate fails, fix only the named surface. Common misses and the fix:

- `[catalogue-count]` or `[pack-count]`: a `72` remains in `docs/index.html` section 06, a chip COUNT, `still-catalogue.svg`, or the website YAML pack-count claim. Change that claim to 73. Do not change signpost counts. Chip COUNT sum must equal 73.
- `[index] SKILLS.md lists`: line 9 still says 72, or the new table row is missing.
- `[cursor]`: `.cursor-plugin/plugin.json` lacks `./packs/fhwa-its-se/SKILL.md`.
- `[routing-map]`: Topics Packs column lacks `fhwa-its-se`, or a Licences row was added for a Public Domain pack. Remove the Licences row. Do not add one.
- `[classification-rules]` or `[map-replay]`: assignment count, note count, and the four generator literals disagree, or `generated_on` differs across rules and the live map. Re-run Task 4 Step 3.
- `[source-watch]`: watchlist row missing, URL in a value, or `last_checked` not `YYYY-MM-DD`.
- `[sitemap]` or `[pack-rev]`: re-run `python tooling/gen_pack_pages.py --only fhwa-its-se`.

Do not bump `RELEASE-INFO.txt`. Do not bump either plugin `version`. Do not change `catalog.json` `updated`. Do not commit unless the parent execution mode says to commit. Do not push. Do not open a PR.

---

## Testing

All must pass before the cut is done. Commands are the gates, not suggestions.

1. `python tooling/validate_pack.py packs/fhwa-its-se` exits 0.
2. `python tooling/check_pack_quality.py packs/fhwa-its-se` exits 0. The script accepts a pack path. Floor is 30 lines per chapter. Topic Index `chNN` tokens resolve.
3. `python tooling/check_source_watch.py --record fhwa-its-se "Systems Engineering for ITS, fourth generation (December 2022)" <YYYY-MM-DD of the vet>` then `python tooling/check_source_watch.py` exits 0. Record only after the catalog live row and the hand-added watchlist row both exist. Coverage checks the live catalog against the watchlist in both directions.
4. `python tooling/generate_capability_map.py --generated-on <YYYY-MM-DD> --sync-md` then `python tooling/check_capability_map.py` and `python tooling/check_classification_rules.py` exit 0. Override row count must match rules row count. Map total is `728 + N`. On mismatch, fix the paired rows. Do not edit the generator beyond the four literals.
5. `python tooling/gen_pack_pages.py --only fhwa-its-se` and `python tooling/gen_packs_page.py` exit 0. `docs/packs/fhwa-its-se/index.html` exists. `docs/sitemap.xml` contains the fhwa-its-se URL.
6. Search the D6 surfaces for `fhwa-its-se` and confirm each names the pack. Search `packs/fhwa-its-se` for `http://` and `https://` and confirm no URL appears. D2's sibling rule omitted the download URL, so LICENSE has none either.
7. `python tooling/check_release.py` exits 0. Fix only findings this pack introduced.
8. `python tooling/test_catalog_live_set.py`, `python tooling/test_catalogue_count.py`, and `python tooling/test_ci_gate.py` exit 0. `test_catalog_live_set.py` locks `"updated"` at `2026-10-14`.
9. `python ~/.zcode/scripts/prose_check.py` on the new pack's prose files, and on the spec if execution edited it. Zero em dashes in headings and body prose.
10. `git ls-files sources/` is empty.

Count formulas, not a hardcoded chapter total: content packs 73, skills 82 (73 content + 8 signposts + 1 orchestrator), map assignments `728 + N` where N is the Task 1 chapter count (6, 7, or 8).

## Self-review

Spec coverage: D1 is Task 1 Step 1 (re-fetch, no invented report number, rejected candidates stay out). D2 is Task 1 Steps 1, 3, and 4 (tier-1 fields, stop conditions, notes manifest). D3 is Task 2 Step 1 (synthesized notes, named-not-quoted, no figures). D4 is Task 2 Steps 1 and 3 (scope limits in chapters and SKILL.md). D5 is Task 1 Step 2 (contents list wins, 6 to 8, no thirteen-way split). D6 is Task 3 (every registration surface) and Task 4 (rules, overrides, generated map and HTML). D7 is Task 3 Step 6 (row 9, bullet marked built, b-32 `done`, no other candidate ranked). D8 is Global Constraints and Task 5 Step 3 (no new tooling, no version bump, `updated` stays `2026-10-14`). Testing items 1 through 8 are the Testing section and Task 5. The Do not list is copied into Global Constraints.

Placeholder scan: no open slots, no deferred-work markers, no "similar to Task N" standing in for a step. `CHAPTER_COUNT`, `VET_DATE`, `PAGE_COUNT`, and `BYTE_SIZE` are Task 1 outputs, not open questions. Cluster names are a closed list the executor picks from the PDF, not a slot to invent.

Type consistency: pin string `Systems Engineering for ITS, fourth generation (December 2022)`, title `Systems Engineering for ITS`, publisher `Federal Highway Administration`, licence `Public Domain (US Government work, 17 U.S.C. § 105)`, and chapter basename with `.md` are defined in Task 1 and Task 2 and copied by Tasks 3 and 4. Catalog row key order matches `faa-8110-49`. Watchlist key order matches the live file. Cursor path is `./packs/fhwa-its-se/SKILL.md`. Claude path is `./packs/fhwa-its-se`.

Deviations from the spec: none.
