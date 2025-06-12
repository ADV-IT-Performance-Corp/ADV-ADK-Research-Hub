# Multi-Client Workflow Runner

This guide explains how to execute the marketing workflow for multiple clients.

1. Add a YAML file under `config/clients/` for each client. The file must
   specify at least `project_id` and `credentials`.
2. Adjust `flows/client_workflow.yaml` if your workflow differs from the default
   marketing flow.
3. Run the helper script:

```bash
python orchestration/multi_client_runner.py
```

The script loads every client config and launches the workflow using Vertex AI
when available. If the Google ADK libraries are missing, it falls back to the
local `examples.simple_workflow` implementation.
