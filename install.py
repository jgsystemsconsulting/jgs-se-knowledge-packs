#!/usr/bin/env python3
# Copyright (c) 2026 JG Systems Consulting Ltd. — MIT License (see LICENSE).
# SPDX-License-Identifier: MIT
"""
install.py — install the jgs-se-knowledge-packs catalogue into a coding agent.

Each pack under packs/<slug>/ is an Agent Skill (a SKILL.md plus supporting files).
This installer copies / transforms the packs into the target agent's skills (or
prompt/command/rule) directory so they load as `/slug` (or the agent's equivalent).

Multi-agent (RR-S-15): the packs follow the open agentskills.io SKILL.md format.
Some agents read that format NATIVELY (the pack folder is copied unchanged); others
need a FORMAT TRANSFORM into their own prompt/rule convention (the SKILL.md index is
inlined into a single prompt/command/rule file).

Usage:
    python install.py --dry-run             # preview packs + target, copy nothing
    python install.py                       # install for Claude Code (default)
    python install.py --agent openclaw      # install for a specific agent
    python install.py --agent all           # install for all user-global agents
    python install.py --list-agents         # list supported agents + their targets
    python install.py --flat                # (Claude/native) drop the vendor namespace
    python install.py --target DIR          # override the agent's skills directory

Native agents (folder copied unchanged, full progressive disclosure):
    claude    ~/.claude/skills/<ns>/<slug>/         (honours $CLAUDE_CONFIG_DIR)
    openclaw  ~/.openclaw/skills/<ns>/<slug>/
    copilot   ~/.copilot/skills/<ns>/<slug>/

Transform agents (SKILL.md index inlined into one file — see docs/other-agents.md):
    codex     ~/.codex/prompts/<slug>.md           (top-level prompt)
    gemini    ~/.gemini/commands/<ns>/<slug>.toml  (TOML command)
    cursor    ./.cursor/rules/<slug>.mdc           (PROJECT-local rule; excluded from --agent all)

No third-party dependencies — stdlib only.
"""
from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path

VENDOR = "jgs-se-knowledge-packs"
REPO_ROOT = Path(__file__).resolve().parent
PACKS_DIR = REPO_ROOT / "packs"

# Agent registry. kind: "native" (copy folder) or "transform" (inline SKILL.md).
# root: base dir (relative to ~ unless project-local); env: optional config-dir override var.
AGENTS: dict[str, dict] = {
    "claude":   {"kind": "native",    "root": ".claude/skills",   "env": "CLAUDE_CONFIG_DIR", "global": True,  "label": "Claude Code"},
    "openclaw": {"kind": "native",    "root": ".openclaw/skills", "env": None,                "global": True,  "label": "OpenClaw"},
    "copilot":  {"kind": "native",    "root": ".copilot/skills",  "env": None,                "global": True,  "label": "GitHub Copilot CLI"},
    "codex":    {"kind": "transform", "fmt": "prompt", "root": ".codex/prompts",   "env": None, "global": True,  "label": "OpenAI Codex CLI"},
    "gemini":   {"kind": "transform", "fmt": "toml",   "root": ".gemini/commands", "env": None, "global": True,  "label": "Gemini CLI"},
    "cursor":   {"kind": "transform", "fmt": "mdc",    "root": ".cursor/rules",    "env": None, "global": False, "label": "Cursor (project-local)"},
}


def discover_packs() -> list[Path]:
    """Every packs/<slug>/ that contains a SKILL.md is an installable pack."""
    if not PACKS_DIR.is_dir():
        return []
    return sorted(p for p in PACKS_DIR.iterdir() if p.is_dir() and (p / "SKILL.md").is_file())


def read_skill_md(pack: Path) -> tuple[dict, str]:
    """Return (frontmatter dict, body) for a pack's SKILL.md. Minimal YAML — top-level scalars only."""
    text = (pack / "SKILL.md").read_text(encoding="utf-8")
    fm: dict[str, str] = {}
    body = text
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            block = text[3:end]
            body = text[end + 4:].lstrip("\n")
            key = None
            for line in block.splitlines():
                if line and line[0] not in " \t" and ":" in line:
                    key, _, val = line.partition(":")
                    key = key.strip()
                    fm[key] = val.strip().strip('"').strip("'")
    return fm, body


def base_for(agent: str, override: str | None, flat: bool) -> Path:
    """Resolve the install base directory for a native agent."""
    spec = AGENTS[agent]
    if override:
        root = Path(override).expanduser().resolve()
    elif spec["env"] and os.environ.get(spec["env"]):
        root = (Path(os.environ[spec["env"]]).expanduser() / "skills").resolve()
    elif agent == "cursor":
        root = (Path.cwd() / ".cursor" / "rules").resolve()
    else:
        root = (Path.home() / spec["root"]).resolve()
    if spec["kind"] == "native":
        return root if flat else root / VENDOR
    return root  # transform agents: files land directly (namespaced per-file where noted)


def transform_to(agent: str, pack: Path, fm: dict, body: str) -> tuple[Path, str]:
    """Return (relative filename, file content) for a transform agent's single-file format."""
    slug = pack.name
    desc = fm.get("description", "").replace('"', "'")
    spec = AGENTS[agent]
    note = (
        f"<!-- jgs-se-knowledge-packs: '{slug}' transformed for {spec['label']} from the "
        "agentskills.io SKILL.md. On-demand chapter loading is a Claude-native feature; this "
        "single-file form inlines the always-loaded index. See docs/other-agents.md. -->\n\n"
    )
    if spec["fmt"] == "prompt":          # Codex: ~/.codex/prompts/<slug>.md
        return Path(f"{slug}.md"), note + body
    if spec["fmt"] == "mdc":             # Cursor: ./.cursor/rules/<slug>.mdc
        head = f"---\ndescription: {desc}\nglobs:\nalwaysApply: false\n---\n\n"
        return Path(f"{slug}.mdc"), head + note + body
    if spec["fmt"] == "toml":            # Gemini: ~/.gemini/commands/<ns>/<slug>.toml
        esc = body.replace("\\", "\\\\").replace('"""', '\\"\\"\\"')
        toml = f'description = "{desc}"\n\nprompt = """\n{note}{esc}\n"""\n'
        return Path(VENDOR) / f"{slug}.toml", toml
    raise ValueError(f"unknown transform fmt for {agent}")


def install_native(agent: str, packs: list[Path], base: Path, dry: bool) -> None:
    for p in packs:
        dest = base / p.name
        if dry:
            print(f"  would install  {p.name:<24} -> {dest}")
            continue
        if dest.exists():
            shutil.rmtree(dest)
        shutil.copytree(p, dest)
        print(f"  installed  {p.name:<24} -> {dest}")


def install_transform(agent: str, packs: list[Path], base: Path, dry: bool) -> None:
    for p in packs:
        fm, body = read_skill_md(p)
        rel, content = transform_to(agent, p, fm, body)
        dest = base / rel
        if dry:
            print(f"  would write    {p.name:<24} -> {dest}")
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(content, encoding="utf-8")
        print(f"  wrote      {p.name:<24} -> {dest}")


def install_for_agent(agent: str, packs: list[Path], override: str | None, flat: bool, dry: bool) -> None:
    spec = AGENTS[agent]
    base = base_for(agent, override, flat)
    print(f"[{agent}] {spec['label']}  ({spec['kind']})")
    print(f"  target  : {base}{'  (flat)' if flat and spec['kind'] == 'native' else ''}")
    if spec["kind"] == "native":
        install_native(agent, packs, base, dry)
    else:
        install_transform(agent, packs, base, dry)
    print()


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Install jgs-se-knowledge-packs into a coding agent.")
    ap.add_argument("--agent", default="claude",
                    help="target agent: " + ", ".join(AGENTS) + ", or 'all' (user-global agents). Default: claude")
    ap.add_argument("--list-agents", action="store_true", help="list supported agents and their targets, then exit")
    ap.add_argument("--dry-run", action="store_true", help="show what would be installed, copy nothing")
    ap.add_argument("--flat", action="store_true", help="(native agents) install packs directly under <skills>/ (no vendor namespace)")
    ap.add_argument("--target", help="override the target directory (single agent only)")
    args = ap.parse_args(argv[1:])

    if args.list_agents:
        print("Supported agents (RR-S-15):")
        for name, spec in AGENTS.items():
            scope = "user-global" if spec["global"] else "project-local"
            print(f"  {name:<9} {spec['label']:<22} {spec['kind']:<9} {scope}  base ~/{spec['root']}")
        print("\n'--agent all' installs every user-global agent (cursor is project-local, run it explicitly).")
        return 0

    packs = discover_packs()
    if not packs:
        print("No packs found under packs/.", file=sys.stderr)
        return 1

    if args.agent == "all":
        targets = [a for a, s in AGENTS.items() if s["global"]]
        if args.target:
            print("--target cannot be combined with --agent all.", file=sys.stderr)
            return 1
    elif args.agent in AGENTS:
        targets = [args.agent]
    else:
        print(f"Unknown agent '{args.agent}'. Try --list-agents.", file=sys.stderr)
        return 1

    print("jgs-se-knowledge-packs installer")
    print(f"  packs found : {len(packs)}  ({', '.join(p.name for p in packs)})")
    print(f"  agents      : {', '.join(targets)}")
    print()

    for agent in targets:
        install_for_agent(agent, packs, args.target, args.flat, args.dry_run)

    if args.dry_run:
        print("Dry run — nothing written. Re-run without --dry-run to install.")
    else:
        print(f"Installed {len(packs)} pack(s) for {len(targets)} agent(s). "
              f"Restart your agent, then invoke a pack by its slug, e.g. /{packs[0].name}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
