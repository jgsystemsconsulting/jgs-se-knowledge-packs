#!/usr/bin/env bash
# Copyright (c) 2026 JG Systems Consulting Ltd. — MIT License (see ../LICENSE).
# SPDX-License-Identifier: MIT
#
# configure_repo.sh — apply the RR-B publish-time PLATFORM state via the `gh` CLI.
#
# RR-B-20..23 configure GitHub platform state (Pages, About panel, Releases, branch
# protection) — not files in the tree — so they can't be verified by RR-B-00's
# "fix it in a tracked file" rule. This script makes that state reproducible and
# re-appliable instead of hand-clicked. It is idempotent: safe to re-run.
#
# Prerequisites: `gh auth login` (scopes: repo, workflow); run from anywhere.
# Usage:  scripts/configure_repo.sh            # apply everything
#         scripts/configure_repo.sh --dry-run  # print the gh calls, change nothing
set -euo pipefail

OWNER="jgsystemsconsulting"
REPO="jgs-se-knowledge-packs"
SLUG="$OWNER/$REPO"
PAGES_URL="https://$OWNER.github.io/$REPO/"
DEFAULT_BRANCH="main"
CI_CONTEXT="content-integrity"   # the job id in .github/workflows/validate.yml

# Version is the single source of truth (stager-equivalent: plugin.json).
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VERSION="$(grep -m1 '"version"' "$ROOT/.claude-plugin/plugin.json" | sed -E 's/.*"version" *: *"([^"]+)".*/\1/')"
TAG="v$VERSION"

DESCRIPTION="Curated, licence-vetted knowledge-pack skills for systems-engineering coding agents (Claude Code / Copilot CLI / Codex / Gemini / Cursor). Only genuinely open sources."
TOPICS=(agent-skills agent-skill skill-md claude-code github-copilot codex gemini-cli openclaw systems-engineering mbse knowledge-base open-source)

DRY=0; [ "${1:-}" = "--dry-run" ] && DRY=1
run() { if [ "$DRY" = 1 ]; then echo "  + $*"; else eval "$*"; fi; }

command -v gh >/dev/null || { echo "gh CLI not found — install + 'gh auth login' first." >&2; exit 1; }

echo "configure_repo.sh — $SLUG @ $TAG  $([ "$DRY" = 1 ] && echo '(dry-run)')"

# --- RR-B-21: About metadata (description, homepage, topics) ---
echo "[RR-B-21] About: description / homepage / topics"
run "gh repo edit '$SLUG' --description \"$DESCRIPTION\" --homepage '$PAGES_URL'"
run "gh repo edit '$SLUG' $(printf -- '--add-topic %s ' "${TOPICS[@]}")"

# --- RR-B-20: GitHub Pages from main:/docs ---
echo "[RR-B-20] Pages: serve from $DEFAULT_BRANCH /docs"
# Create-or-noop: POST returns 409 if already enabled; that's fine under idempotency.
run "gh api -X POST 'repos/$SLUG/pages' -f 'source[branch]=$DEFAULT_BRANCH' -f 'source[path]=/docs' >/dev/null 2>&1 || true"
run "gh api -X PUT  'repos/$SLUG/pages' -f 'source[branch]=$DEFAULT_BRANCH' -f 'source[path]=/docs' >/dev/null 2>&1 || true"

# --- RR-B-22: published GitHub Release for the current tag ---
echo "[RR-B-22] Release: $TAG (notes from CHANGELOG)"
# Extract the CHANGELOG section for this version as release notes.
NOTES_FILE="$(mktemp)"
awk "/^## \\[$VERSION\\]/{f=1;next} /^## \\[/{f=0} f" "$ROOT/CHANGELOG.md" > "$NOTES_FILE" || true
if [ "$DRY" = 1 ]; then
  echo "  + gh release create $TAG --title $TAG --notes-file <CHANGELOG section> (or 'release edit' if it exists)"
else
  if gh release view "$TAG" -R "$SLUG" >/dev/null 2>&1; then
    gh release edit "$TAG" -R "$SLUG" --notes-file "$NOTES_FILE"
  else
    gh release create "$TAG" -R "$SLUG" --title "$TAG" --notes-file "$NOTES_FILE"
  fi
fi
rm -f "$NOTES_FILE"

# --- RR-B-23: default-branch protection (PR + green CI; no force-push/delete) ---
echo "[RR-B-23] Branch protection on $DEFAULT_BRANCH"
PROT_JSON="$(cat <<JSON
{
  "required_status_checks": { "strict": true, "contexts": ["$CI_CONTEXT"] },
  "enforce_admins": false,
  "required_pull_request_reviews": { "required_approving_review_count": 0 },
  "restrictions": null,
  "allow_force_pushes": false,
  "allow_deletions": false
}
JSON
)"
if [ "$DRY" = 1 ]; then
  echo "  + gh api -X PUT repos/$SLUG/branches/$DEFAULT_BRANCH/protection  (PR + CI '$CI_CONTEXT', no force-push/delete)"
else
  echo "$PROT_JSON" | gh api -X PUT "repos/$SLUG/branches/$DEFAULT_BRANCH/protection" \
    -H "Accept: application/vnd.github+json" --input - >/dev/null
fi

echo "Done. Verify: gh repo view $SLUG --json description,homepageUrl,repositoryTopics ; gh release view $TAG -R $SLUG ; gh api repos/$SLUG/pages --jq .html_url"
