# Marketing API Integration

**Focus**: Example of sending a campaign plan to the Google Ads API sandbox.

## push_campaign

Use `push_campaign` from `o3research.marketing`:

```python
from o3research.marketing import push_campaign

plan = {"name": "Sandbox Campaign", "customer_id": "123-456-7890"}
resource = push_campaign(plan)
print(resource)
```
