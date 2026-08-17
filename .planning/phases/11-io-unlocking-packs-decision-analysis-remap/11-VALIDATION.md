---
phase: 11
slug: io-unlocking-packs-decision-analysis-remap
status: draft
nyquist_compliant: false
wave_0_complete: false
created: 2026-08-17
---

# Phase 11 — Validation Strategy

> Pack construction + honest deferral. No runtime. "Done" is GO packs gated + NO-GO recorded.

---

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | repo tooling (`validate_pack.py`, overlap/scan scripts) |
| **Config file** | none — Wave 0 not applicable |
| **Quick run command** | `python tooling/validate_pack.py packs/<slug>` |
| **Full suite command** | `python tooling/validate_pack.py packs/nasa-std-8719-14; python tooling/validate_pack.py packs/is-gps-200n; python tooling/validate_pack.py packs/dod-vva-rpg` |
| **Estimated runtime** | ~30 seconds |

---

## Sampling Rate

- **After every pack commit:** `python tooling/validate_pack.py packs/<slug>`
- **After every plan wave:** Link Policy (`grep -c http docs/SOURCE-VETTING.md` = 0) + no `sources/` in `git show --name-only`
- **Before `/gsd:verify-work`:** all built packs gated; IO-05/06/07 recorded deferred/accept; map JSON untouched
- **Max feedback latency:** 30 seconds

---

## Per-Task Verification Map

| Task ID | Plan | Wave | Requirement | Threat Ref | Secure Behavior | Test Type | Automated Command | File Exists | Status |
|---------|------|------|-------------|------------|-----------------|-----------|-------------------|-------------|--------|
| 11-01-01 | 01 | 1 | IO-03 | T-11-01 | nasa-std-8719-14 gated; no URL leak | tooling | `python tooling/validate_pack.py packs/nasa-std-8719-14` | ❌ W0 | ⬜ pending |
| 11-01-02 | 01 | 1 | IO-04 | T-11-02 | is-gps-200n exemplar gated; DIST-A in notes | tooling | `python tooling/validate_pack.py packs/is-gps-200n` | ❌ W0 | ⬜ pending |
| 11-02-01 | 02 | 2 | IO-02 | — | dod-vva-rpg chapter count > 10; no dodm-5000-102 | tooling | `python tooling/validate_pack.py packs/dod-vva-rpg` | ✅ | ⬜ pending |
| 11-02-02 | 02 | 2 | IO-01 | — | remap table exists; no map JSON edit | docs | `git diff --name-only -- docs/capability-pack-map.json` empty | ✅ | ⬜ pending |
| 11-02-03 | 02 | 2 | IO-05, IO-06, IO-07 | T-11-03 | deferred/accept recorded; no aaf/stakeholder pack | docs | no `packs/aaf-*`; REQUIREMENTS parentheticals dated | ✅ | ⬜ pending |

*Status: ⬜ pending · ✅ green · ❌ red · ⚠️ flaky*

---

## Wave 0 Requirements

Existing infrastructure covers validation. New pack dirs appear during execute.

- `tooling/validate_pack.py`
- Phase 7 scan/overlap commands from 11-RESEARCH Standard Stack
- Link Policy: `grep -c http docs/SOURCE-VETTING.md` = 0

---

## Manual-Only Verifications

| Behavior | Requirement | Why Manual | Test Instructions |
|----------|-------------|------------|-------------------|
| Third-party insert scan on 8719.14C | IO-03 | PDF judgement | P11-PRE-1 quote in PACK.yaml notes |
| DIST-A on extracted IS-GPS-200N | IO-04 | PDF cover | P11-PRE-2 quote in PACK.yaml notes |
| Remap table is apply-ready for Phase 12 | IO-01 | judgement | SUMMARY names ≥1 federal-bca and/or dod-vva-rpg chapter → cluster 16 |

---

## Validation Sign-Off

- [ ] All tasks have `<automated>` verify or Wave 0 dependencies
- [ ] Sampling continuity: no 3 consecutive tasks without automated verify
- [ ] Wave 0 covers all MISSING references
- [ ] No watch-mode flags
- [ ] Feedback latency < 30s
- [ ] `nyquist_compliant: true` set in frontmatter

**Approval:** pending
