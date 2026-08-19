# Phase 8 Research: Agent-Enablement Surface (AE-01..03)

Date: 2026-08-14
Inputs: ROADMAP Phase 8, REQUIREMENTS AE-01..03, docs/ROLE-AGENTS-REQUIREMENTS-V2.md FR-2.x,
docs/capability-pack-map.{md,json}, 7-GAP_ANALYSIS.md routing, tooling/ conventions,
.planning/research/capability-gap-report.md §1.

## Current state (verified live)

- `docs/capability-pack-map.json`: keyless top level — `{"clusters": [{name, chapters: [{pack, chapter, note}]}]}`,
  32 clusters, 570 entries, no `schema_version` / `map_version` / `generated_on`.
- Map covers only the 54 pre-Phase-7 packs (v1.17 catalog). The 7 new GP packs are absent:
  dod-vva-rpg (10 ch), dote-te-guidebook (8), mil-std-40051 (8), dafman-63-119 (7),
  mil-std-881f (7), faa-std-025 (6), federal-bca (6) = **52 chapters**, plus root-level
  `glossary.md` / `patterns.md` / `cheatsheet.md` support files per pack (included only if the
  pack is essentially single-cluster, per the map's rules of construction).
- Baseline (gap-report §1, cross-checked in 7-GAP_ANALYSIS SC-3): cluster 25 = 0 entries
  (EMPTY, Training & Documentation Delivery), cluster 3 = 2, cluster 5 = 2, cluster 15 = 1.
- Downstream consumer contract (ROLE-AGENTS-REQUIREMENTS-V2 FR-2.1/2.3): the generator reads
  **cluster name → list of {pack, chapter}** and re-reads the JSON when packs change. It does
  NOT read notes, metadata, or ordering today; FR-2.3 only requires the data be refreshable.
- tooling/ conventions: stdlib-only, docstring-header + usage, exit non-zero on failure,
  `ROOT = Path(__file__).resolve().parent.parent` (check_release.py style).
- 7-GAP_ANALYSIS routing: Phase 8 must regenerate the map including the 7 new packs, assert
  cluster 25 non-empty and clusters 3/5/15 above critical thresholds vs the inherited baseline.

## 1. Map v2 schema design

**Decision — minimal additive envelope, array of clusters preserved:**

```json
{
  "schema_version": 2,
  "map_version": "1.18.0",
  "generated_on": "2026-08-14",
  "clusters": [
    {
      "name": "Systems Thinking & Fundamentals",
      "chapters": [
        {"pack": "dau-se-guidebook", "chapter": "ch01-introduction.md",
         "note": "SE orientation across the defense acquisition life cycle"}
      ]
    }
  ]
}
```

- Only three new top-level keys; `clusters` / `name` / `chapters` / `pack` / `chapter` / `note`
  are byte-identical in shape to today. This is what FR-2.1 actually reads (cluster name →
  chapters); nothing downstream needs per-entry IDs, cluster numbers, or counts.
- `schema_version` is an int (2), not a string — cheap `map.get("schema_version") == 2` gate.
- `map_version` tracks the release that regenerated the map (v1.17 map implicitly = 1.17.0);
  `generated_on` is ISO date for staleness eyeballing; the gate does not hard-assert it.
- Cluster numbering (1..32) stays in the human `capability-pack-map.md` summary table only —
  the JSON remains name-keyed so inserting clusters never renumbers data. The threshold
  asserts (cluster 25, 3, 5, 15) resolve by NAME via a small lookup table in the gate, not by
  array index.
- **Backward compat**: the old keyless shape remains a valid subset read — a consumer doing
  `data["clusters"]` works unchanged on v2. The only breakage mode is a consumer that asserts
  `set(data.keys()) == {"clusters"}`; the se-agents generator (not yet written; FR-2.1 says
  "source of the mapping at generation time") simply reads v2. Risk: negligible. Note in the
  contract doc: v1 shape deprecated, regenerate consumers to read `schema_version` first.

## 2. Regeneration approach (ponytail)

**Regeneration is an agent pass, not a script.** Chapter→cluster assignment needs judgment
(cross-cutting chapters, "standard's own process definitions go to cluster 30" rule,
single-cluster vs multi-cluster support-file inclusion). Precedent: the 2026-08-16
regeneration was agent-curated and added 68 entries for the 8 v1.17 packs. Those assignments
are NOT reusable here — those packs are already in the map; the 7 GP packs are new and need
fresh classification per the rules of construction in capability-pack-map.md.

The deterministic part is only a validator/gate — `tooling/check_capability_map.py`:

- Loads `docs/capability-pack-map.json`; fails if `schema_version` missing/≠2, or
  `map_version`/`generated_on` missing.
- Staleness vs `packs/`: every pack dir containing `chapters/` (i.e. minus `omg-signpost`,
  `se-standards-signpost`) must appear in ≥1 entry; every referenced `pack`/`chapter` pair
  must exist on disk (catches deleted/renamed chapters).
- Support-file rule: entries ending `(support file)` are legal only for the three known
  filenames; not gate-enforced beyond existence (the single-cluster judgment stays agent-side —
  see Risks).
- Counts: prints per-cluster entry counts and the total; asserts sum of cluster entries ==
  total entries (no double-count bug); asserts by name:
  - Training & Documentation Delivery (25) ≥ 1
  - Requirements Traceability & Allocation (3) ≥ 3 (baseline 2 + 1)
  - Interface Management & ICIDs (5) ≥ 3 (baseline 2 + 1)
  - Opportunity/Benefit Management (15) ≥ 2 (baseline 1 + 1)
- Exit 0/1, stdlib only, ~80 lines, check_release.py header style.
- Idempotence: the gate validates a committed artifact; "idempotent regeneration" means
  re-running the agent pass over unchanged packs produces no diff (guaranteed by judgment +
  gate, not by a script).

**Wiring recommendation: standalone.** check_release.py is a release gate (Phase 9); the map
gate must be runnable in Phase 8 and in the se-agents repo's refresh path without pulling the
whole release suite. Add ONE line to check_release.py §6-adjacent ("SKILLS.md entry count ==
shipped packs") only at Phase 9 if desired: `subprocess`-free — simplest is a §8 bullet
"map gate passes" implemented by importing/running check_capability_map.py's `main()`.
Recommend: keep standalone now, wire into check_release during Phase 9's release-surface plan.

## 3. Phase 8 task sequence

1. **Write `tooling/check_capability_map.py`** (design above). It must PASS against the
   current keyless map? No — it fails on missing schema_version, which is correct: red first,
   green after step 2. Run it to confirm exactly the expected failures (schema + 7 missing
   packs + thresholds).
2. **Agent-regenerate the map**: classify the 7 new packs' 52 chapters into the 32 clusters
   per the map's own rules of construction; include support files only for packs judged
   essentially single-cluster (likely candidates: mil-std-40051 → cluster 25 heavily,
   faa-std-025, federal-bca → cluster 15); add the v2 metadata envelope
   (`schema_version: 2`, `map_version: "1.18.0"`, `generated_on`); update the summary table
   + changelog line in `docs/capability-pack-map.md` to match. Spot-check protocol: for each
   new pack, re-read its SKILL.md When-to-use and confirm every chapter assignment is
   defensible; diff cluster deltas vs the target clusters named in 7-GAP_ANALYSIS.
3. **Gate green**: run check_capability_map.py → PASS (all packs represented, thresholds met).
4. **Document the contract** — recommendation: a section in `docs/PACK-SPEC.md` is tempting,
   but PACK-SPEC governs pack structure, not cross-repo consumption, and the se-agents
   consumer needs a citable standalone artifact. Laziest CORRECT home: a short
   **`docs/capability-map-CONTRACT.md`** (~60 lines): schema (the JSON above), versioning
   rule (schema_version bumps only on breaking shape change; map_version tracks release),
   refresh path (agent pass per rules of construction in capability-pack-map.md → run
   tooling/check_capability_map.py → commit), and the deprecation note for the keyless v1
   shape. Link it from capability-pack-map.md's rules-of-construction block.
5. **Verify SC 1–3** of ROADMAP Phase 8 (metadata present, thresholds, contract documented)
   and hand off to Phase 9.

## 4. Risks

| Risk | Mitigation |
|---|---|
| Agent mis-clusters new chapters (soft misjudgment invisible to the gate) | Spot-check protocol in task 2: per-pack re-read of SKILL.md When-to-use vs assignments; cross-cutting chapters carry the secondary-fit note per the map's own rule; threshold asserts catch the macro outcome (25/3/5/15) even if individual placements drift |
| Gate false-fails on support-file omission rules (multi-cluster packs legitimately omit support files; gate can't know single-cluster-ness) | Gate checks only existence of referenced files + pack coverage — it does NOT require support files to be present or absent; the single-cluster judgment stays in the agent pass and is documented in the rules of construction |
| Downstream breakage of old keyless JSON shape | Additive-only envelope; `data["clusters"]` consumers unchanged; CONTRACT doc marks v1 keyless deprecated and instructs reading `schema_version` first; se-agents generator not yet written (designs against v2 directly) |
| Thresholds encoded by name drift from numbered cluster table | Name-based lookup table in the gate mirrors the summary table names; gate prints counts so a rename fails loudly (name not found → non-zero) |
| Map goes stale again after v1.18 | CONTRACT refresh path + (Phase 9, optional) one check_release bullet invoking the gate keeps staleness visible at release time |
