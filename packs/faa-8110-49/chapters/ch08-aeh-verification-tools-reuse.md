# Chapter 8 - AEH Verification, Tools, and Reuse

Sources: AC 20-152A, Development Assurance for Airborne Electronic Hardware (2022-10-07), sections 5.6-5.10 (printed pages 8-12; custom-device front matter and CD-1 through CD-7 in ch07; COTS IP section 5.11 in ch09).

## Core Idea

After the custom-device classification and base validation/verification path in ch07, AC 20-152A sections 5.6-5.10 tighten four areas ED-80/DO-254 leaves thin or easy to misread: robustness under abnormal and boundary conditions, recognition of HDL code coverage as an elemental-analysis method, tool assessment and qualification against Figure 11-1, previously developed hardware (PDH) reuse, and a short set of Appendix A life cycle data control-category clarifications. Objectives CD-8 through CD-12 live here.

## Frameworks Introduced

- **Robustness as required behavior under abnormal/boundary conditions (section 5.6, CD-8).** Robustness is the expected behavior of the design under abnormal and boundary/worst-case operating conditions of inputs and internal design states. Those conditions are often captured as derived requirements when not allocated from above. Under those conditions the design may not continue to perform as it would under normal conditions; the point is that the expected (possibly degraded) behavior is defined.

- **HDL code coverage as elemental analysis method (section 5.7, CD-9).** When run during requirements-based verification (ED-80/DO-254 section 6.2), HDL code coverage is recognized as a method to perform ED-80/DO-254 elemental analysis per Appendix B section 3.3.1 for digital devices. It shows whether HDL elements were exercised by requirements-based simulations; it is not a verdict on completeness of requirements-based testing or on requirement-coverage effectiveness.

- **Tool assessment flow (section 5.8, CD-10 / CD-11).** ED-80/DO-254 Figure 11-1 remains the backbone. The AC clarifies identification (include environment and revision), process purpose, independent assessment of tool output, when code-coverage tools are excluded from qualification pressure, what "relevant history" actually demands, and that design-tool history is never a stand-alone qualification means. ED-12C/DO-178C and ED-215/DO-330 may also be used for design-tool qualification guidance referenced at Figure 11-1 item 9.

- **Previously developed hardware reuse (section 5.9, CD-12).** PDH is a custom-developed hardware device already installed in airborne system/equipment approved by FAA TC/STC or authorized by TSOA, including hardware developed and approved before ED-80/DO-254 use in civil certification. Reuse runs through ED-80/DO-254 section 11.1; three change classes can invalidate prior assurance credit.

- **Appendix A life cycle data clarifications (section 5.10).** Five table/control fixes so HC levels and Top-Level Drawing / HCI / HECI expectations line up for Levels A-C.

## Key Concepts

### Robustness (CD-8)

For DAL A or DAL B hardware, define abnormal and boundary conditions and the associated expected behavior of the design as requirements. ED-80/DO-254 mentions robustness defects but does not explicitly develop the topic; CD-8 fills that gap at the higher DALs.

### HDL code coverage (CD-9)

- Coverage analysis assesses whether HDL design code has been exercised through HDL simulation and which parts of the logic structure were and were not hit.

- Recognition path: requirements-based verification plus elemental analysis (Appendix B section 3.3.1) for digital devices.

- **CD-9 (DAL A or B, when HDL code coverage is used for elemental analysis).** Define in planning documents the detailed coverage criteria for the HDL code elements used in the design (branches, conditions, and similar). Analyze and justify any non-covered case or element.

- Note: items not covered by code coverage (including some COTS IP instantiations) may need complementary analysis to finish elemental analysis of all elements.

### Tool assessment and qualification (section 5.8)

Walk Figure 11-1 with the AC's clarifications:

1. **Identify the tool.** Include the environment required for tool operation and the tool revision with the identification.

2. **Identify the process the tool supports.** Also state which purpose or activity inside the hardware development process the tool satisfies. If tool output is completely and independently assessed, formal assessment of tool problem reports is not required while judging tool limitations.

3. **Is the tool output independently assessed?** Independent assessment must completely cover potential errors the tool could insert into the design or fail to detect in verification.

   - **CD-10.** When intending independent assessment of tool output, propose an assessment that verifies the output is correct, justify sufficient coverage of that output, and base completeness of the assessment on the design/implementation and/or verification objectives the tool is used to satisfy.

4. **Is it a Level A/B/C design tool or Level A/B verification tool?** Figure 11-1 item 4 excludes activities for tools "used to assess the completion of verification testing, such as in an elemental analysis." The AC narrows that exclusion:

   - Code coverage tools are excluded from tool assessment/qualification activities only when used to assess whether code has been exercised by requirements-based testing/simulations (elemental analysis).
   - If a tool automatically generates test cases or procedures and uses coverage to decide that requirements verification is complete, treat it as a verification tool under item 4 (not as a mere coverage meter).

5. **Does the tool have relevant history?** Prior use alone does not end assessment. The applicant must provide enough data and justification to show the history is relevant and credible for the proposed use.

   - **CD-11.** When claiming credit for relevant tool history, provide sufficient data as part of tool assessment to demonstrate a relevant and credible history that the tool will produce correct results for its proposed use.

9. **Design tool qualification.** Contrary to a note in the supporting text for item 9, tool history must not be used as a stand-alone means of tool assessment and qualification. Relevant history may compensate for particular gaps (for example, explaining an independent-assessment method) and is complementary assurance only. Besides the references already in Figure 11-1 item 9, ED-12C/DO-178C and ED-215/DO-330 may be used for design-tool qualification guidance.

### Previously developed hardware (CD-12)

When proposing PDH reuse, use ED-80/DO-254 section 11.1 and its subordinate paragraphs. Perform the required assessments and analyses so that using the PDH remains valid and prior compliance is not compromised by:

1. Modification of the PDH for the new application or for obsolescence management;
2. Change to the function, to its use, or to a higher failure condition classification of the PDH in the new application; or
3. Change to the design environment of the PDH.

Document results in the PHAC or another appropriate planning document. Any one of the three points can invalidate original development assurance credit. On change or modification, assess per section 11.1; when original design assurance is invalidated, upgrade the custom device based on that assessment and apply the AC objectives that the assessment says still apply.

### Appendix A clarifications (section 5.10)

Relative to ED-80/DO-254 Appendix A Table A-1 and related text:

- 10.1.6 Hardware Process Assurance Plan: also HC2 for Level C (align with row 10.8).
- 10.2.2 Hardware Design Standard: also HC2 for Level C; HDL coding standards are part of Hardware Design Standards.
- 10.3.2.2 Detailed Design Data: HC1 for Levels A, B, and C.
- 10.4.2 Hardware Review and Analysis Procedures: also HC2 for Level C (align with row 10.4.3).
- Top-Level Drawing corresponds to a Hardware Configuration Index (HCI) that completely identifies hardware configuration, embedded logic, and development life cycle data. To support consistent replication (ED-80/DO-254 section 7.1), the Top-Level Drawing includes the hardware life cycle environment or refers to a Hardware Environment Configuration Index (HECI).

## Mental Models

- Robustness requirements answer "what should it do when things are wrong or at the edge," not "it must still meet normal performance."

- HDL code coverage is a structural exercise meter under requirements-based simulation. Green coverage without requirements-based tests does not satisfy the recognition path in section 5.7.

- Independent assessment of tool output is a coverage problem: you must bound what the tool could get wrong relative to the objectives it serves (CD-10).

- "We used this tool last program" is evidence only after you show relevance and credibility for this use (CD-11), and for design tools it never stands alone as qualification.

- PDH credit is brittle: modify the device, change its function/use/failure classification upward, or change its design environment, and section 11.1 reassessment (and possible upgrade) is mandatory.

- HCI/HECI are how you make a custom device reproducible; Top-Level Drawing is not a decorative drawing number.

## Anti-patterns

- **Leaving abnormal/boundary behavior undefined on DAL A/B hardware.** CD-8 requires those conditions and expected behaviors as requirements.

- **Treating HDL code coverage as proof that requirements testing is complete.** Section 5.7 says the opposite.

- **Skipping coverage criteria and justification for holes on DAL A/B elemental analysis.** CD-9 demands both.

- **Auto-generating tests from coverage and calling the generator a non-qualifying coverage tool.** If coverage decides verification completion, item 4 treats it as a verification tool.

- **Claiming tool history without data.** CD-11 blocks hand-waving.

- **Qualifying a design tool on history alone.** Item 9 clarification forbids stand-alone history.

- **Dropping PDH into a new application after modification, role change, or environment change without section 11.1 assessment.** CD-12 lists all three as credit-killers until assessed and, if needed, upgraded.

- **Ignoring the Level C HC tweaks and HCI/HECI replication story in section 5.10.** Those rows are easy to miss when copying an older data-control matrix.

## Key Takeaways

1. CD-8 (DAL A/B) turns robustness into explicit requirements for abnormal and boundary conditions and expected behavior.

2. HDL code coverage is a recognized elemental-analysis method only inside requirements-based verification; CD-9 requires planned coverage criteria and justified holes at DAL A/B.

3. Tool path follows Figure 11-1 with CD-10 (independent output assessment coverage) and CD-11 (credible relevant history); design-tool history is complementary only; DO-330/DO-178C may support design-tool qualification guidance.

4. PDH reuse runs ED-80/DO-254 section 11.1; modification, function/use/failure-class change, or design-environment change can invalidate prior credit and force upgrade against applicable AC objectives (CD-12).

5. Section 5.10 aligns several Appendix A HC categories for Level C, sets Detailed Design Data to HC1 for A/B/C, and equates Top-Level Drawing with HCI (plus HECI or embedded life cycle environment) for replication.

## Connects To

- **ch07** - custom-device applicability, simple/complex classification, and CD-1 through CD-7 validation/verification base that these clarifications extend.

- **ch09** - COTS IP path, including where code coverage may not reach IP instantiations and Appendix B alternatives appear.

- **ch10** - COTS device and CBA processes that still depend on controlled configuration and verification discipline established here.

- **ch05** - software tool qualification transition to DO-330; section 5.8 explicitly allows DO-178C/DO-330 as design-tool qualification guidance references.

- **ch01** - where AC 20-152A sits in the approval map relative to Order 8110.49A and AC 20-115D.
