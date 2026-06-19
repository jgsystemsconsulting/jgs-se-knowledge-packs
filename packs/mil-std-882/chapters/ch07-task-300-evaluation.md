# Chapter 7: Task Section 300 — Evaluation Tasks

## Core Idea
The 300-series tasks translate accumulated hazard analysis and mitigation work into programme-level assessments of readiness and safety status. They are checkpoint tasks: executed before test events, at major programme transitions, during T&E, and in response to engineering changes. Evaluation tasks do not discover new hazards (that is the role of Task 200 analysis) — they synthesise what is known, verify mitigation effectiveness, and ensure that formal risk acceptance decisions are current and documented.

## Frameworks Introduced

- **Task 301 — Safety Assessment Report (SAR)**: comprehensive evaluation of hazard status and associated risks prior to system test, next contract phase, or contract completion; includes HTS data, analysis/test results, HAZMAT summary, event-unique mitigations, and a readiness statement.
  - When to use: before any significant test or operational event, before phase transitions, at contract completion; the SAR is a system safety-specific assessment.

- **Task 302 — Hazard Management Assessment Report (HMAR)**: parallel to the SAR but scoped to cover all functional disciplines using the MIL-STD-882E methodology; includes HAZMAT detail (material type, quantities, precautions, disposal, explosives classifications, EOD requirements) in addition to SAR content.
  - When to use: when the programme uses the HMP (Task 103) rather than the SSPP (Task 102), or when multiple functional disciplines require consolidated hazard status reporting.

- **Task 303 — Test and Evaluation Participation**: active contractor involvement in T&E planning, Safety Release preparation, post-test analysis, and repository maintenance; ensures safety hazards are characterised and communicated to test personnel before and after each test event.
  - When to use: any programme with developmental or operational test and evaluation activity; links the safety programme to formal T&E processes (TES, TEMP).

- **Task 304 — Review of Engineering Change Proposals, Change Notices, Deficiency Reports, Mishaps, and Requests for Deviation/Waiver**: applies the 8-element system safety process to each engineering change, deficiency report, mishap, and waiver/deviation request to identify new or modified hazards and ensure risk is formally accepted before changes are implemented.
  - When to use: any programme with configuration control or change management processes; the safety safety gate on all post-design-freeze changes.

## Key Concepts

- **Safety Release**: the T&E planning document (part of Task 303) that identifies known system hazards for a given test event, recommends test-unique mitigations, and communicates risk acceptance status to test operators, maintainers, and testers before the event.
- **SAR readiness statement**: every SAR must include a summary statement addressing the system's readiness to test, operate, or proceed to the next acquisition phase — this is the safety community's formal "go/no-go" input to programme decision authorities.
- **Event-unique mitigations**: temporary or event-specific risk reduction measures (e.g., test range clearance zones, special PPE requirements for a test event) that are documented in the SAR or HMAR and must be applied during the event.
- **ECP/Change notice safety review (Task 304)**: every engineering change must be assessed for new hazards or modifications to existing risk levels before implementation; hazards identified through change review are added to the HTS.
- **Deficiency report hazard review (Task 304)**: each hardware or software deficiency report is reviewed for potential new hazards or changes to existing risk levels; software deficiencies that could affect safety-significant functions receive full system safety process application.
- **Mishap analysis obligation (Task 304 and 4.3.8)**: programmes must support Class A and Class B mishap investigations by providing analysis of contributing hazards and recommending materiel mitigation measures, with particular emphasis on minimising human errors.
- **Post-test event actions (Task 303)**: after each test event, the contractor must analyse test results for mitigation effectiveness, new hazard identification, and updated risk assessments; findings are fed back into the HTS.
- **T&E repository**: Task 303 requires a repository of T&E results (hazards identified, V&V records, mishap/discrepancy reports with corrective actions) to be maintained and transferred to the Government at contract end.

## Mental Models

- **"Evaluation tasks are the safety programme's periodic health checks"** — the SAR and HMAR are retrospective summaries of everything discovered and done; the readiness statement is the prospective judgment about whether it is safe to proceed.
- **"T&E is both a verification opportunity and a hazard exposure"** — Task 303 treats T&E as the event where planned mitigations are verified AND as an event with its own unique hazard profile requiring separate risk characterisation and acceptance.
- **"Every change is a new PHA in miniature"** — Task 304 requires the full 8-element process to be applied to every ECP, change notice, deficiency, and waiver; the assumption that a change is safety-neutral until proven otherwise is explicitly non-compliant.

## Anti-patterns

- **Writing a SAR at contract completion only**: the standard specifies the SAR is produced "prior to test or operation of a system, before the next contract phase, or at contract completion" — each test event and phase transition is a potential SAR trigger, not just programme close-out.
- **Treating T&E participation as observer-only**: Task 303 requires active participation in TES/TEMP preparation, Safety Release development, and post-test analysis — the safety team is a contributor to T&E planning, not a reviewer of its outputs.
- **Approving ECPs without safety review**: Task 304 explicitly applies the system safety process to every ECP; programmes that process changes through a purely engineering/configuration management path without safety input are non-compliant.

## Key Takeaways

1. SAR (301) and HMAR (302) serve the same programme purpose (hazard status assessment) but differ in scope: SAR is system-safety-discipline-specific; HMAR is multi-discipline and includes more HAZMAT and explosives detail.
2. The Safety Release (Task 303) is the specific document that communicates test-event hazard status to all test participants before the event — it is the T&E counterpart to a formal risk acceptance decision.
3. Task 304 creates a mandatory safety gate on all configuration change processes; it is the primary mechanism preventing post-design risk elevation from going unnoticed.
4. Mishap data from similar systems (Task 304.d) must be reviewed to refine risk assessments and identify previously unknown hazards — lessons learned from analogous systems are a required input, not optional background reading.
5. The T&E repository (Task 303) is a Government deliverable at contract end; its maintenance through the programme is a continuous obligation, not a final deliverable project.

## Connects To

- **Chapter 3 (Risk Assessment)**: SAR/HMAR must cite the specific risk matrix used and summarise all RACs; task 304 re-applies the risk assessment process to every change.
- **Chapter 6 (Task 200 — Analysis)**: evaluation tasks aggregate and summarise analysis outputs; the HTS data that SAR/HMAR draw on is populated by 200-series analysis tasks.
- **Chapter 8 (Task 400 — Verification)**: Task 401 (Safety Verification) provides the V&V evidence that SAR/HMAR report on; T&E participation (Task 303) overlaps with safety verification in test contexts.
- **DoDI 6055.07**: defines Class A and Class B mishap categories referenced in Task 304 and Section 4.3.8 mishap support obligations.
