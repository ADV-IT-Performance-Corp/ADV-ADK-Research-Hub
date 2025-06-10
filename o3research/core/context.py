from typing import Any, Dict


class Context:
    """Simple key-value store for sharing data between components."""

    def __init__(self, initial: Dict[str, Any] | None = None) -> None:
        if initial is not None and not isinstance(initial, dict):
            raise TypeError("initial must be a dict")
        self._data: Dict[str, Any] = dict(initial or {})

    def update(self, data: Dict[str, Any]) -> None:
        if not isinstance(data, dict):
            raise TypeError("data must be a dict")
        self._data.update(data)

    def get(self, key: str, default: Any = None) -> Any:
        return self._data.get(key, default)

    def __getitem__(self, key: str) -> Any:
        return self._data[key]

    def __contains__(self, key: str) -> bool:
        return key in self._data

    def to_dict(self) -> Dict[str, Any]:
        return dict(self._data)
