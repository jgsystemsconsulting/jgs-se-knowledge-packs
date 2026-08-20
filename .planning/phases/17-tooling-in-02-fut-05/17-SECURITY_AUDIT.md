# Phase 17 Security Audit — release tooling (overlap + FUT-05 residual)

**Phase:** 17 — tooling-in-02-fut-05 (plan 17-01)
**Range audited:** execution commits `84a0f35`, `cf1d361`, `ee7534b`, `4ac5072` (+ position `c4d3310` / `7122667` planning only).
**Date:** 2026-08-20
**Auditor method:** adversarial verification per declared disposition; every mitigation assumed absent until file-content / git evidence proved presence at the correct boundary. Implementation files read-only during audit. Analog: `16-SECURITY_AUDIT.md`.
**WINDOWS.md:** not present. Tautology N/A.
**MCP:** not used.
**ASVS depth applied:** L2 (mitigation present AND at correct trust boundary: fixed `ROOT` glob only — no user path argv; WHITELIST module constant + CONTRACT §7; in-process `check_overlap.main()` fail-on-nonzero before map; CI fence `validate.yml` never execs repo Python; CONTRACT §8 refuses byte-stable full-map generator).
**block_on:** high (default; no `.planning/config.json` override)

**Verdict:** SECURED

**Threats Closed:** 6/6 (4 mitigated CLOSED + 2 ACCEPTED T-17-04, T-17-SC) | **threats_open:** 0

---

## 1. Declared threat register (from 17-01-PLAN.md `<threat_model>`)

| Threat ID | Category | Severity | Disposition | Evidence found | Status |
|-----------|----------|----------|-------------|----------------|--------|
| T-17-01 | Tampering | medium | mitigate | `tooling/check_overlap.py:32-34` module-level `WHITELIST = {"ch01-introduction.md"}` only. Collisions filtered at `:52` `name not in WHITELIST` → FAIL. CONTRACT §7 lists whitelist + requires explicit WHITELIST edit for new shared basenames (not silent pass). Live dups assert: only `ch01-introduction.md`; un-whitelisted set empty → `OVERLAP_ASSERT_OK`. | CLOSED |
| T-17-02 | Elevation of Privilege | medium | mitigate | `.github/workflows/validate.yml` header: "never" + "executes checked-out repository code". Workflow uses inline `python3 - <<'PY'` only. `check_overlap` / `check_capability_map` / `tooling/check_overlap` **absent**. Phase commits do not touch `.github/workflows/validate.yml`. | CLOSED |
| T-17-03 | Tampering | medium | mitigate | `tooling/check_release.py:216-223` block `# 5d. overlap (TOOL-20)`: `import check_overlap`; `rc = check_overlap.main()`; `fail` on `rc != 0` and on `Exception`. No `subprocess`/`Popen`/`os.system` in `check_overlap.py` or `check_release.py`. Same shape as map block `# 5e`. Docstring items 8–9 name both local/trusted gates. | CLOSED |
| T-17-04 | Information Disclosure | low | accept | FAIL lines print pack slugs already public under `packs/`. No secrets/PII. Root `SECURITY.md` has no per-phase accepted-risks log; acceptance = PLAN disposition + this ACCEPTED row (same class as T-16-08). | ACCEPTED |
| T-17-05 | Spoofing | medium | mitigate | CONTRACT §8 FUT-05 residual: names mechanical slice in `check_capability_map.py`; states cluster/note need **agent judgment**; sentence "This milestone does **not** claim a byte-stable full-map generator." No `tooling/generate_capability_map.py` (or any `tooling/generate*`). Refresh path remains agent + map checker. | CLOSED |
| T-17-SC | Tampering | high | accept | Phase trees stdlib only (`pathlib`/`sys`). No `requirements.txt` / `pyproject.toml` / lockfile / package-manager installs in `84a0f35^..HEAD` path set for this work. Acceptance = PLAN disposition + verified absence of package installs + this ACCEPTED row. | ACCEPTED |

No unmitigated high/critical. Highest mitigate severity medium — all CLOSED. High severity T-17-SC accepted with verified no-install evidence.

---

## 2. Audit-brief checks (coordinator scope)

### 2a. Path traversal / unsafe file ops in check_overlap

- `ROOT = Path(__file__).resolve().parent.parent` fixed; scan only `(ROOT / "packs").glob("*/chapters/*.md")`.
- No `sys.argv` / `argparse` / `input()` — no user-controlled paths.
- No `open()`, `write`, `unlink`, `rmtree`, `chdir`, `eval`, `exec`, `subprocess`.
- Read-only basename grouping. **PASS.**

### 2b. CI executing untrusted repo Python

- Fence string present (split across header lines 4–5).
- `check_overlap` absent from workflow. No `python tooling/...` step. **PASS.**

### 2c. Secrets in commits

- Secret-prefix scan on phase path diffs for tooling/CONTRACT/SUMMARY range: **0 hits** (AKIA, sk_live_, ghp_/gho_/github_pat_, xox*, BEGIN PRIVATE KEY, api_key=/password= patterns).
- `check_release` still runs LEAK_SENTINELS gate. **PASS.**

### 2d. False FUT-05 "full regen" claim

- CONTRACT §8 refuses byte-stable full-map generator; no generator file added. **PASS.**

### 2e. Whitelist hiding real collisions

- WHITELIST size == 1 (`ch01-introduction.md`).
- Live multi-pack chapter basenames == that single name; un-whitelisted collisions empty.
- New shared basename requires code edit to WHITELIST (reviewed), not runtime toggle. **PASS.**

### 2f. Gates still green (live)

```
OVERLAP: PASS
PASS: capability map OK  (TOTAL: 644)
RELEASE CHECK: PASS
OVERLAP_ASSERT_OK
```

---

## 3. SUMMARY.md `## Threat Flags` mapping

`17-01-SUMMARY.md` has **no** `## Threat Flags` section. No unregistered attack surface beyond declared T-17-01..SC. Unregistered-flag count: **0**.

Coordinator-listed surfaces map as:

| Brief item | Threat ID |
|---|---|
| Path traversal / unsafe file ops | covered by T-17-03 boundary + fixed-ROOT design (audit §2a) |
| CI untrusted repo Python | T-17-02 |
| Secrets in commits | audit §2c (phase leak scan; not a separate PLAN ID) |
| False FUT-05 full regen | T-17-05 |
| Whitelist hiding collisions | T-17-01 |

---

## 4. Notes (informational — no open threats)

- **N1 — Accept documentation.** Root `SECURITY.md` is vuln/licensing policy only. T-17-04 (low) and T-17-SC (high, no-install) acceptance live in PLAN disposition + this ACCEPTED row — same pattern as T-16-08 / T-15-*.
- **N2 — T-17-SC severity high but disposition accept.** Evidence: zero package-manager files/installs in phase; stdlib-only imports. Not reopened.
- **N3 — CI fence assert must split strings.** Full phrase spans two YAML comment lines; `'never' in t and 'executes checked-out repository code' in t` is the correct check (SUMMARY MJ-01).
- **N4 — check_overlap not on authored-header list.** Same as `check_capability_map`; intentional per plan. Not a security gap.
- **N5 — Live porcelain.** Orchestrator may touch `master_flow_state.json`. Not part of execution commit trees for overlap/CONTRACT.

---

## 5. Scope discipline

- Implementation / packs / CI: not modified by this audit.
- Wrote only this artifact: `.planning/phases/17-tooling-in-02-fut-05/17-SECURITY_AUDIT.md`.
- No MCP. No retag. No `git add -A`.

**Verdict:** SECURED — all declared threats CLOSED or ACCEPTED at declared boundaries; audit-brief checks pass; threats_open = 0.
