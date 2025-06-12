"""Execute the marketing flow locally using the ADK runner."""

from __future__ import annotations

from pathlib import Path

from google.adk.runners import InMemoryRunner  # type: ignore

FLOW_FILE = Path(__file__).resolve().parent.parent / "flows" / "marketing_flow.yaml"


def main() -> None:
    runner = InMemoryRunner(flow=str(FLOW_FILE))
    runner.run()


if __name__ == "__main__":  # pragma: no cover
    main()
