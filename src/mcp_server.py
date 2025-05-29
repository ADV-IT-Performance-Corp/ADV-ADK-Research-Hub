"""Minimal orchestrator that routes tasks to sample agents."""
from research_agent import ResearchAgent
from content_agent import ContentAgent


class MCPServer:
    def __init__(self) -> None:
        self.research_agent = ResearchAgent()
        self.content_agent = ContentAgent()

    def route(self, task: str, payload: str) -> str:
        if task == "research":
            return self.research_agent.run(payload)
        if task == "content":
            return self.content_agent.run(payload)
        return f"Unknown task: {task}"


if __name__ == "__main__":
    server = MCPServer()
    print(server.route("research", "competitor analysis"))
    print(server.route("content", "ROI best practices"))
