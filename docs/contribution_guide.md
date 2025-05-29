# 🧭 Contribution Guide: O3 Deep Research Repo

To maintain quality, reproducibility, and consistency, all contributions must follow the PR + CI pipeline.

## ✅ Contribution Checklist

- [ ] PR uses the correct template from `.github/pull_request_template.md`
- [ ] Affected files declared and justified
- [ ] No TODO placeholders or incomplete sections remain
- [ ] All `.md` files are linted (via markdownlint-cli2)
- [ ] All links return HTTP 200
- [ ] Genome version for prompts updated in `prompt_genome.json`
- [ ] `CHANGELOG.md` contains a descriptive section of updates

## 📂 Required File Structure

- `docs/prompt/`: Contains prompt kernels (e.g., `prompt_kernel_v3.4.md`)
- `docs/meta/`: Prompt genome + evaluation metadata
- `docs/performance_marketing/`: Research inputs (Google, Meta, NeuroGym, Reforge...)

## 🚨 CI Will Block PRs If
- Missing required `.md` files (e.g., NeuroGym or Reforge)
- `prompt_genome.json` lacks current version
- Broken external links
- TODOs still present

## 🧪 CI runs automatically on every `push` or `PR`

Check `.github/workflows/validate_repo.yml` for details
