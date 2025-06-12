# ADK Quickstart Snapshot

This file summarizes the official Agent Development Kit (ADK) quickstart from Google Cloud.

Reference: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-development-kit/quickstart

## Summary
The ADK helps build modular, scalable agents that can:
- Handle multi-step tasks
- Maintain memory and state
- Use caching, token optimization, and reflection loops

## Key Concepts
- `google.adk.Agent`: interface for all agents
- `semantic_cache`: stores recent prompts + responses
- `token_optimizer`: trims prompt tokens to stay efficient
- `few_shot_selector`: selects best few-shot examples
- `self_reflection`: allows the agent to score and improve its own answers

## Deployment Targets
- Google AI Studio
- Cloud Run or Cloud Functions
- Vertex AI + Langchain style chains
