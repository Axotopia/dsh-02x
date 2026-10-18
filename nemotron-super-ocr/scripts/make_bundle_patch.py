#!/usr/bin/env python3
"""make_bundle_patch.py - regenerate cordis.patch.yml from agent.cordis.yml.

The bundle patch is a thin wrapper: one @deepseek-ai/dsh-agent-preset insert
whose `plugins` is agent.cordis.yml verbatim, indented under the declaration.
Keeping it generated avoids the two files drifting apart.

Usage: py make_bundle_patch.py <preset-bundle-dir>
"""
import sys
from pathlib import Path

HEADER = """\
# nemotron-super-ocr — DSH 0.2.x bundle patch.
#
# GENERATED from ./agent.cordis.yml by make_bundle_patch.py — edit the entry
# list there, then regenerate this file. The `plugins` list below is that file
# verbatim (re-indented), so the bundle and the reference copy cannot drift.
"""

WRAPPER = """\
- insert:
    - id: preset-{pid}
      name: '@deepseek-ai/dsh-agent-preset'
      config:
        id: {pid}
        name: "{name}"
        description: "{desc}"
        order: {order}
        plugins:
"""


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    entries = (root / "agent.cordis.yml").read_text(encoding="utf-8").rstrip("\n")
    body = "\n".join(("          " + line) if line.strip() else "" for line in entries.splitlines())

    import yaml  # only to read preset.yml
    meta = yaml.safe_load((root / "preset.yml").read_text(encoding="utf-8"))
    desc = " ".join(str(meta.get("description", "")).split())
    out = HEADER + WRAPPER.format(pid="nemotron-super-ocr", name=meta["name"],
                                  desc=desc.replace('"', "'"),
                                  order=meta.get("order", 35)) + body + "\n"
    (root / "cordis.patch.yml").write_text(out, encoding="utf-8")
    print("wrote", root / "cordis.patch.yml", len(out), "bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
