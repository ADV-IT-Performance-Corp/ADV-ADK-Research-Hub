class SelfReflection:
    """Simple self-reflection that scores text quality."""

    def score(self, text: str) -> int:
        length = len(text)
        if length > 200:
            return 5
        if length > 100:
            return 4
        return 3
