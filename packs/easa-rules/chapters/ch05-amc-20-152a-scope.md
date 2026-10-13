# Chapter 5: AMC 20-152A Scope and Background

Sources: S2 AMC 20-152A (ED Decision 2020/010/R; AMC-20 Amendment 19, consolidated in Amendment 23), sections 1 PURPOSE, 2 APPLICABILITY, 3 DOCUMENT HISTORY, 4 BACKGROUND, lines 13-104 of `sources/text/S2.txt` (printed pp. 497-498). Exclusions: EAR footers and title banners. Name-only standards cited here by designation: ED-80/DO-254. Name-only SEE pointer: CRI practice / EASA CM-AS-004 Issue 01 (8 January 2018), not fetched.

## Core Idea

AMC 20-152A is an acceptable means, not the only means, for showing compliance with airworthiness regulations on the electronic hardware aspects of airborne systems and equipment. It covers product certification and ETSO authorisation. Compliance with the AMC is not mandatory; an applicant may use an AltMoC that meets the relevant requirements, ensures an equivalent level of safety, and is approved by EASA on a product or ETSO article basis. The AMC recognises ED-80/DO-254 as the development assurance standard for airborne electronic hardware, then goes further than recognition: it states when to apply that pair and supplements them with additional objectives for custom devices (including COTS IP), COTS devices, and circuit board assemblies. Software applicability is outside this AMC (see ch02).

## Frameworks Introduced

- **Acceptable means with AltMoC escape.** Same shape as the software AMC: the AMC is one path; AltMoC needs equivalent safety and EASA approval on a product or ETSO article basis.
- **Recognised primary pair.** EUROCAE ED-80 (April 2000) and RTCA DO-254 (19 April 2000), Design Assurance Guidance for Airborne Electronic Hardware. Where the AMC writes `ED-80/DO-254`, the two documents are treated as equivalent.
- **Recognition plus supplementation.** Section 1.3 both describes when to apply ED-80/DO-254 and adds AMC-owned objectives and clarifications for three hardware areas the standard leaves thin: custom devices including COTS IP, COTS devices, and CBAs. Objectives are the AMC's form; the applicant describes the process and activities that satisfy them.
- **DAL-bounded AEH coverage.** The AMC applies to AEH that contributes to hardware DAL A, B, or C functions. DAL C takes only a limited objective set, with any per-DAL restriction written into the objective text (for example `For DAL A hardware, ...`).
- **DAL D not required.** Use of this AMC is not required for AEH contributing to hardware DAL D functions. the AMC's own Appendix B clarifications (summarised in ch06) that help show DAL D hardware performs its intended function remain available as optional support (see ch06 appendix summary).
- **SEE out of scope (name-only).** Single Event Effects and hardware susceptibility to SEE are outside this AMC. They are usually handled through CRI practice; further guidance may be found in EASA CM-AS-004 Issue 01 (8 January 2018), not fetched here. The PHAC may still record SEE certification considerations.
- **Objective identity scheme (section 4).** Unique identifiers carry a prefix and index: `CD-i` (custom devices), `IP-i` (COTS IP in custom devices), `COTS-i` (COTS devices), `CBA-i` (circuit board assemblies). Objectives are set in italics in the official AMC text. Detail of each objective lives in ch06.
- **PHAC as the planning vehicle.** The applicant documents, in the Plan for Hardware Aspects of Certification or a related planning document, the process and activities intended to satisfy the AMC objectives, and submits those plans for certification.

## Key Concepts

- **Audience.** Applicants, design approval holders, and developers of airborne systems and equipment containing AEH installed on type-certified aircraft, engines, and propellers, including developers of ETSO articles.
- **What "recognises" means here.** The AMC points at ED-80/DO-254 and does not reprint their life-cycle data or appendix tables. Those documents stay paywalled; this pack names them only (see ED-80/DO-254, not reproduced).
- **What the AMC adds beyond recognition.** When-to-apply rules, plus original AMC objectives for custom devices / COTS IP, COTS devices, and CBAs (ch06). The applicant's job is to describe process and activities against those objectives, not to invent a second hardware standard.
- **Document history.** This document is the initial issue of AMC 20-152, intentionally set at Revision A and jointly developed with the FAA.
- **Topic layout.** Each major topic (custom devices including COTS IP, COTS devices, CBAs) is organised with background, applicability, and uniquely identified objective sections.
- **Software is not answered here.** Product/ETSO software means of compliance belong to AMC 20-115D (ch02-ch04). This chapter stays on electronic hardware.

## Mental Models

- Think of AMC 20-152A as the EASA hardware door: it names ED-80/DO-254 as acceptable and hangs three extra objective racks (custom/IP, COTS, CBA) on that door. The racks are summarised in ch06; the paywalled standard is not reprinted.
- DAL A/B/C is the entry ticket; DAL D is outside the required-use boundary even when structured development still helps.
- SEE is a side door labelled CRI / CM-AS-004, not a chapter body. Name it, do not fetch it.
- The PHAC is where intent becomes auditable: objectives without a planned process are incomplete for certification liaison.

## Anti-patterns

- **Treating the AMC as mandatory law.** Section 1.1 states compliance is not mandatory; AltMoC exists under the stated conditions.
- **Citing paywalled ED-80/DO-254 life-cycle or appendix tables from this pack.** The AMC recognises the standard; it does not ship those tables, and neither does this chapter (see ED-80/DO-254, not reproduced).
- **Applying the full objective set at DAL C by default.** DAL C takes only the limited set; read each objective's own DAL restriction.
- **Requiring this AMC at DAL D.** Section 2 states use is not required for AEH contributing to hardware DAL D functions.
- **Answering the software question from 152A.** Software applicability is AMC 20-115D territory (ch02).
- **Treating SEE as in-scope AMC content.** Section 1.4 puts SEE outside the AMC; keep it name-only (CRI / CM-AS-004).
- **Skipping the PHAC.** Section 4 expects the process and activities against the objectives to be planned and submitted.

## Key Takeaways

1. AMC 20-152A is an acceptable (not sole) means for electronic hardware aspects of product certification and ETSO authorisation; AltMoC needs equivalent safety and EASA approval on a product or ETSO article basis.
2. The AMC recognises ED-80/DO-254 and supplements them with additional objectives for custom devices including COTS IP, COTS devices, and CBAs; the applicant describes process and activities that satisfy those objectives.
3. Applicability covers applicants, DAHs, and developers of AEH on type-certified aircraft, engines, and propellers, including ETSO article developers.
4. The AMC applies to AEH contributing to hardware DAL A, B, or C; DAL C takes a limited objective set written into the objective text; use is not required at DAL D.
5. SEE aspects are outside this AMC (CRI practice; CM-AS-004 name-only); the PHAC may still record SEE certification considerations.
6. Objective IDs use CD/IP/COTS/CBA prefixes; planning against them belongs in the PHAC or a related planning document submitted for certification.
7. Software applicability is outside this chapter.

## Connects To

- **ch01** - which AMC and which ED Decision answer which question; AltMoC at the pack level.
- **ch02** - AMC 20-115D software scope (not answered here).
- **ch06** - the added AEH objectives for custom devices, COTS IP, COTS devices, and CBAs.
- **ch07** - joint software and hardware planning interfaces (PHAC/PSAC-style).
- **faa-8110-49** - FAA-side twin material where AC 20-152A matters; not a substitute for this AMC text.
