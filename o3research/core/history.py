import json
from pathlib import Path
from typing import List


class History:
    """Simple persistent history of messages."""

    def __init__(self, file_path: str | Path, entries: List[str] | None = None) -> None:
        self.file_path = Path(file_path)
        self.entries: List[str] = entries or []

    @classmethod
    def load(cls, file_path: str | Path) -> "History":
        path = Path(file_path)
        if path.exists():
            data = json.loads(path.read_text())
            if not isinstance(data, list):
                raise ValueError("History data must be a list")
            entries = [str(item) for item in data]
        else:
            entries = []
        return cls(file_path, entries)

    def add(self, message: str) -> None:
        self.entries.append(message)

    def save(self) -> None:
        self.file_path.write_text(json.dumps(self.entries))
