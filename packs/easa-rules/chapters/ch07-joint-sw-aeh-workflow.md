# Chapter 7: Joint Software and AEH Certification Workflow

Sources: S1 AMC 20-115D planning-interface passages (section 6 life-cycle/PSAC use of ED-12C/DO-178C, lines 162-201 of `sources/text/S1.txt`, EAR pp. 418-419 cite; supplement application via PSAC/TQP, lines 214-233, EAR p. 419 cite; CIA results into PSAC or SAS, lines 500-513, EAR p. 423 cite); S2 AMC 20-152A planning-interface passages (PHAC may record SEE considerations, lines 42-44 of `sources/text/S2.txt`, EAR p. 497 cite; PHAC documents process and activities against AMC objectives, lines 100-103, EAR p. 498 cite; hardware/software interface and HW/SW interface data for COTS usage, lines 1190-1215, EAR pp. 514-515 cite). Cite-only workflow chapter: does not own body pages. Exclusions: EAR footers; paywalled PSAC/PHAC templates and objective tables (not reproduced). Name-only standards cited here by designation: ED-12C/DO-178C, ED-215/DO-330, technique supplements, ED-80/DO-254. Name-only pointer: AMC 20-189 (open-problem hygiene), not fetched.

## Core Idea

Software and airborne electronic hardware meet in the certification workflow through planning documents the two AMCs already name, not through a third standard invented here. On the software side, AMC 20-115D points applicants at a **plan for software aspects of certification (PSAC)** (and, where tools use technique supplements, a **tool qualification plan (TQP)**), with change-impact results summarised in the PSAC or the **software accomplishment summary (SAS)**. On the hardware side, AMC 20-152A points applicants at a **Plan for Hardware Aspects of Certification (PHAC)** or a related planning document that records the process and activities intended to satisfy the AMC's objectives and that is submitted for certification. The joint seam is the hardware/software interface: intended function, unused-function control on complex COTS, and HW/SW interface data the hardware standard introduces and the AMC expects the applicant to use. This chapter describes those AMC-pointed plan roles. It does not template PSAC or PHAC contents from a paywalled standard.

## Frameworks Introduced

- **PSAC as software liaison plan.** When using ED-12C/DO-178C under AMC 20-115D, the applicant satisfies the objectives for the assigned software level, develops the associated life cycle data, plans and executes activities against each objective, submits the liaison data the recognised standard specifies (including tool-qualification liaison data as applicable), and makes further life cycle data available to EASA on request. CS-specific AMC on software-level mapping, when published, takes precedence over the level-relationship section of the recognised standard.
- **PSAC describes supplement application.** When one or more technique supplements apply, the PSAC states how the primary document and each supplement are used together, which objectives come from which document for which software components, and how planned activities satisfy all applicable objectives. Supplements are not stand-alone means of compliance.
- **TQP when tools use supplement techniques.** For tool qualification levels 1 through 4, if a qualified tool will use techniques the supplements address, the TQP states which tool-qualification objectives the technique use affects and how planned activities satisfy added or modified objectives.
- **CIA results land in PSAC or SAS.** When software is modified, the applicant runs a software change impact analysis, performs the verification the CIA indicates, and summarises CIA results in the PSAC or the SAS. The planning/accomplishment pair is where modification scope becomes visible to certification liaison (detail of CIA content is ch03/ch04).
- **PHAC as hardware liaison plan.** The applicant documents in the PHAC, or any other related planning document, the process and activities intended to satisfy AMC 20-152A objectives, and submits those plans for certification. Objective identity and area detail live in ch05-ch06; this chapter only fixes the planning vehicle.
- **PHAC may still carry SEE considerations.** Single Event Effects sit outside AMC 20-152A body scope (CRI practice; CM-AS-004 name-only in ch05). The PHAC may still document SEE certification considerations without pulling SEE into the AMC body.
- **Hardware/software interface seam.** For COTS device usage, the applicant ensures usage is defined and verified to the hardware's intended function, including the hardware-software interface and hardware-to-hardware interface. At hardware DAL A or B, unused functions of the COTS device must not compromise integrity and availability of used functions; effective deactivation, when available, should be used and verified. Verification level may be hardware, software, or equipment as appropriate. ED-80/DO-254 Section 10.3.2.2.4 introduces HW/SW interface data that can reference the software interface data of the COTS device (standard text not reproduced; designation only).
- **Open-problem hygiene pointer.** **AMC 20-189** is named only for open-problem-report hygiene across the joint workflow. It is not fetched and is not a chapter body in this release.

## Key Concepts

- **What "PSAC/PHAC-style" means here.** The AMCs name planning documents that make process, objectives coverage, supplement use, modification impact, and hardware objective intent auditable for EASA. The style is AMC-facing liaison planning, not a paste of paywalled plan templates.
- **Life cycle data duties stay with the applicant.** Under 115D section 6, producing planned activities and life cycle data that satisfy applicable objectives is the applicant's responsibility. EASA receives specified liaison data and may request further data described in the recognised standard and applicable supplements.
- **Type-design data is level-sensitive.** Not every life cycle data item the recognised standard lists for type design applies at every software level (for example, design description and source code are not type-design data for Level D software, per the AMC's pointer into the standard). Detail remains in the paywalled tables; this pack does not reprint them.
- **Software stack and hardware stack stay parallel until the interface.** PSAC-class artefacts own software objectives and CIA/SAS closeout. PHAC-class artefacts own AEH objective process descriptions. They meet where intended function and interface data cross the HW/SW boundary.
- **Related planning documents are allowed.** Both AMCs allow "related planning documents" beside the named PSAC/PHAC. The name on the cover matters less than whether process and activities against the claimed objectives are written and submitted.
- **No paywalled template in this pack.** Do not expect a filled PSAC or PHAC outline copied from ED-12C/DO-178C or ED-80/DO-254. Buy those documents if you need their data-item descriptions; use avionics-signpost for designations.

## Mental Models

- Two plan spines, one certification body. PSAC (and TQP/SAS as needed) carries the software spine; PHAC carries the hardware spine; EASA reads both against the product or ETSO article.
- Supplements ride inside the PSAC story. A technique supplement without a joint-application description is an incomplete claim.
- CIA without a PSAC/SAS summary is a private analysis; the AMC wants the impact story in the liaison record.
- The HW/SW interface is a shared surface: hardware intends a function, software exercises it, unused COTS behaviour is controlled, and interface data has a named home in the hardware standard (not reprinted here).
- Open problems are a hygiene stream (AMC 20-189 name-only), not a substitute for PSAC/PHAC planning.

## Anti-patterns

- **Templating PSAC or PHAC from a paywalled standard inside this pack.** Describe AMC-pointed roles only; mark standard data-item detail as `see ED-12C/DO-178C` or `see ED-80/DO-254, not reproduced`.
- **Treating a technique supplement as a stand-alone MoC.** The PSAC must show joint application with ED-12C/DO-178C.
- **Satisfying hardware objectives with no PHAC (or related plan) submitted.** Section 4 of AMC 20-152A expects the process and activities to be documented and submitted.
- **Leaving CIA results only in engineering notebooks.** Section 9.b.4 expects summary in the PSAC or SAS.
- **Ignoring HW/SW interface and unused COTS functions at DAL A/B.** Intended-function verification and unused-function control are part of the joint seam the AMC states.
- **Fetching AMC 20-189 into a chapter body.** Keep it name-only for open-problem hygiene.
- **Using this chapter as a substitute for ch03 or ch06 body rules.** Planning interfaces point at assurance and objective chapters; they do not replace them.

## Key Takeaways

1. Joint software and AEH certification under these AMCs runs through PSAC-class and PHAC-class planning documents the AMCs already name, plus SAS closeout and TQP when tools use supplement techniques.
2. Under AMC 20-115D, using ED-12C/DO-178C means satisfying applicable objectives, producing life cycle data, submitting specified liaison data, honouring CS-specific level-mapping AMC when present, and describing supplement application in the PSAC (and TQP when required).
3. Software modification impact is analysed by CIA and summarised in the PSAC or SAS.
4. Under AMC 20-152A, the PHAC or a related planning document records process and activities against AMC objectives and is submitted for certification; it may also record SEE considerations even though SEE is outside AMC body scope.
5. The HW/SW seam covers intended function, hardware-software and hardware-hardware interfaces, unused COTS function control at DAL A/B, verification at an appropriate level, and HW/SW interface data referenced from ED-80/DO-254 (name-only).
6. This chapter does not ship paywalled PSAC/PHAC templates or objective tables.
7. **AMC 20-189** is a name-only pointer for open-problem hygiene; it is not fetched in this release.

## Connects To

- **ch01** - which AMC and which ED Decision answer which question; free versus paywalled split; AltMoC.
- **ch02** - AMC 20-115D scope and replacement that open the software door.
- **ch03** - software life cycle processes, supplement use, and modify/reuse flow that feed PSAC/SAS content.
- **ch04** - tool qualification pointer (TQP path) and GM1 CIA practices.
- **ch05** - AMC 20-152A scope, DAL bounds, SEE name-only, and PHAC as planning vehicle.
- **ch06** - AEH objectives whose process and activities the PHAC describes.
- **faa-8110-49** - FAA-side planning and review twin material; not a substitute for these AMC interfaces.
- **avionics-signpost** - paywalled plan data-item and objective-table designations (no standard text here).
