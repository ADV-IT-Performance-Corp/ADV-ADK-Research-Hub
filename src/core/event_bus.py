class EventBus:
    """Very small publish/subscribe bus."""

    def __init__(self) -> None:
        self.subscribers: dict[str, list[callable]] = {}

    def subscribe(self, topic: str, callback: callable) -> None:
        self.subscribers.setdefault(topic, []).append(callback)

    def publish(self, topic: str, message: str) -> None:
        for callback in self.subscribers.get(topic, []):
            callback(message)
