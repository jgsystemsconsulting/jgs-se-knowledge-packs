# Chapter 10 - COTS Devices and Circuit Board Assemblies

Sources: AC 20-152A, Development Assurance for Airborne Electronic Hardware (2022-10-07), sections 6-7 (printed pages 19-25 until section 8 Related material; section 8 and Appendix B feedback form out of scope).

## Core Idea

Section 6 addresses commercial-off-the-shelf semiconductor devices (fully packaged ICs or multi-chip modules, not board assemblies) that applicants use without manufacturer design data and usually without aviation-grade development assurance. As integration density and configurability rose after ED-80/DO-254 (2000), interfaces that used to be visible between separate parts disappeared inside one chip, so incomplete verification and latent design errors became harder to catch. Section 6 adds objectives COTS-1 through COTS-8 for complexity classification, electronic component management, out-of-datasheet use, microcode, errata and failure modes, and controlled usage including unused functions and critical configuration settings. Section 7 adds CBA-1 so circuit board assemblies that host complex custom or complex COTS devices still capture, validate, verify, and configuration-manage board-level requirements with proper flow-down.

## Frameworks Introduced

- **COTS device boundary.** Semiconductor product fully encapsulated in a package (digital, hybrid, or mixed-signal). Explicitly not a circuit board assembly. FPGA/PLD devices that embed manufacturer Hard IP in produced silicon are in section 6 only for the COTS part of those devices.

- **Complexity gate (section 6.3, COTS-1).** Section 6.4 development-assurance objectives for complex COTS apply only after the complexity assessment. A device is complex when (1) multiple functional elements can interact, and (2) it offers a significant number of functional modes, and (3) functions are configurable with different data/signal flows and resource sharing; **or** when (4) it contains advanced data processing, advanced switching, or multiple processing elements (multicore, graphics, networking, complex bus switching, multi-master interconnect fabrics, and similar). Consider all functions, including those intended to be unused. Completely verifying every configuration of a complex COTS device is treated as impractical.

- **Electronic component management process (COTS-2).** Selection, qualification, and configuration management of COTS devices, plus access to user manual, datasheet, errata, installation manual, and manufacturer change information. For DAL A/B contributors, selection of complex COTS also considers device maturity and mitigates identified risks. Recognized industry ECM standards may support building the process (see AC 00-72).

- **Usage definition (COTS-7 / COTS-8).** Used and unused functions, deactivation means, reset and power-on behavior, clock domains, operating conditions, hardware-software and hardware-hardware interfaces, and protection of critical configuration settings at DAL A/B.

- **CBA process (CBA-1).** Board or collection of boards contributing to hardware DAL A/B/C that contain complex custom or complex COTS devices need requirements capture, validation, verification, configuration management, and flow-down so the CBA performs its intended function and allocations to complex devices stay consistent.

## Key Concepts

### Applicability (section 6.2)

- Digital, hybrid, and mixed-signal COTS devices contributing to hardware DAL A, B, or C. DAL C gets a limited objective set.

- Also FPGA/PLD parts that embed Hard IP in manufacturer silicon, for the COTS portion only.

- Section 6.4 applies only to devices classified complex under section 6.3.

### Background pressure (section 6.1)

COTS parts are qualified by semiconductor-industry processes aimed at consumer, automotive, telecom, and similar markets, not airborne DAL rigor. Design data are usually unavailable to the user. ED-80/DO-254 section 11.2 already said COTS usage is verified through the overall design process and supporting processes; modern integration makes function-to-function interfaces inside the chip inaccessible, raises configuration count, and leaves residual risk of post-release design errors or use beyond manufacturer specifications.

### Complexity assessment (COTS-1)

Assess complexity of COTS devices in the design using section 6.3 high-level criteria. Document the list of relevant devices and classification rationale in the PHAC or related hardware planning document.

- Note 1: not a full bill-of-materials scrub; assess devices relevant to classification, including boundary cases. Document resulting simple/complex calls for boundary and definitely-complex devices.
- Note 2: classification rationale is required for boundary devices (meeting only part of the criteria) that are still called simple.
- AC 00-72 gives illustrative classification examples (named only; not restated here).

### Electronic component management and datasheet limits (COTS-2, COTS-3)

**COTS-2.** Ensure an ECM process covers selection, qualification, configuration management, and access to component data and manufacturer change information. For devices contributing to DAL A or B functions, complex-COTS selection considers maturity; mitigate identified risks.

**COTS-3.** When a complex COTS device is used outside the device manufacturer's specification limits (for example recommended operating limits), establish reliability and technical suitability of the device in the intended application. Ties to ED-80/DO-254 section 11.2.1 items 4 and 6 on technical suitability and related concerns.

### Microcode (COTS-4)

Some COTS devices need microcode to execute hardware functions the applicant uses. If microcode is delivered by the manufacturer, controlled under the manufacturer's configuration management, and qualified together with the device by the manufacturer, it is accepted as part of the qualified COTS device. If it is not manufacturer-qualified, or if the applicant modifies it, it is **not** part of the qualified COTS device.

**COTS-4.** In those non-qualified or modified cases, ensure a means of compliance for the microcode integrated in the COTS device is proposed by the appropriate process (hardware, software, or system) and is commensurate with usage of the device. Document microcode existence in the PHAC (or related plan) and point to the process that addresses it.

### Malfunctions, errata, failure modes (COTS-5, COTS-6)

**COTS-5.** Assess errata relevant to the intended application; identify and verify mitigation means. If mitigation is not implemented in hardware, feed it back to and verify it in the appropriate process (hardware, software, system, or other).

**COTS-6.** Identify failure modes of used functions and possible associated common modes; feed both into the system safety assessment process.

### Usage and critical configuration (COTS-7, COTS-8)

Configuration of a complex COTS device must be manageable so required settings can be applied consistently, replicated on another item, and modified under control. Configuration topics include at least:

- Used functions (identification, configuration characteristics, modes);
- Unused functions and internal/external deactivation means;
- Means to control inadvertent activation of unused functions or inadvertent deactivation of used functions;
- Device reset management;
- Power-on configuration;
- Clocking configuration (clock domains);
- Operating conditions (clock frequency, supply, temperature, and similar).

**COTS-7.** Ensure usage of the COTS device is defined and verified against the intended function of the hardware, including the hardware-software interface and hardware-to-hardware interfaces. When the device is used in a hardware DAL A or B function, show that unused functions do not compromise integrity and availability of used functions. Effective deactivation, when available, should be used and verified. Verification level may be hardware, software, or equipment as appropriate. ED-80/DO-254 section 10.3.2.2.4 hardware/software interface data is a reference for defining software interface data of the COTS device.

**Critical configuration settings** are settings the applicant deems necessary for proper hardware usage which, if inadvertently altered, could change COTS device behavior so it no longer fulfills the hardware intended function.

**COTS-8 (complex COTS contributing to DAL A or B).** Develop and verify a means that ensures appropriate mitigation if any critical configuration setting is inadvertently altered. Mitigation may sit at hardware, software, system, or a combination, and may be defined by the safety assessment process.

### Circuit board assemblies (section 7, CBA-1)

**Applicability.** CBA (a board or collection of boards) contributing to hardware DAL A, B, or C.

**CBA-1.** Have a process for development of CBAs that contain complex custom devices or complex COTS devices so the CBA performs its intended function. Include requirements capture, validation, verification, and configuration management, and ensure appropriate requirements flow-down. See AC 00-72 for additional information. The CBA process may be defined together with the equipment process when that is relevant.

Board-level function definition is what makes allocation and flow-down into complex devices coherent; without it, device-level assurance floats free of the equipment/system intent. Section 6 usage talk ("intended function of the hardware") is considered defined through this CBA development process.

## Mental Models

- Packaged silicon is section 6; the board that holds it is section 7. Do not apply COTS-device objectives to a CBA, or CBA-1 alone to a bare die problem.

- Complexity is about interaction, modes, configurability, or advanced processing, including unused logic. "We only use one mode" does not erase complexity if the silicon still hosts interacting configurable elements.

- ECM is the industrial hygiene layer (pick, qualify, config-manage, get errata and change data). COTS-3 through COTS-8 are the assurance layer on top for complex parts.

- Microcode is either inside the manufacturer's qualified device envelope or it is your problem under some other means of compliance. There is no quiet middle.

- Unused functions and critical configuration settings are DAL A/B integrity problems: show non-interference and protect the settings that, if flipped, break the intended function.

- CBA-1 is the glue: device objectives assume an intended hardware function that the board process is responsible for stating and flowing down.

## Anti-patterns

- **Skipping complexity assessment or assessing the entire BOM.** COTS-1 wants relevant and boundary devices with rationale, not theater and not silence.

- **Calling a boundary device simple with no rationale.** Note 2 under COTS-1 requires it.

- **No ECM process, or ECM without errata/change-data access.** COTS-2 is explicit.

- **Running past datasheet limits without a reliability and suitability case.** COTS-3.

- **Applicant-modified or unqualified microcode treated as "part of the COTS chip."** COTS-4 reassigns it to an explicit means of compliance and a PHAC pointer.

- **Filing errata without verified mitigation, or keeping software/system mitigations off the verifying process.** COTS-5.

- **Never feeding COTS failure modes and common modes into system safety.** COTS-6.

- **DAL A/B use with live unused functions and no non-interference argument.** COTS-7.

- **Critical configuration settings with no inadvertent-alteration mitigation at DAL A/B.** COTS-8.

- **Complex devices on a board with no CBA requirements/validation/verification/CM/flow-down process.** CBA-1.

## Key Takeaways

1. Section 6 covers packaged COTS semiconductor devices (and the COTS portion of FPGAs/PLDs with manufacturer-embedded Hard IP) at hardware DAL A/B/C; section 6.4 applies only after a documented complexity assessment (COTS-1).

2. Complex COTS work rests on an electronic component management process (COTS-2), with extra maturity/risk attention at DAL A/B; out-of-spec use needs an explicit reliability and suitability case (COTS-3).

3. Microcode is part of the qualified device only when manufacturer-delivered, CM-controlled, and qualified with the device; otherwise propose a commensurate means of compliance and record it (COTS-4).

4. Errata mitigations must be identified and verified (COTS-5); used-function failure modes and common modes feed system safety (COTS-6); usage including interfaces is defined and verified, with unused-function non-interference and critical-configuration protection at DAL A/B (COTS-7, COTS-8).

5. CBA-1 requires a board-level development assurance process (requirements, validation, verification, CM, flow-down) for assemblies that contain complex custom or complex COTS devices at DAL A/B/C; AC 00-72 is the named companion best-practices AC.

## Connects To

- **ch07** - complex custom devices that sit on the same CBA and share PHAC planning discipline.

- **ch08** - tool, PDH, and verification clarifications that still apply when custom logic shares a board with COTS silicon.

- **ch09** - applicant-instantiated COTS IP versus manufacturer-embedded Hard IP (the latter routes here under section 6).

- **ch01** - where AC 20-152A and AC 00-72 sit relative to software ACs and Order 8110.49A.

- **ch05** - software means-of-compliance pattern when COTS-4 sends microcode to a software process.
