<!--
Copyright (c) 2026 JG Systems Consulting Ltd. — MIT License (see ../LICENSE).
SPDX-License-Identifier: MIT
-->

# Pack Specification

A **knowledge pack** is a self-contained, installable agent skill built from one vetted
open source. It follows the [Agent Skills](https://github.com/agentskills/agentskills)
`SKILL.md` convention, so it loads in Claude Code, GitHub Copilot CLI, and Amp without
modification.

## Required layout

```
packs/<slug>/
├── SKILL.md          # REQUIRED. Always-loaded index: frontmatter + core frameworks
│                     #   + chapter index + topic index. Keep body < ~4,000 tokens.
├── PACK.yaml         # REQUIRED. Provenance + licence metadata (schema below).
├── LICENSE           # REQUIRED. Reproduces the SOURCE's licence/terms.
├── chapters/         # REQUIRED. On-demand chapter files, chNN-<slug>.md.
│   └── chNN-*.md     #   Loaded only when a topic routes to them (progressive disclosure).
├── glossary.md       # optional — key terms, alphabetical, with chapter refs.
├── patterns.md       # optional — concrete techniques (when to use / how / trade-offs).
└── cheatsheet.md     # optional — decision rules, selection tables, tells & smells.
```

## `SKILL.md` rules

- **YAML frontmatter** with `name` (= folder slug) and a `description` that states what
  the pack covers **and its scope limits** (be honest about what the source is thin on).
- Body order: most important first (hosts truncate from the end on compaction).
  - `## How to Use This Skill`
  - `## Core Frameworks & Mental Models` (~2,000 tokens — the toolkit, not a summary)
  - `## Chapter Index` (table linking every `chapters/chNN-*.md`)
  - `## Topic Index` (alphabetical term → chapter routing — this is how the agent
    navigates)
  - `## Supporting Files`
  - `## Scope & Limits` (what the pack does *not* cover; which source version)
- Every `chapters/` link in the index must resolve to a real file (CI checks this).

## Chapter file rules

Reference-depth structure (prose bodies of knowledge): `Core Idea`, `Frameworks
Introduced`, `Key Concepts`, `Mental Models`, `Anti-patterns` (if any), `Key Takeaways`,
`Connects To`. Ground every claim in the source slice — **do not invent frameworks the
source does not contain.** Synthesize compactly; never copy long verbatim passages
(both a quality rule and a licence-safety rule).

## `PACK.yaml` schema

```yaml
slug: sebok                       # folder name, kebab-case
title: "Guide to the Systems Engineering Body of Knowledge (SEBoK)"
publisher: "BKCASE Project (Trustees of the Stevens Institute of Technology)"
source_version: "v2.13 (2025-11-17)"
license: "CC BY-NC-SA 3.0"        # the SOURCE licence, verbatim name
license_tier: 2                   # 1 | 2 | 3  (see docs/SOURCE-VETTING.md)
commercial_use: false             # false if NC; true if PD or non-NC
share_alike: true                 # true if SA — pack content inherits the licence
attribution_required: true
build:
  method: "book-to-skill + offset-mapped parallel chapter generation"
  source_pages: 1465
  chapters: 41
  built_on: "2026-06-19"
notes: >
  CC BY-NC-SA: pack content is released under the same licence as SEBoK, not the
  repo's MIT. Non-commercial; attribution and share-alike carried forward.
```

`title`, `publisher`, `license`, `license_tier`, and `commercial_use` are **mandatory**
and checked by `tooling/validate_pack.py`. `license_tier` must be 1, 2, or 3 — never the
Excluded tier. **No `source_url` / source-material link is stored or published** — the
source is identified textually (title + publisher + version), and `publisher` carries the
attribution, per the no-source-link policy in [LICENSING.md](LICENSING.md).

## Installing a pack (end user)

```bash
# Claude Code — clone the whole repo, symlink/copy the pack into your skills dir:
git clone https://github.com/jgsystemsconsulting/jgs-se-knowledge-packs.git
cp -r jgs-se-knowledge-packs/packs/sebok ~/.claude/skills/sebok
# then in a session:  /sebok <topic>
```

(A future `tooling/install.py <slug>` will automate per-pack install across hosts.)

## Validation

```bash
python tooling/validate_pack.py packs/<slug>
```

Checks: required files present, frontmatter valid, every chapter link resolves,
`PACK.yaml` mandatory fields filled, and `license_tier ∈ {1,2,3}`. CI runs this on
every pack on every PR.
