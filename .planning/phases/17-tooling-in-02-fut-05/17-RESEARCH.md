# Phase 17: Tooling (IN-02 + FUT-05) - Research

**Researched:** 2026-08-20
**Domain:** Release tooling (overlap collision detection + deterministic capability-map generation)
**Confidence:** HIGH

## Summary

Release gate (`check_release.py`) already imports `check_capability_map` in-process and fails on non-zero. Overlap detection (TOOL-20-01/02) adds a minimal stdlib chapter-basename collision check under `tooling/`. Single observed collision (`ch01-introduction.md` across 3 packs) is intentional (different sources, same canonical topic) — gate must treat it as non-fatal or whitelist. FUT-05 (TOOL-20-03) is already partially satisfied by `check_capability_map.py` uniqueness + staleness rules; full byte-stable regen from committed inputs only is not feasible without reintroducing agent judgment for cluster assignment and notes. Honest residual documented in CONTRACT.

**Primary recommendation:** Add `check_overlap.py` (stdlib, ~60 LOC) that scans `packs/*/chapters/*.md` basenames, reports collisions, exits 0 on clean or on whitelist, non-zero on un-whitelisted duplicates. Wire as step 5d in `check_release.py` before map check. FUT-05: keep current mechanical gate + document residual agent procedure.

## User Constraints (from CONTEXT.md)

No CONTEXT.md present for this phase — no locked decisions or discretion areas.

## Architectural Responsibility Map

| Capability | Primary Tier | Secondary Tier | Rationale |
|------------|-------------|----------------|-----------|
| Overlap collision detection | Tooling (Python stdlib) | — | Pure filesystem scan; no runtime state |
| Capability map validation | Tooling (Python stdlib) | — | Already implemented in check_capability_map.py |
| Release gate composition | Tooling orchestration | — | check_release.py already imports and calls map checker |

## Standard Stack

### Core
| Library | Version | Purpose | Why Standard |
|---------|---------|---------|--------------|
| Python 3 stdlib | 3.11+ | pathlib, json, re, sys | Zero new dependencies; repo policy |

### Supporting
| Library | Version | Purpose | When to Use |
|---------|---------|---------|-------------|
| PyYAML (optional) | — | PACK.yaml parse | Only if chapter metadata needed beyond basename |

### Alternatives Considered
| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| stdlib pathlib | os.walk | More verbose, same result |

**Installation:** None (stdlib only).

## Package Legitimacy Audit

No external packages. All checks use Python stdlib already present in repo.

## Architecture Patterns

### Recommended Project Structure
```
tooling/
├── check_release.py          # existing orchestrator
├── check_capability_map.py   # existing map validator
├── check_overlap.py          # NEW minimal collision detector
└── validate_pack.py
```

### Pattern 1: Gate Composition (existing)
**What:** `check_release.py` imports sibling modules and calls `main()`; aggregates errors; exits 1 on any failure.
**When to use:** Adding new mechanical checks to release path.
**Example:**
```python
# Source: tooling/check_release.py:216-222 [VERIFIED: tooling/check_release.py:216-222]
try:
    import check_capability_map
    rc = check_capability_map.main()
    if rc != 0:
        fail(errs, "[map] check_capability_map.py failed")
except Exception as e:
    fail(errs, f"[map] check_capability_map failed to run: {e}")
```

### Anti-Patterns to Avoid
- **Hand-rolled framework:** No pytest, click, typer — repo uses raw `if __name__ == "__main__": sys.exit(main())`.

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| Chapter collision detection | Custom DB or hash index | `pathlib.rglob` + `dict.setdefault` | 5-line scan is sufficient and deterministic |
| Map regeneration | Full agent re-classification | Existing `check_capability_map` uniqueness gate | Mechanical slice already prevents duplicates; residual cluster assignment requires judgment |

**Key insight:** One observed basename collision is semantically correct (different source packs covering same topic). Gate must not false-fail on it.

## Common Pitfalls

### Pitfall 1: False collision on canonical chapter names
**What goes wrong:** Gate reports `ch01-introduction.md` duplicate and blocks release.
**Why it happens:** Multiple authoritative sources legitimately name their intro chapter identically.
**How to avoid:** Whitelist known-good duplicates or gate only on "same pack" collisions (none exist).
**Warning signs:** Gate fails on clean repo state.

## Code Examples

### Overlap Check Skeleton (stdlib)
```python
# Source: proposed tooling/check_overlap.py
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent

def main() -> int:
    chaps: dict[str, list[str]] = {}
    for p in (ROOT / "packs").rglob("chapters/*.md"):
        chaps.setdefault(p.name, []).append(p.parent.parent.name)
    dups = {k: v for k, v in chaps.items() if len(v) > 1}
    if not dups:
        print("OVERLAP: PASS — no chapter basename collisions")
        return 0
    # whitelist logic here (e.g., ch01-introduction.md across 3 packs)
    print(f"OVERLAP: {len(dups)} collision(s)")
    for name, packs in dups.items():
        print(f"  {name}: {packs}")
    return 1  # or 0 if all whitelisted

if __name__ == "__main__":
    sys.exit(main())
```

## State of the Art

Current map already enforces:
- `(pack, chapter)` uniqueness across clusters
- Bidirectional pack/chapter staleness
- Support-file rows distinguished by ` (support file)` suffix
- Name-keyed thresholds (no index fragility)

FUT-05 mechanical slice is therefore already delivered; residual is honest agent classification documented in CONTRACT.

## Assumptions Log

None — all claims verified by direct file reads and command execution this session.

## Sources

### Primary (HIGH confidence)
- `tooling/check_release.py:1-253` — gate composition and map invocation [VERIFIED: tooling/check_release.py:216-222]
- `tooling/check_capability_map.py:1-254` — uniqueness, staleness, threshold logic [VERIFIED: tooling/check_capability_map.py:143-150,168-197]
- `docs/capability-pack-map.json:1-80` — v2 envelope + sample entries [VERIFIED: docs/capability-pack-map.json:1-4]
- `docs/capability-map-CONTRACT.md:1-100` — consumption rules and refresh path [VERIFIED: docs/capability-map-CONTRACT.md:66-83]

### Secondary (MEDIUM confidence)
- PACK.yaml samples — chapter metadata is minimal; basename collision is the only mechanical signal

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH — stdlib only, verified by execution
- Architecture: HIGH — direct reads of gate and map checker
- Pitfalls: HIGH — single collision observed and explained

**Research date:** 2026-08-20
**Valid until:** 30 days (stable tooling domain)