# Chapter 5: Four Characteristics of a Reliable TRA

## Core Idea
A TRA is only as useful as it is reliable. GAO judges TRA quality against **four characteristics**: a reliable TRA is **comprehensive**, **well-documented**, **credible**, and **defensible**. These are the quality standard a TRA must meet to be trusted in a decision — and the lens an auditor uses to find where a TRA falls short.

## Frameworks Introduced
- **The four characteristics** — comprehensive, well-documented, credible, defensible — each backed by specific best practices and evidence.
  - When to use: to plan a TRA that will hold up, and to evaluate an existing TRA's trustworthiness.
- **Characteristic-as-failure-mode** — each characteristic names a way TRAs go wrong (incomplete, undocumented, biased, indefensible), so the framework doubles as a checklist of risks.
  - When to use: when critiquing a TRA or deciding how much weight to give its conclusions.

## Key Concepts — the four characteristics
- **Comprehensive**: all CTEs are identified and each is assessed against complete, defined criteria in the correct environment. *Failure mode*: a missing CTE or a partial assessment that leaves real maturity gaps unmeasured.
- **Well-documented**: the evidence, methods, assumptions, environments, and TRL rationale are captured so the assessment can be traced, understood, and repeated by someone else. *Failure mode*: a bare TRL number with no traceable basis — an assertion, not an assessment.
- **Credible**: the assessment is performed by **qualified, independent** assessors using sufficient, objective evidence; dissent is captured. *Failure mode*: self-assessment by developers, or thin/cherry-picked evidence.
- **Defensible**: the conclusions follow logically from the evidence and **withstand independent scrutiny** and oversight. *Failure mode*: ratings that cannot survive a challenge because the evidence does not actually support them.

## Mental Models
- The four characteristics are a chain: a TRA that is not comprehensive cannot be defensible (it missed something); one that is not well-documented cannot be credible (no one can check it). Weakness in one undermines the others.
- "Would this survive a hostile, independent review?" is the defensibility test — and the single best question to ask of any TRA before relying on it.
- Documentation is what makes the other three checkable: comprehensiveness, credibility, and defensibility are all claims that can only be verified if the work is written down and traceable.

## Anti-patterns
- **Bare-number TRAs**: TRLs reported with no documented evidence, environment, or rationale.
- **Insider assessments**: ratings produced by those with a stake in the answer, defeating credibility.
- **Optimistic, undefensible ratings**: conclusions that read well but cannot withstand independent challenge.
- **Partial coverage**: assessing the easy CTEs thoroughly and the hard ones lightly, breaking comprehensiveness.

## Key Takeaways
1. A reliable TRA is **comprehensive, well-documented, credible, and defensible**.
2. **Comprehensive** = all CTEs assessed against complete criteria in the right environment.
3. **Well-documented** = traceable, repeatable evidence, methods, assumptions, and rationale.
4. **Credible** = qualified, **independent** assessors and sufficient, objective evidence.
5. **Defensible** = conclusions follow from evidence and survive independent scrutiny.
6. The characteristics form a **chain** — weakness in one undermines the rest; documentation makes all of them checkable.

## Connects To
- **ch04 (Five-Step Process)**: the process is how a TRA earns these four characteristics.
- **ch03 (CTEs)**: comprehensiveness depends on a complete CTE list.
- **ch02 (TRLs)**: defensible ratings require the correct environment and evidence.
- **ch07 (Using TRAs in Decisions)**: only a reliable TRA should carry weight in a milestone decision.
- **`requirements-writing` pack**: the same "verifiable, traceable, defensible" discipline applied to requirements.
