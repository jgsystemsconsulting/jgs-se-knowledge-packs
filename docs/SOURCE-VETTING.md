<!--
Copyright (c) 2026 JG Systems Consulting Ltd. MIT License (see ../LICENSE).
SPDX-License-Identifier: MIT
-->

# Source Vetting

This is the integrity document for the repository. **No pack is accepted unless its
source clears this rubric.** The whole value of `jgs-se-knowledge-packs` is that every pack
is redistributable by construction, so a colleague can install it, and we can publish it,
without a copyright or licence breach.

The governing principle:

> **"Free to download" is not "free to redistribute."**

A document you can read for free on a website may still be all-rights-reserved. A
knowledge pack *reproduces and transforms* a source into new files that we then publish.
That is redistribution plus derivative work. It needs an actual grant.

---

## The eligibility tiers

A source must land in **Tier 1 or Tier 2** to be packaged. Tier 3 is case-by-case and
needs a written rationale in the pack's `PACK.yaml`. The Excluded tier is a hard stop.

### 🟢 Tier 1: Public domain (maximum freedom)

Works with no copyright, or an explicit public-domain dedication. Reproduce, transform,
and redistribute freely. Attribution is courtesy, not obligation.

- **US Government works**: not subject to copyright in the US (17 U.S.C. § 105).
  Examples: NASA, NIST, US DoD, FAA publications.
- Look for a **Distribution Statement A** ("Approved for public release; distribution is
  unlimited") on defense documents, or a US-gov-authorship statement.
- CC0 / explicit public-domain dedication.

### 🟡 Tier 2: Open licence (shareable with conditions)

A licence that grants redistribution and (ideally) derivative works. The pack **must
carry the source's conditions forward**: attribution, share-alike, non-commercial,
trademark limits.

- **Creative Commons** BY, BY-SA, BY-NC, BY-NC-SA. (NC and SA propagate to the pack;
  see "Carrying conditions forward" below.)
- Permissive software/content licences (MIT, Apache-2.0, BSD) where they cover the text.

> **Not Tier 2: OMG specifications.** The OMG Specification License *looks* open but its
> public grant is informational-use-only (no network posting, no modification; see the
> Excluded list). Do not classify OMG specs as Tier 2.

### 🟠 Tier 3: Caution (verbatim-only or unclear grant)

Package only with an explicit written justification in `PACK.yaml` and, where the grant
is ambiguous, a note that the maintainers judged it defensible (or sought permission).

- **No-derivatives clauses** (e.g. CC BY-ND). A knowledge pack transforms the source, so a
  strict no-derivatives source is normally **not** packageable, at most a verbatim excerpt
  with heavy citation. Prefer to exclude. (OMG specs are fully **Excluded**; see below.)
- **"Freely available" with no stated licence.** Free download ≠ redistribution grant.
  Treat as Excluded until a real grant is found or permission is obtained.

### 🔴 Excluded: read-only, not redistributable (hard stop)

These are valuable and you may *read and cite* them, but you may **not** package them.
This list exists so the repo never ships something that triggers a takedown.

| Source | Why excluded |
|---|---|
| **ISO / IEC / IEEE standards** (e.g. 15288, 42010, 12207, 29148, 21839) | Paywalled, all-rights-reserved. Licensed per-user, often via BSI/Accuris/IHS. Requirements engineering (29148) and tailoring (21839) are the same per-user licence model. (Verified 2026-08-14.) |
| **INCOSE SE Handbook** | Copyrighted (Wiley). Not redistributable. (Verified 2026-08-14.) |
| **SWEBOK v4** (IEEE) | Free download, but licence says "may not alter the text in any way," individual & non-commercial only. |
| **MITRE SE Guide** | "© The MITRE Corporation. All rights reserved." |
| **The Open Group TOGAF / ArchiMate** | Evaluation/member licence; not redistributable. |
| **PMI PMBOK** | PMI copyright. |
| **INCOSE SE Vision 2035** | Freely downloadable but no stated redistribution/derivative grant (Tier 3 → treat as excluded pending permission). |
| **INCOSE Systems Engineering Competency Framework (2nd ed.)** | Freely downloadable (Excel) but © INCOSE, all rights reserved; no redistribution/derivative grant — reuse routed through INCOSE Permissions & Copyrights. Same pattern as the SE Vision 2035 row. (Verified 2026-08-14.) |
| **OMG formal specifications** (UML, SysML, BPMN, UAF, CORBA, MOF, XMI, OCL, DDS…) | OMG Specification License public grant is informational-use-only: the spec "will not be copied or posted on any network computer … or … transferred for commercial purposes" and "no modifications are made to this specification." A hosted, transformed pack breaches both. Confirmed by two independent licence reads (2026-06-19). Cite + link to the OMG download; never package. |
| **IEEE 15288.2-2014** `[T2-01]` | Purchase/subscription only; not in the IEEE GET program; IEEE sole copyright holder, GET downloads are personal-use with no redistribution/derivative grant. (Verified 2026-08-14.) |
| **ECSS standards (incl. ECSS-E-ST-10C Rev.1)** `[T2-02]` | Free download from ecss.nl but © ESA; "No ECSS document may be reproduced in any form without the explicit consent of ESA" (ECSS-P-00C §5.8). A pack is reproduction + derivative work. (Verified 2026-08-14.) |
| **INCOSE Guide to Writing Requirements** | Purchase-only, all-rights-reserved (INCOSE). Revisit only if an open-licence edition appears (FUT-02). (Verified 2026-08-14.) |
| **DAU/WARU SE Guidebook (Feb 2022) re-pack** | Duplicate of existing `packs/dau-se-guidebook/` in the 48-pack baseline (US-gov public domain; excluded for duplication, not licence). (Verified 2026-08-14.) |

> If you are licensed to read one of these (e.g. an employer's BSI/Accuris seat for an
> ISO standard), that licence is **yours**, not the repo's. Building a pack from it for
> your own private use may be fine; **publishing that pack here is not.** Keep
> source-restricted packs in a private/local skills directory, never in this repo.

### Vetted candidates (v1.17.0) — statute-basis; confirm in-source at build

Source URLs for all vetted/excluded/UNVERIFIED candidates are recorded in
`.planning/phases/2-source-vetting-ruled-out-register/2-RESEARCH.md` (Link Policy: never
published in docs or packs).

Statute-basis rows below rest on 17 U.S.C. § 105 (US Government works). In-PDF statements
(NIST footers, CISA title page, DOE SEM third-party notices, Distribution Statement A on
DoD handbooks) are confirmed at build time in Phase 3 — these rows are pending that
in-source confirmation.

| Source | Tier | Licence evidence |
|---|---|---|
| **NIST SP 800-171 Rev.3** (NIST CSRC; Protecting CUI in Nonfederal Systems; final 2024-05-14) | Tier 1 | US Government work (17 U.S.C. § 105); NIST staff-authored publication. Confirm PDF footer at build. |
| **NIST SP 800-61 Rev.3** (NIST; Incident Response Recommendations; final 2025-04-03) | Tier 1 | US Government work (17 U.S.C. § 105); same NIST basis. Confirm PDF footer at build. |
| **MIL-HDBK-338B** (DoD Electronic Reliability Design Handbook, 1 Oct 1998; Notice 2 2007) | Tier 1 | Distribution Statement A + US Gov work (17 U.S.C. § 105). Confirm statement on PDF cover/i page at build. |
| **MIL-HDBK-516C** (DoD Airworthiness Certification Criteria, 2014 w/ Change 1 2016) | Tier 1 | Distribution Statement A + US Gov work (17 U.S.C. § 105). Quote confirmed from DLA-hosted document. |
| **NASA-STD-7009B + NASA-HDBK-7009** (NASA Standard/Handbook for Models and Simulations; STD-7009B 2024-03-05) | Tier 1 | NASA-authored US Government work (17 U.S.C. § 105); not subject to copyright in the United States; attribution courtesy. |
| **DOE O 413.3B Chg 7** (DOE Order, Program and Project Management for the Acquisition of Capital Assets; LtdChg 2023-06-21) | Tier 1 | US DOE government work (17 U.S.C. § 105). Confirm no third-party-copyright notices inside the PDF at build. |
| **CISA CPG 2.0** (CISA Cross-Sector Cybersecurity Performance Goals 2.0; ~2024-25) | Tier 1 | CISA federal-employee authorship → public domain (17 U.S.C. § 105). Verify PDF title/disclaimer page at build; watch for embedded third-party logos/content. |
| **DOE SEM3** (US DOE Systems Engineering Methodology, SEM version 3) | Tier 1 | DOE-authored US Government work (17 U.S.C. § 105). Confirm no third-party copyright notice inside the PDF at build. |

### Vetted candidates (v1.18.0) — statute-basis; confirm in-source at build

Source URLs for all vetted/excluded candidates are recorded in
`.planning/phases/6-source-vetting-unverified-resolution/6-RESEARCH.md` (Link Policy: never
published in docs or packs).

Statute-basis rows below rest on 17 U.S.C. § 105 (US Government works) unless noted.
In-PDF statements (Distribution Statement A, releasability lines, NTRS copyright metadata)
are confirmed at build time in Phase 7 — these rows record the Phase 6 verdict with that
build caveat.

| Source | Tier | Licence evidence |
|---|---|---|
| **GP-07 / MIL-STD-40051-2C** (DoD page-based TM preparation; rev -2C 15 DEC 2015; -1/-2 family supersedes base 40051) | Tier 1 | US Government work (17 U.S.C. § 105); DIST-A on DLA ASSIST family records. Build caveat: Distribution Statement is a scanned image on the mirror copy — DIST-A must be visually confirmed on the cover at build (6-RESEARCH.md §1a). (Verified 2026-08-14.) |
| **NASA SP-7084** (Grammar, Punctuation, and Capitalization: A Handbook for Technical Writers and Editors; Mary K. McCaskill, NASA Langley) | Tier 1 | NTRS metadata: "Work of the US Gov. Public Use Permitted"; Distribution Limits Public. Prefer 1998 rev if mirror has text layer, else NTRS 1990 canonical (6-RESEARCH.md §1b). (Verified 2026-08-14.) |
| **GP-01 / DoD VV&A RPG** (DoD VV&A Recommended Practice Guide; OUSW(R&E); multi-chapter web delivery) | Tier 1 | US Government work (17 U.S.C. § 105). Build model: no consolidated PDF — chapter-wise build with per-chapter provenance in PACK.yaml; confirm DIST-A / authorship inside each chapter PDF used (6-RESEARCH.md §1c). (Verified 2026-08-14.) |
| **GP-05 / MIL-STD-881F** (Defense Work Breakdown Structures; Active on DLA ASSIST) | Tier 1 | US Government work (17 U.S.C. § 105). Fetch via DLA ASSIST-QuickSearch (free account) or GovTribe attachment (everyspec has only 881E); DIST-A visual confirm at build; resolve exact revision date on QuickSearch detail page (6-RESEARCH.md §1d). (Verified 2026-08-14.) |
| **GP-02 / FAA-STD-025** (FAA Interface Documentation IRD/ICD/IR) | Tier 1 | US Government work (17 U.S.C. § 105). Rev E canonical (ROSAP full-text PDF) + rev F mirror; record chosen revision in PACK.yaml (6-RESEARCH.md §2a). (Verified 2026-08-14.) |
| **GP-03 / DOT&E T&E Enterprise Guidebook** (Test & Evaluation Enterprise Guidebook) | Tier 1 | US Government work (17 U.S.C. § 105). Target Aug 2022 edition (8.02) from dote.osd.mil if a direct PDF is obtainable; fall back to the afacpo fixed-URL single-encoded mirror PDF (v3 June 2022) if direct download unavailable; PACK.yaml records the edition actually built (8.02 or mirror v3-June) (6-RESEARCH.md §2b). (Verified 2026-08-14.) |
| **GP-04 / DAFMAN 63-119** (DAF Mission-Oriented Test Readiness Certification; 15 Apr 2021) | Tier 1 | In-document "RELEASABILITY: There are no releasability restrictions on this publication"; USAF publication → 17 U.S.C. § 105. Title corrected to Mission-Oriented Test Readiness Certification (6-RESEARCH.md §2c). (Verified 2026-08-14.) |
| **GP-06 / federal-bca** (dual-source: OMB Circular A-94 + US Army CBA Guide) | Tier 1 | Both are U.S. Government works, public domain per 17 U.S.C. § 105 (licence basis per 6-RESEARCH.md §2 spot-check scope and capability-gap-report shortlist item 5). Record per-source provenance for both documents in PACK.yaml. (Verified 2026-08-14.) |

**GP-08 deferral note:** NASA-HDBK-2203 standards-page PDF is a placeholder; content is swehb.nasa.gov wiki HTML only — deferred out of v1.18 (see REQUIREMENTS Out of Scope and 6-RESEARCH.md §4). Optional future rescope to NPR 7150.2 + NASA-STD-8739.8 (downloadable PDFs).

### Def Stan 00-051 — UNVERIFIED / excluded from this milestone `[T2-03]`

**Def Stan 00-051** (*Environmental Management Requirements for Defence Systems*, Issue 2
2021) is **UNVERIFIED** and **excluded from v1.17.0** pending a registered DSTAN user
recording the exact cover/inside-front copyright/reuse statement.

- **Subject correction:** 00-051 is environmental management for defence systems — **not**
  system safety. System safety is **Def Stan 00-056** (Safety Management Requirements). The
  original v1.17.0 candidate description conflated the two.
- **Access:** Crown copyright; downloads are free of charge but registration-gated via the
  DSTAN / UK Defence Standardization portal. No public fetchable PDF was available, so
  in-document reuse terms could not be inspected this milestone.
- **Pending decision path:** If OGL v3.0 applies inside the document → Tier 2 (attribution
  carried forward). If bespoke MOD-consent / no-reproduction terms → stays Excluded.
- **Recorded outcome (2026-08-14):** deferred-excluded for this milestone; no pack build
  until the in-document terms are recorded by a registered DSTAN user.

---

## Carrying conditions forward

When a source is Tier 2, the pack inherits its obligations:

- **Attribution (BY)**: `PACK.yaml` records title, author/publisher, version, URL; the
  pack `LICENSE` file reproduces the source notice.
- **Share-alike (SA)**: the pack's *content* is released under the same licence as the
  source (not the repo's MIT). State this in the pack `LICENSE`.
- **Non-commercial (NC)**: the pack is flagged `commercial_use: false` in `PACK.yaml`.
  The repo tooling (MIT) is separate from pack *content* licences.
- **Trademark / no-endorsement**: do not imply the source's authors endorse the pack;
  do not use a trademarked spec name on a transformed work (OMG rule).

The repository tooling and scaffolding are MIT. **Pack content licences are independent
and per-pack**: a pack folder always contains its own `LICENSE`.

---

## The vetting checklist (run before opening a pack PR)

1. [ ] Identified the exact source document, version, and publisher. (Read the source's
   own licence to vet it; the source URL is used for vetting only, never published.)
2. [ ] Found the **licence statement** in the source itself (not a third-party claim).
3. [ ] Assigned a tier (1 / 2 / 3) with the licence named.
4. [ ] Source is **not** on the Excluded list.
5. [ ] If Tier 2: NC / SA / BY / trademark conditions recorded in `PACK.yaml`.
6. [ ] If Tier 3: written justification present.
7. [ ] Pack folder contains a `LICENSE` reproducing the source's terms.
8. [ ] `PACK.yaml` `title`, `publisher`, `license`, `license_tier`, `commercial_use`
   filled: textual attribution, **no source-material URL published** (see LICENSING.md).

CI enforces 4, 7, and 8 mechanically (`tooling/validate_pack.py`). Tiers 1–3 judgement
is human and reviewed on the PR.

> **Link policy.** Source-material URLs are recorded during vetting but are **not**
> published anywhere in a pack or the docs. Attribution travels as text (title +
> publisher + version + licence) plus the licence-deed link, which the licences accept.
> See [LICENSING.md](LICENSING.md) §4.
