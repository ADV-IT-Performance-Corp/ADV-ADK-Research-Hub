# Utility Scripts

Two helper scripts streamline validation and development:

* `setup_env.sh` – Installs Node.js, markdownlint, `jq`, and `yamllint` so local
  checks match CI. Run once after cloning:

  ```bash
  ./scripts/setup_env.sh
  ```


* `validate_golden_prompts.sh` – Ensures each prompt test contains the required
  `INPUT`, `EXPECTED`, and `NOTES` sections and includes version tags:

  ```bash
  bash scripts/validate_golden_prompts.sh
  ```

Both scripts exit non‑zero on failure so they can be used in automation.

* `refresh_link_cache.py` – Checks external documentation links and updates `docs/link_cache.txt` with the latest HTTP status codes:

  ```bash
  python scripts/refresh_link_cache.py
  ```
