from typing import Dict, Optional


class SemanticCache:
    """Simple in-memory cache using a dictionary."""

    def __init__(self) -> None:
        self._cache: Dict[str, str] = {}

    def get(self, key: str) -> Optional[str]:
        return self._cache.get(key)

    def set(self, key: str, value: str) -> None:
        self._cache[key] = value
