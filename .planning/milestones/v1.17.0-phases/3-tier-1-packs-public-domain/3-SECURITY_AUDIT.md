---
phase: 3-tier-1-packs-public-domain
audit: security
date: 2026-08-15
auditor: security-audit subagent (GSD)
asvs_level: 2 (no explicit config; verification performed at L2-L3 — tools re-run against live sources)
block_on: high (default; no explicit config found)
commits_in_scope:
  - c6820a7 (nist-800-171)
  - 5e4663d (nist-800-61)
  - 62bd340 (cisa-cpg)
  - 301a47d (doe-sem)
  - 4dfba84 (mil-hdbk-338)
  - 7ac09ad (mil-hdbk-516)
  - 7767a7b (nasa-ms-7009)
  - 570adf3 (doe-413-3b)
  - 863bfeb (registration)
---

# Phase 3 Security Audit — 8 Tier-1 Public-Domain Packs

**Verdict:** SECURED

Every declared mitigation was re-verified against the implemented artifacts (not
SUMMARY claims): check_overlap and scan_generated_skill were re-run against the
source extracts still present under `sources/`, the in-copy DIST-A and DOE
copyright checks were re-executed via grep on the extracted full text, and all 9
commits plus the entire git history were checked for `sources/` leakage.

## Threat Verification

Threat register consolidated from `<threat_model>` blocks of 3-01-PLAN.md,
3-02-PLAN.md, 3-03-PLAN.md (12 threats total).

| Threat ID | Category | Severity | Disposition | Evidence | Status |
|-----------|----------|----------|-------------|----------|--------|
| T-3A-01 | Repudiation (PACK.yaml provenance) | medium | mitigate | All 8 PACK.yaml: source_pages/chapters/built_on filled, 0 TODOs; `validate_pack.py` re-run PASS ×8 | CLOSED |
| T-3A-02 | Licence-tier elevation (cisa-cpg) | high | mitigate | packs/cisa-cpg/PACK.yaml:5 licence is exactly `Public Domain (US Government work, 17 U.S.C. § 105)`, license_tier 1; notes record P3-PRE-1 handling | CLOSED |
| T-3A-03 | Information disclosure (sources/, full_text) | high | mitigate | .gitignore:17 `sources/`; `git show --name-only` on all 9 commits = 0 leaks; `git log --all -- sources/` empty (never committed in any history) | CLOSED |
| T-3A-04 | IP theft (verbatim copying) | high | mitigate | check_overlap re-run vs sources/nist-800-171 extract: exit 0 | CLOSED |
| T-3B-01 | Tampering (mirror source substitution) | high | mitigate | DIST-A re-verified in extracted text: `DISTRIBUTION STATEMENT A. Approved for public release...` present in mil-hdbk-338 and mil-hdbk-516 full_text; mirrors (nde-ed.org / everyspec.com) recorded in PACK.yaml notes | CLOSED |
| T-3B-02 | Information disclosure (sources/) | high | mitigate | Same evidence as T-3A-03 (commits 4dfba84, 7ac09ad clean) | CLOSED |
| T-3B-03 | DoS (extraction abort on scanned PDFs) | medium | mitigate | Vector absent: both PDFs had text layers; chars/page floor evidence recorded (338=2407.1, 516=2954.2, floor 300); OCR contingency documented in PACK.yaml notes ("OCR not required") | CLOSED |
| T-3B-04 | IP theft (verbatim copying) | high | mitigate | check_overlap re-run vs both DoD extracts: exit 0 ×2 | CLOSED |
| T-3C-01 | Tampering (nasa dual-source provenance) | medium | mitigate | packs/nasa-ms-7009/PACK.yaml notes record two-source build (STD 88pp + HDBK 175pp); source_pages=263 summed | CLOSED |
| T-3C-02 | Repudiation (registration sweep) | medium | mitigate | `check_release.py` re-run: `RELEASE CHECK: PASS`; catalog.json 54 packs, 8 new tier-1 live entries; NOTICE 8 `[pack: ...]` blocks; SKILLS.md 8 backtick-slug rows | CLOSED |
| T-3C-03 | Information disclosure (sources/) | high | mitigate | Same evidence as T-3A-03 (commits 7767a7b, 570adf3, 863bfeb clean) | CLOSED |
| T-3C-04 | IP theft (verbatim, dual source) | high | mitigate | check_overlap re-run vs BOTH nasa extracts (work_std, work_hdbk): exit 0 ×2 | CLOSED |

## Task-Declared Threat Areas (mapped to register)

| Area | Verification performed | Result |
|------|----------------------|--------|
| Licence compliance: all 8 US-gov public domain | All 8 PACK.yaml carry statute string, license_tier 1; all 8 LICENSE files carry `17 U.S.C. § 105` text; DoD packs carry DIST-A variant | PASS (T-3A-02 family) |
| cisa-cpg statute string | Exact P3-PRE-1 string at PACK.yaml:5; corroborated in notes | PASS |
| DoD DIST-A | DIST-A text re-grepped present in both extracted source texts | PASS (T-3B-01) |
| No third-party copyright content (DOE in-PDF notices) | Copyright sweep re-run on ALL 10 source extracts (incl. both DOE, both CISA, both NASA, both NIST): 0 hits for `copyright ©`, `© <year>`, `all rights reserved` | PASS |
| Link policy: zero source URLs | URL grep across all 8 pack trees: 0 matches; source-domain grep (energy.gov, cisa.gov, nvlpubs, standards.nasa.gov, everyspec, nde-ed, dla.mil) across README/docs/catalog/NOTICE/SKILLS.md: only pre-existing NOTICE:320 everyspec caveat (see Notes) | PASS |
| No verbatim source reproduction | check_overlap re-run ×10 (8 packs; dual sources for cisa-cpg and nasa-ms-7009): all exit 0, `No verbatim run >= 12 words` | PASS (T-3A-04, T-3B-04, T-3C-04) |
| Prompt injection in pack content | scan_generated_skill.py re-run on all 8: `passed: no known injection or authority patterns found` ×8; manual marker grep (`<system`, `ignore previous`, `disregard`, `system override`, etc.) across all 8 packs: 0 hits; no advisories surfaced, so no EARS-style false positives to disposition | PASS |
| Secrets / PII | Key-pattern grep (AKIA, sk-, ghp_, xox, private keys, webmail addresses): 0 matches; `password`/`api key` hits in nist-800-171 are access-control domain content (the source standard's subject matter), not credentials | PASS |
| sources/ never committed | 9/9 commits clean; full-repo history `git log --all -- sources/` empty | PASS (T-3A-03, T-3B-02, T-3C-03) |

## Unregistered Flags / Notes (informational, non-blocking)

1. **NOTICE:320 everyspec.com mention** — text inside the pre-existing
   `faa-system-safety` attribution block warning AGAINST third-party reprints.
   Not a hyperlink, not a source URL for any of the 8 Phase 3 packs, predates
   this phase's content. No action.
2. **doe-413-3b source substitution (O 413.3C vs named O 413.3B Chg 7)** —
   documented deviation; successor order is US-gov PD, provenance recorded in
   PACK.yaml notes, LICENSE, and SKILL Scope. Licence compliance unaffected.
   Maps to the provenance threat family (T-3C-01/T-3A-01); not unregistered
   attack surface.
3. **Third-party mirrors used for DoD PDFs** (nde-ed.org, everyspec.com) — this
   risk IS in the register (T-3B-01) and was mitigated by in-copy DIST-A
   verification, independently re-confirmed by this audit.

## Methodology Notes

- No `asvs_level`/`block_on` config found in `.planning/`; audit performed at
  L2-L3 depth (tool re-runs against live source extracts, full-history leak
  checks) which exceeds L1 grep-presence checks.
- SUMMARY files contain no `## Threat Flags` sections; the observations above
  were surfaced by the auditor and all map to existing register entries or
  non-threats.
- Implementation files were not modified; the only write is this audit report.

**threats_open:** 0

**Verdict:** SECURED
