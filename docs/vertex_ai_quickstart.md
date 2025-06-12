# Vertex AI Quickstart

Summary of Google ADK steps for running agents on Vertex AI.

* Enable Vertex AI APIs
* Configure service account permissions
* Deploy the agent with `gcloud ai agents deploy`

## Deploying the marketing flow

1. Update `.adk.json` with your project ID and service account.
2. Run:

   ```bash
   gcloud ai agents deploy --config .adk.json
   ```

   This will use `flows/marketing_flow.yaml` as the active flow.
3. The GitHub Actions workflow `deploy_vertex_ai.yml` can automate this step when changes are pushed.
