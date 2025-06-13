__version__ = "4.0.0"


class EchoAgent:
    """Simple agent that echoes received messages."""

    def __init__(self, name: str = "EchoAgent") -> None:
        self.name = name

    def run(self, message: str) -> str:
        """Return a formatted echo response."""
        from o3research.lifecycle import finish_run, start_run

        start_run(self.name)
        try:
            return f"{self.name}: {message}"
        finally:
            finish_run(self.name)


if __name__ == "__main__":
    agent = EchoAgent()
    print(agent.run("Hello world"))
