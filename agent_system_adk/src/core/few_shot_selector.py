class FewShotSelector:
    """Selects few-shot examples based on simple heuristics."""

    def select(self, examples, k=3):
        return examples[:k]
