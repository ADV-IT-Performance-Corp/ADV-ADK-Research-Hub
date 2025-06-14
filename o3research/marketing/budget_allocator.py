from typing import Dict, Union

import time
from google.adk import Agent
from o3research.lifecycle import finish_run, start_run
from .prompt_observability import record_prompt


class BudgetAllocatorAgent(Agent):
    """Allocate budget across channels based on performance goals."""

    def __init__(self) -> None:
        super().__init__(name="BudgetAllocatorAgent")

    def run(  # type: ignore[override]
        self,
        channel_metrics: Dict[str, Dict[str, Union[int, float]]],
        target: float,
        goal: str = "CPA",
    ) -> str:
        """Return recommended spend per channel and daily budget.

        Parameters
        ----------
        channel_metrics:
            Mapping of channel names to metric dicts with
            ``conversions`` and ``revenue``.
        target:
            Desired CPA or ROAS value.
        goal:
            Either ``"CPA"`` or ``"ROAS"`` determining how allocations are computed.
        """
        start_run(self.name)
        start = time.perf_counter()
        allocation: Dict[str, float] = {}
        total_spend = 0.0

        goal_upper = goal.upper()
        for channel, metrics in channel_metrics.items():
            conversions = float(metrics.get("conversions", 0))
            revenue = float(metrics.get("revenue", 0))

            if goal_upper == "ROAS":
                spend = revenue / target if target else 0.0
            else:  # default CPA
                spend = target * conversions

            allocation[channel] = round(spend, 2)
            total_spend += spend

        daily_budget = round(total_spend / 30.0, 2)

        lines = [f"Recommended spend per channel ({goal_upper} target {target}):"]
        for ch, spend in allocation.items():
            lines.append(f"- {ch}: ${spend}")
        lines.append(f"Daily budget: ${daily_budget}")
        result = "\n".join(lines)
        latency = time.perf_counter() - start
        record_prompt(
            "budget_allocation",
            self.name,
            result,
            timing=latency,
            cost=0.0,
        )
        finish_run(self.name)
        return result


if __name__ == "__main__":  # pragma: no cover
    example_metrics = {
        "search": {"conversions": 30.0, "revenue": 1200.0},
        "social": {"conversions": 20.0, "revenue": 800.0},
    }
    agent = BudgetAllocatorAgent()
    print(agent.run(example_metrics, target=10, goal="CPA"))
