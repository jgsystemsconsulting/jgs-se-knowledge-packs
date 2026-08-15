# Cheatsheet — CISA CPG 2.0

## Decision rules
1. **Need a prioritized baseline for critical infrastructure IT/OT?** Start with CPGs, not full control catalogs.
2. **Still on 1.x IDs?** Remap to 2.0 before scoring.
3. **No GOVERN owners?** Fix responsibilities (1.A) before tool sprawl.
4. **OT present?** Apply universal goals with safety-aware implementation — do not ignore OT as “out of scope IT.”
5. **Where to start if everything is red?** Identity/MFA, defaults, segmentation, backups, logging, IR plan.
6. **MSP in the path?** Treat as GOVERN risk (1.E) plus access hardening.
7. **Board briefing?** Use outcome language; keep recommended actions in the appendix.
8. **Done with CPGs?** No — expand toward fuller CSF/sector programs; CPGs are the floor.

## Function → chapter map
| Function | Goals (examples) | Chapter |
|----------|------------------|---------|
| GOVERN | 1.A–1.E | ch02 |
| IDENTIFY | 2.A–2.E | ch02 |
| PROTECT | 3.A–3.S | ch03 |
| DETECT | 4.A–4.B | ch04 |
| RESPOND | 5.A–5.B | ch04 |
| RECOVER | 6.A | ch04 |
| IT/OT how-to | — | ch05 |

## Quick goal anchors
| Need | Goal |
|------|------|
| Cyber roles/authorities | 1.A |
| IR plan maintained | 1.C |
| Supplier incident/vuln notice | 1.D |
| MSP risk | 1.E |
| Asset inventory | 2.A/2.B |
| Topology docs | 2.E |
| Default passwords gone | 3.A |
| MFA | 3.F |
| Separate admin accounts | 3.G/3.H |
| Segmentation | 3.I |
| Backups + restore | 3.O |
| Logs retained | 3.Q |
| Internet-facing hardened | 3.S |
| Malware detection | 4.A |
| Incident comms/reporting | 5.A/5.B |
| Recovery execution | 6.A |

## Tells & smells
| Smell | Likely gap |
|-------|------------|
| Shared plant passwords on HMIs | 3.A/3.C/3.G |
| VPN without MFA | 3.F |
| Flat IT–OT network | 3.I |
| Backups never restored | 3.O / 6.A |
| Three-day log retention | 3.Q |
| No one owns cyber outcomes | 1.A |
| MSSP can jump in with shared root | 1.E |
| Tracker still says “CPG 2.W” | 1.x remap missing |

## What this pack is not
- Not a full CSF 2.0 reference (see nist-csf)
- Not sector SSG detail
- Not CSET user documentation
- Not legal advice on mandatory reporting
