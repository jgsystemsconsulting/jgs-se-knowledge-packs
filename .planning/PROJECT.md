# JG Systems SE Knowledge Packs

## What This Is

A curated library of licence-clean systems-engineering "knowledge packs" — Agent Skills distilled from authoritative sources (NASA, DoD, FAA, NIST, GAO, SEBoK, EU, OMG) — installable into Claude Code, Copilot CLI, and other Agent-Skills hosts. Each pack is a single-source reference oracle built with the jgs-reference-skill pipeline (fork of book-to-skill).

## Core Value

Every pack must be a licence-clean, validated, single-source reference that an engineer can trust and an agent can load without filling its context window.

## Business Context

- **Customer**: Systems engineers and engineering agents (JG Systems Consulting practice + open-source users)
- **Revenue model**: Open-source (MIT tooling, per-pack source licences); consulting lead-generation
- **Success metric**: Pack count × install/usage validity (CI-validated catalogue)
- **Strategy notes**: Non-commercial (NC) and share-alike (SA) sources carry licence obligations forward — licence tiering is a hard gate, not a nicety

## Current State

**Shipped:** v1.19.0 (2026-08-17) — Agent IO Depth. Catalog 63 packs / 65 dirs (+2 signposts); capability map schema 2, map_version 1.19.0, 644 entries, 32 clusters; dual-gate (`check_capability_map` wired into `check_release`); 2 new Tier-1 packs (`nasa-std-8719-14`, `is-gps-200n`) + VV&A RPG chapter depth + Decision Analysis remap. Honest deferrals: AAF (IO-05/06), Army CBA (FUT-04), IO-07 accept (no pack).

## Current Milestone: v1.19.1 Cleanup + Carried Backlog

**Goal:** Make planning/ledger truth match shipped reality, then clear the full carried backlog (retries, IN-02, FUT-05) and ship a coherent v1.19.1 surface.

**Target features:**
- GSD ledger hygiene residual: verify already-moved milestone archives + master-flow (HYG-20-01/02/03); tick MAP-19-01..05 and annotate VET-19 not-built in archived v1.19.0-REQUIREMENTS; refresh live MILESTONES/PROJECT surfaces (HYG-20-04/05/06)
- Planning-surface refresh (PROJECT / ROADMAP / STATE / REQUIREMENTS / MILESTONES)
- FUT-04 Army CBA Guide PDF retry — build only if licence-cleared
- AAF Product Support + Software pathway licence spot-check — build Integration/Logistics packs only if cleared; else keep deferred
- IN-02 minimal committed overlap checker in tooling/ + release gate
- FUT-05 deterministic capability-map generator (or honest partial with residual agent-judgment documented)
- Conditional packs only when sources clear; release surface + tag v1.19.1 when gates PASS

## Constraints

- Pack content licences are inherited from sources (Tier 1 public domain → Tier 3 excluded); vetting is a hard stop, not advisory
- Packs must stay plain Markdown, progressive-disclosure structured (SKILL.md index + on-demand chapters)
- CI `content-integrity` gate must pass for any release commit
- Do not invent packs when sources stay uncleared (record deferral)
- se-agents consumer refresh stays in the sibling repo
- Per-role packs remain rejected

## Evolution

This document evolves at phase transitions and milestone boundaries.

**After each phase transition** (via `/gsd-transition`):
1. Requirements invalidated? → Move to Out of Scope with reason
2. Requirements validated? → Move to Validated with phase reference
3. New requirements emerged? → Add to Active
4. Decisions to log? → Add to Key Decisions
5. "What This Is" still accurate? → Update if drifted

**After each milestone** (via `/gsd:complete-milestone`):
1. Full review of all sections
2. Core Value check — still the right priority?
3. Audit Out of Scope — reasons still valid?
4. Update Context with current state
