<!--
Copyright (c) 2026 JG Systems Consulting Ltd. MIT License (see ../LICENSE).
SPDX-License-Identifier: MIT
-->

# Cross-pack boundaries

A publication has one content owner. The owner is one sector repo. A sibling may name that slug and that repo. A sibling must not ship a same-slug content copy or a same-slug signpost copy. UK defence publications keep the same one content owner rule, already recorded in `jgs-uk-defence-knowledge-packs` `docs/CROSS-PACK-BOUNDARIES.md`.

| Slug | Kind | Owner repo | SE action in v1.24.5 |
|---|---|---|---|
| easa-rules | content | jgs-aviation-knowledge-packs | deleted, no replacement |
| faa-8110-49 | content | jgs-aviation-knowledge-packs | deleted, no replacement |
| avionics-signpost | signpost | jgs-aviation-knowledge-packs | deleted, no replacement |
| fda-med-device | content | jgs-med-device-knowledge-packs | deleted, no replacement |
| nhtsa-vehicle | content | jgs-automotive-knowledge-packs | deleted, no replacement |
| automotive-signpost | signpost | jgs-automotive-knowledge-packs | deleted, no replacement |
| functional-safety-signpost | signpost | jgs-automotive-knowledge-packs | deleted, no replacement |
| nrc-nuclear | content | jgs-nuclear-knowledge-packs | deleted, no replacement |

Sector copies are canonical. SE diffs against those copies are drift evidence. This cut does not transplant, merge, or import those diffs.

This cut does not edit `jgs-nuclear-knowledge-packs`. That repo is 42 commits ahead of origin. A checker pointer line there is deferred. The ownership row above still names nuclear as the owner of `nrc-nuclear`. Do not edit the nuclear repo to satisfy this sentence.
