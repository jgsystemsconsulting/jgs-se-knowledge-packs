# Create 1.23.0 Release Surfaces Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Move every release-gate version surface from 1.22.1 to 1.23.0 on `packages-2026-10-27`, rewrite the changelog, regenerate version-stamped pages, pass the post-commit receipt gate, and create the annotated tag `v1.23.0` locally. Stop. No push.

**Architecture:** One commit. Page generators read `RELEASE-INFO.txt` at render time, so that file is edited before `python tooling/gen_pack_pages.py` and `python tooling/gen_packs_page.py`. The pre-commit smoke gate proves the tree agrees; its sha is not the release sha. The post-commit gate on the committed tree is the receipt the tag binds to. Order is gate, then commit, then receipt gate, then tag. Do not reorder it.

**Tech Stack:** Markdown, YAML, JSON, HTML. Python 3 stdlib tooling already in the repo (`tooling/check_release.py`, `tooling/gen_pack_pages.py`, `tooling/gen_packs_page.py`, `tooling/test_ci_gate.py`). Git annotated tag. No new dependencies. No tooling edits.

**Spec:** `docs/superpowers/specs/2026-10-28-create-release.md` (review pair clean, cert sha256 `6ce18e719a857b0a9d5257ed8e8d2249cdd775ec2deff2cd66c15a53b3f43396`)

## Global Constraints

- D1: Version is 1.23.0. Two new content packs (`jsp-936`, `fhwa-its-se`) are MINOR-level additions under SemVer. The CI gate group is feature-level and rides the same bump. A patch bump would understate two new packs.
- D2: `.cursor-plugin/plugin.json` version stays at 1.22.0. The version single-source (local check 4 and the CI heredoc) does not read it, so leaving it does not break a gate. Folding its version line into the single-source is P60, out of scope. The release section states the gap in one line rather than hiding it.
- D3: The Unreleased Changed bullet claiming "all 80 skill paths" is rewritten in the 1.23.0 section to the final count, 82. 80 was true at `adb7c5d` (2026-10-26). `jsp-936` registration took it to 81 and `fhwa-its-se` registration to 82. Shipping the stale number would document a lie.
- D4: `RELEASE-INFO.txt` `Staged:` is set to 2026-10-28T00:00:00Z, the release date. The 2026-09-27 stamp belongs to the 1.22.0 cut and was never refreshed at 1.22.1.
- D5: The run creates the annotated tag locally and stops. No push. Tag command is `git tag -a v1.23.0 -m "jgs-se-knowledge-packs 1.23.0"`, matching the `v1.22.1` message shape. The user pushes the tag and the branch.
- D6: Planning-doc commits do not appear in the changelog. Precedent: the 1.22.1 section lists user-visible fixes, inventory prose, and tooling, and lists no spec, plan, EXECUTED, or IVL log. Group 5 stays out.
- D7: The 1.23.0 section documents the landing-pages group and the CI-gates group explicitly, each as its own bullet, not folded into a pack bullet.
- Branch is `packages-2026-10-27`. Do not switch branches. Do not merge to `main`.
- `CITATION.cff` `date-released` stays `2026-09-27`. Spec step 6 names only `version:`. The gate does not read `date-released`.
- `catalog.json` `"updated"` stays frozen. Do not touch it.
- Do not edit pack content, `packs/*/PACK.yaml`, `packs/*/SKILL.md`, or chapter files.
- Do not edit `.github/workflows/validate.yml` or any heredoc. A heredoc edit would force a `test_ci_gate.py` parity update this run does not need.
- Do not edit anything under `tooling/`.
- Do not create the GitHub Release. The user does that after pushing the tag.
- Check 4 reads three files and demands they agree: `RELEASE-INFO.txt` `Version:`, the first `## [x.y.z]` heading in `CHANGELOG.md` (`re.search(r"^##\s*\[(\d+\.\d+\.\d+)\]", cl, re.M)`), and `.claude-plugin/plugin.json` `version`. Check 4a reads `version:\s*"([0-9]+\.[0-9]+\.[0-9]+)"` in `docs/products/website/01-jgs-se-knowledge-packs.yaml` and `docs/products/website/catalog.yaml`. `[site-version]` reads three `docs/index.html` loci: `"softwareVersion":\s*"(\d+\.\d+\.\d+)"`, `REV <b>(\d+\.\d+\.\d+)</b>`, and `<span class="label">Rev</span><b>(\d+\.\d+\.\d+)</b>`. Check 19 reads the same masthead and footer patterns on every `docs/packs/<slug>/index.html`.
- Fresh empty `## [Unreleased]` must sit above `## [1.23.0]: 2026-10-28`. Check 4 matches the first `## [x.y.z]` heading. An Unreleased heading has no version digits, so the first match is 1.23.0. A missing Unreleased heading would still pass the regex, but the spec requires the empty heading so the next cut has somewhere to land.

## Codebase context

Ad-hoc context, re-checked on branch `packages-2026-10-27` while writing this plan (HEAD `f79d140`, later than the spec's `53d4413`; the extra commits are planning docs and do not change version surfaces). Precedent tag: `v1.22.1` is an annotated tag whose message is `jgs-se-knowledge-packs 1.22.1`.

- Version single-source today is local check 4 plus CI "Version single-source" in `.github/workflows/validate.yml`. Neither reads `.cursor-plugin/plugin.json`. Local-only check 6b reads the cursor skills list, by design.
- `tooling/gen_packs_page.py` `version()` reads `Version:\s*([0-9]+\.[0-9]+\.[0-9]+)` from `RELEASE-INFO.txt`. `tooling/gen_pack_pages.py` imports that function. Both stamp masthead `REV <b>{ver}</b>` and footer `<span class="label">Rev</span><b>{ver}</b>`. `write_sitemap()` always rewrites `docs/sitemap.xml` and sets `<lastmod>` to `date.today().isoformat()` on every loc. That file is part of the commit, not noise.
- Live counts: `catalog.json` holds 73 packs. `packs/` holds 82 directories (73 content, 8 signposts, 1 orchestrator). `.claude-plugin/plugin.json` declares 82 skill paths. `.cursor-plugin/plugin.json` declares 79 and sits at `"version": "1.22.0"`. `docs/packs/*/index.html` holds 73 pages.
- Current hand-edit anchors, all `1.22.1` except where noted:
  - `RELEASE-INFO.txt` lines 3-5: `Version:    1.22.1`, `Tag:        v1.22.1`, `Staged:     2026-09-27T00:00:00Z`
  - `CHANGELOG.md` line 12: `## [Unreleased]`. Lines 16-27 are the Added and Changed bullets this cut rewrites. Line 29: `## [1.22.1]: 2026-10-11`
  - `.claude-plugin/plugin.json` line 4: `"version": "1.22.1"`
  - `docs/products/website/01-jgs-se-knowledge-packs.yaml` line 15: `version: "1.22.1"`
  - `docs/products/website/catalog.yaml` line 13: `version: "1.22.1"`
  - `README.md` line 10 badge URL and `alt="Version 1.22.1"`, line 63 `(version 1.22.1)`, line 267 `Current: 1.22.1`
  - `CITATION.cff` line 4: `version: 1.22.1`. Line 5 `date-released: 2026-09-27` stays.
  - `docs/index.html` four loci, lines 31, 76, 228, and 240. Exact strings are in Task 1 Step 8.
- Twelve `tooling/test_*.py` modules: `test_catalog_live_set.py`, `test_catalogue_count.py`, `test_ci_gate.py`, `test_gen_pack_pages.py`, `test_generate_capability_map.py`, `test_html_assets.py`, `test_install_guard.py`, `test_link_policy.py`, `test_pack_quality.py`, `test_routing_map.py`, `test_source_watch.py`, `test_validate_pack.py`.

## Research

research: section-url

Release conventions in the spec, not re-derived here. Keep a Changelog 1.1.0 (https://keepachangelog.com/en/1.1.0/), Semantic Versioning (https://semver.org/), annotated tags as the git default release marker (https://git-scm.com/docs/git-tag).

## File map

Hand-edit in Task 1:

- `RELEASE-INFO.txt`
- `CHANGELOG.md`
- `.claude-plugin/plugin.json`
- `docs/products/website/01-jgs-se-knowledge-packs.yaml`
- `docs/products/website/catalog.yaml`
- `README.md`
- `CITATION.cff`
- `docs/index.html`

Regenerate and commit in Task 1 (do not hand-edit):

- `docs/packs.html`
- `docs/sitemap.xml`
- `docs/packs/<slug>/index.html` for all 73 catalog packs

Not touched:

- `.cursor-plugin/plugin.json` (D2)
- `catalog.json`
- anything under `packs/`
- `.github/workflows/validate.yml`
- `tooling/`

Task 2 commits the Task 1 diff and creates the tag. Task 3 reads only. No commit in Task 3.

---

## Task 1: Edit version surfaces, rewrite changelog, regenerate pages

**Gate:** gate-enforced (spec steps 1-9; smoke gate must pass before Task 2 commits).

**Files:**
- Modify: `RELEASE-INFO.txt`
- Modify: `CHANGELOG.md`
- Modify: `.claude-plugin/plugin.json` (version line only)
- Modify: `docs/products/website/01-jgs-se-knowledge-packs.yaml` (version line only)
- Modify: `docs/products/website/catalog.yaml` (version line only)
- Modify: `README.md` (every `1.22.1`)
- Modify: `CITATION.cff` (version line only)
- Modify: `docs/index.html` (four loci)
- Regenerate: `docs/packs.html`, `docs/sitemap.xml`, `docs/packs/<slug>/index.html` (73 files)
- Test: `python tooling/check_release.py` and `python tooling/test_ci_gate.py` on the working tree

**Interfaces:**
- Consumes: nothing from an earlier task.
- Produces: a dirty working tree whose version surfaces all read `1.23.0`, whose `## [Unreleased]` sits above `## [1.23.0]: 2026-10-28`, and whose smoke gate prints `RELEASE CHECK: PASS (v1.23.0 @ <short-sha>)`. That sha is HEAD before the release commit. Task 2 commits this tree and re-runs the gate.

**Model:** standard

- [ ] **Step 1: Confirm branch and that version files are clean**

```bash
git branch --show-current
git status -sb -- RELEASE-INFO.txt CHANGELOG.md .claude-plugin/plugin.json docs/products/website/01-jgs-se-knowledge-packs.yaml docs/products/website/catalog.yaml README.md CITATION.cff docs/index.html docs/packs.html docs/sitemap.xml .cursor-plugin/plugin.json catalog.json
```

Expected: branch `packages-2026-10-27`. The listed paths show no local modifications. If any of them is already dirty, stop and report. Do not layer this cut on an unrelated edit.

- [ ] **Step 2: Edit `RELEASE-INFO.txt` (spec step 1, D4)**

Replace the three version lines. Leave Product, Vendor, and Licence lines as they are.

```text
Version:    1.23.0
Tag:        v1.23.0
Staged:     2026-10-28T00:00:00Z
```

The file after the edit, whole file:

```text
jgs-se-knowledge-packs — Release
Product:    jgs-se-knowledge-packs
Version:    1.23.0
Tag:        v1.23.0
Staged:     2026-10-28T00:00:00Z
Vendor:     JG Systems Consulting Ltd.
Licence:    MIT (tooling); pack content under each source's own licence (see NOTICE)
```

- [ ] **Step 3: Rewrite the changelog section (spec step 2, D2, D3, D6, D7)**

Replace the block from `## [Unreleased]` through the blank line before `## [1.22.1]: 2026-10-11`. Do not edit `## [1.22.1]` or any older section. Do not list planning-doc commits (D6).

Replacement, verbatim from the spec Changelog content section, with the empty Unreleased heading the spec's step 2 requires:

```markdown
## [Unreleased]

## [1.23.0]: 2026-10-28

### Added

- `fhwa-its-se` content pack from Systems Engineering for ITS, fourth generation (December 2022), reconstructed notes, registered on the catalogue surfaces.
- `jsp-936` content pack from JSP 936 Part 1 Directive V1.1, reconstructed notes, registered on the catalogue surfaces.

### Changed

- `.claude-plugin/plugin.json` declares all 82 skill paths. 73 content packs, 8 signposts, 1 orchestrator. The 80 figure was true on 2026-10-26 and went stale when `jsp-936` and `fhwa-its-se` registered.
- Per-pack landing pages now cover the full live catalogue, `docs/packs/<slug>/index.html` for all 73 content packs, with `docs/sitemap.xml` generated from `catalog.json` rather than from the run list. A title-suffix collision is fixed for pack titles that already end in a colon phrase.
- CI trust gates added since 1.22.1: pack licence and signpost shape, html-assets over `docs/*.html` and pack landing pages, sitemap and pack-page REV on the release gate, and `actions/checkout` pinned to the v4 commit SHA. The CONTRIBUTING registration checklist and pre-tag section were expanded to match.
- Doc-truth fixes: PACK-SPEC install path points at the root installer, the website YAML family inventory matches the live catalogue, and shipped META keys and PACK-BACKLOG pointers are dropped from the build orchestrator.

### Noted, not a change

- `.cursor-plugin/plugin.json` stays at version 1.22.0 and lists 79 skills. Its version is outside the single-source by design. Closing that gap is P60.

Catalogue line: 73 content packs, 8 signposts, 1 orchestrator, 82 skills.
```

The next heading after that block stays `## [1.22.1]: 2026-10-11`.

- [ ] **Step 4: Edit `.claude-plugin/plugin.json` (spec step 3)**

Change line 4 only:

```json
  "version": "1.23.0",
```

Do not touch the `skills` array. Do not reformat the file.

- [ ] **Step 5: Edit the two website YAMLs (spec step 4)**

In `docs/products/website/01-jgs-se-knowledge-packs.yaml` line 15, replace `version: "1.22.1"` with:

```yaml
version: "1.23.0"
```

In `docs/products/website/catalog.yaml` line 13, replace `version: "1.22.1"` with:

```yaml
    version: "1.23.0"
```

Keep the four-space indent on the catalog.yaml line. Do not touch `catalog.json`. Do not change any `N packs` claim.

- [ ] **Step 6: Edit `README.md` (spec step 5)**

Replace every `1.22.1` in the file. Three loci today:

Line 10, both the badge URL and the alt text:

```html
  <img src="https://img.shields.io/badge/version-1.23.0-green" alt="Version 1.23.0">
```

Line 63:

```text
Repository: https://github.com/jgsystemsconsulting/jgs-se-knowledge-packs (version 1.23.0).
```

Line 267:

```markdown
See [CHANGELOG.md](CHANGELOG.md). Current: 1.23.0.
```

Then confirm the file has no remaining `1.22.1`:

```bash
rg -n "1\.22\.1" README.md
```

Expected: no matches. If a match remains, replace it with `1.23.0` and re-run. The grep at the end of this task is the completeness check. Do not rely on the three-locus list alone.

- [ ] **Step 7: Edit `CITATION.cff` (spec step 6)**

Change line 4 only:

```yaml
version: 1.23.0
```

Leave `date-released: 2026-09-27` as it is.

- [ ] **Step 8: Edit `docs/index.html` at four loci (spec step 7)**

The gate checks three. The fourth, the provenance label, is not gated and goes stale silently, so edit it too. Replace `1.22.1` with `1.23.0` in each of these four strings and nowhere else in the file:

```html
"softwareVersion":"1.23.0"
REV <b>1.23.0</b>
REV: <span style="color:var(--text)">1.23.0</span>
<span class="label">Rev</span><b>1.23.0</b>
```

Line 31 is the softwareVersion string. Line 76 is the masthead REV. Line 228 is the provenance label. Line 240 is the footer Rev.

Confirm:

```bash
rg -n "1\.22\.1" docs/index.html
```

Expected: no matches.

- [ ] **Step 9: Regenerate pages (spec step 8)**

`RELEASE-INFO.txt` must already say `Version:    1.23.0`. The generators read it at render time. Run both, in this order:

```bash
python tooling/gen_pack_pages.py
python tooling/gen_packs_page.py
```

Expected: both exit 0. `gen_pack_pages.py` prints `wrote docs/sitemap.xml (73 live catalog packs)` and rewrites all 73 `docs/packs/<slug>/index.html` files. `docs/sitemap.xml` `<lastmod>` stamps today's date on every loc. Commit that file with the rest. Do not revert it as noise.

Confirm generated REV loci moved:

```bash
python -c "
import pathlib
root = pathlib.Path('docs/packs')
pages = list(root.glob('*/index.html'))
stale = [str(p) for p in pages if '1.22.1' in p.read_text(encoding='utf-8')]
print('pages', len(pages))
print('stale', len(stale))
html = pathlib.Path('docs/packs.html').read_text(encoding='utf-8')
print('packs.html has 1.23.0', '1.23.0' in html)
print('packs.html has 1.22.1', '1.22.1' in html)
"
```

Expected: `pages 73`, `stale 0`, `packs.html has 1.23.0 True`, `packs.html has 1.22.1 False`. If stale is not 0, do not hand-edit the pages. Re-read `RELEASE-INFO.txt` and re-run both generators.

- [ ] **Step 10: Pre-commit smoke gate (spec step 9)**

```bash
python tooling/check_release.py
python tooling/test_ci_gate.py
```

Expected: `check_release.py` prints `RELEASE CHECK: PASS (v1.23.0 @ <short-sha>)` and exits 0. That sha is current HEAD, not the release sha. Record it only so Task 2 can prove the post-commit sha differs. `test_ci_gate.py` exits 0 with no edits. No heredoc pin changes in this run, so the parity assertions must pass without edits.

If `check_release.py` fails on a version disagreement, fix the named surface from Steps 2-9 and re-run. If it fails on pack content, `catalog.json`, routing, classification, or any check this plan did not touch, stop and report. Do not fix pack content here. If `test_ci_gate.py` fails, the cause is outside this spec. Stop. Do not edit `.github/workflows/validate.yml`.

Do not commit in this task. Task 2 commits.

---

## Task 2: Commit, post-commit receipt gate, annotated tag

**Gate:** gate-enforced (spec steps 10-12; the post-commit PASS line is the receipt the tag binds to).

**Files:**
- Commit: every path Task 1 changed. No new edits.
- Test: `python tooling/check_release.py` on the committed tree, then `git rev-parse v1.23.0^{}`

**Interfaces:**
- Consumes: the dirty tree from Task 1, smoke gate already PASS.
- Produces: one commit on `packages-2026-10-27` with subject `docs: complete the 1.23.0 release surfaces`, and annotated tag `v1.23.0` whose peeled commit equals that commit. The PASS line sha equals the short HEAD printed in Step 2.

**Model:** standard

- [ ] **Step 1: Stage only the release surfaces**

```bash
git add -- \
  RELEASE-INFO.txt \
  CHANGELOG.md \
  .claude-plugin/plugin.json \
  docs/products/website/01-jgs-se-knowledge-packs.yaml \
  docs/products/website/catalog.yaml \
  README.md \
  CITATION.cff \
  docs/index.html \
  docs/packs.html \
  docs/sitemap.xml \
  docs/packs
git diff --cached --stat
git diff --cached --name-only -- .cursor-plugin/plugin.json catalog.json .github/workflows/validate.yml tooling packs
```

Expected: cached diff is the eight hand-edited files plus `docs/packs.html`, `docs/sitemap.xml`, and 73 paths under `docs/packs/`. The second command prints nothing. If it prints a path, unstage that path and stop if the path was edited. Those paths are out of scope.

If the second command printed a path, unstage it. Example for the four forbidden trees:

```bash
git restore --staged -- .cursor-plugin/plugin.json catalog.json .github/workflows/validate.yml tooling packs
```

- [ ] **Step 2: Commit (spec step 10)**

```bash
git commit -m "docs: complete the 1.23.0 release surfaces"
git rev-parse HEAD
git rev-parse --short HEAD
```

Record both. `SHORT` is the short HEAD printed above. This commit is the release commit. Do not amend it after the tag exists.

- [ ] **Step 3: Post-commit receipt gate (spec step 11)**

Working tree must be clean of release-surface edits before this run. The gate reads the files on disk and the short HEAD sha from the command in Step 2.

```bash
python tooling/check_release.py
git rev-parse --short HEAD
```

Expected: the script prints `RELEASE CHECK: PASS (v1.23.0 @ <short-sha>)` and exits 0. `<short-sha>` equals the `SHORT` from Step 2, character for character. An `@ no-git` receipt never satisfies this. A sha that still matches the pre-commit HEAD means the commit did not land. Stop and do not tag.

This receipt is what the tag and the Testing section bind to.

- [ ] **Step 4: Create the annotated tag (spec step 12, D5)**

```bash
git tag -a v1.23.0 -m "jgs-se-knowledge-packs 1.23.0"
git rev-parse v1.23.0^{}
git rev-parse HEAD
git for-each-ref refs/tags/v1.23.0 --format='%(objecttype)'
```

Expected: `git rev-parse v1.23.0^{}` equals `git rev-parse HEAD`. `for-each-ref` prints `tag`. If the peeled commit differs, delete the local tag (`git tag -d v1.23.0`) and stop. Do not push a bad tag. There is nothing to push anyway.

- [ ] **Step 5: Run the twelve test modules**

```bash
for t in tooling/test_*.py; do python "$t" || exit 1; done
```

Expected: twelve modules, each exits 0. The set is `test_catalog_live_set.py`, `test_catalogue_count.py`, `test_ci_gate.py`, `test_gen_pack_pages.py`, `test_generate_capability_map.py`, `test_html_assets.py`, `test_install_guard.py`, `test_link_policy.py`, `test_pack_quality.py`, `test_routing_map.py`, `test_source_watch.py`, `test_validate_pack.py`. If one fails, the cause is outside this spec. Stop. Do not edit `tooling/` or `.github/workflows/validate.yml` to make it pass.

- [ ] **Step 6: Confirm no push**

```bash
git status -sb
git rev-parse v1.23.0
git ls-remote --tags origin v1.23.0
```

Expected: status shows `packages-2026-10-27` ahead of its remote. It must not show a successful push. The remote tag listing prints nothing, because the tag exists only locally. Stop here. Do not push the branch. Do not push the tag. Do not merge to `main`. Do not open a pull request. Do not create the GitHub Release.

---

## Task 3: Verification sweep

**Gate:** not gate-enforced (read-only; no commit).

**Files:**
- Read: the live version surfaces, `CHANGELOG.md`, `.cursor-plugin/plugin.json`, `CONTRIBUTING.md`
- Test: grep plus the CONTRIBUTING pre-tag checks, re-run as evidence

**Interfaces:**
- Consumes: the tag and the release commit from Task 2.
- Produces: a pass/fail note in the task report. No file edits. No commit.

**Model:** flash

- [ ] **Step 1: Grep stale 1.22.1 off the live surfaces**

`CHANGELOG.md` may keep `1.22.1` inside the `## [1.22.1]` section and nowhere else. `.cursor-plugin/plugin.json` keeps `1.22.0` (D2). Generated pages and `docs/sitemap.xml` must not contain `1.22.1`.

```bash
python -c "
import pathlib, re
root = pathlib.Path('.')
live = [
    'RELEASE-INFO.txt',
    'README.md',
    'CITATION.cff',
    '.claude-plugin/plugin.json',
    'docs/products/website/01-jgs-se-knowledge-packs.yaml',
    'docs/products/website/catalog.yaml',
    'docs/index.html',
    'docs/packs.html',
    'docs/sitemap.xml',
]
bad = []
for rel in live:
    text = pathlib.Path(rel).read_text(encoding='utf-8')
    if '1.22.1' in text:
        bad.append(rel)
for p in pathlib.Path('docs/packs').glob('*/index.html'):
    if '1.22.1' in p.read_text(encoding='utf-8'):
        bad.append(str(p))
cl = pathlib.Path('CHANGELOG.md').read_text(encoding='utf-8')
# 1.22.1 allowed only inside the historical 1.22.1 section.
head, sep, rest = cl.partition('## [1.22.1]')
if '1.22.1' in head:
    bad.append('CHANGELOG.md (above ## [1.22.1])')
cursor = pathlib.Path('.cursor-plugin/plugin.json').read_text(encoding='utf-8')
if '\"version\": \"1.22.0\"' not in cursor:
    bad.append('.cursor-plugin/plugin.json version is not 1.22.0')
if '1.23.0' in cursor:
    bad.append('.cursor-plugin/plugin.json contains 1.23.0')
print('bad', len(bad))
for b in bad:
    print(b)
"
```

Expected: `bad 0`. Any hit is a miss. Do not fix it in this task. Report the path and stop so Task 1 can be reopened. Do not commit a fix from Task 3.

- [ ] **Step 2: CONTRIBUTING "Before you tag" checks, verbatim in substance**

From `CONTRIBUTING.md` section "Before you tag":

- Run `python tooling/check_release.py` on the exact commit you are about to tag. PASS is required. The PASS line reads `RELEASE CHECK: PASS (v<version> @ <short-sha>)` and the sha must match the commit you are about to tag. An `@ no-git` receipt never satisfies it.
- CI green is necessary but not sufficient.
- Local-only classes: full pack validation, source-watch freshness, generator replay (capability map and packs.html), and tracked-sources emptiness. The check-by-check list stays in the header of `.github/workflows/validate.yml` and in the docstring of `tooling/check_release.py`. Do not treat this section as that list.
- Do not cut a tag or a GitHub Release on CI green alone.

Re-run the receipt and bind it to the tag:

```bash
python tooling/check_release.py
echo "HEAD $(git rev-parse --short HEAD)"
echo "TAG  $(git rev-parse --short v1.23.0^{})"
git for-each-ref refs/tags/v1.23.0 --format='%(objecttype) %(subject)'
```

Expected: PASS line `RELEASE CHECK: PASS (v1.23.0 @ <short-sha>)`. HEAD short sha, tag peeled short sha, and the PASS sha are the same string. `for-each-ref` prints `tag` and subject `jgs-se-knowledge-packs 1.23.0`.

`check_release.py` already aggregates the local-only classes (pack validation, source-watch, generator replay, tracked-sources emptiness). A PASS on this commit is the evidence. Do not re-implement those checks by hand. Do not treat a prior CI green run as a substitute.

- [ ] **Step 3: No-push evidence**

```bash
git status -sb
git ls-remote --tags origin v1.23.0
```

Expected: branch `packages-2026-10-27` is ahead of its remote. `ls-remote` prints nothing for `v1.23.0`. No push happened. Stop. Do not push.

---

## Testing

Bound to the release commit, not to the pre-commit smoke run.

- `python tooling/check_release.py` prints `RELEASE CHECK: PASS (v1.23.0 @ <short-sha>)` and the sha equals the short HEAD of the release commit. An `@ no-git` receipt never satisfies it. CI green is necessary and not sufficient. Do not cut the tag on CI green alone.
- The twelve `tooling/test_*.py` modules pass (`for t in tooling/test_*.py; do python "$t"; done`), including `tooling/test_ci_gate.py`. No heredoc pin changes, so the parity assertions must pass without edits. If one fails, the cause is outside this spec and the run stops.
- Grep for `1.22.1` across the live surfaces returns nothing: `RELEASE-INFO.txt`, `README.md`, `CITATION.cff`, `.claude-plugin/plugin.json`, both website YAMLs, `docs/index.html`, `docs/packs.html`, `docs/sitemap.xml`, `docs/packs/*/index.html`. `CHANGELOG.md` keeps `1.22.1` inside the `## [1.22.1]` section and nowhere else. `.cursor-plugin/plugin.json` keeps `1.22.0` (D2).
- `git rev-parse v1.23.0^{}` equals the release commit. The tag object type is `tag` (`git for-each-ref refs/tags/v1.23.0` with format `%(objecttype)`).
- `git status -sb` shows the branch ahead of its remote and shows no push has happened.

CONTRIBUTING "Before you tag", in substance: run `python tooling/check_release.py` on the exact commit tagged; PASS line reads `RELEASE CHECK: PASS (v<version> @ <short-sha>)` and the sha matches that commit; local-only classes (full pack validation, source-watch freshness, generator replay, tracked-sources emptiness) are inside that gate, not a second list to invent; do not cut a tag or a GitHub Release on CI green alone.

## Do not

- Do not push the branch or the tag.
- Do not merge to `main`. Branch integration stays the user's decision. The finishing-branch menu stays open.
- Do not open a pull request.
- Do not edit pack content, `packs/*/PACK.yaml`, `packs/*/SKILL.md`, or chapter files.
- Do not change `catalog.json`, including its `updated` stamp.
- Do not edit a version string anywhere outside the files named above. `map_version`, `source_version`, and historical changelog sections stay as they are.
- Do not bump `.cursor-plugin/plugin.json`, and do not extend the version single-source to read it. That is P60.
- Do not edit `.github/workflows/validate.yml` or any heredoc. A heredoc edit would force a `test_ci_gate.py` parity update this run does not need.
- Do not list planning-doc commits in the changelog (D6).
- Do not create the GitHub Release. The user does that after pushing the tag.

## Self-review

Spec coverage: D1 is the 1.23.0 bump in Task 1 Steps 2-8. D2 is the cursor-manifest non-edit, the Noted bullet in Task 1 Step 3, and the Task 3 version assertion. D3 is the 82-path Changed bullet, copied verbatim. D4 is the `Staged:` stamp in Task 1 Step 2. D5 is the tag command in Task 2 Step 4 and the no-push stop in Task 2 Step 6. D6 is the changelog rewrite, which contains no spec, plan, EXECUTED, or IVL line. D7 is the landing-pages bullet and the CI-gates bullet, each its own Changed item. Spec steps 1-8 are Task 1 Steps 2-9. Spec step 9 is Task 1 Step 10. Spec steps 10-12 are Task 2 Steps 2-4. The order is smoke gate, then commit, then post-commit receipt gate, then tag. Testing items are Task 2 Steps 3-6 and Task 3. The Do not list is copied verbatim. `date-released` left at 2026-09-27 because spec step 6 names only `version:`.

Placeholder scan: no open items, no cross-task shorthand. Commands, replacement strings, and expected output are written out. `SHORT` is the short HEAD printed after the commit, not an open choice.

Type consistency: version string is `1.23.0` on every surface. Tag name is `v1.23.0`. Commit subject is `docs: complete the 1.23.0 release surfaces`. Tag message is `jgs-se-knowledge-packs 1.23.0`. PASS receipt form is `RELEASE CHECK: PASS (v1.23.0 @ <short-sha>)`. Check 4's first `## [x.y.z]` match is `## [1.23.0]: 2026-10-28` because `## [Unreleased]` has no version digits.

## Out of scope

- P60, bringing `.cursor-plugin/plugin.json` under the version single-source and mirroring check 6b into CI. (The manifest is not short three skills: `easa-rules`, `med-device-eu`, and `sebok` are `commercial_use: false` and correctly excluded; 79 is the exact eligible count.)
- Pushing, merging, and the GitHub Release.
- Any pack content change found during the gate run. A gate failure caused by pack content stops the run and gets reported, not fixed here.
