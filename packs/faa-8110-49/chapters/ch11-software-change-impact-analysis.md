# Chapter 11 - Software Change Impact Analysis

Sources: S4 AC 00-69, Best Practices for Airborne Software Development Assurance Using EUROCAE ED-12( ) and RTCA DO-178( ) (2017-07-21), section 3.1, lines 24-68 of `sources/text/S4.txt`. Best practices, not guidance, and not an acceptable means of compliance. Complements ED-12C/DO-178C (and ED-12B/DO-178B) sections 12.1.1-12.1.3 and AC 20-115D section 9.b(4); those documents are named by designation only.

## Core Idea

AC 00-69 section 3.1 is complementary best-practice material for software change impact analysis (CIA). It is not guidance and not an acceptable means of compliance. Use it when a project already needs a CIA under the recognized standards and under AC 20-115D. The AC deepens the recognition-side CIA duty in AC 20-115D section 9.b(4) (legacy modify path; pack flow in ch06): identify the change, analyze extent and impact, verify as the CIA indicates, and summarize results in the PSAC or SAS. The industry change-control spine sits in ED-12C/DO-178C sections 12.1.1-12.1.3 (named only; not quoted or reconstructed here).

## Frameworks Introduced

- **CIA as a baseline-anchored package.** The analysis starts from the released software baseline the proposed software will build on, then packages three deliverables: change summary and impact, problem reports and change requests in scope, and new functions to activate or implement.

- **Change-class checklist (original summary).** Eight classes the CIA addresses where applicable: software level; development or verification environment; software processes; tools; processor and other hardware components and interfaces; configuration data; software interface characteristics and input/output requirements; software requirements, design, architecture, and code (including life-cycle data affected by the change, not only the modified items).

- **Per-class impact and activity close-out.** For each applicable class, the CIA describes resulting impact and names the activities needed so the project continues to satisfy ED-12C/DO-178C (or ED-12B/DO-178B) and safe-operation requirements.

- **Recognition-side trigger.** AC 20-115D section 9.b(4) requires CIA when legacy software is modified; this chapter is the best-practice depth for that trigger, not a second means of compliance.

## Key Concepts

### What the CIA identifies (section 3.1.2)

| CIA element | What it captures |
|---|---|
| Released baseline | The approved software baseline the proposed change builds on |
| Change summary and impact | Concise description of what changes and what those changes affect |
| Problem reports / change requests | Listing and descriptions of OPRs corrected by the change and/or related change requests |
| New functions | Listing of functions to be activated and/or newly implemented |

Without a named baseline, impact statements float. Without the PR/CR and new-function lists, reviewers cannot see the full intended delta.

### Change classes the CIA addresses (section 3.1.3)

Present these as an original summary table, not as a paste of the AC checklist:

| Class | Typical CIA attention |
|---|---|
| Software level | Assigned level change, or level consequences of the modification |
| Development or verification environment | Host, target, simulators, test benches, build chain |
| Software processes | Planning, development, verification, CM, QA process shifts |
| Tools | New tool version, or modified use of an existing tool |
| Processor / hardware components and interfaces | CPU, peripherals, buses, and hardware interface changes |
| Configuration data | Activation or deactivation of functions via configuration |
| Interface characteristics and I/O requirements | Software interface behavior and input/output requirements |
| Requirements, design, architecture, and code | Modified life-cycle data **and** data affected by the change |

The last row is the common miss: teams inventory only the files they edited and skip dependents the edit ripples into.

### Per-item impact and follow-on activities (section 3.1.4)

For every applicable row above, the CIA:

1. Describes the resulting impact.
2. Identifies activities to perform so the project still satisfies ED-12C/DO-178C or ED-12B/DO-178B and continues to meet safe-operation requirements.

Impact without planned activity is incomplete. Activity without impact rationale is ungrounded.

### Relationship to AC 20-115D and the standards

- **AC 20-115D section 9.b(4)** is the applicant-facing recognition requirement this chapter deepens for the legacy modify path (see ch06 for the full Figure 1 flow).
- **ED-12C/DO-178C sections 12.1.1-12.1.3** (and the ED-12B/DO-178B counterparts) are the industry change-control references named by the AC. This pack does not quote those sections or rebuild any deleted order-chapter checklists.

## Mental Models

- CIA answers three questions in order: what baseline am I leaving, what delta am I introducing (PRs, CRs, new functions), and which change classes actually move.
- Configuration-data activation is a real change class even when source code is untouched.
- "Affected by" is wider than "modified." Architecture and interface dependents belong in the inventory.
- Best practices sit beside the means of compliance; they do not replace AC 20-115D or ED-12C/DO-178C.

## Anti-patterns

- **CIA with no named released baseline.** Section 3.1.2 anchors the whole analysis on that baseline.
- **Listing edited units only.** Section 3.1.3.8 expects affected requirements, design, architecture, and code, not just touched files.
- **Ignoring tool or environment churn.** New tool versions and modified tool use are first-class change classes (3.1.3.4); so are development and verification environment shifts (3.1.3.2).
- **Treating configuration activation as "no software change."** Section 3.1.3.6 calls out configuration data, especially function activation and deactivation.
- **Impact narrative with no follow-on activities.** Section 3.1.4 pairs every applicable class with activities that keep the ED-12/DO-178 satisfaction story intact.
- **Using AC 00-69 as the means of compliance.** The AC states it is best practices and complementary information, not guidance and not an AMC.

## Key Takeaways

1. AC 00-69 section 3.1 gives best-practice depth for software CIA; it complements ED-12C/DO-178C sections 12.1.1-12.1.3 and AC 20-115D section 9.b(4), and is not itself guidance or a means of compliance.

2. A complete CIA names the released baseline, summarizes changes and impact, lists in-scope problem reports and change requests, and lists new functions to activate or implement.

3. Where applicable, address all eight change classes: level, environment, processes, tools, processor/hardware interfaces, configuration data, I/O and interfaces, and requirements/design/architecture/code including affected data.

4. For each applicable class, record impact and the activities required to keep standards satisfaction and safe operation.

5. On the legacy path, ch06 carries the AC 20-115D section 9.b(4) flow; this chapter is the CIA content depth behind that step.

## Connects To

- **ch06** - AC 20-115D section 9 legacy flow; section 9.b(4) is the recognition-side CIA trigger this chapter deepens.
- **ch05** - DO-178C recognition, life-cycle data, and tool transition rules that CIA follow-on activities often re-enter.
- **ch02** - certification liaison and software reviews that consume PSAC/SAS CIA summaries.
- **ch12** - data and control coupling practices that often surface when interface and dependency changes are in the CIA scope.
- **ch13** - design-level error handling practices to re-check when architecture or code changes touch runtime behavior.
