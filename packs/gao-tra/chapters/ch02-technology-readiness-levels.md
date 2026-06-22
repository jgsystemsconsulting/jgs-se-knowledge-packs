# Chapter 2: Technology Readiness Levels

## Core Idea
Technology Readiness Levels (TRL 1–9) are a standardized nine-level scale for expressing how far a technology has been demonstrated, keyed to the **fidelity of the environment** in which it has been shown to work. The decisive maturity jumps are from laboratory to a *relevant* environment, and from a relevant environment to an *operational* one. Readiness is more than a single TRL — manufacturing (MRL) and integration (IRL) readiness matter too.

## Frameworks Introduced
- **The TRL 1–9 scale** — the common maturity ladder, originated by NASA and adopted across government, anchored to environment fidelity.
  - When to use: to rate each critical technology element's maturity in a TRA.
- **The three environments** — **laboratory**, **relevant**, **operational** — the fidelity ladder that distinguishes the levels.
  - When to use: to assign and, crucially, to *defend* a TRL; the environment is what makes a rating honest.
- **Companion scales (MRL, IRL)** — Manufacturing Readiness Levels (can it be produced affordably at rate?) and Integration Readiness Levels (do the elements work together?).
  - When to use: when a high TRL alone would overstate true readiness — producibility or integration is the binding risk.

## Key Concepts — the scale
- **TRL 1** — basic principles observed and reported.
- **TRL 2** — technology concept and/or application formulated.
- **TRL 3** — analytical and experimental proof-of-concept of critical function (laboratory).
- **TRL 4** — component/breadboard validated in a **laboratory** environment.
- **TRL 5** — component/breadboard validated in a **relevant** environment.
- **TRL 6** — system/subsystem model or prototype demonstrated in a **relevant** environment.
- **TRL 7** — system prototype demonstrated in an **operational** environment.
- **TRL 8** — actual system completed and qualified through test and demonstration.
- **TRL 9** — actual system proven through successful **mission** operations.
- **Decisive transitions**: 4→5/6 (lab → relevant environment) and 6→7 (relevant → operational environment). Most maturity disputes and over-ratings cluster here.
- **Hardware vs. software**: the levels apply to both, but the *evidence* differs — software maturity is demonstrated through integration, scale, and operational-environment execution rather than physical prototypes.
- **Environment fidelity is the crux**: a "relevant" environment reproduces the key stresses the technology will face; an "operational" environment is the real (or fully representative) one. Demonstrating in a softer environment than claimed inflates the TRL.

## Mental Models
- A TRL is shorthand for "demonstrated to work, *in this environment*, on this evidence." Strip the environment and the number is meaningless.
- Read TRLs skeptically at the 5/6 and 7 lines: that is where "we tested it" most often means a less representative environment than "relevant" or "operational" implies.
- One number rarely tells the whole story: a TRL 7 technology that cannot yet be manufactured at rate (low MRL) or integrated cleanly (low IRL) is not as ready as the TRL suggests.

## Anti-patterns
- **Environment inflation**: claiming TRL 6/7 from a laboratory or bench demonstration that does not reproduce operational stresses.
- **TRL-only readiness**: reporting a high TRL while ignoring manufacturing (MRL) or integration (IRL) immaturity.
- **Self-assessed TRLs**: developers rating their own technology upward without independent, evidence-based review.
- **Stretching definitions**: redefining "relevant" or "operational" to fit a desired rating.

## Key Takeaways
1. TRLs are a **1–9 scale keyed to environment fidelity** (laboratory → relevant → operational).
2. The **decisive jumps** are lab→relevant (TRL 4→5/6) and relevant→operational (TRL 6→7).
3. A TRL is only meaningful **with its evidence and environment** — the number alone is an opinion.
4. **MRL** (producibility) and **IRL** (integration) complement TRL — readiness is more than one number.
5. The most common error is **environment inflation** — claiming a higher-fidelity demonstration than actually occurred.

## Connects To
- **ch03 (Critical Technology Elements)**: TRLs are assigned to CTEs.
- **ch04 (Five-Step Process)**: step 3 assesses readiness against these criteria and environments.
- **ch05 (Four Characteristics)**: defensible TRLs require documented evidence and the correct environment.
- **ch07 (Using TRAs in Decisions)**: milestone thresholds (e.g., TRL 6/7) draw the line for committing.
- **`nasa-npr-7123` pack**: NASA's TRL appendix (breadboard/brassboard/engineering unit) — the scale's origin.
