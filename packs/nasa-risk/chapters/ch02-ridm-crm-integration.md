# Chapter 2: RIDM–CRM Integration and RM Planning

## Core Idea
RIDM and CRM are not independent processes — they operate within every organisational unit, hand off outputs to each other, and trigger re-execution when conditions change; a preliminary Risk Management Plan (RMP) is prepared before RIDM begins, then finalised once CRM is initialised.

## Frameworks Introduced
- **Coordination of RIDM and CRM**: The mechanism by which RIDM's risk analysis of the selected alternative seeds CRM's initial risk list, and CRM's evolving products can feed back into RIDM to reconsider a decision.
  - When to use: At every programme/project transition point where requirements are being set or reset.
- **Requirements Rebaselining Process**: When CRM cannot manage performance risk within current requirements, RIDM is re-invoked at Part 1 (Identification of Alternatives) to produce a new baseline.
  - When to use: When CRM identifies an unmanageable risk or when a modification to the selected alternative changes derived requirements at lower levels.
- **Preliminary Risk Management Plan (RMP)**: A planning document prepared before RIDM that guides how the RIDM process will be conducted at the project level.
  - When to use: When project-level RIDM is initiated; the programme-level RMP already exists and provides the requirements basis.

## Key Concepts
- **RIDM to CRM Initialisation**: The scenarios from the RIDM risk analysis of the selected alternative become the initial risk list for CRM, seeding the Identify, Analyse, and Plan activities.
- **Parameter-Based vs. Scenario-Based Models**: During RIDM, cost and mass growth models tend to be parameter-based (aggregate from components). CRM transitions to scenario-based models (event trees, fault trees) that account for project-specific conditions and departures.
- **Requirements Rebaselining**: Two triggers exist — (1) an unresolvable new risk scenario forces elevation and rebaselining; (2) a chosen mitigation modifies derived requirements flowing to lower units. Both warrant RIDM re-invocation when the degree of modification is sufficiently large.
- **Sunk Cost / Status Quo Mindset**: A pitfall NASA explicitly warns against when rebaselining — the scope of RIDM on re-invocation should be as narrow as practical but not reflect sunk cost bias; alternatives previously discarded may now be attractive.
- **Maintaining a Functioning RIDM Capability**: Requires live access to objectives hierarchies, risk analysis frameworks, risk models, and discipline expertise throughout the project life cycle — not just at milestones.
- **Elevation Protocol**: When a unit cannot manage its risk to its requirements, the risk management decision is elevated to the next higher level, which can release margin, relax requirements, or re-execute RIDM.

## Mental Models
- Think of the RIDM-to-CRM handoff as seeding a garden: RIDM plants the initial risk list and performance commitments; CRM tends and grows that list through implementation, sending new information back to update the seeds.
- When CRM produces a mitigation strategy applicable across alternatives, check whether it retroactively shifts the preferred alternative — if so, re-examine the decision.
- Rebaselining scope should be narrow but unbiased: look only at what has changed, but don't exclude previously rejected alternatives simply because resources have already been spent.

## Anti-patterns
- **Treating the initial RIDM risk list as the complete CRM risk list**: The RIDM analysis targets discriminators between alternatives; non-discriminator performance measures are often only modelled simply. CRM must complete and expand this picture.
- **Executing RIDM in isolation from CRM feedback**: If CRM produces improved mitigation data and it is not fed back into the RIDM risk model, decisions are based on stale analysis.

## Key Takeaways
1. The RIDM risk analysis of the selected alternative is not a replacement for CRM — it is a starting point that CRM must expand and update.
2. A preliminary RMP is prepared before RIDM and finalised at CRM initialisation; the two versions differ mainly in level of detail.
3. Rebaselining is not a failure of CRM — it is a recognised pathway back to RIDM when existing requirements become unachievable.
4. When elevation occurs, affected organisational units at all levels whose derived requirements change must participate in the rebaselining process.
5. Maintaining live, accessible risk models and objectives hierarchies throughout the life cycle is essential infrastructure for a functioning RM capability.

## Connects To
- **NPR 8000.4A**: Specifies the RIDM and CRM requirements and the organisational hierarchy within which they operate.
- **NASA Systems Engineering Handbook**: Provides the requirements flowdown and negotiation process context.
- **Section 3 (RIDM Process)**: Detailed RIDM steps that feed into the integration.
- **Section 4.1 (CRM Initialisation)**: Where RIDM outputs are formally received into CRM.
