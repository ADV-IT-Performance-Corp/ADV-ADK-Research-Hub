import os
from typing import Any, Callable, List, Dict


class TelemetryClient:
    """Simple telemetry client that buffers events until flushed."""

    def __init__(self, collector: Callable[[Dict[str, Any]], None]) -> None:
        self.collector = collector
        self._buffer: List[Dict[str, Any]] = []

    def log_event(
        self,
        event: Dict[str, Any],
        *,
        timing: float | None = None,
        cost: float | None = None,
    ) -> None:
        """Add *event* to the buffer if telemetry is enabled.

        Optional ``timing`` and ``cost`` values are inserted into the event
        dictionary when provided.
        """
        if timing is not None:
            event["timing"] = timing
        if cost is not None:
            event["cost"] = cost
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


# -- Prompt Observability Helpers -------------------------------------------------

# Global telemetry client used for prompt logging. The default collector simply
# ignores events until configured by the application or tests.
_prompt_client = TelemetryClient(lambda _event: None)


def configure_prompt_collector(collector: Callable[[Dict[str, Any]], None]) -> None:
    """Set the collector for prompt telemetry events."""
    global _prompt_client
    _prompt_client = TelemetryClient(collector)


def get_prompt_client() -> "TelemetryClient":
    """Return the global prompt telemetry client."""
    return _prompt_client


def log_prompt(
    prompt_id: str,
    agent_name: str,
    tokens: int,
    *,
    timing: float | None = None,
    cost: float | None = None,
) -> None:
    """Record a prompt event with token count and optional metrics."""
    event = {
        "type": "prompt",
        "prompt_id": prompt_id,
        "agent_name": agent_name,
        "tokens": tokens,
    }
    _prompt_client.log_event(event, timing=timing, cost=cost)
