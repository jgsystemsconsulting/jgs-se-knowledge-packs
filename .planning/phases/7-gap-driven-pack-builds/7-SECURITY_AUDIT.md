---
phase: 7-gap-driven-pack-builds
audit: security
scope: "7 GP packs, commits bab559d..e00ac7d (15 commits)"
asvs_level: 2
block_on: high
audited: 2026-08-14
verdict: SECURED_WITH_NOTES
threats_open: 0
---

# Phase 7 Security Audit — Gap-Driven Pack Builds (7 GP packs)

**Verdict:** SECURED_WITH_NOTES

Scope: the 7 new packs (`faa-std-025`, `dote-te-guidebook`, `dafman-63-119`,
`federal-bca`, `mil-std-881f`, `mil-std-40051`, `dod-vva-rpg`) plus the
registration sweep, across the full commit range `bab559d~1..e00ac7d`
(15 commits: 7 feat + 1 fix + 1 registration + 6 docs). All threats in the
three plan threat registers (T-7A-*, T-7B-*, T-7C-*) are `mitigate`
disposition; no accept/transfer entries to check against SECURITY.md.

Every mitigation was re-verified against the working tree AND the local
gitignored `sources/` build artifacts — SUMMARY claims were not accepted as
evidence. All gates (validate, check_overlap, scan_generated_skill,
check_release) were re-run fresh by the auditor on 2026-08-14.

## Threat Verification (Plan 7-01, Wave A)

| Threat | Category | Sev | Disposition | Evidence (freshly verified) | Status |
|--------|----------|-----|-------------|------------------------------|--------|
| T-7A-01 | Tampering (evidence integrity) | high | mitigate | federal-bca PACK.yaml:19-25 records P7-PRE-2 dual gate. A-94 PASS verified against `sources/federal-bca/work_main/book_skill_work/full_text.txt`: identity confirmed ("CIRCULAR NO. A-94", "Revised, Nov. 9, 2023"), zero copyright notices (8 literal "(c)" hits are list-item markers). Army FAIL claim is truthful: `sources/federal-bca/US_Army_Cost_Benefit_Analysis.pdf` is a 489-byte "Access Denied" HTML stub. Halt-and-rescope executed BEFORE generation (title/version/catalog all A-94-only). | CLOSED (note 3) |
| T-7A-02 | Tampering (fetched variants) | medium | mitigate | dafman releasability line found verbatim in obtained text: "RELEASABILITY: There are no releasability restrictions on this publication"; title page + 103pp recorded; 1995 wrong edition rejected. dote DIST-A verbatim in-PDF (2 occurrences). faa P7-PRE-5 negative scan verified: 0 rights/copyright lines in extraction. | CLOSED |
| T-7A-03 | Repudiation (provenance) | medium | mitigate | All 7 PACK.yaml `source_version` carry edition + mirror/source + retrieval date; source_pages match metadata basis (40051=151 selected; vva=283 summed). | CLOSED |
| T-7A-04 | Information disclosure (sources/) | high | mitigate | `git log --name-only bab559d~1..e00ac7d` — zero `sources/`, `full_text.txt`, `*.pdf`, `selected_body*`, `chapter_fulltexts` paths in any commit. `.gitignore:17` covers `sources/`. Working tree clean. | CLOSED |
| T-7A-05 | IP theft (verbatim) | high | mitigate | check_overlap freshly re-run: exit 0 on faa/dote/dafman + federal-bca vs A-94 full_text. Overlap fix commit `2e7bc2e` (authority-clause paraphrase) is in range and narrowed to 1 file. | CLOSED |

## Threat Verification (Plan 7-02, Wave B)

| Threat | Category | Sev | Disposition | Evidence | Status |
|--------|----------|-----|-------------|----------|--------|
| T-7B-01 | Tampering (DIST-A evidence) | high | mitigate | 40051: pixmap visual cover check recorded in PACK.yaml:24-28; DIST-A line confirmed in `selected_body.txt:19` ("distr bution" OCR typo, immaterial). 881F: cover genuinely lacks a printed DIST block; PACK.yaml:25-30 records the honest basis — ASSIST QuickSearch Dist Stmt column A for Rev F + Active status — corroborated by the provenance header in the build full_text. Deviation self-flagged in 7-02-SUMMARY. | CLOSED (note 1) |
| T-7B-02 | Tampering (881E/F substitution) | medium | mitigate | `source_version: "MIL-STD-881F, 13 May 2022"`; provenance header records "supersedes MIL-STD-881E"; edition cross-checked to QuickSearch — not the 881E fallback. | CLOSED |
| T-7B-03 | Spoofing (extraction quality) | high | mitigate | `selected_stats.txt` = 443929 chars / 151 pages = 2939.9 cpp >= 300; plates skipped; OCR-not-needed recorded; whole-file number recorded as informational only. | CLOSED |
| T-7B-04 | Repudiation (provenance) | medium | mitigate | Fetch path (everyspec 37.7MB mirror) + 151-page selection basis recorded in PACK.yaml:20-34. | CLOSED |
| T-7B-05 | Information disclosure | high | mitigate | Same range-wide leak check as T-7A-04 — clean. | CLOSED |

## Threat Verification (Plan 7-03, Wave C)

| Threat | Category | Sev | Disposition | Evidence | Status |
|--------|----------|-----|-------------|----------|--------|
| T-7C-01 | Tampering (per-chapter evidence) | high | mitigate | 10/10 chapter fulltexts under `sources/dod-vva-rpg/chapter_fulltexts/` carry build-time provenance headers recording DEBoK Copyright Details = Public Domain + OSD/OUSD R&E authorship + P7-PRE-4 PASS per chapter; dropped chapter (T&E/V&V Checklist) recorded as selection, not licence. | CLOSED (note 2) |
| T-7C-02 | Repudiation (per-chapter provenance) | medium | mitigate | PACK.yaml:24-36 lists all 10 chapters with titles + retrieved 2026-08-16; no URLs (bare domain "de-bok.org" mention only — not a link). | CLOSED |
| T-7C-03 | Tampering (registration counts) | high | mitigate | Freshly verified: check_release.py PASS; catalog 61; cursor 62; packs/ 63 dirs; SKILLS.md "61 packs (+2 signposts)"; README packs-61; 7 NOTICE `[pack: <slug>]` blocks present; slug-set complete. | CLOSED |
| T-7C-04 | Information disclosure | high | mitigate | Range-wide leak check clean; working tree clean. | CLOSED |
| T-7C-05 | IP theft (verbatim) | high | mitigate | check_overlap freshly re-run against all 10 chapter fulltexts: 0 failures. | CLOSED |

## Coordinator-Declared Audit Items (P7-PRE / T-6-03 enforcement)

1. **Build-time licence obligations — all 7 landed.** 881F: ASSIST Dist Stmt A
   basis recorded honestly (PACK.yaml:25-30, incl. "cover has no separate
   printed Distribution Statement block"). 40051: pixmap visual check recorded
   (PACK.yaml:24-28) + DIST-A in selected body. VV&A: DEBoK Copyright=Public
   Domain per-chapter in all 10 provenance headers. federal-bca: A-94 in-source
   clean (verified) + Army exclusion recorded truthfully (403 stub on disk).
   dafman: releasability line verified verbatim in obtained text. dote: DIST-A
   in PDF (verified, 2 hits). faa: Rev F everyspec mirror + honest P7-PRE-5
   negative finding.
2. **Link policy — 0 source URLs.** `git grep https\?://` over all 7 packs at
   `e00ac7d`: zero hits. Registration-commit added lines contain only
   self-referential github.com pack links, the shields.io badge, and the
   json-schema.org `$schema` id — none are source-material links
   (docs/LICENSING.md policy satisfied).
3. **No verbatim reproduction.** check_overlap exit 0 on all 7 packs
   (10 sources for vva), freshly re-run. Independent spot-grep: distinctive
   10-word runs from dafman, A-94, and 881F sources appear in no pack file.
4. **Prompt injection.** `scan_generated_skill.py` re-run on all 7 packs:
   "no known injection or authority patterns found", exit 0 each. No EARS-style
   advisories even surfaced on re-run.
5. **Secrets/PII — none.** Secret-pattern grep over the 7 packs: only
   "ri**sk-**" substring false positives (risk-informed/managed/assessment).
   Email/SSN grep: zero hits. Registration surfaces clean of
   atob/otmmapi/JSESSION/Authorization patterns.
6. **sources/ never committed.** Full-range `git log --name-only` audit:
   zero leaks; only packs/, .planning/, and the 6 registration surfaces
   touched.

## Notes (non-blocking)

1. **881F/VV&A DIST-A evidence is metadata-based, not in-PDF text.** The
   fetched 881F cover and RPG chapter covers carry no printed DIST-A prose,
   so the mitigation landed as ASSIST QuickSearch Dist Stmt (881F) and DEBoK
   Copyright=PD + OSD authorship (VV&A). Both substitutions are honestly
   recorded in PACK.yaml and self-flagged in the plan SUMMARYs with the same
   metadata-evidence pattern. This is a defensible T-6-03 disposition, not a
   gap — but it is a weaker evidence class than an in-source statement and
   should ride with the packs if the licence basis is ever challenged.
2. **`sources/dod-vva-rpg/debok_meta_summary.json` is empty** ({} for every
   chapter — failed OTMM metadata capture). The per-chapter DEBoK PD evidence
   lives only in the executor-written provenance headers, not in persisted
   raw third-party metadata. Local-only, gitignored either way; evidence
   chain rests on build-time records.
3. **federal-bca PACK.yaml wording**: "no third-party copyright / (c) /
   all-rights-reserved notices" — the A-94 extraction does contain 8 literal
   "(c)" strings, all enumeration list markers. Substance verified (zero
   actual copyright notices); wording is imprecise.

## Unregistered Flags (from SUMMARY deviations/patterns)

- `r.jina.ai` reader-proxy fetch (dafman) and DEBoK OTMM guest session (vva)
  are new fetch patterns introduced this phase. Both map to the existing
  fetched-variant threats (T-7A-02 / T-7C-01) and were handled with
  verification gates. Session artifacts (`cookies.txt`, `debok.js`) exist
  under gitignored `sources/` and are verified uncommitted. No action.

**threats_open:** 0 (15/15 CLOSED; 3 non-blocking notes)
