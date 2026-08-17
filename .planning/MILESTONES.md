# Milestones

## v1.0.0 → v1.16.3 (2026-05 → 2026-08)

Initial library build-out: 48 knowledge packs across NASA / DoD / FAA / GAO / NIST / EU / SEBoK / OMG lineages; jgs-reference-skill pipeline (book-to-skill fork); licence-vetting toolchain and CI gate; multi-host installers; catalog registry and browsable pack reference page. Baseline recorded retroactively at GSD onboarding (2026-08-14). See CHANGELOG.md for per-release detail.

## v1.17.0 (shipped 2026-08-15)

Source expansion shipped: 8 Tier-1 public-domain packs added (`nist-800-171`, `nist-800-61`, `cisa-cpg`, `doe-sem`, `mil-hdbk-338`, `mil-hdbk-516`, `nasa-ms-7009`, `doe-413-3b`); 3 candidates vetted-out (T2-01/T2-02 Excluded, T2-03 deferred-excluded → 0 Tier-2 packs); formal ruled-out register in docs/SOURCE-VETTING.md; all 11 version surfaces at 1.17.0; CHANGELOG + PACK-SPEC When-to-use/Prerequisites addendum + README table/framing; gate PASS at 54 catalog / 56 dirs.

- **Release commit:** `bcd32af` — `release(v1.17.0): 8 Tier-1 public-domain packs (54 +2 signposts)`
- **Annotated tag:** `v1.17.0` — `v1.17.0: 8 Tier-1 public-domain packs (54 +2 signposts)`
- **GitHub Release:** https://github.com/jgsystemsconsulting/jgs-se-knowledge-packs/releases/tag/v1.17.0
- **Deferred to v1.18+:** rename `doe-413-3b` → `doe-o-413-3` with catalog alias

## v1.18.0 (shipped 2026-08-17)

Gap-driven expansion + agent enablement shipped: 7 Tier-1 packs (`dote-te-guidebook`, `faa-std-025`, `federal-bca`, `dafman-63-119`, `mil-std-881f`, `mil-std-40051`, `dod-vva-rpg`); `doe-413-3b` renamed to `doe-o-413-3` with catalog alias retained; capability-pack-map v2 (schema_version 2, 32 clusters, 628 chapter entries, map_version 1.18.0) + CONTRACT + gate; all 11 version surfaces at 1.18.0; IN-01 cluster-name + OUSD typo + v1.17.0 index.html wording fix; gate PASS at 61 catalog / 63 dirs.

- **Release commit:** `d19be1a` — `release(v1.18.0): 7 gap-driven Tier-1 packs (61 +2 signposts), capability map v2`
- **Annotated tag:** `v1.18.0` — `v1.18.0: 7 gap-driven Tier-1 packs (61 +2 signposts), capability map v2`
- **GitHub Release:** https://github.com/jgsystemsconsulting/jgs-se-knowledge-packs/releases/tag/v1.18.0
- **Deferred to v1.19:** FUT-04 Army CBA retry; FUT-05 (bdc6c9e); 7-CODE-REVIEW IN-02 minimal committed overlap checker; thin clusters 3/5/15; optional PACK.yaml notes + ROSAP Rev E retry

## v1.19.0 (in planning — scoped 2026-08-17)

Agent IO Depth (SEED-001): fatten the 17 thin-primary ISECF competencies so jgs-se-agents can execute IOs. Vet FUT-04 + DoDM 5000.102 / NASA-STD-8719.14 / GPS ICD / SP-7084 / AAF-before-use; build what clears; remap A-94/VV&A into Decision Analysis; regenerate map with a competency-primary floor; hygiene + map-gate wiring; tag v1.19.0. See REQUIREMENTS.md (VET-19 / IO / MAP-19 / HYG / REL-19) and ROADMAP.md phases 10–13. Out of scope: per-role packs, se-agents consumer refresh, FUT-05 generator, committed overlap checker.
