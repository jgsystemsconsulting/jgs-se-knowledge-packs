# Phase 15: Source Retries - Pattern Map

**Mapped:** 2026-08-20
**Files analyzed:** 4
**Analogs found:** 4 / 4

## File Classification

| New/Modified File | Role | Data Flow | Closest Analog | Match Quality |
|-------------------|------|-----------|----------------|---------------|
| `docs/SOURCE-VETTING.md` | documentation (integrity register) | CRUD (add dated retry rows + pointer) | `docs/SOURCE-VETTING.md` (Phase 10 v1.19 update) | exact |
| `.planning/REQUIREMENTS.md` | config/requirements | CRUD (checkbox notes + descope) | `.planning/REQUIREMENTS.md` (Phase 10 Task 3) | exact |
| `.planning/STATE.md` | config/state | CRUD (deviation notes) | `.planning/STATE.md` (Phase 10 Task 4) | exact |
| `.planning/ROADMAP.md` | documentation (milestone planning) | CRUD (phase goal/requirements text) | `.planning/ROADMAP.md` (Phase 10 Task 4) | exact |

## Pattern Assignments

### `docs/SOURCE-VETTING.md` (documentation, CRUD)

**Analog:** Phase 10 execution + existing v1.19 section in the file itself

**Core write-up pattern**:
- Insert new `### Vetted candidates (v1.19.0 retry)` section immediately after the v1.19 section
- Same table format: `| Source | Tier | Licence evidence |`
- Each row ends with `(Verified YYYY-MM-DD.)` date stamp
- Open with pointer paragraph naming `15-RESEARCH.md` as the URL store
- No http/https strings anywhere (Link Policy gate)
- Excluded/pending rows appended to the existing Excluded table using the same `| **Source** | Why excluded |` format with date stamp
- For Army CBA / AAF / ROSAP / faa-std-025: record "still NOT yet vetted" + pointer to 15-RESEARCH.md section if no in-source redistribution grant found

**Error / consistency handling**:
```
test "$(grep -c 'http' docs/SOURCE-VETTING.md)" = "0"
test "$(grep -c 'Verified 2026-08-20' docs/SOURCE-VETTING.md)" -ge N
```

### `.planning/REQUIREMENTS.md` (config, CRUD)

**Analog:** Phase 10 Task 3
**Core pattern**:
- Append notes to existing VET-20-01 / VET-20-02 / VET-20-03 rows rather than rewriting
- Strike-through for descoped items if needed
- Add row to "Out of Scope" table when a candidate is removed
- Never check the VET-20 checkboxes in this phase (they stay open until verify)

### `.planning/STATE.md` (config, CRUD)

**Analog:** Phase 10 Task 4
**Core pattern**:
- Append a single "Deviations/Notes" bullet dated for the phase (e.g., "Phase 15 (2026-08-20): Army CBA / AAF / ROSAP / faa-std-025 retry verdicts in 15-RESEARCH.md")
- Do not touch frontmatter progress fields

### `.planning/ROADMAP.md` (documentation, CRUD)

**Analog:** Phase 10 Task 4
**Core pattern**:
- Update Phase 15 Goal/Requirements lines to match actual number of packs
- Add parenthetical "(AAF descoped ...)" style rationale when needed
- Keep Success Criteria wording intact unless it references a now-invalid pack count

## Shared Patterns

### Link Policy (zero source URLs in published docs)
**Source:** `docs/SOURCE-VETTING.md:194-197` and Phase 10 Task 5
**Apply to:** All edits of `docs/SOURCE-VETTING.md`
```
test "$(grep -c 'http' docs/SOURCE-VETTING.md)" = "0"
```

### Pointer paragraph to RESEARCH store
**Source:** `docs/SOURCE-VETTING.md:117-119` (v1.18/19 sections)
**Apply to:** New v1.19 retry section and any Excluded/pending rows
```
Source URLs for all vetted/excluded/UNVERIFIED candidates are recorded in
`.planning/phases/15-source-retries/15-RESEARCH.md` (Link Policy: never
published in docs or packs).
```

### Honest deferral / Excluded-pending wording
**Source:** `docs/SOURCE-VETTING.md:85` (AAF row) + 10-RESEARCH.md
**Apply to:** Army CBA, AAF, ROSAP, faa-std-025 rows
```
AAF guidebooks are the intended substitute but are NOT yet vetted — licence spot-check deferred ... vet before any future use (15-RESEARCH.md §AAF).
```

### Dated row convention
**Source:** Phase 10 must_haves + Task 1
**Apply to:** Every new Vetted or Excluded row
```
... (Verified 2026-08-20.)
```

## No Analog Found

None. All four files have exact role + data-flow matches in the Phase 10 execution.

## Metadata

**Analog search scope:** `.planning/phases/10-source-vetting/`, `docs/SOURCE-VETTING.md`, `.planning/REQUIREMENTS.md`, `.planning/STATE.md`, `.planning/ROADMAP.md`
**Files scanned:** 5
**Pattern extraction date:** 2026-08-20
**Key constraint observed:** This phase is documentation-only; no `packs/` directories or source URLs may appear in the edited files. Every carried source must have dated evidence; AAF and Army CBA unused unless in-source redistribution grant quoted.
