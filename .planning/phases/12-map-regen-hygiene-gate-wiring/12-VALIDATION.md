---
phase: 12
slug: map-regen-hygiene-gate-wiring
status: draft
nyquist_compliant: false
wave_0_complete: false
created: 2026-08-17
---

# Phase 12 — Validation Strategy

> Docs + two stdlib gates. No runtime.

---

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | `tooling/check_capability_map.py`, `tooling/check_release.py` |
| **Config file** | none |
| **Quick run command** | `python tooling/check_capability_map.py` |
| **Full suite command** | `python tooling/check_capability_map.py; python tooling/check_release.py` |
| **Estimated runtime** | ~15 seconds |

---

## Sampling Rate

- **After map commit:** `python tooling/check_capability_map.py`
- **After wire + hygiene:** `python tooling/check_release.py` (must include map)
- **Before verify:** both gates PASS; plugin/CHANGELOG still 1.18.0
- **Max feedback latency:** 15 seconds

---

## Per-Task Verification Map

| Task ID | Plan | Wave | Requirement | Test Type | Automated Command | Status |
|---------|------|------|-------------|-----------|-------------------|--------|
| 12-01-01 | 01 | 1 | MAP-19-01/02/03 | tooling | `python tooling/check_capability_map.py` | ⬜ pending |
| 12-01-02 | 01 | 1 | MAP-19-05 | docs | grep CONTRACT 628/502/Cybersecurity/Digital Engineering | ⬜ pending |
| 12-02-01 | 02 | 2 | MAP-19-04 | tooling | `rg check_capability_map tooling/check_release.py`; `check_release.py` PASS | ⬜ pending |
| 12-02-02 | 02 | 2 | HYG-01..04 | docs | no CHANGELOG BOM; `.gitattributes`; topic-index greps; PACK.yaml (c) | ⬜ pending |

---

## Wave 0 Requirements

Existing gates cover all phase requirements. No new test framework.

---

## Manual-Only Verifications

| Behavior | Requirement | Why Manual | Test Instructions |
|----------|-------------|------------|-------------------|
| New-pack cluster assignment vs When-to-use | MAP-19-01 | agent judgment | Spot-check SKILL.md vs assigned clusters |
| Remap rows applied (not copied) | MAP-19-03 | membership | DA has the three named chapters; old clusters do not |

---

## Validation Sign-Off

- [ ] All tasks have automated verify
- [ ] Feedback latency < 15s
- [ ] `nyquist_compliant: true` set in frontmatter

**Approval:** pending
