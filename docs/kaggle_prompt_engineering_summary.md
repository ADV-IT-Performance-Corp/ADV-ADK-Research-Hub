# Prompt Engineering Patterns – Kaggle Summary

Source: https://www.kaggle.com/whitepaper-prompt-engineering

## Patterns to Apply

- **Few-shot prompting**: provide 1–3 examples with variation
- **Chain-of-Thought (CoT)**: model walks through reasoning before output
- **ReAct (Reason + Act)**: LLM plans → acts → observes → continues
- **Self-Reflection**: model scores/improves its own answers
- **Semantic memory embedding**: for context reuse across prompts
- **Instructional clarity**: role + task + goal = output reliability

## Deployment Strategy
Use patterns in combination with:
- token economy tracking
- multi-agent orchestration
- fine control over prompt structure (JSON schema / CoT blocks)
