# ✅ Release Checklist — O3 Prompt System (v3.5+)

Use this guide when publishing a new minor version. Complete each step before merging to `main`.

## 🔖 Version Declaration
- Create the prompt file `docs/prompt/prompt_kernel_v3.5.md`.
- Add the version entry to `docs/meta/prompt_genome.json`.
- Update `CHANGELOG.md` with `## [v3.5.x]`.

## 📚 Source Documentation
- Add new research files to `docs/performance_marketing/`.
- Update `source_index.json` with new source tags.

## 🧠 Prompt Validation
- Confirm prompt structure follows the latest O3 spec.
- Include EXTERNAL CONTEXT and ROLE sections.
- Add semantic memory or token optimization notes if applicable.

## 🔗 Link Integrity
- Validate all links using `CI Validate O3 Repo`.
- Ensure no broken external references or redirects.

## 🔍 Prompt Review
- Review with a human strategist.
- Submit through a PR using the provided template.

## 📈 Evaluation Results
- Update `docs/meta/evaluation_results.json` with the new version, scores, reviewer, and date.
- Update `evaluation_results.json`.

## 🧪 Final Test
- Run the CI workflow and confirm all checks pass.
- Execute `scripts/bump_version.sh` and verify version consistency.
- Once complete, merge to `main`.
