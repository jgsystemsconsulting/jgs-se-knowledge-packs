# Phase 8 Security Audit — Agent-Enablement Surface

**Range audited:** `d821099..ab42f7a` (3 files: docs/capability-map-CONTRACT.md, docs/capability-pack-map.json, docs/capability-pack-map.md)
**Date:** 2026-08-17
**Method:** diff-scoped scans (added lines) + whole-file scans of all 3 changed docs + programmatic scan of all 628 map entries + adversarial gate-bypass tests in a sandbox copy.

**Verdict:** SECURED

## Findings

| # | Check | Result | Evidence |
|---|---|---|---|
| S1 | No URLs / secrets / PII in new docs | PASS | Added lines in range: 0 matches for `https?://`, `www.`, `ftp://`, email patterns; 0 matches for api-key/token/secret/password patterns (two `sk-` regex hits were false positives inside "ri**sk-a**nd"). Whole-file scans of CONTRACT.md and map md: 0 URLs/emails. |
| S2 | No source-URL leakage in map + contract | PASS | Programmatic scan of all 628 entries (pack/chapter/note): 0 URL/email hits. No full URLs anywhere in the changed docs; no bare domains introduced either. Source identity is by pack slug and standard short-name only. |
| S3 | Gate cannot be bypassed by fake paths | PASS (with hardening note SEC-1) | Reasoned + tested. Chapter coverage cannot be faked: chapter-set equality is name-exact and bidirectional (verified RED on add/delete/new-pack mutations), envelope/threshold/uniqueness violations all exit 1 (tested: duplicate (pack,chapter) pair, thinned threshold cluster, v1 keyless shape — all exit 1). Non-support rows with odd paths land in `map_chapters` and fail set equality. One narrow gap: support-file existence check accepts traversal/absolute paths (SEC-1). |
| S4 | No prompt-injection content in new docs | PASS | 0 matches for injection markers (ignore/disregard/system prompt/you are now/override/jailbreak/as an AI/…) in CONTRACT.md, map md, and all 628 JSON notes. Notes are plain one-line capability rationales. |
| S5 | Commits touch only expected paths | PASS | `git diff --name-only d821099..ab42f7a` = exactly the 3 expected docs files. Post-range follow-ups (99d3c8c, 097ba0c) touch `.planning/` only. No tooling/, packs/, or scripts/ changes in range. |
| S6 | Gate script hygiene | PASS | `check_capability_map.py` is stdlib-only, read-only filesystem + JSON parse, no shell/eval/network, no secrets, MIT header + SPDX intact. |

## SEC-1 (WARNING, hardening — not an open threat)

`check_capability_map.py` builds support-file paths as `packs_root / pack / rel` where `rel` is the entry text minus the `" (support file)"` suffix, and only checks `path.is_file()`. It does not confine the resolved path to the pack root. Verified in sandbox (gate exit 0 for both):

- `"chapter": "chapters/../cheatsheet.md (support file)"` — traversal to a real pack-root file passes.
- `"chapter": "<absolute path to a repo file> (support file)"` — absolute paths pass (pathlib join replaces the base).

**Why contained:** it cannot fake chapter coverage or evade staleness (those checks are name-exact against `packs/`); it only lets a support-file row point outside its pack. The map JSON is a first-party, human-reviewed, in-repo file with no untrusted-input producer in this repo's pipeline, and the gate is a staleness check, not a trust boundary. Residual risk sits with downstream consumers that naively join `packs/<pack>/<chapter>` for support rows (path could resolve outside the pack root).

**Recommended fix (one guard clause):** reject entries where `chapter` contains `..` components or `Path.is_absolute()` before the existence check, or verify `path.resolve().is_relative_to((packs_root / pack).resolve())`.

Secondary hardening nit: duplicate cluster names would last-win-overwrite in the `counts` dict (currently 32/32 unique — no live issue).

## Threat Flags

None beyond SEC-1 (contained, documented above with repro and fix).
