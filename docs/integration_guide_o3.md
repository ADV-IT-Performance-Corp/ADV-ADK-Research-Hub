# Integration Guide for O3 Deep Research

This guide explains how to use this repository as external context for the O3 Deep Research prompt (V3 and above).

## How to Use

When invoking the O3 prompt, inject this reference block into your initial instruction:

```
📘 EXTERNAL KNOWLEDGE CONTEXT:
Use GitHub repository: https://github.com/DanCanadian/ADK

Core reference files:

* `ADK_quickstart.md` — ADK startup architecture
* `adk_docs_snapshot.md` — Agent modules: base_agent, semantic_cache, few_shot_selector, etc.
* `kaggle_prompt_engineering_summary.md` — Prompting strategies (CoT, ReAct, Self-reflection)
* `performance_marketing/` — Industry models from Google, Meta, IBM, Reforge, NeuroGym

Publicly accessible reference sources:

* [Google Cloud Docs](https://cloud.google.com/docs)
* [OpenAI Platform Docs](https://platform.openai.com/docs/overview)
* [ChatGPT API Docs GPT](https://chatgpt.com/g/g-I1XNbsyDK-api-docs)
* [IBM Developer AI](https://developer.ibm.com/technologies/artificial-intelligence/)
* [IBM AI Learning Path](https://developer.ibm.com/learningpaths/get-started-artificial-intelligence/)
* [IBM Tech YouTube](https://www.youtube.com/@IBMTechnology)
```

## Purpose

This repository provides all necessary structured content to ground the O3 Deep Research prompt:
- It aligns prompting and architectural analysis
- Helps simulate agent behavior with performance/ROI context
- Ensures version control and source traceability

Ensure the repository is public or properly connected via ChatGPT's GitHub integration settings.
