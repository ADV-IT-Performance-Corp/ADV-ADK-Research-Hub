import io
import runpy
from contextlib import redirect_stdout


def test_run_mcp_server_via_run_module() -> None:
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        runpy.run_module("o3research.mcp_server", run_name="__main__")
    lines = [line for line in buffer.getvalue().splitlines() if line.strip()]
    assert len(lines) == 6


def test_run_sample_agent_via_run_module() -> None:
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        runpy.run_module("o3research.agents.sample_agent", run_name="__main__")
    output = buffer.getvalue()
    assert "Hello world" in output
