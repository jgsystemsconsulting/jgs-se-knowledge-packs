# CI local-gate coverage gap (P5, 2026-09-14)

PR CI runs four shallow checks; the local gate (`tooling/check_release.py`) runs eleven plus three extras. Phases 19-20 map/overlap/classification/replay work is invisible to CI, so a PR can be green while the repo is not release-ready. This package closes the highest-value CI-blind gaps with inline stdlib checks that read repo files as data, documents what must stay local-only, and adds an honest pre-tag fail-closed control. It does not touch the P4 host-list parity work.

## Research

research: skipped (in-repo CI/gate alignment only; no external APIs, libraries, platforms, or version-sensitive choices; GitHub Actions inline python3 stdlib is already the established pattern in this repo)

## Codebase context

- Local gate: `tooling/check_release.py`, eleven documented checks plus extras 5b (RR-S-13), 5c (RR-B-30 packs.html), 6b (cursor manifest). Checks 5, 5c, 8, 9, 10, 11 import repo modules and can never run in CI under the trust posture; 5b scans SKILL.md text with stdlib only (CI-closable in principle, not added by this package).
- CI: `.github/workflows/validate.yml`, four steps (leak sentinels, link policy, frontmatter lint, catalog JSON), `permissions: read-all`, ubuntu-latest, `actions/checkout@v4` only. The P4 parity assert lives inside the link step: CI enforces from an inline `TRUSTED_HOSTS` frozenset and fails if `tooling/link-policy-hosts.txt` drifts either way. Do not weaken it.
- Trust boundary: the workflow never executes checked-out repository code. Inline bash plus python3 stdlib heredocs only; no PyYAML, no third-party actions. A PR that could make CI run checkout code would run arbitrary attacker code under Actions.
- P4 precedent for drift: trusted inline copy for enforcement, data file as the shared source, parity assert between them, and an assert-based local probe (`tooling/test_link_policy.py`).
- Pre-tag today: nothing mechanical requires `check_release.py` before a tag. No hook, no tag-triggered workflow, no release gate. Documentation only.

## Goals

1. CI covers the version agreement (including both website YAMLs), the SKILLS.md vs pack count, the overlap basename invariant, and the pure-data subset of the map/classification checks.
2. Every new CI copy carries a named drift control against its `check_release` twin, on the P4 pattern.
3. The local-only remainder is documented where operators will see it.
4. Pre-tag failure mode for skipped local checks: a concrete control, honestly labeled.
5. Trust posture unchanged: `read-all`, no checkout-code execution, stdlib only.

## Non-goals

- Host-list parity (P4, landed in 1e47bb0..a42e3d9).
- Running `tooling/check_release.py` in CI, in any form.
- Full `validate_pack`, packs.html regeneration equality, generator replay in CI.
- Content-quality evals; Phase 21 CONTRACT prose; restoring the deleted `tooling/eval` pytest suite.
- Third-party actions or PyYAML.
- Closing the residual leak/link scan-scope differences (suffix sets, SKIP_DIRS) between CI and local.

## Design

### New CI steps in .github/workflows/validate.yml

Four steps appended after "Catalog JSON valid". Each is a python3 stdlib heredoc that reads repo files as data. Each failure prints `::error::` lines prefixed with the local check tag so CI logs grep like local gate output.

#### Step 5: Version single-source (twins check 4 + 4a)

Enforced: `.claude-plugin/plugin.json` `version`, first `## [N.N.N]` in `CHANGELOG.md`, `Version:` in `RELEASE-INFO.txt`, and the `version: "N.N.N"` line in `docs/products/website/01-jgs-se-knowledge-packs.yaml` and `docs/products/website/catalog.yaml` all agree; any missing or empty value fails.

Mechanism: inline python3, same extraction as the local gate, byte-identical regex literals:

- CHANGELOG: `^##\s*\[(\d+\.\d+\.\d+)\]` (multiline; first match wins, so `## [Unreleased]` above it is harmless)
- RELEASE-INFO: `Version:\s*([0-9]+\.[0-9]+\.[0-9]+)`
- website YAMLs: `version:\s*"([0-9]+\.[0-9]+\.[0-9]+)"`, compared against the RELEASE-INFO value

Failures: `[version] disagreement / missing: {...}` and `[version] <path>: website YAML version 'X' != RELEASE-INFO 'Y'`, exit 1.

Remains local-only: nothing for this check; the CI port is complete.

#### Step 6: SKILLS index count (twins check 6)

Enforced: the number of `` [`slug`](packs/...) `` links in `SKILLS.md` (excluding signpost slugs) equals the number of non-signpost directories under `packs/`.

Mechanism: signpost detection identical to the existing link step (`^kind:\s*signpost\s*$` on `packs/*/SKILL.md`), `re.findall(r"\[`([^`]+)`\]\(packs/", text)`, filter signpost names, compare to non-signpost pack dir count. Fails `[index] SKILLS.md lists N packs but M are shipped`.

Remains local-only: nothing; this is the full check.

#### Step 7: Chapter basename overlap (twins check 8)

Enforced: no chapter basename appears under two packs unless whitelisted. Scan scope `packs/*/chapters/*.md` only; pack-root support files are excluded by path.

Mechanism: build a basename to slugs multiset, fail on any entry with more than one slug that is not in the whitelist. Whitelist source: `tooling/overlap-whitelist.txt` (new data file, see below), read fail-closed: missing or malformed file fails the step with `[overlap] whitelist data file ...`. Failures carry the `[overlap]` tag and list `basename: pack1, pack2`.

Remains local-only: nothing; `check_overlap.py` logic is pure, so the CI copy is complete.

#### Step 8: Map and classification data invariants (subset of checks 9 and 10)

One heredoc, two files, tagged `[map-data]` and `[rules-data]`. Asserts only facts the local checkers also guarantee, so CI red always means real drift:

- Envelope: `docs/capability-pack-map.json` exists, is an object, `schema_version == 2`, non-empty `map_version`, `generated_on` matches `YYYY-MM-DD`. Same for `docs/classification-rules.json` with `schema_version == 1`. Regex literals must mirror the local `MAP_VERSION_RE` / `GENERATED_ON_RE` pins, and the probe asserts literal parity for them.
- Cross-file: `map_version` equal and `generated_on` equal between the two files (rules-vs-map `generated_on` fidelity is already enforced locally since a9bfae4).
- Map vs disk set equality: the set of `(pack, chapter)` pairs across `clusters[].chapters[]` — after dropping rows whose chapter ends with ` (support file)`, mirroring `check_capability_map.py`'s `SUPPORT_SUFFIX` exclusion — equals the set of all files under `packs/*/chapters/` (all files, matching the local twin's `is_file` scan). The disk side must be derived exactly as the local twin derives it (packs by `chapters/` directory existence; `check_capability_map.py` never reads `signpost_packs`), so the two gates cannot disagree on the pack set. `rules.signpost_packs` exact-value fidelity stays a local-only guarantee.
- Rules coverage: every assignment row `(pack, chapter)` with `is_support: false` points at an existing `packs/<pack>/chapters/<chapter>`; every on-disk chapter of a non-signpost pack has an `is_support: false` assignment row; no assignment row names a pack in `signpost_packs` (read as a set for exclusion only; its exact-value fidelity stays local-only). Support-file rows (`is_support: true`) are skipped; support policy stays local.

Remains local-only: cluster minimum thresholds, note and override consistency, rules-of-construction edge semantics, and the generator replay. The CI subset is deliberately weaker than the local checkers and must stay a strict subset of their guarantees.

### Drift control (per check)

| CI copy | Twin | Control |
|---|---|---|
| Version regexes | check_release check 4/4a | Literal-parity asserts in the probe (below) plus header comment naming the twin |
| SKILLS link and signpost regexes | check_release check 6 | Literal-parity asserts; signpost regex is already duplicated by P4, precedent accepted |
| Overlap whitelist | `check_overlap.py` | Single shared data file read by both sides, fail-closed both ways; parity by construction |
| Map/rules envelope pins | checks 9/10 | CI pins only what local checkers enforce (`schema_version` 2 and 1); a local bump turns CI red and forces the sync |
| Workflow text itself | n/a | Probe extracts and runs the real heredocs (below), so workflow breakage fails locally too |

Rule carried forward: any policy-bearing constant copied into the workflow gets the P4 pin-plus-parity treatment or moves to a shared data file. Logic too complex to duplicate honestly stays local-only.

### Overlap whitelist extraction

New file `tooling/overlap-whitelist.txt`, same shape as `tooling/link-policy-hosts.txt`: one token per line, `#` comments, blank lines allowed. Initial content: `ch01-introduction.md` with its rationale comment (three source packs legitimately share the canonical intro chapter name).

`tooling/check_overlap.py` stops defining `WHITELIST` as a constant and loads the data file fail-closed: unreadable or malformed file prints `OVERLAP: FAIL` with the reason and exits 1, mirroring how `check_release.py` handles `link-policy-hosts.txt`. `check_release.py` needs no change for this; it calls `check_overlap.main()`.

Honest residual, stated in the workflow comment and here: the whitelist file is PR-editable, so a PR can relax the gate in both places at once. That is exactly today's posture with the constant inside `check_overlap.py`, also PR-editable. Review is the control; the data file only removes accidental divergence, which is the drift direction the context gate flagged as the structural risk.

### Local-only remainder documentation

- Workflow header comment gains a coverage map: which local check ids each step twins, followed by the explicit list of what CI does not cover and why: full `validate_pack` (non-trivial parser, fork invites permanent drift), RR-B-30 packs.html regeneration equality (needs the generator), full map threshold and note logic, full classification semantics beyond set coverage, and `generate_capability_map --check` replay (definitionally generator execution).
- `tooling/check_release.py` module docstring gains the same split in two lines: "CI-covered: version, index, overlap, map/rules data invariants. Local-only required before tag: pack validation, packs.html freshness, full map/rules checks, replay." This is where an operator already looks.
- `.planning/codebase/TESTING.md` CI-gap note refreshed at implementation time (its line references are stale anyway); CHANGELOG entry.

### Pre-tag fail-closed

No mechanical control is trustworthy here. CI cannot execute repo code, so it cannot verify a local run happened; any stamp or attestation in the repo is self-issued and forgeable, and a release workflow with attestations is design-heavy machinery for a solo-maintained repo. So the control is procedural, made as strong as the posture allows:

1. `check_release.py` PASS banner becomes `RELEASE CHECK: PASS (v<version> @ <short-sha>)`, version from the already-parsed RELEASE-INFO value, short sha from `git rev-parse --short HEAD`; if git is unavailable the banner prints `RELEASE CHECK: PASS (v<version> @ no-git)` — distinct, and by the rule in item 2 such a receipt can never satisfy the pre-tag sha match. Three lines, and it makes a pasted transcript verifiable against a commit.
2. The docstring and TESTING.md state the pre-tag rule: before tagging, run `python tooling/check_release.py` at the exact commit being tagged and require the PASS line whose sha matches that commit.
3. Enforcement point is the release procedure: P8 (`gsd-ship`) already owns the human-driven release path and will require the pasted PASS transcript. Wiring that step into the ship skill is P8 work, not this package.

Recorded plainly: this does not make it impossible to tag without running the gate. It makes the skipped-gate state visible in the one artifact the release process already requires.

### Failure UX and posture

- New steps keep local tags: `[version]`, `[index]`, `[overlap]`, `[map-data]`, `[rules-data]`.
- All failures via `::error::` / `::error file=...::` annotations, exit 1.
- Header contract extended, not replaced: self-contained inline bash + python3 stdlib; never executes checked-out repository code; no new `uses:`; `permissions: read-all` unchanged; no `pull_request_target`.

## Verification

New probe `tooling/test_ci_gate.py`, assert-based, no test framework, following `tooling/test_link_policy.py`:

1. Extracts each new heredoc from `.github/workflows/validate.yml` by its step marker and executes it with `cwd` set to a fixture tree, so the shipped workflow text is what gets tested, not a mirror of it. The four extraction markers are the pinned step names: `Version single-source`, `SKILLS index count`, `Chapter basename overlap`, `Map and classification data invariants`; the probe fails loudly if extraction matches zero heredocs. If extraction proves brittle at implementation time, fall back to the P4 mirror-functions pattern and say so in the probe header.
2. Negative demo per new step (each must exit 1 with the right tag):
   - version: plugin.json at 1.2.3 against RELEASE-INFO at 1.2.4; missing website YAML version line.
   - index: two packs, one SKILLS link; signpost pack wrongly counted.
   - overlap: two packs sharing an unwhitelisted basename; whitelist data file missing.
   - map/rules: map missing one on-disk chapter; assignment row pointing at a nonexistent file; wrong `schema_version`; `generated_on` mismatch between the two files.
3. Positive runs: every extracted heredoc against the real repo tree expecting exit 0, which is what CI will see on a clean tree.
4. Literal-parity asserts: the three version regexes, the SKILLS link regex, and the signpost regex each appear verbatim in both `check_release.py` and `validate.yml`; `MAP_VERSION_RE` and `GENERATED_ON_RE` appear verbatim in both `validate.yml` and their local twins (`tooling/check_capability_map.py`, `tooling/check_classification_rules.py`). A failure message says "regex drifted between check_release.py and validate.yml; sync them".

Repo-level checks: `python tooling/check_release.py` still PASS after the whitelist extraction; `python tooling/check_overlap.py` PASS; `python tooling/test_ci_gate.py` exits 0; the PR's own CI run is green with the four new steps executing.

## Files touched

- `.github/workflows/validate.yml`: four new steps, header coverage map.
- `tooling/overlap-whitelist.txt`: new shared data file.
- `tooling/check_overlap.py`: load whitelist from the data file, fail-closed.
- `tooling/check_release.py`: docstring coverage split, PASS banner with version and sha.
- `tooling/test_ci_gate.py`: new probe.
- `.planning/codebase/TESTING.md`, CHANGELOG.md: doc updates at implementation.

## Approach

Extend `validate.yml` with four inline-stdlib steps that read repo files as data and twin local checks 4+4a, 6, 8, and the pure-data subset of 9/10; move the overlap whitelist into a shared data file both sides read fail-closed; control drift with heredoc-extracting probe plus regex literal-parity asserts; document the local-only remainder in the workflow header and the gate docstring; and answer pre-tag fail-closed with a sha-stamped PASS receipt plus a documented release rule, since no mechanical control is trustworthy under the no-checkout-execution posture.

## Open questions

None. The pre-tag control is the documented procedural option the dispatch sanctioned: nothing mechanical can verify a local run without executing repo code, so the spec records the control honestly instead of blocking on a human ruling.
