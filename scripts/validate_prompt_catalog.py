#!/usr/bin/env python3
"""Validate prompt catalog metadata."""

import sys
from pathlib import Path
import yaml


def main():
    root = Path("prompt_catalog")
    if not root.exists():
        print("prompt_catalog directory missing", file=sys.stderr)
        return
    required = [
        "description",
        "adk_agent_type",
        "input_schema",
        "output_contract",
        "language",
        "version",
        "access_level",
        "encryption_required",
        "last_updated",
    ]
    ok = True
    for md in root.glob("*.md"):
        meta = md.with_suffix(".meta.yaml")
        if not meta.exists():
            print(f"Missing meta for {md}")
            ok = False
            continue
        data = yaml.safe_load(meta.read_text())
        for key in required:
            if key not in data:
                print(f"{meta} missing field {key}")
                ok = False
    if not ok:
        sys.exit(1)
    print("Prompt catalog validation passed")


if __name__ == "__main__":
    main()
