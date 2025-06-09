import unittest
from o3research.core.base_agent import BaseAgent


class DummyAgent(BaseAgent):
    """Trivial subclass without overriding run."""

    pass


class TestBaseAgent(unittest.TestCase):
    def test_run_not_implemented(self):
        agent = DummyAgent(name="dummy")
        with self.assertRaises(NotImplementedError) as cm:
            agent.run("msg")
        self.assertEqual(str(cm.exception), "")


if __name__ == "__main__":
    unittest.main()
