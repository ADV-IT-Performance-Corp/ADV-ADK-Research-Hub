from __future__ import annotations

import time
from typing import Dict

from ..core.base_agent import BaseAgent

class GovernanceAgent(BaseAgent):
    """Prototype agent to monitor other agents and handle escalation."""

    def __init__(self) -> None:
        super().__init__(name="GovernanceAgent")
        self._heartbeats: Dict[str, float] = {}

    def record_heartbeat(self, agent_name: str) -> None:
        """Record a heartbeat timestamp for another agent."""
        self._heartbeats[agent_name] = time.time()

    def run(self, status: str) -> str:
        now = time.time()
        stale = [name for name, ts in self._heartbeats.items() if now - ts > 30]
        if stale:
            agents = ", ".join(stale)
            return f"{self.name} ALERT: {agents} heartbeat stale"
        return f"{self.name} reviewed status: {status}"

if __name__ == "__main__":
    agent = GovernanceAgent()
    print(agent.run("ok"))
