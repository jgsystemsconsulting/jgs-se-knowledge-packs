# Phase 2 Research: Source Vetting + Ruled-Out Register

Date: 2026-08-14. Method: WebSearch/WebFetch verification of each candidate's
authoritative URL, licence statement, and distribution statement. Tier definitions
per docs/SOURCE-VETTING.md ("Free to download" is not "free to redistribute").

**Headline findings (deviations from the expected tier plan):**

- **IEEE 15288.2-2014 (expected Tier 2): actually EXCLUDED-leaning.** The IEEE page
  offers *purchase/subscription only*; it is **not** in the IEEE GET program, and GET
  terms state IEEE "is, and shall remain the sole copyright holder" and downloads are
  "explicitly labeled as not in the 'Public Domain'". No redistribution/derivative
  grant exists. T2-01 cannot proceed as planned.
- **ECSS-E-ST-10C Rev.1 (expected Tier 2): actually EXCLUDED-leaning.** ECSS licence:
  ESA holds copyright; "No ECSS document may be reproduced in any form without the
  explicit consent of ESA". A pack is reproduction + derivative work. T2-02 cannot
  proceed without ESA written consent.
- **Def Stan 00-051: UNVERIFIED + probable subject mismatch.** Def Stan 00-051 is
  *Environmental Management Requirements for Defence Systems*, not safety (that is
  Def Stan 00-056). Redistribution terms are inside a registration-gated portal.
- All 8 Tier-1 candidates verified as US-government works (Tier 1).

---

## Tier-1 candidates

### 1. NIST SP 800-171 Rev. 3 — **Tier 1 (VERIFIED)**
- Source: NIST CSRC, "Protecting Controlled Unclassified Information in Nonfederal
  Systems and Organizations", Rev. 3, final 2024-05-14 (authors Ross, Pillitteri).
- URL resolves: https://csrc.nist.gov/pubs/sp/800/171/r3/final (confirmed).
- Licence evidence: NIST publication page links only a copyright-policy footer; NIST
  publications by NIST staff are works of the US Government, not subject to US
  copyright (17 U.S.C. § 105) — the basis on which prior NIST-derived packs in this
  repo were tiered. Full PDF at nvlpubs.nist.gov (DOI: 10.6028/NIST.SP.800-171r3).
- Page count: ~111 pp (PDF; approximate — confirm at build time).
- Unique topic: CUI protection / 110-security-requirement baseline; complements
  existing NIST packs (none cover 800-171).

### 2. NIST SP 800-61 Rev. 3 — **Tier 1 (VERIFIED)**
- Source: NIST, "Incident Response Recommendations and Considerations for
  Cybersecurity Risk Management", Rev. 3, final 2025-04-03 (Nelson, Rekhi, Souppaya,
  Scarfone). Supersedes Rev. 2 (2012).
- URL resolves: https://csrc.nist.gov/pubs/sp/800/61/r3/final (confirmed).
- Licence evidence: same NIST US-Government-work basis as above; PDF at nvlpubs
  (DOI: 10.6028/NIST.SP.800-61r3).
- Page count: not stated on page (~68 pp; confirm at build time).
- Unique topic: incident response / IR lifecycle; no existing pack covers it.

### 3. MIL-HDBK-338B (1998) — **Tier 1 (VERIFIED)**
- Source: DoD "Electronic Reliability Design Handbook", 1 Oct 1998 (Rome Laboratory
  support); Notice 2 (2007-06-29) keeps it active.
- Authoritative record: DLA ASSIST QuickSearch ident_number=54022
  (https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=54022). Full PDF
  mirrored at https://www.nde-ed.org/NDEEngineering/SafeDesign/MILHDBK338B.pdf
  (resolves).
- Licence evidence: Distribution Statement A — "Approved for public release;
  distribution is unlimited" (DoD handbook, US Gov work per 17 U.S.C. § 105).
  Confirm the statement is on the PDF's cover/i page at build time (DLA page itself
  is dynamic; search snippet confirmed the statement).
- Page count: ~716 pp (large; pack must select chapters).
- Unique topic: electronic reliability design (reliability prediction/derating/MTBF);
  not covered by existing packs.

### 4. MIL-HDBK-516C (2014) — **Tier 1 (VERIFIED)**
- Source: DoD "Airworthiness Certification Criteria", 516C, 2014 (Rev C, 12 Dec 2014
  w/ Change 1 2016 per DLA record).
- Authoritative source: DLA ASSIST/QuickSearch (search returned the actual DLA-hosted
  PDF, https://quicksearch.dla.mil/WMX/Default.aspx?token=346737) — the PDF text
  begins "DISTRIBUTION STATEMENT A. Approved for public release; distribution …".
- Licence evidence: Distribution Statement A + US Gov work. Quote confirmed from the
  DLA-hosted document itself.
- Page count: ~320 pp (approx; confirm at build).
- Unique topic: airworthiness certification criteria; not covered elsewhere.

### 5. NASA-STD-7009B + NASA-HDBK-7009 — **Tier 1 (VERIFIED)**
- Source: NASA "Standard for Models and Simulations", NASA-STD-7009B approved
  2024-03-05 (43 mandatory requirements), plus its implementation handbook
  NASA-HDBK-7009 (current revision B, final PDF 2026-02-03 at standards.nasa.gov).
- URLs resolve: https://standards.nasa.gov/standard/NASA/NASA-STD-7009 and
  https://standards.nasa.gov/standard/NASA/NASA-HDBK-7009 (confirmed via search of
  the official pages; HDBK-7009B PDF at
  /system/files/tmp/NASA-HDBK-7009B_Final 02-03-2026.pdf).
- Licence evidence: NASA-authored standard/handbook = US Government work (17 U.S.C.
  § 105); NASA standards are published for unrestricted use. Note: NASA documents
  state "not subject to copyright in the United States"; attribution is courtesy.
- Page count: STD-7009B ~30 pp (approx); HDBK-7009B substantial (100+ pp). Confirm
  at build.
- Unique topic: M&S credibility/risk assessment standard; unique in library.

### 6. DOE O 413.3B (Chg 7, LtdChg 2023-06-21) — **Tier 1 (VERIFIED)**
- Source: DOE Order "Program and Project Management for the Acquisition of Capital
  Assets", O 413.3B, Change 7 (limited change), approved 2023-06-21; raised the
  full-order threshold from $50M to $300M.
- Authoritative source: DOE Directives Library,
  https://www.energy.gov/management/directives-library (lists "DOE O 413.3B Chg 7
  (LtdChg), 6/23/2023" with PDF). Note: the old deep link
  /directives/doe-o-4133b-... returns 404 — use the Directives Library entry.
- Licence evidence: US DOE government work (17 U.S.C. § 105). DOE directives carry no
  copyright restriction; confirm no third-party-copyright notices inside the PDF at
  build time.
- Page count: ~100+ pp (approx; Chg 7 is a limited change to the base order — pack
  should target the consolidated Chg 7 PDF).
- Unique topic: capital-asset project management / Critical Decision milestones;
  unique in library.

### 7. CISA CPG 2.0 — **Tier 1 (VERIFIED)**
- Source: CISA "Cross-Sector Cybersecurity Performance Goals 2.0" (aligned to NIST
  CSF 2.0, incl. GOVERN function; consolidated IT/OT goals; ~2024-25 refresh).
- URLs resolve: https://www.cisa.gov/cybersecurity-performance-goals-2-0-cpg-2-0 and
  the report page under /cross-sector-cybersecurity-performance-goals; controls-list
  PDF at cisa.gov/sites/default/files/publications/ (confirmed pattern).
- Licence evidence: CISA is a US federal agency; works authored by federal employees
  are public domain (17 U.S.C. § 105). No CC/public-domain statement appears on the
  landing page itself — the PDFs are US-Gov authored (verify the PDF's own
  title/disclaimer page at build time; watch for embedded third-party logos/content).
- Page count: main report ~40 pp (approx).
- Unique topic: baseline cybersecurity performance goals for critical infrastructure;
  complements NIST 800-171 pack.

### 8. DOE SEM (SEM3) — **Tier 1 (VERIFIED URL; licence per US-gov basis)**
- Source: US DOE "Systems Engineering Methodology", SEM version 3 (SEM3).
- URL resolves: https://www.energy.gov/sites/prod/files/cioprod/documents/SEM3_1231.pdf
  — WebFetch received the PDF (application/pdf), i.e. the link is live and public.
- Licence evidence: DOE-authored document → US Government work (17 U.S.C. § 105).
  Confirm no third-party copyright notice inside the PDF at build time (PDF content
  could not be read by the fetch tool).
- Page count: unknown (PDF not machine-read) — confirm at build; treat as
  substantial.
- Unique topic: DOE's SEM lifecycle methodology; the only end-to-end "methodology"
  (vs standard) in the new batch.

---

## Tier-2 candidates

### 9. IEEE 15288.2-2014 — **EXCLUDED-leaning (was expected Tier 2) — free-download premise NOT confirmed**
- Source: IEEE Std 15288.2-2014, "Technical Reviews and Audits on Defense Programs".
- URL resolves: https://standards.ieee.org/ieee/15288.2/5705/ — but the only access
  options shown are **Purchase / Subscription**; no free PDF.
- Licence evidence: page footer "© Copyright 2026 IEEE – All rights reserved."
  The IEEE GET program (which grants some standards at no charge) does **not** list
  15288.2 (catalog covers 802, Design Automation, AI Ethics, 1680, N42, C95), and
  its terms state the material is "explicitly labeled as not in the 'Public Domain'"
  and "the IEEE is, and shall remain the sole copyright holder" — personal-use
  download only, no redistribution/derivative grant.
- Tier decision: **Excluded** (paywalled / all-rights-reserved; same bucket as the
  existing "ISO / IEC / IEEE standards" row). If IEEE later re-admits 15288.2 to the
  GET program, GET terms still forbid redistribution, so it stays excluded for
  packaging.
- Page count: n/a (not accessible without purchase).
- Unique topic (for future reference): defense technical reviews/audits entry/exit
  criteria — coverage gap that stays open.

### 10. ECSS-E-ST-10C Rev.1 — **EXCLUDED-leaning (was expected Tier 2)**
- Source: ECSS-E-ST-10C Rev.1, "Space engineering — System engineering general
  requirements", 15 Feb 2017. Free download at
  https://ecss.nl/standard/ecss-e-st-10c-rev-1-...-15-february-2017/ (page exists,
  PDF/Word offered after accepting the licence).
- Licence evidence (https://ecss.nl/license-agreement-disclaimer/, per ECSS-P-00C
  clause 5.8, 2013): "The European Space Agency, on behalf of the participating
  members, holds copyright for all ECSS documents. No ECSS document may be
  reproduced in any form without the explicit consent of ESA." Consent is granted
  only to ECSS members for their own/contractor use; non-member use requires a
  signed agreement approved by the ECSS Steering Board; quoted text in derived
  documents must acknowledge ECSS copyright and identify modifications.
- Tier decision: **Excluded** absent written ESA/ECSS consent — a pack reproduces and
  transforms the standard, which the licence expressly forbids for non-members.
  (Possible path if ever pursued: request ESA written consent; or a quotation-based
  Tier 3 pack with heavy citation — but that is not the current plan of record.)
- Page count: ~60-80 pp (approx; not downloaded).
- Unique topic: European space SE process requirements — coverage stays open.

### 11. UK Def Stan 00-051 — **UNVERIFIED (decision blocked) + subject-mismatch flag**
- Source: Def Stan 00-051, "Environmental Management Requirements for Defence
  Systems", Issue 2 (2021), Part 1 (Requirements, ~42 pp) + Part 2 (Guidance).
  **Caution:** research shows 00-051 is *environmental management*, not "generic
  product safety" (that is Def Stan 00-056, Safety Management Requirements). The
  v1.17.0 candidate description appears to conflate the two — REQUIREMENTS/T2-03
  should be re-pointed or corrected before build.
- Access: DSTAN portal (now via gov.uk "UK Defence Standardization"; downloads free
  of charge; historically required free registration). No public, fetchable PDF of
  00-051 Issue 2 could be retrieved without registration, so the in-document
  copyright page could not be inspected.
- Licence evidence: Def Stans are Crown copyright. GOV.UK pages state "All content
  is available under the Open Government Licence v3.0, except where otherwise
  stated" — but this is a site-wide footer, NOT confirmed for Def Stan 00-051
  specifically. Some Def Stans carry their own reuse statement. **Unverified:** the
  actual reuse/redistribution terms inside the 00-051 document.
- Tier decision: **UNVERIFIED — pending manual retrieval.** Required evidence: a
  registered DSTAN user must download 00-051 (Part 1) Issue 2 and record (a) the
  exact copyright/reuse statement on its cover/inside-front pages, and (b) whether
  it references OGL v3.0 or bespoke Crown-copyright conditions. If OGL v3.0 applies
  → Tier 2 (attribution condition); if bespoke "no reproduction without MOD
  consent" → Excluded. Record the build-or-exclude decision in SOURCE-VETTING.md
  per T2-03.
- Page count: Part 1 ~42 pp; Part 2 longer (approx).
- Unique topic: environmental management for defence systems (or, if re-pointed,
  safety management via 00-056).

---

## Ruled-out confirmations (RO-01 rows)

| Source | Status | Rationale to record |
|---|---|---|
| INCOSE SE Handbook | Confirmed (already partially in Excluded table) | Wiley-published, paid; copyrighted; not redistributable. Row exists ("Copyrighted (Wiley). Not redistributable.") — extend with INCOSE-GWR below or leave as-is. |
| INCOSE Guide to Writing Requirements | Confirmed paid | INCOSE-published, purchase-only, all-rights-reserved; no open-licence edition. Add new Excluded row; note FUT-02 revisit trigger. |
| ISO/IEC/IEEE 15288, 29148, 21839 full texts | Confirmed paywalled | Existing row "ISO / IEC / IEEE standards (e.g. 15288, 42010, 12207)" already covers 15288; extend the example list to name 29148 and 21839 explicitly (requirements eng. + tailoring, licensed per-user via BSI/Accuris/IHS). |
| DAU/WARU SE Guidebook (Feb 2022) | Confirmed duplicate | Pack `packs/dau-se-guidebook/` already exists in the 48-pack baseline, built from the same Feb-2022 DAU Systems Engineering Guidebook. New candidate would duplicate content. Add Excluded row (or a "already packaged" note) pointing at the existing pack. (Note: public domain, so it is a *dedup* exclusion, not a licence exclusion — worth stating so readers don't infer a licence problem.) |

---

## How docs/SOURCE-VETTING.md should be extended

1. **New Excluded rows** (add to the existing table, following its two-column
   `Source | Why excluded` format; optionally add a date per the Phase 2 criterion):
   - **IEEE 15288.2-2014** — "Purchase/subscription only; not in the IEEE GET
     program; IEEE sole copyright, GET downloads are personal-use, no
     redistribution/derivatives. (Verified 2026-08-14.)"
   - **ECSS standards (incl. ECSS-E-ST-10C Rev.1)** — "Free download from ecss.nl
     but © ESA; 'No ECSS document may be reproduced in any form without the
     explicit consent of ESA' (ECSS-P-00C §5.8). Pack would be reproduction +
     derivative. (Verified 2026-08-14.)"
   - **INCOSE Guide to Writing Requirements** — "Purchase-only, all-rights-reserved
     (INCOSE). Revisit only if an open-licence edition appears (FUT-02)."
   - **DAU/WARU SE Guidebook (Feb 2022) re-pack** — "Duplicate of the existing
     `dau-se-guidebook` pack (US-gov public domain; excluded for duplication, not
     licence)."
2. **Amend the existing ISO/IEC/IEEE row** to name 29148 and 21839 in the examples.
3. **Def Stan 00-051**: hold a placeholder pending the UNVERIFIED evidence; when
   resolved, add either a Tier 2 entry note (OGL v3.0, attribution carried forward)
   or an Excluded row ("Crown copyright; registration-gated; terms not confirmed as
   granting redistribution — excluded pending MOD/DStan permission"). Also correct
   the doc's subject (environmental management, not product safety) wherever the
   candidate is described.
4. **REQUIREMENTS impact (flag for the planner):** T2-01 (IEEE 15288.2) and T2-02
   (ECSS) fail vetting as scoped. Phase 4's "3 Tier-2 packs" reduces to 0-1 packs
   (Def Stan pending). Phase 5's "59+ packs" count needs recomputation (likely
   8 Tier-1 additions → 56 packs, or fewer if 00-051 is excluded).

## Verification gaps (UNVERIFIED items)

- Def Stan 00-051 in-document copyright/reuse terms (registration-gated) — blocks
  the T2-03 build-or-exclude decision.
- Exact page counts for all candidates (marked approximate above) — to be confirmed
  from the PDFs at build time.
- NIST PDF footer statements and CISA PDF title-page notices were not directly read
  (PDF fetch unsupported by tooling); tier decisions rest on the US-Government-work
  statute plus consistent repo precedent.
