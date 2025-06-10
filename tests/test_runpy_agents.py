import io
import runpy
from contextlib import redirect_stdout


def _capture_run(module_name: str) -> str:
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        runpy.run_module(module_name, run_name="__main__")
    return buffer.getvalue()


def test_run_research_agent_via_run_module() -> None:
    output = _capture_run("o3research.agents.research_agent")
    assert "researched" in output


def test_run_content_agent_via_run_module() -> None:
    output = _capture_run("o3research.agents.content_agent")
    assert "blog post" in output


def test_run_engagement_agent_via_run_module() -> None:
    output = _capture_run("o3research.agents.engagement_agent")
    assert output == ""


def test_run_optimization_agent_via_run_module() -> None:
    output = _capture_run("o3research.agents.optimization_agent")
    assert output == ""


def test_run_analytics_agent_via_run_module() -> None:
    output = _capture_run("o3research.agents.analytics_agent")
    assert output == ""


def test_run_campaign_agent_via_run_module() -> None:
    output = _capture_run("o3research.agents.campaign_agent")
    assert "campaign" in output


def test_run_governance_agent_via_run_module() -> None:
    output = _capture_run("o3research.agents.governance_agent")
    assert "reviewed status" in output
