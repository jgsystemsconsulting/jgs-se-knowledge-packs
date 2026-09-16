# Catalog Live-Set Parity (P16) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Date:** 2026-09-16

**Goal:** Align `catalog.json` metadata to the staged release date, and fail-closed when the live catalog slug set drifts from content `packs/*` (signposts excluded from catalog).

**Architecture:** Filesystem inventory of `packs/*/SKILL.md` yields content and signpost slug sets (same `kind: signpost` rule as P15). `catalog.packs` live slugs (status `live` or absent) must equal the content set both ways. Signpost slugs must not appear in `catalog.packs`. Check 14 lives in `tooling/check_release.py`; CI inlines a stdlib twin; probes cover parsers and parity pins.

**Tech Stack:** Python 3 stdlib only.

**Spec:** docs/superpowers/specs/2026-09-16-catalog-live-set-parity.md

**Research:** research: skipped (in-repo catalogue honesty; no external API)

## Global Constraints

- Live slugs from filesystem only; never hardcode the set size inside check 14.
- Signpost detection: after opening `---`, a line matching `^kind:\s*signpost\s*$` (case-insensitive).
- `planned[]` is free; do not require planned == anything.
- `updated` set to `2026-08-27` (RELEASE-INFO staged date). Gate does not continuously pin `updated` to RELEASE-INFO.
- No landing HTML, packs.html, version bump, CHANGELOG, plugin.json, or RELEASE-INFO edits.
- Em-dash-free durable prose.
- Gates: `python tooling/test_catalog_live_set.py`, `python tooling/test_ci_gate.py`, `python tooling/check_release.py`.

---

### Task 1: Bump catalog.json updated

**Files:**
- Modify: `catalog.json`

**Model:** flash

- [ ] **Step 1: Set updated**

Change `"updated": "2026-08-17"` to `"updated": "2026-08-27"`. Leave `packs` and `planned` alone unless a recount shows drift.

- [ ] **Step 2: Confirm set equality still holds**

```bash
python - <<'PY'
import json, re
from pathlib import Path
ROOT = Path('.')
c = json.loads((ROOT/'catalog.json').read_text(encoding='utf-8'))
assert c['updated'] == '2026-08-27'
content, signs = set(), set()
for d in (ROOT/'packs').iterdir():
    if not d.is_dir():
        continue
    t = (d/'SKILL.md').read_text(encoding='utf-8')
    fm = re.match(r'^---\s*\n(.*?)\n---', t, re.S)
    assert fm, d
    if re.search(r'^kind:\s*signpost\s*$', fm.group(1), re.I|re.M):
        signs.add(d.name)
    else:
        content.add(d.name)
live = {p['slug'] for p in c['packs'] if p.get('status') in (None, 'live')}
assert content == live and not (signs & {p['slug'] for p in c['packs']})
print('catalog updated + set OK', len(live))
PY
```

---

### Task 2: check_release check 14 [catalog-live-set]

**Files:**
- Modify: `tooling/check_release.py`

**Model:** deep

- [ ] **Step 1: Docstring**

Add check 14 after check 13. Extend CI-covered line to include catalog-live-set / check 14.

- [ ] **Step 2: Helpers**

- `inventory_pack_slugs(packs_root) -> (content_slugs, signpost_slugs, errors)` sharing the P15 frontmatter / signpost rule. Prefer reusing the same missing-SKILL failure shape with `[catalog-live-set]` when called from this check, or share a neutral inventory and retag; keep messages clear.
- `check_catalog_live_set(packs_root, catalog_dict) -> list[str]` implementing the spec equality rules. Pin-worthy literals for CI: `"[catalog-live-set]"`, and a stable path/open string for `"catalog.json"` if needed.

- [ ] **Step 3: Wire into main()**

After check 13 (or adjacent to catalog load), run check 14. Fail closed on JSON read errors with the tag.

- [ ] **Step 4: Smoke**

```bash
python tooling/check_release.py
```

---

### Task 3: CI twin

**Files:**
- Modify: `.github/workflows/validate.yml`

**Model:** standard

- [ ] **Step 1: Coverage map**

```text
#   Catalog live-set parity                     twins check_release 14 [catalog-live-set]
```

- [ ] **Step 2: New step after Catalog JSON valid**

Step name exactly `Catalog live-set parity`. Inline `python3 - <<'PY'` stdlib only. Same equality rules as check 14. Shared literals byte-identical for pins.

---

### Task 4: Probes

**Files:**
- Create: `tooling/test_catalog_live_set.py`
- Modify: `tooling/test_ci_gate.py`

**Model:** standard

- [ ] **Step 1: test_catalog_live_set.py**

Assert inventory slugs, matching fixture passes, extra catalog slug fails with `[catalog-live-set]`, signpost-in-catalog fails, real tree clean.

- [ ] **Step 2: test_ci_gate.py**

Add `"Catalog live-set parity"` to `PINNED_STEPS` (six -> seven). Add `CATALOG_LIVE_SET_PAIR` literals. Negative demo + positive real-tree run.

- [ ] **Step 3: Run**

```bash
python tooling/test_catalog_live_set.py
python tooling/test_ci_gate.py
python tooling/check_release.py
```

---

### Task 5: Status artifacts and package close

**Files:**
- Modify: `docs/superpowers/packages/2026-09-16-jgs-se-knowledge-packs-packages.md` (P16 -> done)
- Create: EXECUTED, FCL/ARL/IVL triage logs for this stem
- Leave `docs/superpowers/backlog.md` b-03 as `promoted`

**Model:** flash

- [ ] Full green gates including catalogue-count from P15
- [ ] Negative demo on catalog then restore
- [ ] Mark P16 done; EXECUTED one line `done`
- [ ] Commit

## Out of scope

- Landing HTML / still / packs.html
- P8, version bump, RELEASE-INFO body edits
- planned[] promotion

## Success criteria

- updated `2026-08-27`; slug set locked by check 14 + CI twin + probes
- check_release PASS; catalogue-count still green
- P16 done; b-03 remains promoted
