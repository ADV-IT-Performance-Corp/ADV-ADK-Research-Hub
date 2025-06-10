from pathlib import Path

DEFAULT_PROMPT = "Default prompt text"


def get_prompt(path: Path | str = Path("prompt.txt")) -> str:
    p = Path(path)
    if p.exists():
        return p.read_text(encoding="utf-8")
    return DEFAULT_PROMPT
