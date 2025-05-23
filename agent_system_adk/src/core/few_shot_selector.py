class FewShotSelector:
    """Selects few-shot examples based on context."""

    def select_examples(self, examples, k=3):
        return examples[:k]
