# Spec: ci-link-policy-parity (2026-09-14)

## Problem

The repo enforces one link policy through two gates that each carry their own host banlist:

- CI (`.github/workflows/validate.yml:43-45`, inline `HOSTS` regex): 14 tokens, ends at `dau.edu`.
- Local release gate (`tooling/check_release.py:54`, `SOURCE_HOSTS`): the same 14 plus `cisa.gov`, `energy.gov`, `nde-ed.org`, `everyspec.com`.

Because CI is the weaker copy, a PR can introduce source-material URLs on the four missing hosts, pass GitHub Actions, and only fail a later human-run local check. Link policy is the licence-compliance mechanism: docs/LICENSING.md section 4 keeps published docs free of source-material links, and both gates exempt `kind: signpost` citation packs from the ban (.github/workflows/validate.yml:40-57, tooling/check_release.py:97-103). Silent drift between the two lists gets worse every time one side is extended without the other.

## Goals

- CI and local enforce the identical banned-host set (the current 18 tokens) by the end of this work.
- Future host additions start in one place (the data file), with the workflow's trusted copy updated in the same commit; a missed sync fails CI parity mechanically instead of drifting silently.
- The CI trust boundary holds: the workflow reads repo files as data and never executes checked-out `tooling/*.py`.
- Stdlib only. No new dependencies, no PyYAML, no third-party actions.

## Non-goals

- Leak-sentinel duplication (separate known duplicate, out of package scope).
- Scan-scope residual differences (CI suffix set and skip rules differ slightly from local `SKIP_DIRS`; accepted as-is).
- Release-gate CI expansion beyond host-list parity (separate package P5).
- Pack content edits, website YAML/version surfaces.
- Branch protection or CODEOWNERS configuration (ops-level complement, noted under residuals, not built here).

## Codebase context

Findings from the context gate (`docs/superpowers/context/2026-09-14-ci-link-policy-parity-context.md`), corroborated against the working tree:

- Exactly two executable banlists exist: the CI heredoc regex and `check_release.py` `SOURCE_HOSTS`. All other enumerations (`.planning/codebase/*`, CHANGELOG, package ledger) are documentary.
- Both regexes share the match shape `https?://[^\s)"']*(token|token|...)`: scheme required, token is a host substring. Bare domains without a scheme never match.
- Signpost exemption is behaviorally identical in both gates: `packs/*/SKILL.md` files whose frontmatter matches `^kind:\s*signpost\s*$` exclude their directory from the URL scan before any host matching. Live signposts: `packs/omg-signpost`, `packs/se-standards-signpost`.
- CI runs inline bash + python3 stdlib only, `permissions: read-all`, triggers on push to main and all PRs, fails with `::error` lines and nonzero exit. Local gate is trusted, may import `tooling/*.py`, fails via `fail(errs, "[links] ...")` entries and a final `RELEASE CHECK: FAIL`.
- No shared data file exists today (negative search, CORROBORATED).
- The workflow header and link-policy comments (`.github/workflows/validate.yml:6,40`) claim the list "mirrors" `check_release.py`; nothing verifies that hand-maintained claim.

## Research

research: skipped (in-repo regex/data parity only; no external APIs, libraries, platforms, or version-sensitive choices; CI trust boundary is documented in-repo)

## Design decisions

### D1: Enforcement architecture. Chosen: trusted inline CI copy plus parity assert against a shared data file (option C)

Three options were on the table:

- **A, shared data file only.** Both gates read one file. Rejected: the data file is PR-editable, so a PR can weaken the banlist and add a banned URL in the same diff. CI reading the checkout-supplied file as its only enforcement source lets the policy self-weaken with no signal beyond review diligence.
- **B, two inline copies plus a parity check.** Rejected as the primary mechanism: local would have to parse a Python literal out of the workflow YAML with regex to compare, which is fragile without PyYAML and re-creates the drift problem it tries to solve.
- **C, hybrid (chosen).** One shared data file is the single source for the local gate. CI keeps its own inline trusted copy (a frozenset literal inside the workflow heredoc) and *enforces with that copy*, then asserts set-equality against the data file and fails the build on any divergence.

Why C wins against the trust boundary: CI's enforcement input is no longer PR-controllable as data. Weakening the data file alone breaks parity and fails CI, naming the diff in both directions. Weakening CI requires editing the workflow file itself, a distinct and visible diff class that reviewers (and optional branch protection on workflow paths) treat differently from content edits. This is the strongest arrangement available without repo-settings changes, and it matches the locked preference that CI's enforcement copy stays out of the PR-editable data plane.

Residual accepted: a PR that edits both the workflow literal and the data file consistently weakens both gates. No in-repo mechanism prevents that; branch protection on `.github/workflows/` is the real control and stays out of scope, but the spec records it as the recommended ops complement.

### D2: Data file location and format. Chosen: `tooling/link-policy-hosts.txt`, one plain token per line

- Path: `tooling/link-policy-hosts.txt`, next to the gate that depends on it.
- Format: one host token per line, UTF-8, `#` comment lines and blank lines ignored, tokens stored plain (`nist.gov`, not `nist\.gov`; `eur-lex`; bare substring tokens like `sebokwiki`, `ntrs`, `dodcio` allowed exactly as today).
- Both consumers apply `re.escape()` per token and join with `|` inside the existing `https?://[^\s)"']*(...)` wrapper. `re.escape("nist.gov")` reproduces `nist\.gov`, so the effective regex is byte-identical in behavior to both current lists. Storing plain tokens keeps the file human-editable and keeps scheme-less tokens (which are not domains) expressible without format changes.
- Set comparison, not order comparison; the file is kept sorted so diffs stay readable.
- Token charset is `[A-Za-z0-9.-]+`. Both loaders strip surrounding whitespace, skip `#` comment lines and blank lines, and fail closed on anything else: locally `fail(errs, "[links-parity] malformed line in tooling/link-policy-hosts.txt: ...")`; in CI a parity `::error` naming the offending line and exit 1. A malformed line must never silently become a dead token that unbans a host.
- Self-scan safety: bare tokens contain no `https?://` prefix, so the `.txt` file and the workflow never flag themselves. Test fixtures use the repo's fragment-assembly idiom (see D5).

### D3: Failure idioms and check placement

- **CI** (inside the existing "Link policy check" heredoc step, parity asserted before the scan): on divergence, print one `::error::link-policy parity: tooling/link-policy-hosts.txt differs from workflow enforcement copy (only-in-file=[...] only-in-workflow=[...])` and `sys.exit(1)`. CI parses the data file with the same line rules as the local loader; a missing or unparseable file counts as divergence and exits 1 the same way. The scan itself keeps the current `::error file=<path>::source-material URL: ...` idiom, now built from the inline trusted set.
- **Local**: the host list joins check 3 (link policy, `[links]` tag). `SOURCE_HOSTS` is no longer a literal; it is compiled at runtime from `load_banned_hosts()` over the data file. Fail-closed handling: if the file is missing or unreadable, `fail(errs, "[links-parity] cannot read tooling/link-policy-hosts.txt: ...")`; if it parses to zero tokens, `fail(errs, "[links-parity] host list empty")`. Either way the report ends `RELEASE CHECK: FAIL`. `tooling/link-policy-hosts.txt` is also added to `REQUIRED_FILES` so check 1 names it with the existing `[files]` idiom.
- The local gate deliberately does **not** parse the workflow to cross-check it; that comparison lives in CI (authoritative) and in the kept test script (development-time, D5). Keeping it out of `check_release.py` avoids regex-parsing YAML in the release path for a failure mode CI already catches.

### D4: Signpost exception stays duplicated, by design

The signpost skip is logic over pack frontmatter (glob `packs/*/SKILL.md`, regex `^kind:\s*signpost\s*$`, exclude the pack directory before scanning), not host data. Moving it into the data file adds format machinery for no trust gain. Decision: it remains implemented in both gates and must stay behaviorally identical; any future change to the exemption touches both gates in one commit. This package changes nothing about how the exemption works. Acceptance includes the exemption still functioning (a banned URL inside `packs/omg-signpost` continues to pass both gates; the same URL anywhere else fails both).

### D5: Verification

Repo convention is release-gate verification; pytest is out of favor. Two artifacts:

1. **Kept assert-based script** `tooling/test_link_policy.py`, plain `python3` with `assert`, no framework. It covers: (a) the loader returns the expected token set from the data file; (b) the compiled regex matches a URL for every one of the 18 tokens, explicitly including the four previously CI-missing hosts; (c) benign URLs (for example `https://example.com/policy`) do not match; (d) a divergence-detection helper fed two differing sets reports the exact tokens on each side. Banned-URL fixtures are assembled from string fragments (`"https://www." + "cisa.gov" + "/x"`) so the test file does not trip check 3 against itself.
2. **Documented gate runs** recorded in the PR description: `python tooling/check_release.py` ends `RELEASE CHECK: PASS` on the clean tree; the CI run on the PR is green with the 18-token enforcement; a scratch divergence (one token removed from the data file on a throwaway commit, then restored) produces the parity `::error`, demonstrated once to prove detection works in both directions.

## Known residual risks

- A PR editing the workflow literal and the data file together weakens both gates. Mitigation is procedural (review of workflow diffs) plus optional branch protection on `.github/workflows/`; recorded here, built nowhere.
- Scan-scope residual (CI suffix set, local `SKIP_DIRS` differences) remains; a URL caught locally may not be scanned by CI or vice versa for scope reasons. Host-list parity does not address this and P5 owns gate expansion.

## Rollout

1. Add `tooling/link-policy-hosts.txt` with the 18 current tokens, sorted: cisa.gov, dau.edu, dla.mil, dod.mil, dodcio, energy.gov, eur-lex, europa.eu, everyspec.com, govinfo.gov, nasa.gov, nato.int, nde-ed.org, nist.gov, ntrs, ocw.mit, omg.org, sebokwiki.
2. Rework `tooling/check_release.py`: loader + runtime-compiled `SOURCE_HOSTS`, `[links-parity]` fail-closed paths, `REQUIRED_FILES` entry, docstring updated to say the list is data, not a literal.
3. Rework the CI link-policy step: inline `TRUSTED_HOSTS` frozenset, parity assert first, scan from the trusted copy, header comment updated to describe the data file and parity check instead of a hand-maintained "mirrors" claim.
4. Add `tooling/test_link_policy.py`.
5. Doc sync: `.planning/codebase/INTEGRATIONS.md` 14-host enum, `.planning/codebase/CONCERNS.md` duplication note marked resolved, CHANGELOG entry.
6. Run the D5 verification set.

## Approach

Option C: shared plain-text data file `tooling/link-policy-hosts.txt` is the single source for the local gate; CI enforces from a trusted inline frozenset and fails the build on set-divergence from the data file, naming the diff both ways. This keeps CI's enforcement copy out of the PR-editable data plane, closes the four-host gap immediately, and makes future host additions a one-file change plus a visible workflow diff. Signpost exemption stays as duplicated, behavior-identical logic in both gates. No human fork remains; the trust tradeoff is settled in favor of the PR-uneditable enforcement copy per the locked constraint.

## Open questions

none
