# Context: validate-pack-signpost-parity (2026-09-14)

## Context brief

**Primary question**: Teach `tooling/validate_pack.py` the `kind: signpost` pack shape so `--all` and `tooling/check_release.py` agree that a clean release-ready tree is valid.

**Sub-questions**:
1. Exact `validate_pack.check_pack` requirements and `--all` iteration paths (line refs).
2. How `check_release` detects and pre-filters signpost dirs before calling `validate_pack`.
3. Live signpost pack shapes vs a normal content pack.
4. Reproduced disagreement (exact FAIL lines and exit codes).
5. Package constraints + design choices the spec must settle.

**Success criteria**: SC1 code paths; SC2 check_release pre-filter; SC3 live shapes; SC4 exit-code disagreement; SC5 design constraints for relaxed signpost checks and doc alignment.

**Out of scope** (ledger P6): signpost pack body or citation edits; CI workflow edits (P4/P5); pytest; new pack content rules.

**Budget**: single-pass context gate.

**Workspace baseline**: HEAD `a42e3d9611df7d5e54abc52661e6fd8d9d0b8380` on `main`; untracked `docs/superpowers/` only.

**Parent-verified package facts** (packages.md P6): standalone `--all` treats every `packs/*` dir as a full content pack; signposts intentionally lack `LICENSE` and `chapters/`; `check_release` pre-filters signposts and passes; tools disagree on what valid means.

## Findings

Grades: CORROBORATED 8, SINGLE-SOURCE 7, CONFLICTED 0, STALE 2 (CONCERNS / package line refs after P4 growth).

| # | Claim | Grade |
|---|-------|-------|
| 1 | `check_pack` always requires LICENSE + chapters/ at L67-74 | CORROBORATED |
| 2 | `--all` / bare argv iterates every `packs/*` dir at L117-118 | CORROBORATED |
| 3 | Exit 0 only when `total_fail == 0`; any FAIL returns 1 (L127-138) | CORROBORATED |
| 4 | Module docstring lists LICENSE + chapters as universal required files (L11-12) | SINGLE-SOURCE |
| 5 | `check_release` builds `signpost_dirs` via `kind: signpost` on `packs/*/SKILL.md` (L132-135) | CORROBORATED |
| 6 | Pack validate loop excludes `signpost_dirs` before `validate_pack.check_pack` (L184-191) | CORROBORATED |
| 7 | Live signposts: `omg-signpost`, `se-standards-signpost` only (SKILL.md + PACK.yaml) | CORROBORATED |
| 8 | Content pack contrast has LICENSE + chapters/ (+ optional furniture) | CORROBORATED |
| 9 | Reproduced: `--all` exits 1 with 63/65; `check_release` exits 0 PASS | CORROBORATED |
| 10 | Per-signpost FAIL errors are exactly missing LICENSE + missing chapters/ | CORROBORATED |
| 11 | Documented run commands live in validate_pack docstring, CONTRIBUTING, PACK-SPEC | SINGLE-SOURCE |
| 12 | CONCERNS standalone-validator concern still correct in substance; pack counts and check_release line refs stale | STALE/SS |
| 13 | Package evidence cites check_release.py:141; live filter is ~L184-185 | STALE |
| 14 | P6 in_scope/out_scope as ledger; stdlib-only already true for validate_pack | CORROBORATED |
| 15 | Signpost PACK.yaml already carries mandatory scalar fields + `kind: signpost` | SINGLE-SOURCE |

## Exact current state (quoted)

### validate_pack.py — required files (`check_pack`, L57-74)

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

No branch reads `kind:` before these checks. Signpost and content packs share one requirement set.

### validate_pack.py — remaining checks (still unconditional when files exist)

| Check | Lines | Behavior |
|-------|-------|----------|
| SKILL.md YAML frontmatter | 77-90 | require `name` + `description`; `name` == folder slug |
| Chapter links in SKILL.md body | 91-94 | every `(chapters/chNN-*.md)` link must exist |
| PACK.yaml mandatory fields | 97-109 | `REQUIRED_PACK_FIELDS` = slug, title, publisher, license, license_tier, commercial_use; tier in {1,2,3}; slug == folder |

### validate_pack.py — CLI / `--all` (L114-138)

```python
if "--all" in args or not args:
    packs = sorted(p for p in (repo_root / "packs").iterdir() if p.is_dir())
else:
    packs = [Path(a).resolve() for a in args]
...
errs = check_pack(pack)
...
return 1 if total_fail else 0
```

- Empty argv behaves like `--all`.
- Every directory under `packs/` is a candidate; no name or frontmatter filter.
- Print `FAIL`/`PASS` per pack; summary `passed/total`; exit 1 if any FAIL.

### validate_pack.py — docstring usage (L7-19)

Documents:
- `python tooling/validate_pack.py packs/<slug>`
- `python tooling/validate_pack.py --all`
- required files always include `LICENSE` and `chapters/ with >=1 chapter`
- exit 0 = all checked packs pass; 1 = at least one failure
- stdlib only

### check_release.py — signpost detection (L132-135)

```python
signpost_dirs = {p.parent for p in ROOT.glob("packs/*/SKILL.md")
                 if re.search(r"^kind:\s*signpost\s*$", p.read_text(encoding="utf-8", errors="ignore"), re.M)}
```

Same regex used for the link-policy exemption (L146: `if p.parent in signpost_dirs: continue`).

### check_release.py — pack-validation interplay (L184-191)

```python
import validate_pack  # type: ignore
packs = sorted(p for p in (ROOT / "packs").iterdir() if p.is_dir() and p not in signpost_dirs)
for pack in packs:
    perrs = validate_pack.check_pack(pack)
    for e in perrs:
        fail(errs, f"[pack:{pack.name}] {e}")
```

- Pre-filter only: does not teach `validate_pack` about signposts.
- Delegates structure/tier checks to `validate_pack.check_pack` for content packs only.
- Downstream uses of the filtered `packs` list also skip signposts: RR-S-13 When-to-use/prereq (L195-210), SKILLS.md count vs pack count (L225-232).
- Docstring check 5 still says "Every pack passes tooling/validate_pack.py" while the implementation means every non-signpost pack.

## Live pack shapes

### Signpost packs (2)

| Path | Contents |
|------|----------|
| `packs/omg-signpost/` | `SKILL.md`, `PACK.yaml` only |
| `packs/se-standards-signpost/` | `SKILL.md`, `PACK.yaml` only |

Absent by design: `LICENSE`, `chapters/`, glossary/patterns/cheatsheet furniture.

**SKILL.md frontmatter** (both):

```yaml
---
name: <slug>
kind: signpost
description: "..."
---
```

- `omg-signpost/SKILL.md:3` and `se-standards-signpost/SKILL.md:3`: `kind: signpost`
- Body is citation/index prose (download pointers). No `chapters/chNN-*.md` links required for structure; omg body intentionally contains OMG URLs (link-policy exemption target).

**PACK.yaml** (both carry):

- `slug`, `kind: signpost`, `title`, `publisher`, `license: "MIT"`, `license_tier: 2`, `commercial_use: true`, folded `notes:`
- Mandatory scalars for `REQUIRED_PACK_FIELDS` are present today; `kind` is extra and ignored by `parse_simple_yaml` consumers except as a human/marker field.

### Content pack contrast (`packs/requirements-writing/`)

| Present | Notes |
|---------|-------|
| `SKILL.md` | name + description; no `kind:`; has `## When to use`, Prerequisites, chapter index |
| `PACK.yaml` | full mandatory fields; no `kind: signpost` |
| `LICENSE` | required by validator |
| `chapters/` | `ch*.md` files required |
| optional | `cheatsheet.md`, `glossary.md`, `patterns.md` |

Repo pack dir count at gate time: **65** under `packs/` (63 content + 2 signpost).

## Disagreement reproduced (this workspace)

### Standalone validator

```text
$ python tooling/validate_pack.py packs/omg-signpost packs/se-standards-signpost
FAIL  omg-signpost
        - missing LICENSE (must reproduce the source's terms)
        - missing chapters/ directory
FAIL  se-standards-signpost
        - missing LICENSE (must reproduce the source's terms)
        - missing chapters/ directory
0/2 pack(s) passed.
# exit 1

$ python tooling/validate_pack.py --all
... (63 PASS lines) ...
FAIL  omg-signpost
        - missing LICENSE (must reproduce the source's terms)
        - missing chapters/ directory
...
FAIL  se-standards-signpost
        - missing LICENSE (must reproduce the source's terms)
        - missing chapters/ directory
...
63/65 pack(s) passed.
# exit 1

$ python tooling/validate_pack.py packs/requirements-writing
PASS  requirements-writing
1/1 pack(s) passed.
# exit 0
```

### Release gate

```text
$ python tooling/check_release.py
...
RELEASE CHECK: PASS — repo is release-ready against the mechanical gate.
# exit 0
```

**Exact exit-code disagreement**: on the same clean tree, documented `validate_pack.py --all` returns **1** (two signpost FAILs); `check_release.py` returns **0**. Validity is not shared: release gate defines valid = content packs only; standalone defines valid = every `packs/*` dir must look like a content pack.

## Concerns / planning notes

`.planning/codebase/CONCERNS.md` (standalone-validator section, ~L7-13 and Known Bugs ~L55-61):

- Issue statement matches live behavior.
- Stale counts: text still says "46/48 pack(s) passed"; live is **63/65**.
- Stale `check_release` line refs (CONCERNS and packages evidence still cite older lines; live signpost filter for pack validate is **L184-185**, detection **L134-135**).
- Fix approach matches P6 in_scope: detect `kind: signpost` in SKILL.md and relax LICENSE/chapters so both tools agree without relying on pre-filter alone.

## Documented run commands (alignment targets)

| Location | What it says today |
|----------|--------------------|
| `tooling/validate_pack.py` L7-19 | `--all` + per-slug; required files always include LICENSE + chapters/ |
| `CONTRIBUTING.md` ~L38 | `python tooling/validate_pack.py packs/<slug>` only |
| `CONTRIBUTING.md` ~L54 | "CI runs validate_pack.py on every pack" (does not mention signpost carve-out or `--all`) |
| `docs/PACK-SPEC.md` ~L94-98 | per-slug command; checks list implies full content shape |
| `docs/SOURCE-VETTING.md` ~L248 | CI enforces via validate_pack (tier mechanics) |
| `README.md` ~L179-180 | documents signposts as citation-only, not packs, zero reproduced content |
| `docs/capability-pack-map.md` L12 | signposts have no chapters and are not mapped |

P6 "align documented run commands" means at least the validator docstring (and any doc that claims `--all` / "every pack" without the signpost kind) must match the new behavior so contributors are not told a command that fails on mainline.

## Package constraints (P6)

**in_scope**:
- Detect `kind: signpost` in SKILL.md frontmatter inside `validate_pack.check_pack` / `--all`.
- Relax LICENSE and `chapters/` requirements for signposts only.
- Align documented run commands so `--all` and `check_release` agree on a clean tree.

**out_scope**:
- Signpost pack body or citation edits.
- CI workflow edits (P4/P5).
- pytest.
- New pack content rules.

**Implied engineering constraints** (from module + ledger + repo norms):
- Minimal diff; stdlib only (already true: `re`, `sys`, `pathlib`).
- Do not invent new mandatory files or body sections for signposts.
- Do not require editing the two signpost packs to pass.
- Prefer teaching `validate_pack` over leaving correctness only in `check_release` pre-filter (CONCERNS fix approach).

## Design considerations the spec must settle

1. **Where to detect `kind: signpost`**
   - (Recommended) Inside `check_pack`, after confirming `SKILL.md` exists: same regex as `check_release` (`^kind:\s*signpost\s*$`, multiline). One definition of "is signpost" for single-pack and `--all` paths.
   - Do not key only on directory name (`*-signpost`); live marker is frontmatter.
   - PACK.yaml also has `kind: signpost` today; treating SKILL.md as SoT matches check_release and P6 wording. Spec may note PACK.yaml as optional corroboration, not a second required detector.
   - Missing SKILL.md remains a hard fail even for would-be signposts (cannot prove kind).

2. **What "relaxed" means for signposts (which checks still apply)**

   | Requirement | Content pack | Signpost |
   |-------------|--------------|----------|
   | SKILL.md present | yes | yes |
   | PACK.yaml present | yes | yes |
   | LICENSE present | yes | **no** |
   | chapters/ dir + >=1 `ch*.md` | yes | **no** |
   | frontmatter name + description; name==slug | yes | yes |
   | resolve chapter links if any appear in body | yes | yes (vacuous if none) |
   | PACK.yaml REQUIRED_PACK_FIELDS + tier + slug | yes | yes (live packs already satisfy) |
   | RR-S-13 When-to-use / prereq | check_release only, content | still skipped by check_release filter |
   | Link-policy host ban | check_release/CI | still exempt via signpost_dirs |

   Do not add new signpost-only rules (out_scope). Do not drop tier/slug/name checks for signposts without an explicit package change (not requested).

3. **How `--all` reports signposts**
   - After relaxation, a well-formed signpost should contribute **PASS** (or an explicit non-fail status) and **must not increment `total_fail`**.
   - Options for the printer: (A) `PASS  <slug>` same as content; (B) `PASS  <slug> (signpost)` / `SKIP  <slug>` with skip counted as non-fail. Spec should pick one; exit-code goal is exit 0 on clean tree either way.
   - Summary line should reflect that signposts were included in the checked set without failing (e.g. 65/65, or 63 passed + 2 signpost OK). Avoid leaving them invisible if docs claim `--all` validates every pack dir.

4. **Relationship to `check_release` pre-filter**
   - Minimum P6 fix: teach `validate_pack` so standalone `--all` is green. Pre-filter may remain (defense in depth; also drives RR-S-13 and SKILLS count).
   - Optional cleanup (still in tooling, still small): stop excluding signposts from the validate loop once `check_pack` accepts them, so check 5 literally runs every pack dir through the same function. Spec should say whether pre-filter removal is required or optional; SKILLS/RR-S-13 filtering must stay if those checks remain content-only.
   - CONCERNS residual after P4 already notes signpost exemption duplication for **links**; pack-validate duplication is the P6 target.

5. **Documentation alignment**
   - Update `validate_pack.py` module docstring required-files bullet to state content packs need LICENSE+chapters; signposts (`kind: signpost` in SKILL.md) do not.
   - Touch CONTRIBUTING / PACK-SPEC only as needed so "every pack" / validation blurbs do not contradict signpost shape; README already describes signposts as citation-only.
   - Do not expand into PACK-SPEC redesign or new content rules.

6. **Failure UX for broken signposts**
   - A dir with `kind: signpost` but missing SKILL name/description or PACK.yaml fields should still FAIL with the existing error strings.
   - A content pack missing LICENSE must still FAIL (no accidental kind default).

7. **Non-goals**
   - No pytest harness this package (out_scope; separate CONCERNS test-debt item).
   - No CI workflow change.
   - No edits under `packs/omg-signpost` or `packs/se-standards-signpost` bodies/citations.
   - No PyYAML.

## Synthesis

SC1-SC5 covered. Root cause is one content-pack schema in `check_pack` plus an unfiltered `--all` iterator, while `check_release` secretly narrows the set. Minimum fix: detect `kind: signpost` in SKILL.md inside `check_pack`, skip only LICENSE and chapters/ requirements, keep other structural/tier checks, refresh docstring (and light doc mentions) so `--all` exits 0 on the same tree that prints `RELEASE CHECK: PASS`.

## Evidence index

| Loc | Kind |
|-----|------|
| tooling/validate_pack.py:4-20 | doc (usage + required files) |
| tooling/validate_pack.py:27-28 | code (REQUIRED_PACK_FIELDS / tiers) |
| tooling/validate_pack.py:52-111 | code (check_pack) |
| tooling/validate_pack.py:67-74 | code (LICENSE + chapters hard reqs) |
| tooling/validate_pack.py:114-138 | code (--all + exit discipline) |
| tooling/check_release.py:10-23 | doc (check list incl. validate_pack) |
| tooling/check_release.py:132-135 | code (signpost_dirs detection) |
| tooling/check_release.py:146 | code (link skip) |
| tooling/check_release.py:184-191 | code (pre-filter + check_pack loop) |
| tooling/check_release.py:195-210 | code (RR-S-13 skips via filtered packs) |
| tooling/check_release.py:225-232 | code (SKILLS count excludes signpost names) |
| packs/omg-signpost/SKILL.md | config (kind: signpost) |
| packs/omg-signpost/PACK.yaml | config (signpost meta) |
| packs/se-standards-signpost/SKILL.md | config (kind: signpost) |
| packs/se-standards-signpost/PACK.yaml | config (signpost meta) |
| packs/requirements-writing/* | config (content-pack contrast) |
| .planning/codebase/CONCERNS.md:7-13,55-61 | doc (standalone validator concern; stale counts) |
| docs/superpowers/packages/2026-09-14-jgs-se-knowledge-packs-packages.md P6 | doc (problem/scope) |
| CONTRIBUTING.md:38,54 | doc (validate command) |
| docs/PACK-SPEC.md:75,94-98 | doc (validate command + checks) |
| README.md:179-180 | doc (signpost product meaning) |
| Live runs: validate_pack --all exit 1; check_release exit 0 | runtime |
