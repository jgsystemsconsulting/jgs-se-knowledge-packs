# Cheatsheet — NIST SP 800-61 Rev. 3

## Decision rules
1. **Need tactical packet-level how-to?** Use live playbooks/CPRT/sector guides — not r3 as an encyclopedia.
2. **Need IR integrated with enterprise cyber risk?** Start with the CSF life-cycle model + Community Profile.
3. **Still on r2 phases?** Use Table 1 mapping, then retire pure circular thinking for continuous improvement.
4. **Who acts?** Confirm policy authorities before incident actions that disconnect or shut down assets.
5. **Prep or respond row?** Table 2 = preparation/lessons; Table 3 = DE/RS/RC execution.
6. **Priority Low on Table 2?** Still implement if mission/law requires — Low means “not unique to active IR.”
7. **Lesson identified mid-incident?** Feed ID.IM now; do not wait for final recovery report.
8. **Restore complete?** Only after integrity checks and recovery declaration criteria — not merely “ping succeeds.”

## Life-cycle quick map
| Need | Functions | Chapter |
|------|-----------|---------|
| Strategy, policy, appetite | GV | ch02, ch04 |
| Assets, risk, improvement | ID (+ID.IM) | ch02, ch04, ch06 |
| Safeguards, reduce blast radius | PR | ch04 |
| Find/analyze/declare | DE | ch05 |
| Manage/contain/eradicate/notify | RS | ch05 |
| Restore/verify/communicate | RC | ch05 |

## Profile annotation keys
| Tag | Meaning |
|-----|---------|
| R | Recommendation — should do |
| C | Consideration — should consider |
| N | Note — supporting info |
| H/M/L | IR-relative priority starting point |

## Tells & smells
| Smell | Likely gap |
|-------|------------|
| IR run entirely inside SOC tickets | Missing multi-role model (ch03) |
| No one sure who can isolate a plant network | Policy authorities missing |
| Postmortems only; detections never change | ID.IM pipeline broken |
| MSSP contract lacks surge IR terms | External coordination pack missing |
| r2 binder still treated as current law | Supersession not socialized (ch01) |
| Restore from last night’s backup untested | RC integrity gate missing |
| Public tweets before legal review | RS.CO/RC.CO plan missing |
| Tabletop once a year, no playbooks | Procedures not executable |

## What this pack is not
- Not a packet forensics manual
- Not legal advice on breach notification statutes
- Not the full CSF 2.0 reference (see nist-csf)
- Not SP 800-61r2 resurrected
