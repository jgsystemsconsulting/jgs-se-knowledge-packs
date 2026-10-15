# Cheatsheet: faa-8110-49

Decision rules for FAA airborne software and hardware approval questions. Each rule names the chapter that owns the detail; the paywalled industry standards live behind the avionics-signpost pack.

## Which document governs my question? → ch01

- FAA staff procedure (reviews, involvement sizing, conformity): Order 8110.49A. (ch01, ch02, ch03, ch04)
- Airborne software development assurance: AC 20-115D. (ch01, ch05, ch06)
- Airborne electronic hardware development assurance: AC 20-152A. (ch01, ch07 to ch10)
- What the standard itself demands (DO-178C objectives, DO-254 process text, Annex tables): paywalled and out of this pack; avionics-signpost carries the designations and purchase points. (ch01)
- Guidance is not regulation: the ACs are acceptable means, and the order binds FAA staff, not applicants. (ch01)
- Citations to "8110.49 chapters 5-16" point at deleted Chg 2 text; translate before trusting. (ch01)

## What does the FAA review, and how? → ch02

- Reviews assess compliance with the certification basis and the applicable DO-178B/C objectives through life cycle data; DO-178B/C Section 9 liaison is the channel. (ch02)
- Desk and on-site reviews are both valid; on-site buys access to people, automation, and the test setup. (ch02)
- On-site rests on nine agreed arrangements: scope, dates and locations, authority personnel, designees, agendas and expectations, data before and at the review, procedures, resources, and the results channel including corrective actions. (ch02)
- Four review objectives: technical interpretation, visibility into compliance, evidence of plan adherence, and designee monitoring. (ch02)
- Delegation does not end authority interest; a monitoring path for designee work stays in scope. (ch02)

## How much FAA involvement (LOI)? → ch03

- Determine and document LOI as early as practicable; a late LOI is an anti-pattern, not a shortcut. (ch02, ch03)
- Eight factors shape it: software level, product attributes, new technologies, novel methods, applicant experience, designee availability, DO-178B/C Section 12 issues, and software issue papers. (ch03)
- Worksheet 1 bands: Level D LOW; Level C LOW or MEDIUM; Levels A and B MEDIUM or HIGH. (ch03)
- Worksheet 2 scores experience, demonstrated capability, service history, this application's complexity and novelty, and designee capacity into the TSR; novelty and complexity score DOWN. (ch03)
- Worksheet 3 combines TSR with software level to land LOW / MEDIUM / HIGH inside the level's band. (ch03)
- The worksheets are optional examples; any early, explicit, reasoned method satisfies the order. (ch03)

## Is a conformity inspection required, and which one? → ch04

- Each test run for certification credit: software part conformity, first. (ch04)
- Any FAA aircraft-level ground or certification flight test (for example under a TIA): software installation conformity, only after part conformity succeeded. (ch04)
- The ASE establishes baseline, test-configuration match, artifact control, tool qualification status, and SCM retention; the ASI executes the witness and verify list on Form 8120-10. (ch04)
- Delegated baseline approval: a DER's Form 8110-3, stating the baseline is approved for FAA testing. (ch04)
- Special-purpose environmental test software is verified, validated, and configuration-controlled as part of the test setup. (ch04)
- Tool qualification incomplete at conformity time? Document the tools and supporting-data configuration anyway. (ch04)

## Am I on DO-178C yet? (recognition, transition, tools) → ch05

- Recognized set: DO-178C/ED-12C plus DO-330 (tools) and DO-331/DO-332/DO-333 (techniques); "DO-178C" in the AC includes them as applicable. (ch05)
- Keep DO-178B processes for new development only if all six section 5 criteria hold; any failure upgrades to DO-178C, and new process shops start there. (ch05)
- Never both: declaring DO-178C satisfaction while developing or modifying under unchanged DO-178B processes is forbidden. (ch05, ch06)
- Under DO-178C: satisfy every applicable objective, submit section 9.3 (and DO-330 section 9.0.a) data, treat section 9.4 as type design (Level D drops Design Description and Source Code), and keep section 11 data available. (ch05)
- Even if the FAA steps back from liaison, the Table A-10 data must exist before liaison objectives count as satisfied. (ch05)
- Tools: DO-330 and TQLs for new work; Table 2 correlates legacy DO-178B tool types. Development tools keep DO-178B processes only if the prior level meets the required TQL; TQL-4 verification tools requalify under DO-330. (ch05)
- Tool and software equivalence diverge: a DO-330 tool claim never makes legacy software DO-178C-equivalent, and upgraded software never makes unmodified tools DO-330-equivalent. (ch05, ch06)

## Modifying or reusing legacy software? FLS? UMS? → ch06

- Follow Figure 1: usage-history gate, Table 1 level fit, then the modify-or-not branches. Leave the flow only with certification-office coordination. (ch06)
- Open safety-related OPRs, service difficulties, or airworthiness directives with no resolution plan block reuse. (ch06)
- Table 1 decides whether the legacy level satisfies the assigned level; an unacceptable level upgrades the baseline via DO-178C (and DO-330). (ch06)
- Keeping original-version processes for modifications requires every 9.b(7) condition, and forbids a DO-178C equivalence claim. (ch06)
- Modified software: run change impact analysis, verify as it indicates, and summarize results in the PSAC or SAS. Best-practice contents of that analysis are in ch11 (AC 00-69), which is best practices, not a means of compliance. (ch06)
- Equivalence is declared after full process upgrades, and never extends to unmodified tools. (ch06)
- Supplements attach to techniques, not stand-alone: the PSAC names which objectives from which documents hit which components, and DO-331 MB.6.8.1 simulation substitution needs per-objective justification. (ch06)
- FLS: developer support data, corruption and partial-load protection, verifiable loaded part number, and inhibit during flight or other safety-critical phases. (ch06)
- UMS: the modifiable partition is developed at least at the assigned software level. (ch06)
- Data coupling and control coupling are separate analyses and both are required. (ch12)
- Design-level error handling: put the mitigation in the requirements; runtime protection is named for levels A and B. (ch13)

## Custom AEH device: simple or complex? → ch07

- CD-1 in the PHAC: the DAL, the classification, and for simple devices the criteria-based justification. (ch07)
- Simple requires a technical assessment that comprehensive deterministic tests and analyses verify correct performance under all foreseeable operating conditions with no anomalous behavior. (ch07)
- Weigh function and interface simplicity, processing simplicity, and independence; digital designs add clock and state-machine criteria. (ch07)
- A bag of simple blocks can still be complex; classify the integrated item. (ch07)
- Complex: full ED-80/DO-254 plus AC sections 5.5 through 5.11. Simple: reduced data, but intended function, configuration management, and build conformance remain. (ch07)
- CD-3: validate all custom device requirements, not just derived ones, with independence at DAL A/B. (ch07)
- CD-4, CD-5, CD-6: detailed design review (traceability at DAL A/B), design-tool report review, and verification case and procedure review. (ch07)
- CD-7: verify timing across temperature, supply, and process variation; static timing analysis is one means. (ch07)
- DAL D hardware is outside the AC's required use; AC 00-72 may still help. SEE assessment is out of scope. (ch07)

## AEH verification and tools → ch08

- CD-8 at DAL A/B: abnormal and boundary conditions and their expected behavior become requirements. (ch08)
- HDL code coverage counts as elemental analysis only inside requirements-based verification; CD-9 needs planned coverage criteria and justified holes. (ch08)
- The coverage-tool exclusion is narrow: coverage that decides verification completion makes the tool a verification tool under Figure 11-1 item 4. (ch08)
- CD-10: independent assessment must cover what the tool could insert or miss, sized to the objectives the tool serves. (ch08)
- CD-11: relevant history needs data proving relevance and credibility for this use. (ch08)
- Design-tool history is never a stand-alone qualification means; ED-12C/DO-178C and ED-215/DO-330 may guide design-tool qualification. (ch08)
- CD-12: PDH credit dies on modification, on a change of function, use, or failure condition classification, or on a design-environment change, until section 11.1 reassessment. (ch08)
- Section 5.10: Level C control-category tweaks, Detailed Design Data at HC1 for A/B/C, and Top-Level Drawing as HCI (with HECI or an embedded environment) for replication. (ch08)

## COTS IP inside a custom device → ch09

- Applicant-inserted Soft, Firm, or Hard IP at hardware DAL A/B/C is section 5.11; manufacturer-embedded Hard IP is a COTS-device question instead. (ch09, ch10)
- IP-1: selection on technical suitability, data quality, implementation information, and demonstrability; popularity is not a criterion. (ch09)
- IP-2: provider and data assessment, documented and submitted for certification. (ch09)
- IP-3: unmet IP-2 items 1, 2, 4, or 5 require complementary DO-254-based assurance activities. (ch09)
- IP-4: the verification strategy covers the IP itself, the IP after your design steps, and integration, with unused functions disabled and non-interfering. (ch09)
- IP-5: the plan identifies IP versions and formats, flow points, the assurance process, and tool aspects. (ch09)
- IP-6: requirements (including derived requirements for used functions, unused-function deactivation, and correct control) are sized to the strategy and validated with the device. (ch09)
- IP-7 at DAL A/B: satisfy ED-80/DO-254 Appendix B; safety-specific analysis is the explicit path when code coverage cannot see into the IP. (ch09)

## COTS devices and circuit board assemblies → ch10

- COTS-1 comes before the section 6.4 objectives: assess complexity for relevant and boundary devices and document rationale in the PHAC; it is not a bill-of-materials scrub. (ch10)
- Complex means interacting functional elements with many configurable modes, or advanced processing, switching, or multiple processing elements; unused logic counts. (ch10)
- COTS-2: an ECM process with selection, qualification, configuration management, and errata and change-data access; device maturity counts at DAL A/B. (ch10)
- COTS-3: use beyond the manufacturer's specification limits needs a reliability and technical suitability case. (ch10)
- COTS-4: microcode is part of the qualified device only if manufacturer-delivered, manufacturer-controlled, and qualified with it; otherwise propose a commensurate means of compliance and record it in the PHAC. (ch10)
- COTS-5 and COTS-6: verify errata mitigations, and feed used-function failure modes and common modes into system safety. (ch10)
- COTS-7: usage is defined and verified including hardware-software and hardware-hardware interfaces, with unused functions shown non-interfering at DAL A/B. (ch10)
- COTS-8 at DAL A/B: mitigation for inadvertent alteration of critical configuration settings. (ch10)
- CBA-1: assemblies hosting complex custom or complex COTS devices need board-level requirements capture, validation, verification, configuration management, and flow-down. (ch10)

## Quick anchors

| Need | Answer | Chapter |
|------|--------|---------|
| Which document governs? | 8110.49A staff procedure; 20-115D software; 20-152A hardware | ch01 |
| Review forms and objectives | Desk vs on-site; nine arrangements; four objectives | ch02 |
| LOI band for Levels A and B | MEDIUM or HIGH (Worksheet 1), refined by the TSR | ch03 |
| Conformity order | Part conformity before installation conformity | ch04 |
| DO-178B reuse test | Six section 5 criteria; any failure upgrades | ch05 |
| DO-178C equivalence claim | Only after full process upgrade; tools never inherit it | ch05, ch06 |
| FLS and UMS add-ons | Load integrity plus inhibit; modifiable partition at level | ch06 |
| Simple custom device test | Comprehensive deterministic verification feasible | ch07 |
| Coverage tool exclusion | Elemental analysis only, never completeness calls | ch08 |
| COTS IP entry gates | IP-1 selection; IP-2 assessment submitted | ch09 |
| Microcode rule | Manufacturer-qualified envelope or your own means of compliance | ch10 |
| Paywalled standard | Designations and purchase points, no text | avionics-signpost |

## Tells & smells

| Smell | Likely gap | Chapter |
|-------|------------|---------|
| Review calendar invented before LOI is documented | Order 8110.49A timing rule | ch02, ch03 |
| Novelty scored as a bonus | Worksheet 2 scale direction inverted | ch03 |
| Installation conformity requested before part conformity | Sequence rule broken | ch04 |
| DO-178C claim on unchanged DO-178B processes | Section 5 and 9.b conflict | ch05, ch06 |
| DO-330 tool claim treated as software equivalence | Tools and software diverge | ch05, ch06 |
| "Simple" device with no justification in the PHAC | CD-1 item 3 is mandatory | ch07 |
| Timing closed at nominal only | CD-7 corners missing | ch07 |
| Green coverage read as complete requirements testing | Section 5.7 says the opposite | ch08 |
| Tool history claimed without data | CD-11 blocks hand-waving | ch08 |
| Vendor unit tests as the whole IP verification strategy | IP-4 three aspects unmet | ch09 |
| One-mode use erasing COTS complexity | Complexity includes unused logic | ch10 |
| Pointing at DO-178C tables from this pack | Paywalled; use avionics-signpost | ch01 |

## What this pack is not

- Not regulation: the ACs are acceptable means, the order binds FAA staff, and nothing here is legal advice. (ch01)
- Not the standards: no DO-178C, DO-254, or supplement text and no objective tables; buy from the owners, with designations via avionics-signpost. (ch01)
- Not EASA: AMC 20-115D and AMC 20-152A exist free through the EASA Easy Access Rules (AMC-20) and are outside this pack. (ch01)
- Not current-policy insurance: sources are pinned 2017 to 2022; check the FAA website before relying on a single requirement. (ch01)
