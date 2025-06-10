import unittest

from o3research.agents import EchoAgent


class TestEchoAgent(unittest.TestCase):
    def test_echo(self) -> None:
        agent = EchoAgent()
        result = agent.run("hi")
        self.assertEqual(result, "EchoAgent: hi")


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
