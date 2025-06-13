#!/usr/bin/env python3
# limit_output
"""Scaffold a marketing workflow prompt and matching meta file."""

import sys
from datetime import date
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from limited_io import _LimitedIO  # noqa: E402


sys.stdout = _LimitedIO(sys.stdout)
sys.stderr = _LimitedIO(sys.stderr)


def main():
    if len(sys.argv) != 2:
        print("Usage: new_prompt.py <prompt_name>")
        sys.exit(1)
    name = sys.argv[1].strip().lower().replace(" ", "_")
    root = Path("prompt_catalog")
    root.mkdir(exist_ok=True)

    md_path = root / f"{name}.md"
    meta_path = root / f"{name}.meta.yaml"

    if md_path.exists() or meta_path.exists():
        print("Prompt files already exist", file=sys.stderr)
        sys.exit(1)

    title = name.replace("_", " ").title()
    md_content = (
        f"# {title} Workflow\n\n"
        f"Describe the {name.replace('_', ' ')} workflow here.\n"
    )
    md_path.write_text(md_content)

    meta_content = (
        "---\n"
        f"description: Guidance for {name.replace('_', ' ')}\n"
        "adk_agent_type: marketing_assistant\n"
        "input_schema: generic\n"
        "output_contract: standard\n"
        'language: "en"\n'
        "version: 1.0\n"
        "access_level: public\n"
        "encryption_required: false\n"
        f"last_updated: {date.today()}\n"
    )
    meta_path.write_text(meta_content)
    print(f"Created {md_path} and {meta_path}")


if __name__ == "__main__":
    main()
