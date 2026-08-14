# JG Systems SE Knowledge Packs

## What This Is

A curated library of 48 "knowledge packs" — Agent Skills distilled from authoritative systems-engineering sources (NASA, DoD, FAA, NIST, GAO, SEBoK, EU, OMG) — installable into Claude Code, Copilot CLI, and other Agent-Skills hosts. Each pack is a licence-clean reference oracle over one source, built with the jgs-reference-skill pipeline (fork of book-to-skill, synced to upstream v1.4.0).

## Core Value

Every pack must be a licence-clean, validated, single-source reference that an engineer can trust and an agent can load without filling its context window.

## Business Context

- **Customer**: Systems engineers and engineering agents (JG Systems Consulting practice + open-source users)
- **Revenue model**: Open-source (MIT tooling, per-pack source licences); consulting lead-generation
- **Success metric**: Pack count × install/usage validity (CI-validated catalogue)
- **Strategy notes**: Non-commercial (NC) and share-alike (SA) sources carry licence obligations forward — licence tiering is a hard gate, not a nicety

## Requirements

### Validated

Shipped through v1.16.3:

- [x] 48 packs across NASA / DoD / FAA / GAO / NIST / EU / SEBoK / OMG lineages, each conforming to docs/PACK-SPEC.md
- [x] Deterministic licence-vetting + validation toolchain (vet_source, validate_pack, check_overlap, check_release; CI gate in .github/workflows/validate.yml)
- [x] Multi-host installers (Claude Code, OpenClaw, Copilot CLI) + catalog.json registry
- [x] Build pipeline promoted to jgs-reference-skill (fork of book-to-skill, synced v1.4.0)

### Active

(Defined per milestone — see REQUIREMENTS.md and ROADMAP.md for v1.17.0)

### Out of Scope

- Reproducing paywalled standards text (ISO/IEC/IEEE full texts, INCOSE Handbook) — not licence-viable; tracked in docs/SOURCE-VETTING.md Excluded list
- Non-SE domains (pure software architecture, generic LLM prompting) — outside the library's charter
- Runtime dependencies (MCP servers, API keys) — packs are plain Markdown by design

## Context

- Content-first repo: Markdown packs + stdlib-only Python tooling; no package manager
- The 7-doc codebase map lives in `.planning/codebase/`; PACK-SPEC constraints in `.planning/intel/`
- Known concerns (from map): signpost-pack validation false-fails, CI gate logic duplication, catalog.json drift unguarded, hardcoded local paths in build_all_packs.workflow.js, stale .pyc-only tests
- Next milestone (v1.17.0): 11 researched candidates (8 Tier-1 builds + 3 vetted-out; 0 Tier-2 packs) + ruled-out source tracking

## Constraints

- Pack content licences are inherited from sources (Tier 1 public domain → Tier 3 excluded); vetting is a hard stop, not advisory
- Packs must stay plain Markdown, progressive-disclosure structured (SKILL.md index + on-demand chapters)
- CI `content-integrity` gate must pass for any release commit
