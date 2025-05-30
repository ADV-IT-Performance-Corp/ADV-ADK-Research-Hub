# Integration Guide for O3 Deep Research (V3.2)

This guide explains how to use this repository as the external knowledge context for the O3 Deep Research prompt (V3.2 and above).

## How to Use

When invoking the O3 prompt, include this reference block in your initial instruction:

```
📘 EXTERNAL KNOWLEDGE CONTEXT:
Use GitHub repository: https://github.com/DanCanadian/ADK

## Core Reference Files

### Foundation
* `ADK_quickstart.md` — ADK system overview and quickstart guide
* `adk_docs_snapshot.md` — Core ADK components and architecture
* `kaggle_prompt_engineering_summary.md` — Advanced prompting techniques (CoT, ReAct, Self-reflection)
* `prompt/prompt_kernel_v3.md` — Complete V3.2 Unified Final prompt

### Performance Marketing
* `performance_marketing/` — Strategic playbooks and industry models:
  - `reforge_growth_loops.md`
  - `neurogym_neuromarketing.md`
  - `meta_ai_strategy.md`
  - `google_insights_summary.md`
  - `ibm_ai_learning.md`
  - `gemini_api_docs.md`
  - `openai_api_docs.md`
  - `microsoft_ai_builder.md`
  - `nvidia_optimizations.md`
  - `amd_developer_ai.md`

### Meta & Simulations
* `meta/prompt_genome.json` — Prompt lineage and evolution tracking
* `meta/meta_evaluation_template.md` — Framework for prompt evaluation
* `simulations/72hr_campaign_sim.md` — 72-hour PPC campaign simulation

## Public Reference Sources

### Cloud & AI Platforms
* [Google Cloud Platform](https://cloud.google.com/)
* [Google AI Studio](https://makersuite.google.com/app/home)
* [Vertex AI](https://cloud.google.com/vertex-ai)
* [Gemini API](https://ai.google.dev/gemini-api)
* [OpenAI Platform](https://platform.openai.com/)

### Enterprise AI
* [IBM watsonx](https://www.ibm.com/watsonx)
* [Microsoft AI Builder](https://www.microsoft.com/ai/builder)
* [Google Cloud AI](https://cloud.google.com/solutions/ai)

### Performance & Hardware
* [NVIDIA AI Enterprise](https://www.nvidia.com/en-us/data-center/products/ai-enterprise/)
* [AMD Instinct](https://www.amd.com/en/products/instinct-ai-accelerators)

**Note:** The O3 Deep Research system is authorized to use any reliable external sources from the internet as needed for comprehensive analysis, with preference given to the sources listed in `source_index.json`.
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
- **Current Version:** 3.5.7
- **Last Updated:** 2025-06-01
- **Compatibility:** Designed for use with O3 Deep Research V3.0 and above
