# Phase 12 Security Audit — Map regen + hygiene + gate wiring

**Phase:** 12 — map-regen-hygiene-gate-wiring (plans 12-01, 12-02)
**Scope:** map regen + MAP-19-03 MOVE + MAP-19-02 floors + MAP-19-05 CONTRACT + MAP-19-04 in-process wire + HYG-01..04. Files: `docs/capability-pack-map.json`, `docs/capability-pack-map.md`, `docs/capability-map-CONTRACT.md`, `tooling/check_capability_map.py`, `tooling/check_release.py`, `CHANGELOG.md`, `.gitattributes`, four SKILL.md nits (`mil-std-881f`, `dafman-63-119`, `mil-std-40051`, `federal-bca`), `packs/federal-bca/PACK.yaml`. Content range: `53099e0^..HEAD` (map regen + floors + CONTRACT + wire + hygiene + SUMMARYs).
**Auditor method:** adversarial verification per declared disposition; every mitigation assumed absent until grep/read proved presence at the correct boundary. Implementation files not modified. Overlap re-run not applicable (no new pack extracts this phase).
**Date:** 2026-08-17 (audit) — evidence rows stamped 2026-08-17 per research date convention.
**WINDOWS.md:** not present. Tautology N/A.
**MCP:** not used.

**Verdict:** SECURED

**Threats Closed:** 10/10 declared rows (T-12-01, T-12-02, T-12-03, T-12-04, T-12-05, T-12-06, T-12-07, T-12-08, T-12-09, T-12-10) | **threats_open:** 0
**ASVS depth applied:** L2 (mitigation verified present AND placed at the correct trust boundary: packs/ → map JSON uniqueness/staleness; remap rows → DA-only membership; map JSON → se-agents contract (502 residue / Cyber+DE unbound); check_release.py → local `check_capability_map.main()` not network/subprocess/CI; this repo → sibling `vet_source.py` never vendored; CHANGELOG encoding → version-single-source header).

Both PLAN `<threat_model>` blocks authored at plan time. IDs do not collide across plans (T-12-01..05 in 12-01; T-12-06..10 in 12-02).

---

## 1. Declared threat register (from 12-01-PLAN.md + 12-02-PLAN.md `<threat_model>`)

| Threat ID | Category | Severity | Disposition | Evidence found | Status |
|-----------|----------|----------|-------------|----------------|--------|
| T-12-01 | Tampering | medium | mitigate | `python tooling/check_capability_map.py` exit 0, `PASS: capability map OK`, TOTAL 644. Envelope `schema_version==2`, `map_version=="1.18.0"`, `generated_on=="2026-08-17"`. Bidirectional staleness: `on_disk_only=set()`, `map_only=set()`, 63/63 chapter-bearing packs. `(pack, chapter)` pairs 644 unique / 644 total. Gate checks envelope, file existence, uniqueness, name-keyed THRESHOLDS (`tooling/check_capability_map.py:8-14, 33-43`). | CLOSED |
| T-12-02 | Tampering | medium | mitigate | Live JSON membership: DA set == locked five-row want-set (`nasa-ceh` ch06, `nasa-se-handbook` ch34-6-8, `federal-bca` ch04, `federal-bca` ch06, `dod-vva-rpg` ch06) — 5 entries / 4 packs. `federal-bca` ch04+ch06 **absent** from Opportunity; Opportunity still holds ch01–ch03, ch05 + 3 support files (count 8). `dod-vva-rpg` ch06 **absent** from Assurance. ch08 still Validation; ch10 still Risk. Uniqueness would fail a copy-not-move. | CLOSED |
| T-12-03 | Elevation | medium | mitigate | Integration still 4 entries / 4 packs. `ls packs \| grep -Ei 'aaf-\|army-cba\|stakeholder\|dodm-5000-102\|nasa-sp-7084'` empty. No generator (`tooling/generate_capability_map.py` / `gen_capability_map.py` absent). THRESHOLDS Integration `>=4` without raid. Conjunct: none of five listed primaries is `(count < 4 AND n_packs == 1)`. DA 5/4 `floor_fail=False`. 12-01-SUMMARY: "floor held; AAF still deferred; no raid." | CLOSED |
| T-12-04 | Information disclosure | low | mitigate | CONTRACT §6 (`docs/capability-map-CONTRACT.md:104-112`) states live **628+** / post-regen **644**, **502** is residue, **Cybersecurity & Security Engineering** (69/10) and **Digital Engineering & Digital Twins** (25/4) remain **unbound**. No Cyber/DE binding tables added. Live JSON confirms those counts; clusters exist as map rows only. | CLOSED |
| T-12-05 | Repudiation | low | mitigate | JSON `map_version` is exactly `"1.18.0"` (not 1.19.0). `generated_on` is execute-day `2026-08-17`. CONTRACT example envelope still `"1.18.0"` (`:15`). Phase 13 owns 1.19.0. `capability-pack-map.md:15` v1.19 line is a **changelog bullet** (new slugs + remap), not a version-surface bump. | CLOSED |
| T-12-06 | Tampering | medium | mitigate | Wire only after GREEN: `53099e0` (map) → `7134474` (floors; gate GREEN) → `ca27199` (import). `git merge-base --is-ancestor 7134474 ca27199` true. `check_release.py:215-222` is in-process `import check_capability_map` + `check_capability_map.main()` + `fail()` on non-zero. `subprocess` / `urllib` / `requests` / `http.client` absent from `check_release.py`. Both gates now PASS (`MAP_EXIT:0`, `REL_EXIT:0`); release stdout reprints the map cluster-count block then `RELEASE CHECK: PASS`. Trusted local, not network. | CLOSED |
| T-12-07 | Elevation | medium | mitigate | `.github/workflows/validate.yml` not in `53099e0^..HEAD`. File still comments "never executes checked-out repository code" (`:4-5`). `check_capability_map` string **absent**. CI uses inline `python3 - <<'PY'` heredocs only — no `python tooling/...`. `check_release.py:19-20` restates CI never execs repo code. | CLOSED |
| T-12-08 | Spoofing | low | mitigate | `test ! -e tooling/vet_source.py` holds. `git ls-files` has zero `vet_source` / `jgs-reference-skill` / `.env` / `id_rsa` paths. Phase range name-only list has no sibling files. 12-02-SUMMARY Path A records sibling path `$REF/tools/vet_source.py`, commit `1c8b781`, PR `https://github.com/jgsystemsconsulting/jgs-reference-skill/pull/2` (planning store only). Existing EXCLUDED keys not weakened (SUMMARY). | CLOSED |
| T-12-09 | Tampering | medium | mitigate | CHANGELOG first 8 bytes `3c212d2d0a436f70` (`<!--` + LF + `Cop`); BOM False; CRLF 0. `## [1.18.0]` present; `## [1.19.0]` absent. `.gitattributes` is exactly `*.md text eol=lf\n` (no `* text=auto`). JGSC + SPDX remain in first 600 chars (release header check still PASSes). | CLOSED |
| T-12-10 | Repudiation | low | mitigate | Version trio: plugin `1.18.0` == CHANGELOG top `1.18.0` == RELEASE-INFO `1.18.0`. `.cursor-plugin/plugin.json` also `1.18.0`; neither plugin file contains `1.19.0`. `git tag -l 'v1.19*'` empty; latest annotated release tag is `v1.18.0`. Catalog `dod-vva-rpg.chapters` still **10**. MAP-19 / HYG REQUIREMENTS boxes remain `- [ ]`. | CLOSED |

No unmitigated high. Highest declared severity this phase is medium; all CLOSED.

---

## 2. Audit-brief checks (declared Phase 12 threats)

### 2a. Wiring a RED map into release

Hard-gate order held. Map regen (`53099e0`) and THRESHOLDS (`7134474`) precede the import (`ca27199`). Live `check_capability_map.py` is GREEN (644 / uniqueness / floors). `check_release.py` imports the **local** module after the existing `sys.path.insert(0, str(ROOT / "tooling"))` (`:120`) — same pattern as `validate_pack`. No subprocess, no URL fetch. A non-zero `main()` becomes `[map] check_capability_map.py failed`. Docstring no longer claims standalone (`check_capability_map.py:16`); CONTRACT §4 (`:81-83`) says the gate **is** invoked in-process.

### 2b. URL leak (SOURCE-VETTING + published map/contract/hygiene packs)

`grep -c http docs/SOURCE-VETTING.md` = **0**. Extended: `https`, `://`, `www.`, `mailto:`, `ftp://`, `source_url` = 0. Same zero `http`/`https://` in `capability-pack-map.json`, `capability-pack-map.md`, `capability-map-CONTRACT.md`, and the four hygiene-touched SKILL.md plus `packs/federal-bca/PACK.yaml`. HYG-04 added no URL. Phase range does not touch `docs/SOURCE-VETTING.md`. Planning SUMMARY PR URL lives under `.planning/` (CI/link-policy skip; never ships).

### 2c. Weakening floors

THRESHOLDS keep Training **1**, Traceability **3**, Opportunity **2**. Interfaces raised **3 → 4**. Added DA / Validation / Integration / Ops **4**. Old `"Interface Management & ICIDs": 3` gone. Live counts: DA 5/4, Validation 7/4, Integration 4/4, Interfaces 9/4, Ops 13/5 — all `floor_fail=False`. Opportunity still 8 (≥2). Integration not raided; no invented slug.

### 2d. Committing sibling secrets / vendoring `vet_source.py`

HYG-03 stayed out of this tree. No `tooling/vet_source.py`. No sibling paths in `git ls-files`. Phase commits touch only this-repo map/tooling/hygiene/planning files. Credential/injection scan of phase-touched surfaces: zero `AKIA…` / `sk-…` / `ghp_` / `gho_` / `github_pat_` / `xox[bpars]-` / `AIza…` / `BEGIN PRIVATE KEY` / `password=` / `api_key` / `Bearer`; zero "ignore previous/all/prior/above", "disregard", "forget your instructions", "system prompt", "you are now", "act as an AI", `<system>`, `<|im_start|>`.

### 2e. Version-spoof / premature 1.19 tag

Plugin / CHANGELOG / RELEASE-INFO / cursor plugin / `map_version` all **1.18.0**. No `## [1.19.0]`. No `v1.19*` tag. `catalog.json` and `README.md` and both `plugin.json` files absent from `53099e0^..HEAD`. Catalog leftover (`dod-vva-rpg.chapters == 10`) untouched — Phase 13 fence.

### 2f. CI elevation (repo-Python path)

`validate.yml` unchanged this phase. Inline stdlib only. `check_capability_map` not named. Comment + `check_release.py` docstring both keep the local/trusted vs CI split.

---

## 3. SUMMARY.md `## Threat Flags` mapping

Neither `12-01-SUMMARY.md` nor `12-02-SUMMARY.md` has a `## Threat Flags` section. Both `## Deviations` ledgers are `None.` No new attack surface. No unregistered flags.

---

## 4. Notes (informational — no open threats, no action required this phase)

- **N1 — v1.19 changelog bullet vs version trio.** `docs/capability-pack-map.md` documents the regen under a "Changelog (v1.19)" bullet. That is human history of the *next* release's map content. Envelope `map_version` and the version trio stay 1.18.0. T-12-05 / T-12-10 hold.
- **N2 — 12-01 SUMMARY §4 sentence is historical.** 12-01-SUMMARY:211 records "§4 still says the gate is standalone" at 12-01 close. 12-02 flipped CONTRACT §4 (`ca27199`). Live file is the wired sentence. Not a regression.
- **N3 — HYG-03 PR URL in planning only.** The sibling PR locator is in `12-02-SUMMARY.md` (`.planning/`). SOURCE-VETTING and pack trees stay URL-free. Same class as Phase 11 analog N4 (forward/external locator not a pack leak).
- **N4 — Forward boundary.** Catalog `dod-vva-rpg.chapters` 10→13, README new-slug rows, version trio 1.19.0, `v1.19.0` tag / GitHub Release, and MAP-19 / HYG checkbox ticks remain Phase 13 / verify. This audit closes Phase 12 *enforcement* of "wire only GREEN; do not leak URLs; do not weaken floors; do not vendor sibling; do not tag."

---

## 5. Scope discipline

- Implementation files read-only: audit wrote only this artifact.
- No MCP. No WINDOWS.md.
- Unclassified coverage probes left unresolved (not auto-resolved).
- Sibling `vet_source.py` was not opened as a write target; existence of the vendor copy in *this* repo was disproved.

**Verdict:** SECURED — all declared threats CLOSED at declared boundaries; audit-brief checks pass; threats_open = 0.
