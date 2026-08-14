# Constraints

## Pack required file layout
- source: docs/PACK-SPEC.md
- type: schema
- content: Every pack must reside under `packs/<slug>/` and contain at minimum: `SKILL.md` (always-loaded index with frontmatter + core frameworks + chapter index + topic index, body < ~4,000 tokens), `PACK.yaml` (provenance + licence metadata), `LICENSE` (reproduces the source's licence/terms), and `chapters/` directory with on-demand chapter files named `chNN-<slug>.md`. Optional files: `glossary.md`, `patterns.md`, `cheatsheet.md`.

## SKILL.md structure and section order
- source: docs/PACK-SPEC.md
- type: schema
- content: SKILL.md must have YAML frontmatter with `name` (folder slug) and `description` (states what the pack covers and its scope limits). Body order (most important first): `## How to Use This Skill`, `## Core Frameworks & Mental Models` (~2,000 tokens), `## Chapter Index` (table linking every `chapters/chNN-*.md`), `## Topic Index` (alphabetical term to chapter routing), `## Supporting Files`, `## Scope & Limits`. Every `chapters/` link in the index must resolve to a real file (CI-checked).

## Chapter file structure
- source: docs/PACK-SPEC.md
- type: schema
- content: Chapter files must follow reference-depth structure with sections: `Core Idea`, `Frameworks Introduced`, `Key Concepts`, `Mental Models`, `Anti-patterns` (if any), `Key Takeaways`, `Connects To`. Every claim must be grounded in the source. Frameworks must not be invented beyond what the source contains. Prose must be synthesized compactly; no long verbatim passages (quality and licence-safety rule).

## PACK.yaml mandatory fields
- source: docs/PACK-SPEC.md
- type: schema
- content: `title`, `publisher`, `license`, `license_tier`, and `commercial_use` are mandatory fields in PACK.yaml, validated by `tooling/validate_pack.py`. `license_tier` must be 1, 2, or 3 (never Excluded). Optional fields include `slug`, `source_version`, `share_alike`, `attribution_required`, `build`, `notes`. No `source_url` or source-material link is stored or published (no-source-link policy per LICENSING.md cross-ref). Source is identified textually by title + publisher + version.

## PACK.yaml full schema
- source: docs/PACK-SPEC.md
- type: schema
- content: PACK.yaml schema fields: `slug` (folder name, kebab-case), `title` (string), `publisher` (string), `source_version` (string), `license` (source licence verbatim name), `license_tier` (1|2|3), `commercial_use` (boolean), `share_alike` (boolean), `attribution_required` (boolean), `build.method` (string), `build.source_pages` (integer), `build.chapters` (integer), `build.built_on` (date), `notes` (string).

## Validation rules
- source: docs/PACK-SPEC.md
- type: nfr
- content: `tooling/validate_pack.py packs/<slug>` checks: required files present, frontmatter valid, every chapter link resolves, PACK.yaml mandatory fields filled, and `license_tier in {1,2,3}`. CI runs this on every pack on every PR.

## Agent Skills compatibility
- source: docs/PACK-SPEC.md
- type: protocol
- content: Packs follow the Agent Skills `SKILL.md` convention so they load in Claude Code, GitHub Copilot CLI, and Amp without modification. Installation is via cloning the repo and copying/symlinking the pack into the host's skills directory.
