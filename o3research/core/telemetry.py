import os
from typing import Any, Callable, List, Dict


class TelemetryClient:
    """Simple telemetry client that buffers events until flushed."""

    def __init__(self, collector: Callable[[Dict[str, Any]], None]) -> None:
        self.collector = collector
        self._buffer: List[Dict[str, Any]] = []

    def log_event(self, event: Dict[str, Any]) -> None:
        """Add *event* to the buffer if telemetry is enabled."""
        if os.environ.get("TELEMETRY_ENABLED") == "1":
            self._buffer.append(event)

    def flush(self) -> None:
        """Send buffered events to the collector and clear the buffer."""
        for event in self._buffer:
            self.collector(event)
        self._buffer.clear()

    @property
    def buffer(self) -> List[Dict[str, Any]]:
        """Return a copy of the current event buffer."""
        return list(self._buffer)
