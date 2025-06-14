from __future__ import annotations

__version__ = "4.0.0"

import time
from typing import Dict

from google.adk import Agent
from o3research.lifecycle import finish_run, start_run
from pydantic import ConfigDict


class GovernanceAgent(Agent):
    model_config = ConfigDict(extra="allow")
    """Prototype agent to monitor other agents and handle escalation."""

    def __init__(self) -> None:
        super().__init__(name="GovernanceAgent")
        self._heartbeats: Dict[str, float] = {}

    def record_heartbeat(self, agent_name: str, timestamp: float | None = None) -> None:
        """Record a heartbeat timestamp for another agent."""
        self._heartbeats[agent_name] = timestamp or time.time()

    def run(self, status: str) -> str:
        start_run(self.name)
        try:
            now = time.time()
            stale = [name for name, ts in self._heartbeats.items() if now - ts > 30]
            if stale:
                agents = ", ".join(stale)
                return f"{self.name} ALERT: {agents} heartbeat stale"
            return f"{self.name} reviewed status: {status}"
        finally:
            finish_run(self.name)


if __name__ == "__main__":
    agent = GovernanceAgent()
    print(agent.run("ok"))
