class FewShotSelector:
    """Selects few-shot examples for prompts."""
    def __init__(self, examples=None):
        self.examples = examples or []

    def select(self, n=3):
        return self.examples[:n]
