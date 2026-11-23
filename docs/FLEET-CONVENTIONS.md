<!--
Copyright (c) 2026 JG Systems Consulting Ltd. MIT License (see ../LICENSE).
SPDX-License-Identifier: MIT
-->

# Fleet conventions

Rules for the industry knowledge-pack fleet: how sector repos are named, laid out, owned, indexed, licensed, and gated. Pack layout detail stays in `docs/PACK-SPEC.md`. This file does not restate it.

## Repo naming

Sector catalogue repos use the pattern `jgs-<sector>-knowledge-packs`, where `<sector>` is the short sector slug (for example `se`, `aviation`, `med-device`, `automotive`, `nuclear`, `uk-defence`). The template repository is `jgs-sector-repo-template`. It is not itself a sector catalogue and is not installed as packs.

## Packs layout

Content lives under `packs/<slug>/`. Each pack directory holds at least `SKILL.md` and `PACK.yaml`, plus the chapter and supporting files the pack spec requires for its kind (`content`, `signpost`, or `orchestrator`). Slugs stay lowercase kebab-case: `[a-z0-9-]+`.

## One sector orchestrator per repo

Each sector repo has exactly one orchestrator skill (`kind: orchestrator`). In this repo that directory is `packs/se`. The command users type is `/se`. The orchestrator carries no source content. It routes free-text questions through the routing map in its `SKILL.md`.

## Sibling repos, never absorption

Sector repos are siblings. A new sector does not fold into the SE catalogue. Packs do not migrate across sector boundaries by absorption. If a pack belongs in another sector, it is authored or moved there under that sector's release train. The owner tree is canonical. A diff in this repo against the owner tree is drift evidence, not a merge list.

## Release ownership

Each sector repo owns its own release train: version in `RELEASE-INFO.txt`, website product YAMLs, changelog, tags, and CI. A green build in one sector does not release another. The hub never cuts sector tags.

## Hub index contract

The hub indexes sector repos with links plus metadata only (name, slug, version, status, short scope). The hub does not carry pack content, chapter text, or installer copies of sector packs. Discovery points at the sector repo. Install runs against that repo.

## Licensing split

Pack content licence lives with the pack (`packs/<slug>/LICENSE` and per-pack NOTICE attribution). Repository tooling, scaffolding, docs chrome, and gates are MIT under the root `LICENSE`. Do not relicense pack content under the repo MIT line.

## Link-policy host lockstep

`tooling/link-policy-hosts.txt` and the inline trusted-host set in `.github/workflows/validate.yml` move in lockstep. Edit both or neither. A host present in only one place is drift and fails the gate.

## Sector minimum bar

A sector earns its own repo when a single gate-green instantiation has all of:

1. Content floor. At least one redistributable full pack (tier 1, or tier 2/3 with per-document licence capture), or a landing set of at least two signpost packs whose free-path rows link to shipped landing packs.
2. Orchestrator coverage. A named sector orchestrator whose routing map covers every content pack in the repo.
3. Gates green. `tooling/validate_pack.py`, `tooling/check_release.py`, and CI (`tooling/test_ci_gate.py` parity with `.github/workflows/validate.yml`) exit 0 on the minted repo.

Below the bar the sector stays in programme backlog. No empty repos and no single-signpost-only forks.

## Bumping gate constants

When the live catalogue changes note-row counts or the expected signpost list, update these sites in one commit:

1. `NOTES_COUNT` and the matching `assert NOTES_COUNT == ...` in `tooling/generate_capability_map.py`. Recompute the length from `docs/capability-pack-map-note-overrides.json` after the row edit. Keep a one-line history comment. Do not hand-edit `docs/capability-pack-map.json`. Regenerate it.
2. `expected_signposts` in `tooling/check_classification_rules.py`, in list order.
3. `signpost_packs` in `docs/classification-rules.json`, same names, same order as site 2.
4. The `rules_of_construction` bullet that names the signpost packs, same names as site 2.
5. `map_version` on `docs/classification-rules.json` and `docs/capability-pack-map-note-overrides.json`, set to the `RELEASE-INFO.txt` Version, then regenerate so the map envelope matches.

This repo has no `EMPTY_TREE_PAIR` constant in `tooling/test_ci_gate.py`. Do not add one. `.github/workflows/validate.yml` does not assign `NOTES_COUNT` or `expected_signposts`. Do not add those assignments. Do not lower `THRESHOLDS` in `tooling/check_capability_map.py` to make a floor pass. If a floor fails, stop and report.
