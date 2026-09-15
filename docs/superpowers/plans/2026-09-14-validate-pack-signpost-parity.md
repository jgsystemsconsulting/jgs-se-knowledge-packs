# Validate-Pack Signpost Parity Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Teach `tooling/validate_pack.py` the `kind: signpost` pack shape so `python tooling/validate_pack.py --all` exits 0 at 65/65 on the same clean tree where `tooling/check_release.py` prints its PASS line.

**Architecture:** `check_pack` reads SKILL.md once (errors="ignore") before the required-file checks, computes an `is_signpost` boolean with check_release's exact regex, and guards only the missing-LICENSE and missing-chapters/ checks on it; the frontmatter block reuses the same `body` text instead of a second read. An assert-based probe, `tooling/test_validate_pack.py`, proves the carve-out is narrow. Docs get one docstring bullet rewording and one PACK-SPEC sentence; CONTRIBUTING.md and check_release.py stay untouched.

**Tech Stack:** Python 3 stdlib only (`re`, `sys`, `pathlib`, `tempfile`). No pytest, no PyYAML, no CI edits.

**Spec:** `docs/superpowers/specs/2026-09-14-validate-pack-signpost-parity.md`

## Global Constraints

- Detection regex is exactly `re.search(r"^kind:\s*signpost\s*$", body, re.M)` over the whole SKILL.md text, identical to check_release.py L134-135. SKILL.md is the only detector; PACK.yaml's `kind` field is corroboration, never a second detector.
- Guard exactly two checks on `is_signpost`: the missing-LICENSE error and the missing-chapters/ error including its empty-chapters branch. Every other check (SKILL.md presence, PACK.yaml presence, frontmatter name + description + slug match, chapter-link resolution, PACK.yaml required fields, tier in {1,2,3}, slug match) applies to every pack.
- Missing SKILL.md stays a hard fail even for a would-be signpost: without the file the kind cannot be proven.
- `--all` reports a well-formed signpost as plain `PASS  <slug>` (two spaces after PASS). No new status vocabulary, no `(signpost)` annotation, no skip counter. Exit 0 when `passed == total` (65/65 on the current tree; count is a current-tree annotation, not a permanent contract).
- `check_release.py` is not modified. Its pre-filter, RR-S-13, and SKILLS-count sections stay as they are.
- No edits under `packs/` (signpost bodies, citations, PACK.yaml files). No CI workflow edits. No pytest or any test framework. No PyYAML.
- CONTRIBUTING.md is not modified; L38 and L54 stay accurate after the fix.
- Probe follows the `tooling/test_link_policy.py` convention: assert-based, no framework, `Run:` line in the docstring, fixtures in `tempfile.TemporaryDirectory`, live tree read-only, nonzero exit on first failed assert.
- Platform: Windows, Git Bash. Local runner is `python`. Paths below are repo-relative; run from the repo root.

## Research

research: skipped (in-repo tooling alignment only; no external APIs, libraries, platforms, or version-sensitive choices)

## Codebase context

Full exploration lives in `docs/superpowers/context/2026-09-14-validate-pack-signpost-parity-context.md` (and its `-context-log.md` sibling). Facts the executor needs, verified against HEAD `a42e3d9`:

- `tooling/validate_pack.py` (143 lines total). `check_pack` is L52-111. Required-file checks L57-74 are unconditional today: signpost and content packs share one requirement set, which is the bug. The frontmatter block re-reads SKILL.md at L78 (`body = skill.read_text(encoding="utf-8")`), so the early read in this plan replaces that later read rather than adding a second one. `main` is L114-138: empty argv behaves like `--all`, iterates every directory under `packs/` with no filter, prints `PASS  <name>` / `FAIL  <name>` plus error lines, prints `<passed>/<total> pack(s) passed.`, returns 1 if any pack failed.
- `tooling/check_release.py` L134-135 builds `signpost_dirs` with `re.search(r"^kind:\s*signpost\s*$", p.read_text(encoding="utf-8", errors="ignore"), re.M)` over `packs/*/SKILL.md`, then pre-filters those dirs out of its `validate_pack.check_pack` loop at L184-191. That file is untouched by this plan.
- Live signpost packs: `packs/omg-signpost` and `packs/se-standards-signpost`, each carrying only SKILL.md (with `kind: signpost` on line 3 of the frontmatter) and PACK.yaml. Their PACK.yaml already satisfies every `REQUIRED_PACK_FIELDS` entry, tier 2, and the slug match. Today `python tooling/validate_pack.py --all` exits 1 at 63/65; `python tooling/check_release.py` exits 0 on the same tree.
- Content-pack contrast: `packs/requirements-writing` has SKILL.md, PACK.yaml, LICENSE, `chapters/`, and optional furniture; it must keep passing unchanged.
- Docs surfaces: `tooling/validate_pack.py` docstring L11-16 (required-files bullet at L12), `docs/PACK-SPEC.md` Validation section L91-99 (per-slug command at L94, checks sentence at L97-99), `CONTRIBUTING.md` L38 (per-slug command) and L54-55 ("CI runs `validate_pack.py` on every pack", which becomes accurate where it was misleading). README and SOURCE-VETTING describe signposts as citation-only and stay untouched.
- Probe convention: `tooling/test_link_policy.py` is the model. Shebang, copyright header, docstring with `Run:` line, `from __future__ import annotations`, `sys.path.insert(0, str(Path(__file__).resolve().parent))` before importing the module under test, asserts inside `def main() -> int:`, a final `print("... tests: OK")`, and `raise SystemExit(main())`.

## File structure

- Modify `tooling/validate_pack.py`: docstring bullet (L12), `check_pack` required-files block (L57-74), drop the second SKILL.md read (L78). No signature changes; `main` untouched.
- Create `tooling/test_validate_pack.py`: assert-based probe, roughly 100 lines, stdlib only.
- Modify `docs/PACK-SPEC.md`: one sentence in the Validation section (L91-99).

---

### Task 1: Signpost-aware check_pack with assert-based probe

**Files:**
- Modify: `tooling/validate_pack.py` (docstring L12; `check_pack` L57-74 and L78)
- Create: `tooling/test_validate_pack.py`

**Interfaces:**
- Consumes: `validate_pack.check_pack(pack_dir: Path) -> list[str]` (existing signature, unchanged).
- Produces: `check_pack` returns `[]` for a well-formed signpost pack (SKILL.md matching `^kind:\s*signpost\s*$` multiline, PACK.yaml, no LICENSE, no chapters/) and still returns the existing error strings for every broken shape. `tooling/test_validate_pack.py` runnable as `python tooling/test_validate_pack.py`, exit 0 with `validate_pack tests: OK`.

**Model:** flash

- [ ] **Step 1: Write the failing probe**

Create `tooling/test_validate_pack.py` with exactly this content:

```python
#!/usr/bin/env python3
# Copyright (c) 2026 JG Systems Consulting Ltd. — MIT License (see LICENSE).
# SPDX-License-Identifier: MIT
"""Assert-based checks for validate_pack.check_pack signpost parity (no framework).

Run:  python tooling/test_validate_pack.py
Exits 0 when content-pack and signpost-pack shapes classify as PACK-SPEC expects.
Any failed assert raises and exits nonzero. Fixtures are built in a temp dir;
the live tree is only read (case 7), never mutated.
"""
from __future__ import annotations

import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import validate_pack  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent

CONTENT_SKILL = """---
name: {slug}
description: "Demo content pack used by the validator probe."
---
"""

SIGNPOST_SKILL = """---
name: {slug}
kind: signpost
description: "Demo signpost used by the validator probe."
---
"""

SIGNPOST_NO_DESC = """---
name: {slug}
kind: signpost
---
"""

PACK_YAML = """slug: {slug}
title: "Demo Pack"
publisher: "JG Systems Consulting Ltd."
license: "MIT"
license_tier: 2
commercial_use: true
"""


def build_pack(root: Path, slug: str, *, skill: str | None, pack_yaml: bool = True,
               license_: bool = True, chapters: bool = True) -> Path:
    d = root / slug
    d.mkdir()
    if skill is not None:
        (d / "SKILL.md").write_text(skill.format(slug=slug), encoding="utf-8")
    if pack_yaml:
        (d / "PACK.yaml").write_text(PACK_YAML.format(slug=slug), encoding="utf-8")
    if license_:
        (d / "LICENSE").write_text("MIT", encoding="utf-8")
    if chapters:
        (d / "chapters").mkdir()
        (d / "chapters" / "ch01-intro.md").write_text("# Intro\n", encoding="utf-8")
    return d


def main() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)

        # (1) full content-pack shape passes
        full = build_pack(root, "full-pack", skill=CONTENT_SKILL)
        assert validate_pack.check_pack(full) == [], validate_pack.check_pack(full)

        # (2) content pack minus LICENSE fails with the LICENSE error
        no_lic = build_pack(root, "no-license", skill=CONTENT_SKILL, license_=False)
        errs = validate_pack.check_pack(no_lic)
        assert errs == ["missing LICENSE (must reproduce the source's terms)"], errs

        # (3) content pack minus chapters/ fails with the chapters error
        no_ch = build_pack(root, "no-chapters", skill=CONTENT_SKILL, chapters=False)
        errs = validate_pack.check_pack(no_ch)
        assert errs == ["missing chapters/ directory"], errs

        # (4) signpost shape (SKILL.md + PACK.yaml only) passes
        sign = build_pack(root, "demo-signpost", skill=SIGNPOST_SKILL,
                          license_=False, chapters=False)
        assert validate_pack.check_pack(sign) == [], validate_pack.check_pack(sign)

        # (5) signpost missing SKILL.md fails: kind cannot be proven
        bare = build_pack(root, "bare-signpost", skill=None,
                          license_=False, chapters=False)
        errs = validate_pack.check_pack(bare)
        assert errs == ["missing SKILL.md",
                        "missing LICENSE (must reproduce the source's terms)",
                        "missing chapters/ directory"], errs

        # (6a) signpost missing PACK.yaml still fails
        no_meta = build_pack(root, "no-meta-signpost", skill=SIGNPOST_SKILL,
                             pack_yaml=False, license_=False, chapters=False)
        errs = validate_pack.check_pack(no_meta)
        assert errs == ["missing PACK.yaml"], errs

        # (6b) signpost frontmatter missing description still fails
        no_desc = build_pack(root, "no-desc-signpost", skill=SIGNPOST_NO_DESC,
                             license_=False, chapters=False)
        errs = validate_pack.check_pack(no_desc)
        assert errs == ["SKILL.md frontmatter missing 'description'"], errs

    # (7) both live signpost packs pass on the real tree (read-only)
    for slug in ("omg-signpost", "se-standards-signpost"):
        live = REPO_ROOT / "packs" / slug
        assert live.is_dir(), f"live signpost pack missing: {live}"
        assert validate_pack.check_pack(live) == [], slug

    print("validate_pack tests: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

Notes for the executor:

- The copyright header line reproduces the repo-wide convention used by every file in `tooling/` (it contains an em dash by convention; keep it verbatim for consistency).
- Case 5's expected list is exactly three errors in that order: with no SKILL.md the kind cannot be proven, so `is_signpost` is False and the content-pack LICENSE and chapters/ errors follow the missing-SKILL.md error.
- Case 7 reads the live tree only; it writes nothing.

- [ ] **Step 2: Run the probe to verify it fails**

Run: `python tooling/test_validate_pack.py; echo "exit=$?"`

Expected: exit 1 with a traceback whose assert is case (4), ending in:

```text
AssertionError: ['missing LICENSE (must reproduce the source\'s terms)', 'missing chapters/ directory']
```

Cases (1)-(3) pass before the fix; case (4) fails because `check_pack` still demands LICENSE and chapters/ from signposts.

- [ ] **Step 3: Implement the signpost guard in check_pack**

In `tooling/validate_pack.py`, replace this exact block (current L57-74):

```python
    # --- required files ---
    skill = pack_dir / "SKILL.md"
    pack_yaml = pack_dir / "PACK.yaml"
    lic = pack_dir / "LICENSE"
    chapters = pack_dir / "chapters"

    if not skill.is_file():
        errors.append("missing SKILL.md")
    if not pack_yaml.is_file():
        errors.append("missing PACK.yaml")
    if not lic.is_file():
        errors.append("missing LICENSE (must reproduce the source's terms)")
    if not chapters.is_dir():
        errors.append("missing chapters/ directory")
    else:
        ch_files = sorted(chapters.glob("ch*.md"))
        if not ch_files:
            errors.append("chapters/ contains no chNN-*.md files")
```

with:

```python
    # --- required files ---
    skill = pack_dir / "SKILL.md"
    pack_yaml = pack_dir / "PACK.yaml"
    lic = pack_dir / "LICENSE"
    chapters = pack_dir / "chapters"

    # Signpost detection: same regex as check_release.py so both tools
    # classify a pack identically. Read once here; reused by the
    # frontmatter block below instead of a second read.
    body = skill.read_text(encoding="utf-8", errors="ignore") if skill.is_file() else ""
    is_signpost = bool(re.search(r"^kind:\s*signpost\s*$", body, re.M))

    if not skill.is_file():
        errors.append("missing SKILL.md")
    if not pack_yaml.is_file():
        errors.append("missing PACK.yaml")
    if not is_signpost:
        if not lic.is_file():
            errors.append("missing LICENSE (must reproduce the source's terms)")
        if not chapters.is_dir():
            errors.append("missing chapters/ directory")
        else:
            ch_files = sorted(chapters.glob("ch*.md"))
            if not ch_files:
                errors.append("chapters/ contains no chNN-*.md files")
```

Then drop the second read: replace this exact block (current L76-79):

```python
    # --- SKILL.md frontmatter + chapter links ---
    if skill.is_file():
        body = skill.read_text(encoding="utf-8")
        fm = re.match(r"^---\s*\n(.*?)\n---\s*\n", body, re.S)
```

with:

```python
    # --- SKILL.md frontmatter + chapter links ---
    if skill.is_file():
        fm = re.match(r"^---\s*\n(.*?)\n---\s*\n", body, re.S)
```

Behavior note (intended): the single read now uses `errors="ignore"`, matching check_release's read. A SKILL.md with undecodable bytes no longer raises UnicodeDecodeError; it is read lossily like check_release reads it, which keeps the two tools classifying identically.

- [ ] **Step 4: Reword the docstring required-files bullet**

In `tooling/validate_pack.py`, replace this exact line (current L12):

```python
  - required files present: SKILL.md, PACK.yaml, LICENSE, chapters/ with >=1 chapter
```

with:

```python
  - required files present: SKILL.md and PACK.yaml always; content packs also need
    LICENSE and chapters/ with >=1 chapter (signpost packs, marked `kind: signpost`
    in SKILL.md, carry neither and skip those two checks)
```

- [ ] **Step 5: Run the probe to verify it passes**

Run: `python tooling/test_validate_pack.py; echo "exit=$?"`

Expected:

```text
validate_pack tests: OK
exit=0
```

- [ ] **Step 6: Live-tree verification**

Run each command from the repo root and check the expected result:

1. `python tooling/validate_pack.py --all; echo "exit=$?"`
   Expected: exit 0; `PASS  omg-signpost` and `PASS  se-standards-signpost` among the lines; final summary line `65/65 pack(s) passed.` (65 = current dir count: 63 content + 2 signpost; annotation only).
2. `python tooling/validate_pack.py; echo "exit=$?"` (empty argv behaves like `--all`)
   Expected: identical output and exit 0.
3. `python tooling/validate_pack.py packs/omg-signpost packs/se-standards-signpost; echo "exit=$?"`
   Expected: two `PASS` lines, `2/2 pack(s) passed.`, exit 0.
4. `python tooling/validate_pack.py packs/requirements-writing; echo "exit=$?"`
   Expected: `PASS  requirements-writing`, `1/1 pack(s) passed.`, exit 0 (content-pack path unchanged).

- [ ] **Step 7: Prove the probe bites**

Temporarily comment out the kind line in the case (4) fixture: in `tooling/test_validate_pack.py`, change the `SIGNPOST_SKILL` line `kind: signpost` to `# kind: signpost`. Run: `python tooling/test_validate_pack.py; echo "exit=$?"`

Expected: exit 1 with `AssertionError: ['missing LICENSE (must reproduce the source\'s terms)', 'missing chapters/ directory']` at case (4) (a signpost without the kind marker is judged a content pack and fails both content-pack-only checks). Restore the line exactly as written in Step 1 and rerun to confirm `validate_pack tests: OK`.

- [ ] **Step 8: Commit**

```bash
git add tooling/validate_pack.py tooling/test_validate_pack.py
git commit -m "tooling: teach validate_pack the kind: signpost pack shape"
```

---

### Task 2: PACK-SPEC sentence and full-tree verification sweep

**Files:**
- Modify: `docs/PACK-SPEC.md` (Validation section, L91-99)
- Verify-only: `CONTRIBUTING.md` (L38, L54-55, unchanged), `tooling/check_release.py` (unchanged)

**Interfaces:**
- Consumes: the Task 1 `check_pack` behavior and probe.
- Produces: documentation that matches the new validator behavior; the spec's fixed verification list fully green.

**Model:** flash

- [ ] **Step 1: Add the signpost sentence to PACK-SPEC.md**

In `docs/PACK-SPEC.md`, replace this exact block (current L91-99):

````markdown
## Validation

```bash
python tooling/validate_pack.py packs/<slug>
```

Checks: required files present, frontmatter valid, every chapter link resolves,
`PACK.yaml` mandatory fields filled, and `license_tier ∈ {1,2,3}`. CI runs this on
every pack on every PR.
````

with:

````markdown
## Validation

```bash
python tooling/validate_pack.py packs/<slug>
```

Signpost packs (`kind: signpost` in SKILL.md, e.g. `packs/omg-signpost`) skip the
LICENSE and `chapters/` checks; every other check still applies.

Checks: required files present, frontmatter valid, every chapter link resolves,
`PACK.yaml` mandatory fields filled, and `license_tier ∈ {1,2,3}`. CI runs this on
every pack on every PR.
````

- [ ] **Step 2: Confirm check_release still passes unchanged**

Run: `python tooling/check_release.py; echo "exit=$?"`

Expected: exit 0 with a final line starting `RELEASE CHECK: PASS` (no output change from before this plan).

- [ ] **Step 3: Full verification sweep**

Run each command and check the expected result:

1. `python tooling/validate_pack.py --all; echo "exit=$?"` → exit 0, `65/65 pack(s) passed.` (current-tree annotation).
2. `python tooling/validate_pack.py packs/omg-signpost packs/se-standards-signpost; echo "exit=$?"` → exit 0, `2/2 pack(s) passed.`
3. `python tooling/test_validate_pack.py; echo "exit=$?"` → `validate_pack tests: OK`, exit 0.
4. `python tooling/test_link_policy.py; echo "exit=$?"` → `link-policy tests: OK`, exit 0 (neighbor probe still green).
5. `git diff --name-only` → exactly `docs/PACK-SPEC.md` (Task 1 files are already committed; run from a tree with no uncommitted changes beyond Task 1's commits). If `CONTRIBUTING.md` or anything under `tooling/check_release.py`'s path or `packs/` appears, stop and fix the diff.

- [ ] **Step 4: Prose and placeholder pass over touched files**

Run: `python ~/.zcode/scripts/prose_check.py docs/PACK-SPEC.md tooling/validate_pack.py tooling/test_validate_pack.py`

Expected: no new em-dash or placeholder findings in added lines. Two justified residuals: validate_pack.py has pre-existing em dashes (copyright header L2, title L5, tier message L105, one comment L46) that this plan does not touch, and test_validate_pack.py's copyright header reproduces the repo-wide tooling convention per Task 1 Step 1. All prose this plan adds is clean.

- [ ] **Step 5: Commit**

```bash
git add docs/PACK-SPEC.md
git commit -m "docs: note signpost packs skip LICENSE and chapters checks in PACK-SPEC"
```
