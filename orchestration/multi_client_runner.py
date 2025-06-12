"""Run marketing workflows for multiple clients."""

from __future__ import annotations

import runpy
from pathlib import Path
from typing import Any, Dict

import yaml
from o3research.lifecycle import finish_run, start_run

CLIENTS_DIR = Path(__file__).resolve().parent.parent / "config" / "clients"
FLOW_FILE = Path(__file__).resolve().parent.parent / "flows" / "client_workflow.yaml"


def load_config(path: Path) -> Dict[str, Any]:
    """Load a client configuration file."""
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def run_workflow(settings: Dict[str, Any]) -> None:
    """Execute the client workflow using Vertex AI if available."""
    project_id = settings.get("project_id")
    credentials = settings.get("credentials")
    region = settings.get("region", "us-central1")

    try:  # defer import so tests don't require the package
        from google.adk.runners import VertexAIRunner  # type: ignore

        runner = VertexAIRunner(
            flow=str(FLOW_FILE),
            project_id=project_id,
            credentials=credentials,
            region=region,
        )
        start_run("MultiClientRunner")
        try:
            runner.run()
        finally:
            finish_run("MultiClientRunner")
    except Exception as exc:  # pragma: no cover - optional path
        print(f"Falling back to local workflow: {exc}")
        runpy.run_module("examples.simple_workflow", run_name="__main__")


def main() -> None:
    for cfg_path in sorted(CLIENTS_DIR.glob("*.yaml")):
        print(f"Running workflow for {cfg_path.stem}")
        settings = load_config(cfg_path)
        run_workflow(settings)


if __name__ == "__main__":  # pragma: no cover
    main()
