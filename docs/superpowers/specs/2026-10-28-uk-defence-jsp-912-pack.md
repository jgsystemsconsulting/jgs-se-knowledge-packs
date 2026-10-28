# uk-defence-jsp-912-pack

Package P57. Build `packs/jsp-912` from JSP 912 Parts 1 and 2 (one pack, two PDFs) and register it on every live surface `jsp-936` already uses. Family already ships `jsp-815`, `jsp-376`, and `jsp-936`. This cut finishes the next ranked member. It does not design a new family.

## Research

Live pin, fetched 2026-10-28. Publication page HTTP 200. Both PDFs HTTP 200, `%PDF-1.7`.

- Publication page: https://www.gov.uk/government/publications/human-factors-integration-in-defence-systems-jsp-912
- Page title: Human Factors Integration in defence systems (JSP 912)
- Publisher: Ministry of Defence
- Published: 3 February 2014
- Last updated: 3 May 2024. Update note: "Updated: JSP 912: Human Factors Integration in defence systems, Parts 1 and 2."
- Short description: "This Joint Service Publication defines MOD policy regarding the process of Human Factors Integration (HFI) in defence systems."
- OGL deed: https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- Page footer, verbatim sense: "All content is available under the Open Government Licence v3.0, except where otherwise stated" and "© Crown copyright". No withdrawn notice. No login wall.

Attachments on that page, both free:

| Part | Link text | URL | Page size | Observed bytes | PDF pages | Cover |
|---|---|---|---|---|---|---|
| 1 | JSP 912: Human Factors Integration in defence systems (Part 1: directive). Ref: JSP 912 Part 1 | https://assets.publishing.service.gov.uk/media/6634dc9ccf3b5081b14f314b/JSP_912_Part_1_V3.0.pdf | 353 KB, 16 pages | 360,991 | 16 | JSP 912, Human Factors Integration for Defence Systems, Part 1: Directive, Version 3.0 Mar 2024. Running footer `JSP 912 Pt 1 (V3.0 Mar 24)`. Cover also carries a stale "Version 3.0 Oct 2021" line under the Mar 2024 line. Body footer and filename say Mar 2024. Pin Mar 2024. |
| 2 | JSP 912: Human Factors Integration in defence systems (Part 2: guidance) | https://assets.publishing.service.gov.uk/media/6634dcae1834d96a0aa6d0da/JSP_912_Part_2_V3.0.pdf | 1.27 MB, 65 pages | 1,326,830 | 65 | JSP 912 Part 2, Version 3.0 Mar 2024. Running footer `JSP 912 Pt 2 (V3.0 Mar 24)`. |

Neither PDF body states an Open Government Licence exception, a Crown carve-out, or an all-rights-reserved line. "Reproduced" appears only as ordinary prose, not as a licence restriction. Third-party standards and other JSPs are named. They are not the licence of this publication.

2026-10-14 research gate row (https://www.gov.uk/government/publications/human-factors-integration-in-defence-systems-jsp-912, V3.0 Mar 2024, page last updated 3 May 2024, two free PDFs about 16 and 65 pages, OGL v3 footer) still matches the live page. Page has not moved. Versions have not changed. Byte sizes above replace the gate's "about" figures.

Rank context from that gate, line 79: after JSP 376 and JSP 936 Part 1, JSP 912 Parts 1 and 2 is the next family member. JSP 940, JSP 945, JSP 816, JSP 375, and JSP 520 stay later work.

## Codebase context

Pattern precedent is `packs/jsp-936/` for registration and OGL text. No sibling ships two PDFs: `jsp-815` is a single-PDF pack (Framework plus Annex H in one document), so this cut defines the two-PDF convention itself. `jsp-936` being single-PDF is not a limit to copy. Required content-pack layout is `docs/PACK-SPEC.md`: `SKILL.md`, `PACK.yaml`, `LICENSE`, `chapters/` with at least one chapter. Glossary and cheatsheet are optional. Both OGL siblings ship them, so this pack ships them too.

Licence class is tier 2, same as `jsp-815`, `jsp-376`, and `jsp-936`. Not tier 1. `license_tier: 2`, `attribution_required: true`. Full OGL v3.0 text goes in `packs/jsp-912/LICENSE`.

Live counts before this cut, read 2026-10-28 on main after 1.23.0: `catalog.json` `packs` 73, `docs/source-watchlist.json` `sources` 73, `docs/classification-rules.json` assignments 735, `docs/capability-pack-map-note-overrides.json` notes 735. Catalogue prose says 82 skills (73 content, 8 signposts, 1 orchestrator). `SKILLS.md` line 9 says "73 packs (+8 signposts, +1 orchestrator)". Adding one content pack moves those to 74 content packs, 83 skills, and 735 plus the new chapter count on the map. Signposts stay 8. Orchestrator stays 1.

`tooling/generate_capability_map.py` hardcodes `735` (module docstring and the notes-length check near line 195). That literal must move with the new chapter count. `tooling/check_classification_rules.py` and `tooling/check_capability_map.py` do not hardcode 735.

Registration surfaces that already name `jsp-936` and must name `jsp-912`:

- `catalog.json` live row. Nine keys, same order as the `jsp-936` row: `slug`, `title`, `publisher`, `source_version`, `license`, `license_tier`, `commercial_use`, `chapters`, `status`. Do not change top-level `updated`. It stays `2026-10-14`.
- `docs/source-watchlist.json` full `sources[]` object, hand-added, then `--record`.
- `SKILLS.md` row and the opening count line.
- `packs/se/SKILL.md` Defence safety management row (line 118) and the Licences table (line 161). OGL packs are required rows. Public-domain exemption does not apply.
- `NOTICE` one `[pack: jsp-912]` block, same shape as `[pack: jsp-936]`.
- `.claude-plugin/plugin.json` skills array (`"./packs/jsp-912"`). `.cursor-plugin/plugin.json` skills array (`"./packs/jsp-912/SKILL.md"`). Do not bump either `version`.
- `README.md` packs badge (`packs-73`) and the catalogue table row.
- `docs/index.html` §06 h2, the "82 skills" sentence, and the `UK · 3` chip.
- `docs/assets/still-catalogue.svg` subtitle and footer.
- `docs/products/website/01-jgs-se-knowledge-packs.yaml` "73 packs" claim and the `UK MOD (3)` sentence.
- `docs/classification-rules.json` and `docs/capability-pack-map-note-overrides.json`, hand-added, one pair per chapter. Then regenerate. Do not hand-edit `docs/capability-pack-map.json` or `docs/capability-pack-map.md`.
- `docs/packs/jsp-912/index.html` via `tooling/gen_pack_pages.py --only jsp-912` (rewrites `docs/sitemap.xml` from the full live catalog).
- `docs/packs.html` via `tooling/gen_packs_page.py`.
- `CHANGELOG.md` one Unreleased bullet. No version bump. Do not edit the `[1.23.0]` section.
- `docs/candidate-packs.md` row 4 and the unranked-remainder sentence.
- `docs/superpowers/backlog.md` b-41 status cell only.

No `source_url` in `PACK.yaml` or `catalog.json`. Source and licence URLs live only in `packs/jsp-912/LICENSE`. Same rule as `docs/PACK-SPEC.md`.

`tooling/check_release.py` check 15 (`[routing-map]`) requires a Licences row for every non-Public-Domain content pack, and requires every backticked slug in a pack cell to resolve to `packs/<slug>/SKILL.md`. The Defence topic row is already at six packs if you count wrong: it currently lists three (`jsp-815`, `jsp-376`, `jsp-936`). Adding `jsp-912` makes four. That is inside the at-most-six cap. Do not open a second Defence row to "make room".

## Decision register

- D1: Source pin is JSP 912 Parts 1 and 2, both Version 3.0 March 2024, one pack. Part 1 Directive (16 pages, 360,991 bytes) and Part 2 Guidance (65 pages, 1,326,830 bytes). URLs in Research. Do not drop Part 2. Do not split into two packs. Two-PDF convention (defined here; no in-repo precedent): every chapter title carries its part, `SKILL.md`'s chapter index keeps a strict Part-1 block before the Part-2 block, and `PACK.yaml` `source_version` names both parts with their shared V3.0 (March 2024). The stale "Version 3.0 Oct 2021" line on the Part 1 cover is not the pin.
- D2: Licence class is Open Government Licence v3.0, `license_tier: 2`, `commercial_use: true`, `share_alike: false`, `attribution_required: true`, matching `jsp-936`. Execution must re-fetch the publication page and both PDFs before any chapter prose. Record vet date, both byte sizes, both page counts, and the exception-scan result in `PACK.yaml` `notes`. Stop if the page footer no longer states Open Government Licence v3.0, if either PDF URL is dead, or if either PDF states an exception that removes the reuse grant from the body.
- D3: One pack, two parts, same shape as `jsp-815` (one slug, several source files, one `LICENSE`). Chapter files are not split by part label. A chapter may draw from Part 1, Part 2, or both. `SKILL.md` must say which part a claim comes from.
- D4: Reconstruction rule copies `jsp-936`. Synthesized reference notes. Short defined terms may be kept. No long verbatim passages. Name JSP 375, JSP 536, JSP 815, JSP 822, DEF-STANs, and third-party standards. Do not quote their text. Do not embed PDF figures. HuFIMS and Defence Learning Environment URLs in the preface are out of scope. Do not reproduce those URLs in chapter prose.
- D5: Position is HFI for Defence acquisition, the human component of capability. Companion to `jsp-815` and `jsp-376`, not a second SMS and not a second acquisition-safety policy. `SKILL.md` scope limits name those siblings and state they are not reproduced.
- D6: Chapter count is 6 to 10, files `chapters/chNN-<slug>.md`. Contents lists of both PDFs win over the provisional table in Approach. If a provisional theme is absent from both contents lists, do not write that chapter. If the lists force a merge to stay inside 10, merge. Do not exceed 10 files. Do not go under 6.
- D7: Full registration on every surface in Codebase context. Partial registration is the miss this package exists to avoid. `docs/candidate-packs.md` changes only row 4, the unranked-remainder sentence, and the `uk-defence-*` proposed-pack bullet.
- D8: b-41 closes on the 912 side only. Status becomes `done` for the 912 promotion. The evidence cell must say 940, 945, 816, 375, and 520 stay needs-info. Do not mark those built. Do not delete the row.
- D9: No new tooling, except the one-line `735` literal in `tooling/generate_capability_map.py`, which must become `735 + N` where N is the chapter count. Do not bump `RELEASE-INFO.txt`, either plugin `version`, or `catalog.json` `updated`.

## Problem

Build-order row 4 (`docs/candidate-packs.md`) is still partial. `jsp-815`, `jsp-376`, and `jsp-936` are live. `packs/jsp-912` is absent. The unranked-remainder sentence on that page still names JSP 912 as if the 2026-10-14 gate had not already ranked it. `/se` Defence routing and the Licences table name only the three shipped JSPs. Shipping the folder without the registration surfaces leaves a CI-green pack the orchestrator and the indexes do not route. Shipping without a fresh per-document OGL check repeats the licence miss the family rule already forbids.

## Approach

Copy the `jsp-936` cut for registration and OGL text. Copy the `jsp-815` cut for source shape: two PDFs, one slug. Reconstructed notes in chapters, then the same generators.

Execution order:

1. Vet. Re-fetch the publication page and both PDF URLs in Research. Confirm publisher (Ministry of Defence), version (V3.0 Mar 2024) on both covers or running footers, page counts (16 and 65), free download, and the OGL v3.0 plus Crown copyright footer. Scan both PDFs for a stated licence exception that would carve the body out of OGL. Record date, both byte sizes, both page counts, and the exception-scan result in `PACK.yaml` `notes`. Stop if D2 fails.
2. Extract both contents lists. Freeze 6 to 10 chapter titles from those lists. Discard the provisional map wherever it disagrees with either PDF.
3. Write `packs/jsp-912/` per PACK-SPEC. Copy `packs/jsp-936/LICENSE` structure: attribution statement `Contains public sector information licensed under the Open Government Licence v3.0.`, source identification for both parts, both publication facts, the publication URL, the deed URL, a reconstructed-notes statement, non-endorsement, and an excluded-material section (other JSPs and third-party standards named, not quoted).
4. Register on every D7 surface. Hand-edit rules and overrides. Bump the generator `735` literal to `735 + N`. Regenerate the map and the HTML. Do not hand-edit generated JSON or HTML.
5. Resolve b-41 as D8 states.
6. Run the gates in Testing. Fix only this pack's findings.

Provisional chapters. Grouping aid only. D6 wins wherever the PDFs disagree.

Part 1 contents (Directive, 16 pages): 1 Introduction (Policy, Scope, Applicability, Associated Standards and Guidance); 2 MOD HFI Process (Goals, Activities, Tailoring); 3 MOD Staff Responsibilities (Project Team Leader, HFI Focus, Requirements Management, Capability Sponsor, Capability Integration Working Group, HFI Support Function); 4 HFI Resource Competencies; 5 References; 6 Acronyms and Abbreviations.

Part 2 contents (Guidance, 65 pages): 1 Introduction to HFI (What is HFI, Human Component of Capability, HFI Domains, HFI and Systems Engineering, HFI and Defence Lines of Development); 2 Overview of the HFI Process (Goals, Activities, System Readiness Levels); 3 HFI Process: Stages and Core Activities (HFI-1.0 User Need Definition, HFI-2.0 System Requirements Definition, HFI-3.0 Assess Tenders, HFI-4.0 Detailed System Design, HFI-5.0 Test and Acceptance, HFI-6.0 In-Service Feedback); 4 Tailoring the Process; 5 Roles and Responsibilities; 6 HFI Resource Competencies; 7 References; 8 Acronyms and Abbreviations; 9 Glossary.

| Ch | Working title | Drawn from |
|---|---|---|
| 01 | What HFI is and why Defence mandates it | Part 1 §1 and Part 2 §1. Policy, scope, applicability, human component of capability, HFI domains. |
| 02 | HFI and systems engineering | Part 2 §1 (HFI and Systems Engineering, Defence Lines of Development) and Part 2 §2 (System Readiness Levels). |
| 03 | HFI process goals, activities, tailoring | Part 1 §2 and Part 2 §2 and §4. One chapter, not three. |
| 04 | User need and system requirements (HFI-1.0, HFI-2.0) | Part 2 §3. |
| 05 | Tenders and detailed design (HFI-3.0, HFI-4.0) | Part 2 §3. |
| 06 | Test, acceptance, in-service feedback (HFI-5.0, HFI-6.0) | Part 2 §3. |
| 07 | Roles and responsibilities | Part 1 §3 and Part 2 §5. Six named roles. Do not invent a seventh. |
| 08 | Competencies, ethics, conduct | Part 1 §4 and Part 2 §6. Research ethics and conduct stay named, not quoted from JSP 536. |

References, acronym lists, and the Part 2 glossary do not become chapters. Fold defined terms into `glossary.md`. If HFI-4.0 is too large for one chapter with HFI-3.0, split chapter 05 into two and drop nothing else: that is 9, still inside D6. If a contents heading above is absent on the execution-time extract, delete that chapter and merge its neighbour. Do not write a chapter neither contents list contains.

`PACK.yaml` field values once vet passes:

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
```

`build.chapters` must equal the chapter file count. `build.built_on` is the execution date. `build.method` states synthesized from the two pinned PDFs, not adapted from a sibling prototype. `change_indication: "reconstructed as synthesized reference notes"`. `notes` carries the OGL attribution line, Crown copyright, no MOD endorsement, vet date, both byte sizes, both page counts, the exception-scan result, and the named-not-quoted list (JSP 375, JSP 536, JSP 815, JSP 822, third-party standards).

`SKILL.md` frontmatter `name` is `jsp-912`. Description states HFI in Defence acquisition and the limits in D5. Body order matches PACK-SPEC: `## When to use`, then a `**Prerequisites:**` line, `## How to use this skill`, core frameworks drawn only from the two PDFs, chapter index, topic index, supporting files, scope and limits. No source URL in the skill body. A `**Source:**` line may name the OGL attribution statement and Crown copyright, as `jsp-815` does, and must point at `LICENSE` for the URLs.

`glossary.md`: terms either PDF defines, alphabetical, with the chapter that uses each. `cheatsheet.md`: the six HFI stage gates and the six roles, described, not copied as page images.

Cluster assignment for each chapter uses a name already in `docs/classification-rules.json` `cluster_names`. Likely fits: Human Systems Integration; Requirements Engineering; Supplier, Procurement & Acquisition; Verification; Validation; Governance, Reviews, Gates & Control Points; Standards, Tailoring & Process Models. Do not invent a cluster. If "Human Systems Integration" is not in `cluster_names`, use the nearest existing name and say so in the override note. Each override note is one sentence, no em dash, and says the note is from JSP 912 V3.0 March 2024. One assignment and one note per chapter file. `glossary.md` and `cheatsheet.md` get no rows.

`/se` changes, and only these:

- Defence safety management row (currently `jsp-815`, `jsp-376`, `jsp-936`): add `jsp-912` to the pack cell. Add keywords human factors, HFI, human component of capability. Do not remove existing safety keywords. Do not create a second Defence row. Four packs, inside the six-pack cap.
- Licences table: add a row `` `jsp-912` | Open Government Licence v3.0 ``. OGL packs are required rows. Omitting it fails `[routing-map]`.
- AI and cyber-physical row stays on `jsp-936`. Do not add `jsp-912` there. HFI is not dependable-AI policy.

`docs/candidate-packs.md`: row 4 status text gains jsp-912 built on the execution date and keeps other JSPs and DEF-STANs pending. The unranked-remainder sentence drops JSP 912 and keeps JSP 940 and DEF-STANs. The `uk-defence-*` proposed-pack bullet gains the same built mark. No other candidate row changes.

`docs/superpowers/backlog.md`: b-41 status `promoted` becomes `done`. Evidence cell gains the execution date and states that 940, 945, 816, 375, and 520 remain needs-info. Do not delete the row.

Plugin skills arrays: `.claude-plugin/plugin.json` gains `"./packs/jsp-912"`; `.cursor-plugin/plugin.json` gains `"./packs/jsp-912/SKILL.md"`. Keep JSON valid. Do not change either `version` field. Cursor stays 1.22.0. That gap is P60, not this cut.

Count sentences that must move with the pack, from the post-1.23.0 baseline (73 / 82 / 735), not from the older jsp-936 spec (72 / 81 / 728):

- `SKILLS.md` line 9: "73 packs" becomes "74 packs".
- `README.md` badge `packs-73` becomes `packs-74`, and the catalogue table gains the jsp-912 row.
- `docs/index.html` §06 h2 "73 packs" becomes "74 packs". The skills sentence "82 skills" / "73 knowledge packs" becomes "83 skills" / "74 knowledge packs". The `UK · 3` chip becomes `UK · 4` and names JSP 912. Chip sum must equal 74. Signposts chip stays 8. Orchestrator chip stays 1 and is exempt from the content sum.
- `docs/assets/still-catalogue.svg` subtitle and footer: both "73 packs" become "74 packs". Signpost figure stays 8.
- `docs/products/website/01-jgs-se-knowledge-packs.yaml`: "73 packs across the SE catalogue" becomes "74 packs". `UK MOD (3)` becomes `UK MOD (4)` and names JSP 912. Do not renumber NASA, DoD, NIST, FAA, or other family counts.
- `docs/candidate-packs.md` catalogue-count sentence, if it still says 82 packs / 73 content packs, becomes 83 / 74.
- `tooling/generate_capability_map.py`: both `735` literals become `735 + N`.

New totals: 74 content packs, 83 skills, 735 + N map rows. Signposts 8. Orchestrator 1.

`catalog.json` `updated` stays `2026-10-14`. `RELEASE-INFO.txt` stays 1.23.0. Both plugin `version` fields stay as they are.

## Scope

In:

- Live OGL v3 re-fetch of the publication page and both PDFs before prose.
- `packs/jsp-912/` per PACK-SPEC, 6 to 10 chapters, glossary, cheatsheet.
- Registration on every surface in Codebase context.
- The `735` literal bump in `tooling/generate_capability_map.py`.
- b-41 closed on the 912 side only.
- Count sentence updates from 73/82 to 74/83.

Out:

- JSP 940, JSP 945, JSP 816, JSP 375, JSP 520, JSP 939, JSP 600, and any DEF-STAN.
- Changes to `jsp-815`, `jsp-376`, or `jsp-936` chapter prose.
- A second pack for Part 2, or a Part-1-only pack.
- New validators, new page templates, new licence tiers.
- Quoting JSP 375, JSP 536, JSP 815, JSP 822, or third-party standard text. Embedding PDF page images.
- `source_url` in `PACK.yaml` or `catalog.json`.
- GitHub release, plugin publish, or commit. This spec does not authorize those.

## Testing

All must pass before the cut is done:

1. `python tooling/validate_pack.py packs/jsp-912` exits 0.
2. `python tooling/check_source_watch.py --record jsp-912 "<version string matching PACK.yaml source_version>" <YYYY-MM-DD of the vet>` then `python tooling/check_source_watch.py` exits 0. Hand-add the watchlist object first. `--record` rewrites an existing slug. It does not create one. Record only after the catalog live row exists.
3. `python tooling/generate_capability_map.py --generated-on <YYYY-MM-DD> --sync-md` then `python tooling/check_capability_map.py` exits 0. Override row count must match rules row count after the new chapters. On mismatch, fix the paired rows. Do not edit the generator except the `735` literal D9 names.
4. `python tooling/gen_pack_pages.py --only jsp-912` and `python tooling/gen_packs_page.py` exit 0. `docs/packs/jsp-912/index.html` exists. `docs/sitemap.xml` contains the jsp-912 URL.
5. Search the repo for `jsp-912` on the D7 surfaces and confirm each names the pack. Search `packs/jsp-912` for `http://` and `https://` and confirm URLs appear only in `LICENSE`.
6. `python tooling/check_pack_quality.py` on the new pack if the script accepts a path. If it is catalog-wide only, run it once and fix only jsp-912 findings.
7. `python tooling/check_release.py` exits 0. Fix only findings this pack introduced. `[routing-map]` must see the Licences row. `[catalogue-count]` must see 74 and chip sum 74.
8. `python ~/.zcode/scripts/prose_check.py` on the new pack's prose files. Zero em dashes in headings and body prose.

Map total after the cut is 735 plus the chapter count. Content-pack count is 74. Skill count is 83.

## Non-goals

- Do not treat the 2026-10-28 fetch in Research as a substitute for the execution-time re-fetch. Step 1 is mandatory.
- Do not add a third PDF to raise chapter count.
- Do not widen `/se` into a general human-factors or occupational-health router. `nasa-hsi` and `faa-hf-std` stay non-Defence HSI routes.
- Do not republish either PDF. Do not add a `sources/` tree. `tooling/check_release.py` fails tracked extracts.
- Do not bump `RELEASE-INFO.txt`, either plugin `version`, or `catalog.json` `updated`.
- Do not edit neighbour pack prose to make room on the Defence row. Four packs fit.

## Do not

- Do not build if the gov.uk footer no longer says Open Government Licence v3.0.
- Do not build if either PDF URL returns non-200, or the body is not a PDF, or the running footer is not V3.0 Mar 2024.
- Do not build if either PDF carves its body out of the OGL reuse grant.
- Do not ship Part 1 without Part 2.
- Do not bump `RELEASE-INFO.txt`.
- Do not bump plugin `version` or any release version file.
- Do not change `catalog.json` `updated`. It stays `2026-10-14`.
- Do not edit neighbour packs' chapter files.
- Do not commit anything under `sources/`.
- Do not mark JSP 940, JSP 945, JSP 816, JSP 375, or JSP 520 built.
- Do not hand-edit `docs/capability-pack-map.json`, `docs/capability-pack-map.md`, `docs/packs.html`, or `docs/sitemap.xml`. Generators own those files.
