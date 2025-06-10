# ✅ Release Checklist — O3 Prompt System (v3.5+)

## 🔖 Version Declaration
- [ ] Create new prompt file: `docs/prompt/prompt_kernel_v3.5.md`
- [ ] Add new version entry to `docs/meta/prompt_genome.json`
- [ ] Update `CHANGELOG.md` with `## [v3.5.x]`

## 📚 Source Documentation
- [ ] Add any new research files to `docs/performance_marketing/`
- [ ] Update `source_index.json` with new source tags

## 🧠 Prompt Validation
- [ ] Confirm prompt structure follows latest O3 spec
- [ ] Include EXTERNAL CONTEXT and ROLE sections
- [ ] Add semantic memory or token optimization notes if applicable

## 🔗 Link Integrity
- [ ] Validate all links using `CI Validate O3 Repo`
- [ ] Run `bash scripts/online_link_check.sh` to ensure no dead links remain
- [ ] No broken external references or redirects

## 🔍 Prompt Review
- [ ] Review with human strategist
- [ ] Submit through PR using the provided PR template

## 📈 Evaluation Results
- [ ] Update `docs/meta/evaluation_results.json` with the new version, scores, reviewer, and date
- [ ] Update `evaluation_results.json`

## 🧪 Final Test
- [ ] CI runs and passes successfully
- [ ] Run `scripts/bump_version.sh` and verify version consistency
- [ ] Ready for `main` branch merge
