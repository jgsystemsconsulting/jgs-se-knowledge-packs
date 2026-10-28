# cursor-plugin-ssot-gates

Package P60. Bring `.cursor-plugin/plugin.json` under the version single-source and under CI. Today that file is the Cursor marketplace install surface and neither gate reads it. After the 1.23.0 ship it still says `1.22.0`. `RELEASE-INFO.txt`, `CHANGELOG.md` heading `[1.23.0]`, and `.claude-plugin/plugin.json` say `1.23.0`. Check 6b already compares the Cursor skills array to commercially eligible packs, and that comparison is local-only. CI never re-runs it. This cut adds the file to both gates. It does not bump a release. It does not edit pack content.

## Research

Gate mechanics were read from the working tree on 2026-10-28, post-P59, product version 1.23.0. No external API. The public Cursor plugin manifest shape is the vendor reference for the `skills` path form already in this repo.

research: https://cursor.com/docs/plugins

research: skipped (no external source beyond the vendor manifest doc; gate behavior is in-tree)

Live disagreement, read this date:

| Surface | Version | Skills |
|---|---|---|
| `.cursor-plugin/plugin.json` | 1.22.0 | 80 paths, `./packs/<slug>/SKILL.md` |
| `.claude-plugin/plugin.json` | 1.23.0 | 83 paths, `./packs/<slug>` |
| `RELEASE-INFO.txt` `Version:` | 1.23.0 | n/a |
| `CHANGELOG.md` first `## [x.y.z]` | 1.23.0 | n/a |

`CHANGELOG.md` under `## [1.23.0]` `### Noted, not a change` says the Cursor manifest stays at 1.22.0, lists 79 skills, and names P60. The 79 figure is stale. A live count on 2026-10-28 is 80 skills, 80 parsed slugs, zero missing, zero extra, against 83 `packs/*/SKILL.md` directories minus the three `commercial_use: false` packs (`easa-rules`, `med-device-eu`, `sebok`). Those three are absent from the Cursor array. That set is correct. Do not "fix" it to 79 or to 83. Do not edit the 1.23.0 section to correct the 79. The Unreleased bullet records the live count.

## Codebase context

Post-P59 baseline on main. Pack count 74 content, 8 signposts, 1 orchestrator, 83 skill directories. `catalog.json` `updated` is `2026-10-14`. Do not touch those counts or that date.

Version check 4 lives in `tooling/check_release.py` around line 1164. It fills a dict `versions` with three keys today: `plugin.json` from `.claude-plugin/plugin.json` field `version`, `CHANGELOG.md` from the first `^##\s*\[(\d+\.\d+\.\d+)\]`, `RELEASE-INFO.txt` from `Version:\s*([0-9]+\.[0-9]+\.[0-9]+)`. Website YAML versions and `docs/index.html` loci compare to `RELEASE-INFO.txt` and are not dict keys. Failure is `len(distinct) > 1 or "" in versions.values()`, message `[version] disagreement / missing: {versions}`. The module docstring item 4 names `plugin.json` and does not mention the Cursor file. CI-covered list in the same docstring (around line 74) names `version` and does not name check 6b.

CI twin is `.github/workflows/validate.yml` step `Version single-source`, heredoc starting at line 1173, python body lines 1176-1329, terminator `PY` then the next step `SKILLS index count` at line 1331. Same three dict keys. Same three regexes. Exit is `sys.exit(1 if fails else 0)` at line 1328. Header coverage map (lines 14-26) lists the pinned steps and does not mention Cursor. Header "CI does not cover" (lines 28-39) names the b-38 residual: full `validate_pack` beyond the mechanical licence subset stays local, because a fork of the rest invites permanent drift. Backlog `b-38` is that ruling. This cut does not import `validate_pack` and does not add a step that runs repository code.

`tooling/test_ci_gate.py` pins step names in `PINNED_STEPS` (lines 61-72), ten names, and asserts `len(bodies) == len(PINNED_STEPS)` with the string `expected exactly ten pinned heredocs` (line 463). `VERSION_BASE` (lines 232-238) is a five-file dict used only by the version-step negative demos. It has no `.cursor-plugin/plugin.json` entry. The version disagreement demo (around line 482) writes `VERSION_BASE` as-is: plugin and changelog say 1.2.3, `RELEASE-INFO.txt` says 1.2.4, and expects a non-zero exit containing `[version]`. Positive runs (line 1028) execute every pinned heredoc against the real tree and require exit 0. Parity literals in `RELEASE_PAIR` are the three version regexes plus the SKILLS link regex. They are not the open() path.

Check 6b (`tooling/check_release.py` lines 1363-1407) is the MA-01 backstop. If `.cursor-plugin/plugin.json` exists, parse JSON, require `skills` to be a list, collect slugs from `packs/<slug>/` path segments, subtract packs whose `PACK.yaml` contains the substring `commercial_use: false`, and fail `[cursor]` when the slug sets differ or the counts differ. Missing file is a silent pass. CI has no twin. Eligible count today is 80. Cursor count today is 80. The gate would pass on skills and fail on version once the Cursor file joins the version dict, until the version field moves to 1.23.0.

`CONTRIBUTING.md` "Before you tag" (line 115) requires `python tooling/check_release.py` on the tagged commit. The install note at lines 83-85 already says new packs go into both plugin `skills` arrays. It does not say the Cursor file is version-SSOT.

`CHANGELOG.md` `## [Unreleased]` already has `### Changed` (line 18) with two rebuild bullets. The 1.23.0 section is frozen by this spec.

## Decision register

- D1: Version SSOT gains one dict key, `cursor-plugin.json`, read from `.cursor-plugin/plugin.json` field `version`. Same `.get("version", "")` and same try/except shape as the claude read. Key name is not `plugin.json`. That key stays the claude manifest. Both keys sit in `versions`. Existing disagreement test (`len(distinct) > 1 or "" in versions.values()`) is the failure. Do not add a second comparison. Do not rename the claude key.
- D2: Missing or unreadable `.cursor-plugin/plugin.json` fails `[version]`, same as a missing claude manifest. Do not keep check 6b's file-absent-skip posture for the version read: this file is a shipped install surface. A missing file or a missing version fails through the except-path `fail()` call (the claude-shaped try/except never assigns the dict key on exception), so the empty-string disagreement arm never fires for this case.
- D3: CI version heredoc gains the same key, same path, same try/except, byte-compatible with the local read. On read failure, print `::error::[version] cannot read cursor-plugin.json: {e}`, set `versions["cursor-plugin.json"]` to `""`, and let the existing `fails += 1` on disagreement fire. Do not `sys.exit` inside the except. The claude except also falls through. Sibling steps stay untouched. Sitemap and pack-rev blocks inside this heredoc stay untouched.
- D4: `VERSION_BASE` gains `.cursor-plugin/plugin.json` with body `{"version": "1.2.3"}\n`, matching the claude fixture version, not the 1.2.4 RELEASE-INFO fixture. Existing disagreement demo keeps failing because RELEASE-INFO is 1.2.4. No new demo is required for the happy disagreement path. Add one negative demo that copies `VERSION_BASE`, sets the cursor file to `{"version": "9.9.9"}\n`, sets `RELEASE-INFO.txt` to `Version:    1.2.3\n` so the other four agree, and expects non-zero plus `[version]`. That is the cursor-specific disagreement. Follow the `v2 = dict(VERSION_BASE)` pattern already used for the website-YAML demo. Do not add a demo framework.
- D5: Check 6b moves into CI as a new step `Cursor skills eligible set`, placed immediately after `SKILLS index count` and before `Chapter basename overlap`. Pure data. Stdlib `json`, `re`, `pathlib` only. No import of `validate_pack`, `check_release`, or any other repository module. Eligibility rule stays the local substring test: a pack is excluded when `packs/<slug>/PACK.yaml` contains `commercial_use: false`. Slug parse stays `packs/<slug>/` via the same `re.search` shape as check 6b. Fail closed when the file is missing, JSON is bad, or `skills` is not a list. Local check 6b's silent skip on a missing file stays as-is. Changing that skip is out of scope. CI is the backstop that refuses a deleted manifest. Do not "align" the local skip in this cut.
- D6: `PINNED_STEPS` gains `"Cursor skills eligible set"` as the eleventh name, inserted after `"SKILLS index count"` so the list order matches workflow order. The assertion text changes from `expected exactly ten pinned heredocs` to `expected exactly eleven pinned heredocs`. The module docstring references also move: `ten inline CI gates` and `ten pinned steps` (top-of-file comments) become eleven. No other assertion string changes. Positive run against the real tree must exit 0, which it will: live sets match at 80.
- D7: Cursor skills negative demo, one case, same `demo()` helper. Tiny tree: `packs/alpha/SKILL.md`, `packs/alpha/PACK.yaml` with `commercial_use: true`, `packs/beta/SKILL.md`, `packs/beta/PACK.yaml` containing `commercial_use: false`, `.cursor-plugin/plugin.json` whose `skills` lists only `./packs/beta/SKILL.md`. Expect non-zero and `[cursor]`. Beta is excluded, so the eligible set is alpha, and the manifest has an extra excluded slug and a missing eligible slug. Do not assert the full missing/extra wording. `[cursor]` is enough, matching how the version demo asserts `[version]`.
- D8: One sentence in `CONTRIBUTING.md` under `## Before you tag`, after the sentence that CI green is necessary but not sufficient. State that `.cursor-plugin/plugin.json` version is in the single-source with the claude manifest, `RELEASE-INFO.txt`, and `CHANGELOG.md`, and that CI also checks the Cursor skills array against packs whose `PACK.yaml` does not contain `commercial_use: false`. Do not rewrite the section.
- D9: One `CHANGELOG.md` `## [Unreleased]` `### Changed` bullet. Name the gate change, not a release. State that `.cursor-plugin/plugin.json` `version` joins the single-source and is set to 1.23.0 so the tree passes, and that CI now re-checks the skills array (80 eligible packs; `easa-rules`, `med-device-eu`, `sebok` stay excluded). Do not edit `## [1.23.0]` or its Noted bullet. Do not add an `## [x.y.z]` heading.
- D10: The only product-file edit is `.cursor-plugin/plugin.json` field `version`, from `1.22.0` to `1.23.0`. No other key in that JSON changes. Skills array stays 80 entries. Do not add the three excluded packs. Do not remove a path. Do not reformat the file.

## Problem

Cursor installs from `.cursor-plugin/plugin.json`. Release tooling never reads that file's version. A ship can bump `RELEASE-INFO.txt`, the changelog heading, and the claude manifest, tag, and leave Cursor one release behind. That is the 1.22.0 versus 1.23.0 gap on this tree. The skills array is correct today and nothing in CI would notice if a later pack add updated only the claude manifest. Check 6b catches that locally, and only if someone runs `check_release.py` before the tag. CONTRIBUTING already requires that run. It does not require the Cursor file to agree, because the gate does not look.

## Approach

Four edits, one fixture, two docs lines. No new module.

1. In `tooling/check_release.py` check 4, after the claude `plugin.json` read, read `.cursor-plugin/plugin.json` into `versions["cursor-plugin.json"]` per D1 and D2. Update docstring item 4 so `plugin.json` is no longer the only manifest name. Mention `.cursor-plugin/plugin.json` in the same sentence. Update the CI-covered sentence so version coverage names both manifests. Do not add check 6b to the "CI-covered" list until the workflow step exists; then add one clause that check 6b's eligible-set comparison is mirrored by step `Cursor skills eligible set`, with the local missing-file skip called out as not mirrored.
2. Set `.cursor-plugin/plugin.json` `version` to `1.23.0` per D10. Do this in the same change as step 1. A version-dict edit without the field bump fails `check_release.py` on this tree.
3. In `.github/workflows/validate.yml`, extend the `Version single-source` heredoc per D3. Add step `Cursor skills eligible set` per D5. Add one coverage-map line for that step, next to the SKILLS index line. Add one clause to the header "CI does not cover" list only if something about 6b stays local: the missing-file skip. One line. Do not rewrite the b-38 paragraph.
4. In `tooling/test_ci_gate.py`, extend `VERSION_BASE` and `PINNED_STEPS` per D4 and D6. Add the cursor version disagreement demo per D4. Add the skills demo per D7. Update the eleven-heredoc assertion string.
5. Docs per D8 and D9.

CI skills step, behavior the heredoc must implement. Not a line-for-line paste of check 6b. Same rule, fail closed on a missing file.

- Read `.cursor-plugin/plugin.json`. Missing file, bad JSON, or `skills` not a list: print `::error::[cursor] ...` and exit 1.
- Collect pack directories from `packs/*/SKILL.md`.
- Exclude a directory when `PACK.yaml` exists and its text contains `commercial_use: false`. A pack with `SKILL.md` and no `PACK.yaml` stays eligible. That matches check 6b, which only adds to `nc_packs` when the file exists and the substring hits.
- Parse each skills entry with `packs[/\\]([^/\\]+)[/\\]`. Non-strings and non-matches are ignored, same as local.
- If slug sets differ or counts differ, print one `::error::[cursor]` line including both counts, then exit 1.
- Else print a one-line `[cursor]` pass and exit 0.

Regex literals that `test_ci_gate.py` already requires to appear in both files stay byte-identical. Do not rewrap them. The new cursor read is not in `RELEASE_PAIR`. Do not add it there. The open path is not a parity literal today, and making it one would force the CI heredoc to use `ROOT /` paths it does not use.

Workflow header and the check_release docstring are the only comments this cut adds. No new workflow `on:` triggers. No new job. No permissions change.

## Scope

In:

- `.cursor-plugin/plugin.json` field `version` set to `1.23.0`.
- `tooling/check_release.py` check 4 dict key `cursor-plugin.json`, plus the docstring sentences in Approach step 1.
- `.github/workflows/validate.yml` version heredoc cursor read, new step `Cursor skills eligible set`, and the two header comment lines (coverage map, missing-file skip).
- `tooling/test_ci_gate.py` `VERSION_BASE` entry, `PINNED_STEPS` entry, assertion count string, two negative demos.
- One sentence in `CONTRIBUTING.md` `## Before you tag`.
- One `CHANGELOG.md` Unreleased Changed bullet.

Out:

- `## [1.23.0]` and its Noted bullet, including the stale 79.
- `RELEASE-INFO.txt`, `.claude-plugin/plugin.json`, website YAMLs, `docs/index.html`, pack-page REV.
- Any file under `packs/`. Any `PACK.yaml`. Any skill path add or remove.
- Pack-count surfaces, badges, `catalog.json` `updated`, `map_version`.
- Check 6b's missing-file skip. Leave the local silent pass.
- Importing `validate_pack` or any repository module from a workflow step.
- A release bump, a tag, a GitHub release, a plugin publish, a push, a commit. This spec does not authorize those.
- Other `validate.yml` steps. Sitemap, pack-rev, link policy, pack licence, overlap, map.

## Testing

- `python tooling/check_release.py` exits 0. PASS line version is 1.23.0. Before the field bump this command fails `[version]` with both manifests in the dict. That failure is the point of D1. Do not weaken the comparison to make a stale cursor version pass.
- `python tooling/test_ci_gate.py` exits 0. Parity probe still passes. New cursor disagreement demo fails the version step. New skills demo fails the cursor step. Positive run of `Cursor skills eligible set` against the real tree exits 0.
- Full suite, the 12 modules under `tooling/test_*.py`, exits 0: `test_catalog_live_set.py`, `test_catalogue_count.py`, `test_ci_gate.py`, `test_gen_pack_pages.py`, `test_generate_capability_map.py`, `test_html_assets.py`, `test_install_guard.py`, `test_link_policy.py`, `test_pack_quality.py`, `test_routing_map.py`, `test_source_watch.py`, `test_validate_pack.py`.
- `python ~/.zcode/scripts/prose_check.py` on this spec and on the CONTRIBUTING and CHANGELOG sentences touched. Fix findings or justify.
- Confirm `.cursor-plugin/plugin.json` skills length is still 80 and `version` is `1.23.0`. Confirm `easa-rules`, `med-device-eu`, and `sebok` are still absent from that array.
- Confirm `catalog.json` `updated` is still `2026-10-14`. Confirm no `packs/*/PACK.yaml` diff.

Negative demos are not skipped. D4 and D7 name them. The existing version disagreement demo stays. It still fails on RELEASE-INFO 1.2.4 versus the other files at 1.2.3, now including the cursor fixture.

## Non-goals

- Do not treat the 1.23.0 Noted bullet's "79 skills" as a defect to fix in that section. Live count is 80. Unreleased records it.
- Do not add the three `commercial_use: false` packs to the Cursor manifest. Exclusion is the product rule, not an omission.
- Do not make CI import `check_release.py` so the twin cannot drift. b-38 forbids executing repository code from the workflow. The twin is inline stdlib. `test_ci_gate.py` is the drift control for pinned steps, not a shared import.
- Do not bump to 1.24.0 or any other version. The field moves to the current single-source value, 1.23.0, so the gate can pass. The next release cut owns the next bump, and after this change that bump must edit the cursor field too or check 4 fails.
- Do not close backlog rows. `b-38` stays. This cut respects it.
