# Chapter 1: Means-of-Compliance Map

Sources: S5 ED Decision 2017/020/R of 19 October 2017 (decision number and date anchor, lines 1-40 of `sources/text/S5.txt`); S6 ED Decision 2020/010/R of 17 July 2020 (decision number and date anchor, lines 1-40 of `sources/text/S6.txt`); S1 AMC 20-115D opening sections 1-2 (EAR pp. 416-417 cite, lines 13-83 of `sources/text/S1.txt`); S2 AMC 20-152A opening sections 1-2 (EAR pp. 497-498 cite, lines 13-70 of `sources/text/S2.txt`). Cite-only orientation chapter: does not own body pages (body ownership is ch02-ch06). Exclusions: EAR footers and title banners; S5/S6 instrument bodies beyond number and date (not paraphrased as AMC content); S7 and bulk AMC-20 outside the two sections. Name-only standards cited here by designation: ED-12C/DO-178C and supplements, ED-80/DO-254. Name-only pointer: AMC 20-193 (multi-core) to the glossary, not fetched.

## Core Idea

Two EASA Executive Director Decisions anchor the pack's means of compliance. **ED Decision 2017/020/R of 19 October 2017** issued AMC-20 Amendment 14 and carries AMC 20-115D (airborne software development assurance using EUROCAE ED-12 and RTCA DO-178). **ED Decision 2020/010/R of 17 July 2020** issued AMC-20 Amendment 19 and carries AMC 20-152A (airborne electronic hardware). Both AMC sections now sit consolidated in AMC-20 Amendment 23 as read from the June 2023 Easy Access Rules compilation. Each AMC is an acceptable means, not the only means: compliance is not mandatory, and an applicant may use an alternative means of compliance (AltMoC) that meets the relevant requirements, ensures an equivalent level of safety (software safety on the 115D side), and is approved by EASA on a product or ETSO article basis. The free-to-read AMC layer points at paywalled industry standards it does not reprint.

## Frameworks Introduced

- **Decision anchors (cite, not paraphrase as AMC).** ED Decision 2017/020/R (19 October 2017) names the software AMC path; ED Decision 2020/010/R (17 July 2020) names the hardware AMC path. This chapter records number and date only. The AMC body text lives in the EAR slices owned by later chapters, not in a rewrite of the decision instruments.
- **Two AMC doors, one pack.** AMC 20-115D answers software aspects of product certification and ETSO authorisation. AMC 20-152A answers electronic hardware aspects for the same audience domains. Wrong door yields the wrong recognition set.
- **Free versus paywalled split.** EASA publishes the AMC text in the Easy Access Rules AMC-20 volume (free to read in the compilation used here). The development standards the AMCs recognise (ED-12C/DO-178C plus supplements; ED-80/DO-254) are paywalled industry documents. This pack restates what the AMCs themselves say and names those standards only (see avionics-signpost). It does not ship objective tables from the paywalled set.
- **AltMoC as supervised escape.** Both openings state the AMC is acceptable but not sole. AltMoC must meet the relevant requirements, ensure equivalent safety (equivalent software safety under 115D), and receive EASA approval on a product or ETSO article basis. AltMoC is not a free pass around the safety bar.
- **Acceptable means are non-binding.** The decision-anchor whereas clauses treat acceptable means of compliance as non-binding standards that may be used to demonstrate compliance; when they are complied with, the related requirements are met. That framing supports the AltMoC exit rather than mandatory AMC use.
- **ETSO shares the doors.** Both openings put ETSO authorisation beside product certification. Software in ETSO articles and AEH in ETSO articles stay inside their respective AMC, not outside in a separate ETSO-only means invented by this pack.
- **Recognition is a pointer.** 115D recognises ED-12C/DO-178C (with tool and technique supplements as applicable) and supporting ED-94C/DO-248C. 152A recognises ED-80/DO-254 and then supplements them with AMC-owned objectives for custom devices, COTS IP, COTS devices, and CBAs (detail in ch05-ch06).

## Key Concepts

- **Which instrument answers which question.**
  - Software development assurance under EASA AMC → AMC 20-115D (decision 2017/020/R; body ch02-ch04).
  - Airborne electronic hardware under EASA AMC → AMC 20-152A (decision 2020/010/R; body ch05-ch06).
  - Which decision issued which AMC amendment → this chapter's anchors only.
  - Joint software and hardware planning interfaces → ch07 (PSAC/PHAC-style).
  - Paywalled standard designations and purchase orientation → avionics-signpost (no standard text here).
  - FAA twin material → faa-8110-49 (not a substitute for these AMC sections).
- **What "consolidated in Amendment 23" means here.** The pinned read is the two AMC sections as they appear in the June 2023 EAR AMC-20 compilation. Later AMC-20 amendments are outside this pack's freeze.
- **What this chapter does not own.** Body pages of AMC 20-115D and AMC 20-152A belong to ch02-ch06. Related-material name lists, availability sections, and bulk AMC-20 outside the two sections (including S7) are exclusions, not chapter bodies.
- **AMC 20-193 (multi-core).** Name-only signpost to the pack glossary; not fetched and not a section in this release.
- **Audience shared shape.** Applicants, design approval holders, and developers of airborne systems and equipment: software installed on type-certified aircraft, engines, and propellers or used in ETSO articles (115D); AEH on the same installation domain including ETSO article developers (152A).

## Mental Models

- Two labelled doors on one building. Software questions go through 115D; hardware questions go through 152A. The building directory is this map; the room contents are later chapters.
- Free AMC layer, paywalled standard layer. If a sentence needs an objective table from ED-12C/DO-178C or ED-80/DO-254, buy the standard; do not expect it from this pack.
- Decision number and date are the legal pegs; the AMC section text is the means description. Do not treat a paraphrase of S5/S6 as if it were the AMC body.
- AltMoC is a supervised side exit with three locks: relevant requirements, equivalent safety, EASA product or ETSO approval.
- ETSO is inside both doors, not a third door.

## Anti-patterns

- **Treating either AMC as mandatory law.** Both openings state compliance is not mandatory; AltMoC exists under the stated conditions.
- **Paraphrasing ED Decision 2017/020/R or 2020/010/R as if they were the AMC text.** Cite number and date; read AMC body in ch02-ch06.
- **Answering hardware from 115D or software from 152A.** Wrong door.
- **Reproducing paywalled ED/DO objective tables from this pack.** Recognition is a pointer (see ED-12C/DO-178C and ED-80/DO-254, not reproduced).
- **Expanding S7 or bulk AMC-20 into this pack.** Scope is the two AMC sections and their GM material only.
- **Fetching AMC 20-193 into a chapter body.** Keep it as a one-line glossary signpost.
- **Inventing a separate ETSO-only software or hardware means.** Both openings already cover ETSO authorisation.

## Key Takeaways

1. **ED Decision 2017/020/R of 19 October 2017** anchors AMC 20-115D (software); **ED Decision 2020/010/R of 17 July 2020** anchors AMC 20-152A (AEH); both appear consolidated in AMC-20 Amendment 23 as pinned from the June 2023 EAR compilation.
2. Each AMC is an acceptable means, not the only means; AltMoC needs relevant requirements met, equivalent safety (equivalent software safety on the 115D side), and EASA approval on a product or ETSO article basis.
3. Free-to-read AMC text in Easy Access Rules points at paywalled ED/DO standards this pack names only and does not reprint.
4. Software questions → ch02-ch04 under AMC 20-115D; hardware questions → ch05-ch06 under AMC 20-152A; joint planning interfaces → ch07.
5. Product certification and ETSO authorisation share each AMC's domain; do not invent a third ETSO-only door.
6. AMC 20-193 (multi-core) is a name-only glossary signpost in this release, not a fetched section.
7. This chapter is cite-only orientation; it does not own AMC body pages.

## Connects To

- **ch02** - AMC 20-115D purpose, applicability, and replacement of AMC 20-115C.
- **ch03** - software life cycle assurance as AMC 20-115D frames it.
- **ch04** - tool qualification pointer and GM1-GM3 clarifications.
- **ch05** - AMC 20-152A purpose, applicability, DAL coverage, and background.
- **ch06** - AEH objectives AMC 20-152A adds (custom devices, COTS IP, COTS, CBAs).
- **ch07** - joint software and hardware certification workflow (PSAC/PHAC-style).
- **faa-8110-49** - FAA-side twin recognition material; not a substitute for these AMC sections.
- **avionics-signpost** - paywalled RTCA/EUROCAE designations and where to obtain them (no standard text here).
