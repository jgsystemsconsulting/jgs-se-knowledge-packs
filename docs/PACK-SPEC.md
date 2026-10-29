<!--
Copyright (c) 2026 JG Systems Consulting Ltd. MIT License (see ../LICENSE).
SPDX-License-Identifier: MIT
-->

# Pack Specification

A **knowledge pack** is a self-contained, installable agent skill built from one vetted
open source. It follows the [Agent Skills](https://github.com/agentskills/agentskills)
`SKILL.md` convention, so it loads in Claude Code, GitHub Copilot CLI, and Amp without
modification.

## Required layout (content packs)

```
packs/<slug>/
├── SKILL.md          # REQUIRED. Always-loaded index: frontmatter + core frameworks
│                     #   + chapter index + topic index. Keep body < ~4,000 tokens.
├── PACK.yaml         # REQUIRED. Provenance + licence metadata (schema below).
├── LICENSE           # REQUIRED. Reproduces the SOURCE's licence/terms.
├── chapters/         # REQUIRED. On-demand chapter files, chNN-<slug>.md.
│   └── chNN-*.md     #   Loaded only when a topic routes to them (progressive disclosure).
├── glossary.md       # optional: key terms, alphabetical, with chapter refs.
├── patterns.md       # optional: concrete techniques (when to use / how / trade-offs).
└── cheatsheet.md     # optional: decision rules, selection tables, tells & smells.
```

## `SKILL.md` rules

- **YAML frontmatter** with `name` (= folder slug) and a `description` that states what
  the pack covers **and its scope limits** (be honest about what the source is thin on).
- Body order: most important first (hosts truncate from the end on compaction).
  - `## When to use` (immediately followed by a `**Prerequisites:**` line naming what
    the reader should already have/know - RR-S-13; enforced by tooling/check_release.py)
  - `## How to Use This Skill`
  - `## Core Frameworks & Mental Models` (~2,000 tokens: the toolkit, not a summary)
  - `## Chapter Index` (table linking every `chapters/chNN-*.md`)
  - `## Topic Index` (alphabetical term → chapter routing: this is how the agent
    navigates)
  - `## Supporting Files`
  - `## Scope & Limits` (what the pack does *not* cover; which source version)
- Every `chapters/` link in the index must resolve to a real file (checked by
  `tooling/validate_pack.py` in the local release gate; CI does not run the
  structural validator, see the Validation section below).

## Chapter file rules

Reference-depth structure (prose bodies of knowledge): `Core Idea`, `Frameworks
Introduced`, `Key Concepts`, `Mental Models`, `Anti-patterns` (if any), `Key Takeaways`,
`Connects To`. Ground every claim in the source slice. **Do not invent frameworks the
source does not contain.** Synthesize compactly; never copy long verbatim passages
(both a quality rule and a licence-safety rule).

## Build rules

Established by the 2026-10-28 cuts `docs/superpowers/specs/2026-10-28-rebuild-nasa-risk-handbook-v2.md`, `docs/superpowers/specs/2026-10-28-rebuild-faa-ams-vv-v4.md`, and `docs/superpowers/specs/2026-10-28-uk-defence-jsp-912-pack.md`.

**Multi-PDF / part pin.** A source that ships as more than one PDF or part is still one pack when the publisher treats the parts as one document. Pin every part. Record each part's identifier, byte size, and page count in `PACK.yaml` `notes`. `source_version` names every part. Do not drop a part to shrink the pack. Do not split parts into two slugs. Chapter titles name the part they draw from. Worked examples: `packs/nasa-risk` (handbook plus examples volume), `packs/jsp-912` (Part 1 Directive and Part 2 Guidance). A single-PDF source stays one pack; do not invent a second pack for appendices. Worked example: `packs/faa-ams-vv`.

**Contents list wins.** Freeze chapter titles from the source's own contents list (every pinned PDF). A provisional map, a prior pack's grouping, or a TOC that disagrees with the contents list loses. If a heading is absent from every pinned contents list, do not write that chapter. Definitions, acronym lists, and appendices do not become chapters unless the contents list gives them body that the pack is reconstructing. Worked examples: `packs/faa-ams-vv` (contents list, not the 3.0 grouping), `packs/nasa-risk`, `packs/jsp-912`.

**Verify what you wrote.** After chapter and support prose is written, read it back against the extract before registration. Repair function words, articles, and section marks that a transport or generation pass stripped. `validate_pack.py`, `check_release.py`, and CI stay green on stripped prose. The read-back is the check. Worked examples of the miss: the faa-ams-vv V4 rebuild (repaired before close) and `packs/jsp-912/LICENSE` (advisory a-29, still awkward, terms intact).

## `PACK.yaml` schema

```yaml
slug: sebok                       # folder name, kebab-case
title: "Guide to the Systems Engineering Body of Knowledge (SEBoK)"
publisher: "BKCASE Project (Trustees of the Stevens Institute of Technology)"
source_version: "v2.14 (2025-11-17)"
license: "CC BY-NC-SA 3.0"        # the SOURCE licence, verbatim name
license_tier: 2                   # 1 | 2 | 3  (see docs/SOURCE-VETTING.md)
commercial_use: false             # false if NC; true if PD or non-NC
share_alike: true                 # true if SA: pack content inherits the licence
attribution_required: true
build:
  method: "synthesized reference notes from the pinned source, chapter freeze from the contents list"
  source_pages: 1465
  chapters: 41
  built_on: "2026-06-19"
notes: >
  CC BY-NC-SA: pack content is released under the same licence as SEBoK, not the
  repo's MIT. Non-commercial; attribution and share-alike carried forward.
```

`title`, `publisher`, `license`, `license_tier`, and `commercial_use` are **mandatory**
and checked by `tooling/validate_pack.py`. `license_tier` must be 1, 2, or 3, never the
Excluded tier. **No `source_url` / source-material link is stored or published.** The
source is identified textually (title + publisher + version), and `publisher` carries the
attribution, per the no-source-link policy in [LICENSING.md](LICENSING.md).

## Installing a pack (end user)

Clone the repo and run the root installer from the repo root. The default copies every pack into `~/.claude/skills/jgs-se-knowledge-packs/<slug>/` (`<slug>` is the pack directory name under `packs/`, for example `sebok`). The installer honours `$CLAUDE_CONFIG_DIR`. `install.sh` and `install.ps1` are wrappers around the same script and pass every argument through.

```bash
git clone https://github.com/jgsystemsconsulting/jgs-se-knowledge-packs.git
cd jgs-se-knowledge-packs
python install.py --dry-run          # preview pack list and target, copy nothing
python install.py                    # Claude Code default, namespaced
python install.py --flat             # drop the vendor namespace
python install.py --list-agents      # supported agents and their targets
python install.py --agent openclaw   # one non-default agent
python install.py --agent all        # all user-global agents at once
```

Native agents get the pack folder. Transform agents get the `SKILL.md` index inlined into one file. Install procedure and the agent matrix live in the [README](../README.md) install sections and in [docs/other-agents.md](other-agents.md).

## Validation

```bash
python tooling/validate_pack.py packs/<slug>
```

Member kinds (`kind:` in SKILL.md frontmatter):

| Kind | Members | Requires | Skips |
|---|---|---|---|
| content pack (default) | the 74 catalogue packs | Full layout above: `LICENSE` reproducing the source's terms and `chapters/` with at least one chapter | Nothing |
| `signpost` | `packs/omg-signpost`, `packs/se-standards-signpost`, `packs/automotive-signpost`, `packs/functional-safety-signpost`, `packs/avionics-signpost`, `packs/rail-signpost`, `packs/space-signpost`, `packs/maritime-signpost` | `SKILL.md` + `PACK.yaml`, all remaining checks | The `LICENSE` and `chapters/` checks (citation-only, zero reproduced content) |
| `orchestrator` | `packs/se` | `SKILL.md` + `PACK.yaml`, all remaining checks | The `LICENSE` and `chapters/` checks (routes to packs, no source content). Its `SKILL.md` body carries the whole routing map and ships in every transform prompt, so it is reviewed against a 24,000-byte ceiling (a review criterion, not a gate). |

Checks: required files present, frontmatter valid, every chapter link resolves,
`PACK.yaml` mandatory fields filled, and `license_tier ∈ {1,2,3}`. The validator
runs locally via `tooling/check_release.py` (check 5) and is deliberately kept
out of CI to avoid parser fork drift; CI runs inline data-invariant heredocs
instead (see the `.github/workflows/validate.yml` header), including a
pack-quality subset (orphan chapter files, 30-line chapter floor, Topic Index
resolution) twinned with `tooling/check_pack_quality.py` (check 16). CI checks
content-pack `LICENSE` presence, the six mandatory `PACK.yaml` fields, and
`license_tier` in {1, 2, 3}, and a `kind: signpost` tree must contain only
`SKILL.md` and `PACK.yaml`. Full structural validation remains
`python tooling/validate_pack.py`.
