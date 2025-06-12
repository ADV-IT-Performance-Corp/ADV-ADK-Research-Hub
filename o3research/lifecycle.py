from __future__ import annotations

"""Lightweight wrappers for ADK lifecycle hooks."""

try:
    from google.adk.lifecycle import start as adk_start, end as adk_end  # type: ignore
except Exception:  # pragma: no cover - optional dep

    def adk_start(_name: str) -> None:
        pass

    def adk_end(_name: str) -> None:
        pass


def start_run(agent_name: str) -> None:
    """Signal that *agent_name* started processing."""
    adk_start(agent_name)


def finish_run(agent_name: str) -> None:
    """Signal that *agent_name* finished processing."""
    adk_end(agent_name)
