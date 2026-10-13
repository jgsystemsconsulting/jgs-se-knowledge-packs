# Chapter 6: AEH Objectives AMC 20-152A Adds

Sources: S2 AMC 20-152A (ED Decision 2020/010/R; AMC-20 Amendment 19, consolidated in Amendment 23), sections 5 CUSTOM DEVICE DEVELOPMENT, 6 USE OF COMMERCIAL OFF-THE-SHELF DEVICES, 7 Development Assurance of Circuit Board Assemblies (CBAs), lines 105-1256 of `sources/text/S2.txt` (printed pp. 498-515). Exclusions: EAR footers; section 8 RELATED MATERIAL and section 9 AVAILABILITY (name lists, not body). Name-only standards cited here by designation: ED-80/DO-254, ED-12C/DO-178C, ED-215/DO-330. Objective tables below are original summaries of the AMC's own CD/IP/COTS/CBA objectives, not transcribed ED-80/DO-254 appendix tables. ED-80/DO-254 Appendix A/B references that appear inside sections 5.10 and 5.11.3.6 are summarised here; this carrier has no discrete AMC Appendices A/B/C as annex files. Single Event Effects remain a name-only pointer to CRI practice / CM-AS-004 (see ch05); not fetched.

## Core Idea

Beyond recognising ED-80/DO-254, AMC 20-152A adds objectives-based guidance for three hardware areas: custom devices (PLDs, FPGAs, ASICs, including COTS IP instantiated inside them), COTS semiconductor devices, and circuit board assemblies. Each area follows the same pattern: background and applicability, then uniquely identified objectives the applicant satisfies by describing process and activities (normally in the PHAC or a related planning document). Complex custom devices take ED-80/DO-254 plus the AMC clarifications in sections 5.5 to 5.11; simple custom devices take a reduced process under CD-2 with selected clarifications still in force. COTS and CBA objectives close the gaps the standard leaves when design data is unavailable or when boards integrate complex parts. This chapter summarises those AMC objectives as original notes. It does not reprint ED-80/DO-254 life-cycle data or appendix tables (see ED-80/DO-254, not reproduced).

## Frameworks Introduced

- **Custom device scope (section 5).** Digital or mixed-signal custom devices (PLD/FPGA/ASIC, ED-80/DO-254 "custom micro-coded components") contributing to hardware DAL A, B, or C. The AMC recognises ED-80/DO-254 Appendix A for modulating life-cycle data by hardware DAL.
- **Simple versus complex split (section 5.2, CD-1).** Simple only when a technical assessment of design content supports full deterministic test-and-analysis verification under all foreseeable operating conditions with no anomalous behaviour. Criteria include function count and simplicity, interface count and simplicity, data/signal processing simplicity, block independence, and digital-specific factors (synchronous vs asynchronous, independent clocks, state-machine count/size/independence). An assembly of simple items may itself be complex. CD-1 records DAL, classification, and simple-classification justification in the PHAC.
- **Complex path (section 5.3).** Satisfy ED-80/DO-254 plus AMC objectives/clarifications in sections 5.5 to 5.11.
- **Simple path (section 5.4, CD-2).** Reduced life-cycle data is expected. CD-2 requires a planned process covering function definition, complete verification by tests and analyses, configuration management (including problem reporting and reproduction instructions), and build-conformance assessment. Sections 5.5.2.4 and 5.5.2.5 still apply to verification. Tool use pulls in section 5.8; PDH reuse pulls in ED-80/DO-254 Section 11.1 and section 5.9; COTS IP pulls in section 5.11. Simple-device life-cycle data may be combined with other hardware data.
- **Validation and verification clarifications (section 5.5, CD-3 to CD-7).** Validate all custom-device requirements (derived and non-derived) per the recognised standard's validation process; DAL A/B validation with independence (Appendix A of the standard names acceptable independence means). Detailed-design review and traceability at DAL A/B; design-standard satisfaction at DAL C. Tool-report review when tools convert detailed design to physical implementation. Verification-case/procedure review for correct and complete requirement coverage. Timing performance verification across temperature, supply, and fabrication-process variation (static timing analysis is one accepted means for digital parts).
- **Abnormal and boundary conditions (section 5.6, CD-8).** For DAL A or B, define abnormal and boundary conditions and expected behaviour as requirements.
- **HDL code coverage (section 5.7, CD-9).** When HDL code coverage supports elemental analysis (ED-80/DO-254 Appendix B Section 3.3.1) at DAL A/B, plan detailed coverage criteria over the HDL elements used; analyse and justify non-covered cases. Coverage may need complementary analysis for items the metric cannot reach (common with some COTS IP instantiations).
- **Tool assessment clarifications (section 5.8, CD-10, CD-11).** Builds on the standard's tool-assessment flow: identify tool and revision/environment; identify the process purpose the tool supports; independent assessment of tool output when claimed (CD-10) with coverage justified against the design/implementation or verification objectives the tool satisfies; code-coverage tools used only to show code was exercised by requirements-based testing keep the elemental-analysis exclusion, but tools that auto-generate tests and use coverage to declare requirements verification complete are verification tools; relevant history needs credible supporting data (CD-11) and is not a stand-alone qualification means for design tools; ED-12C/DO-178C and ED-215/DO-330 may also be used for design-tool qualification guidance (name-only).
- **Previously developed hardware (section 5.9, CD-12).** Reuse PDH under ED-80/DO-254 Section 11.1. Assess whether prior compliance is compromised by modification (including obsolescence), by change of function/use/higher failure-condition classification, or by design-environment change. Any of the three can invalidate prior credit; upgrade per the assessment and apply applicable AMC objectives. Document results in the PHAC.
- **ED-80/DO-254 Appendix A clarifications (section 5.10).** In-body corrections to life-cycle data classification rows (see appendix summary below); Top-Level Drawing maps to a Hardware Configuration Index (HCI) that identifies configuration, embedded logic, and life-cycle data, and includes or references the hardware life-cycle environment / HECI so the device can be replicated.
- **COTS IP in custom devices (section 5.11, IP-1 to IP-7).** Soft/Firm/Hard commercial IP inserted into a custom device (digital, analogue, mixed-signal) at DAL A/B/C. Hard IP already manufactured into FPGA/PLD silicon is a COTS-device matter (section 6), not section 5.11. Assurance follows IP category and design-error risk through selection, provider/data assessment, complementary assurance, three-layer verification strategy, planning, requirements/validation, verification inside the custom-device process, and Appendix B considerations at DAL A/B.
- **COTS devices (section 6, COTS-1 to COTS-8).** Digital, hybrid, and mixed-signal COTS semiconductors at DAL A/B/C (limited set at DAL C). Also the COTS portion of FPGA/PLD devices that embed Hard IP in manufactured silicon. Section 6.4 objectives apply to devices classified complex under section 6.3. ECMP, errata, failure modes, usage/configuration, unused-function isolation, and critical-configuration-setting protection are the AMC additions over ED-80/DO-254 Section 11.2.
- **Circuit board assemblies (section 7, CBA-1).** CBAs (board or board set) at DAL A/B/C that contain complex custom or complex COTS devices need a development process with requirements capture, validation, verification, configuration management, and requirement flow-down so the CBA performs its intended function. May be defined with the equipment process when relevant.

## Key Concepts

### Original summary: custom-device objectives (CD-1 to CD-12)

| ID | Focus | DAL notes (original summary) |
|----|-------|------------------------------|
| CD-1 | Record DAL, simple/complex class, and simple justification in PHAC | All custom devices in scope |
| CD-2 | Simple-device process: functions, complete verification, CM/reproduction, build conformance; 5.5.2.4-5 still apply; tools/PDH/COTS IP pull their sections | Simple path |
| CD-3 | Validate all requirements (derived and non-derived) per recognised validation process; independence at DAL A/B | Independence A/B |
| CD-4 | Detailed-design review vs standards and vs requirements/trace (A/B); design-standard satisfaction (C) | Split A/B vs C |
| CD-5 | Review synthesis / place-and-route (or similar) tool reports when tools produce the physical implementation | Tool-using flows |
| CD-6 | Review each verification case/procedure for appropriateness and complete requirement coverage | All applicable |
| CD-7 | Verify timing across temperature, supply, and fab-process variation (STA is one digital means) | All applicable |
| CD-8 | Capture abnormal/boundary conditions and expected behaviour as requirements | A/B only |
| CD-9 | Plan HDL coverage criteria for elemental analysis; justify gaps; complement where coverage cannot reach | A/B when used for Appendix B elemental analysis |
| CD-10 | Independent tool-output assessment with justified coverage of the objectives the tool supports | When independent assessment is claimed |
| CD-11 | Credible, relevant tool history data when history credit is claimed; history is not stand-alone for design tools | When history credit is claimed |
| CD-12 | PDH reuse under recognised Section 11.1; assess modification, use/FCC change, environment change; upgrade when credit breaks | PDH reuse |

Exact objective wording is in the AMC; use the official text for a certification decision. Paywalled standard objectives stay behind `see ED-80/DO-254, not reproduced`.

### Original summary: COTS IP objectives (IP-1 to IP-7)

| ID | Focus | Notes (original summary) |
|----|-------|--------------------------|
| IP-1 | Select acceptable IP: technical fit; architecture/modes/config and source-format understanding; data quality for integration/verification; physical-implementation info; intended-function demonstration | Selection gate |
| IP-2 | Assess provider and IP data: integration/implementation info; documented options/scale; trustworthy verification covering the applicant use case; errata/limitations feed; service experience for the use case | Provider/data gate |
| IP-3 | If IP-2 items 1, 2, 4, or 5 are incomplete from provider data, define complementary ED-80/DO-254-based assurance for the gaps (item 3 feeds the verification strategy) | Gap mitigation |
| IP-4 | Verification strategy covering (1) IP itself vs IP-2 item 3 risk, (2) IP after applicant design steps, (3) integrated IP in the custom device; provider tests and standard vectors may contribute; used functions minimum; unused functions disabled without interference | Three-layer verify |
| IP-5 | PHAC approach: IP identity/version/source-format and integration point; function summary; process for section 5.11.3 objectives; design-integration/usage process; tool assessment when tools design or verify the IP | Planning |
| IP-6 | Capture allocated IP-function requirements commensurate with the verification strategy; derived requirements for used functions/config, unused-function deactivation, and correct control per provider data; full ED-80/DO-254 capture if strategy is requirements-based testing only; validate with the custom device | Requirements/validation |
| IP-7 | For IP in DAL A/B hardware, satisfy ED-80/DO-254 Appendix B; safety-specific analysis may identify safety-sensitive IP portions and needed extra requirements, design features, and verification, fed back to the process | Appendix B at A/B |

IP verification execution (section 5.11.3.5) sits inside the overall custom-device verification process per the recognised standard and the planned strategy; there is no separate IP verification objective beyond that path.

### Original summary: COTS device objectives (COTS-1 to COTS-8)

| ID | Focus | Notes (original summary) |
|----|-------|--------------------------|
| COTS-1 | Classify relevant devices under section 6.3 complexity criteria; document list and rationale in PHAC (not the whole bill of materials; boundary simple claims need rationale) | Complexity gate |
| COTS-2 | ECMP for selection, qualification, configuration management, and access to manuals/datasheet/errata/change data; at DAL A/B, complex selection considers maturity and mitigates identified risks; industry ECMP standards may support (see appendix summary) | ECMP |
| COTS-3 | If used outside manufacturer specification limits, establish reliability and technical suitability in the intended application | Off-datasheet use |
| COTS-4 | If embedded microcode is unqualified by the manufacturer or is modified by the applicant, propose a means of compliance in the appropriate process (hardware, software, or system), commensurate with use; PHAC notes existence and owning process | Microcode |
| COTS-5 | Assess errata relevant to the intended use; identify and verify mitigations; non-hardware mitigations feed the owning process | Errata |
| COTS-6 | Identify failure modes of used functions and possible common modes; feed system safety assessment | Safety feed |
| COTS-7 | Define and verify usage against the hardware intended function, including HW/SW and HW/HW interfaces; at DAL A/B, show unused functions do not compromise used-function integrity/availability (deactivation recommended when available) | Usage/interfaces |
| COTS-8 | At DAL A/B, develop and verify mitigation for inadvertent alteration of critical configuration settings (hardware, software, system, or combination; may come from safety assessment) | Critical config |

Section 6.3 complexity (original summary): a COTS device is complex when it has multiple interacting functional elements, a significant number of functional modes, and configurability that yields different data/signal flows and resource sharing; or when it contains advanced data processing, advanced switching, or multiple processing elements (for example multicore, graphics, networking, complex bus switching, multi-master interconnect fabrics). Completely verifying all configurations of a complex COTS device is treated as impractical.

### Original summary: CBA objective

| ID | Focus | Notes (original summary) |
|----|-------|--------------------------|
| CBA-1 | Process for CBAs that contain complex custom or complex COTS devices: requirements capture, validation, verification, configuration management, and requirement flow-down so the CBA performs its intended function; may share the equipment process | DAL A/B/C CBAs in scope |

### Appendix-related content in this carrier (summary, not transcription)

This EAR slice does not ship discrete AMC Appendices A, B, or C as separate annex files. Appendix material appears only as in-body references; original summary of what the slice actually carries:

- **ED-80/DO-254 Appendix A (life-cycle data by DAL).** Recognised for modulating custom-device life-cycle data by hardware DAL (section 5.1). Also referenced for acceptable independence means (CD-3 note). Section 5.10 clarifies selected Table A-1 rows: Hardware Process Assurance Plan also HC2 at Level C; Hardware Design Standard (including HDL coding standards) also HC2 at Level C; Detailed Design Data HC1 at Levels A, B, and C; Hardware Review and Analysis Procedures also HC2 at Level C. Top-Level Drawing corresponds to an HCI (and HECI reference) that fully identifies configuration, embedded logic, life-cycle data, and the life-cycle environment for replication. Exact table cells stay in the paywalled standard (`see ED-80/DO-254, not reproduced`).
- **ED-80/DO-254 Appendix B (design assurance for DAL A/B elemental methods).** HDL code coverage is recognised as one elemental-analysis method (section 5.7 / CD-9), with planned criteria and gap justification. For COTS IP at DAL A/B, Appendix B still applies even when code coverage cannot reach IP internals; safety-specific analysis is an accepted alternative path (section 5.11.3.6 / IP-7) that finds safety-sensitive IP portions and feeds extra requirements, design features, and verification back into the process.
- **AMC "Appendix B" / "GM Appendix" name-checks inside objectives.** COTS-2 and CBA-1 point at additional ECMP or CBA information under an Appendix B label in the AMC text; COTS-1 points at classification examples in a GM Appendix. Those supporting illustrations are not present as discrete annex body in this carrier, so this pack records the pointer only and does not invent appendix prose.
- **Glossary Appendix A name-check.** Soft/Firm/Hard IP definitions and the commercial-IP scope note point at an Appendix A glossary in the AMC; definitions used above follow the in-body section 5.11 text rather than a missing annex dump.

### SEE (name-only)

Single Event Effects stay outside AMC 20-152A body scope (ch05). No SEE objective appears in sections 5-7. Keep the pointer at CRI practice / CM-AS-004; do not fetch that document from this pack.

## Mental Models

- Three racks hang on the ED-80/DO-254 door: custom/IP (CD + IP), COTS device (COTS), and board (CBA). Most certification arguments pick a rack per part, then show process evidence against each ID.
- Simple is earned by verifiability, not by hope. If you cannot fully test and analyse the device under all foreseeable conditions, it is complex, even when every block looked simple alone.
- COTS IP is not free assurance. Selection and provider assessment (IP-1/IP-2) decide how much complementary work (IP-3) and how wide the three-layer verification net (IP-4) must be.
- Complex COTS is a usage-and-management problem more than a redesign-the-silicon problem: ECMP, errata, failure-mode feed, configuration control, unused-function isolation, critical-setting protection.
- The CBA process is the requirement spine that makes device-level assurance add up at board level. Without flow-down, CD and COTS evidence float.
- Appendix references in this chapter are signposts into ED-80/DO-254 or into AMC supporting labels, not a licence to paste paywalled tables into plans or into this pack.

## Anti-patterns

- **Running the full complex custom stack on a device that truly meets simple criteria, or the reverse: calling a device simple without CD-1 justification.** Classification is evidence-based (section 5.2).
- **Dropping COTS IP in without IP-1/IP-2 and a written IP-4 strategy.** Provider marketing is not verification.
- **Claiming elemental analysis via HDL coverage without planned criteria, gap justification, or complementary analysis for unreachable IP.** CD-9 and IP-7 exist for those gaps.
- **Using tool history as the sole design-tool qualification story.** CD-11 and the section 5.8 design-tool note reject stand-alone history.
- **Reusing PDH after modification, use/FCC change, or environment change without a Section 11.1-style assessment.** CD-12 treats any of the three as potential credit breakers.
- **Ignoring errata, unused functions, or critical configuration settings on complex COTS at DAL A/B.** COTS-5, COTS-7, and COTS-8 are the usual finding sources.
- **Treating board integration as pure manufacturing with no CBA requirements path when complex devices sit on the board.** CBA-1 expects capture, validation, verification, CM, and flow-down.
- **Transcribing ED-80/DO-254 Appendix A/B tables into this pack or into applicant notes sourced from this pack.** Summaries above are original; official cells stay in the standard (`see ED-80/DO-254, not reproduced`).
- **Fetching CM-AS-004 or expanding SEE into fake AMC objectives.** SEE stays name-only.

## Key Takeaways

1. AMC 20-152A adds AMC-owned objectives for custom devices (CD-1 to CD-12), COTS IP inside them (IP-1 to IP-7), complex COTS devices (COTS-1 to COTS-8), and CBAs with complex devices (CBA-1); the applicant describes process and activities, typically in the PHAC.
2. Complex custom devices satisfy ED-80/DO-254 plus sections 5.5-5.11; simple custom devices follow CD-2 with selected clarifications still mandatory when tools, PDH, or COTS IP apply.
3. COTS IP assurance is risk-based: select and assess (IP-1/IP-2), mitigate provider gaps (IP-3), verify at IP, post-implementation, and integrated layers (IP-4), plan and capture requirements (IP-5/IP-6), and meet Appendix B expectations at DAL A/B (IP-7).
4. Complex COTS work centres on ECMP, off-spec use justification, microcode ownership, errata mitigation, safety-failure feed, defined/verified usage including interfaces, unused-function isolation, and critical-configuration protection.
5. CBAs that host complex custom or complex COTS devices need an explicit development process with requirement flow-down (CBA-1).
6. ED-80/DO-254 Appendix A/B content appears in this carrier only as in-body references and section 5.10/5.11.3.6 clarifications; discrete AMC Appendices A/B/C are absent here and are not invented. Objective tables in this chapter are original summaries.
7. SEE is not given objectives in sections 5-7; keep the ch05 name-only pointer.

## Connects To

- **ch05** - AMC 20-152A purpose, applicability (DAL A-C, DAL D not required), recognition-plus-supplementation frame, objective ID scheme, SEE out-of-scope rule.
- **ch02-ch04** - software-side AMC 20-115D material; not a substitute for these hardware objectives.
- **ch07** - PHAC/PSAC-style joint planning interfaces, including hardware/software interface data and SEE considerations recorded in planning documents.
- **faa-8110-49** - FAA-side twin material where AC 20-152A matters; not a substitute for this AMC text.
