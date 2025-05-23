class BaseAgent:
    """Minimal base class for O3 agents."""
    def __init__(self, name: str):
        self.name = name

    def run(self, *args, **kwargs):
        raise NotImplementedError("Agents must implement the run method")
