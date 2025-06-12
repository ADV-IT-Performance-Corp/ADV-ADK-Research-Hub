"""Tweak prompts based on performance feedback."""

from __future__ import annotations

from typing import Iterable

__version__ = "3.5.9"


class PromptTuner:
    """Adjust prompts using feedback signals."""

    def tune(self, prompt: str, feedback: Iterable[str]) -> str:
        """Return a refined prompt based on *feedback*."""
        notes = " | ".join(feedback)
        return f"{prompt} -> refined using feedback: {notes}"


__all__ = ["PromptTuner"]
