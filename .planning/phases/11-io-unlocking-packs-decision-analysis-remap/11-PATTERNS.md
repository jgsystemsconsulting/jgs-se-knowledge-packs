# Phase 11: IO-unlocking packs + Decision Analysis remap - Pattern Map

**Mapped:** 2026-08-17
**Files analyzed:** 3 new packs + 1 extend + remap spec + deferral records
**Analogs found:** 4 / 4

## File Classification

| New/Modified File | Role | Data Flow | Closest Analog | Match Quality |
|-------------------|------|-----------|----------------|---------------|
| `packs/nasa-std-8719-14/**` | pack (new) | CRUD (extract→scaffold→generate) | `packs/nasa-ms-7009/**` | exact |
| `packs/is-gps-200n/**` | pack (new, exemplar) | CRUD (extract→scaffold→generate) | `packs/faa-std-025/**` | role-match |
| `packs/dod-vva-rpg/**` | pack (extend chapters) | CRUD (per-chapter add) | `packs/dod-vva-rpg/**` (self) + `packs/federal-bca/**` (dual-source) | exact |
| IO-01 remap table (in SUMMARY) | specification | transform (map source) | `packs/federal-bca/**` (A-94 remap source) | role-match |

## Pattern Assignments

### `packs/nasa-std-8719-14/**` (pack, new, IO-03)

**Analog:** `packs/nasa-ms-7009/**`

**Imports / metadata pattern** (PACK.yaml lines 1-14):
```
slug: nasa-std-8719-14
title: "Process for Limiting Orbital Debris (NASA-STD-8719.14C)"
publisher: "NASA"
source_version: "NASA-STD-8719.14C (Approved 2021-11-05)"
license: "Public Domain (US Government work, 17 U.S.C. § 105)"
license_tier: 1
commercial_use: true
share_alike: false
attribution_required: false
build:
  method: "jgs-reference-skill extraction + offset-mapped parallel chapter generation"
  source_pages: 77
  chapters: 6
  built_on: "2026-08-17"
```

**SKILL.md contract pattern** (SKILL.md lines 11-14):
```
## When to use
Reach for this pack when ...
**Prerequisites:** none — plain Markdown; no MCP server, API key, or licence tier needed at runtime.
```

**LICENSE pattern** (LICENSE lines 1-23):
```
nasa-std-8719-14 pack — content licence
===================================
This pack is derived from:
    NASA Technical Standard NASA-STD-8719.14C — Process for Limiting Orbital Debris
      Approved: 2021-11-05 (Office of Safety and Mission Assurance)
Source licence: Public Domain (US Government work, 17 U.S.C. § 105)  (tier 1)
No source-material download link is published (see ../../docs/LICENSING.md).
...
NOTE: This file governs the CONTENT of this pack. The repository tooling is licensed
separately under MIT (see ../../LICENSE).
```

**P11-PRE-1 gate (notes in PACK.yaml):** third-party insert scan quote recorded verbatim.

---

### `packs/is-gps-200n/**` (pack, new exemplar, IO-04)

**Analog:** `packs/faa-std-025/**`

**SKILL.md Scope & Limits cross-reference pattern** (faa-std-025/SKILL.md line 88):
```
## Scope & Limits
This pack is a worked ICD/IS using IS-GPS-200N as the exemplar. It complements
`faa-std-025` (preparation rules) — do not use this pack for IRD/ICD authoring
guidance; route to faa-std-025 for that. See also: faa-std-025.
```

**DIST-A licence string** (PACK.yaml + LICENSE):
```
license: "Public Domain (US Government work, 17 U.S.C. § 105; Distribution Statement A — Approved for public release; distribution is unlimited)"
```

**P11-PRE-2 gate (notes in PACK.yaml):** DIST-A sentence re-confirmed on extracted copy; SAIC contractor line recorded as watch-item only.

**Chapter strategy:** Select §§1–3 + §6 + short "how appendices work" chapter. Skip App II–IV transcription.

---

### `packs/dod-vva-rpg/**` (pack, extend chapters, IO-02)

**Analog:** self (existing `dod-vva-rpg`) + `packs/federal-bca/**` (dual-source pattern)

**Extend pattern (no scaffold):** `build_pack.py` refuses existing slug. Add `chapters/chNN-*.md`, update SKILL.md Chapter/Topic Index, bump PACK.yaml `build.chapters` / `source_pages` (sum) / notes provenance (title + retrieved date, no URL).

**Per-chapter gate (P7-PRE-4):** VET each new PDF; chars/page ≥ 300; provenance line in notes; overlap run against new full_text only.

**No new pack:** Do not create `dodm-5000-102`. IO-02 = leftover RPG chapters only.

---

### IO-01 remap specification (no pack, Phase 12 apply)

**Analog:** `packs/federal-bca/**` (A-94 source for Opportunity/Benefit cluster)

**Remap table pattern** (write to SUMMARY; apply in Phase 12 MAP-19-03):
```
| Pack | Chapter | From (today) | To | Why |
| federal-bca | ch06-reporting-and-decision-use.md | Opportunity/Benefit | Decision Analysis & Trade Studies | Decision-use / OMB-facing choice documentation |
| federal-bca | ch04-uncertainty-and-sensitivity.md | Opportunity/Benefit | Decision Analysis & Trade Studies | Uncertainty/sensitivity is the A-94 decision-analysis method spine |
| dod-vva-rpg | ch06-accreditation-agent-role.md | Assurance & System Assurance | Decision Analysis & Trade Studies | Accreditation is the authority decision |
```
Result target: Decision Analysis 2 → 5 entries, 2 → 4 packs. Do not edit `docs/capability-pack-map.json` in Phase 11.

---

## Shared Patterns

### Authentication / licence tier
**Source:** All Tier-1 packs (`nasa-ms-7009`, `faa-std-025`)
**Apply to:** All new packs
```
license_tier: 1
commercial_use: true
share_alike: false
attribution_required: false
```

### Error / provenance handling
**Source:** PACK.yaml `notes` field (nasa-ms-7009 lines 15-28)
**Apply to:** All packs
```
notes: >
  US Government work -- public domain (17 U.S.C. § 105); no copyright...
  Extraction used pdftotext fallback...
  scan_generated_skill reviewed at build.
change_indication: "reconstructed as synthesized reference notes"
```

### Validation gate chain
**Source:** 7-01-PLAN.md Task 1 verify block
**Apply to:** All new/extended packs
```
python tooling/validate_pack.py packs/$SLUG
python "$REF/tools/check_overlap.py" --source "$WRK/..." --pack packs/$SLUG
python "$REF/tools/scan_generated_skill.py" packs/$SLUG
grep -c "^## When to use" packs/$SLUG/SKILL.md
grep -c "^\*\*Prerequisites:\*\*" packs/$SLUG/SKILL.md
! grep -qi "TODO" packs/$SLUG/PACK.yaml
[ -z "$(git show --name-only --pretty=format: HEAD | grep -E 'sources/|full_text.txt')" ]
```

### SKILL.md contract (RR-S-13 / SC-5)
**Source:** docs/PACK-SPEC.md lines 33-34 + all shipped packs
**Apply to:** Every non-signpost pack
```
## When to use
...
**Prerequisites:** none — plain Markdown; no MCP server, API key, or licence tier needed at runtime.
```

## No Analog Found

| File | Role | Data Flow | Reason |
|------|------|-----------|--------|
| IO-05/06 deferral records | specification | transform | Honest deferral pattern (Phase 10 FUT-04) is in REQUIREMENTS/STATE only; no pack tree |
| IO-07 accept record | specification | transform | Same — recorded outcome only, no pack |

## Metadata

**Analog search scope:** packs/nasa-ms-7009, packs/faa-std-025, packs/dod-vva-rpg, packs/federal-bca, docs/PACK-SPEC.md, tooling/*.py, .planning/phases/7-gap-driven-pack-builds/7-01-PLAN.md
**Files scanned:** 4 packs + 3 tooling + 2 planning docs
**Pattern extraction date:** 2026-08-17
