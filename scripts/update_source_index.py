#!/usr/bin/env python3
# limit_output
"""Regenerate docs/source_index.json from external doc stubs."""
import json
import os
import re
import datetime
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from limited_io import _LimitedIO  # noqa: E402


sys.stdout = _LimitedIO(sys.stdout)
sys.stderr = _LimitedIO(sys.stderr)

ROOT = os.path.join("docs", "external")


def parse_stub(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    name_match = re.search(r"^#\s+(.*)", text, re.MULTILINE)
    url_match = re.search(r"\*\*URL:\*\*\s*(\S+)", text)
    rel_match = re.search(r"\*\*Relevance:\*\*\s*([^\n]+)", text)
    used_match = re.search(r"\*\*Used by Agents:\*\*\s*([^\n]+)", text)
    desc_match = re.search(r"## Description\n([^\n]+)", text)
    name = name_match.group(1).strip() if name_match else os.path.basename(path)[:-3]
    url = url_match.group(1).strip() if url_match else ""
    tags = (
        [t.strip() for t in re.split(r"[ ,]+", rel_match.group(1).strip())]
        if rel_match
        else []
    )
    used = (
        [u.strip() for u in re.split(r"[ ,]+", used_match.group(1).strip())]
        if used_match
        else []
    )
    description = desc_match.group(1).strip() if desc_match else ""
    return {
        "name": name,
        "link": url,
        "description": description,
        "used_by": used,
        "tags": tags,
        "last_reviewed": datetime.date.today().isoformat(),
        "type": "external",
    }


def collect_existing_core(index_path):
    with open(index_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    core = [s for s in data.get("sources", []) if s.get("type") != "external"]
    meta = data.get("metadata", {})
    return core, meta


def main():
    index_path = os.path.join("docs", "source_index.json")
    core_sources, meta = collect_existing_core(index_path)
    ext_sources = []
    names_seen = set()
    links_seen = set()
    for root, _, files in os.walk(ROOT):
        for fname in files:
            if not fname.endswith(".md"):
                continue
            stub = parse_stub(os.path.join(root, fname))
            name = stub.get("name")
            link = stub.get("link")
            if name in names_seen or (link and link in links_seen):
                continue
            names_seen.add(name)
            if link:
                links_seen.add(link)
            ext_sources.append(stub)
    meta["last_updated"] = datetime.date.today().isoformat()
    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(
            {
                "sources": core_sources + sorted(ext_sources, key=lambda x: x["name"]),
                "metadata": meta,
            },
            f,
            indent=2,
        )


if __name__ == "__main__":
    main()
