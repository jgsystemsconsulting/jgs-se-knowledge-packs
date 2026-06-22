# Chapter 4: Technical Management Processes (8)

## Core Idea
The eight **technical management** processes run continuously across the acquisition life cycle, giving the PM, Systems Engineer, and Lead Software Engineer the insight and control to keep the technical effort on track for performance, schedule, and cost. They wrap around and govern the eight technical processes (ch05).

## Frameworks Introduced
- **The eight technical management processes** — Technical Planning, Decision Analysis, Technical Assessment, Requirements Management, Risk Management, Configuration Management, Technical Data Management, Interface Management. Mapped to ISO/IEC/IEEE 15288.
  - When to use: across every phase; they are not gated to a single life-cycle stage.
- **Risk, Issue, and Opportunity (RIO) management** — one process managing three distinct objects with three reporting matrices.
  - When to use: continuously; the central technical-management discipline for uncertainty.
- **TPM hierarchy and leading indicators** — quantitative measures tracked against planned profiles, with forward-looking indicators that trigger mitigation before thresholds are breached.
  - When to use: throughout development to assess whether the design will meet requirements.

## Key Concepts — the eight processes
- **Technical Planning**: plan, organize, schedule, and resource the technical effort; outputs feed the SEP and integrate with the IMP, IMS, and WBS. Defines how the other 15 processes are applied and scaled.
- **Decision Analysis**: apply documented criteria, alternatives, and analysis (e.g., trade studies, AoA support) to significant technical decisions — not verbal consensus.
- **Technical Assessment**: measure technical progress against plans; conduct technical reviews; track **TPMs** and **leading indicators**; report status to inform decisions.
- **Requirements Management**: maintain **bidirectional traceability** (requirement ↔ parent ↔ allocated children) and control requirement changes across the life cycle.
- **Risk Management (RIO)**:
  - **Risk** = a *future* event with negative consequence — scored on a **likelihood × consequence** 5×5 matrix; handled by accept / avoid / transfer / control (mitigate).
  - **Issue** = a realized risk or current problem — scored on a consequence-based issue matrix; handled by corrective-action burn-down.
  - **Opportunity** = a potential *future benefit* — scored on an opportunity matrix; handled by pursue / reject with cost-benefit.
- **Configuration Management**: establish and control configuration items and the functional/allocated/product baselines; manage change so integrity and traceability are preserved.
- **Technical Data Management**: capture, control, and provide access to technical data — trade studies, analyses, models, reports — under a data taxonomy and data-rights strategy.
- **Interface Management**: identify, define, and control internal and external interfaces (ICDs/IRSs); essential where multiple teams, contractors, or constituent systems integrate.

## Mental Models
- Technical management is the "control loop" of SE: technical processes *produce* the design; technical management *measures, decides, and controls* its maturation.
- RIO triage in one question: *has it happened yet?* Not yet, bad → **risk**; already happened (or is happening) → **issue**; not yet, good → **opportunity**. Each goes on its own matrix with its own playbook.
- Leading indicators earn their keep by being *forward-looking*: a TPM that only reports today's value is a lagging gauge; an indicator that shows the *trend toward* a threshold buys time to act.
- If a requirement cannot be traced both up to its parent and down to its allocation, Requirements Management has failed — and Configuration Management will not be able to control its change.

## Anti-patterns
- **Confusing risks and issues**: putting a realized problem on the risk matrix (and "mitigating" something that has already happened) — issues need corrective-action burn-down, not likelihood reduction.
- **Decision Analysis by assertion**: choosing a design without documented criteria, alternatives, and analysis.
- **TPMs without thresholds or trends**: tracking numbers with no planned profile or leading indicator, so problems are seen only after a breach.
- **Uncontrolled interfaces**: integrating across teams/contractors without baselined interface definitions — a leading cause of late integration failure.

## Key Takeaways
1. Eight technical management processes provide continuous **insight and control**: Technical Planning, Decision Analysis, Technical Assessment, Requirements Management, Risk Management, Configuration Management, Technical Data Management, Interface Management.
2. **RIO**: risk (future bad), issue (realized), opportunity (future good) — three objects, three matrices, three playbooks.
3. **TPMs** track design adequacy against a planned profile; **leading indicators** signal trouble *before* a threshold is breached.
4. **Requirements Management** maintains bidirectional traceability and change control.
5. **Configuration Management** owns the functional/allocated/product baselines and their change.
6. **Interface Management** is decisive for SoS and multi-contractor integration.

## Connects To
- **ch05 (Technical Processes)**: technical management governs and measures the technical processes that create the design.
- **ch03 (Technical Reviews & Audits)**: Technical Assessment conducts reviews; Configuration Management establishes/verifies baselines at them.
- **ch01 / SEP**: Technical Planning generates the SEP and integrates with IMP/IMS/WBS.
- **`nasa-risk` pack**: NASA's RIDM + CRM risk model — a deeper, complementary risk treatment.
- **DoD RIO Management Guide for Defense Acquisition Programs**: the detailed source for the RIO matrices.
