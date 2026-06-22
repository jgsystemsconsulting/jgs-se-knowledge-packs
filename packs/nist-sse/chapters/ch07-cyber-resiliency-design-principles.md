# Chapter 7: Cyber-Resiliency Design Principles (Vol 2)

## Core Idea
Vol 2 provides cyber-resiliency **design principles** that guide *which* techniques to select and *where* to place them in the architecture. They come in two kinds: **strategic** design principles (cross-cutting, shaping the overall resiliency approach and risk posture) and **structural** design principles (concrete guidance applied to the architecture and design of the system).

## Frameworks Introduced
- **Strategic design principles** — high-level, cross-cutting principles that frame the resiliency strategy (how to think about the adversary, risk, and the overall approach).
  - When to use: when setting the resiliency posture and priorities for a system or program.
- **Structural design principles** — principles applied directly to architecture and design decisions, mapping toward specific techniques and approaches.
  - When to use: when architecting and designing the system, to place resiliency where it counts.

## Key Concepts
- **Strategic principles (cross-cutting)** — examples in spirit: focus on the mission/business functions that matter most; assume the adversary will compromise systems and maintain a presence; expect the adversary to adapt; reduce attack surfaces; plan and manage resiliency as an ongoing risk-driven activity; make the adversary's job harder and costlier. Strategic principles shape *what posture* and *which trade-offs*.
- **Structural principles (architecture/design)** — examples in spirit: limit the need for trust and constrain trust relationships; control and contain the spread of adversity (segmentation, least functionality); maintain situational awareness and the ability to detect; support graceful degradation and recovery of essential function; introduce diversity and unpredictability where they raise adversary cost; layer and coordinate defenses. Structural principles map toward the techniques (Ch 6).
- **Principles bridge framework to architecture**: goals/objectives say *why* and *what to achieve*; techniques/approaches are the *capability*; design principles are the *decision rules* that connect them to a specific architecture — they answer "given these objectives and this adversary, where and how do I apply which techniques?"
- **Risk- and adversary-driven**: principles are applied in light of the mission risk and the adversary's expected behavior (Ch 8); they are not universal mandates but guides for trade-off.

## Mental Models
- Strategic = posture, structural = placement: strategic principles decide how aggressively and where to invest in resiliency; structural principles decide exactly where in the architecture each technique goes.
- Principles are the glue between Ch 5 (framework) and Ch 6 (techniques): without them, you have aims and a toolbox but no rule for assembling them into *this* system.
- Make the adversary's life expensive: a recurring thread — every placement decision should raise the adversary's cost, uncertainty, or exposure.
- Trust is the lever: many structural principles reduce, constrain, or verify trust — echoing Vol 1's minimal-trusted-elements principle (Ch 3).

## Anti-patterns
- **Techniques without principles**: deploying resiliency techniques with no design-principle rationale for placement — resiliency in the wrong places.
- **Strategic/structural confusion**: stating posture ("be resilient to APTs") but never translating it into structural placement decisions.
- **Universal application**: treating principles as mandates to apply everywhere rather than risk-driven trade-off guides.
- **Trust sprawl**: ignoring the trust-reducing structural principles, leaving a large, unconstrained trust base for the adversary to exploit.

## Key Takeaways
1. Cyber-resiliency design principles are **strategic** (cross-cutting posture) and **structural** (architecture/design placement).
2. They are the **decision rules** connecting goals/objectives to techniques/approaches in a specific architecture.
3. **Strategic = posture and trade-offs; structural = where techniques go.**
4. They are **risk- and adversary-driven**, applied as trade-off guides, not universal mandates.
5. A recurring aim: **raise the adversary's cost, uncertainty, and exposure**; **constrain and verify trust**.

## Connects To
- **ch05 (Framework)**: principles guide selection toward objectives and goals.
- **ch06 (Techniques)**: principles say which techniques to place where.
- **ch08 (Applying & Risk)**: principles are applied against the APT and mission risk.
- **ch03 (Vol 1 design principles)**: Vol 1's trustworthy-secure-design principles (e.g. minimal trusted elements, reduced complexity) underpin the structural resiliency principles.
