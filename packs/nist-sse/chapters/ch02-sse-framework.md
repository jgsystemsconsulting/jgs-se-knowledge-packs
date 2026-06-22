# Chapter 2: The SSE Framework — Three Contexts (Vol 1)

## Core Idea
The systems security engineering framework organizes all security activity into **three interacting contexts** — the **problem** context, the **solution** context, and the **trustworthiness** context. Together they ensure the security problem is well-defined, the solution actually addresses it, and there is evidence the solution is trustworthy. The contexts iterate and share a common foundation of system security analyses; they are not a strict waterfall.

## Frameworks Introduced
- **The three-context SSE framework** — a conceptual view of the key security contexts and the activities/tasks within each.
  - When to use: to structure any SSE effort and to check coverage (have we framed the problem, built a solution, and evidenced trustworthiness?).
- **Common base of system security analyses** — the shared analytical foundation (asset, loss, consequence, adversity, and trust analyses) that feeds all three contexts.
  - When to use: continuously; the analyses are reused and refined across contexts.

## Key Concepts
- **Problem Context** — *what must be protected, from what, and why.* Establishes: stakeholder security needs and protection needs; the assets and the losses/consequences to be prevented; the adversity to be addressed; the security requirements; and the security-relevant aspects of the operational environment and constraints. A security problem that is wrong or incomplete cannot be solved by any solution.
- **Solution Context** — *how protection is achieved.* Defines and realizes the security architecture and design, the security aspects of each system element, and the security-relevant decisions and trade-offs that satisfy the problem-context requirements. This is where the design principles (Ch 3) are applied.
- **Trustworthiness Context** — *why anyone should believe it.* Produces assurance and the assurance case — the structured evidence and argument that the solution's security claims are substantiated (Ch 4). Without it, the solution is an unproven assertion.
- **Interaction, not sequence**: although the contexts look sequential (problem → solution → trustworthiness), they interact continuously — solution decisions reshape the understood problem, and trustworthiness gaps drive solution changes. The framework facilitates these interactions.
- **Applies at every level**: the three contexts apply recursively to a mechanism, component, element, system, or system of systems.

## Mental Models
- Three questions, always all three: *What's the problem? What's the solution? Why believe it?* Skipping any one produces, respectively, solving the wrong problem, hand-waving, or unfounded confidence.
- The problem context is the highest-leverage: time spent getting protection needs and adversity right pays back across the whole effort, because the solution and trustworthiness contexts both serve it.
- Trustworthiness is planned from the start, not discovered at the end: if you don't know what evidence will substantiate the claims, you can't design to produce it.
- The contexts share one analytical base: asset/loss/adversity analyses done once feed all three, so keep them coherent.

## Anti-patterns
- **Solution-first**: jumping to controls/architecture before the problem context (protection needs, adversity, requirements) is defined — solving an unstated problem.
- **Skipping trustworthiness**: delivering a solution with no assurance case, so "secure" is an assertion.
- **Treating the contexts as a one-way waterfall**: refusing to let solution/trustworthiness findings revise the problem understanding.
- **Inconsistent analyses across contexts**: different asset/adversity assumptions in problem vs. solution work.

## Key Takeaways
1. The SSE framework has **three contexts**: problem (what/why), solution (how), trustworthiness (why believe it).
2. They **interact and iterate** over a **common base of security analyses** — not a strict waterfall.
3. The **problem context** is highest-leverage — get protection needs and adversity right first.
4. The **trustworthiness context** must be planned from the start so the solution is designed to produce its evidence.
5. The framework applies **recursively** at every system level.

## Connects To
- **ch01 (Foundations)**: "adequately secure" and trustworthiness, the aims the framework serves.
- **ch03 (Design Principles)**: applied within the solution context.
- **ch04 (Trustworthiness & Assurance)**: the trustworthiness context in depth.
- **ch05 (Cyber-Resiliency Framework)**: Vol 2's framework operates within these contexts for the APT problem.
- **`nist-ai-rmf`**: a comparable Govern/Map/Measure/Manage structuring of a hard assurance problem.
