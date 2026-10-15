# Chapter 2: AMC 20-115D Scope and Replacement

Sources: S1 AMC 20-115D (ED Decision 2017/020/R; AMC-20 Amendment 14, consolidated in Amendment 23), sections 1 PURPOSE, 2 APPLICABILITY, 3 REPLACEMENT, lines 13-88 of `sources/text/S1.txt` (printed pp. 416-417). Exclusions: EAR footers and title banners. Name-only standards cited here by designation: ED-12C/DO-178C, ED-215/DO-330, ED-216/DO-333, ED-217/DO-332, ED-218/DO-331, ED-94C/DO-248C, ED-12B/DO-178B.

## Core Idea

AMC 20-115D is an acceptable means, not the only means, for showing compliance with airworthiness regulations on the software aspects of airborne systems and equipment. It covers product certification and European technical standard order (ETSO) authorisation. Compliance with the AMC is not mandatory; an applicant may use an alternative means of compliance (AltMoC) that meets the relevant requirements, ensures an equivalent level of software safety, and is approved by EASA on a product or ETSO article basis. The AMC replaces and cancels AMC 20-115C (12 September 2013), moving the recognised development basis to ED-12C/DO-178C and the related tool and technique supplements.

## Frameworks Introduced

- **Acceptable means with AltMoC escape.** The AMC is one path to compliance. AltMoC is available when EASA approves it for the product or ETSO article and the equivalent software-safety bar is met.
- **Recognised primary standards.** EUROCAE ED-12C and RTCA DO-178C (Software Considerations in Airborne Systems and Equipment Certification) are the primary recognised pair. ED and DO forms with matching numbers are treated as equivalent where the AMC pairs them with a shared number (the AMC's own ED-nnn/DO-nnn notation).
- **Tool and technique supplements (name-only).** ED-215/DO-330 (tool qualification), ED-216/DO-333 (formal methods), ED-217/DO-332 (object-oriented technology), and ED-218/DO-331 (model-based development and verification) sit with the primary pair. References to ED-12C/DO-178C in this AMC include those supplements as applicable.
- **Supporting clarification documents.** ED-94C and DO-248C collect FAQs and discussion papers that clarify ED-12C/DO-178C guidance; they are supporting, not primary, means.
- **Legacy-process and transition guidance (purpose-level).** The AMC establishes guidance for using existing ED-12B/DO-178B processes on new development, and for transitioning software previously approved under earlier ED-12/DO-178 editions when modifications are made. Detail of those rules lives in later chapters.
- **Audience and installation domain.** Applicants, design approval holders (DAHs), and developers of airborne systems and equipment containing software installed on type-certified aircraft, engines, and propellers, or used in ETSO articles.

## Key Concepts

- **Product certification and ETSO software.** Both product certification and ETSO authorisation sit inside the AMC's domain. Software in an ETSO article is in scope the same way as software in a type-certified installation.
- **What "recognises" means.** The AMC points at the EUROCAE/RTCA documents listed in section 1.b and does not reprint their objectives. Those documents supply life cycle process guidance; this pack names them only.
- **Supplement inclusion rule.** When the AMC says "ED-12C/DO-178C", the reference already folds in ED-215/DO-330 and the three technique supplements as they apply to the project.
- **Supporting documents versus primary.** ED-94C/DO-248C clarify the primary guidance through FAQs and discussion papers. They do not replace ED-12C/DO-178C.
- **Replacement of AMC 20-115C.** Section 3 cancels AMC 20-115C dated 12 September 2013. The D-issue purpose text adds the B-process reuse path and the transition path as visible additions over the cancelled C-issue.
- **Hardware is out of this AMC.** Applicability is software. Airborne electronic hardware questions belong to AMC 20-152A (see ch05).

## Mental Models

- Think of AMC 20-115D as the EASA door, not the development manual. The door names which industry documents are acceptable; the manuals stay paywalled and are not reproduced here.
- AltMoC is a supervised exit, not a free pass. Equivalent software safety plus EASA product/ETSO approval are required.
- Product certification and ETSO share one software AMC. Do not invent a separate ETSO-only software means inside this pack.
- "Using ED-12C/DO-178C" already means "plus applicable supplements." Plan which supplements apply before claiming the primary pair alone.

## Anti-patterns

- **Treating the AMC as mandatory law.** Section 1.a states compliance is not mandatory; AltMoC exists under the stated conditions.
- **Citing paywalled objective tables from this pack.** The AMC recognises the standard; it does not ship those tables, and neither does this chapter (see ED-12C/DO-178C, not reproduced).
- **Forgetting ETSO.** Applicability explicitly covers software used in ETSO articles, not only type-certified installations.
- **Answering the hardware question from 115D.** Hardware applicability is AMC 20-152A territory.
- **Reading "ED-12C/DO-178C" as primary-only.** Section 1.d folds tool qualification and the technique supplements into that reference as applicable.

## Key Takeaways

1. AMC 20-115D is an acceptable (not sole) means for software aspects of product certification and ETSO authorisation; AltMoC needs equivalent software safety and EASA approval on a product or ETSO article basis.
2. The AMC recognises ED-12C/DO-178C plus ED-215/DO-330 and supplements ED-216/DO-333, ED-217/DO-332, and ED-218/DO-331; ED-94C/DO-248C are supporting clarification documents.
3. References to ED-12C/DO-178C in the AMC include the tool and technique supplements as applicable.
4. The AMC applies to applicants, DAHs, and developers of software installed on type-certified aircraft, engines, and propellers, or used in ETSO articles.
5. AMC 20-115D replaces and cancels AMC 20-115C (12 September 2013) and adds purpose-level guidance for ED-12B/DO-178B process reuse and for transition of earlier-edition software.
6. Hardware applicability is outside this AMC.

## Connects To

- **ch01** - which AMC and which ED Decision answer which question; AltMoC at the pack level.
- **ch03** - how the AMC frames software life cycle processes, B-process reuse criteria, and modification/reuse of legacy software.
- **ch04** - tool qualification pointer and GM1-GM3 clarification material (CIA, coupling, error handling).
- **ch05** - AMC 20-152A scope for airborne electronic hardware (not answered here).
- **ch07** - joint software and hardware planning interfaces (PSAC-style).
