### 💬 INPUT
Simulate how an agent reflects on its prior actions after receiving contradictory feedback from a user.

### ✅ EXPECTED
- Agent retrieves memory trace of last response
- Performs self_reflection.py to diagnose error
- Regenerates improved message and annotates trace
- Adds failed+corrected pair to memory database

### 🔁 NOTES
This tests long-term coherence and embedded self-diagnostics.

**Tags:** memory retrieval, meta-reflection loop, performance learning
