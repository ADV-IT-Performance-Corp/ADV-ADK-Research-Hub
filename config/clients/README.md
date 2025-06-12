# Client Configuration Directory

Place per-client YAML files here. Each file should define the following fields:

```yaml
project_id: "my-gcp-project"
credentials: "/path/to/service_account.json"
region: "us-central1"  # optional
```

The orchestration script in `/orchestration/multi_client_runner.py` will load
all `.yaml` files in this folder and run the workflow for each client.
