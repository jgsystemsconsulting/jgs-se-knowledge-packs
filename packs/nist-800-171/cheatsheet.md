# Cheatsheet — NIST SP 800-171 Rev. 3

## Decision rules
1. **Does the component process, store, transmit, or protect CUI?** If no → out of 800-171 scope. If yes → in scope.
2. **Is the system operated on behalf of a federal agency?** If yes → FISMA/full federal controls, not the nonfederal 800-171 set alone.
3. **Can CUI be isolated?** Prefer a dedicated security domain before enterprise-wide rollout.
4. **ODP blank?** Agency should set it; if not, nonfederal org must assign a value before assessment.
5. **Enduring limitation vs temporary gap?** Enduring → document in SSP. Temporary → POA&M with owner/date/resources.
6. **External provider touches CUI?** Flow down requirements + oversight + monitoring (acquisition/SCRM families).
7. **Crypto used for CUI confidentiality?** Manage keys and prefer FIPS-validated modules.
8. **Discussion text vs requirement text?** Only the requirement statement is normative.

## Family → chapter map
| Families | Chapter |
|----------|---------|
| Fundamentals, tailoring, ODP model | ch01 |
| AC + IA | ch02 |
| AT + PS + PE | ch03 |
| AU + CM | ch04 |
| IR + MA + MP | ch05 |
| RA + CA-like assessment/monitoring + PL | ch06 |
| SC + SI | ch07 |
| SA + SR | ch08 |

## Quick requirement anchors
| Need | Start at |
|------|----------|
| MFA | 03.05.03 (ch02) |
| Least privilege | 03.01.05–07 (ch02) |
| Audit failure response | 03.03.04 (ch04) |
| Allow-list software | 03.04.08 (ch04) |
| IR plan | 03.06.05 (ch05) |
| Media sanitization | 03.08.03 (ch05) |
| Vulnerability scanning | 03.11.02 (ch06) |
| POA&M | 03.12.02 (ch06) |
| SSP | 03.15.02 (ch06) |
| Boundary protection | 03.13.01 (ch07) |
| Flaw remediation | 03.14.01 (ch07) |
| SCRM plan | 03.17.01 (ch08) |

## Tells & smells
| Smell | Likely gap |
|-------|------------|
| CUI on general-purpose file shares with broad ACLs | Scope isolation + AC/flow enforcement |
| Shared admin passwords | IA + AC privileged account controls |
| No MFA on VPN to CUI enclave | 03.05.03 / remote access |
| Logs retained but never reviewed | 03.03.05 |
| Golden image never updated | CM baseline drift |
| IR binder dated 3+ years, no exercises | 03.06.03–05 |
| Vendor remote access always-on | 03.07.05 |
| Disks surplus'ed without wipe certs | 03.08.03 |
| Open assessment findings without POA&M | 03.12.02 |
| EOL OS “because the app needs it” | 03.16.02 |
| SaaS holds CUI, no flow-down clause | 03.16.03 / 03.17.xx |

## What this pack is not
- Not CMMC scoring guidance
- Not a substitute for SP 800-171A assessor procedures
- Not legal advice on DFARS/contract clauses
- Not a full SP 800-53 control catalog
