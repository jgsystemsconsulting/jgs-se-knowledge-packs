---
phase: 5-release-surface-v1-17-0
audit: security
target: release commit bcd32af + annotated tag v1.17.0 + GitHub Release v1.17.0
date: 2026-08-15
asvs_level: 2
block_on: high
---

# Phase 5 Security Audit — v1.17.0 Release Surface

**Verdict:** SECURED_WITH_NOTES

**Threats Closed:** 5/5 | **threats_open:** 0 | **ASVS Level:** 2 (mitigation verified present AND at the correct boundary)

Audit subject is the public release act: release commit `bcd32af` (`release(v1.17.0): 8 Tier-1 public-domain packs (54 +2 signposts)`), annotated tag `v1.17.0`, and GitHub Release `v1.17.0`. Every mitigation was re-verified against the live artifacts (git objects, tag tree, `gh release view`, gate re-run) — not against SUMMARY claims.

## Threat Verification

| Threat ID | Category | Severity | Disposition | Status | Evidence |
|-----------|----------|----------|-------------|--------|----------|
| T-5-01 | Tampering (staging) | high | mitigate | CLOSED | `git show --name-only bcd32af`: exactly the 10 declared files. `docs/ROLE-AGENTS-REQUIREMENTS-V2.md`, `docs/capability-pack-map.md`, `docs/capability-pack-map.json` absent from commit AND from tag tree (`git ls-tree bcd32af -- <files>` empty); still untracked in working tree now. No `git add -A` blast radius. |
| T-5-02 | Repudiation (tag provenance) | medium | mitigate | CLOSED | `git cat-file -t v1.17.0` → `tag` (annotated, not lightweight); message `v1.17.0: 8 Tier-1 public-domain packs (54 +2 signposts)` colon-style per v1.16.3 convention; peels to `bcd32af` (`git rev-parse v1.17.0^{}`); both tag and peeled refs confirmed on origin via `git ls-remote --tags origin`. Release commit remains last content commit on main (post-tag commits `fab28bd`, `d99c348`, `85f4e5d` touch only `.planning/`). |
| T-5-03 | Tampering (OneDrive sync lag) | medium | mitigate | CLOSED | Commit message body embeds pre-commit gate evidence (`python tooling/check_release.py: RELEASE CHECK: PASS`). Live re-run during this audit: exit 0, `RELEASE CHECK: PASS` on a content-identical tree (`git diff --name-only v1.17.0 HEAD` = `.planning/` only). No drift between tagged content and working tree. |
| T-5-04 | Information disclosure (link policy) | low | mitigate | CLOSED | `tooling/check_release.py:47` `SOURCE_HOSTS` regex scans CHANGELOG.md (in `text_files`, not in `SKIP_DIRS`) — mitigation at the correct boundary. Gate PASS. Em-dash count in `## [1.17.0]` entry: 0. Entry contains zero `http` URLs. Full-diff URL scan of `bcd32af` shows only own-repo / shields.io / keepachangelog / semver URLs on context or version-bump lines. |
| T-5-05 | DoS of release (red gate) | high | mitigate | CLOSED | Tag exists on `bcd32af` (the commit whose body records gate PASS). Independent basis verified at the tag itself: `git show v1.17.0:catalog.json` → 54 packs; `git ls-tree v1.17.0:packs` → 56 dirs. Gate re-run live: exit 0 PASS. |

## Scope Checks (audit charter)

1. **Release commit contains nothing sensitive — PASS.** Full diff (`git show bcd32af`, 244 lines) scanned for credential patterns (`ghp_`, `AKIA`, `sk_live`, `xox`, `BEGIN PRIVATE KEY`, `api_key`, `password`, `secret`, `token`, `Bearer`): only false positives (`ri`**`sk-i`**`nformed`, `~2,000 `**`token`**`s`). PII scan (emails, phone patterns, distribution markers): sole email is the author's GitHub `noreply` address in commit metadata. All URLs are repo-infrastructure (own repo, badges, changelog/versioning standards); zero source-material URLs.
2. **GitHub Release notes contain no source-material URLs — PASS.** `gh release view v1.17.0 --json body`: zero `http(s)://` matches, zero secret patterns, zero em dashes in body. (Title `v1.17.0 — 8 Tier-1 public-domain packs` em dash was explicitly specified by plan Task 6.)
3. **Link policy still enforced — PASS.** `python tooling/check_release.py` → exit 0, `RELEASE CHECK: PASS`. CHANGELOG is inside the scanned set (verified in source, not assumed).
4. **No untracked user docs published — PASS.** The three user docs are absent from the release commit, the tag tree, and remain untracked (`git status`).
5. **Licence compliance unchanged — PASS.** `git show --name-only bcd32af` contains zero content/licence paths (no `packs/`, `sources/`, `NOTICE`, `LICENSE`, `COPYRIGHT`, `catalog.json`, `SKILLS.md`); commit is docs/metadata only. `git diff v1.17.0 HEAD -- NOTICE LICENSE COPYRIGHT catalog.json SKILLS.md` is empty — licence surfaces identical between tag and HEAD. Catalog at tag = 54 packs / 56 dirs, matching the declared basis.

## Unregistered Flags

SUMMARY.md (5-01-SUMMARY.md) contains no `## Threat Flags` section; no new attack surface introduced by implementation. Untracked-flag count: 0.

## Notes (informational — no action required for this release)

1. **Branch-protection bypass notice on push (from SUMMARY "Issues Encountered").** The release push to `main` reported a branch-protection bypass notice. The releasing identity can bypass `main` protection, so the annotated tag is the tamper-evidence control (T-5-02), not branch rules. Not phase-introduced attack surface and no declared threat covers repo governance — recorded for v1.18 planning: consider enforced branch protection or a required release workflow.
2. **Bare source-host domain names in CHANGELOG and release notes.** `CHANGELOG.md:56` and the release-notes body mention `cisa.gov, energy.gov, nde-ed.org, everyspec.com` as plain prose (policy-extension bullet). The gate's `SOURCE_HOSTS` regex only matches URLs with a scheme, so this is policy-conformant — domains are named, not linked. Recorded so future audits do not misread it as a link-policy violation.
3. **Temp release-notes file left no residue.** The Windows fallback path `.planning/phases/5-release-surface-v1-17-0/_v1.17.0-notes.md` (SUMMARY deviation 4) is absent from the working tree and from all commit history (`git log --all` on the path: empty).

## Method

Git-object-level verification (`git show`, `ls-tree`, `cat-file`, `rev-parse`, `ls-remote`), live `gh release view v1.17.0`, live `python tooling/check_release.py` re-run, pattern scans of the full 244-line release diff, and boundary analysis of `tooling/check_release.py` scan scope (SKIP_DIRS vs text_files). Implementation files were read-only; no app/pack/tooling files modified.

---
*Audit artifact — Phase 5, v1.17.0 release surface.*
