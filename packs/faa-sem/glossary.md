# FAA Systems Engineering Manual — Glossary

Key terms from the FAA Systems Engineering Manual (SEM) v1.0.1, alphabetical, with chapter references. The SEM is the FAA's civil-agency SE process companion, wrapped around the Acquisition Management System (AMS) and the National Airspace System (NAS).

**Acquisition Category (ACAT)** — designation, set from dollar thresholds plus qualitative factors (program risk, complexity, political sensitivity, likely NAS safety impact), that scales the rigor of Investment Analysis. (Ch 1)

**Acquisition Management System (AMS)** — the FAA's 1996 acquisition policy framework that the SEM wraps SE around; covers strategic planning, budgeting, enterprise architecture, portfolio management, and investment decisions. Detailed policy lives in the FAA Acquisition System Toolset (FAST). (Ch 1)

**Acquisition Program Baseline (APB)** — the cost/schedule/performance contract binding three parties (the investment decision authority, the service organization that implements the solution, and the community of users); finalized just before the Final Investment Decision. Critical Performance Requirements are copied into it verbatim. (Ch 1, Ch 3)

**Allocated baseline** — the design-requirements baseline, typically set after the System Requirements Review; second of the five FAA baselines. (Ch 5)

**Architectural Design Synthesis** — SEM 3.4 process that turns requirements (framed by the functional architecture) into a physical architecture by developing alternatives, allocating requirements, and evaluating alternatives on cost/schedule/performance/risk. (Ch 3)

**Availability (Inherent Ai / Equipment-and-Service Aes / Operational Aop)** — three availability constructs: Ai is the theoretical hardware-only maximum; Aes adds unscheduled outages, logistics, and administrative delay but excludes scheduled downtime; Aop includes all downtime. The SEM rejects availability as a primary contractual requirement for software-intensive systems. (Ch 6)

**Baseline (CM)** — a dated, agreed-to description of a product's attributes that serves as the reference for managing change. The five FAA baselines are Functional, Allocated, Product, Facility, and Operational. (Ch 5)

**Concept Maturity Level (CML 1–4)** — maturity scale giving a shared read on a concept's developmental status; drives funding allocation, aligns NextGen research priorities, and tracks progress. (Ch 2)

**Concept of Operations (ConOps)** — the primary repository for a concept's assumptions, constraints, and operational environment, written from the user's point of view; exists at Service, NAS, and Solution levels, with lower levels kept consistent with higher ones. (Ch 2)

**Configuration Control Board (CCB)** — FAA-authorized forum that establishes CM baselines and adjudicates changes; the NAS CCB (chartered by the JRC) is the highest-ranking board. (Ch 5)

**Configuration Control Decision (CCD)** — the legally binding FAA notice of a CCB's decisions and directives; its closure marks completed change implementation. (Ch 5)

**Configuration Management (CM)** — discipline that holds the *product* truth version-by-version under board control; governed by FAA Order 1800.66 and enforced by CCBs. (Ch 5)

**Critical Performance Requirements (CPR)** — the minimal set of make-or-break performance attributes, written as Mature Requirements Statements, copied verbatim into the APB; their V&V status gates milestone approvals. (Ch 3, Ch 5)

**Decision Analysis (DA)** — structured method for choosing among alternatives using documented criteria, weights, and a Decision Report; tool-agnostic (Pugh, QFD, TOPSIS, decision trees, M&S, etc.), with technique fidelity matched to decision stakes. (Ch 5)

**Decision point** — formal AMS gate concluding a lifecycle phase; demands a defined set of completed activities and an approved documentation package. The five numbered decision points punctuate the AMS lifecycle. (Ch 1)

**E3 (Electromagnetic Environmental Effects)** — the bidirectional, environment-relative discipline covering EMC, susceptibility, RADHAZ, EMP, ESD, lightning, and precipitation static; FCC compliance (mostly Class A for NAS devices) is necessary but not sufficient for operational compatibility. (Ch 6)

**EOSH (Environmental, Occupational Safety and Health)** — the integration of environmental, occupational-safety, and sustainability mandates into acquisition; managed bidirectionally and cradle-to-grave. (Ch 7)

**Functional Analysis** — SEM 3.2 process that dissects a ConOps into implementation-free functions, sub-functions, and interfaces; functions are *not* allocated — requirements derived from them are. Output is the Functional Architecture Document. (Ch 2)

**Functional Architecture Document (FAD)** — the seven-part output of Functional Analysis (context diagrams, functional hierarchy, functional flow, N² diagrams, interface list, lexicon, acronyms); a living document maintained across the lifecycle. (Ch 2)

**Functional Flow Block Diagram (FFBD)** — the FAA's preferred time-sequenced "control" diagram; verb-noun functions as nodes with AND / Exclusive-OR / Inclusive-OR logic. Complemented by the N² diagram for "data". (Ch 2)

**Hazard** — any condition, actual or potential, that can injure, sicken, or kill; damage or destroy a system, equipment, or property; or harm the environment; the unit of System Safety work. (Ch 7)

**Human Factors Engineering (HFE)** — specialty discipline treating operators and maintainers as first-class system elements; uses the Human Performance Interfaces taxonomy and 24 Areas of Interest, and feeds human-reliability analysis back into RMA. (Ch 6)

**In-Service Decision (ISD)** — the fifth AMS decision point, gating the move into operational service. (Ch 1, Ch 6)

**Information Security Engineering (ISE)** — specialty discipline managing risk to IT confidentiality, integrity, and availability; anchored in FISMA, FIPS 199/200, the NIST RMF, and FAA Order 1370.82A's Security Authorization process. (Ch 7)

**Integrated Logistics Support (ILS / NAILS)** — the nine-element supportability discipline (maintenance planning, support facility, staffing, supply, support equipment, training, technical data, PHS&T, computer resources) tied to each AMS phase. (Ch 6)

**Integrated Multidisciplinary Team (IMT)** — the cross-discipline team of stakeholders, SMEs, and engineers within which the systems engineer acts as catalyst; triggers and tailors Decision Analysis. (Ch 4, Ch 5)

**Integrated Systems Engineering Framework (ISEF)** — the guidance source for which enterprise-architecture products an initiative needs; NAS/NextGen architecture views are documented in ISEF (based on DoDAF). (Ch 1, Ch 3)

**Integrated Technical Management (ITM)** — the "plan + control" technical-management discipline producing the SEMP, ISPD, and Life Cycle Plan, then monitoring via TPM/CPR/EVM and controlling via reviews and audits. (Ch 4)

**Interface Control Document (ICD)** — controls interface *design* (the as-built solution); usually vendor-produced; must comply with the IRD. (Ch 4)

**Interface Requirements Document (IRD)** — controls interface *requirements* in verifiable terms; placed under CM; must stay aligned with the final Program Requirements Document. Governed by FAA-STD-025f. (Ch 4)

**Interface Working Group (IWG)** — the body that controls interface change via the Interface Change Request (ICR). (Ch 4)

**Joint Resources Council (JRC)** — the FAA investment-decision authority that approves key SE products (e.g., the FAD) and charters the NAS CCB. (Ch 1, Ch 2, Ch 5)

**Life Cycle Engineering (LCE)** — six-step supportability/cost discipline mapped onto AMS phases; premise is that early decisions lock in most lifetime cost, dominated by support. (Ch 6)

**Mature Requirements Statement (MRS)** — a complete specification sentence synthesized from a Primitive Requirements Statement; carries a paragraph number, directive verb, and verification reference. (Ch 3)

**Measure of Effectiveness / Performance (MOE / MOP)** — MOEs measure outcomes; MOPs measure outputs; TPMs derive from MOPs and are kept few. (Ch 3)

**N² (N-squared) diagram** — an N×N matrix with entities on the diagonal and interface inputs/outputs off-diagonal; captures the "data" side of a complete functional model and pinpoints interface conflicts. (Ch 2, Ch 4)

**NAPRS service** — a National Airspace Performance Reporting System service (FAA Order 6040.15) against which Service Threads are defined; lets NAS-level requirements tie to real fielded services. (Ch 6)

**NAS Change Proposal (NCP)** — the internal vehicle for requesting changes to FAA-managed NAS baselines; processed through the National CM support tool. (Ch 1, Ch 5)

**NextGen (Next Generation Air Transportation System)** — the comprehensive NAS modernization the SEM is written to support; the reason the NAS is treated as an evolving System of Systems. (Ch 1)

**PDCA (Plan-Do-Check-Act)** — Shewhart/Deming continuous-improvement cycle the systems engineer may overlay on iterating processes; structures SEIM activities. (Ch 1, Ch 5)

**Plan strategy (RIO)** — the chosen response for a risk: Avoid, Transfer, Control (most common), Accept, or Research and Knowledge. (Ch 4)

**Primitive Requirements Statement (PRS)** — a requirement captured in punctuation-free `Name + Relation + Value` form; first assigned to a function, then matured into an MRS. (Ch 2, Ch 3)

**Probability Impact Diagram (PID)** — the matrix used to show aggregate RIO status. (Ch 4)

**Product baseline** — the delivered configuration, established only after both the Functional Configuration Audit (FCA) and the Physical Configuration Audit (PCA) pass; third of the five FAA baselines. (Ch 5)

**Program Requirements Document (pPRD → iPRD → fPRD)** — the maturing requirements document series; an approved fPRD with an 80%-stable set gates a full investment decision. The enterprise level sits in the NAS-RD. (Ch 3)

**Quality Management System (QMS)** — the always-present system of policies, processes, and procedures over which the seven technical management disciplines run; the government may require a contractor have one but generally cannot dictate which. (Ch 4)

**Requirements Allocation Matrix (RAM)** — two-way traceability from physical architecture ↔ requirements ↔ functional architecture; minimally carries function ID/name, the derived requirement, and the implementing component. (Ch 3)

**Requirements Analysis** — SEM 3.3 process = Requirements Development + Requirements Management; develops functional/performance requirements from the functional architecture and controls them under CM. (Ch 3)

**Research for Service Analysis (RSA)** — a non-phase activity recurring across phases that feeds Service Analysis, drawing on the RE&D and CMTD portfolios to mature concepts and reduce risk. (Ch 1, Ch 2)

**Risk / Issue / Opportunity (RIO)** — the FAA's unified treatment of three objects (future-negative Risk, realized/certain-negative Issue, future-positive Opportunity) run through one five-step process; issues skip likelihood scoring. (Ch 4)

**Risk Management Board (RMB)** — the governance body that dispositions RIO items per a defined status lifecycle (Watch Item → … → Closed/Retired/Realized). (Ch 4)

**RMA (Reliability, Maintainability, Availability)** — the dependability-over-time specialty; allocated top-down through Service Threads for software-intensive information systems, and by lifecycle-cost/expert judgment for distributed and infrastructure systems. (Ch 6)

**Safety Risk Management (SRM)** — the SMS five-phase loop: (1) describe the system; (2) identify its hazards; (3) analyze each risk; (4) assess that risk; (5) treat — mitigate — it. (Ch 7)

**Security Authorization** — the FAA process (FAA Order 1370.82A) under which every system is categorized and assessed before going operational; residual risk is accepted by the Authorizing Official and worked down via POA&Ms. (Ch 7)

**Service Thread / STLSC** — a reliability block diagram of all "sensor-to-glass" equipment delivering a NAPRS service, classified by Service Thread Loss Severity Category (Essential .9999, Efficiency-Critical .99999, Safety-Critical split into two independent .99999 threads). (Ch 6)

**Shortfall** — the gap between future service needs and current capability; stated early as a level-of-service improvement and documented in the ConOps as Operational Improvements / Sustainments. (Ch 2)

**Specification (Type A / B / C)** — Type A System Specification (FAA-E spec per FAA-STD-067, baselined at SRR), Type B Development Specification (baselined at PDR), Type C Product Specification (baselined at CDR). (Ch 3)

**Systems Engineering Information Management (SEIM)** — the FAA's deliberate rename of INCOSE Information Management; a PDCA cycle over acquire → validate → maintain → distribute → archive → retire. (Ch 5)

**Systems Engineering Management Plan (SEMP)** — the master document integrating all SE activities with cost/performance/schedule; exists as a Program SEMP and a Contractor's SEMP (CSEMP). (Ch 4)

**System of Systems (SoS)** — independently purposed, independently operated systems whose union produces emergent capability; networking can introduce new vulnerabilities, so assurance properties must be reassessed. (Ch 1)

**System Safety Engineering (SSE)** — specialty discipline identifying, evaluating, and controlling hazards via the SMS Manual and SRMGSA; produces the OSA/CSA/PHA/SSHA/SHA/O&SHA ladder culminating in the SSAR. (Ch 7)

**Technical Performance Measurement (TPM)** — quantitative tracking of a critical parameter's maturation toward its target value over time; an early-warning trend, not a snapshot. (Ch 3, Ch 4)

**Verification & Validation (V&V)** — verification confirms the product was "built right" (incremental, against requirements); validation confirms "the right product" was built (iterative, early, against the ConOps/EA). Anchored in the V model, the VRTM, and the AMS V&V Guidelines. (Ch 5)

**Verification Requirements Traceability Matrix (VRTM)** — the matrix tying every requirement to a verification method (Inspection, Analysis, Demonstration, Test); part of every FAA requirements/specification document. (Ch 3, Ch 5)

**Work Breakdown Structure (WBS)** — defines total project scope (rule of thumb: 3–4 tiers deep, 5–9 elements wide); treated as the evolving core of the SEMP rather than a frozen waterfall. (Ch 4)
