# NIST SSDF v1.1 Cheatsheet

## Decision Rules

| Situation | Go-to Practice |
|-----------|---------------|
| Starting a new project / programme | PO.1 — define security requirements first |
| Onboarding a new supplier | PO.1.3 — flow security requirements into contracts with attestation |
| Setting up a new build pipeline | PO.3 — toolchains-as-code + artefact generation |
| Running agile sprints | PO.4 — add security criteria to Definition-of-Done |
| Designing new software | PW.1 — threat model; document risk responses |
| Reviewing a software design | PW.2 — independent qualified reviewer |
| Adding a new open-source dependency | PW.4.1 + PW.4.4 — acquire and continuously verify |
| Writing code | PW.5 — follow secure coding practices for your language |
| Configuring the build | PW.6 — enable compiler hardening; clean-build |
| Merging code | PW.7 — static analysis + peer review gate |
| Pre-release testing | PW.8 — dynamic testing, fuzz, pen test if high-risk |
| Shipping a release | PS.1 + PS.2 + PS.3 — lock down code, publish hashes, archive SBOM |
| CVE published against a dependency | RV.1.1 + RV.2.1 — confirm, assess, prioritise |
| Vulnerability report received | RV.1.3 (PSIRT) + RV.2 — triage → remediate → advisory |
| Post-patch retrospective | RV.3 — root cause → class fix → SDLC update |

---

## Practice Group Quick-Reference

| Group | ID | Practice Name | Key Output |
|-------|----|---------------|-----------|
| **PO** | PO.1 | Define Security Requirements | Requirements documents; supplier contract clauses |
| **PO** | PO.2 | Implement Roles and Responsibilities | Role matrix; training plan |
| **PO** | PO.3 | Implement Supporting Toolchains | Toolchain artefacts; pipelines-as-code |
| **PO** | PO.4 | Define and Use Security Check Criteria | KPIs/KRIs; gate records |
| **PO** | PO.5 | Implement Secure Dev Environments | Segmented envs; hardened endpoints |
| **PS** | PS.1 | Protect All Forms of Code | Signed commits; least-privilege repos |
| **PS** | PS.2 | Provide Release Integrity Mechanism | Published hashes; code signatures |
| **PS** | PS.3 | Archive and Protect Each Release | SBOM; provenance archive |
| **PW** | PW.1 | Design to Meet Security Requirements | Threat model; risk response record |
| **PW** | PW.2 | Review Software Design | Design review findings |
| **PW** | PW.4 | Reuse Well-Secured Software | Vetted component registry |
| **PW** | PW.5 | Adhere to Secure Coding Practices | Code compliant with standards |
| **PW** | PW.6 | Configure Build for Executable Security | Hardened build config |
| **PW** | PW.7 | Review/Analyze Human-Readable Code | Static analysis + review findings |
| **PW** | PW.8 | Test Executable Code | Dynamic test results; fuzz findings |
| **PW** | PW.9 | Secure Settings by Default | Default config baseline; documented settings |
| **RV** | RV.1 | Identify and Confirm Vulnerabilities | Confirmed vulnerability records |
| **RV** | RV.2 | Assess, Prioritize, Remediate | Risk scores; patches; advisories |
| **RV** | RV.3 | Analyze Root Causes | Root cause wiki; SDLC updates |

---

## Tells and Smells (Signs a Practice is Missing)

- **No security requirements document** → PO.1 not done; no basis for design decisions or supplier contracts.
- **Security role = job title with no training** → PO.2 not done; training plan and proficiency review are required.
- **Build pipeline configured via UI clicks, no code** → PO.3 gap; configuration drift and non-reproducible builds.
- **Security work deferred every sprint** → PO.4 gap; security criteria not in Definition-of-Done.
- **Anyone on the team can push to main** → PS.1 gap; no least-privilege access or commit signing.
- **No hash or signature published with releases** → PS.2 not done; acquirers cannot verify integrity.
- **No SBOM; can't say what's in the release** → PS.3 gap; post-release CVE triage will be blind.
- **No threat model for the design** → PW.1 gap; risk-based architecture decisions are impossible.
- **All dependencies are latest-at-adoption, never rechecked** → PW.4.4 gap; accumulated unpatched CVEs.
- **No static analysis in CI** → PW.7 gap; vulnerabilities reach review/test that analysis would catch cheaply.
- **Software ships with debug mode on by default** → PW.9 gap; insecure default configuration.
- **Vulnerability patched, no root cause documented** → RV.3 gap; same class will reappear.
- **No disclosure programme; researchers have no way to report** → RV.1.3 gap; external findings go unreported or go public without coordination.

---

## Key Thresholds from the Document
- Security requirements: review **at least annually**, or sooner after major incidents or new regulatory requirements.
- Roles and responsibilities: **annual review** of all defined roles.
- Third-party exceptions to requirements: **periodic review of all approved exceptions** — no permanent waivers.
- Design exceptions: **periodically re-evaluate** all approved exceptions to security requirements.
- Environment monitoring: **continuous** logging, monitoring, and auditing — not periodic snapshots.
