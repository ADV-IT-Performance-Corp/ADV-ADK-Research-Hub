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

CI enforces specific prefixes (`feat:`, `fix:`, `chore:`, etc.) on every commit.
Automatic merge commits created by Git will fail this check. When pulling the
latest `master` into a feature branch, either squash the merge or reword the
commit so the message starts with an allowed prefix, for example:

```bash
git commit --amend -m "chore: merge master into feature-X"
```

This ensures CI passes for merge commits.

**Note:** Merge commits with messages like `Merge branch 'master'` must be
reworded (e.g., `chore: merge master into feature-X`) or squashed before
pushing. Otherwise CI will block the PR.
