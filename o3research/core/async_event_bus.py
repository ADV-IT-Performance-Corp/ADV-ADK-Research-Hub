import asyncio
from collections import defaultdict
from .types import AsyncCallback

class AsyncEventBus:
    """Simple asyncio-based publish/subscribe bus."""

    def __init__(self) -> None:
        self.subscribers: dict[str, list[AsyncCallback]] = defaultdict(list)

    def subscribe(self, topic: str, callback: AsyncCallback) -> None:
        self.subscribers[topic].append(callback)

    async def publish(self, topic: str, message: str) -> None:
        tasks = [callback(message) for callback in self.subscribers.get(topic, [])]
        if tasks:
            await asyncio.gather(*tasks)
