# CI Link Policy Parity Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make CI and the local release gate enforce the identical 18-token banned-host set, with the host list as a data file for the local gate, a trusted inline CI copy, and a mechanical parity assert that fails CI on divergence in either direction.

**Architecture:** Option C from the spec. New data file `tooling/link-policy-hosts.txt` is the single source for `tooling/check_release.py`, which compiles its ban regex at runtime through a `load_banned_hosts()` helper and fails closed on missing, empty, or malformed data. The CI link-policy step keeps a trusted inline `TRUSTED_HOSTS` frozenset, asserts set-parity against the data file before scanning, and scans from the trusted copy. Signpost exemption stays duplicated and byte-identical in both gates. A kept assert-based script `tooling/test_link_policy.py` locks the loader, the regex, and the divergence helper.

**Tech Stack:** Python 3 stdlib only (`re`, `pathlib`, `sys`). GitHub Actions inline `python3` heredoc. No PyYAML, no new dependencies, no third-party actions.

**Spec:** `docs/superpowers/specs/2026-09-14-ci-link-policy-parity.md`

## Research

research: skipped (in-repo regex/data parity only; no external APIs, libraries, platforms, or version-sensitive choices; CI trust boundary is documented in-repo)

## Global Constraints

- Exactly 18 banned-host tokens, stored plain and sorted: `cisa.gov`, `dau.edu`, `dla.mil`, `dod.mil`, `dodcio`, `energy.gov`, `eur-lex`, `europa.eu`, `everyspec.com`, `govinfo.gov`, `nasa.gov`, `nato.int`, `nde-ed.org`, `nist.gov`, `ntrs`, `ocw.mit`, `omg.org`, `sebokwiki`.
- Token charset `[A-Za-z0-9.-]+`. `#` comment lines and blank lines are ignored by both loaders. Any other line fails closed; a malformed line must never silently become a dead token.
- Both consumers apply `re.escape()` per token and join with `|` inside the existing wrapper `https?://[^\s)"']*(...)`. Scheme-less bare domains never match.
- Stdlib only. No PyYAML, no new dependencies, no third-party actions.
- CI trust boundary: the workflow reads repo files as data and never imports or executes checked-out `tooling/*.py`.
- Signpost exemption is unchanged in both gates: glob `packs/*/SKILL.md`, frontmatter regex `^kind:\s*signpost\s*$`, exclude the pack directory before any host matching.
- Local failure idioms: scan hits keep the `[links]` tag; data-file problems use a new `[links-parity]` tag; a missing required file keeps the `[files]` tag. Report ends `RELEASE CHECK: FAIL` or `RELEASE CHECK: PASS`.
- CI failure idioms: `::error` lines and exit 1. Parity error line format is exactly: `::error::link-policy parity: tooling/link-policy-hosts.txt differs from workflow enforcement copy (only-in-file=[...] only-in-workflow=[...])`.
- Local fail-closed messages begin with the `[links-parity]` tag followed by these gists: `cannot read tooling/link-policy-hosts.txt: ...`, `host list empty` (the loader appends a parenthesized detail), `malformed line in tooling/link-policy-hosts.txt: ...`.
- Local runner is `python` (Windows); CI runner is `python3` (ubuntu-latest).
- Repo conventions after this work: `python tooling/check_release.py` ends `RELEASE CHECK: PASS`; `python tooling/test_link_policy.py` exits 0.
- Minimal-diff style: touch only the files named in the tasks. Other documentary mentions of the host list (`.planning/codebase/CONVENTIONS.md`, ARCHITECTURE, TESTING, STRUCTURE) are out of scope per the spec's doc-sync list.

## Codebase context

Context gate output (reused, not re-explored): `docs/superpowers/context/2026-09-14-ci-link-policy-parity-context.md` and `docs/superpowers/context/2026-09-14-ci-link-policy-parity-context-log.md`.

Current state, verified against the working tree on 2026-09-14 (versions 1.20.0 across plugin.json, RELEASE-INFO.txt, CHANGELOG top; clean-tree run of `python tooling/check_release.py` ends `RELEASE CHECK: PASS`, exit 0):

- CI banlist, `.github/workflows/validate.yml:43-45`, inside the "Link policy check" heredoc step (step spans lines 37-64):

```python
HOSTS = re.compile(r"https?://[^\s)\"']*(sebokwiki|nasa\.gov|ntrs|nist\.gov|"
                   r"govinfo\.gov|omg\.org|ocw\.mit|dodcio|dod\.mil|dla\.mil|"
                   r"eur-lex|europa\.eu|nato\.int|dau\.edu)")
```

- Local banlist, `tooling/check_release.py:54`:

```python
SOURCE_HOSTS = re.compile(r"https?://[^\s)\"']*(sebokwiki|nasa\.gov|ntrs|nist\.gov|govinfo\.gov|omg\.org|ocw\.mit|dodcio|dod\.mil|dla\.mil|eur-lex|europa\.eu|nato\.int|dau\.edu|cisa\.gov|energy\.gov|nde-ed\.org|everyspec\.com)")
```

- CI is the weaker copy: it misses `cisa.gov`, `energy.gov`, `nde-ed.org`, `everyspec.com`.
- The workflow header comment (lines 6-8) claims it "Mirrors tooling/check_release.py"; nothing verifies that claim.
- Local link check is `tooling/check_release.py:95-107` (signpost exclusion at 99-103, scan at 101-107). `REQUIRED_FILES` is `tooling/check_release.py:39-47`. The module docstring check list is at lines 10-23 (check 3 on line 12).
- Signpost exemption is behaviorally identical in both gates. Live signposts: `packs/omg-signpost`, `packs/se-standards-signpost`. `packs/omg-signpost/SKILL.md` contains `https://www.omg.org/spec/...` URLs today, so a clean `RELEASE CHECK: PASS` doubles as proof the exemption still works (if the exemption broke, those URLs would flag).
- CI scan suffix set is `{".md", ".json", ".yaml", ".yml", ".txt"}`; the local gate scans more suffixes and skips more dirs. That scan-scope residual is accepted by the spec and is not touched here.
- Both gates scan `.txt` and `.yml` files, so the new data file, the workflow, and the test script must never contain a banned URL with a scheme in one contiguous source string. Bare tokens like `nist.gov` and fragment-assembled fixtures like `"https://www." + "cisa.gov" + "/x"` are safe. The regex wrapper literal `https?://[^\s)\"']*( ` is also self-safe: the `)` stops the character-class run before any token can follow.

### File structure

| File | Action | Responsibility |
|------|--------|----------------|
| `tooling/link-policy-hosts.txt` | Create | Single source of the 18 banned-host tokens (local gate input; CI parity target) |
| `tooling/check_release.py` | Modify | `load_banned_hosts()` loader, runtime-compiled ban regex, `[links-parity]` fail-closed paths, `REQUIRED_FILES` entry, docstring update |
| `tooling/test_link_policy.py` | Create | Kept assert-based test script (no pytest): loader set, per-token matches, benign non-matches, divergence helper |
| `.github/workflows/validate.yml` | Modify | Trusted inline `TRUSTED_HOSTS`, parity assert before the scan, scan from the trusted copy, header comment update |
| `.planning/codebase/INTEGRATIONS.md` | Modify | Replace the 14-host enum with the data-file plus parity description |
| `.planning/codebase/CONCERNS.md` | Modify | Mark the duplication concern resolved |
| `CHANGELOG.md` | Modify | `[Unreleased]` entry |

---

### Task 1: Create the banned-host data file

**Files:**
- Create: `tooling/link-policy-hosts.txt`

**Interfaces:**
- Consumes: nothing.
- Produces: `tooling/link-policy-hosts.txt`, 18 sorted tokens, one per line, charset `[A-Za-z0-9.-]+`, `#` comments and blank lines allowed. Later tasks parse exactly this format.

**Model:** flash

- [ ] **Step 1: Create the file with exactly this content** (trailing newline at end)

```
# Banned source-material hosts (link policy, docs/LICENSING.md section 4).
# One plain token per line; both gates match it as a URL substring after the scheme.
# Source of truth: tooling/check_release.py loads this file at runtime.
# CI (.github/workflows/validate.yml) enforces from a trusted inline copy and
# fails on any set-divergence from this file. Keep sorted. '#' comments and
# blank lines are ignored; every other line must match [A-Za-z0-9.-]+.
cisa.gov
dau.edu
dla.mil
dod.mil
dodcio
energy.gov
eur-lex
europa.eu
everyspec.com
govinfo.gov
nasa.gov
nato.int
nde-ed.org
nist.gov
ntrs
ocw.mit
omg.org
sebokwiki
```

- [ ] **Step 2: Verify count, sort order, and charset**

Run:

```bash
grep -vE '^(#|$)' tooling/link-policy-hosts.txt | sort -c && echo "sorted OK"
grep -cvE '^(#|$)' tooling/link-policy-hosts.txt
grep -vE '^(#|$)' tooling/link-policy-hosts.txt | grep -vE '^[A-Za-z0-9.-]+$' && echo "BAD CHARS" || echo "charset OK"
```

Expected: `sorted OK`; then `18`; then `charset OK` (the third pipeline prints nothing from the inner grep).

- [ ] **Step 3: Run the release gate**

Run: `python tooling/check_release.py`
Expected: ends `RELEASE CHECK: PASS`, exit 0. The data file is inert at this point (nothing loads it yet) and safe to scan: its tokens are bare, with no scheme prefix.

- [ ] **Step 4: Commit**

```bash
git add tooling/link-policy-hosts.txt
git commit -m "tooling: add link-policy-hosts.txt data file (18 banned hosts)"
```

---

### Task 2: Rework the local gate to load the data file

**Files:**
- Modify: `tooling/check_release.py` (docstring line 12; `REQUIRED_FILES` lines 39-47; lines 53-54; lines 95-107)

**Interfaces:**
- Consumes: the data file from Task 1.
- Produces: `check_release.HOST_DATA` (str, `"tooling/link-policy-hosts.txt"`), `check_release.LinkPolicyDataError(Exception)`, `check_release.load_banned_hosts() -> list[str]` (sorted, de-duplicated; raises `LinkPolicyDataError` with message bodies `"cannot read tooling/link-policy-hosts.txt: ..."`, `"malformed line in tooling/link-policy-hosts.txt (line N): '...'"`, `"host list empty ..."`). The `SOURCE_HOSTS` module-level name is removed. Task 3 imports `load_banned_hosts`.

**Model:** standard

- [ ] **Step 1: Update the module docstring (check 3 line)**

Old (line 12):

```python
  3. No source-material links published (link policy — see docs/LICENSING.md).
```

New:

```python
  3. No source-material links published (link policy — see docs/LICENSING.md).
     Banned hosts load from tooling/link-policy-hosts.txt at runtime; the list
     is data, not a literal in this file.
```

- [ ] **Step 2: Add the data file to REQUIRED_FILES**

Old (line 46):

```python
    "tooling/validate_pack.py", "tooling/build_pack.py",
```

New:

```python
    "tooling/validate_pack.py", "tooling/build_pack.py", "tooling/link-policy-hosts.txt",
```

- [ ] **Step 3: Replace the SOURCE_HOSTS literal with the loader**

Old (lines 53-54):

```python
# Source-material hosts that must never appear as published links (link policy).
SOURCE_HOSTS = re.compile(r"https?://[^\s)\"']*(sebokwiki|nasa\.gov|ntrs|nist\.gov|govinfo\.gov|omg\.org|ocw\.mit|dodcio|dod\.mil|dla\.mil|eur-lex|europa\.eu|nato\.int|dau\.edu|cisa\.gov|energy\.gov|nde-ed\.org|everyspec\.com)")
```

New:

```python
# Source-material hosts that must never appear as published links (link policy).
# The list is data: one plain token per line in tooling/link-policy-hosts.txt.
HOST_DATA = "tooling/link-policy-hosts.txt"
_HOST_TOKEN = re.compile(r"^[A-Za-z0-9.-]+$")


class LinkPolicyDataError(Exception):
    """The banned-host data file is missing, empty, or malformed (fail closed)."""


def load_banned_hosts() -> list[str]:
    """Load banned-host tokens from HOST_DATA, sorted and de-duplicated.

    Skips blank lines and '#' comments. Any other malformed line, an unreadable
    file, or zero tokens raises LinkPolicyDataError so the gate fails closed
    instead of silently unbanning hosts.
    """
    try:
        lines = (ROOT / HOST_DATA).read_text(encoding="utf-8").splitlines()
    except OSError as e:
        raise LinkPolicyDataError(f"cannot read {HOST_DATA}: {e}") from e
    tokens: list[str] = []
    for lineno, raw in enumerate(lines, 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if not _HOST_TOKEN.fullmatch(line):
            raise LinkPolicyDataError(
                f"malformed line in {HOST_DATA} (line {lineno}): {raw!r}"
            )
        tokens.append(line)
    if not tokens:
        raise LinkPolicyDataError(f"host list empty ({HOST_DATA} has no tokens)")
    return sorted(set(tokens))
```

- [ ] **Step 4: Rework check 3 to compile the regex at runtime and fail closed**

Old (lines 95-107):

```python
    # 3. no source-material links (exclude pack chapter content — those are prose, but
    #    they are synthesized and should also be clean; include them to be strict)
    # ponytail: a "signpost" pack is pure citation — it MUST name where a spec lives, so it
    # is exempt from the link ban. Marked by `kind: signpost` in its SKILL.md frontmatter.
    signpost_dirs = {p.parent for p in ROOT.glob("packs/*/SKILL.md")
                     if re.search(r"^kind:\s*signpost\s*$", p.read_text(encoding="utf-8", errors="ignore"), re.M)}
    for p in text_files:
        if p.parent in signpost_dirs:
            continue
        body = p.read_text(encoding="utf-8", errors="ignore")
        m = SOURCE_HOSTS.search(body)
        if m:
            fail(errs, f"[links] source-material URL in {p.relative_to(ROOT)}: {m.group(0)}")
```

New:

```python
    # 3. no source-material links (exclude pack chapter content — those are prose, but
    #    they are synthesized and should also be clean; include them to be strict)
    # ponytail: a "signpost" pack is pure citation — it MUST name where a spec lives, so it
    # is exempt from the link ban. Marked by `kind: signpost` in its SKILL.md frontmatter.
    signpost_dirs = {p.parent for p in ROOT.glob("packs/*/SKILL.md")
                     if re.search(r"^kind:\s*signpost\s*$", p.read_text(encoding="utf-8", errors="ignore"), re.M)}
    try:
        hosts = load_banned_hosts()
        source_hosts = re.compile(
            r"https?://[^\s)\"']*(" + "|".join(re.escape(t) for t in hosts) + ")"
        )
    except LinkPolicyDataError as e:
        fail(errs, f"[links-parity] {e}")
        source_hosts = None
    if source_hosts is not None:
        for p in text_files:
            if p.parent in signpost_dirs:
                continue
            body = p.read_text(encoding="utf-8", errors="ignore")
            m = source_hosts.search(body)
            if m:
                fail(errs, f"[links] source-material URL in {p.relative_to(ROOT)}: {m.group(0)}")
```

The signpost exemption logic (glob, frontmatter regex, directory exclusion) is byte-identical to before. When the loader fails, the scan is skipped entirely (never run with an empty policy) and the `[links-parity]` failure alone drives `RELEASE CHECK: FAIL`.

- [ ] **Step 5: Sanity-check the loader, then run the gate**

Run:

```bash
grep -n "SOURCE_HOSTS" tooling/check_release.py
python -c "import sys; sys.path.insert(0, 'tooling'); import check_release; print(len(check_release.load_banned_hosts()))"
python tooling/check_release.py
```

Expected: the grep prints nothing (old literal fully removed); the one-liner prints `18`; the gate ends `RELEASE CHECK: PASS`, exit 0. The PASS also proves the signpost exemption survived: `packs/omg-signpost/SKILL.md` carries `https://www.omg.org/spec/...` URLs, which would flag `[links]` if the exemption broke.

- [ ] **Step 6: Prove the fail-closed paths**

Run:

```bash
mv tooling/link-policy-hosts.txt tooling/link-policy-hosts.txt.bak
python tooling/check_release.py; echo "exit=$?"
mv tooling/link-policy-hosts.txt.bak tooling/link-policy-hosts.txt
printf 'bad host! line\n' >> tooling/link-policy-hosts.txt
python tooling/check_release.py; echo "exit=$?"
git checkout -- tooling/link-policy-hosts.txt
python tooling/check_release.py
```

Expected: missing file prints two failures, `[files] missing required file: tooling/link-policy-hosts.txt` (Step 2 added it to `REQUIRED_FILES` in this same task) and `[links-parity] cannot read tooling/link-policy-hosts.txt: ...`, ending `RELEASE CHECK: FAIL (2 issue(s))`, exit 1. Malformed line prints `[links-parity] malformed line in tooling/link-policy-hosts.txt (line 25): 'bad host! line'` (6 comment lines + 18 tokens precede the appended line) and ends FAIL, exit 1. After restore, PASS again.

- [ ] **Step 7: Commit**

```bash
git add tooling/check_release.py
git commit -m "check_release: load banned hosts from link-policy-hosts.txt, fail closed on bad data"
```

---

### Task 3: Add the kept assert-based test script

**Files:**
- Create: `tooling/test_link_policy.py`

**Interfaces:**
- Consumes: `check_release.load_banned_hosts()` from Task 2 (imported via `sys.path` insert of the `tooling/` directory; importing `check_release` is safe, the gate runs only under `if __name__ == "__main__"`).
- Produces: `parity_diff(file_tokens: set[str], workflow_tokens: set[str]) -> tuple[list[str], list[str]]` (both sides sorted), and the standing command `python tooling/test_link_policy.py` (exit 0 on success, nonzero on any failed assert). Runs before the release-gate verification in Task 6.

**Model:** flash

- [ ] **Step 1: Create the test script with exactly this content**

```python
#!/usr/bin/env python3
# Copyright (c) 2026 JG Systems Consulting Ltd. — MIT License (see LICENSE).
# SPDX-License-Identifier: MIT
"""Assert-based checks for the link-policy data file and loader (no framework).

Run:  python tooling/test_link_policy.py
Exits 0 when the loader, the compiled ban regex, and the parity helper all
behave. Any failed assert raises and exits nonzero.

Banned-URL fixtures are assembled from string fragments so this file never
contains a contiguous banned URL and does not trip the link scan against itself.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_release  # noqa: E402

EXPECTED = {
    "cisa.gov", "dau.edu", "dla.mil", "dod.mil", "dodcio", "energy.gov",
    "eur-lex", "europa.eu", "everyspec.com", "govinfo.gov", "nasa.gov",
    "nato.int", "nde-ed.org", "nist.gov", "ntrs", "ocw.mit", "omg.org",
    "sebokwiki",
}
# Enforced only by the local gate until the parity fix; CI missed these four.
CI_FORMERLY_MISSING = {"cisa.gov", "energy.gov", "nde-ed.org", "everyspec.com"}


def parity_diff(file_tokens: set[str], workflow_tokens: set[str]) -> tuple[list[str], list[str]]:
    """Return (only-in-file, only-in-workflow), both sorted. Mirrors the CI check."""
    return sorted(file_tokens - workflow_tokens), sorted(workflow_tokens - file_tokens)


def main() -> int:
    # (a) the loader returns the expected token set from the data file
    hosts = check_release.load_banned_hosts()
    assert set(hosts) == EXPECTED, f"loader token drift: {sorted(set(hosts) ^ EXPECTED)}"
    assert hosts == sorted(hosts), "loader output not sorted"

    # (b) the compiled regex matches a URL for every one of the 18 tokens,
    #     explicitly including the four previously CI-missing hosts
    pattern = re.compile(
        r"https?://[^\s)\"']*(" + "|".join(re.escape(t) for t in hosts) + ")"
    )
    for token in sorted(EXPECTED):
        url = "https://www." + token + "/page"
        m = pattern.search(url)
        assert m, f"banned host not matched: {token}"
        assert token in m.group(0), f"match lost token: {token}"
    for token in sorted(CI_FORMERLY_MISSING):
        assert pattern.search("http://docs." + token + "/a"), \
            f"formerly CI-missing host unmatched: {token}"

    # (c) benign URLs do not match
    for benign in ("https://example.com/policy",
                   "https://microsoft.com/en-us/licenses",
                   "http://localhost:8000/index"):
        assert not pattern.search(benign), f"benign URL matched: {benign}"

    # (d) the divergence helper reports the exact tokens on each side, both ways
    drifted = (EXPECTED - {"dau.edu"}) | {"acme.example"}
    only_in_file, only_in_workflow = parity_diff(EXPECTED, drifted)
    assert only_in_file == ["dau.edu"], only_in_file
    assert only_in_workflow == ["acme.example"], only_in_workflow
    assert parity_diff(EXPECTED, set(EXPECTED)) == ([], [])

    print("link-policy tests: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

Note: the copyright header line uses the repo's existing tooling-file convention (see `tooling/check_release.py:2`), em dash included; keep it byte-identical to that convention. The regex wrapper literal in this file is self-scan safe: after `https?://` the `)` in the character class source stops the match before any token. The fixtures never join scheme and token in one source string.

- [ ] **Step 2: Run the test script**

Run: `python tooling/test_link_policy.py; echo "exit=$?"`
Expected: prints `link-policy tests: OK`, exit 0.

- [ ] **Step 3: Prove the test bites (scratch drift, then restore)**

Run:

```bash
sed -i '/^dau\.edu$/d' tooling/link-policy-hosts.txt
python tooling/test_link_policy.py; echo "exit=$?"
git checkout -- tooling/link-policy-hosts.txt
python tooling/test_link_policy.py
```

Expected: with `dau.edu` removed, the script raises `AssertionError: loader token drift: ['dau.edu']` and exits 1. After restore, `link-policy tests: OK` again.

- [ ] **Step 4: Commit**

```bash
git add tooling/test_link_policy.py
git commit -m "tooling: add assert-based link-policy test script"
```

---

### Task 4: Rework the CI link-policy step (trusted copy plus parity assert)

**Files:**
- Modify: `.github/workflows/validate.yml` (header comment lines 4-8; "Link policy check" step lines 37-64)

**Interfaces:**
- Consumes: the data file format contract from Task 1. Parses it as data (stdlib only); never imports repo code.
- Produces: the CI parity error line, exactly `::error::link-policy parity: tooling/link-policy-hosts.txt differs from workflow enforcement copy (only-in-file=[...] only-in-workflow=[...])`, plus `::error::link-policy parity: <reason>` with exit 1 for a missing or malformed data file. The scan itself keeps the existing `::error file=<path>::source-material URL: ...` idiom, built from the trusted copy.

**Model:** standard

- [ ] **Step 1: Update the workflow header comment**

Old (lines 4-8):

```
# RR-S-12 CI quality gate. Self-contained (inline bash + python3 stdlib only); never
# executes checked-out repository code. Runs on push to main and on every PR.
# Mirrors tooling/check_release.py (leak sentinels, link policy with signpost
# exemption, frontmatter lint, catalog validity). Both leak and link gates skip
# .planning identically (internal GSD workflow state; never ships).
```

New:

```
# RR-S-12 CI quality gate. Self-contained (inline bash + python3 stdlib only); never
# executes checked-out repository code. Runs on push to main and on every PR.
# Leak sentinels, link policy with signpost exemption, frontmatter lint, catalog
# validity. Link policy enforces from a trusted inline host set and asserts
# set-parity against tooling/link-policy-hosts.txt (the data file the local gate
# tooling/check_release.py loads) before scanning; any divergence fails the build.
# Both leak and link gates skip .planning identically (internal GSD workflow state;
# never ships).
```

- [ ] **Step 2: Replace the Link policy check step**

Old (lines 37-64): the whole step from `- name: Link policy check (no source-material URLs)` through the first `          PY` terminator, containing the `HOSTS = re.compile(...)` 14-token literal.

New (replace the whole step with exactly this):

```yaml
      - name: Link policy check (no source-material URLs)
        run: |
          python3 - <<'PY'
          # Source-material URLs are banned everywhere EXCEPT inside a `kind: signpost`
          # pack (pure citation by design). Enforcement uses the trusted inline
          # TRUSTED_HOSTS copy below, never the PR-editable data file. The parity
          # assert fails the build if tooling/link-policy-hosts.txt (loaded by the
          # local gate tooling/check_release.py) drifts from this set in either
          # direction; a missing or unparseable data file counts as divergence.
          import re, sys, pathlib
          TRUSTED_HOSTS = frozenset({
              "cisa.gov", "dau.edu", "dla.mil", "dod.mil", "dodcio", "energy.gov",
              "eur-lex", "europa.eu", "everyspec.com", "govinfo.gov", "nasa.gov",
              "nato.int", "nde-ed.org", "nist.gov", "ntrs", "ocw.mit", "omg.org",
              "sebokwiki",
          })
          DATA_PATH = "tooling/link-policy-hosts.txt"
          TOKEN = re.compile(r"^[A-Za-z0-9.-]+$")

          def parse_host_file():
              """Returns (tokens, error); tokens is None exactly when error is set."""
              try:
                  lines = pathlib.Path(DATA_PATH).read_text(encoding="utf-8").splitlines()
              except OSError as e:
                  return None, f"cannot read {DATA_PATH}: {e}"
              tokens = []
              for lineno, raw in enumerate(lines, 1):
                  line = raw.strip()
                  if not line or line.startswith("#"):
                      continue
                  if not TOKEN.fullmatch(line):
                      return None, (f"malformed line in {DATA_PATH} "
                                    f"(line {lineno}): {raw!r}")
                  tokens.append(line)
              return tokens, None

          file_tokens, err = parse_host_file()
          if file_tokens is None:
              print(f"::error::link-policy parity: {err}")
              sys.exit(1)

          only_in_file = sorted(set(file_tokens) - TRUSTED_HOSTS)
          only_in_workflow = sorted(TRUSTED_HOSTS - set(file_tokens))
          if only_in_file or only_in_workflow:
              print("::error::link-policy parity: tooling/link-policy-hosts.txt differs "
                    "from workflow enforcement copy "
                    f"(only-in-file={only_in_file} only-in-workflow={only_in_workflow})")
              sys.exit(1)

          HOSTS = re.compile(r"https?://[^\s)\"']*("
                             + "|".join(re.escape(t) for t in sorted(TRUSTED_HOSTS)) + ")")
          root = pathlib.Path(".")
          signpost_dirs = {
              p.parent for p in root.glob("packs/*/SKILL.md")
              if re.search(r"^kind:\s*signpost\s*$", p.read_text(encoding="utf-8", errors="ignore"), re.M)
          }
          fails = 0
          for p in root.rglob("*"):
              # .planning: internal GSD workflow state, never ships, holds vetting evidence URLs.
              if p.suffix not in {".md", ".json", ".yaml", ".yml", ".txt"} or ".git" in p.parts or ".planning" in p.parts:
                  continue
              if p.parent in signpost_dirs:
                  continue
              m = HOSTS.search(p.read_text(encoding="utf-8", errors="ignore"))
              if m:
                  print(f"::error file={p}::source-material URL: {m.group(0)} (see docs/LICENSING.md)")
                  fails += 1
          print("no source-material links" if not fails else f"{fails} link-policy violation(s)")
          sys.exit(1 if fails else 0)
          PY
```

Order matters: the parity assert runs before the scan (spec D3), the scan compiles its regex from `sorted(TRUSTED_HOSTS)`, and the signpost block plus scan loop keep their previous behavior byte-for-byte apart from the regex source. The workflow stays self-scan safe: frozenset tokens are plain (no scheme), and the wrapper literal's `)` breaks the character-class run before any token.

- [ ] **Step 3: Run the heredoc locally against the repo (from repo root)**

The step body is plain stdlib Python over repo files, so it runs locally with `python` for verification (CI still runs its own copy as `python3`).

Run:

```bash
python - <<'EOF'
from pathlib import Path
text = Path(".github/workflows/validate.yml").read_text(encoding="utf-8")
step = text.split("Link policy check", 1)[1].split("Pack frontmatter lint", 1)[0]
body = step.split("<<'PY'\n", 1)[1].rsplit("\n          PY", 1)[0]
dedented = "\n".join(line[10:] if line.startswith(" " * 10) else line for line in body.split("\n"))
Path("ci_link_check.tmp.py").write_text(dedented, encoding="utf-8")
print("extracted", len(dedented), "chars")
EOF
python ci_link_check.tmp.py; echo "exit=$?"
```

Expected: `extracted N chars` (N in the low thousands), then `no source-material links`, `exit=0`.

- [ ] **Step 4: Prove parity detection in both directions, plus fail-closed (scratch edits, restored each time)**

Run:

```bash
mv tooling/link-policy-hosts.txt tooling/link-policy-hosts.txt.bak
python ci_link_check.tmp.py; echo "exit=$?"
mv tooling/link-policy-hosts.txt.bak tooling/link-policy-hosts.txt

sed -i '/^dau\.edu$/d' tooling/link-policy-hosts.txt
python ci_link_check.tmp.py; echo "exit=$?"
git checkout -- tooling/link-policy-hosts.txt

printf 'example.test\n' >> tooling/link-policy-hosts.txt
python ci_link_check.tmp.py; echo "exit=$?"
git checkout -- tooling/link-policy-hosts.txt

python ci_link_check.tmp.py; echo "exit=$?"
rm ci_link_check.tmp.py
```

Expected, in order:
1. Missing file: `::error::link-policy parity: cannot read tooling/link-policy-hosts.txt: ...`, `exit=1`.
2. Token removed: `::error::link-policy parity: tooling/link-policy-hosts.txt differs from workflow enforcement copy (only-in-file=[] only-in-workflow=['dau.edu'])`, `exit=1`.
3. Token added: same line shape with `(only-in-file=['example.test'] only-in-workflow=[])`, `exit=1`.
4. Restored: `no source-material links`, `exit=0`.

These probes are the D5 demonstration that detection works in both directions; record the outputs in the PR description. The real GitHub Actions run on the PR must come back green with the 18-token enforcement.

- [ ] **Step 5: Confirm the workflow still parses as YAML and the repo is clean**

Run:

```bash
python -c "import pathlib; t = pathlib.Path('.github/workflows/validate.yml').read_text(encoding='utf-8'); assert t.count(\"<<'PY'\") == 2, t.count(\"<<'PY'\"); assert 'TRUSTED_HOSTS' in t and 'Mirrors tooling/check_release.py' not in t; print('workflow OK')"
python tooling/check_release.py
```

Expected: `workflow OK` (two heredocs remain: link policy and frontmatter lint; the "Mirrors" claim is gone); the gate ends `RELEASE CHECK: PASS`.

- [ ] **Step 6: Commit**

```bash
git add .github/workflows/validate.yml
git commit -m "ci: enforce link policy from trusted host set with parity assert vs data file"
```

---

### Task 5: Sync the documentary surfaces

**Files:**
- Modify: `.planning/codebase/INTEGRATIONS.md` (CI Pipeline bullet, line 47)
- Modify: `.planning/codebase/CONCERNS.md` (Tech Debt entry, lines 13-17)
- Modify: `CHANGELOG.md` (insert an `[Unreleased]` section before `## [1.20.0]: 2026-08-27`)

**Interfaces:**
- Consumes: the completed Tasks 1-4 (names and paths referenced in the text).
- Produces: documentary text only. No gate behavior change.

**Model:** flash

- [ ] **Step 1: Replace the INTEGRATIONS.md CI Pipeline bullet**

Old (line 47, one long bullet):

```markdown
- `.github/workflows/validate.yml` — job `content-integrity` on push to `main` and all PRs; `permissions: read-all`; four gates: leak sentinels (assembled fragments like `"CONFI""DENTIAL"`), source-material URL link policy (banned hosts: sebokwiki, nasa.gov, ntrs, nist.gov, govinfo.gov, omg.org, ocw.mit, dodcio, dod.mil, dla.mil, eur-lex, europa.eu, nato.int, dau.edu — exempted inside `kind: signpost` packs), SKILL.md frontmatter lint (kebab-case `name`, non-empty `description`), `catalog.json` JSON validity. Mirrors `tooling/check_release.py`; deliberately self-contained (inline bash + python3 stdlib; never executes checked-out code).
```

New:

```markdown
- `.github/workflows/validate.yml` — job `content-integrity` on push to `main` and all PRs; `permissions: read-all`; four gates: leak sentinels (assembled fragments like `"CONFI""DENTIAL"`), source-material URL link policy (18 banned hosts: CI enforces from a trusted inline set and asserts set-parity against `tooling/link-policy-hosts.txt` before scanning; the local gate `tooling/check_release.py` loads that file as its source; exempted inside `kind: signpost` packs), SKILL.md frontmatter lint (kebab-case `name`, non-empty `description`), `catalog.json` JSON validity. Deliberately self-contained (inline bash + python3 stdlib; never executes checked-out code).
```

The 14-host enum is dropped on purpose: the token list lives in `tooling/link-policy-hosts.txt`, and re-listing it here would recreate the drift this package removes.

- [ ] **Step 2: Mark the CONCERNS.md duplication note resolved**

Old (lines 13-17):

```markdown
**CI gate logic duplicated in three places:**
- Issue: The link-policy host regex and leak sentinels exist in `tooling/check_release.py:44-47`, `.github/workflows/validate.yml` (inline python), and indirectly in pack docs. The duplication is deliberate (CI must not execute repo code), but nothing verifies the copies stay in sync.
- Files: `tooling/check_release.py:44-47`, `.github/workflows/validate.yml` (Link policy check step)
- Impact: A host added to one copy but not the others silently weakens the other gates (e.g., a new source domain banned locally but still publishable from CI, or vice versa).
- Fix approach: Extract the host list into a plain data file (e.g., `tooling/link-policy-hosts.txt`) that both the local gate and CI read as data (reading data is not "executing repo code"), or add a CI step that diffs the regexes against a canonical definition.
```

New:

```markdown
**CI gate logic duplicated across gates (resolved 2026-09-14):**
- Issue: The link-policy host lists existed separately in `tooling/check_release.py` and `.github/workflows/validate.yml` with nothing verifying the copies stayed in sync; CI lagged the local gate by four hosts (cisa.gov, energy.gov, nde-ed.org, everyspec.com).
- Resolution: Host tokens moved to `tooling/link-policy-hosts.txt` (plain data, loaded by the local gate at runtime). CI enforces from a trusted inline set and fails the build on any set-divergence from the data file, naming the diff in both directions. `tooling/test_link_policy.py` covers the loader and parity helper.
- Files: `tooling/link-policy-hosts.txt`, `tooling/check_release.py`, `tooling/test_link_policy.py`, `.github/workflows/validate.yml` (Link policy check step)
- Residual: Leak sentinels remain deliberately duplicated (separate known duplicate). The signpost exemption stays duplicated by design (frontmatter logic, not host data); changes to it must touch both gates in one commit. A PR that edits the workflow literal and the data file consistently can weaken both gates; branch protection on `.github/workflows/` is the procedural control (ops-level, out of repo scope).
```

This also retires the stale `check_release.py:44-47` line references (the literal lived at line 54).

- [ ] **Step 3: Insert the CHANGELOG entry**

Old (lines 9-12):

```markdown
[Semantic Versioning](https://semver.org/).

## [1.20.0]: 2026-08-27
```

New:

```markdown
[Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added

- `tooling/link-policy-hosts.txt`: single data file with the 18 banned
  source-material host tokens; `tooling/check_release.py` loads it at runtime
  instead of carrying a literal.
- `tooling/test_link_policy.py`: assert-based checks for the host loader, the
  ban regex (including the four hosts CI previously missed), and parity
  reporting.

### Changed

- CI link policy enforces from a trusted inline host set and fails on
  set-divergence from the data file, closing the four-host gap (cisa.gov,
  energy.gov, nde-ed.org, everyspec.com) that GitHub Actions missed.

## [1.20.0]: 2026-08-27
```

The `[Unreleased]` heading is safe for the version gate: `check_release.py` check 4 matches `^##\s*\[(\d+\.\d+\.\d+)\]` with `re.search`, so a non-version heading is skipped and `1.20.0` still wins. Do not bump versions; website YAML and version surfaces are out of scope.

- [ ] **Step 4: Verify the gates still hold**

Run:

```bash
python tooling/check_release.py
python tooling/test_link_policy.py; echo "exit=$?"
```

Expected: `RELEASE CHECK: PASS` (proves the `[Unreleased]` heading does not trip the version agreement check and the edited files scan clean; `cisa.gov` appears bare in the CHANGELOG, which cannot match without a scheme); `link-policy tests: OK`, exit 0.

- [ ] **Step 5: Commit**

```bash
git add .planning/codebase/INTEGRATIONS.md .planning/codebase/CONCERNS.md CHANGELOG.md
git commit -m "docs: sync link-policy parity across INTEGRATIONS, CONCERNS, CHANGELOG"
```

---

### Task 6: Final verification sweep

**Files:**
- None modified. Verification only.

**Interfaces:**
- Consumes: everything above. Produces the D5 evidence set for the PR description.

**Model:** flash

- [ ] **Step 1: Run the kept test script**

Run: `python tooling/test_link_policy.py; echo "exit=$?"`
Expected: `link-policy tests: OK`, exit 0.

- [ ] **Step 2: Run the release gate**

Run: `python tooling/check_release.py; echo "exit=$?"`
Expected: final line `RELEASE CHECK: PASS — repo is release-ready against the mechanical gate.`, exit 0.

- [ ] **Step 3: Assemble PR-description evidence (D5 item 2)**

The PR description must record:
- The probe outputs from Task 2 Step 6 (local `[links-parity]` fail-closed paths).
- The probe outputs from Task 4 Step 4 (parity `::error` in both directions, plus missing-file fail-closed).
- The green GitHub Actions run on the PR with the 18-token enforcement.

- [ ] **Step 4: Confirm nothing is left uncommitted**

Run: `git status --short`
Expected: empty output (Tasks 1-5 each ended with a commit). Any stragglers belong to the task that created them; commit them there, not here.

---

## Self-review notes

- Spec coverage: rollout steps 1-6 map to Tasks 1-6; D1 (option C) is Task 4's trusted copy plus parity assert; D2 (format, charset, fail-closed both loaders) is Tasks 1, 2, and 4; D3 (message formats, parity before scan, `[links-parity]` tags, `REQUIRED_FILES`, docstring) is Task 2 and Task 4; D4 (signpost exemption untouched) is preserved byte-for-byte in Tasks 2 and 4 and proven by the clean PASS over `packs/omg-signpost`; D5 (kept script, gate runs, divergence demo) is Tasks 3, 4, and 6. Non-goals respected: no leak-sentinel, scan-scope, P5, pack, website, or branch-protection changes.
- The four previously CI-missing hosts (`cisa.gov`, `energy.gov`, `nde-ed.org`, `everyspec.com`) are in the data file (Task 1), the loader expectations (Task 3), the CI frozenset (Task 4), and the CHANGELOG entry (Task 5).
- No placeholders: every step carries full file content or exact old/new blocks with commands and expected outputs.
