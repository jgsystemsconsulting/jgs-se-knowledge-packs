# Phase 6 Research — UNVERIFIED Resolution + Evidence Spot-Checks (v1.18.0)

**Date:** 2026-08-14
**Scope:** VET-01/VET-02 (ROADMAP Phase 6). Resolve the 5 UNVERIFIED items from
`.planning/research/capability-gap-report.md` §4, spot-check 3 ranked candidates,
confirm 2 rule-out rationales, decide GP-08 stretch.
**Method:** live HTTP checks (curl HEAD/GET with browser UA), in-PDF text-layer
inspection where fetchable, NTRS/SEI/DAU/cto.mil page reads. Link Policy: source URLs
live only in this research store, never in docs/ or packs.

---

## 1. The 5 UNVERIFIED items

### 1a. MIL-STD-40051 (Technical Data Packages / TM preparation) — Tier 1 CONFIRMED (with build-time caveat)

- **Family / current revisions:** the standard is split — MIL-STD-40051-1 (IETMs; latest
  commonly cited rev -1D, Change 1) and MIL-STD-40051-2 (page-based TMs; rev **-2C,
  15 DEC 2015** is the latest on mirrors). Base MIL-STD-40051 (1992-era) is superseded
  by the split pair. Canonical registry: DLA ASSIST-QuickSearch (free account).
- **Evidence (resolved):** everyspec mirror page for MIL-STD-40051-2C live:
  `https://everyspec.com/MIL-STD/MIL-STD-10000-and-Up/MIL-STD-40051-2C_53570/`
  with download `.../download.php?spec=MIL-STD-40051-2C.053570.pdf` →
  HTTP 200, `application/octet-stream`, 37,734,344 bytes, valid `%PDF`, **1168 page
  objects** (base std + extensive appendices). Full text decompressed and searched.
- **Licence caveat:** the cover-page Distribution Statement on this (DLA-origin,
  scanned-cover) copy is an **image**, not text — the only text-layer hits are
  boilerplate ("Distribution statement... shall follow" instruction text). DIST-A must
  be confirmed visually on the cover at build time (same pattern as Phase 3's
  MIL-HDBK builds). DLA ASSIST records for the 40051 family list Distribution A.
- **Verdict:** Tier 1 (17 U.S.C. § 105 DoD standard; DIST-A visual confirm at build).
  Enables GP pack for cluster 25 (+24). Pages: -2C main body est. ~150 (appendices are
  per-TM format plates; select). Mirror acceptable (DLA-origin document; confirm
  DIST-A in-copy).

### 1b. NASA SP-7084 — Tier 1 CONFIRMED (title corrected)

- **Title correction:** the gap report called it "Grammar/Style/Usage guide"; the actual
  title is **"Grammar, Punctuation, and Capitalization: A Handbook for Technical Writers
  and Editors"** (Mary K. McCaskill, NASA Langley).
- **Evidence (resolved):** NTRS record `https://ntrs.nasa.gov/citations/19900017394`
  (1990 edition) — HTTP 200; direct PDF
  `https://ntrs.nasa.gov/api/citations/19900017394/downloads/19900017394.pdf` —
  HTTP 200 `application/pdf`. NTRS metadata states:
  - Distribution Limits: **"Public"**
  - Copyright: **"Work of the US Gov. Public Use Permitted."**
- **Edition note:** a later revision exists (everyspec lists 03 Aug 1998 rev,
  `https://everyspec.com/NASA/NASA-SP-PUBS/NASA-SP-7084_11125/`). Prefer the 1998 rev
  if the mirror carries a text layer; otherwise NTRS 1990 is canonical + licence-clean.
- **Verdict:** Tier 1 confirmed, cleanest licence evidence of the five. ~120 pp.
  Enables GP pack for cluster 25 (+28).

### 1c. DoD VV&A RPG — Tier 1 CONFIRMED, but "consolidated PDF" premise is DEAD (rescope)

- **Finding:** `https://www.cto.mil/sea/vva_rpg/` is an **HTML index only** — no single
  downloadable PDF/ZIP of the whole guide. Content is delivered as many **separate
  per-chapter documents** (Key Concepts intro; Core Documents for Legacy and New
  Development with role-based guides for user / developer / M&S PM / V&V agent /
  accreditation agent; ~17 Special Topics; Reference Documents incl. T&E/V&V Checklist;
  tools/templates/glossary). Individual chapter links resolve to PDFs hosted via
  de-bok.org search URLs; there is also a web-based Use Case Overview at
  `https://www.cto.mil/sea/vva-rpg-uco/`.
- **Licence:** no copyright/distribution statement on the index page itself (standard
  US-gov site boilerplate only). RPG documents are OUSW(R&E) DoD works → Tier 1 by
  17 U.S.C. § 105; confirm DIST-A / authorship statement inside each chapter PDF used
  at build.
- **Verdict:** Tier 1 confirmed for a **multi-chapter build** (download selected chapter
  PDFs: core role guides + fidelity/validation/data-V&V/risk special topics + T&E/V&V
  checklist). The gap report's "~200 pp PDF build exists" is wrong — it is web-chapters.
  Third-party whole-RPG ZIPs (SE Goldmine mirrors) remain fallback-only, not canonical.
  Enables GP pack for clusters 8, 7, 16, 9 — with per-chapter provenance in PACK.yaml.

### 1d. MIL-STD-881F (Work Breakdown Structures) — Tier 1 CONFIRMED (access-path caveat)

- **Canonical:** DLA ASSIST-QuickSearch record
  `https://quicksearch.dla.mil/qsdocdetails.aspx?ident_number=36026` — live, status
  **Active**. 881F is the current revision (cited as 13 May 2022 in AF/DoD references,
  e.g. DAFI 65-508; one vendor page claims a 2025 touchless update — resolve exact
  revision date on the QuickSearch detail page at build; direct PDF download from
  QuickSearch requires the free account/session).
- **Mirrors:** everyspec has **only 881E/D**
  (`https://everyspec.com/MIL-STD/MIL-STD-0800-0899/MIL-STD-881E_56929/`), no 881F.
  A full 881F PDF circulates as a GovTribe solicitation attachment
  (`https://govtribe.com/file/government-file/b08-attachment-4-mil-std-881f-dot-pdf`,
  HTML download wrapper, not a bare PDF). MIL-HDBK-881 legacy guidance mirror already
  recorded in the gap report.
- **Licence:** DoD standard → Tier 1 via 17 U.S.C. § 105; DIST-A confirmed in-copy at
  build (881E mirror cover carries it; 881F copy from QuickSearch/GovTribe to be
  checked the same way).
- **Verdict:** Tier 1 confirmed. Build note: fetch via QuickSearch (preferred) or the
  GovTribe attachment; verify DIST-A in-copy. If only 881E is obtainable, it is still
  Tier 1 but must be labelled with its revision. Enables GP pack for clusters 17, 26.

### 1e. AFOTEC Test Design Guide — DEFERRED → recommend EXCLUDE (stale + unverifiable)

- **Finding:** DTIC is currently serving an **"Under Maintenance"** page on both the
  citation app and PDF endpoints (`apps.dtic.mil/sti/citations/ADA205489` and
  `.../sti/tr/pdf/ADA205489.pdf` return 200 `text/html` maintenance shells), so no
  in-copy licence check was possible today.
- **Substance:** the only DTIC hit (accession **AD-A205 489**) is the **1989** AFOTEC
  Test Design Guide era (AD-A numbers of that range are late-1980s). Even when DTIC
  returns, that edition is ~37 years stale against live coverage of the same ground by
  DAFMAN 63-119 (2021, confirmed live, §2c below) and the DOT&E Enterprise Guidebook
  (2022, confirmed live).
- **Verdict:** **Excluded for v1.18** — no current public edition; DTIC outage prevents
  verification; historical edition adds no cluster (9-T&E) value over confirmed live
  sources. Record in SOURCE-VETTING Excluded table with dated rationale; revisit only
  if AFOTEC publishes a modern public edition.

---

## 2. Spot-checks of already-ranked candidates (all live)

### 2a. FAA-STD-025 — CONFIRMED

- Canonical ROSAP record `https://rosap.ntl.bts.gov/view/dot/42955` — HTTP 200, and it
  exposes a **full-text PDF** (`dot_42955_DS1.pdf`, ~1.06 MB). Record is revision
  **E (FAA-STD-025e), dated 2002-08-09**; the everyspec mirror carries rev F
  (`.../download.php?spec=FAA-STD-025F.003031.pdf`).
- ROSAP record itself carries no explicit rights statement beyond the repository
  archival disclaimer; FAA = US Government work → Tier 1 (17 U.S.C. § 105); confirm
  in-PDF statement at build. Choose rev E (canonical) or F (newer, mirror) and record
  which in PACK.yaml.

### 2b. DOT&E T&E Enterprise Guidebook — CONFIRMED, with URL correction

- The afacpo mirror URL in the gap report is **double-encoded** (`%2526E`) and returns
  404. The **single-encoded** form resolves:
  `https://www.afacpo.com/AQDocs/DOT%26E%20Test%20and%20Evaluation%20Enterprise%20Guidebook_FINAL_v3%20June%202022.pdf`
  → HTTP 200 `application/pdf`. Fix wherever recorded.
- Canonical: `https://www.dote.osd.mil/Guidance/` is live and lists the **current
  edition as "Test & Evaluation Enterprise Guidebook 2022 August"** (i.e. v3 June was
  superseded by the Aug 2022 release); prior editions in the Guidance Archive.
- Additional official-adjacent mirror: DMI/IDA
  `https://www.dmi-ida.org/knowledge-base-detail/test-and-evaluation-enterprise-guidebook`
  with PDF `.../download-pdf/pdf/TE%20Enterprise%20Guidebook%208.02.pdf` (HTTP-resolvable link).
- Verdict: Tier 1 confirmed. Build against the **Aug 2022 (8.02)** edition from
  dote.osd.mil if a direct PDF is obtainable in-browser; afacpo v3-June mirror remains
  the fetchable fallback (label edition in PACK.yaml).

### 2c. DAFMAN 63-119 — CONFIRMED (title corrected)

- `https://static.e-publishing.af.mil/production/1/saf_aq/publication/dafman63-119/dafman63-119.pdf`
  — the server 403s plain HTTP clients (bot protection) but the document is fully
  retrievable via rendered fetch: **DAFMAN 63-119, 15 APRIL 2021, "Mission-Oriented
  Test Readiness Certification"** (~103 pp). Title correction: it is the MOTRC
  compliance manual, not a general "AF T&E enterprise manual".
- In-document statement (quoted from retrieved text): **"COMPLIANCE WITH THIS
  PUBLICATION IS MANDATORY ... RELEASABILITY: There are no releasability restrictions
  on this publication."** USAF publication → Tier 1 (17 U.S.C. § 105).
- Verdict: confirmed live, licence-clean. Enables clusters 9, 7, 27.

---

## 3. Rule-out rationale confirmations

### 3a. DoD DAG (retired) — CONFIRMED

- DAU AAF guidebooks page (`https://aaf.dau.edu/guidebooks/`) states verbatim:
  *"The Defense Acquisition Guidebook has been retired and replaced by a modern set of
  guidebooks aligned with our new acquisition policies."*
- AFCAPO notice "Defense Acquisition Guidebook is Being Retired" (2022-08-15,
  `https://www.afacpo.com/mpm/2022/08/15/defense-acquisition-guidebook-is-being-retired/`).
- Exclusion stands: dead canonical URLs, Wayback-only text, provenance/versioning risk.
  AAF guidebooks remain the Tier 1 substitute.

### 3b. CMU SEI — CONFIRMED excluded

- `https://www.sei.cmu.edu/legal/intellectual-property/`: SEI material is © Carnegie
  Mellon University; reproductions/derivative works **for government purposes** require
  no additional permission but must retain the copyright notice — i.e. no general
  redistribution/derivative grant. Non-government reuse is routed through the permission
  request form / **permission@sei.cmu.edu** (see standard notice on SEI tech reports,
  e.g. DTIC AD1169453: "Requests for permission should be directed to the Software
  Engineering Institute at permission@sei.cmu.edu").
- The "DISTRIBUTION STATEMENT A" that appears on some SEI reports governs DoD
  *distribution*, not CMU copyright — it does not create a Tier 1/2 grant for this
  repo. Exclusion stands absent written CMU/SEI permission.

---

## 4. GP-08 stretch decision — NASA-HDBK-2203: DEFER / DESCOPED (not viable as planned)

- `https://standards.nasa.gov/standard/NASA/NASA-HDBK-2203` is live; access is marked
  **"Internet Public"** (cleared for public accessibility). Tier basis itself is fine
  (NASA work, 17 U.S.C. § 105).
- **However:** the PDF link on the standards page is a ~5.9 KB placeholder — there is
  **no true full-handbook PDF** there. The handbook actually lives as the Confluence
  wiki `https://swehb.nasa.gov/` (Books A–E; per-SWE-requirement pages with
  Rationale/Guidance/Small Projects/Assurance sections; Book F/SPAN is NASA-only).
  Only per-page "Export to PDF" exists; no whole-document or per-chapter PDF edition.
- Consequences: the assumed "select chapters from a ~350 pp PDF" slicing model does not
  exist. A GP-08 pack would require a curated per-SWE HTML harvest + per-page PDF
  exports — a much heavier, fragmentation-prone build with per-page provenance.
- **Decision: defer GP-08** out of v1.18 (record as deferred in SOURCE-VETTING
  candidate notes). If cluster 19/13/32 fattening is still wanted cheaply, build from
  the companion PDFs instead: **NPR 7150.2** and **NASA-STD-8739.8** (both downloadable
  PDFs; 8739.8 cover carries "APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED",
  observed during this check) — rescope GP-08 to those if schedule allows.

---

## 5. Summary table

| Item | Verdict | Key evidence | Effect on v1.18 |
|---|---|---|---|
| MIL-STD-40051 (-1/-2 family) | Tier 1 confirmed (DIST-A visual check at build) | everyspec -2C PDF 200/37.7 MB/1168 pp-obj; cover statement is scanned image | GP (cluster 25) GO |
| NASA SP-7084 | Tier 1 confirmed | NTRS 19900017394 PDF 200; "Work of the US Gov. Public Use Permitted" | GP (cluster 25) GO |
| VV&A RPG | Tier 1 confirmed, **no consolidated PDF — chapter-wise build** | cto.mil HTML index; per-chapter PDFs; no whole-guide file | GP (8/7/16/9) GO, rescope |
| MIL-STD-881F | Tier 1 confirmed (QuickSearch free-account fetch or GovTribe copy) | quicksearch ident 36026 Active; everyspec has only 881E | GP (17/26) GO |
| AFOTEC Test Design Guide | **Excluded (v1.18)** | DTIC under maintenance; only hit is 1989-era ADA205489 | candidate dies |
| FAA-STD-025 (spot-check) | Live, Tier 1 | ROSAP 42955 + full-text PDF (rev E, 2002); mirror rev F | GO |
| DOT&E Guidebook (spot-check) | Live, Tier 1 | afacpo single-encoded URL 200 PDF; canonical dote lists Aug 2022 (8.02); DMI mirror | GO (use 8.02, fix URL) |
| DAFMAN 63-119 (spot-check) | Live, Tier 1 | full text retrieved; "no releasability restrictions"; 15 Apr 2021, MOTRC | GO |
| DoD DAG (rule-out) | Confirmed excluded | aaf.dau.edu "has been retired"; AFCAPO 2022-08-15 notice | stays excluded |
| CMU SEI (rule-out) | Confirmed excluded | © CMU; gov-purpose-only carve-out; permission@sei.cmu.edu | stays excluded |
| GP-08 NASA-HDBK-2203 | **Deferred/descoped** | standards.nasa.gov PDF is placeholder; content is swehb.wiki HTML only | GP-08 out of v1.18; optional NPR 7150.2 + NASA-STD-8739.8 rescope |

**Candidates that died:** AFOTEC Test Design Guide (excluded); VV&A "single PDF"
assumption (source survives, build model changes); GP-08 as specified (deferred).
