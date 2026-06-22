# Chapter 5: Cyber-Resiliency Engineering Framework (Vol 2)

## Core Idea
Cyber resiliency is the ability to **anticipate, withstand, recover from, and adapt to** adverse conditions, stresses, attacks, or compromises on systems that use or are enabled by cyber resources. Vol 2 gives an engineering framework — a hierarchy of **goals → objectives → techniques → implementation approaches → design principles** — for building systems that keep delivering essential function even when a capable adversary is inside.

## Frameworks Introduced
- **The cyber-resiliency engineering framework** — a layered hierarchy from the four high-level goals down to concrete design principles, selected and tailored to the system and its adversary.
  - When to use: for any system whose mission depends on cyber resources and must survive compromise (assume breach), not merely prevent it.
- **The four goals** — Anticipate, Withstand, Recover, Adapt — taken directly from the definition of cyber resiliency.
  - When to use: as the top-level organizing aims that every objective and technique serves.

## Key Concepts
- **The 4 Goals**:
  - **Anticipate** — stay prepared and forewarned for adversity (contingency planning, threat intelligence, pre-positioned capability).
  - **Withstand** — continue essential mission/business functions *despite* adversity (absorb the hit, keep critical functionality).
  - **Recover** — restore mission/business functions during and after adversity (and deny the adversary advantage during recovery).
  - **Adapt** — change functions or supporting capabilities in response to predicted or actual changes in the threat or environment.
- **Objectives**: more specific, assessable statements that support the goals — e.g. *Prevent/Avoid, Prepare, Continue, Constrain, Reconstitute, Understand, Transform, Re-Architect*. Objectives are where resiliency becomes measurable.
- **Techniques** (14, see ch06): categories of capability that achieve objectives (e.g. Analytic Monitoring, Diversity, Redundancy, Deception).
- **Implementation Approaches**: specific methods within a technique (e.g. within Redundancy: protected backup and restore, surplus capacity, replication).
- **Design Principles** (see ch07): strategic and structural principles guiding which techniques to select and where to place them.
- **Assume-breach stance**: unlike prevention-first security, cyber resiliency assumes the advanced persistent threat (APT) is present or will get in, and engineers the system to keep operating and to deny the adversary freedom of action (Ch 8).
- **The hierarchy is a selection tool, not a checklist**: organizations *select, adapt, and use some or all* of the goals/objectives/techniques against their specific mission risk and adversary — not implement everything.

## Mental Models
- Resiliency is "keep fighting hurt": prevention tries to stop the hit; resiliency assumes the hit lands and keeps the mission going — anticipate before, withstand during, recover after, adapt for next time.
- Read the hierarchy top-down to *justify* and bottom-up to *build*: goals say why, objectives make it assessable, techniques/approaches make it real, principles say where.
- It's a portfolio choice against an adversary: you pick the techniques whose cost/benefit fits the mission risk and the APT's likely vectors — not the whole catalog.
- The biological analogy: cyber-resilient systems are like organisms that withstand and recover from injury, and when they can't recover to the prior state, they *adapt*.

## Anti-patterns
- **Prevention-only mindset**: assuming controls will keep the adversary out, with no plan for operating through compromise.
- **Implement-everything**: applying all 14 techniques regardless of mission risk or adversary — cost without focus.
- **Goals without objectives**: stating "be resilient" with no assessable objectives to design and measure against.
- **Resilience theater**: backups/redundancy that an APT can corrupt or that were never exercised under adversity.

## Key Takeaways
1. Cyber resiliency = **anticipate, withstand, recover, adapt** to adversity on cyber-enabled systems.
2. The framework is a hierarchy: **goals → objectives → techniques → approaches → design principles**.
3. **Assume breach** — engineer to keep essential function and deny the APT freedom of action, not just to prevent entry.
4. **Objectives** make resiliency assessable; **techniques/approaches** make it real; **principles** say where to place it.
5. It's a **selection/tailoring** tool against mission risk and a specific adversary — use *some or all*, not everything.

## Connects To
- **ch06 (Techniques & Approaches)**: the 14 techniques that achieve the objectives.
- **ch07 (Design Principles)**: strategic/structural principles for selecting and placing resiliency.
- **ch08 (Applying & Risk)**: the APT model and tailoring to mission risk and RMF.
- **ch01–ch04 (Vol 1)**: cyber resiliency is a specialty SSE approach operating within the SSE framework.
- **`nist-csf`**: the Recover function and resilience at the organizational level.
