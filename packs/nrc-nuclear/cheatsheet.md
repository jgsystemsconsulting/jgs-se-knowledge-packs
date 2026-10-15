# Cheatsheet: nrc-nuclear

Decision rules for NRC software assurance questions on digital computer software in nuclear power plant safety systems. Each rule names the chapter that owns the detail; endorsed IEEE, IEC, and IAEA standards are designation-and-edition citations only.

## Which document governs my question? → ch01

- Six RGs tell applicants what to do: 1.168 V&V and reviews/audits, 1.169 CM plans, 1.170 test documentation, 1.171 unit testing, 1.172 SRS, 1.173 life cycle processes. BTP 7-14 tells reviewers what to check. (ch01)
- The RG path is acceptable, not exclusive; alternatives need adequate demonstration. (ch01)
- The SRP (NUREG-0800) is staff review guidance and imposes no new requirements. (ch01)
- Edition rule: the pack pins the July 2013 RGs and BTP 7-14 Rev 6; the plant licensing basis, not the pack, decides which revision binds. (ch01, ch08)

## Life cycle process question? → ch02

- Building life cycle processes runs on RG 1.173 / IEEE Std 1074-2006 with nuclear clarifications; compliance means every mandatory activity is present. (ch02)
- Planning acceptance criteria for the nine software plans (SMP through SSP, B.3.1.1-B.3.1.9) live here, plus the B.2 information triad. (ch02)
- Installation work-arounds, technical-specification inoperability, and the maintenance-as-development remap are ch02 rules. (ch02)
- Conformance claims must name the followed parts; "consistent with RG 1.173" alone draws a request for additional information. (ch02)

## SRS question? → ch03

- Content and qualities of the software requirements specification (RG 1.172 / IEEE Std 830-1998): bidirectional traceability, completeness with per-variable accuracy and deterministic timing, internal and external consistency, full verifiability. (ch03)
- Complex electronics requirements share the same SRS discipline. (ch03)
- SRS baselining and change control point to ch04; design-output scoring of the SRS is B.3.3.1 in ch07. (ch03, ch04, ch07)

## CM plan question? → ch04

- What an SCMP must control (RG 1.169 / IEEE Std 828-2005): identification and control of designs, code, and interfaces; documentation; vendors; qualification information; configuration audits; status accounting; build, release, and delivery. (ch04)
- B.3.1.11 staff review checks librarian ownership, breadth of controlled items, and stated test/verification of modifications. (ch04)
- Compilers and support tools are configuration items; downward adaptation is not endorsed for safety system software. (ch04)

## V&V, review, or audit question? → ch05

- V&V method (RG 1.168 / IEEE Std 1012-2004) and reviews, inspections, walkthroughs, and audits (IEEE Std 1028-2008), with integrity level 4 as the nuclear floor. (ch05)
- Independence is technical, financial, and managerial; a separate company is not required, and the licensee keeps ultimate responsibility. (ch05)
- Audits, regression analysis and testing, secure analysis, test evaluation, and user-documentation evaluation are minimum tasks even where the standard calls them optional. (ch05)
- The SVVP staff review itself is B.3.1.10 in this chapter. (ch05)

## Test documentation or unit testing question? → ch06

- Test documentation (RG 1.170 / IEEE Std 829-2008): the Master Test Plan anchors the set, documents may combine only with identity preserved, integrity level never drops, and conformance documentation is complete before implementation. (ch06)
- Unit testing (RG 1.171 / ANSI/IEEE Std 1008-1987): eight-item documentation minimum, justified coverage stronger than statement coverage, products under CM. (ch06)
- The STP staff review B.3.1.12 spans unit through installation testing, requires retest after failure and full testing after modification, and locks final system testing to V&V. (ch06)

## What do staff examine in implementation and design outputs? → ch07

- B.3.2 implementation acceptance: safety analysis, V&V, configuration management, and testing carried out as the accepted plans state, with the thread audit as the sampling method. (ch07)
- B.3.3 design-output acceptance: SRS, SAD, SDS, CL, SBDs, ICTs, OMs, SMMs, and STMs scored on functional and process characteristics, as applicable per output. (ch07)
- B.4 review procedures: plan commitment checks, sampled implementation audits, sampled design-output reviews, heavier planning emphasis for new software or unproven teams. (ch07)

## Standards lookup? → ch08

- Any IEEE, IEC, IAEA, RG 1.152, BTP 7-18, BTP 7-19, or NUREG/CR lookup: answer from ch08 with designation and edition only, and state that the standard text is outside the pack. (ch08)
- Editions are as cited by the pinned sources: IEEE 603-1991, 7-4.3.2-2003, 828-2005, 829-2008, 830-1998, 1008-1987, 1012-2004, 1028-2008, 1074-2006; IEC 60880 ed. 2.0:2006, 61513 ed. 2.0:2011, 62138 ed. 2.0:2018. (ch08)
- Framework orientation, the six-RG map, and which document answers which question: ch01. (ch01)

## Quick anchors

| Need | Answer | Chapter |
|------|--------|---------|
| Which document governs? | Six RGs build, BTP 7-14 grades; RG path acceptable, not exclusive | ch01 |
| Life cycle processes and the nine plans | RG 1.173 / IEEE Std 1074-2006; B.3.1.1-B.3.1.9 planning acceptance | ch02 |
| SRS content and qualities | RG 1.172 / IEEE Std 830-1998; bidirectional traceability, deterministic timing | ch03 |
| SCMP content and review | RG 1.169 / IEEE Std 828-2005; B.3.1.11; librarian owns versions | ch04 |
| V&V, reviews, audits | RG 1.168 / IEEE Std 1012-2004 and 1028-2008; integrity level 4; independence | ch05 |
| Test documentation and unit testing | RG 1.170 / IEEE Std 829-2008; RG 1.171 / IEEE Std 1008-1987; B.3.1.12 | ch06 |
| Implementation and design outputs | B.3.2, B.3.3, B.4; thread audit; SRS through STMs | ch07 |
| Standard designation or edition | Name-only map; text outside the pack | ch08 |

## Tells & smells

| Smell | Likely gap | Chapter |
|-------|------------|---------|
| "Consistent with RG 1.173" with no named parts | Conformance claims must identify the followed guidance | ch02 |
| Safety software assigned below integrity level 4 | Level 4 or equivalent is the floor; likelihood downgrades rejected | ch05, ch06 |
| Statement coverage claimed as complete unit testing | Licensees justify stronger module-structure criteria | ch06 |
| V&V team inside development budget or schedule | Independence is the central B.3.1.10 check | ch05 |
| CM plan listing operational code only | Designs, interfaces, documentation, vendors, tools, qualification data also controlled | ch04 |
| "Meets the intent of" without named clauses | Unverifiable; each requirement needs a constructible check | ch03, ch07 |
| Undocumented code submitted for safety use | CL review requires developer intent to be clear | ch07 |
| Installed version differs from the tested build | SBDs and ICTs lock build and configuration identity | ch07 |
| IEEE or IEC clause text in the notes | Name-only: designation and edition, text outside the pack | ch01, ch08 |
| RG 1.152 Rev 4 or BTP 7-19 Rev 9 treated as in-pack | Adjacent NRC documents are named only | ch08 |

## What this pack is not

- Not the standards: no IEEE, IEC, or IAEA text; endorsed standards are designation-and-edition citations carrying the NRC's own discussion. (ch01, ch08)
- Not the whole of SRP Chapter 7: RG 1.152 Rev 4, BTP 7-18, BTP 7-19 Rev 9, SRP Appendix 7.1-D, and other SRP sections are named only. (ch08)
- Not a source reprint: synthesized reference notes from the pinned July 2013 RGs and BTP 7-14 Rev 6; check the current NRC listing before relying on any single requirement. (ch01, ch08)
- Not licensing advice: the plant licensing basis, not this pack, decides which revision binds. (ch01)
