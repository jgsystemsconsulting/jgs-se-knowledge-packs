# NASA NPR 7150.2D Patterns & Techniques

Reusable techniques for applying NPR 7150.2D. Each pattern is grounded in the
directive's requirements; none invents process the source does not contain.

## Pattern 1: Classify First, Then Map Requirements

**When to use**: At the start of any NASA software effort, and again whenever a system or subsystem changes in intended use, criticality, or investment.

**How**: Classify each system and subsystem containing software at the highest applicable class (SWE-020), using Appendix D and its five factors — usage with/within a NASA system, system criticality, human dependence, developmental/operational complexity, and Agency investment. Then read the applicable, "X"-marked requirements for that class out of the Appendix C Requirements Mapping Matrix. Almost everything else (CMMI level, traceability links, cost-model count, IV&V applicability) is downstream of the class.

**Trade-offs**: Classifying too low under-applies assurance to something that needed it; classifying too high adds avoidable rigor. The directive resolves ambiguity by rounding up, so when two classes both fit, take the higher one and document the rationale.

---

## Pattern 2: Tailor Through the Requirements Mapping Matrix, Not Around It

**When to use**: Whenever a project cannot or should not meet an applicable requirement as written.

**How**: Treat relief as an evidence package, not an omission. Capture the requirement, the rationale, a risk evaluation, and any mitigations in the Requirements Mapping Matrix; obtain the signature of the authority named for that requirement in Appendix C; get concurrence from every impacted discipline (safety, quality, cybersecurity, health); and have the responsible program/project/operations manager formally accept the residual risk. For human-safety risk, the actual risk takers (or their spokesperson and supervisory chain) must agree to assume it.

**Trade-offs**: The signature-and-concurrence chain is deliberate friction; it stops a deviation in one discipline being granted in isolation. Skipping it produces an unbacked compliance claim that fails audit.

---

## Pattern 3: Hold Acquired and Generated Code to the Developed-Code Bar

**When to use**: Whenever software is bought (COTS/GOTS/MOTS/OSS), reused, or auto-generated rather than freshly written.

**How**: For off-the-shelf and reused components (SWE-027), identify which requirements they meet, ensure adequate documentation, resolve license/ownership/proprietary questions with Center Intellectual Property Counsel, plan future support, verify and validate to the *same level* as an equivalent developed component, and periodically review vendor-reported defects. For auto-generated code (SWE-146), define the approach including tool V&V, configuration management of tools and inputs/outputs, scope limits, manual-change policy, and V&V of the generated code under the same standards as hand-written code.

**Trade-offs**: Changing the *source* of code never lowers the *bar* for it, so "we just bought it" buys no V&V relief. The cost is real assurance work on third-party code; the alternative is unassessed risk riding into a mission system.

---

## Pattern 4: Layer Safety-Critical Behavior Plus Quantitative Gates

**When to use**: When a component is determined safety- or mission-critical per the NASA-STD-8739.8 criteria (SWE-205).

**How**: Implement the behavioral safe-state requirements (SWE-134): initialize to a known safe state at start and restart, transition safely between predefined states, terminate to a safe state, require two independent operator actions for hazardous overrides, reject out-of-sequence hazardous commands, detect and recover from inadvertent memory modification, perform I/O integrity and prerequisite checks before safety-critical commands, ensure no single event initiates a hazard, and respond to off-nominal conditions in time to prevent harm. Reinforce with the hard gates: 100% MC/DC coverage (SWE-219) and cyclomatic complexity ≤ 15, with any exceedance reviewed and waived with rationale (SWE-220). Prefer an independent party to design and run the safety-critical testing.

**Trade-offs**: Defense in depth costs design and test effort; the complexity ceiling can force refactoring. That is the intent — high-complexity safety paths raise testing burden and failure risk exactly when a hazard is in play.

---

## Pattern 5: Build the Bidirectional Traceability Spine by Class

**When to use**: From requirements definition onward, scaled to the software class (Table 1 in Chapter 3).

**How**: Establish traceability running both directions across the element chain (SWE-052): higher-level requirements to software requirements, requirements to system hazards, requirements to design components, design components to code, requirements to verifications, and requirements to non-conformances. Read Table 1 to see which links are mandatory for Class A/B/C versus Class D versus Class F, and instrument the toolchain to keep the links current rather than reconstructing them at a review.

**Trade-offs**: A complete spine is bookkeeping overhead, but a break in it — a requirement with no test, code with no requirement — is itself a defect to reconcile, and the coverage triage (Pattern 7) depends on the spine being intact.

---

## Pattern 6: Treat Tools and Build Environments as Configuration Items

**When to use**: Throughout the life cycle, the moment software configuration management is established (SWE-081/082).

**How**: Put under control not only source code but the records, data, models, scripts, and — critically — the tools and settings that build the software: compiler/assembler versions, makefiles, batch files, and specific environment settings. Define the control levels each item passes through, name who may authorize a change, and separately name who may make it (SWE-082). Validate and accredit critical development and analysis tools so they cannot silently inject defects (SWE-136).

**Trade-offs**: Capturing the build environment in the configuration ledger adds setup effort, but a reproducible build is impossible without it, and an unaccredited tool can corrupt otherwise-correct work.

---

## Pattern 7: Triage Coverage Gaps Into Four Causes

**When to use**: Whenever structural code coverage falls short of 100% (SWE-189/190).

**How**: Do not read uncovered code as merely "missing tests." Classify each gap into one of four causes — a missing requirement, a missing test, extraneous/dead code, or deactivated code — because each demands a different corrective action by the project manager. A missing requirement means the spec is incomplete; a missing test means add the test; dead code means remove or justify it; deactivated code means document and guard it. Verify coverage by analyzing actual test-execution results, not by inspection.

**Trade-offs**: The triage converts a single coverage number into a structured investigation, which costs analysis time but turns a metric into actionable diagnosis instead of a number to be gamed.

---

## Pattern 8: Weave Cybersecurity Through Development, Not Onto It

**When to use**: Across the full life cycle for flight and ground software, especially systems with communications capability.

**How**: Treat ordinary coding defects (buffer overflows, inconsistent error handling) as security weaknesses, not just quality issues. Perform cybersecurity assessments that include risks from off-the-shelf and reused components (SWE-156), identify and plan mitigations for flight and ground systems (SWE-154), test and record mitigation results (SWE-159), identify and implement secure coding practices (SWE-207), verify code against the secure coding standard using static analysis (SWE-185), and define data collection and reporting for adversarial-action detection (SWE-210). For communications-capable systems, apply NASA-STD-1006 protection (SWE-157).

**Trade-offs**: Security woven through development is harder to defer or cut than a bolt-on review, which is the point; it raises ongoing engineering load but closes the gap where late security checks routinely miss design-level flaws.

---

## Pattern 9: Run the Supporting Disciplines Continuously, Not as Phases

**When to use**: Across the entire life cycle, in parallel with the phased engineering work.

**How**: Operate the five Chapter 5 disciplines as continuous services rather than one-time gates: configuration management (with custody rules and audits), software risk management (tracking residual risk after mitigation), peer reviews and inspections (instrumented with entry/exit criteria, a reading technique, tracked actions, and recorded measures), the multi-level measurement program (project → Center → Chief Engineer, with margins and requirements-volatility tracked), and non-conformance management (severity-classified, with a closed-loop process assessment on every high-severity issue).

**Trade-offs**: Continuous operation costs steady effort rather than spiky milestone effort, but a high-severity non-conformance is only truly closed when the process that allowed it is assessed — fixing only the product leaves the cause in place.

---

## Pattern 10: Treat Records as a Tailored, Reader-First Menu

**When to use**: When deciding which software records to produce and what they contain (Chapter 6).

**How**: Start from the users and stakeholders who will rely on a record — their needs and background determine its content — then select from the typical product menu (plans, specifications, test artifacts, version descriptions, reuse and trade-study records, and so on) only what the project actually needs. Use NASA-HDBK-2203 for content and timing and the SPAN library for examples and templates. Accept Center or contractor formats as long as the required content is present, and review and update records as living artifacts.

**Trade-offs**: Tailoring the record set risks omitting something a downstream reader needed, so justify omissions against stakeholder need rather than convenience; over-producing every record by reflex wastes effort the directive explicitly does not demand.
