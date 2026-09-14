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
