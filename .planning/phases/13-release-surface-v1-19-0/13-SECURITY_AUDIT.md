# Phase 13 Security Audit — Release Surface v1.19.0

**Phase:** 13 — release-surface-v1-19-0 (plans 13-01, 13-02)
**Range audited:** release commit `bb9df10` (13 files), tag object `49feb74` → `bb9df10`, GitHub Release `v1.19.0`. Content range: `830fdd9..bb9df10` (consolidated 13-01 surfaces). Post-tag `.planning` follow-up `3007134` inspected only to confirm it did not rewrite the tagged tree.
**Date:** 2026-08-17
**Auditor method:** adversarial verification per declared disposition; every mitigation assumed absent until git-object / gate / `gh` evidence proved presence at the correct boundary. Implementation files read-only. Analog: `9-SECURITY_AUDIT.md` (release-surface) + `12-SECURITY_AUDIT.md` (threat-register table).
**WINDOWS.md:** not present. Tautology N/A.
**MCP:** not used.

**Verdict:** SECURED

**Threats Closed:** 11/12 mitigated CLOSED + 1/12 ACCEPTED (T-13-11, declared accept) | **threats_open:** 0
**ASVS depth applied:** L2 (mitigation verified present AND placed at the correct trust boundary: working tree → explicit-path release commit; version trio / CHANGELOG → public notes; local `check_release` / `check_capability_map` → tag; annotated tag → origin + GitHub Release; `.planning` records → follow-up commit after the tag).

Both PLAN `<threat_model>` blocks authored at plan time. IDs do not collide across plans (T-13-01..06 in 13-01; T-13-07..12 in 13-02).

---

## 1. Declared threat register (from 13-01-PLAN.md + 13-02-PLAN.md `<threat_model>`)

| Threat ID | Category | Severity | Disposition | Evidence found | Status |
|-----------|----------|----------|-------------|----------------|--------|
| T-13-01 | Tampering | high | mitigate | Release commit `bb9df10` is 13 `M` paths only (version trio, CHANGELOG, README, catalog, 6 docs surfaces + `capability-pack-map.md`). `git show --name-only bb9df10` has zero `sources/`, `packs/`, `.planning/`, `_v1.19.0-notes.tmp.md`, `master_flow_state.json`, `.edge-coverage.json`. No `git add -A` blast. Working-tree `??` state files remain untracked. | CLOSED |
| T-13-02 | Tampering | medium | mitigate | `RELEASE-INFO.txt` Version/Tag `1.19.0`, Staged `2026-08-17T22:56:12Z` (not the stale `2026-08-17T00:59:27Z`). `docs/packs.html` regenerated (REV 1.19.0); live re-run `python tooling/gen_packs_page.py` then `git diff --stat docs/packs.html` empty. File is in the release commit as a generated surface, not a hand-edit. | CLOSED |
| T-13-03 | Information disclosure | low | mitigate | CHANGELOG `[1.19.0]` body (between headings): zero `http`, zero U+2014. Gate scans CHANGELOG (`python tooling/check_release.py` → `RELEASE CHECK: PASS`). `docs/SOURCE-VETTING.md` `http` count = **0** on HEAD and on `v1.19.0`. Release-commit URL scan: 9 unique, all own-repo / shields.io / keepachangelog / semver — **zero source-material URLs**. | CLOSED |
| T-13-04 | Spoofing | medium | mitigate | Tagged `docs/capability-pack-map.json` `map_version` == `"1.19.0"`, `schema_version` == 2, TOTAL 644. CONTRACT example envelope `"map_version": "1.19.0"`; historical `1.17.0` line remains. Membership not regenerated this phase (`packs/*/chapters/*` absent from `830fdd9..bb9df10`). | CLOSED |
| T-13-05 | Elevation of privilege | high | mitigate | `.github/workflows/validate.yml` absent from `bb9df10` and from `830fdd9..HEAD`. File still line-wraps "never / executes checked-out repository code". `check_capability_map` string **absent**. `check_release.py` still in-process `import check_capability_map` + `check_capability_map.main()`; `subprocess` / `urllib` / `requests` / `http.client` absent. | CLOSED |
| T-13-06 | Repudiation | medium | mitigate | Tagged `catalog.json`: 63 packs; `dod-vva-rpg.chapters` == **13**. README live rows include `nasa-std-8719-14` (7) and `is-gps-200n` (6); RPG `(13 chapters)`. Gate does not assert the leftover integer; REL-19-01 honesty is in the tagged tree. | CLOSED |
| T-13-07 | Tampering | high | mitigate | Same explicit 13-path index as T-13-01. 13-02-SUMMARY records soft-reset to `PRE_RELEASE_HEAD=830fdd9` then `git add --` of named paths. `docs/capability-pack-map.md` included only because 13-01 edited it (allowed). No research/VALIDATION/PLAN files in the release commit. | CLOSED |
| T-13-08 | Repudiation | medium | mitigate | `git cat-file -t v1.19.0` → `tag` (annotated, not lightweight). Tagger `jgsystemsconsulting`; message `v1.19.0: 2 IO-unlock packs + VV&A chapters + DA remap (63 +2 signposts)` colon-style matching v1.17/v1.18. Peels to `bb9df10`. Origin: `refs/tags/v1.19.0` = `49feb74`, `^{}` = `bb9df10` — byte-identical to local. | CLOSED |
| T-13-09 | Tampering | medium | mitigate | Both gates re-run this audit on a content-identical tree (`git diff --name-only v1.19.0 HEAD` = `.planning/` only): map `PASS` TOTAL 644 exit 0; `RELEASE CHECK: PASS` exit 0 (map cluster block prints first). Notes file written under phase dir, never `/tmp`; path absent from working tree and from `git ls-files` / history. | CLOSED |
| T-13-10 | DoS (of release) | high | mitigate | Tag points at `bb9df10`, whose body records both-gates PASS. Independent basis at the tag: catalog 63 / dirs 65; map_version 1.19.0 / 644. Live re-run this audit: MAP_EXIT 0, REL_EXIT 0. Not tagged on a red gate. | CLOSED |
| T-13-11 | Elevation of privilege | low | accept | Admin-bypass remains in force by user opt-in (13-02-SUMMARY: push printed bypass notice; no PR; branch protection unchanged). Declared accept. Annotated tag (T-13-08) is the tamper-evidence control, not branch rules. Not phase-introduced attack surface. | ACCEPTED |
| T-13-12 | Information disclosure | low | mitigate | `_v1.19.0-notes.tmp.md` does not exist on disk; `git log --all` on the path empty; not tracked. `git status --short` shows only unrelated `.planning/*/master_flow_state.json` and `.edge-coverage.json` (never staged). | CLOSED |

No unmitigated high. Highest declared severity this phase is high (T-13-01, T-13-05, T-13-07, T-13-10); all four CLOSED.

---

## 2. Audit-brief checks (declared Phase 13 threats)

### 2a. Release commit file list (no `sources/`, no secrets, no `git add -A`)

`git show --name-status bb9df10` = exactly 13 `M` files:

`.claude-plugin/plugin.json`, `.cursor-plugin/plugin.json`, `CHANGELOG.md`, `README.md`, `RELEASE-INFO.txt`, `catalog.json`, `docs/capability-map-CONTRACT.md`, `docs/capability-pack-map.json`, `docs/capability-pack-map.md`, `docs/index.html`, `docs/packs.html`, `docs/products/website/01-jgs-se-knowledge-packs.yaml`, `docs/products/website/catalog.yaml`.

Zero adds. Zero `sources/`, `packs/`, `.github/`, `SKILLS.md`, `NOTICE`, `LICENSE`, notes tmp, or `.planning/` internals in the commit. Credential-pattern scan of the 264-line diff (`ghp_`, `gho_`, `github_pat_`, `AKIA…`, `sk-…`, `BEGIN PRIVATE KEY`, `api_key`, `password=`, `Bearer`, `xox[bpars]-`, `AIza…`): **0 hits**. PII: no emails in the diff; sole email is the author's GitHub `noreply` address in commit metadata (`245595077+jgsystemsconsulting@users.noreply.github.com`).

`.planning` files exist in the **historical tagged tree** (already on `main` before the release act: 13-01/02 PLAN, RESEARCH, PATTERNS, VALIDATION, PLAN_CHECK, PLAN_REVIEW). They were **not staged into the release commit**. That is the declared boundary (working tree → release commit), same class as Phase 9 (range adds under `.planning/` accounted for; release commit itself clean).

### 2b. SOURCE-VETTING `http=0`

`Path('docs/SOURCE-VETTING.md').read_text().count('http')` = **0** on HEAD. `git show v1.19.0:docs/SOURCE-VETTING.md` same **0**. File is not in `bb9df10` (no heading rewrite this phase). Residual `v1.18.0` heading is history-only, as required.

### 2c. Tag is annotated, not lightweight

`git cat-file -t $(git rev-parse v1.19.0)` = `tag`. `git for-each-ref refs/tags/v1.19.0` = `tag 49feb74378276822a795cb1a161aa5b14661fb39`. Lightweight tag would have been `commit`. Do not retag.

### 2d. Shipping RED gates

Precondition held. Live this audit: `python tooling/check_capability_map.py` exit 0, `PASS: capability map OK`, TOTAL 644, map_version 1.19.0. `python tooling/check_release.py` exit 0, map cluster block first, then `RELEASE CHECK: PASS`. Catalog 63 / dirs 65. Version trio plugin == cursor == RELEASE-INFO == CHANGELOG top == `1.19.0`.

### 2e. Leaking URLs (CHANGELOG + GitHub Release notes)

CHANGELOG new entry: `http` absent; em dash absent. `gh release view v1.19.0 --json body` → `https?://` count **0**. Title `v1.19.0 — Agent IO Depth (2 packs + VV&A chapters + DA remap)` uses the specified public em dash; body stays em-dash-free and names IO-01..07 with IO-05/06 DEFERRED and IO-07 ACCEPT (no invented-pack / built claim).

### 2f. Staging `.planning` internals into the release commit

Release commit file list has none. Follow-up `3007134` is `.planning`-only (`STATE.md`, `MILESTONES.md`, `ROADMAP.md`, `REQUIREMENTS.md`). `git merge-base --is-ancestor bb9df10 3007134` true. `git diff --name-only v1.19.0 HEAD` is `.planning/` only — tagged content tree unchanged.

---

## 3. SUMMARY.md `## Threat Flags` mapping

Neither `13-01-SUMMARY.md` nor `13-02-SUMMARY.md` has a `## Threat Flags` section. 13-01 `## Deviations` = `None.` 13-02 deviations are process (soft-reset performed as required; phase-dir notes; `gh auth switch` to `jgsystemsconsulting`; admin-bypass printed). No new attack surface. Unregistered-flag count: 0.

---

## 4. Notes (informational — no open threats, no action required this phase)

- **N1 — Em dash in the release *subject*, not the CHANGELOG body.** `git show bb9df10` subject contains U+2014 (`Agent IO Depth — 2 packs…`), matching the GitHub Release title convention. T-13-03 / link-policy apply to the CHANGELOG `[1.19.0]` entry and notes body, both clean.
- **N2 — Historical `.planning` in the tagged tree.** PLAN/RESEARCH/PATTERNS/VALIDATION were committed to `main` before `bb9df10`. CI / link-policy skip `.planning`. They are not a release-commit leak.
- **N3 — T-13-11 accepted residual.** Same class as Phase 5 note 1: the releasing identity can bypass `main` protection; the annotated tag is the tamper-evidence control. Do not change branch protection in this phase.
- **N4 — Untracked GSD state.** `??` `master_flow_state.json` / `.edge-coverage.json` under later phases remain untracked and were not in `bb9df10`. Keep it that way.

---

## 5. Scope discipline

- Implementation files read-only: audit wrote only this artifact.
- No MCP. No WINDOWS.md. Do not retag.
- Unclassified coverage probes left unresolved (not auto-resolved).
- Analog 9/12/5 methods reused: git-object inspection, live gates, `gh release view`, credential/URL scans, tag-object vs `ls-remote`.

**Verdict:** SECURED — all declared threats CLOSED or ACCEPTED at declared boundaries; audit-brief checks pass; threats_open = 0.
