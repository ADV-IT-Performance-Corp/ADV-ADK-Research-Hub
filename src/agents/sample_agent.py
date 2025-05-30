class EchoAgent:
    """Simple agent that echoes received messages."""

    def __init__(self, name: str = "EchoAgent") -> None:
        self.name = name

    def run(self, message: str) -> str:
        """Return a formatted echo response."""
        return f"{self.name}: {message}"


if __name__ == "__main__":
    agent = EchoAgent()
    print(agent.run("Hello world"))
