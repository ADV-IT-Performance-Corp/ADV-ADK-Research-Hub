#!/usr/bin/env python3
"""Regenerate docs/source_index.json from markdown stubs."""
import json
import os
import re
from datetime import date

root = os.path.dirname(os.path.dirname(__file__))
external_dir = os.path.join(root, 'docs', 'external')
json_path = os.path.join(root, 'docs', 'source_index.json')

pattern_url = re.compile(r"\*\*URL:\*\*\s*(\S+)")
pattern_relevance = re.compile(r"\*\*Relevance:\*\*\s*(.+)")
pattern_agents = re.compile(r"\*\*Used by Agents:\*\*\s*(.+)")

sources = []
for dirpath, _, filenames in os.walk(external_dir):
    for name in filenames:
        if not name.endswith('.md'):
            continue
        path = os.path.join(dirpath, name)
        with open(path, 'r') as f:
            lines = f.read().splitlines()
        if not lines:
            continue
        title = lines[0].lstrip('# ').strip()
        url = ''
        relevance = []
        agents = []
        for line in lines:
            m = pattern_url.search(line)
            if m:
                url = m.group(1)
            m = pattern_relevance.search(line)
            if m:
                relevance = [t.strip() for t in m.group(1).split(',')]
            m = pattern_agents.search(line)
            if m:
                agents = [a.strip() for a in m.group(1).split(',')]
        sources.append({
            "name": title,
            "link": url,
            "tags": relevance,
            "used_by": agents,
            "type": "external",
            "last_reviewed": str(date.today())
        })

with open(json_path) as f:
    data = json.load(f)

# Remove existing external entries
core_sources = [s for s in data["sources"] if s.get("type") != "external"]

data["sources"] = core_sources + sources
data["metadata"]["last_updated"] = str(date.today())

with open(json_path, 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
    f.write('\n')
