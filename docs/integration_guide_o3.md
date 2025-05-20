# Integration Guide for O3 Deep Research

This guide explains how to use this repository as external context for the O3 Deep Research prompt (V3.0 and above).

## How to Use

When invoking the O3 prompt, inject this reference block into your initial instruction:

```
📘 EXTERNAL KNOWLEDGE CONTEXT:
Use GitHub repository: https://github.com/DanCanadian/ADK

Core reference files:

* `ADK_quickstart.md` — ADK system overview and quickstart guide
* `adk_docs_snapshot.md` — Core ADK components and architecture
* `kaggle_prompt_engineering_summary.md` — Advanced prompting techniques (CoT, ReAct, Self-reflection)
* `o3_deep_research_prompt.md` — Complete V3.0 prompt with instructions
* `performance_marketing/` — Strategic playbooks and industry models:
  - `reforge_growth_loops.md`
  - `neurogym_neuromarketing.md`
  - `meta_ai_strategy.md`
  - `google_insights_summary.md`
  - `ibm_ai_learning.md` (coming soon)

Publicly accessible reference sources:

### Cloud & AI Platforms
* [Google Cloud Docs](https://cloud.google.com/docs)
* [Google Cloud Tutorials](https://cloud.google.com/docs/tutorials?doctype=quickstart)
* [Vertex AI Platform](https://cloud.google.com/vertex-ai/docs/start/introduction-unified-platform)
* [Gemini API Docs](https://ai.google.dev/gemini-api/docs)
* [Gemini on Google Cloud](https://cloud.google.com/gemini/docs)
* [OpenAI Platform Docs](https://platform.openai.com/docs/overview)
* [ChatGPT API Docs](https://chatgpt.com/g/g-I1XNbsyDK-api-docs)

### Enterprise AI & Development
* [IBM Developer AI](https://developer.ibm.com/technologies/artificial-intelligence/)
* [IBM AI Learning Path](https://developer.ibm.com/learningpaths/get-started-artificial-intelligence/)
* [IBM Technology YouTube](https://www.youtube.com/@IBMTechnology)
* [Microsoft AI Builder](https://learn.microsoft.com/en-us/ai-builder/)

### Hardware & Performance
* [NVIDIA Developer Docs](https://docs.nvidia.com/)
* [AMD AI Developer Hub](https://www.amd.com/en/developer.html)

**Note:** The O3 Deep Research system is permitted to use any reliable external sources from the internet as needed for comprehensive analysis.
```

## Purpose

This repository serves as the knowledge foundation for the O3 Deep Research system, providing:
- Structured technical documentation for AI agent development
- Reference architectures and design patterns
- Industry-specific insights and strategies
- Version-controlled prompt engineering resources

## Best Practices

1. **Repository Access**
   - Ensure the repository is public or properly connected via ChatGPT's GitHub integration
   - Use the latest version of files from the `main` branch
   - Reference specific file versions when needed for reproducibility

2. **External Sources**
   - The system can access and reference any reliable external sources
   - All external references should be properly cited
   - Consider adding valuable new sources to the repository's `source_index.json`

3. **Prompt Integration**
   - Always include the full EXTERNAL KNOWLEDGE CONTEXT block in your prompts
   - Reference specific files when making claims or suggestions
   - Use the provided structure for consistent output formatting

## Version Information
- **Current Version:** 3.0
- **Last Updated:** 2025-05-20
- **Compatibility:** Designed for use with O3 Deep Research V3.0 and above
