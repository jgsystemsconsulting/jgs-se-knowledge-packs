# Requirements — SE Role Agents & Shared Skills (v2)

Status: DRAFT for roadmap input. Supersedes v1 (chat, 2026-08-14).
Inputs: `SE-Framework-Data/data/roles/roles.json` (37 roles), INCOSE SE Competency
Framework (ISECF 2nd ed. — 37 competencies, 5 groups, 5 proficiency levels),
`docs/capability-pack-map.{md,json}` in this repo (32 capability clusters,
502 chapter references).

## 1. Goal

Generate, from SE-Framework-Data roles.json anchored to the INCOSE Competency
Framework, a library of 37 role agents and a shared, industry-standard-aligned
skill library in ZCode/Claude Agent Skills format, such that any agent can be
invoked to perform its role, loads its skills on demand, and draws "what good
looks like" depth from the knowledge packs. Source data remains the single
source of truth; generated artifacts are never hand-edited.

## 2. Definitions & layering

- **Skill** = one capability, anchored to an ISECF competency (v1: free-text
  vocabulary — superseded). One SKILL.md per skill; shared across roles.
- **Agent** = one role from roles.json rendered as an agent file: identity,
  responsibilities, what-good-looks-like, misunderstandings, lessons learned,
  inputs/outputs, and a **competency profile** — the skills it loads with an
  expected ISECF proficiency level (1 Awareness → 5 Expert) per skill.
- **Knowledge base** = knowledge-pack chapters, addressed via
  `capability-pack-map.json` (cluster → chapters).
- **Generator** = script in the new repo reading roles.json + competencies +
  the mapping, emitting agents/skills deterministically.

```
ISECF competencies ──→ skills/ (procedure + KSAB + pack refs)
                            ↑ loaded by name + expected level
roles.json roles    ──→ agents/ (persona + competency profile)
                            ↓ depth
knowledge packs     ──→ chapters via capability-pack-map.json
```

## 3. Functional requirements

**FR-1 Generation**
- FR-1.1 One agent per role (37), one SKILL.md per distinct skill, idempotent
  regeneration.
- FR-1.2 Agent body includes: description, responsibilities,
  whatGoodLooksLike, commonMisunderstandings, lessonsLearned,
  collaborationTips, typicalInputs/Outputs, aliases, primaryProcessArea,
  standardsTrace, associatedProcesses.
- FR-1.3 Agent references skills **by name** with a proficiency level
  (e.g. `Requirements Engineering — Practitioner`); never embeds skill content.
- FR-1.4 Skills derive from ISECF competencies: each SKILL.md carries
  competency name, group, and ID; procedure drawn from KSAB indicators.

**FR-2 Capability→knowledge binding**
- FR-2.1 Each SKILL.md references pack chapters via the capability clusters
  in `capability-pack-map.json` (source of the mapping at generation time).
- FR-2.2 Skills whose cluster is empty or thin (see §6) are still generated
  and flagged in a gap report.
- FR-2.3 Mapping data lives as data (JSON), refreshable when packs change.

**FR-3 Traceability & provenance**
- FR-3.1 Every generated file: generated-header, source commit, do-not-edit.
- FR-3.2 Manifest JSON: agent → skills(+levels) → clusters → pack chapters.

**FR-4 Validation**
- FR-4.1 Validator checks: 37 agents; every referenced skill exists; no
  orphans (unless allowlisted); proficiency levels ∈ 1–5; frontmatter valid;
  manifest matches files. Runs in CI.

## 4. Non-functional requirements

- NFR-1 Skills stay thin (< ~150 lines): knowledge lives in packs.
- NFR-2 Generator is a boring single script + data files.
- NFR-3 Data-side enrichment (roles.json, competencies.json, mapping) improves
  output with no code changes.
- NFR-4 INCOSE framework content used per its terms; attribution headers on
  artifacts that embed KSAB-derived text; check redistribution before any
  open-sourcing of the new repo.

## 5. Constraints & dependencies

- C-1 Blocked on: skills population of roles.json (in flight) **followed by
  reconciliation against ISECF competencies** (map/rename/absorb — the
  free-text skills are draft material, not final).
- C-2 New dedicated repo (e.g. `jgs-se-agents`); SE-Framework-Data and
  knowledge-packs are read-only inputs.
- C-3 ZCode/Claude format first; adapters are v2.
- C-4 New: ISECF 2nd-edition spreadsheet ingested into SE-Framework-Data as
  machine-readable `competencies.json` (groups, competencies, 5 levels, KSAB).

## 6. Known capability gaps (from the mapping exercise)

Coverage is strong overall (502 refs) but uneven. Thin/empty clusters that
will produce shallow skills unless backfilled:

| Cluster | Refs | Note |
|---|---|---|
| Training & Documentation Delivery | 0 | no primary chapter exists |
| Opportunity/Benefit Management | 1 | |
| Traceability & Allocation | 2 | core SE capability — underweight |
| Integration | 2 | underweight |
| Decision Analysis & Trade Studies | 2 | underweight |
| QA & Process Compliance | 2 | partially covered under 30/32 |

Heavy clusters (Safety 71, PM 64, Cybersecurity 40, Measurement 33) need
curation so skill reference lists don't drown the model.

## 7. Out of scope (v1)

Multi-platform adapters; skill registry beyond name matching; runtime
orchestration/workflows between agents; eval harness; specialty engineering
depth beyond pack coverage.

## 8. Open questions

- OQ-1 Skill granularity: 1:1 with ISECF competency (37) vs decomposed —
  recommend start 1:1, split on evidence of need.
- OQ-2 Repo licensing: private vs open for jgs-se-agents (affects headers).
- OQ-3 Agent frontmatter `tools`/permissions vs pure knowledge persona.
- OQ-4 Where the reconciliation pass lives (SE-Framework-Data vs new repo)
  and who owns curation of thin clusters.

## 9. Indicative phase split (for GSD roadmap)

1. ISECF ingestion → competencies.json; reconcile roles.json skills against it.
2. New repo + generator skeleton; copy mapping as data input.
3. Skill library generation (thin clusters flagged).
4. Agent emission with competency profiles.
5. Validator + manifest + ROLE-REQE pilot review.
