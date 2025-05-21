# OpenAI API — Function Calls & Prompt Orchestration

**Source**: https://platform.openai.com/docs

## Key Topics
- Function calling for tool use
- Advanced prompt engineering
- Embedding-based retrieval
- Fine-tuning and customization
- Token management

## Use Cases
| Agent         | Action                        | API Capability         | Implementation Notes |
|---------------|-------------------------------|------------------------|----------------------|
| CampaignAgent | Call `predict_performance()`  | Function calling       | Real-time optimization |
| ResearchAgent | Use RAG pipeline              | Embedding + context    | Enhanced knowledge retrieval |
| ContentAgent  | Generate ad variations        | Chat completions       | A/B test content creation |

## Integration with ADK
- Implement `base_agent` with OpenAI function calling
- Use `semantic_cache` for embedding storage
- Add token counting and optimization

## Best Practices
1. Use structured outputs with JSON mode
2. Implement retry logic for API calls
3. Monitor token usage and costs
