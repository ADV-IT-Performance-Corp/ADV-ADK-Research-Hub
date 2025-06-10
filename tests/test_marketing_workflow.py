import io
import runpy
import unittest
from contextlib import redirect_stdout, redirect_stderr


class TestMarketingWorkflowExample(unittest.TestCase):
    def test_example_runs(self) -> None:
        buffer = io.StringIO()
        with redirect_stdout(buffer), redirect_stderr(buffer):
            runpy.run_module("examples.marketing_workflow", run_name="__main__")
        output = buffer.getvalue()
        self.assertIn("Plan for new SaaS product", output)
        self.assertIn("Recommended spend per channel", output)
        self.assertIn("AnalyticsAgent analyzed data", output)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
