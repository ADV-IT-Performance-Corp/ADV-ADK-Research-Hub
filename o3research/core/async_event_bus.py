import asyncio
from collections import defaultdict
from .logger import get_logger
from .types import AsyncCallback


class AsyncEventBus:
    """Simple asyncio-based publish/subscribe bus."""

    def __init__(self) -> None:
        self.subscribers: dict[str, list[AsyncCallback]] = defaultdict(list)
        self.logger = get_logger(self.__class__.__name__)

    def subscribe(self, topic: str, callback: AsyncCallback) -> None:
        self.logger.debug("Subscriber added to %s", topic)
        self.subscribers[topic].append(callback)

    async def publish(self, topic: str, message: str) -> None:
        tasks = [callback(message) for callback in self.subscribers.get(topic, [])]
        if tasks:
            results = await asyncio.gather(*tasks, return_exceptions=True)
            for result in results:
                if isinstance(result, Exception):
                    self.logger.error("Error in subscriber for %s: %s", topic, result)
