# Utility Scripts

Two helper scripts streamline validation and development:

* `setup_env.sh` – Installs Node.js, curl, markdownlint, `jq`, and `yamllint` so local
  checks match CI. Run once after cloning:

  ```bash
  ./scripts/setup_env.sh
  ```

  The script automatically detects if it is run as root and prefixes
  `apt-get` commands with `sudo` when necessary.

* `validate_golden_prompts.sh` – Ensures each prompt test contains the required
  `INPUT`, `EXPECTED`, and `NOTES` sections and includes version tags:

  ```bash
  bash scripts/validate_golden_prompts.sh
  ```

Both scripts exit non‑zero on failure so they can be used in automation.

* `online_link_check.sh` – Validates external links using `markdown-link-check` (strict by default):

```bash
bash scripts/online_link_check.sh
# or locally ignore failures
bash scripts/online_link_check.sh --warn-only
```

* `generate_evaluation.py` – Computes a weighted evaluation score from a metrics
  file and updates `docs/meta/evaluation_results.json`:

  ```bash
  python scripts/generate_evaluation.py metrics.json
  ```

* `bump_version.sh` – Bumps all documentation references to a new version and writes
  the string to the `VERSION` file. If `CHANGELOG.md` contains an `Unreleased`
  section, it is replaced with the new version and today's date.

  ```bash
  ./scripts/bump_version.sh 3.5.8
  ```
