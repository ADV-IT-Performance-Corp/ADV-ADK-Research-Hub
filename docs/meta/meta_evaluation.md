# Meta Evaluation Usage

The evaluation framework defined in `meta_evaluation.json` assigns a weight to each metric. To compute an overall score programmatically:

```python
from src.core.evaluation import evaluate

score = evaluate({
    "clarity": 5,
    "completeness": 4,
    "alignment": 4,
    "efficiency": 3,
})
```

The `evaluate` function loads the weights from `meta_evaluation.json` and returns the weighted average. Metrics not defined in the JSON are ignored.
