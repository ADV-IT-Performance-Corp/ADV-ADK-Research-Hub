"""Execute the marketing flow on Vertex AI endpoints."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any, Dict

import yaml


ROOT = Path(__file__).resolve().parent.parent
FLOW_FILE = ROOT / "flows" / "marketing_flow.yaml"
CONFIG_FILE = ROOT / "config" / "vertex_config.yaml"


def load_settings() -> Dict[str, Any]:
    """Load config and override with environment variables."""
    with CONFIG_FILE.open("r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f) or {}
    return {
        "project_id": os.getenv("VERTEX_PROJECT_ID", cfg.get("project_id")),
        "credentials": os.getenv("VERTEX_CREDENTIALS", cfg.get("credentials")),
        "region": os.getenv("VERTEX_REGION", cfg.get("region", "us-central1")),
    }


def main() -> None:
    settings = load_settings()
    try:  # defer heavy import
        from google.adk.runners import VertexAIRunner  # type: ignore
    except Exception as exc:  # pragma: no cover - optional dependency
        raise RuntimeError("Google ADK is required to run on Vertex AI") from exc

    runner = VertexAIRunner(
        flow=str(FLOW_FILE),
        project_id=settings["project_id"],
        credentials=settings["credentials"],
        region=settings["region"],
    )
    runner.run()


if __name__ == "__main__":  # pragma: no cover
    main()
# Example Vertex AI workflow
