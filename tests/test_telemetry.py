import os
import unittest
from unittest.mock import patch

from o3research.core.telemetry import TelemetryClient


class DummyCollector:
    def __init__(self) -> None:
        self.events = []

    def __call__(self, event):
        self.events.append(event)


class TestTelemetryClient(unittest.TestCase):
    def test_logging_enabled(self):
        collector = DummyCollector()
        client = TelemetryClient(collector)
        with patch.dict(os.environ, {"TELEMETRY_ENABLED": "1"}):
            client.log_event({"type": "foo"}, timing=0.5, cost=0.1)
            self.assertEqual(
                client.buffer, [{"type": "foo", "timing": 0.5, "cost": 0.1}]
            )
            client.flush()
        self.assertEqual(
            collector.events,
            [{"type": "foo", "timing": 0.5, "cost": 0.1}],
        )
        self.assertEqual(client.buffer, [])

    def test_logging_disabled(self):
        collector = DummyCollector()
        client = TelemetryClient(collector)
        with patch.dict(os.environ, {}, clear=True):
            client.log_event({"type": "foo"})
        with patch.dict(os.environ, {"TELEMETRY_ENABLED": "0"}):
            client.log_event({"type": "bar"})
        self.assertEqual(collector.events, [])
        self.assertEqual(client.buffer, [])

    def test_flush_resets_buffer(self):
        collector = DummyCollector()
        client = TelemetryClient(collector)
        with patch.dict(os.environ, {"TELEMETRY_ENABLED": "1"}):
            client.log_event({"type": "foo"}, timing=0.1, cost=0.0)
            client.log_event({"type": "bar"}, timing=0.2, cost=0.0)
            client.flush()
            self.assertEqual(
                collector.events,
                [
                    {"type": "foo", "timing": 0.1, "cost": 0.0},
                    {"type": "bar", "timing": 0.2, "cost": 0.0},
                ],
            )
            self.assertEqual(client.buffer, [])
