<!--
Copyright (c) 2026 JG Systems Consulting Ltd. — MIT License (see LICENSE).
SPDX-License-Identifier: MIT
-->

# Contributing

Thanks for helping grow the catalogue. The bar for a pack is **quality + provenance**:
faithful to its source, and legally redistributable.

## Before you build: vet the source

This is the non-negotiable first step. Read [docs/SOURCE-VETTING.md](docs/SOURCE-VETTING.md)
and confirm:

1. The source is **Tier 1 (public domain)** or **Tier 2 (open licence)** — or Tier 3 with
   a written justification.
2. The source is **not** on the Excluded list (ISO/IEC/IEEE, SWEBOK, MITRE SE Guide,
   INCOSE Handbook, TOGAF, PMBOK, …).
3. You found the licence **in the source itself**, not a third-party summary.

If a source is merely "free to download," that is not enough. Free ≠ redistributable.

## Build the pack

```bash
# 1. Scaffold with provenance (forces a tier + licence on record):
python tooling/build_pack.py --slug <slug> --title "..." --publisher "..." \
    --version "..." --url "..." --license "..." --tier <1|2|3> --commercial-use <true|false>

# 2. Generate content per docs/PACK-SPEC.md:
#    - extract text (book-to-skill), map chapter offsets, generate reference-depth
#      chapters + glossary/patterns/cheatsheet, then the SKILL.md index.
# 3. Fill the TODOs in packs/<slug>/PACK.yaml and packs/<slug>/LICENSE.
# 4. Add a catalog row and rebuild catalog.json (see tooling/ or hand-edit).

# 5. Validate:
python tooling/validate_pack.py packs/<slug>
```

## Quality rules

- **Ground every claim in the source.** Do not invent frameworks the source does not
  contain. Preserve the source's exact terminology and framework names.
- **Synthesize, don't copy.** No long verbatim passages — it is both a quality rule and a
  licence-safety rule. Reference depth, not reproduction.
- **Be honest about scope.** The `SKILL.md` description and `## Scope & Limits` must say
  what the source is *thin* on, so users do not over-rely on it.

## Open a PR

- One pack per PR.
- PR description: source, version, licence, tier, and a line confirming it is not Excluded.
- CI runs `validate_pack.py` on every pack and blocks invalid licence tiers and broken
  chapter links. Tier judgement (1/2/3) is reviewed by a maintainer.

## Reporting a licensing concern

If you believe a pack misrepresents its source's licence, open an issue with the
`licensing` label — these are triaged first. We would rather pull a pack than ship one
that should not be redistributed.
