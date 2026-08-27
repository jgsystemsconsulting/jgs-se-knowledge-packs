# Capability Pack Map — Consumption Contract

Standalone contract for downstream consumers (notably an se-agents generator
repo that binds roles/skills to pack chapters). This document governs
cross-repo consumption of `docs/capability-pack-map.json`. Pack structure is
out of scope (see `docs/PACK-SPEC.md`).

## 1. Schema (v2)

Top-level JSON object:

```json
{
  "schema_version": 2,
  "map_version": "1.20.0",
  "generated_on": "2026-08-27",
  "clusters": [
    {
      "name": "Systems Thinking & Fundamentals",
      "chapters": [
        {
          "pack": "dau-se-guidebook",
          "chapter": "ch01-introduction.md",
          "note": "SE orientation across the defense acquisition life cycle"
        }
      ]
    }
  ]
}
```

| Field | Type | Meaning |
|---|---|---|
| `schema_version` | int | Shape version. Consumers **must** check `schema_version == 2` first. |
| `map_version` | string | Release that last regenerated the map (semver, e.g. `"1.19.1"`). |
| `generated_on` | string | ISO date (`YYYY-MM-DD`) of regeneration. Informational only. |
| `clusters` | array | Ordered list of capability clusters. |
| `clusters[].name` | string | Stable cluster identity (name-keyed, not numbered). |
| `clusters[].chapters` | array | Entries providing depth for that capability. |
| `chapters[].pack` | string | Pack slug under `packs/<pack>/`. |
| `chapters[].chapter` | string | Filename under `chapters/`, or `"<file> (support file)"` for pack-root support files. |
| `chapters[].note` | string | One-line rationale (human; FR-2.1 does not require consumers to read it). |

**Primary consumer read (FR-2.1):** cluster `name` → list of `{pack, chapter}`.
Notes, ordering, and metadata are optional for generation.

## 2. Versioning

- **`schema_version`** bumps only on a **breaking shape change** (renamed/removed
  required fields, changed types, or a non-additive restructuring of
  `clusters`/`chapters`). Envelope *additions* are additive and do **not** bump
  `schema_version`.
- **`map_version`** tracks the knowledge-pack **release** that regenerated the
  map. The implicit pre-envelope (v1) map corresponds to release `1.17.0`.

## 3. Deprecation (v1 keyless shape)

The v1 shape — top level `{"clusters": [...]}` only, with no envelope keys — is
**DEPRECATED**.

- v1 consumers **must** migrate to reading `schema_version` first.
- `data["clusters"]` access continues to work on v2 (additive envelope).
- New generators (se-agents) should target v2 only and refuse unknown
  `schema_version` values.

## 4. Refresh path

When packs change (new pack, new chapter, rename, delete):

1. Run `python tooling/generate_capability_map.py --generated-on YYYY-MM-DD`
   (add `--sync-md` to rewrite the human summary tables). Classification rules
   (`docs/classification-rules.json`) and note overrides
   (`docs/capability-pack-map-note-overrides.json`) are committed inputs; cluster
   assignment and the v2 envelope are produced mechanically by the generator.
2. Run `python tooling/check_capability_map.py` — must exit 0 (envelope,
   pack/chapter staleness vs `packs/`, file existence, uniqueness, thresholds).
3. Commit both `docs/capability-pack-map.json` and `docs/capability-pack-map.md`
   together.

Mechanical regeneration does not require a live agent to assign clusters. Note
overrides remain the human tuning surface: the committed 644-row overrides file
is still a required generator input (the generator fails closed if it is
missing).

The refresh path still runs `python tooling/check_capability_map.py`, and
`python tooling/check_release.py` invokes `check_capability_map.main()` and
`generate_capability_map.main()` with `--check` in-process (local/trusted; CI
does not exec repo Python).

## 5. Threshold table

Minimum entry counts, resolved by **cluster NAME** (never array index). A
rename that leaves the lookup name missing fails the gate loudly.

| Cluster name | Minimum |
|---|---|
| Training & Documentation Delivery | ≥ 1 |
| Requirements Traceability & Allocation | ≥ 3 |
| Interface Management & ICIDs | ≥ 4 |
| Opportunity/Benefit Management | ≥ 2 |
| Decision Analysis & Trade Studies | ≥ 4 |
| Validation | ≥ 4 |
| Integration | ≥ 4 |
| Operations, Maintenance & Disposal | ≥ 4 |

Thresholds guard thin-cluster fattening from the capability-gap baseline; they
are correctness floors for the agent-enablement surface, not upper bounds.

## 6. Live snapshot vs residue

The live committed snapshot is **628+** chapter entries — post-regen **644**
(16 classified chapters, 0 new support-file rows). Older draft counts (e.g. 502)
are obsolete; consumers must read the live JSON. **Cybersecurity & Security
Engineering** (live 69 entries / 10 packs) and **Digital Engineering & Digital
Twins** (live 25 entries / 4 packs) remain **unbound**. Binding those clusters
is se-agents-side work, not a knowledge-packs release gate.

## 7. Chapter basename overlap gate

`python tooling/check_overlap.py` runs on the local release path via
`check_overlap.main()` inside `tooling/check_release.py` (local/trusted; CI
does not exec repo Python).

- **Scan scope:** `packs/*/chapters/*.md` basenames only. Support files at pack
  root (`glossary.md`, `patterns.md`, `cheatsheet.md`, `SKILL.md`, `PACK.yaml`)
  are out of scope because they are not under `chapters/`.
- **Threshold:** zero un-whitelisted multi-pack chapter basename collisions.
  Any basename shared by two or more packs and absent from WHITELIST fails the
  gate.
- **WHITELIST:** currently contains `ch01-introduction.md` because three
  distinct source packs legitimately share that canonical topic
  (`dau-se-guidebook`, `nasa-npr-7123`, `nasa-system-safety`). Adding a new
  shared basename requires an explicit WHITELIST edit in
  `tooling/check_overlap.py`, not a silent pass.

## 8. FUT-05 residual (note overrides only)

Cluster assignment and mechanical envelope fields (`schema_version`,
`map_version`, `generated_on`, ordered `clusters`) are produced by the committed
generator `tooling/generate_capability_map.py` from
`docs/classification-rules.json` plus
`docs/capability-pack-map-note-overrides.json`.

The remaining human input is the committed 644-row note-overrides file (one
note per live chapter). Envelope, staleness, uniqueness, and threshold gates
stay mechanical in `tooling/check_capability_map.py` and
`tooling/check_classification_rules.py`.
