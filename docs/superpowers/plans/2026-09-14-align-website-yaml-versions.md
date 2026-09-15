# Align Website Product YAML Versions to 1.20.0 (CR-01) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Both public-website product YAMLs carry `version: "1.20.0"`, `python tooling/check_release.py` passes with a new consistency check covering them, and the local annotated tag v1.20.0 points at the fix commit. Nothing is pushed.

**Architecture:** One commit changes two one-line YAML version values and extends check 4 of the release gate with a stdlib-regex scrape of exactly those two files, compared against the RELEASE-INFO version the gate already parses. The commit is then retagged by explicit hash so the local-only annotated tag v1.20.0 tracks the fix, not the stale generator-refresh commit.

**Tech Stack:** Python 3 stdlib only (existing `tooling/check_release.py`), plain YAML text edits, git plumbing (`tag -d` / `tag -a`, `cat-file`, `rev-parse`). No new files, no dependencies, no test framework.

**Spec:** docs/superpowers/specs/2026-09-14-align-website-yaml-versions.md

## Global Constraints

- Both website YAMLs get exactly `version: "1.20.0"` (double quotes kept, single-line in-place edits; every other byte unchanged).
- Worktree files are CRLF, index is LF (`git ls-files --eol`: i/lf w/crlf on all three files). Never rewrite a whole file; single-line edits and the sed commands below preserve line endings.
- Commit message exactly: `fix: align website product YAMLs to 1.20.0 (CR-01)`. One commit total in this package.
- Tag message exactly: `chore: annotate v1.20.0 generator refresh path`. Tag by explicit hash, never a symbolic ref.
- `git push` is banned in all forms, including tag refs. `gh release create` and /gsd-ship are out of scope.
- `tooling/check_release.py` stays stdlib-only (`json`, `re`, `sys`, `pathlib`); no PyYAML import; no new abstractions.
- The new check scans exactly `docs/products/website/01-jgs-se-knowledge-packs.yaml` and `docs/products/website/catalog.yaml`. Never a repo-wide `version:` grep: `packs/*/PACK.yaml` uses `source_version` (different version class) and docs carry keep-class history.
- Keep-class 1.19.1 strings must remain untouched: CHANGELOG.md:44, docs/capability-map-CONTRACT.md:35, docs/capability-pack-map.md:18.
- No `.planning/` edits, no WR-01/02/03, no FUT-04/IO-05/IO-06, no pack content, no new packs.

## Codebase context

All facts re-verified on disk 2026-09-14; they match `docs/superpowers/context/2026-09-14-align-website-yaml-versions-context.md` (Track 1, CONTEXT_COMPLETE).

- Drift: `docs/products/website/01-jgs-se-knowledge-packs.yaml:15` reads `version: "1.19.1"` (top-level, no indent); `docs/products/website/catalog.yaml:13` reads `    version: "1.19.1"` (4-space indent under `products[0]`). Baseline `git grep -n "1.19.1" docs/products/website` returns exactly these 2 hits.
- Version trio already at 1.20.0: RELEASE-INFO.txt:3 (`Version:    1.20.0`), .claude-plugin/plugin.json:4, CHANGELOG.md:12.
- Gate: `fail(errs, msg)` helper at `tooling/check_release.py:61`; check 4 ("version single-source") spans lines 108-122; RELEASE-INFO parse lands in `versions["RELEASE-INFO.txt"]` at lines 117-119; the aggregate disagreement check is lines 120-122. Existing `[version]` call sites: line 113 and line 122.
- Nothing in `tooling/` or `.github/` reads the two website YAMLs; docs/packs.html takes its version from RELEASE-INFO (`tooling/gen_packs_page.py:42-43`). The bump cannot break CI and no derived artifact embeds these versions.
- Tag v1.20.0 is annotated (tag object 61fd653), peels to commit 046799b, and is local-only (`git branch -r --contains 046799b` is empty, verified).
- The graphify post-commit hook no-ops on this tree: its guard at `.git/hooks/post-commit:22` exits because `.planning/graphs/graph.json` is gitignored (`.gitignore:37` is `.planning/`). It can in principle append a second commit if that carve-out ever changes, so every later step anchors to the fix hash explicitly.
- Python 3.14.7 is on PATH as `python`. Baseline `python tooling/check_release.py` exits 0 (PASS verified 2026-09-14, before this plan).
- `packs/dau-se-guidebook/PACK.yaml:4` carries `source_version: "February 2022 (DOPSR Case # 22-S-0595)"`. No tooling validates `source_version` (only `build_pack.py:48` writes it), so a temporary edit there cannot trip any other check.

## Research

research: skipped (version values are fixed by the repo's own RELEASE-INFO.txt and the local annotated tag; no external API, library, platform, or version choice is involved)

---

### Task 1: Bump both website YAML version lines to 1.20.0

**Files:**
- Modify: `docs/products/website/01-jgs-se-knowledge-packs.yaml:15`
- Modify: `docs/products/website/catalog.yaml:13`

**Interfaces:**
- Produces: both files reading `version: "1.20.0"`, which Task 2's check and Task 5's commit depend on.

**Model:** flash

- [ ] **Step 1: Edit the product file**

Old string: `version: "1.19.1"` (unique in the file). New string: `version: "1.20.0"`.
Single-line in-place edit only; sed equivalent (preserves CRLF):

```bash
sed -i 's/version: "1.19.1"/version: "1.20.0"/' docs/products/website/01-jgs-se-knowledge-packs.yaml
```

- [ ] **Step 2: Edit the catalog file**

Old string: `    version: "1.19.1"` (4-space indent, unique in the file). New string: `    version: "1.20.0"`.
Do not copy the product file's line over this one; the indents differ.

```bash
sed -i 's/version: "1.19.1"/version: "1.20.0"/' docs/products/website/catalog.yaml
```

- [ ] **Step 3: Verify**

```bash
git grep -n 'version: "1.20.0"' -- docs/products/website
git grep -n '1.19.1' -- docs/products/website; echo "residual exit=$?"
git diff --stat
```

Expected: first command prints exactly

```
docs/products/website/01-jgs-se-knowledge-packs.yaml:15:version: "1.20.0"
docs/products/website/catalog.yaml:13:    version: "1.20.0"
```

Second command prints nothing with `residual exit=1`. Third shows exactly the two YAML files, ~1 line changed each.

### Task 2: Add the website YAML consistency check to check_release.py

**Files:**
- Modify: `tooling/check_release.py:13` (docstring), `tooling/check_release.py:119-120` (insert block)

**Interfaces:**
- Consumes: `versions["RELEASE-INFO.txt"]` parsed at lines 117-119; `fail(errs, msg)` helper at line 61.
- Produces: a `[version]` failure naming the file whenever either website YAML is missing its `version: "X.Y.Z"` value or disagrees with RELEASE-INFO. Task 3 tests this behavior.

**Model:** flash

- [ ] **Step 1: Update the docstring line**

Old string (line 13):

```
  4. Version single-source agreement: plugin.json == CHANGELOG top == RELEASE-INFO.txt.
```

New string:

```
  4. Version single-source agreement: plugin.json == CHANGELOG top ==
     RELEASE-INFO.txt == the two website product YAMLs under docs/products/website.
```

- [ ] **Step 2: Insert the check**

Old string (lines 119-120, unique):

```python
    versions["RELEASE-INFO.txt"] = m.group(1) if m else ""
    distinct = {v for v in versions.values() if v}
```

New string (inserts block 4a between them):

```python
    versions["RELEASE-INFO.txt"] = m.group(1) if m else ""
    # 4a. CR-01: the two website product YAMLs (RR-B-19 website sources) must carry
    # the release version too. Scoped to exactly these two paths; packs/*/PACK.yaml
    # uses source_version (different class) and docs carry keep-class history.
    expected = versions["RELEASE-INFO.txt"]
    for rel in ("docs/products/website/01-jgs-se-knowledge-packs.yaml",
                "docs/products/website/catalog.yaml"):
        body = (ROOT / rel).read_text(encoding="utf-8", errors="ignore") if (ROOT / rel).is_file() else ""
        m = re.search(r'version:\s*"([0-9]+\.[0-9]+\.[0-9]+)"', body)
        got = m.group(1) if m else ""
        if got != expected:
            fail(errs, f"[version] {rel}: website YAML version '{got}' "
                       f"!= RELEASE-INFO '{expected}'")
    distinct = {v for v in versions.values() if v}
```

First `re.search` match per file is the version key itself: neither file contains any earlier `version:` occurrence. The regex must not be loosened to an unquoted form or widened to more paths.

- [ ] **Step 3: Verify the gate still passes**

```bash
python tooling/check_release.py; echo "exit=$?"
```

Expected: exit=0 and the last output line starts with `RELEASE CHECK: PASS`. Both YAMLs are already 1.20.0 from Task 1, matching RELEASE-INFO.

### Task 3: Negative-test the new gate, then restore

**Files:**
- Temporarily modify: `docs/products/website/catalog.yaml`, `packs/dau-se-guidebook/PACK.yaml` (both fully restored by the end of this task)

**Interfaces:**
- Consumes: the 4a check from Task 2.
- Produces: proof the gate fails with a file-naming `[version]` error on drift, and does not fire on `packs/*/PACK.yaml` `source_version`. Covers acceptance criterion 6.

**Model:** standard

- [ ] **Step 1: Break catalog.yaml temporarily**

```bash
sed -i 's/version: "1.20.0"/version: "0.0.0"/' docs/products/website/catalog.yaml
```

- [ ] **Step 2: Run the gate and confirm the failure names the file**

```bash
python tooling/check_release.py; echo "exit=$?"
```

Expected: exit=1, output contains exactly one issue line:

```
  - [version] docs/products/website/catalog.yaml: website YAML version '0.0.0' != RELEASE-INFO '1.20.0'
```

- [ ] **Step 3: Restore catalog.yaml**

`git checkout` is wrong here: the fix is not committed yet, so checkout would resurrect 1.19.1. Restore by reversing the sed (CRLF preserved).

```bash
sed -i 's/version: "0.0.0"/version: "1.20.0"/' docs/products/website/catalog.yaml
git grep -n 'version: "1.20.0"' -- docs/products/website/catalog.yaml
```

Expected: `docs/products/website/catalog.yaml:13:    version: "1.20.0"`.

- [ ] **Step 4: Control: change a PACK.yaml source_version, expect no [version] error**

```bash
sed -i 's/^source_version: .*/source_version: "1.19.1"/' packs/dau-se-guidebook/PACK.yaml
python tooling/check_release.py; echo "exit=$?"
python tooling/check_release.py 2>&1 | grep '\[version\]' || echo "no [version] lines (expected)"
```

Expected: exit=0, last line starts with `RELEASE CHECK: PASS`, second command prints `no [version] lines (expected)`. The value `1.19.1` is deliberate: it would match the 4a regex if the file were ever scanned, so a pass proves the path scoping, not just value inequality.

- [ ] **Step 5: Restore the control and verify**

`git checkout` is correct here: PACK.yaml was never part of this package's edits, so HEAD holds the original bytes.

```bash
git checkout -- packs/dau-se-guidebook/PACK.yaml
git status --porcelain -- packs/; echo "packs clean exit=$?"
```

Expected: no output, exit=0.

- [ ] **Step 6: Confirm working tree state**

```bash
git status --porcelain
```

Expected exactly (order may vary):

```
 M docs/products/website/01-jgs-se-knowledge-packs.yaml
 M docs/products/website/catalog.yaml
 M tooling/check_release.py
?? docs/superpowers/
```

### Task 4: Full gate run before commit

**Files:** none (verification only)

**Model:** flash

- [ ] **Step 1: Run the release gate**

```bash
python tooling/check_release.py; echo "exit=$?"
```

Expected: exit=0, final line starts with `RELEASE CHECK: PASS`. No `[version]` lines in output.

- [ ] **Step 2: Confirm the pre-commit tree**

`git status --porcelain` shows the same 3 modified tracked files and `?? docs/superpowers/` as Task 3 Step 6. If anything else is modified, stop and investigate before committing.

### Task 5: Commit YAML and tooling edits

**Files:** none created; commits the 3 modified files

**Interfaces:**
- Produces: `FIX_HASH`, the commit hash of `fix: align website product YAMLs to 1.20.0 (CR-01)`, consumed by Tasks 6 and 7. Because SCD workers see one task at a time, later tasks re-derive it with the command in Step 3 rather than trusting a remembered value.

**Model:** standard

- [ ] **Step 1: Stage exactly the three files**

Never `git add -A` or `git add .`: that would sweep the untracked `docs/superpowers/` planning docs into the commit.

```bash
git add docs/products/website/01-jgs-se-knowledge-packs.yaml docs/products/website/catalog.yaml tooling/check_release.py
git status --porcelain
```

Expected: the three files staged (`M ` prefix), `?? docs/superpowers/` still untracked.

- [ ] **Step 2: Commit**

```bash
git commit -m "fix: align website product YAMLs to 1.20.0 (CR-01)"
```

The graphify post-commit hook runs automatically; on this tree it no-ops (guard at `.git/hooks/post-commit:22`, `.planning/` gitignored at `.gitignore:37`).

- [ ] **Step 3: Record the fix hash**

```bash
git log -2 --format="%H %s"
```

Expected: one line ends with `fix: align website product YAMLs to 1.20.0 (CR-01)`. If `git rev-parse HEAD` has that subject, FIX_HASH equals HEAD. If the hook appended a second commit, HEAD differs and the fix commit is HEAD's parent; tag the fix hash either way. Later tasks re-derive it with:

```bash
FIX_HASH=$(git log --format="%H %s" | grep 'fix: align website product YAMLs to 1.20.0 (CR-01)' | cut -d' ' -f1)
```

- [ ] **Step 4: Verify commit contents**

```bash
FIX_HASH=$(git log --format="%H %s" | grep 'fix: align website product YAMLs to 1.20.0 (CR-01)' | cut -d' ' -f1)
git show --stat --format="%H %s" "$FIX_HASH"
```

Expected: subject `fix: align website product YAMLs to 1.20.0 (CR-01)` and exactly 3 files changed: the two YAMLs and `tooling/check_release.py`. Nothing else.

### Task 6: Retag v1.20.0 on the fix commit

**Files:** none (git refs only)

**Interfaces:**
- Consumes: `FIX_HASH` from Task 5 (re-derived below).
- Produces: local annotated tag v1.20.0 peeling to FIX_HASH.

**Model:** standard

- [ ] **Step 1: Re-derive the fix hash and check HEAD (diagnostic)**

```bash
FIX_HASH=$(git log --format="%H %s" | grep 'fix: align website product YAMLs to 1.20.0 (CR-01)' | cut -d' ' -f1)
echo "FIX_HASH=$FIX_HASH"; git rev-parse HEAD
```

Expected: FIX_HASH non-empty. HEAD usually equals FIX_HASH; a mismatch means the hook appended a commit, which is fine because the tag anchors to FIX_HASH explicitly.

- [ ] **Step 2: Delete and recreate the tag on the explicit hash**

```bash
git tag -d v1.20.0
git tag -a v1.20.0 -m "chore: annotate v1.20.0 generator refresh path" "$FIX_HASH"
```

Expected: first command exits 0 printing `Deleted tag 'v1.20.0'` with a was-hash showing the current snapshot value (61fd653 at authoring time; informational, not an assertion); second is silent with exit 0. No push command runs here or anywhere in this package.

- [ ] **Step 3: Verify the tag**

```bash
FIX_HASH=$(git log --format="%H %s" | grep 'fix: align website product YAMLs to 1.20.0 (CR-01)' | cut -d' ' -f1)
git cat-file -t v1.20.0
git rev-parse "v1.20.0^{commit}"
git tag -l --format='%(contents:subject)' v1.20.0
git branch -r --contains "$FIX_HASH"; echo "remote exit=$?"
```

Expected: `tag`; FIX_HASH; `chore: annotate v1.20.0 generator refresh path`; no remote branches listed with `remote exit=1`.

### Task 7: Final acceptance sweep

**Files:** none (verification only)

**Interfaces:**
- Consumes: everything above. Criterion 6 was already exercised in Task 3 and is not repeated.

**Model:** standard

- [ ] **Step 1: Criterion 1, YAML contents and structure**

```bash
git grep -n '1.19.1' -- docs/products/website; echo "residual exit=$?"
git grep -n 'version: "1.20.0"' -- docs/products/website
FIX_HASH=$(git log --format="%H %s" | grep 'fix: align website product YAMLs to 1.20.0 (CR-01)' | cut -d' ' -f1)
git show "$FIX_HASH" -- docs/products/website
```

Expected: no 1.19.1 hits (exit 1); the two `version: "1.20.0"` lines at 01:15 and catalog:13 with original quoting and indent; the diff shows only two hunks:

```
-version: "1.19.1"
+version: "1.20.0"
```

and

```
-    version: "1.19.1"
+    version: "1.20.0"
```

- [ ] **Step 2: Criterion 2, gate PASS**

```bash
python tooling/check_release.py; echo "exit=$?"
```

Expected: exit=0, final line starts with `RELEASE CHECK: PASS`.

- [ ] **Step 3: Criterion 3, tag points at the fix commit**

```bash
FIX_HASH=$(git log --format="%H %s" | grep 'fix: align website product YAMLs to 1.20.0 (CR-01)' | cut -d' ' -f1)
git cat-file -t v1.20.0
git rev-parse "v1.20.0^{commit}"
git show --stat "$FIX_HASH" | head -8
```

Expected: `tag`; equals FIX_HASH; stat lists the two YAMLs plus `tooling/check_release.py`.

- [ ] **Step 4: Criterion 4, tag is local only**

```bash
FIX_HASH=$(git log --format="%H %s" | grep 'fix: align website product YAMLs to 1.20.0 (CR-01)' | cut -d' ' -f1)
git branch -r --contains "$FIX_HASH"; echo "remote exit=$?"
```

Expected: no output, exit 1.

- [ ] **Step 5: Criterion 5, keep-class strings untouched**

```bash
sed -n '44p' CHANGELOG.md
sed -n '35p' docs/capability-map-CONTRACT.md
sed -n '18p' docs/capability-pack-map.md
```

Expected, in order:

```
## [1.19.1]: 2026-08-20
| `map_version` | string | Release that last regenerated the map (semver, e.g. `"1.19.1"`). |
- Changelog (v1.19.1): map_version bump only; membership still 644; no reclassification.
```

- [ ] **Step 6: Criterion 6 restore semantics, clean tree after Task 3 restores**

```bash
git status --porcelain
```

Expected: exactly `?? docs/superpowers/` and nothing else; no modified tracked files anywhere.

- [ ] **Step 7: Criterion 7, record**

CR-01 is satisfied by the above. The master_flow re-gate and `.planning/` ledger ticks are parent-owned bookkeeping; do nothing for them here.
