<!--
Copyright (c) 2026 JG Systems Consulting Ltd. MIT License (see LICENSE).
SPDX-License-Identifier: MIT
-->

# Contributing

Thanks for helping grow the catalogue. The bar for a pack is **quality + provenance**:
faithful to its source, and legally redistributable.

The catalogue ships three member kinds: **content packs** (reconstructed reference notes
from one vetted source), **signposts** (citation-only maps of sources that cannot be
packaged), and the **`se` orchestrator** (routes `/se <question>` to packs; no source
content). This guide is about adding a content pack; see docs/PACK-SPEC.md for the
member kinds.

## Before you build: vet the source

This is the non-negotiable first step. Read [docs/SOURCE-VETTING.md](docs/SOURCE-VETTING.md)
and confirm:

1. The source is **Tier 1 (public domain)** or **Tier 2 (open licence)**, or Tier 3 with
   a written justification.
2. The source is **not** on the Excluded list (ISO/IEC/IEEE, SWEBOK, MITRE SE Guide,
   INCOSE Handbook, TOGAF, PMBOK, …).
3. You found the licence **in the source itself**, not a third-party summary.

If a source is merely "free to download," that is not enough. Free ≠ redistributable.

Source freshness is checked monthly against the revision each live pack was built
from; see [docs/SOURCE-FRESHNESS.md](docs/SOURCE-FRESHNESS.md). A rebuild stays a
maintainer decision, made from that report.

## Build the pack

```bash
# 1. Scaffold with provenance (forces a tier + licence on record):
python tooling/build_pack.py --slug <slug> --title "..." --publisher "..." \
    --version "..." --url "..." --license "..." --tier <1|2|3> --commercial-use <true|false>

# 2. Generate content per docs/PACK-SPEC.md:
#    - extract text (jgs-reference-skill), map chapter offsets, generate reference-depth
#      chapters + glossary/patterns/cheatsheet, then the SKILL.md index.
# 3. Fill the TODOs in packs/<slug>/PACK.yaml and packs/<slug>/LICENSE.
# 4. Register a live catalog pack (any kind other than signpost or
#    orchestrator). Hand-edit each surface. No writer exists for
#    catalog.json or SKILLS.md. Gates fail a bad row.
#    - catalog.json: add one object to "packs" with the same keys as an
#      existing row (slug, title, publisher, source_version, license,
#      license_tier, commercial_use, chapters, status). status is "live".
#    - SKILLS.md: add one table row. The file is hand-maintained.
#      Then: python tooling/gen_packs_page.py
#      (rewrites docs/packs.html; no SKILLS writer).
#    - packs/se/SKILL.md: add the slug to a Topics row and an Agency
#      contexts row. Add a Licences row only when the licence is not
#      public domain.
#    - docs/source-watchlist.json: hand-edit a new object. Copy an
#      existing object's keys (slug, publisher, document, version,
#      last_checked, hint). One entry per live catalog pack.
#      python tooling/check_source_watch.py --record updates an existing
#      slug only (version and last_checked). It refuses a slug that is
#      not already in the file. After the hand-edit, refresh with:
#      python tooling/check_source_watch.py --record SLUG VERSION DATE
#      DATE is YYYY-MM-DD. An empty last_checked fails the local gate.
#    - Capability map, inputs first: hand-edit
#      docs/classification-rules.json (one assignment per chapter:
#      pack, chapter, cluster, is_support). Hand-edit
#      docs/capability-pack-map-note-overrides.json only when a chapter
#      needs a note (pack, chapter, note). Do not hand-edit
#      docs/capability-pack-map.json. The generator owns that file and
#      docs/capability-pack-map.md. Then:
#      python tooling/generate_capability_map.py --generated-on YYYY-MM-DD --sync-md
#      --generated-on is required (no wall-clock default). --sync-md
#      rewrites the human summary tables. Then check:
#      python tooling/check_capability_map.py
#      It must exit 0. Commit the generated JSON and
#      MD together.
#    - Per-pack page and sitemap:
#      python tooling/gen_pack_pages.py --only <slugs>
#      --only takes slugs comma-separated. It limits which pack pages this
#      run rewrites. Omit it and the
#      run rewrites every pack page. docs/sitemap.xml is always rewritten.
#    - Plugin skill lists: add the pack path to the "skills" array in
#      both .claude-plugin/plugin.json (entry ./packs/<slug>) and
#      .cursor-plugin/plugin.json (entry ./packs/<slug>/SKILL.md).
#      marketplace.json has no skills array.
#    A signpost or an orchestrator: do not add a catalog row and do not
#    add a watchlist entry. Do not run gen_pack_pages.py for that slug
#    (it refuses a slug that is not in catalog.json, and docs/packs/ has
#    no page for these members). Still add the SKILLS.md row (then
#    gen_packs_page.py), the packs/se/SKILL.md rows, and the plugin
#    skills entries when that member is published. Skip the capability
#    map unless the member has chapters. The eight signpost packs have
#    none (classification-rules.json signpost_packs).

# 5. Validate:
python tooling/validate_pack.py packs/<slug>
```

## Quality rules

- **Ground every claim in the source.** Do not invent frameworks the source does not
  contain. Preserve the source's exact terminology and framework names.
- **Synthesize, don't copy.** No long verbatim passages (it is both a quality rule and a
  licence-safety rule). Reference depth, not reproduction.
- **Be honest about scope.** The `SKILL.md` description and `## Scope & Limits` must say
  what the source is *thin* on, so users do not over-rely on it.

## Open a PR

- One pack per PR.
- PR description: source, version, licence, tier, and a line confirming it is not Excluded.
- CI does not run `validate_pack.py`. It runs inline data-invariant checks including leak sentinels, link policy, frontmatter, catalog, version, index count, chapter overlap, and map and classification invariants, and never executes repository code. Before the PR, run `python tooling/validate_pack.py packs/<slug>`. CI runs the mechanical licence subset and the signpost shape check inline and still does not execute `validate_pack.py`. Tier judgement (1/2/3) is reviewed by a maintainer.

## Before you tag

Run `python tooling/check_release.py` on the exact commit you tag. PASS is required. The PASS line reads `RELEASE CHECK: PASS (v<version> @ <short-sha>)` and the sha must match the commit you tag; a `@ no-git` receipt never satisfies it.

CI green is necessary but not sufficient.

Local-only classes: full pack validation, source-watch freshness, generator replay (capability map and packs.html), and tracked-sources emptiness. The check-by-check list stays in the header of [.github/workflows/validate.yml](.github/workflows/validate.yml) and in the docstring of `tooling/check_release.py`. Do not treat this section as that list.

Do not cut the tag or a GitHub Release on CI green alone.

## Reporting a licensing concern

If you believe a pack misrepresents its source's licence, open an issue with the
`licensing` label: these are triaged first. We would rather pull a pack than ship one
that should not be redistributed.
