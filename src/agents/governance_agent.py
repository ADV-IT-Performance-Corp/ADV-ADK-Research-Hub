from datetime import datetime
import logging

from core.base_agent import BaseAgent

class GovernanceAgent(BaseAgent):
    """Prototype agent to monitor other agents and handle escalation."""

    def __init__(self) -> None:
        super().__init__(name="GovernanceAgent")

    def run(self, status: str) -> str:
        """Check heartbeat status and log the result."""
        timestamp = datetime.utcnow().isoformat()

        if status.lower() in {"ok", "alive", "ready"}:
            message = f"{timestamp} {self.name} heartbeat acknowledged"
            logging.info(message)
        else:
            message = f"{timestamp} {self.name} detected anomaly: {status}"
            logging.warning(message)

        return message

if __name__ == "__main__":
    agent = GovernanceAgent()
    print(agent.run("ok"))
