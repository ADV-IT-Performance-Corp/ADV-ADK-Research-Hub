# GovernanceAgent Concept

The **GovernanceAgent** acts as a supervisory layer that monitors all other agents, enforces compliance rules, and handles escalation. For deployment steps consult the [O3 Integration Guide](integration_guide_o3.md).

## Purpose
- Track agent heartbeats and trigger alerts on failure
- Escalate anomalies to human strategists
- Enforce policy checks before configuration updates

## Heartbeat Logic (Pseudo)

```python
if not agent_heartbeat.ok:
    escalate("Agent offline: " + agent_name)

```

### Coordination Integration

The GovernanceAgent listens on the same Pub/Sub bus used for inter-agent messages. It emits `heartbeat_check` requests and expects a timely `heartbeat_ack` from each agent. Missing acknowledgments trigger a retry and potential escalation.

### Retry & Escalation Flow

1. Send `heartbeat_check` to target agent
2. Wait up to 30 seconds for `heartbeat_ack`
3. If no response, retry twice then send an `escalate` message to the strategist

All escalation events are captured in a persistent audit log. Example entries are shown in the [72-hour simulation](simulations/72hr_campaign_sim.md#sample-log-snippet).

### Heartbeat & Recovery Events
The GovernanceAgent writes timestamped heartbeat acknowledgments to a shared log. Missing heartbeats trigger the retry flow above and are referenced in the simulation logs for clarity.

#### Example Log Extract

```text
2025-05-22T17:15Z OptimizationAgent disabled LinkedIn ad set #32 due to low CTR
2025-05-22T19:30Z GovernanceAgent missing heartbeat from OptimizationAgent; escalation issued
```
