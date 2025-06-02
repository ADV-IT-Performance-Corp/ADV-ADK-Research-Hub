# Configuration Settings Reference

This document explains the keys defined in `config/settings.yaml`.

| Key | Description |
|-----|-------------|
| `prompt_version` | Default prompt kernel version used by all agents |
| `routing_weight` | Weighting factor applied by `ConfigAgent` when routing tasks |
| `log_level` | Logging verbosity for the shared logger |
| `event_bus` | Event bus implementation: `async` or `sync` |
| `max_queue_size` | Maximum queue length for the async event bus |
