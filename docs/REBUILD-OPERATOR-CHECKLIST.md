# Edition rebuild operator checklist

Use this when rebuilding an existing live pack onto a new source edition (not when adding a new slug). Add-new registration stays in [CONTRIBUTING.md](../CONTRIBUTING.md). Source-watch policy stays in [SOURCE-FRESHNESS.md](SOURCE-FRESHNESS.md). This file is tracked on purpose: rebuild plans under `docs/superpowers/` are gitignored and do not ship operator guidance.

A rebuild is a maintainer decision. The monthly watch records drift; it never edits pack content.

## Before you start

1. Confirm the target edition from the publisher page (not a secondary mirror alone).
2. Note the current pack pin: `packs/<slug>/PACK.yaml` `source_version`, `build.chapters`, `build.method`.
3. Confirm commercial/licence tier still matches [SOURCE-VETTING.md](SOURCE-VETTING.md).

## Pack body

1. Rebuild chapters to the publisher contents list (PACK-SPEC: contents list wins; multi-PDF pin every part).
2. Refresh glossary / patterns / cheatsheet / `SKILL.md` index as needed.
3. Update `packs/<slug>/PACK.yaml`: `source_version`, chapter count, `built_on`, build notes. Keep method on the canonical string (`synthesized reference notes from the pinned source, chapter freeze from the contents list`).
4. Update `packs/<slug>/LICENSE` if source terms or edition name changed.
5. Run `python tooling/validate_pack.py packs/<slug>`.

## Registration twins (live catalog pack)

Hand-edit; no writer exists for these rows.

1. `catalog.json` — matching pack object: `source_version`, `chapters`, licence fields.
2. `SKILLS.md` — table row title/edition text if it names the edition.
3. `packs/se/SKILL.md` — Topics / Agency / Licences rows if they name this pack or edition.
4. Plugin skill lists if the path changed (rare on rebuild): `.claude-plugin/plugin.json`, `.cursor-plugin/plugin.json`.

## Source watch

1. After the pin is correct:  
   `python tooling/check_source_watch.py --record <slug> "<observed_version>" <YYYY-MM-DD>`
2. Do not invent a watchlist row on rebuild (row already exists for live catalog packs).
3. Run `python tooling/check_source_watch.py` and keep it green.

## Capability map and notes

1. If chapter titles or membership changed, edit **only**  
   `docs/capability-pack-map-note-overrides.json`  
   Never hand-edit `docs/capability-pack-map.json`.
2. Notes-length gate: `tooling/generate_capability_map.py` asserts  
   `len(notes) == (743 - 6 + 8)` at the literal sites (search `743 - 6 + 8` in that file).  
   If a rebuild removes or adds note-bearing chapters, update **every** site of that constant in the same change (or wait for the NOTES_COUNT single-source package). Miss one site and map generation fails closed.
3. Regenerate:  
   `python tooling/generate_capability_map.py --generated-on YYYY-MM-DD --sync-md`  
   then `python tooling/check_capability_map.py`.

## Website and pack pages

1. Free-text edition chips on `docs/index.html` and product YAMLs under `docs/products/website/` if they name this pack's edition (example miss: landing chip said 516C while PACK.yaml was 516D).
2. Regenerate pack pages:  
   `python tooling/gen_pack_pages.py --only <slug>`  
   (omit `--only` only when you intend a full fleet regen).
3. `python tooling/gen_packs_page.py` if the packs index row should show the new rev.
4. Spot-check the pack page REV and the landing chip in a browser before cut.

## Release surfaces (when the rebuild ships in a release)

1. `CHANGELOG.md` Unreleased: Fixed/Changed bullets for the rebuild.
2. Root `NOTICE` only if attribution text must change.
3. Do not restamp version tokens until the release cut package runs.

## Gate before stop

```bash
python tooling/validate_pack.py packs/<slug>
python tooling/check_source_watch.py
python tooling/check_capability_map.py
python tooling/check_release.py
```

All four must exit 0 on a clean tree (aside from intentional Unreleased edits awaiting cut).

## Explicit miss hazards

| Miss | Symptom |
|------|---------|
| note-overrides not updated | wrong or missing map notes for rebuilt chapters |
| only one notes-length literal updated | `generate_capability_map.py` fail-closed |
| website chip left on old edition | public contradiction vs PACK.yaml |
| watch `--record` skipped | release gate source-watch stale / wrong version |
| `capability-pack-map.json` hand-edited | next generate overwrites or check fails |
| pack pages not regenerated | stale REV on docs/packs/&lt;slug&gt;/ |

## Out of this checklist

- New-slug registration (CONTRIBUTING).
- Monthly watch cron census (automation derives N/W from the watchlist file).
- Release cut numbering (CHANGELOG Unreleased drain).
