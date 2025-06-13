import importlib
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from types import ModuleType
from unittest.mock import MagicMock, patch


class TestMultiClientRunner(unittest.TestCase):
    def test_main_success_and_fallback(self) -> None:
        # Provide stub google.adk modules before importing the runner
        modules = {
            "google.adk": ModuleType("google.adk"),
            "google.adk.runners": ModuleType("google.adk.runners"),
            "o3research": ModuleType("o3research"),
            "o3research.lifecycle": ModuleType("o3research.lifecycle"),
        }
        modules["google.adk"].Agent = object
        modules["o3research"].lifecycle = modules["o3research.lifecycle"]
        modules["o3research.lifecycle"].start_run = lambda _name: None
        modules["o3research.lifecycle"].finish_run = lambda _name: None
        runner_instance = MagicMock()
        modules["google.adk.runners"].VertexAIRunner = MagicMock(
            return_value=runner_instance
        )
        for name, mod in modules.items():
            sys.modules[name] = mod

        mcr = importlib.import_module("orchestration.multi_client_runner")

        with TemporaryDirectory() as tmpdir:
            cfg_path = Path(tmpdir) / "client.yaml"
            cfg_path.write_text("project_id: test\ncredentials: cred.json\n")

            with patch.object(mcr, "CLIENTS_DIR", Path(tmpdir)):
                with patch("runpy.run_module") as run_mod:
                    mcr.main()
                    modules[
                        "google.adk.runners"
                    ].VertexAIRunner.assert_called_once_with(
                        flow=str(mcr.FLOW_FILE),
                        project_id="test",
                        credentials="cred.json",
                        region="us-central1",
                    )
                    runner_instance.run.assert_called_once()
                    run_mod.assert_not_called()

        # Remove stub modules to trigger fallback path
        sys.modules.pop("google.adk.runners", None)
        sys.modules.pop("google.adk", None)
        sys.modules.pop("o3research", None)
        sys.modules.pop("o3research.lifecycle", None)

        with TemporaryDirectory() as tmpdir:
            cfg_path = Path(tmpdir) / "client.yaml"
            cfg_path.write_text("project_id: test\ncredentials: cred.json\n")

            with patch.object(mcr, "CLIENTS_DIR", Path(tmpdir)):
                with patch("runpy.run_module") as run_mod:
                    mcr.main()
                    run_mod.assert_called_once_with(
                        "examples.simple_workflow", run_name="__main__"
                    )


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
