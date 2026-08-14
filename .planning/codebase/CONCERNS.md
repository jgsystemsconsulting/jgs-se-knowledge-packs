# Codebase Concerns

**Analysis Date:** 2026-08-14

## Tech Debt

**Signpost packs not understood by the standalone validator:**
- Issue: `tooling/validate_pack.py --all` fails on the two `kind: signpost` packs (`packs/omg-signpost`, `packs/se-standards-signpost`) because they intentionally lack `LICENSE` and `chapters/`. `tooling/check_release.py:88-89,118` excludes signpost dirs, but the standalone validator does not — running the documented command `python tooling/validate_pack.py --all` reports "46/48 pack(s) passed" and exit code 1 on a healthy repo.
- Files: `tooling/validate_pack.py:52-111`, `tooling/check_release.py:114-125`
- Impact: Contributors see false failures; CI-equivalent local check disagrees with the actual CI gate; exit code 1 breaks scripted workflows that use the documented command.
- Fix approach: Teach `validate_pack.py` the signpost exemption (detect `kind: signpost` in `SKILL.md` frontmatter and relax the LICENSE/chapters requirement), so both tools agree without `check_release.py` pre-filtering.

**CI gate logic duplicated in three places:**
- Issue: The link-policy host regex and leak sentinels exist in `tooling/check_release.py:44-47`, `.github/workflows/validate.yml` (inline python), and indirectly in pack docs. The duplication is deliberate (CI must not execute repo code), but nothing verifies the copies stay in sync.
- Files: `tooling/check_release.py:44-47`, `.github/workflows/validate.yml` (Link policy check step)
- Impact: A host added to one copy but not the others silently weakens the other gates (e.g., a new source domain banned locally but still publishable from CI, or vice versa).
- Fix approach: Extract the host list into a plain data file (e.g., `tooling/link-policy-hosts.txt`) that both the local gate and CI read as data (reading data is not "executing repo code"), or add a CI step that diffs the regexes against a canonical definition.

**No automated tests for ~1,000 lines of gate tooling:**
- Issue: `tooling/eval/tests/` exists but contains only `__pycache__/` — zero test files. The YAML-subset parser (`parse_simple_yaml`), frontmatter regexes, link scanner, and `gen_packs_page.py` row parser are all regex-heavy and regression-prone.
- Files: `tooling/validate_pack.py:31-49`, `tooling/gen_packs_page.py:28-39`, `tooling/check_release.py`, `tooling/eval/tests/` (empty)
- Impact: A regex tweak (e.g., for quoted YAML values or folded scalars) can silently stop catching violations — the gates are the repo's licence-compliance mechanism.
- Fix approach: Add pytest (or stdlib `unittest`) tests under `tooling/eval/tests/` covering: `parse_simple_yaml` quoting/comments/folded scalars, signpost detection, frontmatter edge cases, and the `gen_packs_page` table-row regex.

**Hardcoded machine-specific absolute paths in the build orchestrator:**
- Issue: `tooling/build_all_packs.workflow.js` defaults `PACKS` to `/c/Users/gower/OneDrive/Documents/GitHub/jgs-se-knowledge-packs` and `REF` to `/c/Users/gower/OneDrive/Documents/GitHub/jgs-reference-skill`.
- Files: `tooling/build_all_packs.workflow.js` (PACKS/REF constants near top)
- Impact: The orchestrator only works on one developer machine without explicit args; any other contributor or CI run fails.
- Fix approach: Derive the repo root from `scriptPath`, and require `refSkillDir` as an explicit arg or env var with a clear error if missing.

**Scaffolding relies on manual TODO completion with no drift gate:**
- Issue: `tooling/build_pack.py:58,60,75` writes `TODO` placeholders into `PACK.yaml` (built_on, notes) and `LICENSE`. Neither `validate_pack.py` nor `check_release.py` checks for lingering `TODO` text — a half-finished pack whose LICENSE still says "TODO: reproduce the source's full licence text" passes every mechanical gate as long as the required fields exist.
- Files: `tooling/build_pack.py:44-81`, `tooling/validate_pack.py:96-109`
- Impact: Licence-compliance risk — the whole point of the per-pack LICENSE is to reproduce source terms; a stub that shipped would publish unverified licence claims.
- Fix approach: Add a `TODO`-sentinel check to `validate_pack.py` for `PACK.yaml` and `LICENSE` (mirroring the leak-sentinel pattern in `check_release.py:42-44`).

## Known Bugs

**Standalone validator exits non-zero on a release-ready repo:**
- Symptoms: `python tooling/validate_pack.py --all` prints FAIL for `omg-signpost` and `se-standards-signpost` (missing LICENSE, missing chapters/) and returns exit 1, while `python tooling/check_release.py` prints "RELEASE CHECK: PASS".
- Files: `tooling/validate_pack.py:63-74`, `packs/omg-signpost/`, `packs/se-standards-signpost/`
- Trigger: Run `tooling/validate_pack.py --all` on a clean checkout.
- Workaround: Use `tooling/check_release.py` as the local gate, or pass pack dirs individually excluding signposts.

## Security Considerations

**CI gate execution trust model (currently sound, document the boundary):**
- Risk: If someone later "simplifies" `.github/workflows/validate.yml` to call `tooling/check_release.py` directly, a malicious PR could execute arbitrary repo code in CI.
- Files: `.github/workflows/validate.yml`, `tooling/check_release.py:18-19`
- Current mitigation: Workflow inlines its own stdlib-only checks and never executes checked-out code; `permissions: read-all`.
- Recommendations: Add a comment-level guard plus a CODEOWNERS entry on the workflow file so changes to it require review.

**Local-only sensitive/bulky material adjacent to the repo:**
- Risk: `sources/` (233 MB of downloaded government PDFs and `.build/full_text.txt` extracts), `.playwright-mcp/` QA snapshots, and interview-prep `.pptx` artifacts live in the working tree. All are correctly listed in `.gitignore` (verified via `git check-ignore`), but `.gitignore` does not protect against accidental `git add -f` or OneDrive sync exposure.
- Files: `.gitignore`, `sources/`, `.playwright-mcp/`, `System_Retirement_SE_Interview*.pptx`
- Current mitigation: `.gitignore` entries; `sources/` excluded from all scanners in `tooling/check_release.py:71-72`.
- Recommendations: Keep as-is; consider moving `sources/` outside the repo root if repo is ever shared as a zip/folder rather than via git.

## Performance Bottlenecks

**check_release.py re-reads every text file multiple times:**
- Problem: Leak scan and link scan each iterate all text files with separate `read_text` calls; on this repo (598 pack .md files) it is fine, but the pattern doubles I/O.
- Files: `tooling/check_release.py:77-96`
- Cause: Two separate loops over the same `text_files` list.
- Improvement path: Read each file once and run both sentinel and link checks per body. Low priority — current runtime is seconds.

## Fragile Areas

**Hand-rolled YAML subset parser:**
- Files: `tooling/validate_pack.py:31-49`
- Why fragile: Only handles flat `key: value` at column 0. Inline comments are not stripped (a value like `MIT # see note` keeps the trailing text), folded scalars (`>`/`|`) are skipped entirely, and multi-word unquoted values with `#` or trailing colons parse oddly. Any pack that uses standard YAML features will be mis-read.
- Safe modification: Extend `parse_simple_yaml` with tests first (see test gap above); do not switch to PyYAML without preserving the "stdlib only" CI constraint documented in the module docstring.
- Test coverage: None.

**Parallel indexes that must be manually kept in sync:**
- Files: `catalog.json`, `SKILLS.md`, `NOTICE`, `README.md`, `CHANGELOG.md`, `docs/packs.html`
- Why fragile: Five artifacts describe the same pack set. Gates exist for some pairs only: SKILLS.md count vs pack count (`check_release.py:156-162`), packs.html regeneration drift (`check_release.py:139-154`). There is no gate comparing `catalog.json` pack entries (46) to shipped pack dirs (48 incl. 2 signposts) — today the difference is intentional (signposts + one `planned` entry), but nothing enforces that intention.
- Safe modification: After adding/removing a pack, run the Register-phase updates for all five files, then `python tooling/gen_packs_page.py` and `python tooling/check_release.py`.
- Test coverage: Partial (see above); catalog-vs-packs drift is unguarded.

**Chapter link validation is one-directional:**
- Files: `tooling/validate_pack.py:92-94`
- Why fragile: Only checks that `SKILL.md` links of the exact form `(chapters/chNN-*.md)` resolve. Orphan chapter files (present in `chapters/` but never linked) are undetected, and links written in any other form (bare paths, anchor-suffixed, reference-style) bypass the check.
- Safe modification: If changing SKILL.md link style, keep the exact `(chapters/chNN-*.md)` pattern or update the regex in lockstep.
- Test coverage: None.

## Scaling Limits

**Pack count growth:**
- Current capacity: 48 packs / 598 chapter files / ~9 MB in `packs/`.
- Limit: `check_release.py` scans every text file with multiple whole-file regex passes; `SKILLS.md` is a single hand-maintained table; `catalog.json` is a single JSON blob. All remain fine at 2-3x scale.
- Scaling path: If packs exceed ~150, consider splitting SKILLS.md by publisher or generating catalog.json from `packs/*/PACK.yaml` (single-source) instead of maintaining it by hand.

## Dependencies at Risk

**External repo dependency for builds:**
- Risk: Pack synthesis depends on the MIT-licensed `jgs-reference-skill` repo (referenced in `tooling/build_pack.py:16-19` and hardcoded in `tooling/build_all_packs.workflow.js`). It is not vendored or pinned.
- Impact: Build pipeline breaks if that repo moves, is renamed, or changes its extraction interface.
- Migration plan: Pin a commit reference in docs and copy the extraction engine into `tooling/` (with licence) if stability becomes a problem.

**Zero third-party runtime dependencies (intentional):**
- Risk: None — stdlib-only Python is a design constraint, not debt. Preserve it: `tooling/validate_pack.py:18`, `.github/workflows/validate.yml` header, `install.py:41`.

## Missing Critical Features

**No per-pack content quality gate:**
- Problem: All gates are structural (files present, fields filled, links resolve, licence tier valid). Nothing checks chapter content depth, glossary/patterns/cheatsheet presence (mentioned as manual step in `build_pack.py:122`), or cross-pack redundancy (the caveat noted for `nasa-se-expanded` in `build_all_packs.workflow.js`).
- Blocks: Detecting thin or overlapping packs before release.

## Test Coverage Gaps

**All tooling code:**
- What's not tested: `tooling/validate_pack.py`, `tooling/check_release.py`, `tooling/build_pack.py`, `tooling/gen_packs_page.py`, `install.py` (multi-agent install/transform logic), `install.sh`, `install.ps1`.
- Files: `tooling/eval/tests/` (empty — only `__pycache__/`)
- Risk: The compliance gates and the installer (which writes into users' home dirs for 6 different agents) can regress unnoticed.
- Priority: High for `validate_pack.py`/`gen_packs_page.py` (they run in CI release decisions); Medium for `install.py` transform formats; Low for shell/PowerShell installers.

---

*Concerns audit: 2026-08-14*
