class BaseAgent:
    """Base class for all agents."""

    def __init__(self, name: str):
        self.name = name

    def run(self, *args, **kwargs):
        raise NotImplementedError
