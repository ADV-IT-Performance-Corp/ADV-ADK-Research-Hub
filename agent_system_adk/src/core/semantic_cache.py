class SemanticCache:
    """Simple in-memory semantic cache stub."""
    def __init__(self):
        self.store = {}

    def get(self, key: str):
        return self.store.get(key)

    def set(self, key: str, value):
        self.store[key] = value
