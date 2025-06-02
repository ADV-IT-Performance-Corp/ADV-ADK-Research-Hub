import unittest
from src.core.event_bus import EventBus
from src.core.async_event_bus import AsyncEventBus
import asyncio

class TestEventBus(unittest.TestCase):
    def test_publish_subscribe(self):
        bus = EventBus()
        received = []
        bus.subscribe('topic', lambda m: received.append(m))
        bus.publish('topic', 'hello')
        self.assertEqual(received, ['hello'])

    def test_async_publish_subscribe(self):
        bus = AsyncEventBus()
        received = []
        async def handler(msg: str) -> None:
            received.append(msg)
        bus.subscribe('topic', handler)
        asyncio.run(bus.publish('topic', 'async'))
        self.assertEqual(received, ['async'])

if __name__ == '__main__':
    unittest.main()
