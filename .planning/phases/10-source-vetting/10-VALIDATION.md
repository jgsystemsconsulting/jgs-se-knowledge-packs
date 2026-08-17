---
phase: 10
slug: source-vetting
# status lifecycle: draft (seeded by plan-phase) → validated (set by validate-phase §6)
# audit-milestone §5.5 distinguishes NOT-VALIDATED (draft) from PARTIAL (validated + nyquist_compliant: false) (#2117)
status: draft
nyquist_compliant: false
wave_0_complete: false
created: 2026-08-17
---

# Phase 10 — Validation Strategy

> Per-phase validation contract for feedback sampling during execution.
> Phase 10 is documentation/vetting only (no runtime, no pack gate). "Done" is a closed decision set plus Link Policy.

---

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | none — docs/planning integrity checks (grep + git) |
| **Config file** | none — Wave 0 not applicable |
| **Quick run command** | `grep -c http docs/SOURCE-VETTING.md` (must print `0`) |
| **Full suite command** | `grep -c http docs/SOURCE-VETTING.md; git diff --name-only -- packs/` (no pack paths) |
| **Estimated runtime** | ~2 seconds |

---

## Sampling Rate

- **After every task commit:** Run `grep -c http docs/SOURCE-VETTING.md` (expect `0`)
- **After every plan wave:** Confirm no `packs/` paths in `git diff --name-only` vs plan start
- **Before `/gsd:verify-work`:** Link Policy + VET-19-01..04 each have a dated decision
- **Max feedback latency:** 5 seconds

---

## Per-Task Verification Map

| Task ID | Plan | Wave | Requirement | Threat Ref | Secure Behavior | Test Type | Automated Command | File Exists | Status |
|---------|------|------|-------------|------------|-----------------|-----------|-------------------|-------------|--------|
| 10-01-01 | 01 | 1 | VET-19-01 | — | Army CBA decided (Tier 1 with in-source quote OR deferred/excluded with dated 403/503 evidence) | docs | REQUIREMENTS/STATE/SOURCE-VETTING contain 2026-08-17 (or execute-day) FUT-04 sentence | ✅ | ⬜ pending |
| 10-01-02 | 01 | 1 | VET-19-02 | — | DoDM 5000.102, NASA-STD-8719.14, GPS ICD select, NASA SP-7084 each dated Tier 1/2/Excluded/deferred | docs | SOURCE-VETTING v1.19 section names all four | ✅ | ⬜ pending |
| 10-01-03 | 01 | 1 | VET-19-03 | — | AAF still "NOT yet vetted — do not use" OR new Tier 1/2 row with in-source quote | docs | SOURCE-VETTING contains AAF unused sentence | ✅ | ⬜ pending |
| 10-01-04 | 01 | 1 | VET-19-04 | T-10-01 | Ruled-out sources in Excluded table; zero URLs | docs | `grep -c http docs/SOURCE-VETTING.md` → `0` | ✅ | ⬜ pending |

*Status: ⬜ pending · ✅ green · ❌ red · ⚠️ flaky*

---

## Wave 0 Requirements

Existing infrastructure covers all phase requirements. No test framework install. Integrity signals:

- `docs/SOURCE-VETTING.md` — published register (Link Policy: no URLs)
- `.planning/phases/10-source-vetting/10-RESEARCH.md` — private URL/quote store
- `git diff --name-only -- packs/` — must stay empty this phase

---

## Manual-Only Verifications

| Behavior | Requirement | Why Manual | Test Instructions |
|----------|-------------|------------|-------------------|
| In-source licence quote is real | VET-19-02 cleared rows | PDF/metadata judgement, not a unit test | Confirm 10-RESEARCH.md quotes match the SOURCE-VETTING rationale (no URL copied into docs/) |
| Unreachable ≠ Tier 1 | VET-19-01 / DoDM / AAF | Human classification | If PDF was not opened, row must be deferred/excluded/pending — not Vetted |

---

## Validation Sign-Off

- [ ] All tasks have `<automated>` verify or Wave 0 dependencies
- [ ] Sampling continuity: no 3 consecutive tasks without automated verify
- [ ] Wave 0 covers all MISSING references
- [ ] No watch-mode flags
- [ ] Feedback latency < 5s
- [ ] `nyquist_compliant: true` set in frontmatter

**Approval:** pending
