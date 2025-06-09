import json
from pathlib import Path


def _load_meta_evaluation() -> dict:
    """Load evaluation metadata from JSON."""
    path = (
        Path(__file__).resolve().parents[2] / "docs" / "meta" / "meta_evaluation.json"
    )
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


META_EVALUATION = _load_meta_evaluation()


def evaluate(metrics: dict[str, float]) -> float:
    """Compute a weighted score based on provided metrics.

    Parameters
    ----------
    metrics: dict[str, float]
        Mapping of metric id to numeric score.

    Returns
    -------
    float
        Weighted evaluation score. Returns 0.0 if no weights match.
    """
    weights = {
        m["id"]: m.get("weight", 0.0)
        for m in META_EVALUATION.get("evaluation_metrics", [])
    }
    weighted_sum = 0.0
    total_weight = 0.0
    for name, score in metrics.items():
        weight = weights.get(name)
        if weight:
            weighted_sum += score * weight
            total_weight += weight
    return weighted_sum / total_weight if total_weight else 0.0
