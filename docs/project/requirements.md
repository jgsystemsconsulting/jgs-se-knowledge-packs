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
