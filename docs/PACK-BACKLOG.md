<!--
Copyright (c) 2026 JG Systems Consulting Ltd. — MIT License (see ../LICENSE).
SPDX-License-Identifier: MIT
-->

# Pack Backlog & Source Ledger

Status of every candidate source considered for the catalogue. Source-material download URLs
are **not** published here (link policy — see [LICENSING.md](LICENSING.md)); they live in the
maintainers' build notes. Each candidate has a terminal status so nothing is silently dropped.

## ✅ Built / shipped

| Pack | Source | Tier | Status |
|------|--------|------|--------|
| `sebok` | Guide to the SE Body of Knowledge v2.13 | 2 (CC BY-NC-SA) | shipped |
| `nasa-se-handbook` | NASA Systems Engineering Handbook (SP-2016-6105 Rev 2) | 1 (US-gov PD) | shipped |

## 🟢 Confirmed Tier 1/2 — queued for v1.1

| Pack | Source | Tier | Notes |
|------|--------|------|-------|
| `nasa-npr-7123` | NASA NPR 7123.1D — SE Processes and Requirements | 1 | NODIS, public |
| `nasa-risk` | NASA/SP-2011-3422 — Risk Management Handbook | 1 | NTRS, title verified |
| `nasa-system-safety` | NASA/SP-2014-612 — System Safety Handbook (Vol 2; Vol 1 = SP-2010-580) | 1 | NTRS, title verified |
| `nasa-hsi` | NASA/SP-2015-3709 — Human Systems Integration Practitioner's Guide | 1 | NTRS, title verified |
| `nist-ai-rmf` | NIST AI 100-1 — AI Risk Management Framework 1.0 | 1 | via GovInfo (nvlpubs 404); 🎯 thesis-relevant |
| `nist-ssdf` | NIST SP 800-218 — Secure Software Development Framework | 1 | NIST PD |
| `nist-csf` | NIST CSF 2.0 (CSWP 29) | 1 | NIST PD |
| `mil-std-882` | MIL-STD-882E — DoD System Safety | 1 | DoD, Distribution A (public release) |
| `eu-ai-act` → **built v1.2.0** | Regulation (EU) 2024/1689 — Artificial Intelligence Act | 2 | EU OJ, freely reproducible with acknowledgement. **Built in v1.2.0** from a user-supplied PDF (EUR-Lex WAF blocked automated download). Now live. |
| `requirements-writing` | EARS patterns (openly published) + requirement quality characteristics grounded in NASA PD | 2 / guidance | **guidance pack** — bespoke multi-source synthesis, not single-PDF |

## ⏸ Deferred

| Candidate | Source | Reason |
|-----------|--------|--------|
| `nasa-expanded-guidance` | NASA Expanded Guidance for SE (SP-2016-6105-SUPPL, multi-vol) | Auto-found URL collided with the SE Handbook; likely redundant with `nasa-se-handbook`. Needs correct SUPPL link + a redundancy check before building. |
| ~~`dodaf`~~ → **built v1.2.0** | DoD Architecture Framework 2.02 Vol II | Was deferred (official server 403'd automated download); **built in v1.2.0 from a user-supplied, title-verified PDF**. Now live. |

## 🔴 Excluded — not packageable

| Source | Why |
|--------|-----|
| **OMG formal specs** (UML, SysML, BPMN, UAF, CORBA, MOF, XMI, OCL, DDS…) | OMG Specification License public grant is informational-use-only: no network posting, no commercial transfer, no modification. Two independent licence reads (2026-06-19). `omg-sysml` was shipped in error in v1.0.0 and has been pulled. |
| **NAF** (NATO Architecture Framework v4.1) | NATO "all rights reserved"; no open/CC redistribution grant. |
| **DAU Defense Acquisition Guidebook** | Retired; replacement is web-only HTML across many pages, no clean single PDF. |
| ISO/IEC/IEEE, INCOSE SE Handbook, SWEBOK, MITRE SE Guide, TOGAF/ArchiMate, PMBOK, INCOSE SE Vision 2035 | See [SOURCE-VETTING.md](SOURCE-VETTING.md). |

## Lesson recorded

License classification MUST be done by reading the **actual public grant clause** of the
source, not a web-search summary. The OMG case (a search summary surfaced the permissive
company→OMG grant, masking the restrictive public grant) is why Phase-0 source confirmation
now content-verifies the licence text directly before any build.
