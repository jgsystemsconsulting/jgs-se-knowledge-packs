# Milestones

## v1.0.0 → v1.16.3 (2026-05 → 2026-08)

Initial library build-out: 48 knowledge packs across NASA / DoD / FAA / GAO / NIST / EU / SEBoK / OMG lineages; jgs-reference-skill pipeline (book-to-skill fork); licence-vetting toolchain and CI gate; multi-host installers; catalog registry and browsable pack reference page. Baseline recorded retroactively at GSD onboarding (2026-08-14). See CHANGELOG.md for per-release detail.

## v1.17.0 (shipped 2026-08-15)

Source expansion shipped: 8 Tier-1 public-domain packs added (`nist-800-171`, `nist-800-61`, `cisa-cpg`, `doe-sem`, `mil-hdbk-338`, `mil-hdbk-516`, `nasa-ms-7009`, `doe-413-3b`); 3 candidates vetted-out (T2-01/T2-02 Excluded, T2-03 deferred-excluded → 0 Tier-2 packs); formal ruled-out register in docs/SOURCE-VETTING.md; all 11 version surfaces at 1.17.0; CHANGELOG + PACK-SPEC When-to-use/Prerequisites addendum + README table/framing; gate PASS at 54 catalog / 56 dirs.

- **Release commit:** `bcd32af` — `release(v1.17.0): 8 Tier-1 public-domain packs (54 +2 signposts)`
- **Annotated tag:** `v1.17.0` — `v1.17.0: 8 Tier-1 public-domain packs (54 +2 signposts)`
- **GitHub Release:** https://github.com/jgsystemsconsulting/jgs-se-knowledge-packs/releases/tag/v1.17.0
- **Deferred to v1.18+:** rename `doe-413-3b` → `doe-o-413-3` with catalog alias

## v1.18.0 (in execution — Phase 6 vetting complete)

Gap-driven expansion + agent enablement: 7 Tier-1 packs targeting the 1 empty + 15 thin capability clusters (research: .planning/research/capability-gap-report.md), versioned capability-pack-map contract for the se-agents generator, v1.17 carry-forwards. See REQUIREMENTS.md (VET/GP/AE/REL-1x) and ROADMAP.md phases 6-9.
