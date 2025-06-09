# 🧭 Contribution Guide: O3 Deep Research Repo

To maintain quality, reproducibility, and consistency, all contributions must follow the PR + CI pipeline.

## ✅ Contribution Checklist

- [ ] PR uses the correct template from `.github/pull_request_template.md`
- [ ] Affected files declared and justified
- [ ] No stub sections remain
- [ ] All `.md` files are linted (via markdownlint-cli2)
- [ ] All links return HTTP 200
- [ ] Genome version for prompts updated in `prompt_genome.json`
- [ ] `CHANGELOG.md` contains a descriptive section of updates
- [ ] `python scripts/generate_evaluation.py tests/sample_metrics.json` run to update evaluation results

## 📂 Required File Structure

- `docs/prompt/`: Contains prompt kernels (e.g., `prompt_kernel_v3.4.md`)
- `docs/meta/`: Prompt genome + evaluation metadata
- `docs/performance_marketing/`: Research inputs (Google, Meta, NeuroGym, Reforge...)

## 🚨 CI Will Block PRs If
- Missing required `.md` files (e.g., NeuroGym or Reforge)
- `prompt_genome.json` lacks current version
- Broken external links
- Unresolved stubs still present

## 🧪 CI runs automatically on every `push` or `PR`

Check `.github/workflows/validate_repo.yml` for details

## 🔨 Commit Messages

CI enforces specific prefixes (`feat:`, `fix:`, `chore:`, etc.) on regular commits.
Merge commits are automatically skipped by CI, so they will not block a build.
If you want to keep a merge commit readable, you can reword it with an allowed
prefix, for example:

```bash
git commit --amend -m "chore: merge master into feature-X"
```

This ensures commit history stays readable.

**Note:** CI skips prefix checks on merge commits, so they won't block the PR.
Rewording them with a prefix (e.g., `chore: merge master into feature-X`) is
still recommended for clarity.

## 📦 Publishing a New Version

1. Update the number in `VERSION` and add an entry to `CHANGELOG.md`.
2. Commit the changes with an appropriate message (e.g., `chore: release vX.Y.Z`).
3. Tag the commit and push the tag:

   ```bash
   git tag vX.Y.Z
   git push origin vX.Y.Z
   ```

4. Build and upload the package to PyPI:

   ```bash
   python -m build
   twine upload dist/*
   ```
