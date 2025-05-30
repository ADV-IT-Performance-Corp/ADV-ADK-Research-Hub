"""In-memory publish/subscribe utilities."""

from __future__ import annotations

from collections import defaultdict
from typing import Awaitable, Callable
import asyncio


class EventBus:
    """Synchronous pub/sub bus."""

    def __init__(self) -> None:
        self.subscribers: dict[str, list[Callable[[str], None]]] = defaultdict(list)

    def subscribe(self, topic: str, callback: Callable[[str], None]) -> None:
        self.subscribers[topic].append(callback)

    def publish(self, topic: str, message: str) -> None:
        for callback in self.subscribers.get(topic, []):
            callback(message)


class AsyncEventBus:
    """Asyncio-based pub/sub bus for concurrent agent communication."""

    def __init__(self) -> None:
        self.subscribers: dict[str, list[Callable[[str], Awaitable[None]]]] = defaultdict(list)

    def subscribe(self, topic: str, callback: Callable[[str], Awaitable[None]]) -> None:
        self.subscribers[topic].append(callback)

    async def publish(self, topic: str, message: str) -> None:
        await asyncio.gather(*(cb(message) for cb in self.subscribers.get(topic, [])))
