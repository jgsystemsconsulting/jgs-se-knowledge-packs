# Chapter 4: Requirements Definition and Functional Design Stages

## Core Idea
Requirements Definition turns planning outputs into complete, traceable, agreed requirements. Functional Design translates those requirements into a logical solution description — what the system must do and how functions relate — before physical/system design commits to structures and technologies.

## Frameworks Introduced
- **Requirements Definition stage**: Elicit, analyze, specify, and baseline requirements with traceability and mission-essential considerations.
- **Functional Design stage**: Develop logical/functional architecture and design work products sized to the project.
- **Requirements Traceability Matrix (RTM)**: Sample SEM exhibit pattern linking needs→requirements→design/test.

## Key Concepts
### Requirements Definition
- **Inputs**: Approved plans, high-level requirements, owner/user expectations, EA constraints.
- **Activities (conceptual)**: Detailed requirements gathering; analysis for completeness/consistency; documentation of functional and non-functional needs; interface identification; mission-essential system checklist considerations; requirements baseline under CM.
- **Traceability**: Maintain matrices so each requirement can be followed into design, construction, and test.
- **Quality**: Structured Walkthroughs on specifications; In-Stage Assessment; Stage Exit authorizing design start.
- **Size tailoring**: Exhibits list activities and work products by project size — small projects still baseline requirements, but with lighter artifacts.

### Functional Design
- **Purpose**: Define the system in functional terms — processes, data flows, user interactions, logical interfaces — without prematurely freezing physical implementation choices that belong in System Design.
- **Work products**: Functional design documentation and related models appropriate to size; updates to RTM; refined interface definitions.
- **Controls**: Same walkthrough/assessment/exit triad; ensure requirements coverage and stakeholder understanding of the proposed functional solution.
- **Handoff**: Successful exit feeds System Design with a stable functional baseline.

## Mental Models
- Requirements answer “what/why/constraints”; functional design answers “logical how”; system design answers “physical how.”
- Traceability is the anti-amnesia mechanism across stages and staff turnover.
- Mission-essential identification drives assurance and continuity expectations later in test/acceptance.
- Changing requirements after functional baseline is a CM event, not a hallway conversation.

## Anti-patterns
- **Designers inventing requirements in silence**: Breaks owner agreement and RTM integrity.
- **Skipping non-functional requirements** (security, performance, audit): SEM is systems-focused; NFRs matter.
- **Physical product selection inside functional design without analysis**: Collapses stages and locks cost early.
- **RTM built only at the end for auditors**: Traceability must guide development, not decorate acceptance.

## Key Takeaways
1. Requirements Definition baselines the agreed problem/solution boundary.
2. Traceability links requirements through design and test.
3. Mission-essential considerations influence rigor downstream.
4. Functional Design produces a logical solution description covering functions and interfaces.
5. Both stages use walkthroughs, assessments, and exits before proceeding.
6. Tailor artifact depth by size without dropping baselining discipline.

## Connects To
- **ch03**: Planning outputs that seed requirements.
- **ch05**: System Design and Construction implement the functional baseline.
- **ch06**: Test cases derive from traced requirements.
- **ch02**: Quality review expectations applied to specs and designs.
