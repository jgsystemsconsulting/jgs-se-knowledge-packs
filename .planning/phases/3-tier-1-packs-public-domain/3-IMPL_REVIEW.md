# Phase 3 Implementation Review (diff-scope)

**Verdict:** PASS_WITH_NOTES

**Reviewed:** 2026-08-14
**Scope:** Implementation commits c6820a7, 5e4663d, 62bd340, 301a47d, 4dfba84, 7ac09ad, 7767a7b, 570adf3, 863bfeb against plans 3-01/3-02/3-03.
**Method:** commit-by-commit file-list audit, tooling re-run, structural spot-check of 3 packs (nist-800-171, cisa-cpg, doe-413-3b) plus PACK.yaml/SKILL.md checks across all 8.

## Verified

- All 8 packs pass `tooling/validate_pack.py` (re-run in review); all contain LICENSE, PACK.yaml, SKILL.md, chapters/, glossary.md, patterns.md, cheatsheet.md.
- SKILL.md contract (check_release rr-s-13): every pack has `## When to use` immediately followed by `**Prerequisites:**` (all at lines 11/14).
- Chapter counts within plan ranges: nist-800-171 8 (6-8), nist-800-61 6 (5-7), cisa-cpg 5 (4-6), doe-sem 7 (6-8), mil-hdbk-338 9 (8-10), mil-hdbk-516 8 (6-8), nasa-ms-7009 7 (6-8), doe-413-3b 6 (5-7).
- Commit hygiene: each pack landed in exactly one commit touching only `packs/<slug>/`; zero `sources/` or `full_text.txt` paths in any commit; no TODO stubs; no source URLs in pack files.
- Chapter Index links resolve (programmatically checked for the 3 spot-check packs; all 8 validated by tooling).
- PACK.yaml provenance real: license_tier 1, statute-bearing licence strings (incl. P3-PRE-1 statute string for cisa-cpg; Distribution Statement A variant in mil-hdbk PACK.yaml/LICENSE per plan), source_pages from extraction metadata (nasa-ms-7009 = 88+175=263 summed two-source build; cisa-cpg = 36+2=38), built_on, notes with scan/overlap dispositions.
- Registration (863bfeb): catalog.json 54 packs / 50 tier-1 / `updated` bumped; 8 backtick-slug rows in SKILLS.md with "54 packs (+2 signposts)" header; 8 `[pack: <slug>]` NOTICE blocks; `tooling/check_release.py` re-run in review: **PASS**.
- Worktree clean of Phase 3 paths (only unrelated master-flow state + untracked docs/ files from other activity).

## Findings

**MAJOR-1 — doe-413-3b built from a different document than planned.** Commit 570adf3 / `packs/doe-413-3b/PACK.yaml:4`: pack content is DOE O 413.3C (approved 2026-08-05), not the O 413.3B Chg 7 PDF named in 3-03-PLAN Task 2 and requirement T1-06. The substitution is well documented (PACK.yaml notes, 3-03-SUMMARY lines 46/122/162, catalog source_version) and the successor order supersedes Chg 7, but the slug `doe-413-3b` and the vague title "…(DOE O 413.3 capital asset order)" no longer match the actual source version, and no plan amendment was recorded — only a SUMMARY note. Recommend a roadmap/plan errata line or slug/title alignment in a later phase; not blocking given full provenance disclosure.

**MINOR-1 — cisa-cpg second source differs from plan.** `packs/cisa-cpg/PACK.yaml:22-26`: plan required "main report and controls-list PDF"; no controls-list PDF existed for CPG 2.0 at build, so the 2-page slick sheet was used instead. Both sources were extracted and overlap-checked; deviation documented in PACK.yaml and SKILL.md Scope & Limits. Acceptable adaptation.

**MINOR-2 — registration commit scope wider than plan file list.** 863bfeb also touched README.md (pack badge 46→54) and docs/index.html (publisher counts +2 DOE, +1 CISA, +2 DoD, +2 NIST, +1 NASA). Plan 3-03 Task 3 listed only catalog.json/SKILLS.md/docs/packs.html/NOTICE. Changes are correct, consistency-motivated (MJ-01), and disclosed in the commit body; scope drift is benign but undeclared against the plan's `files_modified`.

**MINOR-3 — overlap/vet gates not independently re-runnable.** check_overlap.py and vet_source.py depend on gitignored `sources/<slug>/work_dir*.txt` work roots under `$REF`; review confirms the gates ran (dispositions recorded in every PACK.yaml) but the review itself could not re-execute them. Inherent to the no-source-commit policy; no action needed.

No BLOCKER findings. No regressions detected: pre-existing packs, tooling/, and installers untouched by the nine implementation commits; check_release PASS on HEAD.
