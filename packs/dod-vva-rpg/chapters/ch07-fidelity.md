# Chapter 7: Fidelity

## Core Idea
Fidelity is the degree to which the M&S reproduces features of interest of the simuland; the right fidelity is the fidelity required for the intended use—not the highest fidelity achievable.

## Frameworks Introduced
- **Fitness-for-use fidelity**: select attributes (resolution, accuracy, precision, representation breadth) against decision needs.
- **Cost–credibility trade**: higher fidelity usually costs more to build, V&V, and run; excess fidelity can harm schedule without improving decisions.
- **Multi-resolution awareness**: federations and multi-resolution models need explicit fidelity contracts at interfaces.

## Key Concepts
- **Simuland**: the real or notional entity/phenomenon being represented.
- **Referent linkage**: fidelity claims are meaningless without a referent and comparison method (ch08).
- **Attribute-specific fidelity**: a model can be high-fidelity in kinematics and low-fidelity in human factors simultaneously.
- **Communication tool**: fidelity language aligns User expectations with Developer delivery and V&V scope.
- **Documentation**: state what is represented well, poorly, or not at all.

## Mental Models
- **Enough to decide**: stop when additional fidelity does not change the decision under uncertainty.
- **Fidelity is multidimensional**: avoid single scalar “80% fidelity” slogans.
- **Interface fidelity**: in distributed M&S, the weakest justified representation can dominate error.

## Anti-patterns
- Gold-plating fidelity without intended-use mapping.
- Advertising high fidelity from marketing visuals rather than validation evidence.
- Mixing fidelity levels in a federation without reconciliation or sensitivity analysis.
- Using fidelity claims as a substitute for validation results.

## Key Takeaways
1. Fidelity serves intended use; it is not an unbounded quality score.
2. Specify fidelity by attribute and context, then validate those claims.
3. Trade cost and complexity against decision value.
4. Document non-representations as carefully as strengths.

## Connects To
- **ch02**: User expectations and acceptability.
- **ch08**: validation tests fidelity claims against referents.
- **ch05**: V&V scope sized to fidelity promises.
- **ch10**: over- or under-fidelity both create risk.
