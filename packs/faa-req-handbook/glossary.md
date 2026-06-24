# FAA Requirements Engineering Management Handbook — Glossary

Key terms from the Handbook, alphabetical, with the chapter where each is treated
most fully. Definitions are synthesized in original words; they describe the
Handbook's usage, which is slanted toward real-time, embedded avionics systems.

- **Accuracy (input/output)** — the bound on how far a software-read input may deviate from the true monitored value, or how far a controlled variable may diverge from its ideal; specified against the *controlled* variable for outputs, not the output variable. → ch06
- **Allocation (subsystem)** — splitting a system specification into independently developable subsystem specifications by assigning functions to subsystems and exposing the parent's internal variables as new boundary variables. → ch06
- **Alternate course** — a different-but-valid path through a use case that still meets the postconditions; written as an extension of the main scenario. → ch03
- **And/or table** — the tabular specification format used by RSML and SpecTRM to capture the ideal value function. → ch05
- **Black box** — the system viewed with no internal structure exposed; the stance taken by the context diagram and by operational concepts. → ch02, ch03
- **CoRE (Consortium Requirements Engineering)** — the Software Productivity Consortium's extension of SCR/four-variable ideas (used on the C-130J); the source of much of the Handbook's organizing guidance and of the ideal-value/tolerance/latency decomposition. → ch01, ch04, ch05
- **Completeness** — every controlled and internal variable has an assigned ideal value for every system state; gaps are closed or marked UNSPECIFIED. → ch05
- **Consistency** — no system state is assigned two different ideal values; a `<` versus `<=` slip at a boundary is the classic violation. → ch05
- **Context diagram** — a high-level graphic, one per life-cycle context, showing the system as a black box surrounded by its external entities and their interactions. → ch02
- **Controlled variable** — an environmental quantity the system affects directly; one half of the system boundary. → ch02
- **Deadband / hysteresis** — a band around a threshold within which an output is held unchanged to suppress chatter (e.g. the heater and alarm bands in the Isolette). → ch08
- **Dependency diagram** — the graphic that opens the context-diagram black box to show system functions and the variables flowing between them; serves as a graphical table of contents for the detailed requirements. → ch04
- **Derived requirement** — a requirement with no direct trace to a higher-level one (per DO-178B/DO-248B); design choices affecting visible behavior or safety must be flagged as derived and routed to the safety assessment. → ch06
- **Environmental assumption** — an obligation the system places on its world, expressible as a relation over monitored/controlled variables; the precondition half of the requirements contract. → ch03
- **Exception case** — a way a use case fails to meet its goal or postconditions; written as an extension of the main use case. → ch03, ch04
- **External entity** — an operator, neighboring system, sensor, or actuator the system interacts with across its boundary; assumptions are organized around these. → ch02, ch03
- **FHA (Functional Hazard Assessment)** — the safety analysis that names high-level system hazards; drives architecture revision for safety-critical systems. → ch04
- **Fault tree** — the PSSA artifact that apportions failure-probability budgets down to the functions that could cause a hazard. → ch04
- **Four-variable model** — Parnas and Madey's MON/CON plus NAT/REQ frame (via SCR); the formal bridge from system requirements to software requirements. → ch06, ch01
- **Functional architecture** — a recursive grouping of system functions (and the data flowing between them) that organizes the requirements and supplies their traceability. → ch04
- **Goal (system goal)** — an informal statement of stakeholder need; explicitly *not* a requirement (unverifiable, underspecified), but a source of rationale and a trace target. → ch02
- **Hazard (H-numbered)** — an identified condition that could cause harm, classified by severity with a target probability; safety requirements are derived to mitigate it. → ch04, ch08
- **Ideal value function** — the value a perfect system would assign to a controlled or internal variable in every state; the behavioral core of a detailed requirement. → ch05
- **IN / OUT relations** — how each software input relates to monitored variables (IN) and each controlled variable to outputs (OUT), each carrying an ideal-value function, latency, and accuracy. → ch06
- **IN' / REQ' / OUT' (extended software requirements)** — the split of the raw software relation: IN' recreates monitored-variable images, OUT' drives outputs from controlled-variable images, REQ' reuses the system's ideal value function unchanged. → ch06
- **Internal variable** — a variable introduced to name a data dependency between functions; carries no timing/accuracy promise, so latency and tolerance are never specified for it. → ch04, ch05
- **Intent specification** — a SpecTRM structure carrying rationale continuously from top-level goals down through the model to implementation and operator training. → ch01
- **Latency** — the maximum lag allowed between a monitored variable changing and the affected controlled variable taking its new value; always carries a rationale. → ch05
- **Main success scenario ("sunny day")** — the nominal use-case dialogue in which nothing fails; documented first, with failures added later. → ch03
- **Mode** — an externally visible discontinuity in behavior: the same stimulus produces different responses in different modes (e.g. INIT / NORMAL / FAILED). → ch05
- **Mode confusion** — a safety hazard in which operators lose track of which mode the system is in; tied to real aviation accidents. → ch05
- **Monitored variable** — an environmental quantity the system senses directly; the other half of the system boundary. → ch02
- **MON / CON / NAT / REQ** — the four-variable sets: monitored quantities, controlled quantities, the environment's natural relationship (assumptions), and the required MON-to-CON relationship. → ch06
- **MON' / CON'** — the software's recreated images of the monitored/controlled variables; always slightly delayed and deviated from the real quantities (the prime mark is the reminder). → ch06
- **NAT relationship** — the natural relationship the environment maintains that the system depends on; the SCR/CoRE name for environmental assumptions. → ch03
- **Operational concept** — a black-box usage scenario (typically a textual use case) bridging the system overview and the detailed requirements; surfaces overlooked functions and variables. → ch03
- **Physical interface** — the concrete, low-altitude, volatile means of sensing and actuating (discrete I/O, messages, fields, protocols); defined separately from the abstract boundary variables. → ch02
- **Postcondition / precondition** — what must hold after / before a use case; mapped to the requirement/assumption contract that enables independent component development. → ch03
- **PSSA (Preliminary System Safety Assessment)** — determines whether a function could realize a hazard and levies derived safety requirements and probability budgets. → ch04
- **Rationale** — the *why* behind a requirement, assumption, or value; non-binding, never verified, kept separate from the requirement, and cited as the most cost-effective single practice. → ch07
- **REQ relationship** — the input-to-output mapping the system must maintain between monitored and controlled variables. → ch05, ch06
- **Recommended practice** — one of the Handbook's eleven main-level practices (each with sublevels), presented in rough execution order and meant to be tailored. → ch01
- **RSML / RSML-e / SpecTRM** — Leveson-lineage notations (used on TCAS II) for specifying and formally analyzing requirements; SpecTRM extends RSML inside an intent specification. → ch01
- **Safety requirement (SR)** — a requirement derived from a hazard via the FHA/PSSA chain, each carrying an allowed failure probability. → ch08, ch04
- **SCR (Software Cost Reduction)** — the NRL methodology (originating on the A-7E) behind the four-variable model and the tabular formats; a primary source of the Handbook. → ch01, ch06
- **Status attribute** — a health flag on a monitored variable (e.g. Valid/Invalid, unknown/stale) so the system behaves correctly when data is untrustworthy; initialized so the variable is not trusted until first sensed. → ch03, ch06
- **System boundary** — the dividing line between the system and its world, defined concretely as the set of monitored and controlled variables (not an org-chart box). → ch02
- **System overview** — the introductory artifact (synopsis, contexts, external-entity descriptions, goals) that orients a new reader; created early, kept high-level. → ch02
- **Tabular specification (condition / event / mode tables)** — SCR/CoRE table formats that make completeness and consistency checkable by inspection. → ch05
- **Tolerance** — the acceptable deviation from the ideal value for a *numerical* controlled variable; N/A for Boolean/enumerated variables. → ch05
- **Traceability** — the property that lower-level requirements link to higher-level ones; here supplied largely by the functional-architecture structure and by duplicating allocated requirements. → ch04, ch06
- **UNSPECIFIED** — an explicit marker that a variable has no meaningful value in some state; documented so consumers know not to trust it (information, not omission). → ch05, ch08
- **Use case** — the Handbook's preferred vehicle for operational concepts: actors, primary actor, preconditions, postconditions, main success scenario, exceptions; traced to goals and linked to functions. → ch03
- **What, not how** — the dividing line between requirements and design (the Parnas criterion): say everything needed for the correct system and nothing more. → ch01
