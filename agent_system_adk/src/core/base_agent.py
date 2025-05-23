class BaseAgent:
    """Base class for all agents in the O3 system."""

    def __init__(self, name: str):
        self.name = name

    def run(self, *args, **kwargs):
        """Entry point for agent execution."""
        raise NotImplementedError("run must be implemented by subclasses")
