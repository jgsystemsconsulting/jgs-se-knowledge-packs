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

## Current State

**Shipped:** v1.18.0 (2026-08-17) — 63 packs (61 catalog + 2 signposts) across NASA/DoD/FAA/NIST/GAO/DOE/DHS/EU/SEBoK lineages; capability map v2 (schema 2, 628 entries, 32 clusters, hardened gate + CONTRACT) consumable by the se-agents generator; jgs-reference-skill pipeline synced to upstream book-to-skill v1.4.0.

## Next Milestone Goals

v1.19 (unsccoped): carry-forward backlog in STATE.md (FUT-04/05, overlap checker, thin clusters 3/5/15, map-gate wiring, doc hygiene, AAF vetting); candidate seeds in .planning/research/capability-gap-report.md. Strategic option: the se-agents generator repo (docs/ROLE-AGENTS-REQUIREMENTS-V2.md) — the map contract it consumes is now stable.

## Constraints


- Pack content licences are inherited from sources (Tier 1 public domain → Tier 3 excluded); vetting is a hard stop, not advisory
- Packs must stay plain Markdown, progressive-disclosure structured (SKILL.md index + on-demand chapters)
- CI `content-integrity` gate must pass for any release commit
