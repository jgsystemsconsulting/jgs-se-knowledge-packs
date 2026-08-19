# Phase 10: Source Vetting - Pattern Map

**Mapped:** 2026-08-17
**Files analyzed:** 4
**Analogs found:** 4 / 4

## File Classification

| New/Modified File | Role | Data Flow | Closest Analog | Match Quality |
|-------------------|------|-----------|----------------|---------------|
| `docs/SOURCE-VETTING.md` | documentation (integrity register) | CRUD (add dated rows + pointer) | `docs/SOURCE-VETTING.md` (Phase 6 v1.18 update) | exact |
| `.planning/REQUIREMENTS.md` | config/requirements | CRUD (checkbox notes + descope) | `.planning/REQUIREMENTS.md` (Phase 6 Task 3) | exact |
| `.planning/STATE.md` | config/state | CRUD (deviation notes) | `.planning/STATE.md` (Phase 6 Task 4) | exact |
| `.planning/ROADMAP.md` | documentation (milestone planning) | CRUD (phase goal/requirements text) | `.planning/ROADMAP.md` (Phase 6 Task 4) | exact |

## Pattern Assignments

### `docs/SOURCE-VETTING.md` (documentation, CRUD)

**Analog:** Phase 6 execution (`6-01-PLAN.md` Tasks 1–2) + existing v1.18 section in the file itself

**Imports / structure pattern** (lines 115–139 of current file):
```
### Vetted candidates (v1.18.0) — statute-basis; confirm in-source at build

Source URLs for all vetted/excluded candidates are recorded in
`.planning/phases/6-source-vetting-unverified-resolution/6-RESEARCH.md` (Link Policy: never
published in docs or packs).
```

**Core write-up pattern** (Task 1 action in 6-01-PLAN.md):
- Insert new `### Vetted candidates (v1.19.0)` section immediately after the v1.18 section
- Same table format: `| Source | Tier | Licence evidence |`
- Each row ends with `(Verified YYYY-MM-DD.)` date stamp
- Open with pointer paragraph naming `10-RESEARCH.md` as the URL store
- No http/https strings anywhere (Link Policy gate: `grep -c http` expects 0)
- Excluded/pending rows appended to the existing Excluded table using the same `| **Source** | Why excluded |` format with date stamp

**Error / consistency handling** (Task 5):
```
test "$(grep -c 'http' docs/SOURCE-VETTING.md)" = "0"
test "$(grep -c 'Verified 2026-08-17' docs/SOURCE-VETTING.md)" -ge N
```

### `.planning/REQUIREMENTS.md` (config, CRUD)

**Analog:** Phase 6 Task 3

**Core pattern** (scoped Edits only):
- Append notes to existing VET-/IO- rows rather than rewriting
- Strike-through for descoped items: `- [ ] ~~**GP-08** ...~~ — DESCOPED ...`
- Add row to "Out of Scope" table when a candidate is removed
- Never check the VET-19 checkboxes in this phase (they stay open until verify)

**Example excerpt from analog**:
```
GP-08 — change the checkbox line to struck-through ... and add a row to the v1.18 "Out of Scope" table
```

### `.planning/STATE.md` (config, CRUD)

**Analog:** Phase 6 Task 4

**Core pattern**:
- Update the "Packs shipped" target line to reflect new count
- Append a single "Deviations/Notes" bullet dated for the phase (e.g., "Phase 10 (2026-08-17): ... verdicts in 10-RESEARCH.md")
- Do not touch frontmatter progress fields

### `.planning/ROADMAP.md` (documentation, CRUD)

**Analog:** Phase 6 Task 4

**Core pattern**:
- Update Phase N Goal/Requirements lines to match the actual number of packs that will be built
- Change overview bullet to list the exact GP tokens that survived vetting
- Add parenthetical "(GP-08 descoped ...)" style rationale when needed
- Keep Success Criteria wording intact unless it references a now-invalid pack count

## Shared Patterns

### Link Policy (zero source URLs in published docs)
**Source:** `docs/SOURCE-VETTING.md:194-197` and Phase 6 Task 5
**Apply to:** All edits of `docs/SOURCE-VETTING.md`
```
test "$(grep -c 'http' docs/SOURCE-VETTING.md)" = "0"
# 17 U.S.C. § 105 is plain text, not a URL
```

### Pointer paragraph to RESEARCH store
**Source:** `docs/SOURCE-VETTING.md:117-119` (v1.18 section)
**Apply to:** New v1.19 section and any Excluded/pending rows
```
Source URLs for all vetted/excluded/UNVERIFIED candidates are recorded in
`.planning/phases/10-source-vetting/10-RESEARCH.md` (Link Policy: never
published in docs or packs).
```

### Honest deferral / Excluded-pending wording
**Source:** `docs/SOURCE-VETTING.md:85` (AAF row) + RESEARCH.md Pattern 2
**Apply to:** Army CBA, DoDM 5000.102, AAF rows
```
AAF guidebooks are the intended substitute but are NOT yet vetted — licence spot-check deferred ... vet before any future use
```

### Dated row convention
**Source:** Phase 6 must_haves + Task 1
**Apply to:** Every new Vetted or Excluded row
```
... (Verified 2026-08-17.)
```

## No Analog Found

None. All four files have exact role + data-flow matches in the Phase 6 execution.

## Metadata

**Analog search scope:** `.planning/phases/6-source-vetting-unverified-resolution/`, `docs/SOURCE-VETTING.md`, `.planning/REQUIREMENTS.md`, `.planning/STATE.md`, `.planning/ROADMAP.md`
**Files scanned:** 5
**Pattern extraction date:** 2026-08-17
**Key constraint observed:** This phase is documentation-only; no `packs/` directories or source URLs may appear in the edited files.