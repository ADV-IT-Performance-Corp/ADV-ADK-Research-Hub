"""Generate simple landing page HTML from prompt templates."""

from __future__ import annotations

from pathlib import Path

DEFAULT_PROMPT_TEMPLATE = """\
Landing page for {product}
Headline: Experience {product}
Subheadline: {value_prop}
Key points:
- Clear benefits
- Social proof
- Single call to action
"""

DEFAULT_HTML_TEMPLATE = """\
<!doctype html>
<html>
<head>
  <title>{title}</title>
</head>
<body>
  <h1>{headline}</h1>
  <p>{subheadline}</p>
  <ul>
{bullets}
  </ul>
  <button>{cta}</button>
</body>
</html>
"""


def _load(path: str | Path) -> str:
    return Path(path).read_text(encoding="utf-8")


def create_landing_page(
    product: str,
    value_prop: str,
    *,
    prompt_template: str | Path | None = None,
    html_template: str | Path | None = None,
    cta: str = "Get Started",
) -> str:
    """Return HTML for a basic landing page."""
    pt = prompt_template
    if pt is None:
        prompt = DEFAULT_PROMPT_TEMPLATE
    else:
        pt_text = _load(pt) if isinstance(pt, (str, Path)) else pt
        prompt = pt_text
    prompt = prompt.format(product=product, value_prop=value_prop)

    lines = [line.strip() for line in prompt.splitlines() if line.strip()]
    headline = next(
        (
            line.split(":", 1)[1].strip()
            for line in lines
            if line.startswith("Headline:")
        ),
        f"Experience {product}",
    )
    subheadline = next(
        (
            line.split(":", 1)[1].strip()
            for line in lines
            if line.startswith("Subheadline:")
        ),
        value_prop,
    )
    bullet_items = [line.lstrip("- ") for line in lines if line.startswith("-")]
    bullets_html = "\n".join(f"    <li>{item}</li>" for item in bullet_items)

    ht = html_template
    if ht is None:
        html = DEFAULT_HTML_TEMPLATE
    else:
        html = _load(ht) if isinstance(ht, (str, Path)) else ht

    return html.format(
        title=product,
        headline=headline,
        subheadline=subheadline,
        bullets=bullets_html,
        cta=cta,
    )


__all__ = ["create_landing_page"]
