---
id: SEED-001
status: dormant
planted: 2026-08-17
planted_during: post-v1.18.0 (milestones archived)
trigger_when: when scoping v1.19 or any milestone that fattens packs for se-agents IOs
scope: large
---

# SEED-001: Pack depth for se-agents IOs — 17 thin-primary competencies

## Why This Matters

`jgs-se-agents` already generates 37 ISECF-anchored skills + 41 role agents. Skills pull "what good looks like" from knowledge-pack chapters via `data/competency-cluster-map.json` → live `capability-pack-map.json` (v2, 628 entries). **Name match is clean** (every mapped cluster exists). **v1.18 closed the empty cluster** (Training 0→12) and lifted every competency's mapped-cluster sum to ≥12 — there is no competency with *zero* usable depth.

What remains is **primary-cluster starvation**: 17/37 competencies still have a thin primary (count < 8 **or** ≤2 distinct packs). The generator caps refs at 20 and fills from secondaries, so Critical Thinking (SECF-CORE-05) currently emits **2 Decision Analysis refs + 18 Systems Thinking refs** — the agent can talk about systems thinking, not run a trade study. Same pattern: Negotiation / Communications / Facilitation all sit on Stakeholder Engagement (3 entries / 3 packs); Validation (5), Integration (4), Interfaces (4) cannot own their IOs.

This is the pack-side half of "enable the agents." The se-agents half (refresh stale 502-count docs, align `thin: 3` vs pack-side `<8 or ≤2 packs`, optional Cybersecurity / Digital Engineering bindings) lives in that repo — do not mix it into a packs milestone except as a documented consumer contract.

## When to Surface

**Trigger:** when relevant — specifically `/gsd:new-milestone` for v1.19, or any milestone whose goal is "fatten packs so role agents can execute IOs."

Surface this seed when the user mentions: se-agents, ISECF competencies, role agents, "what knowledge is missing", thin clusters 3/5/15, FUT-04, Decision Analysis, Stakeholder Engagement, Validation, Integration, Interfaces.

Do **not** surface as a reason to build per-role packs (rejected 2026-08-16: role lens belongs to the skills layer).

## Scope Estimate

**Large** — a dedicated milestone (v1.19-shaped), not a drive-by:

1. **Vetting phase** for the candidate sources below (same Phase-6 pattern; AAF remains "vet before any use").
2. **Build phase** targeting the poorest primaries first (table). Expect 4–7 Tier-1 packs if the UNVERIFIED items resolve; fewer if they don't.
3. **Map regeneration** (existing agent-pass + `check_capability_map.py`) with an extra assert: no competency primary remains at count < 4 / 1 pack (tighter floor than today's SC-2).
4. **Consumer refresh** (se-agents repo, separate milestone): bump docs off the 502 residue, realign thin-threshold, consider raising/splitting the 20-ref cap so fat secondaries cannot drown a thin primary.

## Breadcrumbs

### Poorest 10 competencies (live map 2026-08-17)

| ID | Competency | Primary cluster | n | Depth | Why it blocks IOs |
|---|---|---|---:|---:|---|
| SECF-PROF-04 | Negotiation | Stakeholder Engagement & Needs | 3 | 12 | No clean Tier-1 source (gap report: SEBoK expansion only) |
| SECF-PROF-01 | Communications | Stakeholder Engagement & Needs | 3 | 15 | same cluster |
| SECF-PROF-06 | Facilitation | Stakeholder Engagement & Needs | 3 | 18 | same cluster |
| SECF-INTE-03 | Logistics | Logistics, Supportability & Sustainment | 12 | 18 | **diversity-thin** (2 packs); DAU AAF Product Support (vet first) |
| SECF-TECH-08 | Transition | Operations, Maintenance & Disposal | 6 | 22 | NASA-STD-8719.14 |
| SECF-MANA-07 | Information Management | Data & Information Management | 7 | 22 | NASA-HDBK-2203 (GP-08 descoped — wiki-only) |
| SECF-TECH-04 | Integration | Integration | 4 | 23 | DAU AAF Software/DevSecOps (vet first); DAFMAN already +1 |
| SECF-TECH-07 | Validation | Validation | 5 | 24 | DoDM 5000.102; more VV&A RPG chapters |
| SECF-CORE-05 | Critical Thinking | Decision Analysis & Trade Studies | 2 | 27 | **worst primary count**; FUT-04 Army CBA; remap A-94 / VV&A decision chapters (today: nasa-ceh + nasa-se-handbook only) |
| SECF-TECH-05 | Interfaces | Interface Management & ICIDs | 4 | 28 | GPS ICD-IS-200/300 exemplars (FAA-STD-025 already +2) |

Also thin-primary: Quality (3), Decision Management (same Decision Analysis primary), Acquisition (7), Coaching/Mentoring (Training 12 but 2 packs), Utilization & Retirement (Ops 6).

### Pack-side candidates (from capability-gap-report.md, still valid)

- **FUT-04** Army CBA Guide — unlocks Decision Analysis (CORE-05, MANA-03) *if* the ASAFM PDF becomes reachable
- DoDM 5000.102 — Validation
- NASA-STD-8719.14 — Ops/Maintenance/Disposal (Transition + Utilization)
- GPS ICD exemplars — Interfaces
- NASA SP-7084 — Training *diversity* (count already 12; still 2 packs)
- NASA-HDBK-2203 / NPR 7150.2 — Data Mgmt + Quality (GP-08 was descoped: no consolidated PDF)
- DAU AAF Product Support + Software pathway — Logistics + Integration (**AAF not yet vetted** — Phase 6 deferral, never use unvetted)

### Unused live clusters (se-agents mapping gap, not a pack gap)

Cybersecurity & Security Engineering (69 / 10 packs) and Digital Engineering & Digital Twins (25 / 4) have deep pack coverage and **zero** competency bindings. Optional se-agents mapping work — do not build more cyber/DE packs to "enable agents"; bind the existing ones.

### Snapshot residue (se-agents docs, not JSON)

`docs/input/capability-pack-map.json` is already live 628. README / ROLE-AGENTS-REQUIREMENTS-V2.md / RUNTIME-INTEGRATION-HANDOFF.md / `docs/input/capability-pack-map.md` still say **502**. Fix on the se-agents side.

## Notes

- Computed 2026-08-17 against live `docs/capability-pack-map.json` (schema 2, 628 entries) and `jgs-se-agents/data/competency-cluster-map.json` (37 competencies, 0 name mismatches).
- Threshold used: pack-side (thin = count < 8 OR ≤2 packs). se-agents mapping still declares `thin: 3` — align as part of the consumer refresh.
- Design constraint (2026-08-16): **no per-role packs**. Role lens stays in the skills/agents layer.
- Related backlog already in STATE.md: FUT-04, FUT-05, thin clusters 3/5/15, AAF vetting-before-use.
