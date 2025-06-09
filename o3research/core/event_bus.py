from .logger import get_logger
from .types import Callback


class EventBus:
    """Very small publish/subscribe bus with basic logging."""

    def __init__(self) -> None:
        self.subscribers: dict[str, list[Callback]] = {}
        self.logger = get_logger(self.__class__.__name__)

    def subscribe(self, topic: str, callback: Callback) -> None:
        self.logger.debug("Subscriber added to %s", topic)
        self.subscribers.setdefault(topic, []).append(callback)

    def publish(self, topic: str, message: str) -> None:
        self.logger.debug("Publishing to %s: %s", topic, message)
        for callback in self.subscribers.get(topic, []):
            callback(message)
