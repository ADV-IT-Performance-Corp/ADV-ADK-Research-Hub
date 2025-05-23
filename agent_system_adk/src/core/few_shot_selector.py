class FewShotSelector:
    """Selects few-shot examples based on task context."""
    def __init__(self, examples=None):
        self.examples = examples or []

    def select(self, k: int = 3):
        return self.examples[:k]
