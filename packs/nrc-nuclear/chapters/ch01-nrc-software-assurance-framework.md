# Chapter 1: NRC digital software assurance framework

Sources: S7 NUREG-0800 Branch Technical Position 7-14, "Guidance on Software Reviews for Digital Computer-Based Instrumentation and Control Systems" (Rev. 6, August 2016, ML16019A308), A. BACKGROUND through B.1 Introduction, lines 56-436 of `sources/text/S7.txt` (printed pp. 2-9); S1 Regulatory Guide 1.168, "Verification, Validation, Reviews, and Audits for Digital Computer Software Used in Safety Systems of Nuclear Power Plants" (Rev. 2, July 2013, ML13073A210), A. INTRODUCTION Purpose and Applicable Rules and B. DISCUSSION through Related Guidance lead-in, lines 16-76 and 113-300 of `sources/text/S1.txt` (printed pp. 1, 3-5); S2 Regulatory Guide 1.169, "Configuration Management Plans for Digital Computer Software Used in Safety Systems of Nuclear Power Plants" (Rev. 1, July 2013, ML12355A642), A. INTRODUCTION body and B. DISCUSSION, lines 16-78 and 115-325 of `sources/text/S2.txt` (printed pp. 1, 3-5); S3 Regulatory Guide 1.170, "Software Test Documentation for Digital Computer Software Used in Safety Systems of Nuclear Power Plants" (Rev. 1, July 2013, ML13003A216), A. INTRODUCTION body and B. DISCUSSION, lines 16-76 and 97-342 of `sources/text/S3.txt` (printed pp. 1, 2-6); S4 Regulatory Guide 1.171, "Software Unit Testing for Digital Computer Software Used in Safety Systems of Nuclear Power Plants" (Rev. 1, July 2013, ML13004A375), A. INTRODUCTION body and B. DISCUSSION, lines 15-73 and 93-275 of `sources/text/S4.txt` (printed pp. 1, 2-5); S5 Regulatory Guide 1.172, "Software Requirements Specifications for Digital Computer Software Used in Safety Systems of Nuclear Power Plants" (Rev. 1, July 2013, ML13007A173), A. INTRODUCTION body and B. DISCUSSION, lines 17-76 and 97-287 of `sources/text/S5.txt` (printed pp. 1, 2-5); S6 Regulatory Guide 1.173, "Developing Software Life Cycle Processes for Digital Computer Software Used in Safety Systems of Nuclear Power Plants" (Rev. 1, July 2013, ML13009A190), A. INTRODUCTION body and B. DISCUSSION, lines 15-76 and 113-327 of `sources/text/S6.txt` (printed pp. 1, 3-6). Exclusions per pin: S1-S6 cover mastheads above A. INTRODUCTION, Purpose-of-RGs and Paperwork Reduction plates, D. IMPLEMENTATION plates, and REFERENCES; S7 cover and review-responsibilities plate, C. REFERENCES, Paperwork/Public Protection, and figure/numbering back matter. Name-only standards cited with edition as printed: IEEE Std 603-1991 (10 CFR 50.55a(h) path and RG applicable-rules text); IEEE Std 279-1971 (alternate construction-permit path the BTP names); IEEE Std 7-4.3.2 as the BTP and RGs name it via RG 1.152; IEEE Std 1012, 1028, 828, 829, 1008, 830, and 1074 named only as the matching RG endorsement pair. Adjacent RG 1.152 and RG 5.71 named only where the sources point to them for computers in safety systems, SDOE, or cyber security. Staff review positions for plans, implementation, and design outputs live in later chapters; this chapter orients the family.

## Core Idea

NRC regulations set high-level quality and design-control expectations for safety system instrumentation and control. The six July 2013 software Regulatory Guides describe methods the staff considers acceptable for meeting those expectations for digital computer software in safety systems. Following a guide is one acceptable path; an applicant may propose an alternative with adequate demonstration. The Standard Review Plan (NUREG-0800) is the staff's own review guidance. BTP 7-14 inside SRP Chapter 7 applies that review lens to software: staff acceptance rests on acceptable plans, evidence the plans were followed through a software life cycle, and acceptable design outputs the process produced.

This chapter is the map. It states what each guide is for, how the BTP frames review, which definitions the BTP uses for planning and product characteristics, and which later chapter carries the detailed staff positions. It does not restate the C. STAFF REGULATORY GUIDANCE bodies or the B.3 plan, implementation, and design-output criteria; those sit in ch02 through ch07.

## Frameworks Introduced

- **Three-legged software acceptance (S7 A. BACKGROUND).** Staff acceptance of safety system software rests on (1) confirmation that acceptable plans controlled development, (2) evidence those plans were followed in an acceptable life cycle, and (3) evidence the process produced acceptable design outputs. The BTP supplies guidelines for evaluating software life cycle processes for digital computer-based I&C. The structure follows the digital I&C review process in SRP Appendix 7.0-A. Plans are assumed to run inside a QA program that meets regulatory requirements and to augment that program, not replace it.
- **Regulatory basis summary (S7 A.1).** The BTP points to SRP Appendix 7.1-A and summarizes: 10 CFR 50.54(jj) and 50.55(i) quality standards commensurate with safety importance; 10 CFR 50.55a(h) protection and safety systems, which requires compliance with IEEE Std 603-1991 (and the January 30, 1995 correction sheet), with plant-specific licensing-basis or IEEE Std 279-1971 options for older construction-permit cohorts as the BTP states; GDC 1 quality standards and records; GDC 21 protection system reliability and testability; and 10 CFR Part 50 Appendix B Criteria III (design control), V (instructions, procedures, and drawings), VI (document control), VII (purchased material, equipment, and services), and XI (test control). IEEE Std 603-1991 appears here by name only where the source cites it; evaluation detail lives in SRP appendices the BTP names, outside this pack's chapter bodies.
- **Relevant guidance map (S7 A.2).** The BTP lists the companion guides that carry detailed methods: RG 1.28 for QA program criteria; RG 1.152 for criteria for use of computers in safety systems (endorsing IEEE Std 7-4.3.2 with noted exceptions) and SDOE; RG 1.168 for V&V plus reviews and audits (IEEE Std 1012 and IEEE Std 1028 with exceptions); RG 1.169 for configuration management plans (IEEE Std 828); RG 1.170 for test documentation (IEEE Std 829); RG 1.171 for unit testing (ANSI/IEEE Std 1008); RG 1.172 for software requirements specifications (IEEE Std 830); and RG 1.173 for life cycle process development (IEEE Std 1074). BTP acceptance criteria sit on that base. Important context still lives in the referenced standards and RGs; the BTP does not replace them.
- **BTP definition set used across later chapters (S7 A.3).** Activity group: life cycle activities related to one topic. Design output: documents that define technical requirements of the end product installed in the plant, including software requirements specifications, software design specifications, hardware and software architecture designs, code listings, system build documents, installation configuration tables, and operations, maintenance, and training manuals. Deterministic timing: guaranteed maximum and minimum delay between stimulus and response. Documentation: recorded life cycle information in written or electronic form. Plan: a document describing a specific implementation of a process. Process: a series of actions bringing about a result (a QA program is an example process definition). Requirements Traceability Matrix (RTM): every requirement broken into sub-requirements as needed, mapped to software requirement, design description, code, and test requirement portions that address the system requirement.
- **Planning characteristic families (S7 A.3.1).** Management: purpose, organization, oversight, responsibilities, risks, security (including SDOE per RG 1.152, with 10 CFR 73.54 and RG 5.71 named for malicious cyber-attack protection of critical digital assets). Implementation: measurement, procedures, record keeping, schedule. Resources: budget, methods and tools, personnel, standards.
- **Functional and process product characteristics (S7 A.3.2).** Functional: accuracy, functionality, reliability, robustness, safety, security (SDOE per RG 1.152), timing. Process: completeness, consistency, correctness, style, traceability, unambiguity, verifiability. Both sets matter for safety system software. Several process definitions cross-reference IEEE Std 830 as endorsed by RG 1.172; this pack keeps those as name-only pointers.
- **B.1 introduction: digital sharing and common-cause concern (S7 B.1).** Digital I&C safety systems must be designed, fabricated, installed, and tested to quality standards commensurate with safety importance; an acceptable software life cycle is how software quality is obtained. Digital systems share code, data transmission, data, and process equipment more than analog systems. That sharing enables capability and also raises common-cause and common-mode failure via software errors that can defeat hardware redundancy. Greater sharing of process equipment within a channel increases the consequences of a single hardware module failure and reduces diversity inside the channel. Staff review therefore emphasizes quality, diversity, and defense-in-depth against common-cause failures. Software develops under a formally defined life cycle chosen and documented by the developer (applicant, licensee, vendor, or commercial developer). Activity groups are common across life cycle models; life cycle work produces process documents and design outputs that can be reviewed.
- **What a Regulatory Guide is (S1-S6 A. INTRODUCTION Purpose pattern).** Each guide describes a method the staff considers acceptable for complying with NRC regulations on its topic for digital computer software used in safety systems of nuclear power plants. The six topics partition the life cycle:
  - **RG 1.168 (S1):** verification, validation, reviews, and audits; endorses IEEE Std. 1012-2004 and IEEE Std. 1028-2008 with exceptions and additions.
  - **RG 1.169 (S2):** configuration management plans; endorses IEEE Std. 828-2005 with provisions.
  - **RG 1.170 (S3):** software and system test documentation; endorses IEEE Std. 829-2008 with provisions and exceptions.
  - **RG 1.171 (S4):** software unit testing; endorses ANSI/IEEE Std. 1008-1987 with provisions and exceptions.
  - **RG 1.172 (S5):** software requirements specifications, including for complex electronics; endorses IEEE Std. 830-1998 with provisions and exceptions.
  - **RG 1.173 (S6):** developing software life cycle processes; endorses IEEE Std. 1074-2006 with provisions and exceptions.
- **Shared regulatory skeleton in each RG purpose and discussion (S1-S6).** Applicable rules repeatedly include GDC 1, Appendix B QA criteria, and the 10 CFR 50.55a(h) path that names IEEE Std 603-1991 (with older-plant alternatives as each guide states). Discussion sections explain why the topic matters for safety software, how the endorsed IEEE standard is used subject to the guide's clarifications, and how the guide relates to the rest of the family (life cycle, V&V, CM, test, requirements). Harmonization and related-guidance lead-ins point across the six RGs and to RG 1.152 where computers in safety systems or SDOE are in view. Staff regulatory guidance bodies (the C sections) are not restated here; they are the bodies of ch02-ch06.
- **Which chapter answers which question.**
  - Framework and "which document": this chapter (ch01).
  - Life cycle processes and planning-document reviews B.3.1.1-B.3.1.9: ch02 (RG 1.173 + BTP planning).
  - Software requirements specification content and qualities: ch03 (RG 1.172).
  - Configuration management plans and B.3.1.11 SCMP review: ch04 (RG 1.169).
  - V&V, reviews, audits, and B.3.1.10 SVVP review: ch05 (RG 1.168).
  - Test documentation, unit testing, and B.3.1.12 STP review: ch06 (RG 1.170, RG 1.171).
  - Implementation acceptance B.3.2, design-output acceptance B.3.3, and B.4 review procedures: ch07.
  - Endorsed standards and adjacent NRC guidance name-only map: ch08.

## Key Concepts

- **RG path is acceptable, not exclusive.** Guides describe methods the staff considers acceptable. Alternatives need adequate demonstration.
- **SRP and BTP are reviewer guidance.** They do not invent new regulations; they tell staff what to check against the existing regulatory basis.
- **Plans, implementation, outputs.** The three acceptance legs structure the entire BTP review.
- **IEEE Std 603-1991 by name only.** Where 10 CFR 50.55a(h) and the guides cite it, this pack names the designation and edition and does not restate IEEE clauses.
- **SDOE versus cyber security.** BTP planning security points to RG 1.152 for SDOE (inadvertent and unwanted modification, predictable undesirable acts). Malicious cyber-attack protection of critical digital assets is a 10 CFR 73.54 / RG 5.71 topic the BTP names separately.
- **Deterministic timing.** Stimulus-to-response delay has guaranteed maximum and minimum; timing shows up again in design-output criteria.
- **RTM is central.** Trace every requirement through software requirement, design, code, and test.
- **Activity groups are the common currency.** Different life cycle models still group work into reviewable activity groups that produce documents and design outputs.
- **Common-cause via shared software is the digital-specific worry.** Quality, diversity, and defense-in-depth are the staff's stated counterweights.
- **Edition and licensing basis.** This pack pins the July 2013 RGs and BTP 7-14 Rev 6. The plant licensing basis decides which revision applies to a given plant.

## Mental Models

- **Six RGs build; BTP grades.** Applicant-facing methods live in RG 1.168-1.173. Reviewer-facing acceptance criteria live in BTP 7-14. Same practice, two voices.
- **ch01 is the legend on the map.** Detailed terrain is ch02-ch07; the gazetteer of foreign standards is ch08.
- **QA program is the floor; software plans are the furniture.** Plans augment and supplement Appendix B processes; they do not float free of them.
- **Functional characteristics ask what the software must do; process characteristics ask whether the product is reviewable and trustworthy.** Both are scored on design outputs in ch07.
- **Sharing buys capability and spends independence.** Every shared code or data path is a potential common-cause bridge; software quality is part of how that risk is managed.

## Anti-patterns

- **Treating an RG as a mandatory exclusive recipe.** It is an acceptable method; alternatives exist with demonstration.
- **Reading BTP 7-14 as if it replaced the six RGs.** The BTP assumes the RG/IEEE pairs and adds review criteria.
- **Skipping plans and jumping to code.** Acceptance still needs plans and evidence the plans were followed.
- **Collapsing SDOE and cyber security into one checklist.** The sources separate RG 1.152 SDOE from 10 CFR 73.54 / RG 5.71 malicious-attack programs.
- **Restating IEEE Std 603-1991 clauses inside pack notes.** Name-only.
- **Assuming the pack's pinned edition is every plant's licensing basis.** Flag the licensing-basis caveat.
- **Looking in ch01 for C-section staff positions or B.3.2/B.3.3 criteria.** Those are ch02-ch07.

## Key Takeaways

1. Staff acceptance of safety system software is three-legged: acceptable plans, followed life cycle, acceptable design outputs.
2. BTP 7-14 is SRP Chapter 7 staff guidance for software reviews, built on the regulatory basis in 10 CFR 50.55a(h) (IEEE Std 603-1991 path as stated), GDC 1 and 21, and Appendix B design control, procedures, document control, purchasing, and test control criteria.
3. The six July 2013 RGs partition life cycle concerns: 1.173 processes, 1.172 requirements, 1.169 configuration management, 1.170 test documentation, 1.171 unit testing, 1.168 V&V and reviews/audits, each endorsing a matching IEEE standard with stated exceptions.
4. BTP definitions of design outputs, RTM, planning characteristics (management, implementation, resources), and functional/process product characteristics are the vocabulary later chapters use when scoring plans and products.
5. Digital sharing raises common-cause concern; staff review emphasizes software quality together with diversity and defense-in-depth.
6. ch02-ch06 carry RG staff positions and planning reviews; ch07 carries implementation and design-output acceptance plus B.4 procedures; ch08 holds the name-only standards map.
7. RG 1.152 and RG 5.71 appear only as the sources point to them for computers in safety systems, SDOE, or cyber security; full adjacent-document orientation is ch08.

## Connects To

- **ch02** - RG 1.173 life cycle processes and BTP B.2/B.3.1 planning acceptance for the nine software plans through the Software Safety Plan.
- **ch03** - RG 1.172 software requirements specifications.
- **ch04** - RG 1.169 configuration management plans and B.3.1.11 SCMP review.
- **ch05** - RG 1.168 V&V, reviews, and audits, and B.3.1.10 SVVP review.
- **ch06** - RG 1.170 test documentation, RG 1.171 unit testing, and B.3.1.12 STP review.
- **ch07** - B.3.2 implementation, B.3.3 design-output acceptance, and B.4 review procedures.
- **ch08** - name-only endorsed IEEE/IEC/IAEA map and adjacent NRC documents (including RG 1.152 Rev 4 and BTP 7-19 Rev 9).
