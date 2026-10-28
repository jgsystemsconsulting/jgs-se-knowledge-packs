Sources: JSP 912 Part 2 V3.0, printed body pp. 25-33 (stage HFI-4.0 Detailed System Design).

# Detailed system design, HFI-4.0 (Part 2)

## Core Idea

The primary goal of the Detailed System Design stage is to ensure all HFI requirements are addressed and HFI considerations are managed and mitigated through the system design process. The design process is principally run by the Solution Provider and assured by the Acquirer. During the Demonstration phase much of the HFI work transitions from MOD to the Solution Provider, while the HFIF(PT) oversees the Solution Provider's design activities and approves outputs and deliverables. The stage is the largest in the process: seventeen core activities spanning joint management structures, the conduct of HFI activities, the shared RAIDO register, requirements and design-change management, and HFI input across the project's documents.

## Frameworks Introduced

- The working machinery: the Solution Provider's HFI Manager manages system and sub-system HFI design activities day to day, including progressive assurance and the considerations the Provider owns. The HFIF(PT) shall ensure a MOD-Solution Provider HFI Working Group is established as soon as possible after contract award and continues at least until MOD accepts the Solution; it is distinct from the MOD HFI Steering Group of HFI-2.3 and may be a standalone group or part of another working group such as Systems Engineering or Supportability. Typical membership spans the HFIF(PT), MOD stakeholders including user representation, the Solution Provider's HFI Manager and SE representative, equipment engineers for HMI and HCI aspects, HF, safety, training, and maintenance and support subject matter experts from both sides, and requirements management representatives. The HFIF(PT) chairs, or nominates a chair, ensures minutes and actions, and suggested Terms of Reference exist as HFI-TR02 in HuFIMS.
- The RAIDO split: the HFI RAIDO Register is concerned with low-level, day-to-day management of HFI considerations and is distinct from the project RAIDO or risk register that deals with major project risks; only significant considerations that will impact delivery of the programme as a whole should be raised to the project register. The register is maintained jointly for the contract's duration, and considerations close only with stakeholder agreement, with the justifying evidence referenced.
- Iteration as doctrine: a key tenet of User-Centred Design is the iteration of analysis, design and test, so results of test and evaluation activities are expected to trigger further analysis and design updates. There is no single prescribable set of HFI activities; what is needed depends on the relevant requirements and the identified and emergent considerations.

## Key Concepts

The Provider's HFI Plan is generated against the SRD and SOR, complying with HFI-PD03 unless otherwise agreed; sub-contractors whose contribution affects the human component produce their own HFI plans, synchronised with the main plan and the Systems Engineering Management Plan. The HFI Working Group reviews the plan first for management aspects, particularly integration of the HFI domains with the wider SE approach, then for detailed scheduling that supports planning user involvement; the HFIF(PT) approves the plan, and approval implies approval of the proposed process, not acceptance of the solution.

Conduct of activities falls into three families. Analysis: requirements analysis and derivation of sub-system requirements; workplace and environment analysis covering noise, vibration, lighting and thermal factors; task analysis and synthesis including cognitive tasks and decision-making; link analysis; allocation of function between humans and machines or autonomy; human performance modelling and prediction; human reliability analysis; training needs analysis; and maintenance space analysis. Design: application of HF standards to HCI and HMI design; modelling, prototyping, simulation and mock-ups; HCI and HMI design; workplace design with environmental specification; training design and fidelity analysis; contribution to the support solution; assessment of maintenance tasks; organisation design including numbers and information flows; and contribution to procedures and documentation. Test and evaluation: assessment of compliance against contracted and derived requirements; HF experiments and trials; manual handling assessment; human performance measurement; contribution to the safety case; assessment of procedures; and evaluation of training delivery. Requirements in the SRD can be high-level and may blend technology and people, so mixed requirements must be decomposed to expose the contributing human performance requirement.

The remainder of the stage is governance. Outcomes are reviewed at the HFI Working Group and assessed by the HFIF(PT) for acceptability against the technical requirement or mitigated risk. Design limitations emerging from trade-offs are MOD-owned considerations: if the CIWG accepts a limited anthropometric range of users, operator selection is affected, and the HFIF(PT) must work with the Personnel DLOD owner so the limitation is managed in recruitment and selection. Design changes, whether pushed by the HFI team for compliance or driven by other engineering domains, must be assessed for unintended consequences and impact on HF compliance before trade decisions. New or amended requirements are matured in the HFI Working Group before presentation to the RWG and CIWG, with negotiation over what is inside or outside the original contract's scope and price, and contract amendment where needed. HFI deliverables named in the source include the HFI Plan, the HFI Log, the HFI Case Report, the Task Analysis Report with task descriptions, the HMI and HCI Style Guide and Design Specification, and detailed test specifications and reports; HFI also inputs to use-case or system modelling, the project risk register, hazard identification and analysis, the safety case, the ITEA Plan, maintenance design, and training design. The HFIF(PT) liaises regularly with the HFI Policy team for assurance and provides input to the Support Solutions Development Tool and GEAR reviews under the Engineering Management Plan.

## Mental Models

- Two chairs, two registers: the HFI Working Group works the day-to-day register, and only escalates programme-level considerations upward.
- Approval is not acceptance: plan approval endorses the process; solution acceptance comes later, on evidence.
- The human is a decomposed requirement: blended system requirements hide human performance contributions until someone decomposes them.

## Key Takeaways

- HFI-4.0 is where MOD becomes the assurer and the Solution Provider the doer; the working group is the joint organ.
- All five domains are worked, with analysis, design, and test-and-evaluation activities chosen per risk, iterated per UCD.
- Documentation is an output of governance: the HFI Log, Case Report, style guides and test artefacts accumulate the audit trail that HFI-5.0 will test against.

## Connects To

Testing and acceptance of these outputs is ch08; the tender plan being executed was assessed in ch06 and written in ch05; the CIWG and RWG interfaces are described in ch02.
