# Spec: align-website-yaml-versions (2026-09-14)

Package P1, size S. Satisfies impl-review CR-01 (`.planning/phases/21-contract-rewrite-release-surfaces/21-IMPL_REVIEW.md:64-71`) so master_flow can re-gate. Bookkeeping and status flips are parent-owned and stay out of this spec's tasks.

## Problem

Phase 21 shipped the 1.20.0 version trio (RELEASE-INFO.txt:3, plugin.json:4, CHANGELOG.md:12) and created the local annotated tag v1.20.0 on commit 046799b, but the two public-website product YAMLs still claim 1.19.1:

- `docs/products/website/01-jgs-se-knowledge-packs.yaml:15`: `version: "1.19.1"` (top-level key)
- `docs/products/website/catalog.yaml:13`: `version: "1.19.1"` (nested under `products[0]`)

These files are the RR-B-19 source the public website is generated from. Pushing or running /gsd-ship from this state publishes a product catalogue that contradicts RELEASE-INFO and the annotated tag, the exact failure class REL-21-02 exists to prevent. No mechanical gate covers the two files today, which is why check_release stayed green through the drift.

## Goal

Both website product YAMLs carry `version: "1.20.0"`, `python tooling/check_release.py` passes, and the local annotated tag v1.20.0 points at the fix commit. Nothing is pushed.

## In scope

- Set `version: "1.20.0"` in both website product YAMLs.
- Optional one-line consistency check in check_release.py covering the two YAML versions vs RELEASE-INFO.txt.
- Re-run `python tooling/check_release.py`; it must PASS.
- Delete and recreate the LOCAL annotated tag v1.20.0 on the fix commit. The tag must NOT be pushed.

## Out of scope

- git push / gh release create / /gsd-ship.
- New packs or pack content edits.
- WR-01 / WR-02 / WR-03 generator residuals (package P7).
- .planning ledger ticks and master_flow re-gate (package P8 and parent-owned bookkeeping).
- FUT-04 / IO-05 / IO-06.

## Codebase context

From `docs/superpowers/context/2026-09-14-align-website-yaml-versions-context.md` (Track 1, CONTEXT_COMPLETE):

- Both version fields are quoted strings. The shapes differ: top-level in the product file, nested under `products[0]` in catalog.yaml. Any scrape must match `version: "X.Y.Z"` at either indent.
- Nothing in tooling/ or CI reads these two YAMLs. packs.html takes its version from RELEASE-INFO (tooling/gen_packs_page.py:42-43) and validate.yml only checks catalog.json. The bump cannot break CI and no derived artifact embeds the version.
- check_release.py check 4 (lines 108-122) is the version single-source block: `json.loads` for plugin.json, `^##\s*\[(\d+\.\d+\.\d+)\]` for CHANGELOG, `Version:\s*([0-9]+\.[0-9]+\.[0-9]+)` for RELEASE-INFO, failures raised through the existing `fail(errs, f"[version] ...")` idiom. Stdlib only; the script never imports yaml.
- Tag v1.20.0 is annotated (tag object 61fd653), peels to commit 046799b, and exists only locally; no remote branch contains it. Existing message: `chore: annotate v1.20.0 generator refresh path`.
- Historical 1.19.1 strings are keep-classified: CHANGELOG.md:44 (`## [1.19.1]:` version heading), docs/capability-map-CONTRACT.md:35 (meaning-table example), docs/capability-pack-map.md:18 (changelog line; v1.20.0 already sits at line 17). `packs/*/PACK.yaml` `source_version` is a different version class and must never enter this check.
- The graphify post-commit hook can in principle append a second commit after the fix commit, so the tag step must anchor to the fix commit explicitly.

## Approach

One commit, then retag, in this order.

1. **Edit both YAMLs.** Set `version: "1.20.0"` at `01-jgs-se-knowledge-packs.yaml:15` and `catalog.yaml:13`. Keep the quotes and surrounding structure byte-identical otherwise; the two lines sit at different indents, so edit each in place rather than copying one over the other.

2. **Optional gate line (contract-optional, recommended).** In check_release.py check 4, after the RELEASE-INFO parse, read the two website YAML files and regex-extract `version:\s*"([0-9]+\.[0-9]+\.[0-9]+)"` from each (first match per file, which is the version key itself). Fail through the existing `fail(errs, f"[version] ...")` idiom if either value is missing or differs from the RELEASE-INFO version that check 4 already parsed into the `versions` dict. Stdlib regex in the existing idiom, no PyYAML. Scope to exactly the two website YAML paths, never a repo-wide `version:` grep: packs carry `source_version` and docs carry keep-class historical 1.19.1 strings. "One-line" is the contract's intent (minimal hardening); the full gate package remains P2, so do not build validation structure beyond this.

3. **Commit.** One commit holding the two YAML edits plus the tooling edit if taken. Suggested message: `fix: align website product YAMLs to 1.20.0 (CR-01)`. Record the commit hash.

4. **Verify HEAD, then retag.** `git rev-parse HEAD` must equal the fix commit hash (the graphify hook can append a second commit). Then delete and recreate the tag on the explicit hash: `git tag -d v1.20.0` followed by `git tag -a v1.20.0 -m "chore: annotate v1.20.0 generator refresh path" <fix-commit-hash>`. Tag by hash, not by a symbolic ref. The tag is safe to move because it is local-only.

5. **Re-run the gate.** `python tooling/check_release.py` must exit 0.

No push commands run at any point in this package. `git push` in any form, including tag refs, is banned here.

## Acceptance criteria

1. `git grep -n "1.19.1" docs/products/website` returns nothing; both files show `version: "1.20.0"` with original quoting and structure intact.
2. `python tooling/check_release.py` exits 0.
3. `git cat-file -t v1.20.0` prints `tag`; `git rev-parse "v1.20.0^{commit}"` equals the fix commit hash; that commit contains the two YAML edits (and the tooling edit if taken).
4. The tag is local only: `git branch -r --contains <fix-commit-hash>` returns empty. No push command runs in this package; that clause is a process contract (see Approach), not a mechanically checkable assertion.
5. Keep-class strings untouched: CHANGELOG.md:44, docs/capability-map-CONTRACT.md:35, docs/capability-pack-map.md:18 still read 1.19.1.
6. If the optional check was added: temporarily setting one website YAML version to a different value makes check_release fail with a `[version]` error naming the file; changing a `packs/*/PACK.yaml` `source_version` does not trigger it. Restore the file afterwards.
7. CR-01 is satisfied. The master_flow re-gate happens outside this package.

## Risks

| Risk | Mitigation |
|------|------------|
| graphify post-commit hook appends a commit after the fix commit, so HEAD moves before tagging | Verify `git rev-parse HEAD` equals the fix hash at tag time; tag the explicit hash |
| Accidental push of the moved tag | All push commands banned in this package; the tag stays local by contract |
| Repo-wide version grep false-fails on packs/*/PACK.yaml and historical docs | Checks scoped to the two website YAML paths; the three keep-class strings are whitelisted and untouched |
| Indent or quote drift in the nested catalog field | Single-line in-place edits; criterion 1 checks the exact `version: "1.20.0"` formatting |

## Research

research: skipped (version values are fixed by the repo's own RELEASE-INFO.txt and the local annotated tag; no external API, library, platform, or version choice is involved)

## Open questions

None.
