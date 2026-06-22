# Chapter 5: Technical Processes (8)

## Core Idea
The eight **technical** processes transform an operational need into a delivered, validated capability. They follow the V-diagram: top-down **design** processes on the left arm (stakeholder requirements → requirements analysis → architecture design → implementation) and bottom-up **realization** processes on the right arm (integration → verification → validation → transition).

## Frameworks Introduced
- **The eight technical processes** — Stakeholder Requirements Definition, Requirements Analysis, Architecture Design, Implementation, Integration, Verification, Validation, Transition. Mapped to ISO/IEC/IEEE 15288.
  - When to use: to create and realize the technical solution, iterating across the V as the design matures.
- **The V-diagram flow** — design flows down (need → requirements → architecture → realized design); realization flows up (assemble → verify → validate → deliver).
  - When to use: to locate where each process operates and to keep verification/validation tied back to the requirements/needs they trace to.

## Key Concepts — the eight processes
- **Stakeholder Requirements Definition**: translate operational requirements from relevant stakeholders into a set of **top-level technical requirements**.
- **Requirements Analysis**: decompose the top-level requirements into a **complete set of system functional and performance requirements** (the "shall" statements), allocated and traceable.
- **Architecture Design**: capture the functional requirements and their interdependencies in the **system architecture** — typically via system modeling, trade-offs, and decision analyses; allocate functions to system elements.
- **Implementation**: mature and realize the design of the system and system elements (make/buy/reuse), generating the **product baseline**.
- **Integration**: assemble the system elements into the system, ready for test.
- **Verification**: **developmental test** — demonstrate the system conforms to its functional/performance requirements ("did we build the system *right*?").
- **Validation**: **operational test** — demonstrate the system meets the **operational need** in its intended environment ("did we build the *right* system?").
- **Transition**: formally deliver the system capability — including enabling system elements — to the end users for operation and sustainment.

## Mental Models
- The V is two questions meeting in the middle: the left arm builds *to the requirements*; the right arm proves *against the requirements (verification)* and *against the need (validation)*. Each right-arm test traces to a left-arm artifact.
- Verification vs. validation, the durable distinction: **verification** = conformance to specification (developmental); **validation** = fitness for operational use (operational). A system can pass verification and still fail validation if the requirements were wrong.
- Architecture Design is where trade-offs live: requirements say *what*; architecture decides *how functions are allocated to elements*, and that allocation is where cost/performance/risk are balanced.
- The technical processes are iterative and overlapping, not a single waterfall pass — the design matures through repeated traversal as knowledge grows.

## Anti-patterns
- **Collapsing verification into validation (or vice versa)**: declaring operational suitability from a developmental test, or accepting a spec-conformant system that does not meet the operational need.
- **Architecture by implementation**: jumping to a design solution without an architecture that allocates functions and exposes trade-offs.
- **Untraceable requirements**: realization and test that cannot be traced back to analyzed requirements and stakeholder needs.
- **"Throw it over the wall" transition**: delivering the end product without the enabling system elements (training, support, spares) needed to operate and sustain it.

## Key Takeaways
1. Eight technical processes run the V: **Stakeholder Requirements Definition → Requirements Analysis → Architecture Design → Implementation** (down) and **Integration → Verification → Validation → Transition** (up).
2. **Requirements Analysis** produces the complete, traceable set of functional/performance "shall" requirements.
3. **Architecture Design** allocates functions to elements and is where trade-offs are made — often model-based.
4. **Verification** = developmental test (built it right); **Validation** = operational test (built the right thing).
5. **Transition** delivers the capability *plus* enabling system elements for operation and sustainment.
6. The processes are iterative/overlapping and stay tied to requirements and needs via traceability.

## Connects To
- **ch04 (Technical Management Processes)**: Requirements Management traces these requirements; Configuration Management baselines them; Technical Assessment measures progress.
- **ch03 (Technical Reviews & Audits)**: SFR/PDR/CDR gate the design processes; SVR/FCA verifies; operational test validates.
- **ch06 (Design Considerations)**: the 24 design considerations are balanced *within* Architecture Design and Implementation.
- **`requirements-writing` pack**: EARS patterns and quality characteristics for the "shall" statements produced by Requirements Analysis.
- **`nasa-npr-7123` / `nasa-se-handbook` packs**: NASA's equivalent system-design/product-realization processes.
