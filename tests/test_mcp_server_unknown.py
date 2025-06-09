import unittest
import importlib.util
from unittest.mock import patch

YAML_AVAILABLE = importlib.util.find_spec("yaml") is not None

if YAML_AVAILABLE:
    from o3research.mcp_server import MCPServer


@unittest.skipUnless(YAML_AVAILABLE, "yaml library not available")
class TestMCPServerUnknown(unittest.TestCase):
    def setUp(self) -> None:
        self.server = MCPServer()
        self.payload = "payload"

    def test_route_known_and_unknown_tasks(self) -> None:
        with patch.object(
            self.server.research_agent,
            "run",
            return_value="r",
        ) as mock_research:
            result = self.server.route("research", self.payload)
            self.assertEqual(result, "r")
            mock_research.assert_called_once_with(self.payload)

        with patch.object(
            self.server.content_agent,
            "run",
            return_value="c",
        ) as mock_content:
            result = self.server.route("content", self.payload)
            self.assertEqual(result, "c")
            mock_content.assert_called_once_with(self.payload)

        with patch.object(
            self.server.engagement_agent,
            "run",
            return_value="e",
        ) as mock_engagement:
            result = self.server.route("engagement", self.payload)
            self.assertEqual(result, "e")
            mock_engagement.assert_called_once_with(self.payload)

        with patch.object(
            self.server.optimization_agent,
            "run",
            return_value="o",
        ) as mock_optimize:
            result = self.server.route("optimize", self.payload)
            self.assertEqual(result, "o")
            mock_optimize.assert_called_once_with(self.payload)

        with patch.object(
            self.server.analytics_agent,
            "run",
            return_value="a",
        ) as mock_analytics:
            result = self.server.route("analytics", self.payload)
            self.assertEqual(result, "a")
            mock_analytics.assert_called_once_with(self.payload)

        with patch.object(
            self.server.config_agent,
            "run",
            return_value="cfg",
        ) as mock_config:
            result = self.server.route("config", self.payload)
            self.assertEqual(result, "cfg")
            mock_config.assert_called_once_with(self.payload)

        unknown_task = "invalid"
        result = self.server.route(unknown_task, self.payload)
        self.assertEqual(result, f"Unknown task: {unknown_task}")


if __name__ == "__main__":
    unittest.main()
