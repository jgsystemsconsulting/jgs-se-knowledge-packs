# Spec: cut the 1.23.0 release surfaces

## Research

research: section-url

Release conventions in this repo are written down, not inferred.

- `CONTRIBUTING.md` section "Before you tag" requires `python tooling/check_release.py` on the exact commit being tagged. The PASS line must read `RELEASE CHECK: PASS (v<version> @ <short-sha>)` and the sha must match that commit. An `@ no-git` receipt never satisfies it. CI green is necessary and not sufficient. Do not cut a tag or a GitHub Release on CI green alone.
- `CHANGELOG.md` states the format follows Keep a Changelog 1.1.0 and versioning follows Semantic Versioning. https://keepachangelog.com/en/1.1.0/ and https://semver.org/
- Precedent for the tag shape: `v1.22.1` is an annotated tag whose message is `jgs-se-knowledge-packs 1.22.1`, created 2026-10-26T10:03:12Z on commit `5b03208` ("docs: complete the 1.22.1 release surfaces"). Annotated tags are the git default for a release marker. https://git-scm.com/docs/git-tag

## Codebase context

context: ad-hoc

Evidence gathered against branch `packages-2026-10-27` at HEAD `53d4413` (2026-10-28).

`v1.22.1` was tagged 2026-10-26T10:03:12Z. 44 commits have landed since. Five groups, named so the release section can cite them.

1. Per-pack landing pages. `f99a0ea` piloted twelve packs. `20ba23a` fixed the title-suffix collision. `e84ad2f` landed the remaining content packs as pages. `1b5c8e1` recorded the full set on the distribution ledger.
2. CI trust. `6c928d3` through `bb3468c` added the licence and signpost shape gate and pinned its error gists. `1f235bd` pinned `actions/checkout` to the v4 commit SHA. `9303157` split the banned URL in the link-policy demo fixtures. `a4d1822` and `fa2e230` added the html-assets gate and pointed it at pack landing pages. `6058cd0` and `e784af9` wired sitemap and pack-page REV into the release gate. `ad53d46` added the local gen-pack-pages probe. `e09dd5d` and `bd83878` expanded the CONTRIBUTING registration checklist and added the pre-tag section.
3. Doc-truth fixes. `34ef62a` corrected the PACK-SPEC install path. `9b224e8` stamped `catalog.json` `updated` to 2026-10-14. `352137a` dropped shipped META keys and PACK-BACKLOG pointers. `e2df267` synced the website YAML family inventory to the live catalogue.
4. Two new content packs. `jsp-936` (Dependable AI in Defence, OGL v3, JSP 936 Part 1 V1.1) and `fhwa-its-se` (Systems Engineering for ITS, fourth generation, December 2022). Both registered on the catalogue surfaces, the capability map, and the generated pages.
5. Planning-doc commits. `53d4413`, `9a30257`, `9b3b81d`, `7be6a26`, `53f2871`, `e7b1674`, `f9b8515`. Backlog grooming, package-loop re-runs, EXECUTED logs, IVL logs, specs, plans.

Version single-source today. `tooling/check_release.py` check 4 reads three files and demands they agree: `RELEASE-INFO.txt` `Version:`, the first `## [x.y.z]` heading in `CHANGELOG.md`, and `.claude-plugin/plugin.json` `version`. Check 4a demands the same string in `docs/products/website/01-jgs-se-knowledge-packs.yaml` and `docs/products/website/catalog.yaml`. The `[site-version]` check demands it at three `docs/index.html` loci: `softwareVersion`, masthead `REV <b>`, footer `Rev`. Check 19 demands it at both REV loci of every `docs/packs/<slug>/index.html` and demands sitemap pack locs match the live catalog. The CI "Version single-source" step in `.github/workflows/validate.yml` twins checks 4, 4a, site-version, and 19 with byte-identical regex literals, and `tooling/test_ci_gate.py` asserts that parity. Neither the version-SSOT check nor the CI heredoc reads `.cursor-plugin/plugin.json` (the local-only check 6b does read the cursor skills list, by design).

Counts as of HEAD. `catalog.json` holds 73 packs. `packs/` holds 82 directories: 73 content packs (no `kind:` key), 8 signposts, 1 orchestrator. `.claude-plugin/plugin.json` declares 82 skill paths. `.cursor-plugin/plugin.json` declares 79 and sits at version `1.22.0`.

## Goal

Prepare the 1.23.0 release surfaces on branch `packages-2026-10-27` for everything shipped since `v1.22.1`, run the gates, and create the annotated tag locally. Stop there. The user pushes, merges, and opens the GitHub Release.

## Decision register

- D1: Version is 1.23.0. Two new content packs (`jsp-936`, `fhwa-its-se`) are MINOR-level additions under SemVer. The CI gate group is feature-level and rides the same bump. A patch bump would understate two new packs.
- D2: `.cursor-plugin/plugin.json` version stays at 1.22.0. The version single-source (local check 4 and the CI heredoc) does not read it, so leaving it does not break a gate. Folding its version line into the single-source is P60, out of scope. The release section states the gap in one line rather than hiding it.
- D3: The Unreleased Changed bullet claiming "all 80 skill paths" is rewritten in the 1.23.0 section to the final count, 82. 80 was true at `adb7c5d` (2026-10-26). `jsp-936` registration took it to 81 and `fhwa-its-se` registration to 82. Shipping the stale number would document a lie.
- D4: `RELEASE-INFO.txt` `Staged:` is set to 2026-10-28T00:00:00Z, the release date. The 2026-09-27 stamp belongs to the 1.22.0 cut and was never refreshed at 1.22.1.
- D5: The run creates the annotated tag locally and stops. No push. Tag command is `git tag -a v1.23.0 -m "jgs-se-knowledge-packs 1.23.0"`, matching the `v1.22.1` message shape. The user pushes the tag and the branch.
- D6: Planning-doc commits do not appear in the changelog. Precedent: the 1.22.1 section lists user-visible fixes, inventory prose, and tooling, and lists no spec, plan, EXECUTED, or IVL log. Group 5 stays out.
- D7: The 1.23.0 section documents the landing-pages group and the CI-gates group explicitly, each as its own bullet, not folded into a pack bullet.

## Approach

One commit on `packages-2026-10-27` that moves the version from 1.22.1 to 1.23.0 across every surface the release gate reads, rewrites the changelog, regenerates the version-stamped pages, then tags.

Order matters because the page generators read `RELEASE-INFO.txt` at render time.

1. Edit `RELEASE-INFO.txt`. `Version:` and `Tag:` to 1.23.0 and v1.23.0. `Staged:` to 2026-10-28T00:00:00Z (D4).
2. Edit `CHANGELOG.md`. Rename `## [Unreleased]` to `## [1.23.0]: 2026-10-28`. Keep both existing Added bullets. Rewrite the Changed bullet to 82 skill paths (D3). Add the landing-pages bullet and the CI-gates bullet (D7). Add the doc-truth bullet. Add one line stating `.cursor-plugin/plugin.json` remains at 1.22.0 pending P60 (D2). Leave a fresh empty `## [Unreleased]` above the new section so the next cut has somewhere to land.
3. Edit `.claude-plugin/plugin.json`. `version` to `1.23.0`. Do not touch the `skills` array.
4. Edit the two website YAMLs. `version:` to `"1.23.0"` in `docs/products/website/01-jgs-se-knowledge-packs.yaml` and `docs/products/website/catalog.yaml`. Do not touch `catalog.json` `updated` or any pack count claim.
5. Edit `README.md`: replace every `1.22.1` occurrence — the version badge URL and its `alt="Version 1.22.1"` text, the install prompt body line, and the Version section `Current:` line. The grep test at the end is the completeness check; do not rely on a locus list alone.
6. Edit `CITATION.cff`. `version: 1.23.0`.
7. Edit `docs/index.html` at four loci. The gate checks three (`softwareVersion`, masthead `REV <b>`, footer `Rev`). The fourth, the provenance label `REV: <span style="color:var(--text)">`, is not gated and goes stale silently, so edit it too.
8. Regenerate. Run `python tooling/gen_pack_pages.py` and `python tooling/gen_packs_page.py` so all 73 `docs/packs/<slug>/index.html` files and `docs/packs.html` pick up 1.23.0 from `RELEASE-INFO.txt`. Both REV loci per page. `docs/sitemap.xml` rewrites in the same run. Its `<lastmod>` stamps the run date, so the regenerated file must be committed with the rest, not treated as noise.
9. Pre-commit smoke gate. `python tooling/check_release.py` on the working tree must pass; the sha it prints is not yet the release sha. Run `python tooling/test_ci_gate.py` (it must pass unchanged: no heredoc pin changes in this run).
10. Commit the surfaces with subject `docs: complete the 1.23.0 release surfaces` (v1.22.1 precedent). This commit is the release commit.
11. Post-commit gate. Run `python tooling/check_release.py` again on the committed tree; it must print `RELEASE CHECK: PASS (v1.23.0 @ <short-sha>)` with the sha equal to `git rev-parse --short HEAD` of the release commit. This is the receipt the tag and Testing bind to.
12. Tag that commit (D5): `git tag -a v1.23.0 -m "jgs-se-knowledge-packs 1.23.0"`. Confirm `git rev-parse v1.23.0^{}` equals the release commit and the PASS line sha. Stop.

## Files touched

Version surfaces, hand-edited:

- `RELEASE-INFO.txt`
- `CHANGELOG.md`
- `.claude-plugin/plugin.json`
- `docs/products/website/01-jgs-se-knowledge-packs.yaml`
- `docs/products/website/catalog.yaml`
- `README.md`
- `CITATION.cff`
- `docs/index.html`

Generated, regenerated and committed:

- `docs/packs.html`
- `docs/sitemap.xml`
- `docs/packs/<slug>/index.html` for all 73 catalog packs

Not touched:

- `.cursor-plugin/plugin.json` (D2)
- `catalog.json`
- anything under `packs/`
- `.github/workflows/validate.yml`
- `tooling/`

## Changelog content

`## [1.23.0]: 2026-10-28`

Added:

- `fhwa-its-se` content pack from Systems Engineering for ITS, fourth generation (December 2022), reconstructed notes, registered on the catalogue surfaces.
- `jsp-936` content pack from JSP 936 Part 1 Directive V1.1, reconstructed notes, registered on the catalogue surfaces.

Changed:

- `.claude-plugin/plugin.json` declares all 82 skill paths. 73 content packs, 8 signposts, 1 orchestrator. The 80 figure was true on 2026-10-26 and went stale when `jsp-936` and `fhwa-its-se` registered.
- Per-pack landing pages now cover the full live catalogue, `docs/packs/<slug>/index.html` for all 73 content packs, with `docs/sitemap.xml` generated from `catalog.json` rather than from the run list. A title-suffix collision is fixed for pack titles that already end in a colon phrase.
- CI trust gates added since 1.22.1: pack licence and signpost shape, html-assets over `docs/*.html` and pack landing pages, sitemap and pack-page REV on the release gate, and `actions/checkout` pinned to the v4 commit SHA. The CONTRIBUTING registration checklist and pre-tag section were expanded to match.
- Doc-truth fixes: PACK-SPEC install path points at the root installer, the website YAML family inventory matches the live catalogue, and shipped META keys and PACK-BACKLOG pointers are dropped from the build orchestrator.

Noted, not a change:

- `.cursor-plugin/plugin.json` stays at version 1.22.0 and lists 79 skills. Its version is outside the single-source by design. Closing that gap is P60.

Catalogue line: 73 content packs, 8 signposts, 1 orchestrator, 82 skills.

## Testing

- `python tooling/check_release.py` prints `RELEASE CHECK: PASS (v1.23.0 @ <short-sha>)` and the sha equals `git rev-parse --short HEAD` of the release commit.
- The twelve `tooling/test_*.py` modules pass (`for t in tooling/test_*.py; do python "$t"; done`), including `tooling/test_ci_gate.py`. No heredoc pin changes, so the parity assertions must pass without edits. If one fails, the cause is outside this spec and the run stops.
- Grep for `1.22.1` across the live surfaces returns nothing: `RELEASE-INFO.txt`, `README.md`, `CITATION.cff`, `.claude-plugin/plugin.json`, both website YAMLs, `docs/index.html`, `docs/packs.html`, `docs/sitemap.xml`, `docs/packs/*/index.html`. `CHANGELOG.md` keeps `1.22.1` inside the `## [1.22.1]` section and nowhere else. `.cursor-plugin/plugin.json` keeps `1.22.0` (D2).
- `git rev-parse v1.23.0^{}` equals the release commit. `git for-each-ref refs/tags/v1.23.0 --format='%(objecttype)'` prints `tag`.
- `git status -sb` shows the branch ahead of its remote and shows no push has happened.

## Do not

- Do not push the branch or the tag.
- Do not merge to `main`. Branch integration stays the user's decision. The finishing-branch menu stays open.
- Do not open a pull request.
- Do not edit pack content, `packs/*/PACK.yaml`, `packs/*/SKILL.md`, or chapter files.
- Do not change `catalog.json`, including its `updated` stamp.
- Do not edit a version string anywhere outside the files named above. `map_version`, `source_version`, and historical changelog sections stay as they are.
- Do not bump `.cursor-plugin/plugin.json`, and do not extend the version single-source to read it. That is P60.
- Do not edit `.github/workflows/validate.yml` or any heredoc. A heredoc edit would force a `test_ci_gate.py` parity update this run does not need.
- Do not list planning-doc commits in the changelog (D6).
- Do not create the GitHub Release. The user does that after pushing the tag.

## Out of scope

- P60, bringing `.cursor-plugin/plugin.json` under the version single-source and mirroring check 6b into CI. (The manifest is not short three skills: `easa-rules`, `med-device-eu`, and `sebok` are `commercial_use: false` and correctly excluded; 79 is the exact eligible count.)
- Pushing, merging, and the GitHub Release.
- Any pack content change found during the gate run. A gate failure caused by pack content stops the run and gets reported, not fixed here.
