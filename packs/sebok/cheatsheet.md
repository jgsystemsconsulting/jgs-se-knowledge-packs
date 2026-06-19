# SEBoK Cheatsheet

Decisions a systems engineer makes, and SEBoK's reasoning. Not definitions — judgment.

## Starting a Problem
- Ill-defined + high uncertainty → ask "What's going on here?" not "What are the requirements?" Systems thinking, root-cause, empathy first; defer formal spec.
- Contested goals, power/ethics/politics in play → **soft systems** (SSM) or critical systems; **not** hard optimization. Hard methods need agreed, well-defined ends.
- Can't fully define or solve the problem (definition shifts as you attack it) → **wicked problem**; iterate to learn, never spec-then-build.
- Don't fix the SoI boundary until the problem is understood. Early boundary lock = wrong solution space.
- Treat the original problem statement as suspect — usually not the right one.

## Life Cycle Model Selection
| Pattern | Use when |
|---|---|
| Sequential/Vee | Requirements stable, low novelty, certification/formal reviews, hardware fab cadence |
| Incremental | Capability can ship in slices; want early feedback before full system |
| Evolutionary | Problem understanding itself is immature; each cycle delivers value **and** learns |
| Agile | Volatile requirements, software-intensive, fast feedback, modular architecture exists |
- Selection is **risk-driven**: pick the approach that retires the most project risk. Compare candidates on risk, not preference.
- Mixed HW/SW system → separate domain-specific models, synchronized at checkpoints. Sync interval: too short = pure overhead; too long = incompatible interfaces. Match to the slower domain.
- Adapt per system element, not once for the whole system; document adaptation; get acquirer–supplier agreement.

## Agile — when NOT to
- Safety-critical, multi-disciplinary, long integration, hardware cycles → agile doesn't transfer cleanly; lengthen + safety-gate iterations.
- Monolithic/tightly-coupled architecture → can't deliver agile; fix coupling first.
- Ceremonies (standups/sprints) without faster sensing/deciding = agility theater.
- "Frequent releases" ≠ evolutionary without real user feedback loops.

## System Classification (drives governance)
| Type | Value via | Governance |
|---|---|---|
| Product | manufacture/exchange | TSE (project lifecycle) |
| Service | availability/performance | SLA + co-creation; QoS = technical TPM **and** subjective QoE |
| Enterprise | strategic alignment | intentional operational **dependence**; PDCA, portfolio |
| SoS | federated capability | governance not control; trust/contract interfaces |
- SoS test = operational **AND** managerial independence (Maier). Complexity/distribution alone ≠ SoS — if no independence, govern as enterprise.
- SoS → expect distributed decisions; hierarchical control generates friction. Align constituent incentives or get passive resistance.

## Reviews, Baselines, Tailoring
- Review timing: **schedule-based** (early, thin info) / **event-based** (artifact-triggered, fuller) / **evidence-based** (risk-threshold-triggered, highest commitment, latest feedback).
- Reviewer mix: close enough for insight, far enough for independence. Too close = biased; too far = misses issues.
- Baseline **just-in-time**, when dependent work commits. Early baselining → high change/rework.
- Process rigor ∝ size × criticality × novelty × certification need. Uniform process across all projects fails. Tailoring is mandatory, evidence-based, documented.
- Don't reuse another project's tailored baseline blind; don't let tool capability dictate process.

## Decisions, Risk, Cost
- Trade study: define value criteria **first**, then design alternatives (value-focused), don't score pre-existing options. Walk-away point → value 0; stretch goal → 100.
- Formal trade study still biased (confirmation/optimism/rankism) → add structural guards: independent review, premortem.
- Risk treatment: evaluate **assume / avoid / mitigate / transfer** — never auto-pick mitigation. Fix root cause, not repeated instances (no band-aids).
- Cost estimate maturity: ROM (early, ballpark) → parametric/analogy → firm (binding). Analogy **must** adjust for cost drivers; calibrate CERs to current data; refresh at milestones. No historical data = a guess.
- Fixed-price + uncertain scope → high bids or supplier insolvency. Use cost-reimbursement + active change control.
- Match acquisition entry phase to technology readiness; RFP needs a SEP first.

## MBSE
- Use the model to **drive** decisions, not document them post-hoc (else you lose the whole value).
- Formality ∝ complexity/criticality: over-formal simple systems waste effort; under-formal safety-critical = ambiguity + integration risk.
- Enforce CM/updates or the model decays → teams revert to documents.
- Establish semantic interoperability across discipline models early, or integration failures surface late.

## Tells & Smells
- **Emergence present**: behavior meaningful only for the whole, unpredictable from parts. Exploit desired emergence, don't only fear it.
- **Standards proliferating**: alignment pursued without SDO commitment / domain-silo viewpoints → competing incompatible standards.
- **Loss concerns siloed**: safety/security/reliability/resilience in separate teams → redundant + conflicting requirements; unify (LDSE), one architectural pattern can cover several loss scenarios.
- **HSI as a "human factors" sub-task**: relegating it to an HFE specialist strips cross-domain authority; deferring humans to training → high manpower cost, poor usability.
- **Specialty engineering late** (logistics, reliability, certification, safety) → costly rework; pull it before requirements freeze.
- **Reductionism without holistic verification**: optimizing elements independently destroys emergent properties.
- **Reliability treated as a testing problem**: testing finds known modes, can't prove absence of unintended function — needs spec-driven design + traceability.
- **COTS over-reliance**: obsolete in ~2 yrs; plan supply or accept unplanned churn.
- **Enterprise requirements frozen**: enterprises are "constantly being designed" — locking requirements misaligns.
