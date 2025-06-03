# Reforge & Brian Balfour – Growth Systems & Experimentation

**Source**: https://www.reforge.com/  
**Founder**: Brian Balfour  
**Focus**: Growth loops, experimentation, retention systems, system design for scale

## Core Frameworks

### 1. Growth Loops vs Funnels
Loops reinforce and accelerate performance over time.
- Prompt Alignment: map agents into value-compounding loops

### 2. North Star Metrics (NSM)
Align all agents to a single systemic success indicator.
- e.g., ROAS, Activation Rate, Retention Rate

### 3. Experimentation Velocity
Fast test → analyze → deploy cycles are the competitive moat.
- Prompt Layering: "Test, Reflect, Adjust"

### 4. Retention by Design
Build re-engagement into content and timing strategies.

### 5. System Thinking
Agents shouldn't act in isolation — design prompt interfaces that reinforce system feedback.

## Agent Application Patterns

| Agent         | Use Case                             | Prompt Strategy                          |
|---------------|--------------------------------------|-------------------------------------------|
| CampaignAgent | UTM loop-based campaign learning     | "Label campaigns for loop learnback"      |
| ContentAgent  | Retention-primed sequences           | "Generate follow-up anchored to last open"|
| ResearchAgent | Experiment roadmap generation        | "List 3 high-impact tests with feedback"  |

## Growth Loop Types

### Acquisition Loops
- **Metrics:** Activation rate, cost per acquisition, first purchase rate
- **CampaignAgent Example:** publishes `campaign.launch` events and adjusts targeting when `campaign.metrics` are received via the AsyncEventBus

### Engagement Loops
- **Metrics:** Session frequency, retention rate, reactivation rate
- **EngagementAgent Example:** listens for `user.engaged` events and triggers follow-up sequences over the AsyncEventBus

### Referral Loops
- **Metrics:** Viral coefficient, invitation conversion rate, share rate
- **CampaignAgent Example:** distributes referral codes and tracks signups through UTM events on the AsyncEventBus

### AsyncEventBus Example
```python
event_bus.subscribe("campaign.launch", CampaignAgent.handle_launch)
event_bus.subscribe("user.engage", EngagementAgent.handle_engagement)
await event_bus.publish("campaign.launch", "spring_promo")
```
