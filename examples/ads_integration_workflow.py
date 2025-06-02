"""Demo workflow for Google and Meta Ads integrations."""

from src.integrations import GoogleAdsClient, MetaAdsClient
from src.core.metrics import MetricsCollector
from src.core.reporting import ReportGenerator


def main() -> None:
    collector = MetricsCollector()
    collector.add_source(lambda: GoogleAdsClient("google.json").fetch_campaign_metrics("123"))
    collector.add_source(lambda: MetaAdsClient("token").fetch_campaign_metrics("abc"))

    metrics = collector.collect()
    report = ReportGenerator().generate(metrics)
    print(report)


if __name__ == "__main__":
    main()
