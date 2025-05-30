import json, re, datetime
from pathlib import Path

base = Path('docs/external')
new_sources = []
for md in base.rglob('*.md'):
    content = md.read_text().splitlines()
    name = content[0].lstrip('# ').strip()
    url = ''
    tags = []
    used_by = []
    for line in content:
        if line.startswith('**URL:**'):
            url = line.split('**URL:**')[1].strip()
        elif line.startswith('**Relevance:**'):
            tags = [t.strip() for t in line.split('**Relevance:**')[1].split(',')]
        elif line.startswith('**Used by Agents:**'):
            used_by = [a.strip() for a in line.split('**Used by Agents:**')[1].split(',')]
    new_sources.append({
        "name": name,
        "link": url,
        "tags": tags,
        "type": "external",
        "used_by": used_by,
        "last_reviewed": datetime.date.today().isoformat(),
    })

index_path = Path('docs/source_index.json')
index = json.loads(index_path.read_text())
core = [s for s in index["sources"] if s.get("type") != "external"]
index["sources"] = core + new_sources
index.setdefault("metadata", {})["last_updated"] = datetime.date.today().isoformat()
index_path.write_text(json.dumps(index, indent=2) + "\n")
print(f"Updated {index_path} with {len(new_sources)} external sources")
