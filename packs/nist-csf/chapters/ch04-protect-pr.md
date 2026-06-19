# Chapter 4: PROTECT (PR) Function

## Core Idea
PROTECT implements safeguards that prevent or lower the likelihood and impact of adverse cybersecurity events across five domains: identity and access control, awareness and training, data security, platform security, and technology infrastructure resilience.

## Frameworks Introduced
- **PROTECT (PR)**: The Function that operationalizes safeguards to manage cybersecurity risks identified and prioritized by IDENTIFY, covering both preventive controls and resilience measures.
  - When to use: once assets and risks are identified and prioritized; PROTECT outcomes are applied continuously to maintain security posture.

## Key Concepts
- **Identity Management, Authentication, and Access Control (PR.AA)**: Limiting access to physical and logical assets to authorized users, services, and hardware, managed commensurate with assessed risk; encompasses credential management (PR.AA-01), identity proofing (PR.AA-02), authentication (PR.AA-03), identity assertion protection (PR.AA-04), least privilege and separation of duties (PR.AA-05), and physical access control (PR.AA-06).
- **Awareness and Training (PR.AT)**: Providing personnel with the cybersecurity knowledge and skills to perform their tasks; covers general workforce awareness (PR.AT-01) and specialized-role training (PR.AT-02).
- **Data Security (PR.DS)**: Protecting the confidentiality, integrity, and availability of data at rest (PR.DS-01), in transit (PR.DS-02), and in use (PR.DS-10), and ensuring tested backups exist (PR.DS-11).
- **Platform Security (PR.PS)**: Managing hardware, software (firmware, OS, applications), and services of physical and virtual platforms through configuration management (PR.PS-01), software maintenance (PR.PS-02), hardware maintenance (PR.PS-03), log generation (PR.PS-04), prevention of unauthorized software (PR.PS-05), and secure software development life-cycle integration (PR.PS-06).
- **Technology Infrastructure Resilience (PR.IR)**: Maintaining security architectures that protect confidentiality, integrity, and availability and ensure organizational resilience, including network protection (PR.IR-01), environmental threat protection (PR.IR-02), resilience mechanisms (PR.IR-03), and capacity management (PR.IR-04).
- **Least Privilege**: The principle, enforced under PR.AA-05, that access permissions are limited to the minimum necessary for a user, service, or hardware component to perform its function.
- **Separation of Duties**: A control principle co-located with least privilege (PR.AA-05) that divides critical functions across multiple individuals or roles to reduce insider risk.
- **Secure Software Development Life Cycle (SSDLC)**: The integration of secure development practices throughout the software development life cycle, monitored under PR.PS-06.

## Mental Models
- Use PR.AA as the access control foundation before other safeguards: unauthorized access undermines every other protection measure.
- Use PR.DS-11 (tested backups) as the prerequisite for RECOVER: backups that have not been verified for integrity (RC.RP-03) are not a reliable recovery asset.
- Use PR.PS-04 (log generation) to feed DETECT: platforms that do not generate accessible log records cannot support continuous monitoring (DE.CM).

## Anti-patterns
- **Skipping identity proofing (PR.AA-02)**: Binding credentials without proofing the identity allows unauthorized actors to legitimately obtain access.
- **Configuration management as a one-time exercise (PR.PS-01)**: Configuration baselines must be maintained and applied continuously; unmanaged configuration drift is a persistent attack surface.
- **Ignoring data-in-use protection (PR.DS-10)**: Protecting only data at rest and in transit leaves memory-resident data exposed to extraction attacks.

## Key Takeaways
1. PROTECT spans five Categories addressing different attack surfaces: identity/access, human factors, data state, platform, and infrastructure resilience.
2. Least privilege and separation of duties (PR.AA-05) are explicitly stated principles within access control, not optional enhancements.
3. Data security must cover all three data states: at rest (PR.DS-01), in transit (PR.DS-02), and in use (PR.DS-10) — and tested backups (PR.DS-11) are part of data protection, not only recovery.
4. Platform security (PR.PS) explicitly includes secure software development (PR.PS-06) and prevention of unauthorized software execution (PR.PS-05), connecting development and operations.
5. Log generation (PR.PS-04) is a PROTECT outcome, but its value is realized in DETECT; protection and detection are interdependent.
6. Technology Infrastructure Resilience (PR.IR) includes capacity management (PR.IR-04), acknowledging that availability failures — not just attacks — are a cybersecurity concern.

## Connects To
- **IDENTIFY (ID)**: Asset inventories and risk prioritization from IDENTIFY determine where PROTECT safeguards are applied and at what intensity.
- **DETECT (DE)**: Log generation (PR.PS-04) and network protection configurations (PR.IR-01) create the monitoring substrate that DETECT relies on.
- **RECOVER (RC)**: Tested backup integrity (PR.DS-11) is the data-level prerequisite for reliable execution of the recovery plan (RC.RP-03).
- **SP 800-53 (Security and Privacy Controls)**: The primary Informative Reference for implementing specific controls that achieve PROTECT outcomes.
- **NIST SP 800-218 (Secure Software Development Framework)**: Guidance that operationalizes the secure development life-cycle integration required by PR.PS-06.
