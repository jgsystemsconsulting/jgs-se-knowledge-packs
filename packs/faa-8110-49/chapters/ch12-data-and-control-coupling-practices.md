# Chapter 12 - Data and Control Coupling Practices

Sources: S4 AC 00-69, Best Practices for Airborne Software Development Assurance Using EUROCAE ED-12( ) and RTCA DO-178( ) (2017-07-21), section 3.2, lines 69-79 of `sources/text/S4.txt`. Best practices, not guidance, and not an acceptable means of compliance. Complements ED-94C/DO-248C FAQ #67 for satisfying objective A-7 (8) of ED-12C/DO-178C and ED-12B/DO-178B; those items are named by designation only.

## Core Idea

AC 00-69 section 3.2 clarifies data coupling and control coupling as complementary best practices. The AC is not guidance and not an acceptable means of compliance. Data coupling analysis and control coupling analysis differ in type and purpose; both are necessary for the verification objective the AC points at. Although the analyses support a verification objective, they depend on design-phase discipline: specify interfaces (inputs and outputs) and dependencies between components early, or the later verification work has nothing solid to measure against. Industry pointers named here by designation only: ED-94C/DO-248C FAQ #67, and objective A-7 (8) of ED-12C/DO-178C (and ED-12B/DO-178B). This pack does not paste FAQ text and does not reproduce objective tables.

## Frameworks Introduced

- **Two analyses, one objective.** Data coupling and control coupling are separate analyses. Completing only one does not satisfy the objective the AC associates with both.

- **Design-phase enablement of a verification objective.** Interface (I/O) specification and component-dependency specification during design are the upstream practices that make the coupling verification objective reachable.

- **Designation-only industry anchors.** ED-94C/DO-248C FAQ #67 is the supporting-information pointer; objective A-7 (8) of ED-12C/DO-178C (and the ED-12B/DO-178B counterpart) is the verification objective named by the AC. Read those documents for normative text; this chapter carries practice posture only.

## Key Concepts

### Data coupling versus control coupling (section 3.2.1)

| Analysis | Role in the AC's clarification |
|---|---|
| Data coupling analysis | Distinct type and purpose from control coupling; required |
| Control coupling analysis | Distinct type and purpose from data coupling; required |
| Both together | Necessary to satisfy the named verification objective |

Treat them as peer work products with different questions. Data coupling follows how data definitions and uses cross component boundaries. Control coupling follows how transfer of control crosses those boundaries. Collapsing them into a single "coupling" checklist loses the distinction the AC insists on.

### Design practices that unlock verification (section 3.2.2)

Coupling analyses support a verification objective, but they are not a pure test-phase invention. The AC's example of good design-phase practice is explicit specification of:

- Interfaces (inputs and outputs) between components.
- Dependencies between components.

When I/O and dependencies are vague in design data, verification teams reverse-engineer coupling from code and hope the picture is complete. When design data name interfaces and dependencies, coupling analysis has a contractual baseline: confirm the designed couplings, and find undesigned ones.

### What this chapter deliberately does not do

- Does not quote ED-94C/DO-248C FAQ #67.
- Does not reproduce ED-12C/DO-178C Annex A objective lists or define objective A-7 (8) beyond naming it.
- Does not fold this topic back into ch06. Coupling clarification is its own AC 00-69 section and its own pack chapter; legacy modify flow in ch06 remains the AC 20-115D section 9 path.

## Mental Models

- Verification finds coupling; design declares the couplings worth finding. Skip the declaration and verification becomes archaeology.
- "We ran a coupling tool" is not the same as "we completed data coupling analysis and control coupling analysis." Tool output still has to answer both purposes.
- Best practices here are complementary to the means of compliance. Objective satisfaction still lives in ED-12C/DO-178C evidence, not in an AC 00-69 citation alone.

## Anti-patterns

- **Running only data coupling or only control coupling.** Section 3.2.1 says both are necessary.
- **Treating coupling as a pure late verification bolt-on.** Section 3.2.2 ties success to design-phase interface and dependency specification.
- **Interfaces described only in prose slideware.** The practice call is specification of I/O and dependencies in the design data the verification process will use.
- **Citing AC 00-69 as proof that objective A-7 (8) is met.** The AC offers best practices and points at FAQ #67 and the standard; it is not the means of compliance.
- **Merging this topic into the legacy CIA narrative and skipping a dedicated coupling story.** CIA (ch11) may discover interface change; coupling analysis still has its own objective path.

## Key Takeaways

1. AC 00-69 section 3.2 is best-practice clarification on data and control coupling; not guidance, not an AMC, complementary to ED-94C/DO-248C FAQ #67 and objective A-7 (8) of ED-12C/DO-178C.

2. Data coupling analysis and control coupling analysis differ in type and purpose; both are required.

3. Specify component interfaces (I/O) and dependencies during design so the verification objective is reachable in practice.

4. Name the industry anchors by designation only; do not paste FAQ text or objective tables into project or pack material from secondary notes.

5. This topic stands alone in the pack (ch12); do not fold it into ch06.

## Connects To

- **ch11** - CIA change classes for interfaces, architecture, and code often expose coupling scope that this chapter's analyses must cover.
- **ch06** - legacy modify and PSAC/SAS paths that will reference verification results; coupling stays its own chapter.
- **ch05** - DO-178C recognition and life-cycle data expectations that hold the verification evidence.
- **ch13** - design-level error handling, another design-phase practice that keeps verification from carrying the whole defect burden.
- **ch02** - reviews that will ask whether both coupling analyses exist and whether design data specified the interfaces they assume.
