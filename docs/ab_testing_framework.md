# A/B Testing and Personalization

The system supports simple A/B testing through the `ABTestingAgent`.

1. **Variant Management**
   - Supply multiple ad creatives to the agent.
   - Metrics are tracked per variant via the metrics pipeline.
2. **Personalization**
   - Use audience segments to route traffic to different variants.
   - Future work can integrate CRM data for deeper personalization.

The agent selects the winning variant based on conversions collected from all integrated platforms.
