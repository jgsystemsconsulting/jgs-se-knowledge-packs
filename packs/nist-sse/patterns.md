# NIST SP 800-160 (SSE) Patterns & Techniques

Reusable patterns from NIST SP 800-160 Vol 1 + Vol 2. Each has When / How / Trade-offs.

## Pattern 1: Frame Security with the Three Contexts

**When to use**: at the start of any security effort, before reaching for controls.

**How**: work the **problem context** first (assets, losses/consequences, adversity, protection needs, security requirements, environment), then the **solution context** (architecture, design, element security, trade-offs), then the **trustworthiness context** (assurance case). Iterate — let solution and trustworthiness findings revise the problem. Keep one shared base of asset/adversity analyses across all three.

**Trade-offs**: front-loading the problem context feels slow when stakeholders want controls now — but solving an unstated or wrong problem is far more expensive. Skipping trustworthiness yields confident-sounding but unproven security.

---

## Pattern 2: Apply the Design Principles as a Design Constraint and Review Gate

**When to use**: throughout architecture and design, and at every security design review.

**How**: treat the Vol 1 principles as constraints — drive toward **reduced complexity**, **minimal trusted elements**, the **"least" family** (privilege/functionality/persistence/sharing), **protective defaults/failure/recovery**, and **mediated access**. Review every security-relevant decision against the catalog; record where principles tension each other and how you resolved the trade-off.

**Trade-offs**: principles can conflict (redundancy vs. reduced complexity); resolving them is judgment, not formula. Applying them in design is cheap; retrofitting them after architecture is fixed is expensive or infeasible.

---

## Pattern 3: Build the Assurance Case from the Claims Backward

**When to use**: from the start of the trustworthiness context — not at the end.

**How**: state the top-level security **claims**, decompose them into **arguments**, and decide *up front* what **evidence** (analyses, tests, reviews, formal proofs) will substantiate each. Design and plan V&V to produce that evidence across the life cycle. Scale rigor to consequence (up to formal verification for the highest assurance).

**Trade-offs**: planning assurance early constrains the design (it must be analyzable) and costs effort — but a claim with no case is an assertion, and end-loaded "prove it at the end" assurance routinely fails.

---

## Pattern 4: Integrate Security Across the Life Cycle, Not as a Silo

**When to use**: when SSE runs inside an existing 15288-based (or NASA/DoD) life cycle.

**How**: add security outcomes and tasks to each process group — technical (requirements→V&V→disposal), technical-management (risk, configuration, information, measurement), organizational-project-enabling, and agreement (supply chain). Manage trust relationships through agreement and configuration/information management.

**Trade-offs**: integration requires SSE to engage every process owner, which is more coordination than a security silo — but siloed security misses the supply chain and the early decisions where trust is set. *(Name the 15288 groups; don't reproduce their text.)*

---

## Pattern 5: Select Cyber-Resiliency Techniques Against the Adversary (Assume Breach)

**When to use**: for systems whose mission depends on cyber resources and must operate through compromise.

**How**: start from the **critical mission functions** and the **APT** (its goals, vectors, adaptation). Choose objectives, then techniques by needed effect — *detect* (Analytic Monitoring, Contextual Awareness, Substantiated Integrity), *contain* (Segmentation, Privilege Restriction, Non-Persistence, Realignment), *survive/recover* (Redundancy, Diversity, Dynamic Positioning, Adaptive Response, Coordinated Protection), *confuse* (Deception, Unpredictability). Place them per the strategic/structural design principles. Pair recovery techniques with Substantiated Integrity so the adversary can't corrupt the recovery.

**Trade-offs**: every technique costs money, performance, and complexity, and the APT adapts — so this is a continual risk investment, not a one-time deployment. Implementing all 14 regardless of mission/adversary is cost without focus.

---

## Pattern 6: Govern Resiliency Through the Risk Framework

**When to use**: when justifying and prioritizing resiliency investment.

**How**: express resiliency techniques as security/privacy controls and enhancements, select/implement/assess/authorize them through the **RMF (SP 800-37)** and **SP 800-53**, and prioritize by mission risk reduced per unit cost, informed by the organizational risk strategy.

**Trade-offs**: routing resiliency through risk governance adds process, but resiliency disconnected from the RMF and control set can't be prioritized, assessed, or sustained.
