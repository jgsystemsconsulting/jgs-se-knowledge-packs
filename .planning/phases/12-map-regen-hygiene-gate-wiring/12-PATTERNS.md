# Phase 12: Map regen + hygiene + gate wiring - Pattern Map

**Mapped:** 2026-08-17
**Files analyzed:** 12
**Analogs found:** 12 / 12

## File Classification

| New/Modified File | Role | Data Flow | Closest Analog | Match Quality |
|-------------------|------|-----------|----------------|---------------|
| `docs/capability-pack-map.json` | data artifact | transform | Phase 8 agent regen (8-01-PLAN.md Task 2) | exact |
| `docs/capability-pack-map.md` | documentation | transform | Phase 8 md sync (8-01-PLAN.md Task 2) | exact |
| `docs/capability-map-CONTRACT.md` | documentation | request-response | existing CONTRACT.md + Phase 8 contract write | exact |
| `tooling/check_capability_map.py` | utility | request-response | self (current file) + Phase 8 gate creation | exact |
| `tooling/check_release.py` | utility | request-response | self (current file lines 119-129) | exact |
| `CHANGELOG.md` | documentation | transform | existing CHANGELOG.md (BOM + LF hygiene) | exact |
| `.gitattributes` | config | file-I/O | new file (HYG-01 pattern) | none (new) |
| `packs/mil-std-881f/SKILL.md` | component | transform | existing SKILL.md (HYG-02 alpha sort) | role-match |
| `packs/dafman-63-119/SKILL.md` | component | transform | existing SKILL.md (HYG-02 alpha sort) | role-match |
| `packs/mil-std-40051/SKILL.md` | component | transform | existing SKILL.md (HYG-02 circular target) | role-match |
| `packs/federal-bca/SKILL.md` | component | transform | existing SKILL.md (HYG-02 label) | role-match |
| `packs/federal-bca/PACK.yaml` | config | transform | existing PACK.yaml (HYG-04 wording) | role-match |

## Pattern Assignments

### `docs/capability-pack-map.json` (data artifact, transform)

**Analog:** Phase 8 agent classification (8-01-PLAN.md Task 2) + live v2 envelope

**Core pattern** (from 12-RESEARCH.md §Pattern 1 and 8-01-PLAN.md Task 2):
- Agent pass (no generator): classify 16 new chapters + apply MAP-19-03 three-row MOVE (delete old rows, never copy).
- Preserve `schema_version: 2`, `map_version: "1.18.0"`, update only `generated_on`.
- Omit support-file rows for multi-cluster new packs (`nasa-std-8719-14`, `is-gps-200n`).
- After regen: 644 entries, 63 chapter-bearing packs; DA = 5/4.

**Envelope pattern** (docs/capability-pack-map.json:1-4):
```json
{
  "schema_version": 2,
  "map_version": "1.18.0",
  "generated_on": "2026-08-17",
  "clusters": [...]
}
```

### `docs/capability-pack-map.md` (documentation, transform)

**Analog:** Phase 8 md sync (8-01-PLAN.md Task 2)

**Core pattern:** After JSON regen, refresh summary table counts + one changelog bullet (new slugs + remap + leftover RPG). Keep single-line convention.

### `docs/capability-map-CONTRACT.md` (documentation, request-response)

**Analog:** existing CONTRACT.md + Phase 8 contract write (8-01-PLAN.md Task 4)

**Core pattern** (MAP-19-05 paragraph):
- One paragraph: live snapshot 628+ (post-regen 644); 502 is residue; Cybersecurity (69/10) + Digital Engineering (25/4) remain unbound — binding is se-agents-side.
- Update §4 "standalone" sentence after wire.

### `tooling/check_capability_map.py` (utility, request-response)

**Analog:** self (current file) + Phase 8 gate creation (8-01-PLAN.md Task 1)

**Imports / header pattern** (lines 1-17):
```python
#!/usr/bin/env python3
# Copyright (c) 2026 JG Systems Consulting Ltd. — MIT License (see LICENSE).
# SPDX-License-Identifier: MIT
"""
check_capability_map.py — validate docs/capability-pack-map.json for agent consumption.
...
stdlib only. Standalone — not imported by check_release.py (Phase 9 may wire it).
"""
```

**THRESHOLDS pattern** (lines 34-39) — name-keyed, extend for MAP-19-02:
```python
THRESHOLDS: dict[str, int] = {
    "Training & Documentation Delivery": 1,
    "Requirements Traceability & Allocation": 3,
    "Interface Management & ICIDs": 3,
    "Opportunity/Benefit Management": 2,
    # MAP-19-02 additions (name-keyed):
    "Decision Analysis & Trade Studies": 4,
    "Validation": 4,
    "Integration": 4,
    "Operations, Maintenance & Disposal": 4,
}
```

**main() return pattern** (lines 238-245):
```python
if errs:
    print(f"FAIL: {len(errs)} issue(s)")
    ...
    return 1
print("PASS: capability map OK")
return 0
```

### `tooling/check_release.py` (utility, request-response)

**Analog:** self (current file lines 119-129)

**Wire pattern** (MAP-19-04, after pack validate block):
```python
sys.path.insert(0, str(ROOT / "tooling"))
try:
    import validate_pack  # type: ignore
    ...
    import check_capability_map  # type: ignore
    rc = check_capability_map.main()
    if rc != 0:
        fail(errs, "[map] check_capability_map.py failed (see output above)")
except Exception as e:
    fail(errs, f"[map] check_capability_map failed to run: {e}")
```

### `CHANGELOG.md` (documentation, transform)

**Analog:** existing CHANGELOG.md first bytes + HYG-01

**Hygiene pattern:**
- Strip UTF-8 BOM (ef bb bf).
- Normalize entire file to LF only.
- Do NOT add `## [1.19.0]` section (Phase 13 fence).

### `.gitattributes` (config, file-I/O)

**Analog:** new file (HYG-01 pattern from 12-RESEARCH.md)

**Content:**
```
*.md text eol=lf
```

### Four SKILL.md files + federal-bca/PACK.yaml (component/config, transform)

**Analog:** existing SKILL.md / PACK.yaml files + HYG-02/04 exact line fixes from 12-RESEARCH.md

**HYG-02 fixes (exact lines):**
- `packs/mil-std-881f/SKILL.md:89` — move "PM / measurement / EVMS mapping" into alpha order.
- `packs/dafman-63-119/SKILL.md:64-65` — move "AFOTEC / …" before "Agile / …".
- `packs/mil-std-40051/SKILL.md:77` — drop ", Topic Index" from circular target.
- `packs/federal-bca/SKILL.md:74` — rename "Opportunity/Benefit Analysis" → "Opportunity cost / benefit identification".

**HYG-04 fix:**
- `packs/federal-bca/PACK.yaml:20` — reword "(c)" claim to note literal enumeration markers.

After edits: `python tooling/validate_pack.py` on the four slugs.

## Shared Patterns

### Agent classification + gate (MAP-19-01/02/03)
**Source:** Phase 8 (8-01-PLAN.md) + 12-RESEARCH.md Pattern 1-3
**Apply to:** map.json regen, check_capability_map.py THRESHOLDS, CONTRACT paragraph
- One agent pass does classification + remap move + floor thresholds.
- Gate must be GREEN before wire.
- Name-keyed THRESHOLDS only; one-shot verify print for the `<4 AND 1 pack` conjunct.

### Import-not-subprocess wire (MAP-19-04)
**Source:** check_release.py:119-129 (validate_pack + gen_packs_page)
**Apply to:** check_release.py + CONTRACT §4 update
- `sys.path.insert(0, str(ROOT / "tooling"))`; `import X; rc = X.main()`; fail on non-zero.
- No subprocess, no CI step, no version bump.

### Hygiene file edits (HYG-01..04)
**Source:** 12-RESEARCH.md §Pattern 5 + exact line numbers
**Apply to:** CHANGELOG, .gitattributes, four SKILL.md, one PACK.yaml
- Record-only for HYG-03 (external PR) if sibling not writable.

## No Analog Found

None. All files have direct Phase 8 or self analogs.

## Metadata

**Analog search scope:** .planning/phases/8-*/**, tooling/*.py, docs/capability-*.md, packs/*/SKILL.md, packs/federal-bca/PACK.yaml
**Files scanned:** 12 (all required)
**Pattern extraction date:** 2026-08-17

---

**Ready for planning.** Planner can reference Phase 8 tasks + exact line excerpts above.