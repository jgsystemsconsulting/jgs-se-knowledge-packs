# NIST SSDF v1.1 Patterns & Techniques

## Pattern: Shift-Left Security Integration
**When to use**: Whenever security is currently addressed only during testing or post-release; when technical debt from late-stage security fixes is escalating.
**How**: Define security requirements at programme inception (PO.1); perform threat modelling and risk assessment at design time (PW.1.1); review designs before implementation (PW.2.1); apply secure coding standards during development (PW.5.1); use static analysis as a CI gate (PW.7).
**Trade-offs**: Requires upfront investment in training and tooling; may slow initial design iterations; pays back through dramatically lower cost of remediation compared to post-release fixes.

---

## Pattern: Security Requirements Flow-Down to Suppliers
**When to use**: When acquiring commercial, open-source, or custom software components from third parties; when supply-chain risk is a concern.
**How**: Define a core set of security requirements in acquisition documents (PO.1.3); require third parties to attest compliance; require provenance data and integrity verification mechanisms; establish processes for exception handling when requirements are not met.
**Trade-offs**: Increases contract complexity and supplier negotiation overhead; reduces supply-chain risk; may limit available supplier pool if requirements are stringent.

---

## Pattern: Toolchain-as-Code with Audit Artefacts
**When to use**: When build and deployment pipelines are manually configured, difficult to audit, or inconsistently applied across teams.
**How**: Specify mandatory tools and integration points (PO.3.1); implement pipelines-as-code and toolchains-as-code (PO.3.2); configure tools to generate signed, tamper-evident artefacts of their security activities (PO.3.3); continuously monitor tool logs for anomalous behaviour.
**Trade-offs**: Initial migration to code-based pipeline configuration has high setup cost; provides reproducible builds, audit trails, and significantly easier incident investigation thereafter.

---

## Pattern: Security Gates (Definition-of-Done for Security)
**When to use**: In agile or continuous-delivery environments where security work competes with feature work and risks being deferred.
**How**: Define KPIs, KRIs, and vulnerability severity thresholds as explicit security criteria (PO.4.1); integrate criteria into the Definition-of-Done for each sprint or release (PO.4.1 Example 3); record approvals, rejections, and exceptions in the workflow tracking system (PO.4.2).
**Trade-offs**: Security gates can slow release velocity if poorly calibrated; properly calibrated gates prevent accumulation of high-severity technical debt.

---

## Pattern: Least-Privilege Code Repository Access
**When to use**: When source code repositories, build systems, or distribution channels have overly broad write access; when supply-chain attack risk is elevated.
**How**: Restrict access to source code, executables, and configuration-as-code based on least privilege (PS.1.1); require commit signing for all contributions; designate code owners to review and approve changes; use cryptographic hashes or signatures to protect file integrity.
**Trade-offs**: Access control overhead and signing key management add operational complexity; provides strong defence against insider threats and supply-chain compromises.

---

## Pattern: SBOM Capture at Release
**When to use**: At every software release; when post-release vulnerability analysis may require knowing component composition.
**How**: Collect provenance data for all components at build time (PS.3.2); store SBOMs in a location separate from release files or sign the data; update the SBOM every time any component is updated; make provenance data available to acquirers in standards-based formats.
**Trade-offs**: Requires tooling investment to automate SBOM generation; enables rapid triage when new CVEs are published against components.

---

## Pattern: Threat Modelling at Design Time
**When to use**: Before architecture is finalised; when designing systems that handle sensitive data, authentication, or privileged operations.
**How**: Train security champions or engage a risk modelling expert (PW.1.1); use threat modelling, attack modelling, or attack surface mapping; record risk responses and mitigations; add mitigations to security requirements; maintain records for audit and maintenance throughout the software life cycle (PW.1.2).
**Trade-offs**: Time investment at design phase; substantially reduces the probability and cost of security vulnerabilities that require architectural rework if found late.

---

## Pattern: Standardised Security Module Reuse
**When to use**: When developers are implementing authentication, cryptography, session management, or logging from scratch.
**How**: Maintain a software repository of vetted modules for standardised security features (PW.1.3); provide configuration-as-code so developers can adopt secure configurations readily; define criteria specifying which security features must be supported by all software under development.
**Trade-offs**: Requires investment in module vetting and maintenance; eliminates entire classes of bespoke implementation vulnerabilities; reduces developer burden.

---

## Pattern: Continuous Third-Party Component Verification
**When to use**: When managing open-source or commercial dependencies that may acquire new CVEs after initial adoption.
**How**: Build automated vulnerability scanning into the CI/CD toolchain (PW.4.4); check whether each component is still actively maintained; obtain provenance information (SBOM, SCA) for each component; establish sanctioned component repositories; have a plan of action for components reaching end-of-life.
**Trade-offs**: Requires toolchain integration and triage capacity for scanner output; prevents accumulation of unpatched dependencies that become exploitable.

---

## Pattern: Clean Build Compiler Hardening
**When to use**: When setting up new build pipelines; when updating compiler or build tool versions.
**How**: Use up-to-date compiler and build tool versions (PW.6.1); enable security-relevant compiler features (ASLR, stack canaries, memory randomisation); treat all compiler warnings as errors — the clean-build concept (PW.6.2 Example 2); make approved configurations available as configuration-as-code; perform all builds in a dedicated, highly controlled build environment.
**Trade-offs**: Eliminating all warnings may initially require code changes; provides systematic reduction in exploitable executable vulnerabilities at zero per-build runtime cost.

---

## Pattern: Layered Code Review (Human + Static Analysis)
**When to use**: Before merging code into main branches; as a continuous CI gate; for high-risk changes involving security-sensitive functionality.
**How**: Define when code review and code analysis should be performed (PW.7.1); use automated static analysis tools for continuous coverage (PW.7.2); supplement with human peer review for security logic, backdoor detection, and design intent; record root causes of discovered issues; document lessons learned in a searchable wiki.
**Trade-offs**: Human review is resource-intensive; automation catches many issues cheaply but misses design-level flaws; both are needed for comprehensive coverage.

---

## Pattern: Vulnerability Disclosure and Root-Cause Feedback Loop
**When to use**: When a vulnerability is confirmed post-release; when building an organisational practice of continuous security improvement.
**How**: Analyse the vulnerability to determine root cause (RV.3.1); search proactively for all instances of the same root cause in the codebase (RV.3.3); update SDLC practices to prevent recurrence (RV.3.4); record findings in a developer-accessible wiki; communicate remediations to acquirers via security advisories (RV.2.2).
**Trade-offs**: Root cause analysis requires dedicated time post-incident; converts one-off patching into systematic process improvement that reduces future vulnerability frequency.

---

## Pattern: Risk-Based Vulnerability Prioritisation
**When to use**: When multiple vulnerabilities have been identified and remediation resources are constrained.
**How**: Analyse each vulnerability for exploitability, potential impact, and other characteristics to produce a risk score (RV.2.1); make a risk-based decision to remediate, accept, or transfer risk for each; develop and release security advisories with temporary mitigations where permanent fixes are not yet available (RV.2.2); deliver remediations via trusted automated channels.
**Trade-offs**: Risk acceptance must be documented and reviewed; prioritisation without risk calculations may lead to focusing on low-risk, high-visibility issues while high-risk issues linger.
