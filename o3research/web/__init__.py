"""Web utilities for generating pages and tracking analytics."""

from .landing_page_creator import create_landing_page
from .analytics_tagging import add_ga4_tag

__all__ = ["create_landing_page", "add_ga4_tag"]
