# Landing Page Utilities

**Focus**: Create simple HTML landing pages and attach GA4 tracking.

## Example usage

```python
from o3research.web import create_landing_page, add_ga4_tag

html = create_landing_page("analytics suite", "understand your visitors")
html = add_ga4_tag(html, "G-XXXX", events=["sign_up"])
print(html)
```
