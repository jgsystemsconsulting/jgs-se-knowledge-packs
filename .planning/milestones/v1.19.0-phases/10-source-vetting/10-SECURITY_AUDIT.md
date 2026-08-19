# Phase 10 Security Audit — Source Vetting (v1.19 register)

**Phase:** 10 — source-vetting (plans 10-01, 10-02)
**Scope:** docs-only integrity register + planning-surface annotations. Files: `docs/SOURCE-VETTING.md`, `.planning/REQUIREMENTS.md`, `.planning/STATE.md`, `.planning/ROADMAP.md`, `10-01-SUMMARY.md`, `10-02-SUMMARY.md`. Research store (URL-allowed): `10-RESEARCH.md`. Content range: `44f777f..84889f3` (10-01 register + 10-02 annotations + SUMMARYs).
**Auditor method:** adversarial verification per declared disposition; every mitigation assumed absent until grep/read proved presence at the correct boundary. No implementation files modified. Not a pack-build security audit (no `packs/` created this phase).
**Date:** 2026-08-17 (audit) — evidence rows stamped 2026-08-17 per research date convention.
**WINDOWS.md:** not present. Tautology N/A.

**Verdict:** SECURED

**Threats Closed:** 7/7 declared (T-10-01, T-10-02, T-10-03, T-10-04, T-10-05, T-10-06, T-10-07) | **threats_open:** 0
**ASVS depth applied:** L2 (mitigation verified present AND placed at the correct trust boundary: research-store → published docs for URLs; unreachable/AAF → not Vetted Tier 1; checkboxes remain execute-unticked).

---

## 1. Declared threat register (from 10-01-PLAN.md + 10-02-PLAN.md `<threat_model>`)

| Threat ID | Category | Severity | Disposition | Evidence found | Status |
|-----------|----------|----------|-------------|----------------|--------|
| T-10-01 | Information Disclosure (Link Policy: source URLs leaking into published docs) | high | mitigate | `grep -c "http" docs/SOURCE-VETTING.md` = 0 (exit 1 / no matches). Extended scan for `://`, `www.`, `mailto:`, `\bhttps?\b` = 0. Extended planning-surface scan: `grep -c http` on `.planning/REQUIREMENTS.md`, `.planning/STATE.md`, `.planning/ROADMAP.md` = 0 each; no `https?://` / `www.` / `ftp://` / `file://`. URLs live only in `10-RESEARCH.md` (`grep -c http` = 24; live locators at e.g. asafm.army.mil PDF, esd.whs.mil / media.defense.gov DoDM paths, standards.nasa.gov 8719.14C, gps.gov IS-GPS-200N, ntrs.nasa.gov SP-7084, aaf.dau.edu / dau.edu guidebook paths). Pointer paragraph names the store only (`SOURCE-VETTING.md:144-146` → `` `.planning/phases/10-source-vetting/10-RESEARCH.md` ``). Boundary held: research-store → docs. | CLOSED |
| T-10-02 | Spoofing / Tampering (unreachable PDFs labelled Tier 1) | high | mitigate | v1.19 Vetted table (`SOURCE-VETTING.md:150-154`) contains only NASA-STD-8719.14C, IS-GPS-200N, NASA SP-7084 — none of Army CBA / DoDM 5000.102 / AAF. FUT-04 is **DEFERRED** with 403/503, "Not Tier 1" (`:158`). DoDM is **UNVERIFIED / deferred-excluded**, "Unreachable is not Tier 1" (`:164-166`). AAF is **NOT yet vetted — do not use** (`:162`, Excluded-pending `:87`, DAG retry `:85`). GP-06 rewritten to `Tier 1 (A-94)` only; Army CBA "not Tier 1" / "Do not treat this row as a dual-source build-clear" (`:136`). Phase 11 handoff: three NO-GO cells (`:175-177`). | CLOSED |
| T-10-03 | Elevation of privilege (build before clear) | high | mitigate | `files_modified` for 10-01 is SOURCE-VETTING only; for 10-02 is REQUIREMENTS / STATE / ROADMAP. `git diff --name-only -- packs/` empty now. Commits `44f777f`, `02fab79`, `5d97eca`, `b9e1160` touch only those docs/planning files. No `packs/` path in the Phase 10 range (`f80e9f3..84889f3`). Handoff table forbids Army CBA pack, `dodm-5000-102`, and any AAF pack (`:175-177`). | CLOSED |
| T-10-04 | Spoofing (AAF copyright footer treated as grant) | high | mitigate | DAG row keeps Phase 6 "NOT yet vetted" and appends "v1.19 retry still NOT yet vetted — do not use (no guidebook PDF opened; 2022 site copyright footer is not a redistribution grant)" (`:85`). Excluded-pending row quotes the © 2022 footer as *not* a redistribution grant (`:87`). Not-cleared bullet + handoff NO-GO (`:162`, `:177`). REQUIREMENTS VET-19-03 / IO-05 / IO-06: "still NOT yet vetted — do not use" / "not cleared — record deferred. No AAF pack." No AAF pack task executed. | CLOSED |
| T-10-05 | Repudiation (undated / untraceable verdicts) | medium | mitigate | New/updated rows carry Verified / Recorded / Reconfirmed 2026-08-17. `grep -c "2026-08-17" docs/SOURCE-VETTING.md` = 11. Dated stamps: AAF Excluded-pending (`:87`), v1.18 SP-7084 reconfirm (`:130`), GP-06 Army CBA retry (`:136`), 8719.14C (`:152`), IS-GPS-200N (`:153`), SP-7084 RECONFIRMED (`:154`), FUT-04 (`:158`), AAF unused (`:162`), DoDM subsection (`:166`). Each traces to a 10-RESEARCH.md § that was read back: §NASA-STD-8719.14 (Tier 1 leaning, Internet Public + title page), §GPS (DIST-A on IS-GPS-200N; no public IS-300), §NASA SP-7084 (NTRS reconfirm), FUT-04 (403/503), §DoDM 5000.102 (403/502, no PDF), §AAF (footer ≠ grant). Pointer at `:145`. STATE deviations bullet names 10-RESEARCH.md as the URL store (`STATE.md:58`). | CLOSED |
| T-10-06 | Tampering / process bypass (REQUIREMENTS checkboxes silently ticked) | high | mitigate | All four VET-19 lines remain `- [ ]`. `grep -nE "^- \[x\] \*\*VET-19" .planning/REQUIREMENTS.md` = none. Each VET-19 line carries `Phase 10 (2026-08-17)` parenthetical matching 10-RESEARCH / 10-01 (retry failed; dated tiers; unused; Excluded-pending). IO-01..07 also stay unchecked. Verify, not execute, owns the tick. | CLOSED |
| T-10-07 | Spoofing (IO annotations claiming AAF / Army / DoDM cleared) | high | mitigate | IO-01: "Army CBA is NO-GO; take the remap… Do not invent a CBA pack." IO-02: "`dodm-5000-102` is NO-GO". IO-03/04 GO only on 8719.14C / IS-GPS-200N. IO-05/06: AAF "not cleared — record deferred. No AAF pack." IO-07: "no new source cleared". STATE `:58` GO / NO-GO names match the handoff table. ROADMAP Phase 11 Goal: "consumes Phase 10: build 8719.14C + IS-GPS-200N; remap/defer Army CBA, DoDM 5000.102, AAF". No annotation claims an uncleared source is cleared. | CLOSED |

## 2. Audit-brief checks (licence register as security property)

### 2a. No unreachable / unused candidate greenlit as Tier 1

v1.19 Vetted table (three rows) read back against `10-RESEARCH.md` decision table (`:326-333`).

| Row | Licence basis claimed | Research backing | Assessment |
|---|---|---|---|
| NASA-STD-8719.14C | 17 U.S.C. § 105 + NTSS "Internet Public" + in-PDF title page; no © / ARR in text layer | §NASA-STD-8719.14: official record + PDF HTTP 200; title-page quote | Sound; Phase 11 third-party scan still required (row records it) |
| GPS IS-GPS-200N | In-PDF DIST-A; public list has 200N/705J/800J — no IS-300 | §GPS: PDF HTTP 200; DIST-A quoted; IS-300 naming error recorded | Sound; SAIC contractor watch-item + DIST-A confirm at build recorded |
| NASA SP-7084 | NTRS "Work of the US Gov. Public Use Permitted"; Distribution Limits Public | §NASA SP-7084: NTRS + PDF HTTP 200; already v1.18 Tier 1 | Sound; RECONFIRMED, not a new clearance |

Army CBA, DoDM 5000.102, and AAF do **not** appear as Vetted Source cells. GP-06 is A-94-only (Tier 1 for A-94, already built); Army CBA half is explicitly not a build-clear. Statute-prediction is labelled prediction on FUT-04 (`:158`). No OMG-style pseudo-open, no NC/ND, no paywalled source greenlit this phase.

### 2b. AAF unused; Army CBA / DoDM not hard-Excluded

AAF remains unused on four surfaces: DAG retry (`:85`), new Excluded-pending row (`:87`), Not-cleared bullet (`:162`), handoff NO-GO (`:177`). Copyright footer is cited as the *reason not to clear*, not as a grant. Army CBA and DoDM are deferred / UNVERIFIED, not new `| **US Army` / `| **DoDM` Excluded-table Source cells (VET-19-04: Excluded-pending for AAF only). Matches 10-RESEARCH preference: reachability defect ≠ hard kill.

### 2c. Link Policy — 0 URLs in SOURCE-VETTING.md (and planning annotations)

Verified: zero `http`/`https` strings, zero `://`, zero `www.`, zero `mailto:` in `docs/SOURCE-VETTING.md`. Same zero on REQUIREMENTS / STATE / ROADMAP. Source URLs exist only in `10-RESEARCH.md` (private research store). "Internet Public" and `17 U.S.C. § 105` are allowed non-URL strings and did not trip the gate. See Note N1 for an in-policy hostname observation.

### 2d. Prompt injection in new rows

Scanned SOURCE-VETTING plus the three planning files for injection payloads: "ignore previous/all/prior/above", "disregard", "forget your instructions", "system prompt", "you are now", "act as an AI/agent", role tags (`<system>`, `<|im_start|>`) — zero matches. This repo's docs are consumed as LLM context (knowledge packs), so the check is material — it passes.

### 2e. Secrets / PII in Phase 10 surfaces

Scanned SOURCE-VETTING + REQUIREMENTS + STATE + ROADMAP for `AKIA…`, `sk-…`, `ghp_/gho_/github_pat_`, `xox[bpars]-`, `AIza…`, `BEGIN PRIVATE KEY`, `password=/token=/api_key/Bearer` — zero matches. Pre-existing `permission@sei.cmu.edu` is the published SEI routing address (Phase 6, not new). "Mary K. McCaskill, NASA Langley" is published-author attribution (not PII). No secrets added this phase.

### 2f. Not a pack-build audit

No `extract.py` / catalog / `vet_source.py` run required or observed. No new pack tree. Phase 11 still owes in-source confirmation on copies actually extracted (8719.14C third-party scan; IS-GPS-200N DIST-A on the extracted file). That is a forward obligation, not an open Phase 10 threat.

## 3. SUMMARY.md `## Threat Flags` mapping

Neither `10-01-SUMMARY.md` nor `10-02-SUMMARY.md` has a `## Threat Flags` section. 10-01 deviations ledger records only a verify-command false-fail (`grep -c 'GO —'` also matches `NO-GO —`); no new attack surface. 10-02 deviations: None. No unregistered flags.

## 4. Notes (informational — no open threats, no action required this phase)

- **N1 — Bare hostnames in vetting rationale (in-policy).** New this phase: `gps.gov` inside the IS-GPS-200N evidence cell (`SOURCE-VETTING.md:153`). Pre-existing: `ecss.nl`, `permission@sei.cmu.edu`, `dote.osd.mil`, `swehb.nasa.gov`. These are not URLs (no scheme/path) and not hyperlinks. Declared gate ("zero http strings") passes exactly. Recorded for the next Link Policy review, not a violation.
- **N2 — DoDM pointer bullet is undated; the subsection is dated.** Plan-prescribed Block 1 bullet for DoDM (`:160`) has no Verified/Recorded stamp; Block 2 heading + body (`:164-166`) carries `(Recorded 2026-08-17.)`. T-10-05's "every new row/note" is satisfied by the authoritative subsection the pointer names.
- **N3 — Forward boundary.** T-10-02 / T-10-03 mitigations for this phase are *recording* (NO-GO / not Tier 1 / no packs/). Enforcement (do not build Army CBA / DoDM / AAF; confirm DIST-A and third-party inserts on GO copies) is Phase 11 pack validation. Phase 11's security pass must verify that enforcement, or those threats re-open there.

## 5. Scope discipline

- Implementation files read-only: audit touched no app/pack/doc source except this artifact.
- No `packs/` or `sources/` paths in the Phase 10 execute commits — no pack builds started, as planned.
- Planning diffs (REQUIREMENTS annotations with boxes still open, STATE deviations bullet, ROADMAP Plans + consumes-vetting clause) match 10-02 tasks; no undisclosed content changes found.
- Unclassified coverage probes left unresolved (not auto-resolved).

**Verdict:** SECURED — all 7 declared threats CLOSED at declared boundaries; audit-brief checks pass; threats_open = 0.
