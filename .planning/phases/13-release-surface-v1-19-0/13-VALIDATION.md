---
phase: 13
slug: release-surface-v1-19-0
status: draft
nyquist_compliant: false
wave_0_complete: false
created: 2026-08-17
---

# Phase 13 — Validation Strategy

> Docs + two stdlib gates + public git/GitHub metadata. No runtime.

---

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | `tooling/check_release.py`, `tooling/check_capability_map.py`, `gh` |
| **Config file** | none |
| **Quick run command** | `python tooling/check_release.py` |
| **Full suite command** | `python tooling/check_capability_map.py; python tooling/check_release.py` |
| **Estimated runtime** | ~20 seconds (plus network for tag/release verify) |

---

## Sampling Rate

- **After version/catalog/README edits:** both gates PASS
- **Immediately before release commit:** re-run `check_release.py`
- **After tag + gh release:** `git cat-file -t v1.19.0` == tag; `gh release view v1.19.0`
- **Max feedback latency:** 20 seconds (local); ~60s for remote verify

---

## Per-Task Verification Map

| Task ID | Plan | Wave | Requirement | Test Type | Automated Command | Status |
|---------|------|------|-------------|-----------|-------------------|--------|
| 13-01-01 | 01 | 1 | REL-19-01 | tooling | `python tooling/check_release.py` | ⬜ pending |
| 13-01-02 | 01 | 1 | REL-19-01 | docs | catalog RPG chapters=13; README new slugs | ⬜ pending |
| 13-01-03 | 01 | 1 | REL-19-02 | git/gh | annotated tag + `gh release view v1.19.0` | ⬜ pending |

---

## Wave 0 Requirements

Existing gates cover local verification. `gh` CLI required for REL-19-02.

---

## Manual-Only Verifications

| Behavior | Requirement | Why Manual | Test Instructions |
|----------|-------------|------------|-------------------|
| CHANGELOG reads as competency IO-unlocks | REL-19-02 | judgment | IO-01..07 named; not slug-only |
| GitHub Release notes match CHANGELOG body | REL-19-02 | remote | `gh release view v1.19.0` |

---

## Validation Sign-Off

- [ ] All tasks have automated verify
- [ ] Feedback latency < 20s local
- [ ] `nyquist_compliant: true` set in frontmatter

**Approval:** pending
