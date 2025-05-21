# Microsoft AI Builder — Enterprise AI Automation

**Source**: https://learn.microsoft.com/en-us/ai-builder/

## Overview
AI Builder enables business users to add intelligence to Power Platform solutions with a no-code interface.

## Key Features
- Prebuilt AI models
- Custom model training
- Business process automation
- Power Platform integration
- Security and compliance

## Use Cases
| Agent         | Trigger                       | AI Builder Module      | Implementation Notes |
|---------------|-------------------------------|------------------------|----------------------|
| EngagementAgent | Sentiment-based messaging     | Text classification    | Customer feedback analysis |
| ContentAgent    | Auto-gen email follow-ups     | Language model flow    | Automated responses |
| AnalyticsAgent  | Document processing           | Form processing        | Extract structured data |

## Integration with ADK
- Connect `base_agent` to Power Automate
- Use `semantic_cache` for model outputs
- Implement business process triggers

## Best Practices
1. Start with prebuilt models
2. Monitor model performance
3. Implement human-in-the-loop reviews
