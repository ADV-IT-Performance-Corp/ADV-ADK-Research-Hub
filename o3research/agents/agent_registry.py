from typing import Type, Dict

from ..marketing.google_ads_agent import GoogleAdsCampaignAgent

# simple registry mapping names to agent classes
_AGENT_REGISTRY: Dict[str, Type] = {}


def register_agent(name: str, agent_cls: Type) -> None:
    """Register an agent class under a unique name."""
    if name in _AGENT_REGISTRY:
        raise KeyError(f"Agent {name} already registered")
    _AGENT_REGISTRY[name] = agent_cls


def get_agent(name: str) -> Type:
    """Retrieve an agent class by name."""
    try:
        return _AGENT_REGISTRY[name]
    except KeyError as exc:
        raise KeyError(f"Agent {name} not found") from exc


def clear_registry() -> None:
    """Remove all registered agents (useful for tests)."""
    _AGENT_REGISTRY.clear()
    # re-register built-in agents
    register_agent("google_ads", GoogleAdsCampaignAgent)


# register default agents
register_agent("google_ads", GoogleAdsCampaignAgent)
