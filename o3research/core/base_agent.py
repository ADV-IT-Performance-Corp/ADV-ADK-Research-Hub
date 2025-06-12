"""Wrapper around google.adk.Agent with relaxed field handling."""

from google.adk import Agent as ADKAgent
from pydantic import ConfigDict


class Agent(ADKAgent):
    """Project base agent using the ADK Agent class."""

    model_config = ConfigDict(extra="allow")


__all__ = ["Agent"]
