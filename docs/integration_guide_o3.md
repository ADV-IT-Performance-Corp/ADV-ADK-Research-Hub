# Integration Guide for O3 Deep Research

This guide explains how to use this repository as external context for the O3 Deep Research prompt (V3 and above).

## How to Use

When invoking the O3 prompt, inject this reference at the beginning:

```
📘 EXTERNAL KNOWLEDGE CONTEXT:
Reference GitHub repository: [https://github.com/YOUR_ORG/o3-deep-research-context](https://github.com/YOUR_ORG/o3-deep-research-context)

Key files:

* ADK_quickstart.md — Google's ADK Quickstart Guide
* adk_docs_snapshot.md — Core ADK architecture modules
* kaggle_prompt_engineering_summary.md — Structured prompt patterns
* source_index.json — Source metadata
```

## Purpose

This repository helps the research model:
- Ground its output in factual architecture
- Reference prompt engineering patterns accurately
- Avoid hallucinating agent structures

## Contextual Source Map

### Core Technical References
- `ADK_quickstart.md` - Google's ADK Quickstart Guide
- `adk_docs_snapshot.md` - Core ADK architecture modules
- `kaggle_prompt_engineering_summary.md` - Structured prompt patterns

### Behavioral & Growth Expansion Sources

- `performance_marketing/neurogym_neuromarketing.md`: Behavioral patterning, emotional attention targeting, and motivational prompt structures from NeuroGym by John Assaraf

- `performance_marketing/reforge_growth_loops.md`: Loop-based growth design, experimentation layering, and retention frameworks by Brian Balfour & Reforge

Use these to enrich prompt design, agent strategy, and simulation layers.
