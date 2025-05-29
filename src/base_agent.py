class BaseAgent:
    """Base class for simple agent examples."""

    def __init__(self, name: str) -> None:
        self.name = name

    def run(self, message: str) -> str:
        """Process an incoming message and return a response."""
        raise NotImplementedError
