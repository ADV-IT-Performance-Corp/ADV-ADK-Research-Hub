import unittest
import importlib.util

YAML_AVAILABLE = importlib.util.find_spec("yaml") is not None

if YAML_AVAILABLE:
    from o3research.mcp_server import MCPServer

@unittest.skipUnless(YAML_AVAILABLE, "yaml library not available")
class TestMCPServer(unittest.TestCase):
    def setUp(self) -> None:
        self.server = MCPServer()

    def test_research_route(self) -> None:
        result = self.server.route("research", "market trends")
        self.assertEqual(result, "ResearchAgent researched: market trends")

    def test_content_route(self) -> None:
        result = self.server.route("content", "AI marketing")
        expected = "ContentAgent suggests a blog post about 'AI marketing'"
        self.assertEqual(result, expected)

    def test_engagement_route(self) -> None:
        result = self.server.route("engagement", "new lead")
        self.assertEqual(result, "EngagementAgent nurtures lead: new lead")

    def test_optimize_route(self) -> None:
        result = self.server.route("optimize", "CTR")
        self.assertEqual(result, "OptimizationAgent optimizes for CTR")

    def test_analytics_route(self) -> None:
        result = self.server.route("analytics", "daily metrics")
        self.assertEqual(result, "AnalyticsAgent analyzed data: daily metrics")

    def test_config_route(self) -> None:
        settings_count = len(self.server.config_agent.load_settings())
        result = self.server.route("config", "")
        self.assertEqual(result, f"ConfigAgent loaded {settings_count} settings")

if __name__ == "__main__":
    unittest.main()
