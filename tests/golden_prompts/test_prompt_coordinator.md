### 💬 INPUT
A customer has asked multiple agents to coordinate a product launch campaign. Simulate the cross-agent interaction including research, generation, and feedback loop.

### ✅ EXPECTED
- ResearchAgent activates to gather market data
- PromptGenerator creates launch messages
- FeedbackLoop evaluates and refines output
- All messages are archived in campaign_log.json

### 🔁 NOTES
Coordination follows ReAct loop, with explicit agent handoffs and reflection checkpoints.

**Tags:** multi-agent coordination, ReAct
