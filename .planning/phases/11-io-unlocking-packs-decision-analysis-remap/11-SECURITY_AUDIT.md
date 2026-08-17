# Phase 11 Security Audit — IO-unlocking packs + Decision Analysis remap spec

**Phase:** 11 — io-unlocking-packs-decision-analysis-remap (plans 11-01, 11-02)
**Scope:** pack-build + thin-register + honest IO records. Files: `packs/nasa-std-8719-14/**`, `packs/is-gps-200n/**`, new `packs/dod-vva-rpg` chapters (ch11–ch13) + PACK.yaml/SKILL.md, `packs/federal-bca/SKILL.md`, `.planning/REQUIREMENTS.md`, `.planning/STATE.md`, thin-register surfaces (`catalog.json`, `SKILLS.md`, `NOTICE`, `.cursor-plugin/plugin.json`, `docs/packs.html`, `README.md`). Content range: `1b3e4f4^..HEAD` (Wave A packs + Wave B extend/records/thin-register + SUMMARYs).
**Auditor method:** adversarial verification per declared disposition; every mitigation assumed absent until grep/read proved presence at the correct boundary. Implementation files not modified. Overlap re-run this audit (cheap; extracts still on disk, gitignored).
**Date:** 2026-08-17 (audit) — evidence rows stamped 2026-08-17 per research date convention.
**WINDOWS.md:** not present. Tautology N/A.
**MCP:** not used.

**Verdict:** SECURED

**Threats Closed:** 10/10 declared rows (T-11-01, T-11-02, T-11-03, T-11-04, T-11-05, T-11-06 IP, T-11-06 map, T-11-07 scope, T-11-07 tick, T-11-08) | **threats_open:** 0
**ASVS depth applied:** L2 (mitigation verified present AND placed at the correct trust boundary: extracted copy → PACK.yaml quotes; `sources/` → never committed; `.planning` URL store → published packs; remap table → not live map JSON; AAF unused → not a pack).

ID collisions across the two PLAN `<threat_model>` blocks are listed as separate rows (same ID, different component). Both registers authored at plan time.

---

## 1. Declared threat register (from 11-01-PLAN.md + 11-02-PLAN.md `<threat_model>`)

| Threat ID | Category | Severity | Disposition | Evidence found | Status |
|-----------|----------|----------|-------------|----------------|--------|
| T-11-01 | Information Disclosure (Link Policy) | high | mitigate | `grep -R -nE "https?://"` on `packs/nasa-std-8719-14`, `packs/is-gps-200n`, `packs/dod-vva-rpg`, `packs/federal-bca/SKILL.md` = no matches. Extended `www.` / `ftp://` / `mailto:` / `source_url` = 0. `grep -c http docs/SOURCE-VETTING.md` = 0; SOURCE-VETTING untouched this phase (`git log 1b3e4f4^..HEAD -- docs/SOURCE-VETTING.md` empty). New NOTICE `[pack: nasa-std-8719-14]` / `[pack: is-gps-200n]` blocks (NOTICE:704–721) have no URL. Planning commit `77e9ec5` added no `https?://` / `www.` lines. LICENSE files state "No source-material download link is published". | CLOSED |
| T-11-02 | Information Disclosure (Link Policy) + spoofed ICD | high | mitigate | `packs/is-gps-200n` tree has zero scheme URLs. P11-PRE-2 quote in PACK.yaml:22–24 is the extracted DIST-A sentence (`DISTRIBUTION STATEMENT A. Approved for public release. Distribution is unlimited.`). Live extract `sources/is-gps-200n/book_skill_work/full_text.txt:8` matches that sentence. SAIC ICC line is watch-item only (PACK.yaml:25–27; LICENSE:25–27). Exemplar-not-dump: 6 chapters; `ch06-appendices-as-a-map.md` is a routing table and explicitly forbids transcribing Apps II–IV / PRN / Gold-code / CNAV bit fields. SKILL.md:74 names `faa-std-025` as complementary, not a live ICD. No `packs/is-gps-705j`, `is-gps-800j`, `icd-gps-153`, `gps-is-200n`. | CLOSED |
| T-11-03 | Elevation / spoofed Integration-Logistics unlock | high | mitigate | IO-05/IO-06 are dated DEFERRED records only (`REQUIREMENTS.md:25–26`). `ls packs \| grep -Ei "aaf-|army-cba|stakeholder|nasa-sp-7084"` empty. No AAF string in the four in-scope pack trees. STATE.md:60 records deferral + SP-7084 skipped. VET-19-03 remains `- [ ]` / "still NOT yet vetted — do not use". | CLOSED |
| T-11-04 | Information Disclosure (source leak) | high | mitigate | `sources/` gitignored (`.gitignore:17`). `git ls-files -- sources/ **/full_text.txt` = 0 tracked. `git log --name-only 1b3e4f4^..HEAD` has zero `sources/` or `full_text.txt` paths. Commits in range touch only pack trees, planning, and thin-register surfaces (`1b3e4f4`, `ee762d0`, `3530290`, `6157641`, `77e9ec5`, `b289e62`, `2309329`). | CLOSED |
| T-11-05 | Tampering / spoofed clearance (leaning treated as skip-confirm) | high | mitigate | NASA PACK.yaml:21–33 records P11-PRE-1 on **this** extract: 0 Copyright / All rights / (c) hits; title-page identity quoted; "Internet Public -- Standard is cleared for public accessibility on the internet"; "Tier 1 leaning was not treated as skip-confirm." Live extract: `grep -c -iE "Copyright\|All rights"` = 0; title-page lines at `full_text.txt:8–14` (`NASA-STD-8719.14C`, `Approved: 2021-11-05`, `Process for Limiting Orbital Debris`). GPS PACK.yaml:22–32 records P11-PRE-2 DIST-A verbatim + SAIC watch-item + "Tier 1 leaning was not treated as skip-confirm." Live extract DIST-A at line 8; SAIC at line 23. IO-02 new chapters: PACK.yaml:37–66 records P7-PRE-4 per ch11/ch12/ch13 (title + retrieved 2026-08-17 + DEBoK PD + OSD/USD(R&E) OPR; no DIST B–F / all-rights). | CLOSED |
| T-11-06 (11-01 IP) | IP theft (verbatim) | high | mitigate | Re-ran this audit: `check_overlap.py` exit 0 on `nasa-std-8719-14` vs extract, `is-gps-200n` vs extract, and `dod-vva-rpg` vs `chapter_fulltexts/ch11.txt`, `ch12.txt`, `ch13.txt` (each: "No verbatim run >= 12 words"). 11-01-SUMMARY records one NASA ch04 paraphrase that closed the only overlap fail before commit `1b3e4f4`. ch06 maps appendices and does not transcribe App II–IV payloads. | CLOSED |
| T-11-06 (11-02 map) | Tampering (double-build IO-01) | high | mitigate | `git log --name-only 1b3e4f4^..HEAD` has no `docs/capability-pack-map.json` or `.md`. `git diff --name-only -- docs/capability-pack-map.json` empty. Last map commit remains `dc35907` (Phase 8, 2026-08-17 01:21). IO-01 is a table in `11-02-SUMMARY.md` + REQUIREMENTS parenthetical only. federal-bca Topic Index nudge (`SKILL.md:64`) is pack-side, not a map edit. | CLOSED |
| T-11-07 (11-01 scope) | Elevation (scope creep) | high | mitigate | `files_modified` held: Wave A = two new pack trees; Wave B = dod-vva-rpg extend + federal-bca SKILL + planning + thin-register. Forbidden slugs absent (`dodm-5000-102`, `aaf-*`, `army-cba`, `stakeholder-engagement`, `nasa-sp-7084`, `is-gps-705j`, `is-gps-800j`, `icd-gps-153`, `gps-is-200n`, `nasa-hdbk-8719-14`). Plugin version still `1.18.0`. No `v1.19.0` / `REL-19-02` tag (`git tag -l` latest release tag is `v1.18.0`). | CLOSED |
| T-11-07 (11-02 tick) | Repudiation / silent tick | medium | mitigate | All IO-01..07 remain `- [ ]`. `grep -c '^\- \[ \] \*\*IO-0[1-7]\*\*'` = 7. IO-05/06 dated DEFERRED; IO-07 dated ACCEPT (`REQUIREMENTS.md:25–27`). No `- [x]` IO lines. Verify, not execute, owns the tick. | CLOSED |
| T-11-08 | Elevation (steal Phase 13) | high | mitigate | `.cursor-plugin/plugin.json` `version` = `1.18.0`; file contains no `1.19.0`. Thin-register commit `b289e62` adds skill paths only. No REL-19-02 / `v1.19.0` tag created. CHANGELOG / GitHub Release not in the phase range. | CLOSED |

No unmitigated high. T-11-07 (silent tick) is medium and is CLOSED anyway.

---

## 2. Audit-brief checks (declared Phase 11 threats)

### 2a. Information disclosure — source URLs in packs

Zero `http`/`https` in either new pack tree, the extended `dod-vva-rpg` tree, and the federal-bca SKILL.md edit. LICENSE / PACK.yaml use "no source-material download link" + title/date provenance. New NOTICE pack blocks have no URL. SOURCE-VETTING still 0 `http` strings. See Note N1 for in-policy bare hostnames.

### 2b. Information disclosure — committed `sources/` or `full_text.txt`

Range `1b3e4f4^..HEAD` name-only list is pack files + planning + thin-register only. `sources/` remains gitignored. Zero tracked `full_text.txt`. Extracts exist on disk for overlap re-run and are not staged.

### 2c. False clearance — Tier 1 leaning used without P11-PRE-1/2 quotes

Not skip-confirm. Both new PACK.yaml notes quote the extracted-copy gates and say leaning was not treated as skip-confirm. Auditor re-read the live extracts: NASA 0 Copyright/All-rights hits + title-page identity; GPS DIST-A sentence present. IO-02 did not inherit clearance: P7-PRE-4 recorded per new chapter.

### 2d. Licence leak — `check_overlap` re-run

Cheap re-run this audit (REF `jgs-reference-skill` `tools/check_overlap.py`):

| Source | Pack | Result |
|---|---|---|
| `sources/nasa-std-8719-14/book_skill_work/full_text.txt` | `packs/nasa-std-8719-14` | exit 0 |
| `sources/is-gps-200n/book_skill_work/full_text.txt` | `packs/is-gps-200n` | exit 0 |
| `sources/dod-vva-rpg/chapter_fulltexts/ch11.txt` | `packs/dod-vva-rpg` | exit 0 |
| `sources/dod-vva-rpg/chapter_fulltexts/ch12.txt` | `packs/dod-vva-rpg` | exit 0 |
| `sources/dod-vva-rpg/chapter_fulltexts/ch13.txt` | `packs/dod-vva-rpg` | exit 0 |

No verbatim run ≥ 12 words. GPS ch06 remains a map (no App II–IV dump).

### 2e. AAF used despite unused

AAF was not built. IO-05/IO-06 are dated DEFERRED with "Not built. Not invented." No `packs/aaf-*`. No AAF guidebook content in the in-scope pack trees. `dod-rio` AAF chapters are explicitly recorded as not licensing AAF guidebooks.

### 2f. Map tampering this phase

`docs/capability-pack-map.json` not in any Phase 11 commit and has no working-tree diff. Last touch remains Phase 8 `dc35907`. Remap is specified for MAP-19-03 / Phase 12 only.

### 2g. Prompt injection in new pack / IO surfaces

Scanned new pack trees, new RPG chapters, federal-bca SKILL.md, and REQUIREMENTS for injection payloads: "ignore previous/all/prior/above", "disregard", "forget your instructions", "system prompt", "you are now", "act as an AI", role tags (`<system>`, `<|im_start|>`) — zero matches.

### 2h. Secrets / PII

Scanned the same surfaces for `AKIA…`, `sk-…`, `ghp_/gho_/github_pat_`, `xox[bpars]-`, `AIza…`, `BEGIN PRIVATE KEY`, `password=` / `api_key` / `Bearer` — zero matches. SAIC street-address mention is recorded as a watch-item and is **not** copied into chapter bodies (plan: skip contractor street address as content).

---

## 3. SUMMARY.md `## Threat Flags` mapping

Neither `11-01-SUMMARY.md` nor `11-02-SUMMARY.md` has a `## Threat Flags` section. 11-01 deviations: When-to-use adjacency vs analog layout; one ch04 overlap paraphrase (required-gate repair). 11-02 deviations: UCO HTML-only skip (pre-authorized). No new attack surface. No unregistered flags.

---

## 4. Notes (informational — no open threats, no action required this phase)

- **N1 — Bare hostnames in pack provenance (in-policy).** `gps.gov` in `packs/is-gps-200n/SKILL.md:74` ("official gps.gov PDF"). `cto.mil` and `de-bok.org` in `packs/dod-vva-rpg/PACK.yaml` notes and `LICENSE:9`. These are not scheme URLs and not hyperlinks. Declared gate (`https?://` in pack trees; zero `http` in SOURCE-VETTING) passes exactly. Same class as Phase 10 analog N1.
- **N2 — Thin-register `docs/packs.html` GitHub hrefs.** `gen_packs_page.py` emitted `https://github.com/jgsystemsconsulting/.../SKILL.md` rows and the README badge uses `img.shields.io`. Those are existing site/generator surfaces, not pack trees, not SOURCE-VETTING, and not new NOTICE pack-licence blocks. T-11-01's pack/SOURCE-VETTING boundary holds.
- **N3 — NOTICE pre-existing CC / font URLs.** NOTICE:25, :105, :185, :733–734 are older pack/font licence lines, not added by `[pack: nasa-std-8719-14]` / `[pack: is-gps-200n]`.
- **N4 — Forward boundary.** Map apply (MAP-19-03), IO checkbox ticks, and REL-19-02 version/tag remain Phase 12 / verify / Phase 13. This audit closes Phase 11 *enforcement* of "do not apply / do not tick / do not tag."

---

## 5. Scope discipline

- Implementation files read-only: audit wrote only this artifact.
- No MCP. No WINDOWS.md.
- Unclassified coverage probes left unresolved (not auto-resolved).
- Overlap re-run used gitignored extracts; extracts were not staged.

**Verdict:** SECURED — all declared threats CLOSED at declared boundaries; audit-brief checks pass; threats_open = 0.
