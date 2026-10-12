# Chapter 7 - AEH Custom Devices

Sources: AC 20-152A, Development Assurance for Airborne Electronic Hardware (2022-10-07), sections 1-5.5 (printed pages 1-8 body; section 5.6 onward covered in ch08; section 5.11 COTS IP in ch09).

## Core Idea

AC 20-152A is the FAA recognition and clarification instrument for airborne electronic hardware (AEH) development assurance. It recognizes EUROCAE ED-80 / RTCA DO-254 (April 2000) as equivalent, states when those documents apply, and adds numbered objectives that supplement them for custom devices (PLDs, FPGAs, ASICs), for COTS IP inside those devices, for COTS semiconductor devices, and for circuit board assemblies. This chapter covers the AC front matter and the custom-device path through simple/complex classification and the validation/verification clarifications in section 5.5 (objectives CD-1 through CD-7).

## Frameworks Introduced

- **Acceptable means, not regulation (section 1).** The AC is an acceptable means, not the only means, and does not bind the public as law. If you use it, follow it in all applicable respects unless the FAA accepts an alternate means or deviation.

- **Recognition pair.** ED-80 and DO-254 are treated as equivalent under the notation ED-80/DO-254. The AC does not reprint those standards; it points at them and adds objectives.

- **Objective families (section 4).** Unique identifiers: CD-i (custom devices), IP-i (COTS IP in custom devices), COTS-i (COTS devices), CBA-i (circuit board assemblies). Objectives are italicized in the source AC.

- **PHAC as the planning vehicle.** Process and activities intended to satisfy the AC objectives are documented in the Plan for Hardware Aspects of Certification (PHAC) or related planning documents, and those plans are submitted for certification.

- **Simple versus complex custom devices (section 5.2).** Classification rests on whether a comprehensive combination of deterministic tests and analyses can verify correct functional performance under all foreseeable operating conditions with no anomalous behavior. Complex custom devices take full ED-80/DO-254 plus AC sections 5.5-5.11; simple devices take a reduced process (CD-2) with selected later sections still applying.

- **DAL modulation.** ED-80/DO-254 Appendix A modulates life cycle data by hardware DAL. The AC recognizes that modulation for custom devices. DAL C gets a limited objective set; DAL D is outside required use of this AC (AC 00-72 may still help).

## Key Concepts

### Purpose, applicability, cancellation, background

- Audience: applicants, design approval holders, and developers of airborne systems and equipment containing AEH for type-certificated aircraft, engines, and propellers, and developers of TSO articles.

- Scope of required use: AEH that contributes to hardware DAL A, B, or C functions. When an objective is DAL-restricted, the objective text says so (for example, "For DAL A hardware...").

- DAL D: structured flow-down still helps, but this AC is not required; AC 00-72 offers optional clarifications so DAL D hardware still performs its intended function.

- Cancels AC 20-152 (2005-06-30).

- Does not address Single Event Effects (SEE) susceptibility. The PHAC may still record SEE certification considerations.

- Background organization: each major topic (custom devices, COTS IP, COTS devices, CBA) carries background, applicability, and uniquely identified objectives.

### Custom devices in scope (section 5 / 5.1)

- Custom devices = PLDs, FPGAs, ASICs; ED-80/DO-254 section 1.2 item 3 "custom micro-coded components."

- Section 5 applies to digital or mixed-signal custom devices contributing to hardware DAL A, B, or C.

- Complex custom devices (section 5.3): satisfy ED-80/DO-254 plus the additional objectives/clarifications in AC sections 5.5 through 5.11.

- Simple custom devices (section 5.4 / CD-2): life cycle data may be significantly reduced, but the device must still perform its intended function, stay under configuration management (including problem reporting and reproduction instructions), and support build conformance assessment. Sections 5.5.2.4 and 5.5.2.5 also apply to simple-device verification. Tool use pulls in section 5.8; PDH reuse pulls in section 5.9 and ED-80/DO-254 section 11.1; COTS IP pulls in section 5.11. Simple-device life cycle data may be combined with other hardware data.

### Simple/complex classification (section 5.2, CD-1)

Classify as simple only when a technical assessment of design content supports comprehensive verification by deterministic tests and analyses under all foreseeable operating conditions with no anomalous behavior. Criteria to weigh:

- Simplicity and number of functions
- Number and simplicity of interfaces
- Simplicity of data/signal processing or transfer functions
- Independence of functions/blocks/stages

Additional digital criteria: synchronous versus asynchronous design; number of independent clocks; number of state machines and states/transitions per machine; independence between state machines. Applicants may propose other or additional simplicity criteria. If it cannot be classified simple, classify complex. An assembly of only simple items may still be complex.

**CD-1.** For each custom device, document in the PHAC or related plan: (1) development assurance level, (2) simple or complex classification, (3) if simple, the justification against the classification criteria.

### Validation and verification clarifications (section 5.5, CD-3 through CD-7)

**Validation (CD-3).** Establishing a correct and complete requirement set is the cornerstone. ED-80/DO-254 section 6.1 focuses validation language on derived requirements; the AC requires validating all custom device requirements (derived and non-derived) per the ED-80/DO-254 validation process (section 6). Upper-level allocations refined or restated at device level are still non-derived if traceable, and they still need to be correct and complete. For DAL A and B, perform validation with independence (ED-80/DO-254 Appendix A defines acceptable independence means).

**Conceptual design review.** Conceptual design produces a high-level design description from hardware requirements (ED-80/DO-254 section 5.2). The review checks consistency with requirements and surfaces interface and architectural constraints for detailed design. Already covered by ED-80/DO-254 section 5.2.2 note; no separate AC objective.

**Detailed design review (CD-4).** Detailed design produces HDL or analog representation, implementation constraints (timing, pinout, I/O), and hardware-software interface description. Design review is essential during detailed design and complements requirements-based verification.

- DAL A or B: review detailed design against design standards and review traceability to custom device requirements so the design covers requirements, stays consistent with conceptual design, and meets hardware design standards.
- DAL C: demonstrate that detailed design satisfies the hardware design standards.

**Implementation / tool-report review (CD-5).** When tools convert detailed design data into physical implementation, review design tool reports (for example synthesis and place-and-route reports) to ensure the tool executed properly when generating its output.

**Verification cases and procedures (CD-6).** Each verification case and procedure is reviewed to confirm it is appropriate for the requirements it traces to and that those requirements are correctly and completely covered.

**Timing performance of the implementation (CD-7).** Implementation is the physical custom device produced from detailed design data; the post-layout netlist is the closest virtual representation after synthesis (digital) and place-and-route. Physical test in the intended operational environment is recommended; for features not reachable from I/O pins, timing, abnormal conditions, or robustness cases, post-layout netlist work may be needed and non-physical coverage must be justified. CD-7 requires verifying timing performance while accounting for temperature and power-supply variation applied to the device and semiconductor fabrication process variation as characterized by the device manufacturer. Static timing analysis (STA) with necessary constraints is one possible means for digital parts.

ED-80/DO-254 section 5.1.2 item 4.g already requires capturing signal timing characteristics under normal and worst-case conditions; CD-7 makes environmental and process variation explicit in the timing evaluation.

## Mental Models

- AC 20-152A is the FAA "how we accept DO-254 work" layer, not a second hardware standard. Objectives CD/IP/COTS/CBA hang off ED-80/DO-254; they do not replace it.

- Simple is a verification claim, not a marketing label. If you cannot comprehensively test-and-analyze the device under all foreseeable conditions without anomalous behavior, it is complex.

- A bag of simple blocks can still be a complex device. Classification looks at the integrated item.

- PHAC is the single place the authority should find DAL, simple/complex call (with justification), and which AC objective families you are running.

- Validation is not only for derived requirements. Anything stated at custom-device level, including restated upper-level allocations, still goes through validation; DAL A/B add independence.

- Tool reports are evidence the implementation path ran cleanly (CD-5); they are not a substitute for requirements-based verification of the device.

## Anti-patterns

- **Calling a device simple without a criteria-based justification in the PHAC.** CD-1 item 3 is mandatory for the simple path.

- **Skipping ED-80/DO-254 on a complex custom device and living only on AC objectives.** Section 5.3 requires both the standard and sections 5.5-5.11.

- **Validating only derived requirements.** CD-3 covers derived and non-derived custom device requirements.

- **DAL A/B detailed design that never checks traceability back to requirements and conceptual design.** CD-4 is stronger than "meets coding style."

- **Shipping synthesis/P&R output without reading the tool reports.** CD-5 exists because silent tool failure is a real implementation risk.

- **Timing closure at nominal only.** CD-7 demands temperature, supply, and process-variation accounting, not a single corner.

- **Treating this AC as required for DAL D AEH.** Section 2 says it is not required at DAL D; do not invent a mandatory DO-254 program from this AC alone.

- **Expecting SEE guidance here.** Section 1 explicitly excludes SEE assessment content.

## Key Takeaways

1. AC 20-152A recognizes ED-80/DO-254, cancels AC 20-152 (2005), and adds CD/IP/COTS/CBA objectives for AEH contributing to hardware DAL A/B/C; it is guidance, not regulation.

2. Custom devices are PLDs/FPGAs/ASICs; complex ones take full DO-254 plus AC sections 5.5-5.11; simple ones take CD-2's reduced process with selected later sections still on the hook.

3. CD-1 records DAL, simple/complex classification, and simple-path justification in the PHAC; simple classification requires a technical assessment that comprehensive deterministic test-and-analysis verification is feasible.

4. CD-3 validates all custom device requirements (independence at DAL A/B); CD-4 through CD-6 cover detailed design review, design-tool report review, and verification case/procedure review; CD-7 verifies timing across environmental and process variation.

5. ED-80/DO-254 Appendix A DAL modulation of life cycle data is recognized; paywalled standard text is not reproduced here (see avionics-signpost for designations only).

## Connects To

- **ch01** - which FAA document answers which question, and the AC-to-RTCA/EUROCAE recognition chain for hardware.

- **ch08** - robustness, HDL code coverage, tool assessment/qualification, previously developed hardware, and Appendix A life cycle data clarifications (sections 5.6-5.10).

- **ch09** - COTS IP selection, provider assessment, planning, and verification inside custom devices (section 5.11).

- **ch10** - COTS semiconductor devices and circuit board assembly development assurance (sections 6-7).

- **ch05** - software-side recognition pattern (AC 20-115D to DO-178C) that parallels this hardware recognition pattern.
