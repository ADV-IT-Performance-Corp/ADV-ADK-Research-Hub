# Vertex AI Quickstart

This repo is built on Google ADK 1.3 + Vertex AI; all agents communicate via the Google Agent‐to‐Agent protocol (A2A v0.6).

Summary of Google ADK steps for running agents on Vertex AI.

## Setup Steps

1. **Enable required APIs**:

   ```bash
   gcloud services enable \
       aiplatform.googleapis.com \
       cloudbuild.googleapis.com
   ```

2. **Create a service account** and grant Vertex AI roles:

   ```bash
   gcloud iam service-accounts create adk-agent
   gcloud projects add-iam-policy-binding <PROJECT_ID> \
       --member="serviceAccount:adk-agent@<PROJECT_ID>.iam.gserviceaccount.com" \
       --role="roles/aiplatform.user"
   ```

3. **Update `.adk.json`** with your project ID, region, and service account.
   Defaults are provided in `config/vertex_ai.yaml`.

4. **Deploy the flow**:

   ```bash
   gcloud ai agents deploy --config .adk.json
   ```

   This uses `flows/marketing_flow.yaml` by default. The GitHub Actions workflow
   `deploy_vertex_ai.yml` can automate deployment on push.
