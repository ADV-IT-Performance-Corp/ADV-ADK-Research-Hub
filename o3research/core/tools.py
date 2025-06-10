"""Utility helpers for agent input sanitization and output formatting."""

from __future__ import annotations

import re
from collections.abc import Mapping, Sequence
from typing import Any

__all__ = ["sanitize_input", "format_table"]

_CONTROL_CHARS = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")


def _sanitize_str(value: str) -> str:
    """Remove ASCII control characters from a string."""
    return _CONTROL_CHARS.sub("", value)


def sanitize_input(data: str | Sequence[Any] | Mapping[Any, Any]) -> Any:
    """Recursively sanitize strings within *data*.

    Parameters
    ----------
    data:
        String, list, or dictionary containing data to sanitize.

    Returns
    -------
    str | list | dict
        Sanitized version of ``data`` with control characters removed.

    Raises
    ------
    ValueError
        If ``data`` is not a ``str``, ``list`` or ``dict`` or contains
        unsupported types.
    """
    if isinstance(data, str):
        return _sanitize_str(data)
    if isinstance(data, Mapping):
        return {
            sanitize_input(key): sanitize_input(value) for key, value in data.items()
        }
    if isinstance(data, Sequence) and not isinstance(data, (str, bytes, bytearray)):
        return [sanitize_input(item) for item in data]
    raise ValueError("Unsupported data type for sanitization")


def format_table(
    data: Sequence[Mapping[str, Any]],
    headers: Sequence[str] | None = None,
) -> str:
    """Return ``data`` formatted as an ASCII table.

    Parameters
    ----------
    data:
        Iterable of dictionaries representing rows.
    headers:
        Column names to include. If omitted, keys from the first row are used.

    Returns
    -------
    str
        Formatted table. Returns an empty string when ``data`` is empty.

    Raises
    ------
    ValueError
        If ``data`` is not a sequence of mappings or ``headers`` is not valid.
    """
    if not data:
        return ""
    if not isinstance(data, Sequence):
        raise ValueError("Data must be a sequence of mappings")
    if not all(isinstance(row, Mapping) for row in data):
        raise ValueError("Data must contain mapping objects")

    if headers is None or not headers:
        headers = list(next(iter(data)).keys())
    if not isinstance(headers, Sequence) or not all(
        isinstance(h, str) for h in headers
    ):
        raise ValueError("Headers must be a sequence of strings")

    # Determine column widths
    col_widths = {h: len(h) for h in headers}
    for row in data:
        for h in headers:
            value = row.get(h, "")
            col_widths[h] = max(col_widths[h], len(str(value)))

    def _row(values: list[str]) -> str:
        return "| " + " | ".join(values) + " |"

    header_line = _row([h.ljust(col_widths[h]) for h in headers])
    separator = _row(["-" * col_widths[h] for h in headers])

    rows = []
    for row in data:
        cells = [str(row.get(h, "")).ljust(col_widths[h]) for h in headers]
        rows.append(_row(cells))

    return "\n".join([header_line, separator, *rows])
