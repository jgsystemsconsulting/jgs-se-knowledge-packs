# Spec: validate-pack-signpost-parity (P6, size S)

Teach `tooling/validate_pack.py` about `kind: signpost` packs so the documented standalone command and `tooling/check_release.py` agree that a clean release-ready tree is valid.

## Problem

`validate_pack.check_pack` applies one requirement set to every pack directory: SKILL.md, PACK.yaml, LICENSE, and a `chapters/` dir with at least one chapter (tooling/validate_pack.py L57-74). `--all` iterates every directory under `packs/` with no filter (L117-118) and exits 1 when any pack fails (L127-138). The two signpost packs (`packs/omg-signpost`, `packs/se-standards-signpost`) intentionally carry only SKILL.md plus PACK.yaml with `kind: signpost` in frontmatter, so the documented `python tooling/validate_pack.py --all` exits 1 at 63/65 on a healthy tree. `check_release.py` detects signposts by regex on `packs/*/SKILL.md` (L132-135) and pre-filters them out of its pack-validation loop (L184-191), so it exits 0 on the same tree. Contributors are told to run the tool that fails.

Root cause: the standalone validator never learned the signpost shape; correctness lives only in check_release's pre-filter.

## Goals

1. `check_pack` recognizes signpost packs from SKILL.md frontmatter and relaxes only the LICENSE and chapters/ requirements for them.
2. `validate_pack.py --all` exits 0 at 65/65 on the same clean tree where `check_release.py` prints its PASS line.
3. Content-pack requirements are unchanged: LICENSE plus chapters/ stay mandatory for every non-signpost pack.
4. Detection logic duplicates check_release's exact regex so the two tools classify packs identically.
5. Negative coverage proves the carve-out is narrow (broken signposts still fail; broken content packs still fail).
6. Documented commands describe the new behavior.

## Non-goals

- Signpost pack body or citation edits.
- CI workflow edits (P4/P5 territory).
- pytest or any test framework; the probe follows the repo's existing assert-based `tooling/test_*.py` convention.
- New pack content rules or new signpost-only mandatory files.
- check_release.py changes. The pre-filter stays; nothing in it breaks once `check_pack` accepts signposts, and its RR-S-13 and SKILLS-count sections must keep excluding signposts because those checks are content-only by design.
- PyYAML or any third-party dependency.

## Research

research: skipped (in-repo tooling alignment only; no external APIs, libraries, platforms, or version-sensitive choices)

## Codebase context

- `validate_pack.check_pack` (tooling/validate_pack.py L52-111): unconditional required-file checks at L57-74; frontmatter name/description and slug match at L77-90; chapter-link resolution at L91-94; PACK.yaml required fields, tier in {1,2,3}, slug match at L96-109.
- `main` / `--all` (L114-138): empty argv behaves like `--all`; per-pack PASS/FAIL lines; summary `passed/total`; exit 1 on any FAIL.
- `check_release.py` signpost detection (L134-135): `signpost_dirs = {p.parent for p in ROOT.glob("packs/*/SKILL.md") if re.search(r"^kind:\s*signpost\s*$", p.read_text(...), re.M)}`. The same set drives the link-policy exemption (L146) and the pack-validate pre-filter (L184-191).
- Live signpost packs: `packs/omg-signpost`, `packs/se-standards-signpost`, each SKILL.md plus PACK.yaml only. Frontmatter carries `name`, `kind: signpost`, `description`. PACK.yaml already satisfies every `REQUIRED_PACK_FIELDS` entry plus valid tier and matching slug.
- Content pack contrast: `packs/requirements-writing` has LICENSE, chapters/, and optional furniture. 65 dirs under `packs/` at gate time (63 content, 2 signpost).
- Docs naming the validator: module docstring (L7-19, claims LICENSE plus chapters always required), CONTRIBUTING.md L38 (per-slug command) and L54 ("CI runs validate_pack.py on every pack"), docs/PACK-SPEC.md L75 and L94-98 (per-slug command plus checks list). README and SOURCE-VETTING describe signpost product meaning and tier enforcement without contradicting the fix.
- Repo probe convention: `tooling/test_link_policy.py` is an assert-based, no-framework script with a `Run:` docstring line that exits nonzero on the first failed assert.

## Design decisions

### D1: Detect kind inside check_pack, keyed on SKILL.md text

Signpost detection lives inside `check_pack`, not in a `--all` pre-filter, so the single-pack path and `--all` get one definition of "is signpost" and `check_release`'s delegation to `check_pack` keeps working unchanged.

Predicate: read SKILL.md text and apply the identical expression check_release uses, `re.search(r"^kind:\s*signpost\s*$", text, re.M)`, over the whole file rather than only the extracted frontmatter block. Same regex, same target file, same case sensitivity, so the two tools classify a pack the same way by construction. A pack with no `kind:` line, or with any case or spacing variant the regex rejects, is a content pack and keeps every existing requirement. Accepted shared edge case: a content pack whose SKILL.md body quotes `kind: signpost` alone on a line would be misclassified by BOTH tools identically; parity-by-construction outranks closing that loophole here, and no live pack quotes it. PACK.yaml's `kind: signpost` field is corroboration only, never a second detector; SKILL.md is the source of truth because that is what check_release reads.

Placement in the function: read the SKILL.md text once before the required-file block (guarded by `skill.is_file()`), compute a boolean, then guard exactly two checks on it: the missing-LICENSE error and the missing-chapters/ error including its empty-chapters branch. The frontmatter section already reads the same text, so the early read replaces the later one instead of adding a second read.

What a signpost must still satisfy (all existing checks, unchanged):

| Check | Content pack | Signpost |
|---|---|---|
| SKILL.md present | yes | yes |
| PACK.yaml present | yes | yes |
| LICENSE present | yes | no |
| chapters/ dir with >=1 `ch*.md` | yes | no |
| frontmatter `name` + `description`; `name` == folder slug | yes | yes |
| chapter links in body resolve | yes | yes (vacuous when none) |
| PACK.yaml required fields, tier in {1,2,3}, slug match | yes | yes |

Missing SKILL.md remains a hard fail even for a would-be signpost: without the file the kind cannot be proven, and the pack fails as today. Presence of LICENSE or chapters/ in a signpost is not an error; the change relaxes requirements, it adds none.

### D2: --all reports signposts as ordinary PASS; exit 0 at 65/65

A well-formed signpost prints `PASS  <slug>` exactly like a content pack and counts toward the summary as passed. No new status vocabulary, no `(signpost)` annotation, no skip counter, no second tally. Rationale: the minimal diff is the one that adds no printer branches, and docs that say `--all` validates every pack stay literally true. Clean-tree output is 65/65 with exit 0, agreeing with check_release's exit 0 on the same tree. A broken signpost prints FAIL with the existing error strings and, as today, forces exit 1.

### D3: Negative coverage in tooling/test_validate_pack.py

One new assert-based probe, `tooling/test_validate_pack.py`, matching the `test_link_policy.py` convention: stdlib only, `Run:` line in the docstring, asserts raise and exit nonzero. Fixtures are built in `tempfile.TemporaryDirectory` dirs so the live tree is never mutated. Cases:

1. Full content-pack shape (SKILL.md, PACK.yaml, LICENSE, one chapter) passes.
2. Same shape minus LICENSE fails with the missing-LICENSE error.
3. Same shape minus chapters/ fails with the missing-chapters error.
4. Signpost shape (SKILL.md with `kind: signpost`, PACK.yaml, no LICENSE, no chapters/) passes.
5. Signpost missing SKILL.md fails (cannot prove kind; missing-SKILL.md error).
6. Signpost missing PACK.yaml, or with frontmatter missing `description`, still fails.
7. Both live signpost dirs return an empty error list from `check_pack` (guards against regressions on the real tree).

This satisfies the repo rule that non-trivial logic leaves one runnable check behind, without introducing pytest.

### D4: Documentation alignment, three surfaces

1. `tooling/validate_pack.py` module docstring: reword the required-files bullet so LICENSE and chapters/ are stated as content-pack requirements and signpost packs (`kind: signpost` in SKILL.md) need only SKILL.md and PACK.yaml. Keep it to the existing bullet style.
2. `docs/PACK-SPEC.md` (around L94-98): one sentence next to the per-slug command noting that signpost packs skip the LICENSE and chapters/ checks.
3. `CONTRIBUTING.md` L54: no change needed; "CI runs validate_pack.py on every pack" becomes accurate where it was misleading. L38 per-slug command already works for both pack kinds after the fix.

README and SOURCE-VETTING already describe signposts as citation-only and stay untouched.

## Implementation sketch

Minimal diff, `validate_pack.py` only plus the new probe and doc lines:

```python
# in check_pack, after slug = pack_dir.name
body = skill.read_text(encoding="utf-8", errors="ignore") if skill.is_file() else ""
is_signpost = bool(re.search(r"^kind:\s*signpost\s*$", body, re.M))

# required files: wrap lic and chapters checks
if not is_signpost:
    if not lic.is_file():
        errors.append("missing LICENSE (must reproduce the source's terms)")
    if not chapters.is_dir():
        errors.append("missing chapters/ directory")
    else:
        ...  # empty-chapters check unchanged
```

The later frontmatter block drops its second read and reuses `body` instead. Estimated size: roughly 10 changed lines in validate_pack.py, one new probe file near 80 lines, one docstring bullet, one PACK-SPEC sentence.

## Verification

1. `python tooling/validate_pack.py --all` exits 0 with passed == total (65/65 on the current tree).
2. `python tooling/validate_pack.py` (empty argv) behaves identically.
3. `python tooling/validate_pack.py packs/omg-signpost packs/se-standards-signpost` exits 0 with passed == total.
4. `python tooling/check_release.py` still exits 0 with no output change.
5. `python tooling/test_validate_pack.py` exits 0; deliberately breaking a fixture (commenting the `kind:` line in case 4's fixture) makes it fail, confirming the probe bites.
6. Em-dash and placeholder pass over touched docs.

## Approach

Teach `check_pack` the signpost shape using check_release's exact regex on SKILL.md, guard only the LICENSE and chapters/ requirements on it, keep every other check for every pack, report signposts as ordinary PASS so `--all` exits 0 at 65/65, prove the carve-out narrow with an assert-based `tooling/test_validate_pack.py`, and align the validator docstring plus one PACK-SPEC sentence. check_release stays untouched.

## Open questions

None. All four dispatched decisions are settled: detection inside `check_pack` on SKILL.md text, plain PASS reporting with exit 0 at 65/65, assert-based probe coverage for the four negative cases (D3 cases 2, 3, 5, 6), and docstring plus PACK-SPEC as the only doc surfaces needing edits.
