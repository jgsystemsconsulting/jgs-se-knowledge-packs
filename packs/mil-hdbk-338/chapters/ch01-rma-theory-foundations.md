# Chapter 1: Reliability, Maintainability, and Availability Theory

## Core Idea
MIL-HDBK-338B Section 5 builds the quantitative foundation for electronic reliability work: definitions of reliability/maintainability/availability, statistical life distributions, failure modeling, and Bayesian methods for sparse data. Later design guidance rests on these measures (including MTBF/MTTR-class metrics).

## Frameworks Introduced
- **R/M/A triad**: Reliability, maintainability, and availability as linked system-effectiveness measures.
- **Life distributions**: Normal, lognormal, exponential, Weibull and related time-to-failure/repair models.
- **Failure modeling**: Hazard-rate views and series/parallel logic for system reliability.
- **Bayesian reliability**: Prior plus data updating when classical samples are thin.

## Key Concepts
- Reliability as probability of success over a defined interval and conditions.
- Maintainability metrics that govern restoration time after failure.
- Availability variants that combine reliability with maintainability and logistics delays.
- Common life distributions used for electronic and mechanical failure times.
- Hazard-rate regimes: early life, useful life, and wearout.
- Series and parallel structure effects on system roll-up.
- When Bayesian updating helps sparse reliability data.

## Mental Models
- Treat MTBF as a model output under stated assumptions, not a vendor slogan.
- Separate inherent design reliability from field reliability degraded by process and use.
- Availability couples reliability to maintainability.

## Anti-patterns
- **Point-estimate worship**: Publishing a single MTBF without distribution, duty cycle, or environment.
- **Ignoring infant mortality**: Skipping screening thinking because steady-state math looks clean.
- **Conflating Ao and Ai**: Using inherent availability where operational availability is what users feel.

## Key Takeaways
1. Section 5 is the math spine for prediction, allocation, and growth topics.
2. Choose distributions from failure physics and data shape.
3. MTBF/MTTR metrics need defined mission/environment profiles.
4. Bayesian methods help thin data; they do not replace sound failure models.
5. System structure changes how component metrics roll up.

## Connects To
- **ch02** for specification/allocation/prediction using these models.
- **ch08** for demonstration and growth against these measures.
- **ch09** for system-level R&M parameters.
