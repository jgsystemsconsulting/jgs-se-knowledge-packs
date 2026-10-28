# fhwa-its-se-pack

Package P42. Build `packs/fhwa-its-se` from one pinned FHWA/USDOT ITS systems-engineering document and register it on every live surface `jsp-936` already uses. This is the first civil-infrastructure content pack. It is tier 1 public domain, not an OGL cut.

## Research

Primary pin, fetched 2026-10-27 (HTTP 200, `application/pdf`, 5,801,248 bytes, 223 pages):

- https://ops.fhwa.dot.gov/seits/files/segbv4rem.pdf

Landing page that names the same file as the document view (HTTP 200):

- https://ops.fhwa.dot.gov/seits/

Parent page that states the federal systems-engineering analysis rule and links the document (HTTP 200):

- https://ops.fhwa.dot.gov/int_its_deployment/sys_eng.htm

Identity, taken from the PDF body, not from a cover sheet. The file has no title page and no report number.

- Title: Systems Engineering for ITS.
- Publisher: Federal Highway Administration, U.S. Department of Transportation. The site is the FHWA Office of Operations Systems Engineering for ITS (SEITS) resource.
- Edition: fourth generation. PDF page 4 states: "This fourth generation Systems Engineering for ITS content, published December 2022. It combines and updates content previously included in the FHWA Systems Engineering Guidebook (SEGB) and Systems Engineering Handbook (SEHB) publications."
- Page count: 223 numbered pages (pdftotext form-feed count).
- Alignment claim in the PDF: consistent with the 4th Edition INCOSE Systems Engineering Handbook and with ISO/IEC/IEEE 15288:2015. Those standards are named. They are not reproduced.
- Licence basis: work of the United States Government, 17 U.S.C. § 105. No copyright line appears in the PDF. Public domain in the United States. No attribution duty, no share-alike.

Rejected candidates, checked the same day:

- November 2009 Systems Engineering Guidebook for ITS. The historical URLs `https://ops.fhwa.dot.gov/publications/seitsguide/index.htm` and `https://ops.fhwa.dot.gov/publications/seitsguide/seguide.pdf` both return the FHWA Operations "page was not found" HTML (HTTP 200, 5,255 bytes, refresh to the Operations home page). Not a live pin.
- FHWA-OP-02-046, *Building Quality Intelligent Transportation Systems Through Systems Engineering*, April 2002, Mitretek Systems under contract DTFH61-00-C-00001. Live HTML at `https://ntlrepository.blob.core.windows.net/lib/jpodocs/repts_te/13620.html`. Contractor monograph. The December 2022 document says it supersedes that handbook generation. Not the pin.
- FHWA-HOP-18-060, *Model Systems Engineering Documents for Closed Circuit Television (CCTV) Systems*, May 2018, `https://ops.fhwa.dot.gov/publications/fhwahop18060/index.htm`. Device-class model documents. Out of scope.
- Caltrans/FHWA SEITS website Version 2.0 (TRID record 798737, publication date 2007-1-2, old URL `http://www.fhwa.dot.gov/cadiv/segb/index.htm`). Predecessor website edition. The current site replaces it. Not the pin.
- `https://www.fhwa.dot.gov/publications/research/operations/its/06108/06108.pdf` is FHWA-HRT-06-108, *Traffic Detector Handbook*, third edition, October 2006. Wrong document. Not the pin.

## Codebase context

Pattern precedent is `packs/jsp-936/` for registration, not for licence. `jsp-936` is tier 2 OGL. This pack copies the registration file list and the reconstructed-notes rule, and uses the tier 1 public-domain field set already in `packs/faa-8110-49/PACK.yaml` and `packs/nrc-nuclear/`.

Live counts before this cut: `catalog.json` `packs` 72, `docs/source-watchlist.json` `sources` 72, `docs/classification-rules.json` `assignments` 728, `docs/capability-pack-map-note-overrides.json` `notes` 728, `docs/capability-pack-map.md` total 728. Catalogue prose says 81 skills (72 content, 8 signposts, 1 orchestrator). Adding one content pack moves those to 73 content packs, 82 skills, and 728 plus the new chapter count on the map.

Registration surfaces that already name `jsp-936` and must name `fhwa-its-se`:

- `catalog.json` live row. Do not change the top-level `updated` field. P55 set it to `2026-10-14` and `tooling/test_catalog_live_set.py` asserts that string. A bump here would fail that test and reopen a frozen policy cut.
- `docs/source-watchlist.json` one source row.
- `SKILLS.md` count line and one pack row.
- `packs/se/SKILL.md` routing map: new civil-infrastructure topic row and an FHWA / USDOT agency row. No Licences row: `tooling/check_release.py` exempts Public Domain packs from the Licences table and errors on an extra row. Do not add this pack to the Defence row or the CISA critical-infrastructure row.
- `NOTICE` one public-domain block.
- `.claude-plugin/plugin.json` and `.cursor-plugin/plugin.json` skills arrays.
- `README.md` badge and any catalogue-count sentence that states 72 or 81.
- `docs/index.html` count sentences (72 packs, 81 skills).
- `docs/classification-rules.json` one assignment per chapter, existing cluster names only.
- `docs/capability-pack-map-note-overrides.json` one note per new assignment. Hand-add both files, then regenerate. Do not hand-edit `docs/capability-pack-map.json` or `docs/capability-pack-map.md`.
- `docs/packs/fhwa-its-se/index.html` via `tooling/gen_pack_pages.py --only fhwa-its-se` (rewrites `docs/sitemap.xml`).
- `docs/packs.html` via `tooling/gen_packs_page.py`.
- `CHANGELOG.md` one unreleased bullet. No version bump.
- `docs/candidate-packs.md` numbered build-order table and the `fhwa-its-se` proposed-pack bullet.
- `docs/superpowers/backlog.md` b-32 status only.

No `source_url` in `PACK.yaml` or `catalog.json`. Source and statute text live only in `packs/fhwa-its-se/LICENSE`. Same rule as `docs/PACK-SPEC.md`.

## Decision register

- D1: Source pin is Systems Engineering for ITS, fourth generation, December 2022, FHWA Office of Operations, one PDF at `https://ops.fhwa.dot.gov/seits/files/segbv4rem.pdf`. No report number exists in the file. Do not invent one. November 2009 SEGB, FHWA-OP-02-046, device model documents, and the Caltrans website edition stay out.
- D2: Licence class is tier 1 public domain. `license: "Public Domain (US Government work, 17 U.S.C. § 105)"`, `license_tier: 1`, `commercial_use: true`, `share_alike: false`, `attribution_required: false`. Not OGL. Not tier 2. Execution re-fetches the PDF before chapter prose and records byte size, page count, and the December 2022 sentence in `PACK.yaml` `notes`. Stop if that sentence is gone or the file is no longer a US Government work.
- D3: Reconstruction rule copies jsp-936. Synthesized reference notes. Short defined terms may be kept. No long verbatim passages. Name INCOSE, ISO/IEC/IEEE 15288, NTCIP, IEEE, SAE, and other third-party standards. Do not quote their clause text. Do not embed PDF figures.
- D4: Scope is ITS project systems engineering for transportation agencies: V process, ConOps, requirements, design, implementation, integration, verification, validation, operations, retirement, cross-cutting processes, tailoring, and ITS procurement. Not construction specifications, not FEMA, not device model-document libraries, not a general SE textbook.
- D5: Chapter count is one file per numbered top-level section in the PDF contents list, inside 6 to 8. The contents list wins over the provisional table: where the table groups subsections as separate chapters and the contents list numbers them under a top-level section, they merge into that section's one file. Expected outcome is six or seven files. Subsections stay inside the parent chapter. Do not split 3.3.1 through 3.3.13 into thirteen chapters. Chapter basenames are `chNN-kebab-title.md` frozen at step 2.
- D6: Full registration on every surface in Codebase context. Partial registration is the miss this package exists to avoid. `docs/candidate-packs.md` changes only the new numbered row and the `fhwa-its-se` bullet.
- D7: b-32 resolves inside this build. Add numbered build-order row 9 for `fhwa-its-se`, status built on the execution date. Mark the proposed-pack bullet built. Set backlog b-32 status to `done`. Do not rank `telecom-3gpp` or any other candidate.
- D8: No new tooling. Validators and generators already in `tooling/` are the gates. Do not bump `RELEASE-INFO`, plugin `version`, or `catalog.json` `updated`.

## Problem

`fhwa-its-se` is the only remaining named tier-1 public-domain full-pack candidate in civil infrastructure. `docs/candidate-packs.md` scores that sector FULL and lists the pack under Proposed packs. It has no `packs/` folder and no numbered build-order rank. Backlog b-32 carries the ranking question and is promoted into P42. Shipping a folder without the registration surfaces leaves a CI-green pack that `/se` and the indexes do not route. Shipping without a pinned FHWA document invites a construction-code dump or a superseded contractor handbook.

## Approach

One public PDF, one content pack, public-domain statement in `LICENSE`, reconstructed notes in chapters, then the same registration edits and generators `jsp-936` used, with tier-1 fields instead of OGL fields.

Execution order:

1. Vet. Re-fetch `https://ops.fhwa.dot.gov/seits/files/segbv4rem.pdf`. Confirm HTTP 200, PDF, page count 223, and the December 2022 fourth-generation sentence on the introduction page. Scan the cover and front matter for a contractor copyright notice; stop if any line reserves copyright to a contractor. Record date, byte size, page count, and the absence of a report number in `PACK.yaml` `notes` — the D2 sentence is the authoritative notes manifest; do not keep a second list. Stop if D2 fails.
2. Extract the contents list. Freeze 6 to 8 chapter titles from the numbered top-level sections. Discard the provisional map where the PDF disagrees.
3. Write `packs/fhwa-its-se/` per PACK-SPEC. `LICENSE` states US Government work under 17 U.S.C. § 105, no attribution duty, courtesy attribution only, no FHWA endorsement, reconstructed-notes statement, and a named-not-quoted section for INCOSE, ISO/IEC/IEEE 15288, and other third-party standards. Model it on `packs/faa-8110-49/LICENSE`: no download URL, source identified by title, publisher, and December 2022 only. No URL in `SKILL.md` or `PACK.yaml`. The `NOTICE` entry follows the `packs/faa-8110-49` block shape (one `[pack: fhwa-its-se]` block, public-domain wording, no OGL deed lines).
4. Register on every D6 surface. Hand-edit rules and overrides. Regenerate the map and the HTML. Do not hand-edit generated JSON or HTML.
5. Resolve b-32 as D7 states.
6. Run the gates in Testing. Fix only this pack's findings.

PDF contents list, from the 2026-10-27 extract. Provisional chapters — this table is a grouping aid only; D5's contents-list rule wins wherever they disagree:

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

`PACK.yaml` field values once vet passes:

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
```

`build.chapters` must equal the chapter file count. `build.built_on` is the execution date. `build.method` states synthesized from the pinned PDF, not adapted from a sibling prototype. `change_indication: "reconstructed as synthesized reference notes"`. `notes` carries the statute line, the vet date, byte size, page count, no-report-number finding, no FHWA endorsement, and the named-not-quoted list.

`SKILL.md` frontmatter `name` is `fhwa-its-se`. Description states ITS systems engineering for transportation agencies and the limits in D4. Body order matches PACK-SPEC: `## When to use`, then a `**Prerequisites:**` line, `## How to use this skill`, core frameworks drawn only from the PDF, chapter index, topic index, supporting files, scope and limits. No source URL in the skill body.

`glossary.md`: terms the document defines, alphabetical, with the chapter that uses each. `cheatsheet.md`: decision rules and tailoring or procurement tables, described, not copied as page images.

Cluster assignment for each chapter uses a name already in `docs/classification-rules.json` `cluster_names`. Likely fits: Standards, Tailoring & Process Models; Requirements Engineering; Verification; Validation; Governance, Reviews, Gates & Control Points; Supplier, Procurement & Acquisition; Operations, Maintenance & Disposal. Do not invent a cluster. Each override note is one sentence, no em dash, and says the note is from Systems Engineering for ITS, December 2022. `glossary.md` and `cheatsheet.md` get no assignment or note rows; one assignment per chapter file only.

`catalog.json` live row mirrors the `faa-8110-49` row keys exactly, in order: `slug`, `title`, `publisher`, `source_version`, `license`, `license_tier`, `commercial_use`, `chapters`, `status` (`live`). Insert after the last civil-infrastructure or alphabetical neighbour as the surrounding rows dictate; `updated` stays `2026-10-14`.

`docs/source-watchlist.json`: hand-add the full `sources[]` object before running `--record` (the tool rewrites an existing slug, it does not create one). Keys in order: `slug`, `publisher`, `document`, `version` (identical to the catalog `source_version`), `last_checked` (execution date), `hint` (`""`). No URL in any value.

`/se` changes:

- Add a Topics row `Civil infrastructure & ITS` with keywords intelligent transportation, ITS, systems engineering analysis, 23 CFR 940, ConOps, and pack list `fhwa-its-se` only (one pack, inside the at-most-six cap).
- Add an Agency row `FHWA / USDOT ITS` with keywords FHWA, ITS, systems engineering analysis, and pack `fhwa-its-se`. Leave the existing `NHTSA / USDOT` row on `nhtsa-vehicle`. Do not merge them.
- No Licences row for this pack. Public Domain packs are exempt from the Licences table, and the routing-map check errors on an extra row.
- Do not put `fhwa-its-se` on the CISA / DHS row. Critical infrastructure performance goals are a different source.

`docs/candidate-packs.md`: insert build-order row 9, `fhwa-its-se`, kind full, status built on the execution date, why-first cell states tier-1 civil infrastructure and the December 2022 pin. Update the sentence that says the remaining full-pack work is only the unfinished uk-defence family, so it no longer hides this pack. Mark the proposed-pack bullet built. Update the catalogue-count sentence from 81 / 72 to 82 / 73 if that sentence is still the live count. No other candidate row changes.

`docs/superpowers/backlog.md`: b-32 status `promoted` becomes `done`. Evidence cell gains the execution date and the row-9 pointer. Do not delete the row.

Plugin skills arrays: `.claude-plugin/plugin.json` gains `"./packs/fhwa-its-se"`; `.cursor-plugin/plugin.json` gains `"./packs/fhwa-its-se/SKILL.md"` (per-file literal, matching existing cursor entries). Keep JSON valid. Both plugin files.

Count sentences that must move with the pack: `SKILLS.md` "72 packs", `README.md` packs badge and catalogue table row, `docs/index.html` "72 packs" h2, "81 skills" sentence, and the section-06 chip count labels (chip sum must equal 73), `docs/assets/still-catalogue.svg` subtitle and footer (both "72 packs"), `docs/products/website/01-jgs-se-knowledge-packs.yaml` "72 packs" claim, `docs/candidate-packs.md` catalogue-count sentence (81/72 becomes 82/73). Signpost count stays 8. Orchestrator stays 1. New totals: 73 content packs, 82 skills.

## Scope

In:

- Live re-fetch of the December 2022 PDF before prose.
- `packs/fhwa-its-se/` per PACK-SPEC, 6 to 8 chapters, glossary, cheatsheet.
- Registration on every surface in Codebase context.
- b-32 resolution and build-order row 9.
- Count sentence updates from 72/81 to 73/82.

Out:

- November 2009 SEGB, FHWA-OP-02-046, FHWA-HOP device model documents, Caltrans Local Assistance SE handbook, FEMA publications, construction specifications.
- Changes to `jsp-936`, `nhtsa-vehicle`, `cisa-cpg`, or any other pack's chapter prose.
- New validators, new page templates, new licence tiers.
- Quoting INCOSE, ISO, IEEE, SAE, or NTCIP clause text, or embedding PDF page images.
- `source_url` in `PACK.yaml` or `catalog.json`.
- Ranking or building `telecom-3gpp` or any other candidate.
- GitHub release, plugin publish, or commit. This spec does not authorize those.

## Testing

All must pass before the cut is done:

1. `python tooling/validate_pack.py packs/fhwa-its-se` exits 0.
2. `python tooling/check_source_watch.py --record fhwa-its-se "<version string matching PACK.yaml source_version>" <YYYY-MM-DD of the vet>` then `python tooling/check_source_watch.py` exits 0. Record only after the catalog live row exists. Coverage checks the live catalog against the watchlist in both directions.
3. `python tooling/generate_capability_map.py --generated-on <YYYY-MM-DD> --sync-md` then `python tooling/check_capability_map.py` exits 0. Override row count must match rules row count after the new chapters. On mismatch, fix the paired rows. Do not edit the generator.
4. `python tooling/gen_pack_pages.py --only fhwa-its-se` and `python tooling/gen_packs_page.py` exit 0. `docs/packs/fhwa-its-se/index.html` exists. `docs/sitemap.xml` contains the fhwa-its-se URL.
5. Search the repo for `fhwa-its-se` on the D6 surfaces and confirm each names the pack. Search `packs/fhwa-its-se` for `http://` and `https://` and confirm URLs appear only in `LICENSE`, or nowhere if D2's sibling rule omitted them.
6. `python tooling/check_pack_quality.py` on the new pack if the script accepts a path. If it is catalog-wide only, run it once and fix only fhwa-its-se findings.
7. `python tooling/check_release.py` exits 0. Fix only findings this pack introduced.
8. `python ~/.zcode/scripts/prose_check.py` on the new pack's prose files and on this spec if it was edited during execution. Zero em dashes in headings and body prose.

Map total after the cut is 728 plus the chapter count. Content-pack count is 73. Skill count is 82.

## Non-goals

- Do not treat the 2026-10-27 fetch as a substitute for the execution-time re-fetch. The vet in step 1 is mandatory.
- Do not add a second primary source to raise chapter count. One PDF.
- Do not widen `/se` into a general civil-engineering or construction router.
- Do not republish the PDF. Do not add a `sources/` tree for this pack. `tooling/check_release.py` fails tracked extracts.
- Do not bump `RELEASE-INFO`, either plugin `version`, or `catalog.json` `updated`.
- Do not edit neighbor pack prose to "make room" in a six-pack topic row. This pack gets its own row.

## Do not

- Do not bump `RELEASE-INFO`.
- Do not edit neighbor packs' chapter files.
- Do not commit anything under `sources/`.
- Do not bump plugin `version` or any release version file.
- Do not change `catalog.json` `updated`. It stays `2026-10-14`.
