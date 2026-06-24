# Chapter — Provide Rationale and Summary of Recommended Practices

## Core Idea

A requirement says *what* a system shall do; a design says *how*; rationale says *why*. The Handbook's eleventh and final main-level practice — Provide Rationale (section 2.11) — closes the gap that the first ten leave open: even a perfectly worded, testable, atomic requirement can be misread, mis-implemented, or needlessly preserved if the reader cannot reconstruct the reasoning that produced it. Rationale is the durable record of that reasoning, attached to individual requirements, environmental assumptions, and specific numeric values or ranges.

The chapter pairs this last practice with the Handbook's overall Summary (section 3), which frames why the whole collection of eleven practices exists. The closing argument is economic, not stylistic: deciding precisely what to build is the hardest and least-recoverable part of system development, so investment in good requirements up front pays back across the entire life cycle. Rationale is singled out as the highest-leverage move inside that investment — the practice cited as the most cost-effective single thing a requirements author can do.

For the embedded, real-time, avionics-leaning systems this Handbook targets, rationale matters acutely because the consequences of a misunderstood timing bound, latency budget, or safety threshold are physical and sometimes irreversible. The recurring Isolette Thermostat example makes this concrete: the *why* behind a temperature limit can be the difference between a safe device and a fatal one.

## Frameworks Introduced (exact source names, when/how)

- **Provide Rationale (Recommended Practice 2.11)** — the main-level practice introduced in this slice, with seven sublevel practices (2.11.1 through 2.11.7) catalogued in *Table 24. Provide Rationale*. It instructs developers to attach commentary that explains the reason a given requirement or environmental assumption is present, or the reason a specific number or interval was selected.

- **The seven sublevel recommended practices (2.11.1–2.11.7)** — introduced as the operational breakdown of the main practice:
  - 2.11.1: provide rationale across all phases of requirements development, explaining why a requirement exists or why specific values are set.
  - 2.11.2: never use rationale as an alternate source of requirements; anything essential to behavior must be promoted to a real requirement.
  - 2.11.3: provide rationale for every requirement whose reason for existing is not obvious.
  - 2.11.4: provide rationale for every environmental assumption whose inclusion is not obvious.
  - 2.11.5: provide rationale for every value or range, explaining why that particular value was chosen.
  - 2.11.6: keep rationale short and relevant; summarize long supporting documents and cite them rather than copying them.
  - 2.11.7: capture rationale by the original author, as soon as possible.

- **Hooks and Farry (reference [22])** — cited as the source of two claims: that providing rationale is the single most effective way to lower cost and raise quality of requirements, and that authors should capture rationale for *every* requirement, not only the non-obvious ones.

- **The Isolette Thermostat example** — the Handbook's running illustration, reused here to ground three of the sublevel practices with concrete artifacts: requirement REQ-MHS-4 (hold the Heat Control unchanged inside the desired temperature band), environmental assumption EA-IS-1 (heating rate bounded at no more than 1°F per minute), and EA-OI-3 (the 93°F lower alarm temperature tied to hypothermia risk).

- **Fred Brooks (reference [46])** — quoted in the Summary to anchor the Handbook's central premise: that deciding what to build is the hardest part of system development and the part most damaging to get wrong and hardest to fix later.

- **The industry survey (reference [1])** — cited in the Summary as the motivating evidence: known good requirements-engineering methods are rarely used in practice, and developers still struggle with how to collect, document, and organize requirements.

- **The 11 main-level recommended practices** — named in the Summary as the Handbook's complete framework, ordered so a developer can move from informal early approaches toward more rigorous methods as requirements mature.

## Key Concepts

- **Three documents, three questions.** Requirements answer *what*, design answers *how*, rationale answers *why*. Keeping these distinct prevents the most common failure of mixing reasoning into normative text or, worse, hiding requirements inside reasoning.

- **Rationale is non-binding.** Because rationale is not contractually enforced and is never verified, it is not a safe place to park anything the system must actually do. The 2.11.2 boundary is strict: if a statement in the rationale is essential to behavior, it must be lifted out and written as a requirement.

- **Rationale forms allowed.** Rationale can be free text, or a pointer to a trade study, another document, a paper, or a book citation. The Handbook notes that the system goals (its section 2.1.3) are frequently a good source.

- **Three explicit targets for rationale.** The practice deliberately separates three things that each warrant a *why*: the existence of a requirement (2.11.3), the inclusion of an environmental assumption (2.11.4), and the choice of any specific value or range (2.11.5). Numbers are called out on their own because a bare value like "93°F" or "1°F per minute" carries no visible justification, yet may be safety-critical and unchangeable.

- **The latency-assumption coupling.** The Isolette example shows rationale documenting a dependency that is otherwise invisible: the allowed latency on the Heat Control is computed from EA-IS-1's maximum heating rate. Without the rationale, a later engineer relaxing the assumption would not see that they had silently broken the latency budget. This is the embedded/real-time slant in action — timing and physical-rate assumptions are tightly coupled and easy to disturb.

- **The cost case for rationale.** The chapter lists the specific cost savings rationale produces: faster comprehension of requirements that are read many times, fewer incorrect assumptions (whose cost grows as development proceeds toward implementation), cheaper maintenance, cheaper creation of product variations, and cheaper onboarding of new staff.

- **Rationale improves the requirement itself.** Forcing an author to articulate why a requirement is necessary often exposes that it is unnecessary or is actually an implementation detail in disguise — letting it be deleted, which removes an unwarranted constraint on developers and the cost of verifying something that never needed to exist.

- **Capture at the moment of authoring.** Rationale recorded while the author is still reasoning is accurate and reviewable; rationale reconstructed later is, in effect, reverse-engineered guesswork. The latency-versus-heating-rate calculation is the example: far simpler to note while computing the latency than to recover afterward.

- **The Summary's framing of the whole Handbook.** The eleven practices are presented roughly in execution order but are explicitly not required to be followed strictly in sequence; iteration among activities is expected as requirements are refined. The practices target real-time, embedded systems, specifically avionics, and lean on software emphasis because software is a growing share of these systems and the practices ease the system-to-software requirements transition.

- **Tailoring is expected.** The Handbook explains each main practice by picking one approach and one running example, but states that the examples and sublevel practices exist to illustrate the main-level practices, not to mandate a style or format. Organizations are expected to modify the practices, possibly heavily, for their own environment; some cited approaches were already tailored in the Handbook to fit alongside the others.

## Mental Models

- **Rationale as the "why" layer in a three-layer stack.** Stack what / how / why as parallel but separate records. A requirement and its design can be perfect while the *why* layer is empty — and that empty layer is exactly what gets expensive years later when someone asks "can we change this number?"

- **The 93°F test.** Treat every literal value as a question waiting to be asked: *what happens if someone changes this to save money or use a more common part?* For EA-OI-3, the rationale answers it — below 93°F, hypothermia risk, fatal for severely ill preterm infants — so the number is visibly non-negotiable. A value without rationale invites exactly the cost-driven substitution that the rationale would have blocked.

- **Rationale as a delete button.** Writing the *why* is a filter. If you cannot produce a credible reason a requirement exists, that is strong evidence it should not exist. Articulating rationale is therefore not only documentation but a quality gate that prunes unnecessary constraints before they reach developers and verifiers.

- **Author-now vs. reverse-engineer-later.** Reasoning is cheapest to record at the instant it is being done. Once the author has moved on, the same rationale must be reconstructed from incomplete memory — slower, less reliable, and unreviewable. Capture is a perishable opportunity.

- **The non-obvious filter.** The minimum bar is: rationale for anything whose reason is not obvious to a reader. Hooks and Farry push the bar higher — rationale for everything — but the Handbook's floor is the non-obvious case, which keeps the practice tractable while still catching the dangerous gaps.

- **Brooks's hardest-part lens for the whole Handbook.** Read the eleven practices as a structured assault on the single hardest, least-recoverable part of building a system: deciding precisely what to build. Every practice, rationale included, is justified by how much it reduces the cost of getting that decision wrong.

## Anti-patterns

- **Rationale as a back-door requirement.** Using rationale to state what the system must do — a behavior the source explicitly forbids in 2.11.2. Because rationale is not binding and is not verified, anything essential hidden there will never be implemented or checked. The fix is to promote it to a real requirement.

- **Rationale as cover for a poor requirement.** The source warns that rationale must not be used as an excuse for writing bad requirements. A weak or vague requirement is not rescued by a paragraph of justification beneath it.

- **Copying instead of summarizing.** Pasting an entire trade study into the rationale rather than summarizing its relationship to the requirement and citing it (2.11.6). Long, copied rationale buries the relevant point and defeats the purpose of keeping rationale short.

## Key Takeaways

- Rationale documents *why* a requirement or assumption exists, or why a value was chosen; it complements — and must stay separate from — the *what* of requirements and the *how* of design.
- Of all the Handbook's practices, providing rationale is cited (via Hooks and Farry) as the single most cost-effective move for improving requirements quality and reducing cost.
- Rationale must never carry binding behavior; anything essential to the system belongs in a requirement, not in the rationale.
- Provide rationale for three distinct targets: non-obvious requirements, non-obvious environmental assumptions, and every specific value or range.
- Specific numbers deserve special attention — the 93°F lower-alarm limit shows how rationale prevents a dangerous, cost-motivated change to a safety-critical value.
- In real-time embedded systems, rationale exposes hidden couplings, such as the Isolette's Heat Control latency being derived from the bounded heating rate in EA-IS-1.
- Keep rationale short and relevant; summarize and cite long supporting documents rather than copying them.
- Capture rationale by the original author, as soon as possible — reasoning recorded in the moment is accurate and reviewable; reasoning reconstructed later is guesswork.
- Articulating rationale is itself a quality filter: a requirement with no defensible *why* is often unnecessary or an implementation detail that should be deleted.
- The Handbook's overall message: a good requirement set is far more than a list of shall statements, it is hard to produce, and the up-front investment ultimately lowers cost while raising product quality.
- The 11 main-level practices progress from informal to rigorous, are not strictly sequential (iteration is expected), and are meant to be tailored, not adopted verbatim.

## Connects To

- **Capture System Goals (the Handbook's section 2.1.3)** — named here as a frequent source of rationale, since the *why* behind a requirement often traces directly back to a stated system goal.
- **Document Environmental Assumptions** — practice 2.11.4 attaches rationale specifically to environmental assumptions, and the EA-IS-1 / EA-OI-3 examples show how assumption rationale guards values and timing budgets.
- **Specify Timing and Latency Requirements** — the embedded/real-time core of the Handbook; the Isolette latency-versus-heating-rate coupling shows rationale protecting a timing budget derived from a physical assumption.
- **Write Good Requirements (clarity, testability, atomicity)** — rationale complements requirements-writing by holding the reasoning that the normative text deliberately excludes, keeping requirements focused on *what* the system does.
- **The full set of 11 main-level recommended practices** — this chapter both completes the practice list (Provide Rationale is the eleventh) and, through the Summary, frames how all eleven fit together and how an organization should select, order, and tailor them.
- **Requirements management and life-cycle cost** — the Brooks quotation and the cited cost evidence (references [22–24] and [47]) connect rationale to the broader argument that early requirements investment reduces downstream cost across maintenance, variation, and onboarding.
