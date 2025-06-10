# Reporting Dashboard

The reporting dashboard centralizes campaign metrics for quick review.

## Features
- View aggregated metrics in real time
- Generate shareable reports for stakeholders
- Export metrics to JSON
- Export metrics to CSV for deeper analysis
- Track KPIs such as CTR, CPC, ROAS, CLV, CPA and retention rate

## Using `ReportGenerator`

The `ReportGenerator` utility converts collected metrics into various formats.
Below is a typical workflow:

1. Gather or compute metrics. The [`MetricsCollector`](../o3research/core/metrics.py)
   class can help aggregate raw values.
2. Instantiate the generator:

   ```python
   from src.core.reporting import ReportGenerator

   reporter = ReportGenerator()
   ```

3. Produce a Markdown table for quick sharing:

   ```python
   table = reporter.to_markdown(metrics)
   print(table)
   ```

4. Export results to CSV:

   ```python
   reporter.export_csv(metrics, "campaign_metrics.csv")
   ```

5. Export the same metrics to JSON:

   ```python
   import json

   with open("campaign_metrics.json", "w") as f:
       json.dump(metrics, f, indent=2)
   ```

## Exporting Metrics

CSV exports are ideal for spreadsheets and BI tools, while JSON works well for
automated pipelines. Both formats help the marketing team spot trends, compare
campaigns and feed data into optimization workflows.

## Dashboard Screenshot

No dashboard screenshot is currently included in the repository.
