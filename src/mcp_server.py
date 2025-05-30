"""Minimal orchestrator that routes tasks to sample agents."""
from agents.research_agent import ResearchAgent
from agents.content_agent import ContentAgent
from agents.engagement_agent import EngagementAgent
from agents.optimization_agent import OptimizationAgent
from agents.analytics_agent import AnalyticsAgent
from agents.config_agent import ConfigAgent


class MCPServer:
    def __init__(self) -> None:
        self.research_agent = ResearchAgent()
        self.content_agent = ContentAgent()
        self.engagement_agent = EngagementAgent()
        self.optimization_agent = OptimizationAgent()
        self.analytics_agent = AnalyticsAgent()
        self.config_agent = ConfigAgent()

    def route(self, task: str, payload: str) -> str:
        if task == "research":
            return self.research_agent.run(payload)
        if task == "content":
            return self.content_agent.run(payload)
        if task == "engagement":
            return self.engagement_agent.run(payload)
        if task == "optimize":
            return self.optimization_agent.run(payload)
        if task == "analytics":
            return self.analytics_agent.run(payload)
        if task == "config":
            return self.config_agent.run(payload)
        return f"Unknown task: {task}"


if __name__ == "__main__":
    server = MCPServer()
    print(server.route("research", "competitor analysis"))
    print(server.route("content", "ROI best practices"))
    print(server.route("engagement", "new lead"))
    print(server.route("optimize", "CTR"))
    print(server.route("analytics", "daily metrics"))
    print(server.route("config", ""))
