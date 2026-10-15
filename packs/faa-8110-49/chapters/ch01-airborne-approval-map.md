# Chapter 1 - Airborne Approval Map

Sources: FAA Order 8110.49A, Software Approval Guidelines (effective 2018-03-29), Chapter 1 paragraphs 1-6 (printed pages 1-1 to 1-2); AC 20-115D, Airborne Software Development Assurance Using EUROCAE ED-12( ) and RTCA DO-178( ) (2017-07-21), sections 1-3 (purpose, recognition set, applicability, cancellation); AC 20-152A, Development Assurance for Airborne Electronic Hardware (2022-10-07), sections 1-3 (purpose, ED-80/DO-254 recognition, applicability, cancellation). Orientation chapter across all three pinned sources; detailed objectives live in later chapters.

## Core Idea

Three public FAA documents split the airborne software and electronic hardware approval problem. Order 8110.49A tells FAA certification staff how to run software reviews and software conformity when the applicant's means of compliance is DO-178B or DO-178C. AC 20-115D is the applicant-facing recognition instrument for software development assurance (ED-12C/DO-178C and companions, with gated DO-178B process reuse). AC 20-152A is the applicant-facing recognition instrument for airborne electronic hardware (ED-80/DO-254, plus objectives for custom devices, COTS IP, COTS devices, and CBAs). None of these documents is itself the RTCA or EUROCAE standard; each points at paywalled industry documents that this pack names only (see avionics-signpost).

## Frameworks Introduced

- **Document roles.**
  - **8110.49A** = internal FAA software approval guidelines (reviews, LOI context, conformity inspection). Audience: AIR offices and designees.
  - **AC 20-115D** = acceptable means for software aspects of type certification or TSO authorization. Audience: applicants, design approval holders, developers of airborne software-bearing systems and TSO articles.
  - **AC 20-152A** = acceptable means for electronic hardware aspects of type certification or TSO authorization. Audience: applicants, design approval holders, developers of AEH-bearing systems and TSO articles.

- **Recognition chain.** FAA Advisory Circular (acceptable means) → names EUROCAE ED / RTCA DO pair as equivalent → applicant satisfies the industry document's objectives, activities, and evidence, plus any AC-added objectives or transition rules. The AC does not reprint the standard.

- **Software recognition set (AC 20-115D section 1.b).** ED-12C/DO-178C (software); ED-215/DO-330 (tool qualification); ED-218/DO-331 (model-based development and verification); ED-217/DO-332 (object-oriented technology); ED-216/DO-333 (formal methods). Supporting FAQs/discussion: ED-94C/DO-248C (not themselves the means of compliance). References to DO-178C in the AC include the tool document and supplements as applicable.

- **Hardware recognition pair (AC 20-152A section 1).** ED-80 (April 2000) / DO-254 (19 April 2000), treated as equivalent. The AC states when to apply them and supplements them with objectives for custom devices (including COTS IP), COTS devices, and CBAs.

- **8110.49 Chg 2 → 8110.49A history.** Order 8110.49A (2018-03-29) cancels and supersedes Order 8110.49 Chg 2 (2017-04-10). Chapters 5-16 from Chg 2 were deleted to remove duplication or conflict; those topics moved to AC 20-115D, to AC 00-69, or were removed. What remains in the order is the software review process (chapter 2), reserved chapter 3, software conformity inspection (chapter 4), and LOI worksheets (Appendix A). AC 00-69 is now in this pack (ch11-ch13); it holds three best-practice blocks, not the deleted order chapters.

## Key Concepts

### Which document answers which question

| Question | Go to | Pack chapter |
|---|---|---|
| How should FAA staff plan and run software reviews (desk vs on-site, arrangements, review objectives)? | Order 8110.49A Ch 2 | ch02 |
| How is level of FAA involvement (LOI) sized and scored? | Order 8110.49A Ch 2 para 2.b + App A | ch03 |
| How do software part and installation conformity inspections work (ASE/ASI, Form 8120-10)? | Order 8110.49A Ch 4 | ch04 |
| What software standards does the FAA recognize, and when may DO-178B processes continue for new development? | AC 20-115D secs 1-6 | ch05 |
| How do tools transition to DO-330 / TQLs? | AC 20-115D sec 10 | ch05 |
| Supplements, field-loadable software, user-modifiable software, legacy software modification flow? | AC 20-115D secs 8-9 | ch06 |
| What AEH standard is recognized, and how are custom devices classified simple vs complex? | AC 20-152A secs 1-5.5 | ch07 |
| AEH robustness, HDL code coverage, tool assessment, PDH, Appendix A data clarifications? | AC 20-152A secs 5.6-5.10 | ch08 |
| COTS IP inside custom devices? | AC 20-152A sec 5.11 | ch09 |
| Complex COTS semiconductor devices and CBA development assurance? | AC 20-152A secs 6-7 | ch10 |
| Best-practice companion notes for DO-254 users (named, not unpacked here)? | AC 00-72 | outside this pack |
| Best-practice notes on change impact analysis, data and control coupling, and design-level error handling? | AC 00-69 | ch11, ch12, ch13 |
| Designations, editions, and purchase points for paywalled RTCA/EUROCAE/SAE standards? | avionics-signpost pack | signpost |

### Order 8110.49A in one page

- Purpose: guide AIR offices and designees applying RTCA/DO-178B and DO-178C (including applicable supplements and DO-330 when the order says "DO-178C") on TC, STC, ATC, ASTC, and TSOA projects.
- Assumes DO-178B/C is the proposed means of compliance; other means need additional policy project-by-project.
- Topics retained: software review process; software conformity inspections. LOI worksheets support early involvement sizing.
- Related publications list points at AC 20-115 (software AC family), production and system-safety ACs, and the RTCA documents themselves (purchase from RTCA; not reproduced here).

### AC 20-115D in one page

- Acceptable means, not the only means, not a regulation; if used, follow in all applicable respects.
- Recognizes the DO-178C stack listed above; cancels AC 20-115C (2013-07-19).
- Establishes gated reuse of existing DO-178B processes for new development, and transition rules when modifying software previously approved under older DO-178 generations (details in ch05-ch06).
- Technical content harmonized as far as practicable with EASA AMC 20-115D (named only; this pack does not restate EASA text).

### AC 20-152A in one page

- Acceptable means for electronic hardware aspects; same "if you use it, follow it" discipline; contents do not have the force and effect of law.
- Recognizes ED-80/DO-254; cancels AC 20-152 (2005-06-30).
- Applies to AEH contributing to hardware DAL A, B, or C; not required for DAL D (AC 00-72 may still help).
- Adds objective families CD-i, IP-i, COTS-i, CBA-i; PHAC (or related plans) records how objectives will be met and is submitted for certification.
- Does not address Single Event Effects assessment (PHAC may still note SEE considerations).

### Cancellations and migrations (history map)

| Retired text | Disposition |
|---|---|
| Order 8110.49 Chg 2 entire order | Superseded by 8110.49A (2018-03-29) |
| Order 8110.49 Chg 2 Chapters 5-16 | Deleted; topics now in AC 20-115D, AC 00-69, or removed (AC 00-69 reconstructed in ch11-ch13) |
| AC 20-115C (2013-07-19) | Cancelled by AC 20-115D |
| AC 20-152 (2005-06-30) | Cancelled by AC 20-152A |

Practical reading rule: do not cite Chg 2 chapters 5-16 as current FAA order material. For software development assurance substance, use AC 20-115D; for AEH, use AC 20-152A; for staff review/conformity procedure, use 8110.49A chapters 2 and 4 plus Appendix A.

### What this pack deliberately does not contain

- No verbatim RTCA DO-178C, DO-254, DO-330 to DO-333, EUROCAE ED-12C, ED-80, ED-215 to ED-218, or SAE ARP4754B/ARP4761A text. Those works are copyrighted and paywalled. Designations and where-to-buy orientation live in the **avionics-signpost** pack.
- No DO-178C Annex A objective tables and no DO-254 life cycle data tables beyond the AC's own clarifications.
- No EASA AMC 20-115D or AMC 20-152A body text. Those questions go to easa-rules. AC 00-69 themes parallel the EASA GM1-GM3 split; this pack does not import that text.
- Guidance is not regulation. Alternate means remain possible when the FAA accepts them.

## Mental Models

- Staff procedure versus applicant means: 8110.49A is how the FAA runs the liaison and conformity machine; the two ACs are how applicants claim software or hardware development assurance.
- Recognition is a pointer, not a paste. If a sentence smells like an objective table from DO-178C or DO-254, it belongs in the purchased standard, not in these notes.
- History folded the old fat order into thin order + fat ACs. When a tribal-knowledge citation says "8110.49 chapter 12," translate through the Chg 2 deletion note before trusting it.
- Software stack and hardware stack are parallel: AC names ED/DO pair, adds transition or clarification objectives, demands plans (PSAC-class on the software side; PHAC on the hardware side).
- Signpost first when you need the standard itself. This pack answers FAA guidance questions; the signpost answers "which edition do I buy."

## Anti-patterns

- **Using Order 8110.49A as the software development standard.** It assumes DO-178B/C and teaches FAA review/conformity; it does not replace AC 20-115D or DO-178C.
- **Using AC 20-115D for AEH, or AC 20-152A for airborne software.** Wrong recognition instrument.
- **Citing deleted Chg 2 chapters 5-16 as live order content.** 8110.49A section 5 moved that material to AC 20-115D, AC 00-69, or removal.
- **Treating an AC as mandatory regulation.** Both ACs state they are acceptable means, not the only means (20-152A also states it does not bind the public as law).
- **Copying paywalled DO/ED objective tables into project paperwork from this pack.** The pack carries none; buy and use the standard (avionics-signpost for designations).
- **Ignoring DAL/software-level limits.** 20-152A is not required at hardware DAL D; 20-115D life cycle data expectations still vary by software level (see ch05).

## Key Takeaways

1. **8110.49A** = FAA staff software review and conformity guidelines under DO-178B/C; **AC 20-115D** = software development assurance recognition and transition; **AC 20-152A** = AEH/DO-254 recognition and hardware objectives.
2. Recognition chain runs FAA AC → equivalent EUROCAE ED / RTCA DO document → applicant evidence against that document (plus AC objectives). Paywalled standards are named only; use **avionics-signpost** for designations and purchase orientation.
3. 8110.49A cancelled Chg 2; Chg 2 chapters 5-16 were deleted because AC 20-115D, AC 00-69, or removal now owns those topics. Remaining order substance is chapters 2 and 4 plus Appendix A LOI worksheets.
4. AC 20-115D cancels AC 20-115C and recognizes the DO-178C + DO-330 + DO-331/332/333 set; AC 20-152A cancels AC 20-152 and recognizes ED-80/DO-254 with CD/IP/COTS/CBA objectives for DAL A/B/C AEH.
5. Read ch02-ch04 for FAA review machinery, ch05-ch06 for software assurance, ch07-ch10 for AEH; keep ACs and the order as guidance under 14 CFR, not as substitutes for the certification basis or the industry standards.

## Connects To

- **ch02** - software review process (Order 8110.49A Ch 2).
- **ch03** - LOI criteria and Appendix A worksheets.
- **ch04** - software conformity inspection.
- **ch05** - AC 20-115D recognition, DO-178B reuse gates, life cycle data, tool transition.
- **ch06** - supplements, FLS, UMS, legacy software modification flow.
- **ch07** - AC 20-152A custom devices, simple/complex classification, CD-1 to CD-7.
- **ch08** - AEH robustness, HDL coverage, tools, PDH, Appendix A clarifications.
- **ch09** - COTS IP in custom devices.
- **ch10** - COTS devices and circuit board assemblies.
- **ch11** - AC 00-69 change impact analysis best practices.
- **ch12** - AC 00-69 data and control coupling practices.
- **ch13** - AC 00-69 design-level error handling.
- **avionics-signpost** - paywalled RTCA/EUROCAE/SAE designations and where to obtain them (no standard text here).
