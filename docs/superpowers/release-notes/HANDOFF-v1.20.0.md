# v1.20.0 ship handoff (pending user execution)

Date: 2026-09-14. Package: P8 (phase 21 planning-ledger close). The execution-time
user gate went unanswered, so the publish did not run and the package stops here.

## Ledger posture

The wave-1 ledger posture is in effect: the planning ledger is closed and ship
pending. No shipped claim exists on any surface. Wave 2 (URL backfills) has not
run.

Ready state at handoff: main is ahead of origin/main (`55ef575`) by 29 commits,
0 behind; HEAD is `5b2183c`. Annotated tag `v1.20.0` peels to `ffe385a`; the tag
and the GitHub Release are absent on origin.
`docs/superpowers/release-notes/v1.20.0.md` is written from CHANGELOG [1.20.0].

## Publish commands (run in order, from the repo root)

    git push origin main
    git push origin v1.20.0
    gh release create v1.20.0 --title "v1.20.0: FUT-05 byte-stable capability-map generator" --notes-file docs/superpowers/release-notes/v1.20.0.md

Order is load-bearing: `main` first so the tagged commit is reachable, then the
annotated tag (pushing cannot move it off `ffe385a`), then the release.

Attempted 2026-09-15: `git push origin main` failed with 403 — the active
credential is `systems-researcher`, which has no push permission to this repo.
Re-run from an account with write access (or fix the credential helper), then
continue with commands 2 and 3. Nothing was published; local state unchanged.

## After publishing: wave 2 backfills

Once the release exists, run the wave-2 URL backfills per tasks 6-7 of
`docs/superpowers/plans/2026-09-14-phase21-planning-ledger-close.md`: backfill
the release URL into STATE, ROADMAP, MILESTONES, PROJECT, and REQUIREMENTS, and
the phase `master_flow` pending-release notes. Never backfill wave 2 without the
release existing.
