import unittest
from o3research.core.event_bus import EventBus
from o3research.core.async_event_bus import AsyncEventBus
from o3research.core.metrics import MetricsCollector
import asyncio
try:
    import yaml  # type: ignore
    YAML_AVAILABLE = True
except Exception:
    YAML_AVAILABLE = False

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

    def test_publish_no_subscribers(self):
        """Publishing to a topic with no subscribers should not raise."""
        bus = EventBus()
        try:
            bus.publish('empty', 'msg')
        except Exception as exc:  # pragma: no cover - should not happen
            self.fail(f"Publish raised unexpectedly: {exc}")

    def test_publish_multiple_exceptions(self):
        bus = EventBus()

        def bad1(_: str) -> None:
            raise ValueError('first')

        def bad2(_: str) -> None:
            raise RuntimeError('second')

        bus.subscribe('topic', bad1)
        bus.subscribe('topic', bad2)

        with self.assertRaises(ValueError):
            bus.publish('topic', 'data')

    def test_async_publish_multiple_exceptions(self):
        bus = AsyncEventBus()

        async def bad1(_: str) -> None:
            raise ValueError('first')

        async def bad2(_: str) -> None:
            raise RuntimeError('second')

        bus.subscribe('topic', bad1)
        bus.subscribe('topic', bad2)

        with self.assertRaises(ValueError):
            asyncio.run(bus.publish('topic', 'data'))


class TestMetricsCollector(unittest.TestCase):
    def test_collect_kpis(self):
        mc = MetricsCollector()
        mc.add(
            impressions=1000,
            clicks=100,
            cost=50.0,
            conversions=10,
            revenue=200.0,
            returning_customers=5,
        )
        result = mc.collect()
        self.assertEqual(result['impressions'], 1000)
        self.assertEqual(result['clicks'], 100)
        self.assertAlmostEqual(result['CTR'], 0.1)
        self.assertAlmostEqual(result['CPC'], 0.5)
        self.assertAlmostEqual(result['ConversionRate'], 0.1)
        self.assertAlmostEqual(result['ROAS'], 4.0)
        self.assertAlmostEqual(result['CLV'], 20.0)
        self.assertAlmostEqual(result['CPA'], 5.0)
        self.assertAlmostEqual(result['RetentionRate'], 0.5)

    def test_zero_division(self):
        mc = MetricsCollector()
        mc.add(
            impressions=0,
            clicks=0,
            cost=0.0,
            conversions=0,
            revenue=0.0,
            returning_customers=0,
        )
        result = mc.collect()
        self.assertEqual(result['CTR'], 0.0)
        self.assertEqual(result['CPC'], 0.0)
        self.assertEqual(result['ConversionRate'], 0.0)
        self.assertEqual(result['ROAS'], 0.0)
        self.assertEqual(result['CLV'], 0.0)
        self.assertEqual(result['CPA'], 0.0)
        self.assertEqual(result['RetentionRate'], 0.0)


class TestQueueLimits(unittest.TestCase):
    def test_async_queue_overflow(self):
        """Ensure queue overflow raises QueueFull if configured."""
        if not YAML_AVAILABLE:
            self.skipTest('yaml library not available')

        with open('config/settings.yaml', 'r') as f:
            settings = yaml.safe_load(f)
        max_size = settings.get('max_queue_size')
        if not max_size:
            self.skipTest('max_queue_size not configured')

        q = asyncio.Queue(maxsize=max_size)
        for i in range(max_size):
            q.put_nowait(i)

        with self.assertRaises(asyncio.QueueFull):
            q.put_nowait('overflow')

if __name__ == '__main__':
    unittest.main()
