# Cheatsheet

Decision rules, tailoring guidance, and selection criteria from the source, stated as prose rules rather than reproduced tables or page images.

## How much systems engineering? (risk-proportionality)

- Apply the process when a project shows risk; scale the detail to the risk, not to enthusiasm or paperwork habit. Even low-risk projects address every element: needs and requirements before design, then verification and validation.
- Grade seven factors low/medium/high: jurisdictions and modes involved; extent of software creation; maturity of hardware and communications technology; number and complexity of new interfaces; completeness of written requirements; completeness of written operating procedures; remaining service life of the technologies. Mixed grades concentrate attention on the high factors.
- Treat as low risk: expansions with no new capabilities, no new interfaces, no new software, proven technologies not near end of service life, documented needs. Treat as high risk: new software development, new interfaces, new operational practices, multi-agency systems, technologies approaching obsolescence.
- Low-risk routes to the required analysis: categorical systems engineering documents per project type; extending a system whose SE documents already exist; extracting elements from a maintained regional ITS architecture; FHWA Model Systems Engineering Documents for common field systems (signals, dynamic message signs, CCTV, sensors).
- Tailoring adjusts formality, never skips the substance: documented requirements, design, and verification procedures stay even on small projects. Write the tailored process down (PMP or SEMP) so everyone agrees on the steps.

## Choosing a life cycle model

- Sequential (waterfall or Vee): requirements well understood and stable, funding complete. Efficient, little recovery room if vision changes.
- Incremental: complete system planned and specified once; successive projects deploy phases. Field-equipment build-outs fit.
- Iterative/Agile: requirements unclear, capability can be delivered in increments, users available for frequent trials. Not for safety-critical functions, long-term-maintenance obligations, or heavy integration of disparate systems.

## Document set decision rules

- Custom software development is the biggest driver: it pushes a standalone SEMP. Hardware-only or purchased-product projects can fold SE content into the PMP.
- SEMP needed when: owner team inexperienced in SE, many deeply involved stakeholders, unclear solution, or custom software. Written in two steps: management framework, then performing-team detail.
- PMP carries tasks, WBS, budgets, schedule constraints (external first), deliverables list, referenced documents. Avoid duplicating PMP content in the SEMP; cross-reference instead.
- Requirements documentation: assign a verification method to every requirement at authoring time (test, demonstration, inspection, or analysis); track attributes (source, author, dates, verification method, priority, status); start the traceability matrix now, not at the end.
- Requirements tool threshold: roughly 100 or more system requirements justifies a requirements management or database tool installed and configured early, with training and stakeholder access; below that, a defined-schema spreadsheet is the low-cost route.
- Configuration management plan adequacy test: could another qualified team upgrade and maintain the system from the records alone? If not, the documentation is not done.

## Verification versus validation

- Verification asks "built the product right": each phase's outputs checked against the prior phase's requirements, ending in system verification against the requirements baseline.
- Validation asks "built the right product": the operational system checked against user needs, planned from a validation plan drafted with the Concept of Operations, often needing before-and-after data collected before deployment.
- Acceptance testing belongs to the trained operations team, documented in advance with expected results and failure handling; tie payment to outcomes where possible.

## Risk management rules

- Identify across seven areas: technical, schedule, cost or funding, institutional, personnel, environmental, commercial.
- Rank qualitatively on impact (catastrophic, critical, marginal, negligible) by likelihood; probability of failure grows with maturity risk (existing system through state of the art) and complexity risk (simple through extremely complex); multiple risks take at least the highest probability.
- Four response postures: mitigate with contingency, accept what cannot realistically be mitigated, avoid by changing requirements or design, transfer (insurance, fixed-price contract).
- A test process finding no defects may mean the testing is incomplete, not that the software is good.

## Trade study rules

- Fix objectives, then define and weight criteria before listing alternatives, so criteria are not biased toward a preferred choice; include a do-nothing base case.
- Evaluate against criteria (quantitatively or qualitatively), estimate lifecycle cost and schedule per alternative, drop alternatives with unacceptable cost or schedule risk, score in a matrix, document the selection and rationale, and validate the choice with stakeholders.

## Procurement selection rules

- RFI for market input before solicitation (cannot award); RFQ plus qualifications-based selection for engineering services where cost negotiates after selection; IDIQ task orders for recurring undetermined scope; RFP with best-value factors (documented and stated in the solicitation) for defined system builds; ITB for well-specified product purchases; P3 where private capital serves public goals.
- Delivery models: design-bid-build suits physical construction with proven local skill; design-build suits technology projects but risks underfunded SE inside a cost-competed contract; construction manager at risk with a guaranteed maximum price for early cost certainty.
- Self-perform SE only with adequate staffing, disciplined process adherence, and objective (independent) evaluation; otherwise contract SE performance, SE monitoring, or both, per phase.

## Regulatory analysis checklist (paraphrased seven elements)

1. Map the project to the portions of the regional ITS architecture being implemented (service packages, elements, information flows); fall back to the national architecture where no regional one exists.
2. Identify participating agencies and their roles and responsibilities.
3. Define the requirements (functional and performance, "what" not "how").
4. Analyze alternative system configurations and technology options.
5. State the procurement options considered for each project phase.
6. Identify applicable ITS standards and testing procedures (a standards report can be generated from regional architecture flows).
7. Define procedures and resources for operations and management across the life cycle.

Scale the analysis to project scope; demonstrate compliance per the FHWA Division Office or FTA Regional Office, commonly through a review form or checklist.
