# Chapter 3: Protect the Software (PS)

## Core Idea
The PS practice group ensures that all components of software — source code, executables, configuration, and provenance data — are protected from tampering and unauthorised access throughout the SDLC and after release, so that acquirers receive software whose integrity and lineage can be verified.

## Frameworks Introduced
- **PS.1 — Protect All Forms of Code from Unauthorized Access and Tampering**: Store all code — source code, executable code, and configuration-as-code — using least-privilege access controls and version-controlled repositories with commit signing.
  - When to use: When setting up or auditing source code repositories, build pipelines, and distribution channels; essential for any software whose integrity or confidentiality matters.
- **PS.2 — Provide a Mechanism for Verifying Software Release Integrity**: Make integrity verification information (e.g., cryptographic hashes, code signatures) available to software acquirers so they can confirm that software has not been tampered with.
  - When to use: Before every software release; when designing distribution channels; when acquirers demand supply-chain assurance.
- **PS.3 — Archive and Protect Each Software Release**: Securely retain release files, integrity verification information, provenance data, and SBOMs so that vulnerabilities discovered post-release can be identified, analysed, and remediated.
  - When to use: At every software release; when establishing retention policies; when post-release vulnerability response requires historical artefact analysis.

## Key Concepts
- **Least-Privilege Code Access (PS.1.1)**: Restricting access to source code, executables, and configuration-as-code so that only authorised personnel, tools, and services can read or modify it; the principle determines access scope, not the code type.
- **Commit Signing**: Cryptographically signing commits in a version control system to establish accountability to an individual account and detect unauthorised changes.
- **Code Signing (PS.1.1)**: Using a certificate-authority-issued certificate to sign executable files, enabling consumers' operating systems or tools to verify signature validity before execution.
- **Configuration-as-Code**: Storing environment and toolchain configuration in versioned repositories, subject to the same access controls and integrity protections as source code.
- **Software Release Integrity Verification (PS.2.1)**: Publishing cryptographic hashes or digital signatures for release files so acquirers can independently confirm authenticity and detect tampering.
- **Provenance Data (PS.3.2)**: A record of the chronology of origin, development, ownership, and changes for all components of a software release; must be protected, updatable, and shareable with acquirers.
- **Software Bill of Materials (SBOM) (PS.3.2)**: A formal, machine-readable record enumerating all components of a software release, enabling supply-chain risk visibility; referenced by NTIA minimum elements guidance.
- **Secure Archive (PS.3.1)**: Read-only retention of release files and supporting data in repositories where integrity verification information and provenance data are stored separately from or signed apart from the release files themselves.

## Mental Models
- Use code signing and cryptographic hashes together: hashes enable independent verification, code signing binds identity to the artefact; both are needed for a complete PS.2 implementation.
- Use provenance data and SBOMs proactively: if post-release vulnerability analysis requires knowing what third-party components are in a release, the SBOM must have been captured at release time, not reconstructed retrospectively.
- Use least privilege on code repositories as a first-order control: most supply-chain attacks (e.g., SolarWinds-style) exploit excessive write access to build infrastructure.

## Anti-patterns
- **Storing integrity verification data in the same location as release files**: PS.3.1 explicitly requires keeping them separate or signing the data; co-location allows an attacker who compromises the release to also falsify the hash.
- **Skipping SBOM capture at release time**: Provenance data must be updated every time software components are updated (PS.3.2); retroactive reconstruction after a vulnerability disclosure is unreliable.

## Key Takeaways
1. All forms of code — source, executable, configuration — must be stored under least-privilege access with version-controlled accountability.
2. Commit signing and code signing provide layered tamper-evidence at the repository and distribution layers respectively.
3. Cryptographic integrity verification information must be published alongside every release so acquirers can independently verify authenticity.
4. SBOMs and provenance data must be collected, protected, and shared at release time and updated with every component change.
5. Archived releases and their provenance data are prerequisite inputs to post-release vulnerability analysis and response.

## Connects To
- **NTIA SBOM Minimum Elements**: PS.3.2 directly references NTIA guidance for structuring provenance data.
- **EO 14028 Section 4e(iii), 4e(vi), 4e(vii), 4e(x)**: PS practices collectively address software supply-chain integrity provisions of the EO.
- **NIST SP 800-161 (C-SCRM)**: PS.3.2 provenance sharing supports supply-chain risk management at the acquisition interface.
- **CNCF Software Supply Chain Best Practices**: PS.1.1, PS.2.1, and PS.3 practices align with CNCF securing-materials and securing-artefacts controls.
