# Testing Patterns

**Analysis Date:** 2026-08-14

## Test Framework

**Runner:**
- No committed unit/integration test suite exists
- Historical evidence only: `tooling/eval/tests/__pycache__/` contains compiled artifacts of former pytest tests (`test_aggregation`, `test_bank_loading`, `test_baseline`, `test_coverage`, `test_report`, `test_scoring` — built with pytest 9.0.2 on Python 3.14) plus `eval.cpython-314.pyc`. The `.py` sources have been deleted; only `.pyc` bytecode remains. The test suite is NOT runnable as committed.

**"Testing" in this repo = validation gates**, not unit tests:

| Gate | Runner | Scope |
|------|--------|-------|
| CI content-integrity | `.github/workflows/validate.yml` (GitHub Actions, `content-integrity` job) | leak sentinels, link policy, frontmatter lint, `catalog.json` JSON validity |
| Pack validation | `python tooling/validate_pack.py packs/<slug>` (or `--all`) | required files, frontmatter name/description, kebab-case name == folder slug, chapter links resolve, `PACK.yaml` mandatory fields, `license_tier` in {1,2,3} |
| Release gate | `python tooling/check_release.py` | required governance files, leak sentinels, link policy, version single-source (`plugin.json` == CHANGELOG top == `RELEASE-INFO.txt`), all packs validate, `SKILLS.md` entry count, JGSC/SPDX headers on authored files |

**Run Commands:**
```bash
python tooling/validate_pack.py --all     # Validate every pack under packs/
python tooling/validate_pack.py packs/dau-se-guidebook   # Validate one pack
python tooling/check_release.py           # Full local release-readiness gate
```
CI runs automatically on push to `main` and every PR (`.github/workflows/validate.yml`).

## Test File Organization

**Location:**
- Former unit tests lived in `tooling/eval/tests/` (mirroring a `tooling/eval/eval.py` module that has also been deleted)
- No other test directories

**Naming (historical):**
- `test_*.py` standard pytest naming, e.g. `tooling/eval/tests/test_scoring.py`

## Validation Script Patterns

The de facto test pattern — reuse it for new checks:

```python
# 1. Collect errors, don't raise early (report ALL failures in one run)
errors: list[str] = check_pack(pack_dir)      # tooling/validate_pack.py

# 2. Emit GitHub Actions annotations when in CI context
print(f"::error file={f}::name not kebab-case: {name}")

# 3. Fail closed on exit code
sys.exit(1 if fails else 0)
```

**Key rules for gate code:**
- stdlib only, no third-party deps (CI must run on bare `python3`)
- CI workflow inlines its own copies of checks and never executes repo code; local `check_release.py` may run repo code — keep this trust boundary in mind when adding checks
- Scanner sentinels assembled from string fragments so scanners don't self-flag

## Fixtures and Factories

**Test Data:**
- Not applicable — no running test suite
- `tooling/build_pack.py --slug ... --tier ...` acts as the de facto factory for new pack fixtures (scaffolds a valid `PACK.yaml`/`LICENSE` stub with `TODO` markers)

## Coverage

**Requirements:** None enforced. There is no coverage tooling and no runnable test suite.

**Effective coverage proxy:** CI validates every pack's structure/licence and the whole repo's link policy and leak sentinels on every PR; `check_release.py` re-validates locally pre-release.

## Test Types

**Unit Tests:** Not present (former suite deleted; `.pyc` remnants only).

**Integration Tests:** Not present. Closest equivalents are the whole-repo gates (`tooling/check_release.py`, CI `content-integrity` job).

**E2E Tests:** Not used. `.playwright-mcp/` contains ad-hoc browser session artifacts (screenshots, console logs, page YAML) from manual verification of `docs/packs.html` — not automated tests.

## Gaps to Know About

- Restoring `tooling/eval/` (eval.py + pytest tests) from git history or rewriting it is a prerequisite for any eval/scoring work
- Pure-Python helpers (`parse_simple_yaml`, `deslop`, host regexes) are duplicated between `tooling/check_release.py` and inline CI python — changes must be made in both places
- Generated artifacts drift risk: `docs/packs.html`, `catalog.json`, `SKILLS.md` counts are only caught by `check_release.py`, not by CI

---

*Testing analysis: 2026-08-14*
