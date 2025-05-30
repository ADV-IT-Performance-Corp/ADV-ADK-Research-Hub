class FewShotSelector:
    """Return example prompts relevant to a given topic."""

    def __init__(self, examples: dict[str, str] | None = None) -> None:
        self.examples = examples or {}

    def select(self, topic: str) -> str:
        return self.examples.get(topic, "")
