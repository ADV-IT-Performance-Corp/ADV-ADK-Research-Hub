from core.base_agent import BaseAgent
from core import EventBus

import time

class GovernanceAgent(BaseAgent):
    """Monitor other agents and handle heartbeats."""

    def __init__(self, bus: EventBus, timeout: float = 30.0) -> None:
        super().__init__(name="GovernanceAgent")
        self.bus = bus
        self.timeout = timeout
        self.last_seen: dict[str, float] = {}
        self.bus.subscribe("heartbeat", self._record_heartbeat)

    def _record_heartbeat(self, message: str) -> None:
        agent, ts = message.split(":", 1)
        self.last_seen[agent] = float(ts)

    def run(self, status: str) -> str:
        missing = self._check_agents()
        if missing:
            return f"{self.name} escalation: missing {', '.join(missing)}"
        return f"{self.name} reviewed status: {status}"

    def _check_agents(self) -> list[str]:
        now = time.time()
        missing = []
        for agent, ts in self.last_seen.items():
            if now - ts > self.timeout:
                missing.append(agent)
        return missing

    def send_heartbeat(self) -> None:
        timestamp = time.time()
        self.bus.publish("heartbeat", f"{self.name}:{timestamp}")

if __name__ == "__main__":
    agent = GovernanceAgent()
    print(agent.run("ok"))
