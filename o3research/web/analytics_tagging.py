"""Utilities for inserting GA4 analytics tags into HTML pages."""

from __future__ import annotations

from typing import Iterable

BASE_SNIPPET = (
    '<script async src="https://www.googletagmanager.com/gtag/js?id='
    '{mid}"></script>\n'
    "<script>\n"
    "window.dataLayer = window.dataLayer || [];\n"
    "function gtag(){{dataLayer.push(arguments);}}\n"
    "gtag('js', new Date());\n"
    "gtag('config', '{mid}');\n"
    "{events}\n"
    "</script>"
)

EVENT_SNIPPET = "gtag('event', '{name}', {{'send_to': '{mid}'}});"


def add_ga4_tag(
    html: str,
    measurement_id: str,
    *,
    events: Iterable[str] | None = None,
) -> str:
    """Return *html* with GA4 snippet inserted before ``</head>``."""
    events_js = "\n".join(
        EVENT_SNIPPET.format(name=ev, mid=measurement_id) for ev in (events or [])
    )
    snippet = BASE_SNIPPET.format(mid=measurement_id, events=events_js)
    return html.replace("</head>", snippet + "\n</head>")


__all__ = ["add_ga4_tag"]
