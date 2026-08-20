# Phase 17: Tooling Patterns (IN-02 + FUT-05)

**Researched:** 2026-08-20
**Domain:** Minimal stdlib release tooling patterns

## Overlap Detection Pattern

**Problem:** Detect multi-pack chapter collisions that matter for release without false positives on intentional canonical names.

**Solution:** Basename-only scan with explicit whitelist for known-good duplicates.

```python
# tooling/check_overlap.py (proposed)
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
WHITELIST = {"ch01-introduction.md"}  # intentional cross-pack canonical topics

def main() -> int:
    chaps: dict[str, list[str]] = {}
    for p in (ROOT / "packs").rglob("chapters/*.md"):
        chaps.setdefault(p.name, []).append(p.parent.parent.name)
    dups = {k: v for k, v in chaps.items() if len(v) > 1 and k not in WHITELIST}
    if not dups:
        print("OVERLAP: PASS")
        return 0
    print(f"OVERLAP FAIL: {len(dups)} un-whitelisted collision(s)")
    for name, packs in dups.items():
        print(f"  {name}: {packs}")
    return 1

if __name__ == "__main__":
    sys.exit(main())
```

**Why it works:** 5-line scan, deterministic, no new deps. Whitelist keeps release unblocked on correct data.

## Gate Wiring Pattern (existing, extend)

See `check_release.py:216-222` — import sibling checker, call `main()`, fail on non-zero.

## FUT-05 Honesty Pattern

Mechanical slice (uniqueness + staleness + thresholds) already complete in `check_capability_map.py`. Full byte-stable regeneration from committed inputs alone is impossible without reintroducing agent judgment for cluster assignment and `note` fields. Document residual procedure in CONTRACT; do not claim full automation.

## Ponytail Constraints Applied

- Stdlib only (pathlib + dict)
- 1 new file max (`check_overlap.py`)
- No frameworks, no YAML parse unless strictly needed
- Existing collision treated as feature, not bug

## Test Approach (tiny assert demo)

```python
# tests/test_overlap.py (optional, Wave 0)
def test_no_false_positive_on_intentional_intro():
    # ch01-introduction.md appears in 3 packs — must be whitelisted
    assert "ch01-introduction.md" in WHITELIST
```

**Execution:** `python tooling/check_overlap.py` must exit 0 on current repo state.