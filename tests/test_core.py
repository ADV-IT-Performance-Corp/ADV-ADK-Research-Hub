import unittest
from src.core.event_bus import EventBus
from src.core.async_event_bus import AsyncEventBus
from src.core.metrics import MetricsCollector
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


class TestMetricsCollector(unittest.TestCase):
    def test_collect_kpis(self):
        mc = MetricsCollector()
        mc.add(impressions=1000, clicks=100, cost=50.0, conversions=10, revenue=200.0)
        result = mc.collect()
        self.assertEqual(result['impressions'], 1000)
        self.assertEqual(result['clicks'], 100)
        self.assertAlmostEqual(result['CTR'], 0.1)
        self.assertAlmostEqual(result['CPC'], 0.5)
        self.assertAlmostEqual(result['ConversionRate'], 0.1)
        self.assertAlmostEqual(result['ROAS'], 4.0)

    def test_zero_division(self):
        mc = MetricsCollector()
        mc.add(impressions=0, clicks=0, cost=0.0, conversions=0, revenue=0.0)
        result = mc.collect()
        self.assertEqual(result['CTR'], 0.0)
        self.assertEqual(result['CPC'], 0.0)
        self.assertEqual(result['ConversionRate'], 0.0)
        self.assertEqual(result['ROAS'], 0.0)

if __name__ == '__main__':
    unittest.main()
