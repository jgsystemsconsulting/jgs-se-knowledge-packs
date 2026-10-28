# EXECUTED: cursor-plugin-ssot-gates (P60)

Cursor install surface brought under the release single-source and CI. Product version stays 1.23.0; counts 74/83 frozen.

## What shipped

- `.cursor-plugin/plugin.json` version 1.22.0 → 1.23.0 (skills array byte-identical, 80 entries = exactly the commercial_use-eligible packs; easa-rules / med-device-eu / sebok excluded).
- `tooling/check_release.py`: versions dict gains `cursor-plugin.json` (except-path `fail()` on missing/unreadable; the empty-string disagreement arm never fires); docstring item 4 names both manifests; CI-covered list names cursor skills with the documented fail-closed delta.
- `.github/workflows/validate.yml`: `Version single-source` heredoc gains the same cursor read; NEW step `Cursor skills eligible set` after `SKILLS index count` — pure-data mirror of check 6b (stdlib, fail-closed, no validate_pack run per the b-38 no-fork ruling).
- `tooling/test_ci_gate.py`: PINNED_STEPS eleven names; assert string `expected exactly eleven pinned heredocs`; docstrings ten→eleven; VERSION_BASE gains the cursor fixture; new negative demos `version-cursor-disagreement` and `cursor-skills-mismatch` (`[cursor]`).
- `CONTRIBUTING.md` pre-tag section: cursor manifest named in the single-source sentence. CHANGELOG Unreleased Changed bullet (1.23.0 section untouched; its historical 79-skills Noted bullet stays).

## Execution notes

- One-wave reviews (skeptic+combined ARL) on spec and plan; two rationale/wording fixes pre-execution (D2 except-path mechanism, D6 docstring counts, heredoc indent 10, skip-reason honesty).
- Final review: one Important (docstring item 4) fixed in 2e64618; two minors adjudicated (CI fail-closed vs local skip delta documented in the docstring; D9 strict prose declined — the bullet states the rule; the count 80 is verifiable from the manifest).
- Eleven-step positive run against the real tree: `Cursor skills eligible set :: [cursor] manifest skills match eligible packs (80)`.

## Gates at close

12/12 test modules; test_ci_gate OK (parity, extraction, negative demos, positive runs); RELEASE CHECK PASS v1.23.0; counts 74/83; tree clean.

done
