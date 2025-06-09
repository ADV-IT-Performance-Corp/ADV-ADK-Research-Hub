# AGENTS Guide for ChatGPT

This repository is often used with the ChatGPT GitHub integration. Follow the rules below when interacting with the project.

## 🗂 Where to find documentation
- Most documentation lives in the `docs/` directory. The `README.md` provides an overview and links.
- When citing a file, reference the relative path (for example `docs/github_chatgpt_integration.md`) and include line numbers where relevant.
- For instructions on connecting this repository to ChatGPT see `docs/github_chatgpt_integration.md`.

## ✅ Commit messages and PRs
- Start commit messages with a short prefix such as `feat:`, `fix:` or `chore:` followed by a concise description.
- Merge commits are automatically skipped by the commit prefix check.
- Use the pull request template `.github/pull_request_template.md` and check all relevant boxes.
- Additional contribution requirements are described in [docs/contribution_guide.md](docs/contribution_guide.md).

## 🧪 Tests and checks before PR
Run the same checks that CI performs in `.github/workflows/validate_repo.yml`:
1. Lint Markdown files with `markdownlint-cli2`.
2. Validate JSON files using `jq` and YAML files using `yamllint`.
3. Search for `TODO:`, `Coming soon`, or `placeholder` in documentation.
4. Ensure required files exist and versions are consistent.
5. Validate the golden prompt files in `tests/golden_prompts/`.

All checks should pass before opening a pull request.
