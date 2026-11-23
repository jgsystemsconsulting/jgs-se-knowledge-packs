# Requirements

## req-1
status: verified
source: 2026-11-03-fix-516c-public-chip

Public free-text surfaces that describe the mil-hdbk-516 pack state the live edition recorded in packs/mil-hdbk-516/PACK.yaml source_version, currently MIL-HDBK-516D (29 May 2026). Covered surfaces: the GitHub Pages landing page (docs/index.html catalogue chips) and website product descriptors under docs/products/website/. Excluded by design: CHANGELOG release history rows, the docs/SOURCE-VETTING.md vetting ledger, internal artifacts under docs/superpowers/, and the supersession note inside the pack's own PACK.yaml build record.

## req-2
status: verified
source: 2026-11-03-cut-unreleased-drain-release

Every public release surface states the same release version as the RELEASE-INFO.txt Version line. Covered surfaces: the current CHANGELOG numbered section heading, the RELEASE-INFO.txt Version and Tag lines, the CITATION.cff version field, the README.md version references, both plugin.json manifests, the docs/index.html version loci, the docs/packs.html REV loci, the generated docs/packs/<slug>/index.html pages, and both website product YAMLs under docs/products/website/. After a release cut, tooling/check_release.py exits 0 and the only tracked occurrences of the retired version string outside this package's own project-memory decision prose are historical CHANGELOG section headings. Generated surfaces satisfy this by regeneration, never by hand edits.

## req-3
status: verified
source: 2026-11-04-retire-scaffold-offset-vocab

Every new-pack authoring surface teaches only the canonical PACK-SPEC build method. Covered surfaces: tooling/build_pack.py PACK_YAML_TEMPLATE build.method string, build_pack.py module docstring content-generation sentence, build_pack.py printed next-step 2, and the README.md How a pack is built pipeline prose. The scaffold template stamps the exact canonical method string "synthesized reference notes from the pinned source, chapter freeze from the contents list" verbatim. No covered surface contains offset-mapped, chapter-offset, or chapter offsets after the change. Live packs/*/PACK.yaml method fields, already normalized by P7, stay untouched.

## req-4
status: accepted
source: 2026-11-22-se-sector-pack-reconciliation

The SE tree does not ship easa-rules, faa-8110-49, fda-med-device, nhtsa-vehicle, nrc-nuclear, automotive-signpost, avionics-signpost, or functional-safety-signpost. Absence covers pack directories, catalog.json live rows, both plugin skill lists, packs/se/SKILL.md routes, NOTICE blocks, classification assignments, note overrides, source-watchlist rows, README.md and SKILLS.md rows, and generated landing pages. Sector repos are not edited to receive SE diffs.

## req-5
status: accepted
source: 2026-11-22-se-sector-pack-reconciliation

The cut ships SE release 1.24.5. RELEASE-INFO.txt, plugin.json version fields, both website product YAMLs, current CHANGELOG heading, docs/index.html version loci, generated pack-page REV stamps, and README.md version loci (badge and two body sentences) all state 1.24.5. tooling/check_release.py exits 0 on release commit. An annotated tag v1.24.5 created locally on commit. Nothing pushed.

## req-6
status: accepted
source: 2026-11-22-se-sector-pack-reconciliation

SE carries docs/FLEET-CONVENTIONS.md and docs/CROSS-PACK-BOUNDARIES.md, and checker promoted: jgs-reference-skill/tools/check_pack_slug_dupes.py exists, UK copy keeps canonical-path note, and aviation, med-device, and automotive carry pointer sentence. boundary note names sector owner each eight removed slugs and states UK defence publication one content owner. After removals are on disk, fleet slug checker exits 0 sector repo and prints RESULT: CLEAN. checker not wired into any CI gate.
