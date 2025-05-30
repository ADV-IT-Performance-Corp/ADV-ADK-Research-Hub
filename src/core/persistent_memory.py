from __future__ import annotations

import json
from pathlib import Path
from typing import Any

class PersistentMemory:
    """Simple file-backed key-value store for agent memory."""

    def __init__(self, path: str = "memory.json") -> None:
        self.path = Path(path)
        if self.path.exists():
            self.data = json.loads(self.path.read_text())
        else:
            self.data = {}

    def get(self, key: str, default: Any = None) -> Any:
        return self.data.get(key, default)

    def set(self, key: str, value: Any) -> None:
        self.data[key] = value
        self.path.write_text(json.dumps(self.data, indent=2))
