# Phase 6 Security Audit — Source Vetting / UNVERIFIED Resolution

**Phase:** 6 — source-vetting-unverified-resolution (plan 6-01)
**Scope:** vetting-register commits `c1dfcf0..6a503ae` (content scan over `e1e6231..6a503ae` so the base commit `c1dfcf0` — the 8 Vetted rows — is included). Files: `docs/SOURCE-VETTING.md`, `.planning/REQUIREMENTS.md`, `.planning/ROADMAP.md`, `.planning/MILESTONES.md`, `.planning/STATE.md`, `6-01-SUMMARY.md`.
**Auditor method:** adversarial verification per declared disposition; every mitigation assumed absent until grep/read proved presence at the correct boundary. No implementation files modified.
**Date:** 2026-08-14 (audit) — evidence rows stamped 2026-08-14 per research date convention.

**Verdict:** SECURED_WITH_NOTES

**Threats Closed:** 3/3 declared (T-6-01, T-6-02, T-6-03) | **threats_open:** 0
**ASVS depth applied:** L2 (mitigation verified present AND placed at the correct trust boundary: research-store → docs for URLs; vetted-row → Phase 7 build for caveats).

---

## 1. Declared threat register (from 6-01-PLAN.md `<threat_model>`)

| Threat ID | Category | Severity | Disposition | Evidence found | Status |
|-----------|----------|----------|-------------|----------------|--------|
| T-6-01 | Information Disclosure (Link Policy: source URLs leaking into published docs) | medium | mitigate | `grep -c "http" docs/SOURCE-VETTING.md` = 0; extended scan for `://`, `www.`, `mailto`, `\bhttps?\b` = 0 matches. URLs live only in `6-RESEARCH.md` (verified: full URLs present there, lines 22, 41-43, 55-62, 76-86, 116-119, 129-136, 143, 159-175, 184-189); the v1.18 section carries the Link Policy pointer paragraph (SOURCE-VETTING.md:117-119). Boundary held: research-store → docs. | CLOSED |
| T-6-02 | Repudiation (undated / untraceable verdicts) | low | mitigate | All 11 new rows dated `(Verified 2026-08-14.)` — file total 18 stamps (7 pre-phase + 11 new), matching plan expectation. Each new row traces to a 6-RESEARCH.md § that was read back and matches: §1a (40051-2C scanned-image DIST-A caveat), §1b (SP-7084 NTRS "Work of the US Gov. Public Use Permitted"), §1c (VV&A chapter-wise rescope), §1d (881F QuickSearch/GovTribe, everyspec=881E-only), §2a (FAA-STD-025 rev E canonical/rev F mirror), §2b (DOT&E 8.02 + single-encoded afacpo fallback), §2c (DAFMAN releasability quote + MOTRC title), §1e/§3a/§3b (AFOTEC/DAG/SEI exclusions). GP-06 trace resolves via gap-report shortlist item 5 (`capability-gap-report.md:157` records Tier 1 for "OMB Circular A-94 (+ Army CBA Guide)"). | CLOSED |
| T-6-03 | Tampering (mirror-fetched PDFs, provenance swap at Phase 7 build) | high | mitigate | All three declared build caveats recorded verbatim in the vetted rows: 40051-2C "DIST-A must be visually confirmed on the cover at build" (SOURCE-VETTING.md:128), 881F "DIST-A visual confirm at build" (:131), VV&A "confirm DIST-A / authorship inside each chapter PDF used" (:130). Plus edition-recording requirements for GP-02 (:132) and GP-03 (:133) and the GP-08 deferral note (:137). Caveats also carried into REQUIREMENTS (GP-01 chapter-wise note, GP-03 8.02-conditional note). Declared boundary: enforcement lands in Phase 7 pack validation — recording (this phase's obligation) is complete. | CLOSED |

## 2. Audit-brief checks (licence compliance as security property)

### 2a. No non-redistributable content greenlit — 8 new Vetted rows vs 6-RESEARCH.md

All 8 rows read back against the research store. Every Tier-1 claim traces to evidence; none of the 8 sources appears on the Excluded list (checked token-by-token against the Excluded section; the only apparent hits — DOT&E, DAFMAN — are mentions inside the AFOTEC rationale citing them as live substitutes, not exclusions of those sources).

| Row | Licence basis claimed | Research backing | Assessment |
|---|---|---|---|
| GP-07 / MIL-STD-40051-2C | 17 U.S.C. § 105 + DIST-A on DLA ASSIST family records | §1a: PDF fetched (200, 37.7 MB, 1168 page objects), cover statement is scanned image, DLA ASSIST lists Distribution A | Sound; build caveat recorded |
| NASA SP-7084 | NTRS "Work of the US Gov. Public Use Permitted", Distribution Limits Public | §1b: NTRS record + PDF both HTTP 200, metadata quoted verbatim | Sound; cleanest of the eight |
| GP-01 / DoD VV&A RPG | 17 U.S.C. § 105, OUSW(R&E) DoD work | §1c: cto.mil index inspected; "consolidated PDF" premise corrected to chapter-wise | Sound; per-chapter in-PDF check required |
| GP-05 / MIL-STD-881F | 17 U.S.C. § 105, DoD standard | §1d: QuickSearch ident 36026 Active; everyspec 881E-only; GovTribe attachment | Sound; DIST-A confirm at build |
| GP-02 / FAA-STD-025 | 17 U.S.C. § 105, FAA US-gov work | §2a: ROSAP full-text PDF live, rev E 2002; mirror rev F | Sound; revision recorded in PACK.yaml |
| GP-03 / DOT&E Guidebook | 17 U.S.C. § 105, DOT&E | §2b: double-encoded mirror URL corrected; canonical lists Aug 2022 (8.02); single-encoded afacpo PDF 200 | Sound; edition recorded in PACK.yaml |
| GP-04 / DAFMAN 63-119 | In-document "no releasability restrictions" quote + 17 U.S.C. § 105 | §2c: full text retrieved, releasability statement quoted from the document itself | Sound; in-document evidence (strongest form) |
| GP-06 / federal-bca | 17 U.S.C. § 105 for both OMB Circular A-94 + US Army CBA Guide | Cited as "§2 spot-check scope + capability-gap-report shortlist item 5" — item 5 exists (`capability-gap-report.md:157`, "Tier 1, canonical whitehouse.gov / army.mil PDFs"); §2 itself did not re-verify these two documents | Sound (statute basis; both are US-federal works) — see Note N2 |

Statute-basis claims are correctly limited to US-federal-authored works; application of the repo's own Tier-1 rubric (SOURCE-VETTING.md §"Tier 1") is consistent with the v1.17 section's convention. No OMG-style pseudo-open, no NC/ND, no paywalled source greenlit.

### 2b. AFOTEC / DoD DAG / CMU SEI properly excluded

Three new Excluded rows present (SOURCE-VETTING.md:84-86), all dated, all rationale-accurate vs research: AFOTEC (§1e: DTIC maintenance shells, only hit is 1989 AD-A205 489, ~37 years stale vs live DAFMAN/DOT&E), DoD DAG (§3a: DAU "has been retired and replaced" verbatim, AFCAPO 2022-08-15 notice, dead canonical URLs), CMU SEI (§3b: © CMU, government-purpose-only reproduction carve-out, DIST-A correctly distinguished from copyright grant, permission@sei.cmu.edu routing). None of the three was greenlit anywhere in the range. GP-08 (NASA-HDBK-2203, wiki-only, no consolidated PDF) descoped rather than vetted — correct per §4.

### 2c. Link policy — 0 URLs in SOURCE-VETTING.md

Verified: zero `http`/`https` strings, zero `://`, zero `www.`, zero `mailto:`. The file passes the declared gate exactly. Source URLs exist only in `6-RESEARCH.md` (private research store, never docs/ or packs/), matching the declared trust boundary. See Note N1 for an in-policy observation.

### 2d. Prompt injection in new rows

Scanned the full range diff (`e1e6231..6a503ae`, 391 lines) for injection payloads: "ignore previous/all/prior/above", "disregard", "forget your instructions", "system prompt", "you are now", "act as an AI/agent", role tags (`<system>`, `<|im_start|>`), exfiltration phrasing — zero matches. Secondary scan hits for "agent"/"model"/"prompt" are the project's own "Agent-Enablement Surface" terminology and grep-command citations, not instructions addressed to an AI. Non-ASCII scan found only benign typography (progress-bar glyphs, arrows, en/em dashes, §). No hidden/bidi/zero-width characters. This repo's docs are consumed as LLM context (knowledge packs), so this check is material, not ceremonial — it passes.

### 2e. Secrets / PII in commits

Scanned the range diff for `AKIA…`, `sk-…`, `ghp_/gho_/github_pat_`, `xox[bpars]-`, `AIza…`, `BEGIN PRIVATE KEY`, `password=/token=/api_key/Bearer` — zero matches. PII scan: the only email is `permission@sei.cmu.edu` — a published institutional routing address explicitly permitted and required by plan Task 2 (bare form, no mailto). The only personal name is "Mary K. McCaskill, NASA Langley" — published-author attribution of a NASA handbook (attribution, not PII). Numeric hits were dates/timestamps. Commit author is a GitHub noreply address. No secrets, no PII.

## 3. SUMMARY.md `## Threat Flags` mapping

SUMMARY declares "None beyond plan threat model" and maps T-6-01/T-6-02/T-6-03 to their artifacts. All map to existing register IDs — informational, no unregistered flags.

## 4. Notes (informational — no open threats, no action required this phase)

- **N1 — Bare hostnames in vetting rationale (in-policy).** `dote.osd.mil`, `swehb.nasa.gov`, `everyspec`, `afacpo` appear as plain host/service names inside fetch-strategy text (SOURCE-VETTING.md:131, 133, 137; `ecss.nl` pre-existing at :81). These are not URLs (no scheme/path) and not hyperlinks; LICENSING.md §4 prohibits source-material *links* and the declared gate ("zero http strings") passes exactly. Mirror-source identifiability via hostname is inherent to tampering-mitigation rationale. Recorded for the next Link Policy review, not a violation.
- **N2 — GP-06 has the lightest evidence trail of the eight.** 6-RESEARCH.md did not itself re-verify OMB Circular A-94 or the US Army CBA Guide; the row leans on statute basis (17 U.S.C. § 105 — correct for both US-federal works), the gap-report shortlist ranking, and the section-wide Phase 7 in-source confirmation preamble. The row is transparent about this ("licence basis per … spot-check scope and capability-gap-report shortlist item 5"). Phase 7 build must apply the in-PDF/at-build confirmation to GP-06's two documents (the row records the PACK.yaml per-source provenance obligation). Watch-item, not a gap: T-6-02's declared mitigation (stamp + traceable reference) is satisfied.
- **N3 — Forward boundary.** T-6-03's declared mitigation for this phase is *recording* caveats (present, verbatim, in the exact rows Phase 7 builds will read); enforcement (DIST-A visual confirmation, per-chapter statement checks, edition recording in PACK.yaml) is explicitly deferred to Phase 7 pack validation. Phase 7's security pass must verify that enforcement, or T-6-03 re-opens there.

## 5. Scope discipline

- Implementation files read-only: audit touched no app/pack/doc source; only this artifact was written.
- No `packs/` or `sources/` paths in the range diff (verified) — no pack builds started in Phase 6, as planned.
- Planning diffs (REQUIREMENTS GP-08 strike + Out-of-Scope with NPR 7150.2 / NASA-STD-8739.8 alternatives, ROADMAP 7-pack alignment, MILESTONES, STATE deviation note) match the plan's tasks; no undisclosed content changes found in the range.

**Verdict:** SECURED_WITH_NOTES — all 3 declared threats CLOSED at declared boundaries; all 4 audit-brief checks pass; threats_open = 0.
