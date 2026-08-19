# Phase 5 Verification — Release surface v1.17.0

Date: 2026-08-14
Phase goal: Catalog, docs, installers, and release artifacts include the new packs; v1.17.0 tagged and released.

**Verdict:** passed

## Criterion 1: check_release.py exits 0; catalog basis 54 / directory basis 56

PASS.

```
$ python tooling/check_release.py
RELEASE CHECK: PASS — repo is release-ready against the mechanical gate.
EXIT=0

$ python -c "import json;print(len(json.load(open('catalog.json'))['packs']))"
54

$ ls packs | wc -l
56
```

Counts match the validate gate basis: 54 catalog entries = 56 pack directories minus 2 signpost entries.

## Criterion 2: v1.17.0 tagged and released

PASS.

Tag is annotated and points at the release commit:

```
$ git tag -l -n3 v1.17.0
v1.17.0         v1.17.0: 8 Tier-1 public-domain packs (54 +2 signposts)

$ git cat-file -t v1.17.0
tag

$ git rev-parse v1.17.0^{commit}
bcd32afeb2ce0f34daf01262e173426dece40af1   (= bcd32af "release(v1.17.0): 8 Tier-1 public-domain packs (54 +2 signposts)")
```

Tag pushed to origin (tag object 2a8b0cb, peeled commit bcd32af — identical to local):

```
$ git ls-remote --tags origin | grep v1.17.0
2a8b0cb480a2c62c4fc83a5163cfb82bc5f5b391    refs/tags/v1.17.0
bcd32afeb2ce0f34daf01262e173426dece40af1    refs/tags/v1.17.0^{}
```

GitHub release published (not draft) with notes:

```
$ gh release view v1.17.0
name:       v1.17.0 — 8 Tier-1 public-domain packs
isDraft:    false
publishedAt: 2026-08-15T05:49:57Z
body:       2992 chars, itemizes all 8 new packs (nist-800-171, nist-800-61, ...)
```

## Version surfaces agree at 1.17.0

- `.claude-plugin/plugin.json` line 4: `"version": "1.17.0"`
- `.cursor-plugin/plugin.json` line 5: `"version": "1.17.0"`
- `README.md` lines 10, 58, 217: version badge / repo line / "Current: 1.17.0"
- `CHANGELOG.md` line 12: `## [1.17.0]: 2026-08-15`
- `docs/SOURCE-VETTING.md` references 1.17.0

## REQUIREMENTS.md

- REL-01: `[x]` — catalog/docs/NOTICE include all new packs; gate passes at 56 (48 baseline + 8 Tier-1).
- REL-02: `[x]` — v1.17.0 tagged at 56 packs; all packs pass validate_pack.py and scan_generated_skill.py.
