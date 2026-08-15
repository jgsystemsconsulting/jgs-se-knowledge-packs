# Chapter 1: Scope, Criticality, and M&S Programmatics

## Core Idea
NASA-STD-7009B governs models and simulations (M&S) that inform critical decisions. Before building or running an M&S, programs record intended use, assess criticality of the decision situation, plan the M&S life cycle, define metrics and acceptance criteria, and keep review and defect history. The handbook adds how technical authority and project management share that responsibility.

## Frameworks Introduced
- **Intended use record**: What real-world system (RWS) aspects are modeled, expected products, validation domain intent, and which decisions the results will support.
- **Criticality assessment**: Influence of the M&S on a decision versus consequence of a wrong decision (Appendix D style matrix is representative, not mandatory form).
- **M&S life-cycle plan**: Acquisition, development, operation, maintenance, retirement, and responsible organizations.
- **Acceptance criteria set**: Verification, validation, uncertainty, sensitivity, and assessment-level thresholds for capability and results.
- **Defect/problem log**: Discovery-to-closure tracking across the M&S life cycle.

## Key Concepts
- **In-scope M&S**: Those supporting critical decisions per the criticality record; other M&S may be pulled in by program/Technical Authority judgment.
- **Programmatic vs technical metrics**: Schedule/cost/CM/delivery metrics alongside V&V, uncertainty, and sensitivity data that feed acceptance.
- **Unique reporting info**: Data that must travel with results later (beyond generic run logs).
- **Technical reviews**: Results of life-cycle reviews are retained and later reported to decision makers.
- **Tailoring**: Standard allows program-level tailoring; criticality and intended use still drive which requirements bite.
- **Handbook depth**: Interpreting/tailoring, compliance posture, and program/project vs delegated Technical Authority roles for M&S governance.

## Mental Models
- Criticality is about the *decision situation*, not how fancy the model is.
- Programmatics create the paper trail that makes later credibility claims auditable.
- "Record shall be maintained" is the STD's dominant pattern: evidence over slogans.
- Plan first, then develop, then use — the three major STD blocks.

## Anti-patterns
- **Building first, inventing intended use later**: Breaks permissible-use and use-assessment chain.
- **Skipping criticality because "it's only a study model"**: If it influences a critical decision, it is in scope.
- **Acceptance criteria written after V&V**: Thresholds must pre-exist assessments.
- **Orphan defect notes**: Problems without closure status undermine results risk claims.

## Key Takeaways
1. Record intended use and criticality before treating an M&S as decision-support.
2. Keep an M&S life-cycle plan with clear ownership.
3. Define V&V/uncertainty/sensitivity acceptance criteria and assessment thresholds up front.
4. Retain technical-review outcomes and defect histories.
5. Handbook guidance clarifies who (PM vs Technical Authority) drives governance.
6. Scope can expand beyond critical-decision M&S by authority discretion.

## Connects To
- **ch02**: Development evidence, pedigree, permissible uses, capability assessment.
- **ch03–ch04**: Verification, validation, uncertainty during development.
- **ch05–ch06**: Use-phase assessment, results, risk, reporting.
- **ch07**: Handbook life-cycle phases that implement the plan.
- **nasa-risk / nasa-pra**: Broader risk and quantitative uncertainty practice.
