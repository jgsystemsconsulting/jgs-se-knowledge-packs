# Chapter 4: Produce Well-Secured Software (PW)

## Core Idea
The PW practice group covers the activities within the SDLC that directly produce software with minimal security vulnerabilities: secure design, secure component reuse, secure coding, secure compilation, code review, executable testing, and secure default configuration.

## Frameworks Introduced
- **PW.1 — Design Software to Meet Security Requirements and Mitigate Security Risks**: Identify security requirements, perform risk modelling (threat modelling, attack modelling, attack surface mapping), document risk responses, and prefer standardised security features over proprietary implementations.
  - When to use: At software design time; when evaluating technology stack risk; when deciding whether to build vs. reuse security features.
- **PW.2 — Review the Software Design to Verify Compliance with Security Requirements and Risk Information**: Have a qualified person not involved with the design (and/or automated toolchain processes) review the design against security requirements and risk models.
  - When to use: After design stabilises and before implementation begins; at any major design change.
- **PW.4 — Reuse Existing, Well-Secured Software When Feasible**: Acquire and maintain well-secured third-party components; create well-secured in-house components for common needs; verify that all third-party components comply with security requirements throughout their life cycles.
  - When to use: Whenever a software function could be fulfilled by an existing library, framework, or module; when managing open-source dependencies.
- **PW.5 — Create Source Code by Adhering to Secure Coding Practices**: Follow secure coding practices appropriate to the development language and environment; validate all inputs; encode outputs; avoid unsafe functions; handle errors gracefully; provide logging and tracing.
  - When to use: Throughout the coding phase; during code review; when updating coding standards.
- **PW.6 — Configure the Compilation, Interpreter, and Build Processes to Improve Executable Security**: Use compiler and build tool features that improve executable security (e.g., memory randomisation, warnings-as-errors, clean builds); document and enforce approved configurations.
  - When to use: When setting up or updating build pipelines; when adopting new compiler versions.
- **PW.7 — Review and/or Analyze Human-Readable Code to Identify Vulnerabilities**: Perform code review (human) and/or code analysis (automated static analysis) based on secure coding standards; record and triage all discovered issues.
  - When to use: Before merging code; as a continuous CI/CD gate; at defined security gates in the SDLC.
- **PW.8 — Test Executable Code to Identify Vulnerabilities**: Scope and perform dynamic testing (functional testing, fuzz testing, penetration testing) on executable code; document results and root causes.
  - When to use: After code compilation; before release; on a continuous basis for supported releases.
- **PW.9 — Configure Software to Have Secure Settings by Default**: Define a secure configuration baseline for all security-relevant settings so that default values do not weaken platform or infrastructure security; document each setting's purpose, options, and operational impact.
  - When to use: Before initial release; whenever default settings are changed; when software is ported to a new platform.

## Key Concepts
- **Threat Modelling / Attack Surface Mapping (PW.1.1)**: Risk modelling techniques used at design time to identify and prioritise security risks so that mitigations can be designed in rather than retrofitted.
- **Secure by Design (PW.1)**: The principle that security requirements and risk responses should shape software architecture from the outset, reducing the cost and difficulty of achieving adequate security.
- **Standardised Security Features (PW.1.3)**: Reuse of existing, vetted modules for security functions (logging, identity management, access control, cryptography) rather than creating proprietary implementations that are harder to audit.
- **Third-Party Component Verification (PW.4.4)**: Ongoing confirmation that acquired commercial, open-source, and other external software components remain compliant with security requirements throughout their life cycles, including checking for newly disclosed vulnerabilities.
- **Provenance / SBOM for Components (PW.4.1)**: Obtaining and analysing source composition analysis or binary composition analysis data for each acquired component to assess supply-chain risk.
- **Secure Coding Practices (PW.5.1)**: Language-appropriate rules including input validation, output encoding, avoiding unsafe functions, error handling, and logging; implemented via developer training, linters, and automated enforcement in IDEs and CI.
- **Clean Build (PW.6.2)**: A build philosophy where all compiler warnings are treated as errors and eliminated (except confirmed false positives), producing a warning-free build baseline.
- **Static Analysis / Code Analysis (PW.7.2)**: Automated tools that examine source code or bytecode for vulnerabilities and coding standard violations without executing the code; produces findings for human triage.
- **Fuzz Testing (PW.8.2)**: Automated testing technique that sends malformed or unexpected inputs to the software to discover input-handling vulnerabilities and crashes.
- **Secure Default Configuration (PW.9.1)**: A defined baseline where every security-relevant setting's default value does not weaken the security functions provided by the platform, network infrastructure, or dependent services.

## Mental Models
- Use threat modelling before writing a line of code: risk identified at design time costs an order of magnitude less to mitigate than risk found post-release.
- Use standardised security modules (PW.1.3) in preference to proprietary implementations: vetted shared code accumulates security review across many users; bespoke cryptography rarely does.
- Use PW.4.4 continuous third-party verification as a pipeline gate, not a one-time check: open-source components acquire new CVEs daily; point-in-time vetting at acquisition is insufficient.
- Use compiler hardening features (PW.6) as the first automated layer of defence: ASLR, stack canaries, and warnings-as-errors are free security gains requiring only configuration.

## Anti-patterns
- **Waiving security requirements without tracking exceptions (PW.1.2)**: All approved exceptions to security requirements must be recorded and periodically re-evaluated; undocumented waivers become permanent hidden risks.
- **Using components beyond their end-of-life (PW.4.4)**: Each component must be verified as still actively maintained; unmaintained components accumulate unpatched vulnerabilities with no vendor remediation path.
- **Performing code review only for functionality, not security**: PW.7 explicitly requires review against secure coding standards and the use of expert reviewers for backdoors and malicious content, not just logic correctness.

## Key Takeaways
1. Security must be addressed at design time via risk modelling; approved exceptions must be documented and re-evaluated.
2. Prefer standardised, vetted security modules over custom implementations for authentication, cryptography, and access control.
3. Third-party components require acquisition-time vetting and ongoing lifecycle verification against newly disclosed vulnerabilities.
4. Compiler and build tool security features (hardening flags, clean-build discipline) should be configured and enforced automatically.
5. Both static code analysis and dynamic executable testing are required; each finds classes of vulnerabilities the other misses.
6. All software must ship with secure default settings that do not degrade platform or infrastructure security.
7. Root causes of all discovered issues should be recorded to inform future prevention.

## Connects To
- **OWASP ASVS / MASVS**: PW.1, PW.5, PW.7 practices align with OWASP Application and Mobile Security Verification Standards.
- **NIST IR 8397 (Developer Verification of Software)**: PW.6, PW.7, PW.8 reference IR 8397 for minimum verification standards.
- **IEC 62443-4-1 (Secure Product Development Lifecycle)**: Multiple PW practices reference IEC 62443 for industrial control system contexts.
- **NIST SP 800-53 SA-11 (Developer Testing and Evaluation)**: PW.7 and PW.8 tasks map to SP 800-53 SA-11 controls.
