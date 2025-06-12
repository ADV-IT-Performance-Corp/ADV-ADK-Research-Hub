# CRM Integration

This guide explains how to authenticate with a CRM API and use the utilities in `o3research.crm`.

## Authentication

`sync_to_crm` expects a bearer token. Export `CRM_TOKEN` in your environment and pass it to the function:

```bash
export CRM_TOKEN="YOUR_TOKEN"
```

## Example Usage

```python
from o3research.crm import LeadScoringAgent, sync_to_crm

lead = {"name": "Ada", "industry": "technology", "annual_revenue": 1500000}
agent = LeadScoringAgent()
score = agent.run(lead)

sync_to_crm({**lead, "score": score}, token=os.environ["CRM_TOKEN"])
```
