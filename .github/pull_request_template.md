# 🚀 Pull Request Summary - v3.5.10

## 📋 Description of Changes
<!-- Briefly describe what this PR implements or fixes for v3.5.10 -->
- [ ] Added new prompt kernel: `docs/prompt/prompt_kernel_v3.5.md`
- [ ] Added evolution log: `docs/meta/prompt_evolution_log/v3.5.yaml`
- [ ] Updated meta evaluation: `docs/meta/meta_evaluation.json`
- [ ] Updated documentation and references

---

## 🗂 Affected Files (v3.5.10)
<!-- Check all that apply -->

### Core Files
- [ ] `docs/prompt/prompt_kernel_v3.5.md`
- [ ] `docs/meta/prompt_evolution_log/v3.5.yaml`
- [ ] `docs/meta/meta_evaluation.json`

### Test Files
- [ ] `tests/golden_prompts/test_prompt_coordinator.md`
- [ ] `tests/golden_prompts/test_memory_reflection.md`
- [ ] `tests/golden_prompts/test_kpi_optimization.md`

### Supporting Files
- [ ] `docs/source_index.json`
- [ ] `CHANGELOG.md`
- [ ] `README.md`

### CI/CD
- [ ] `.github/workflows/validate_repo.yml`
- [ ] `.github/pull_request_template.md`

---

## 🧪 Golden Prompt Integration
- [ ] Added test_prompt_coordinator.md to `/tests/golden_prompts/`
- [ ] Added test_memory_reflection.md to `/tests/golden_prompts/`
- [ ] Added test_kpi_optimization.md to `/tests/golden_prompts/`
- [ ] CI configured to detect and validate golden prompts
- [ ] Golden prompts align with v3.5.10 kernel strategy

---

## ✅ Validation Checklist
Ensure the following items are checked before requesting review:

- [ ] No `TODO:`, `Coming soon`, or `placeholder` remaining
- [ ] All documentation links pass strict validation
- [ ] `source_index.json` updated if new `.md` was added
- [ ] `CHANGELOG.md` updated with version bump
- [ ] PR title follows format: `feat:` `fix:` `chore:` etc.
- [ ] Merge commits reworded (e.g., `chore: merge master into feature-X`) or squashed
- [ ] Golden prompts pass validation checks
- [ ] All tests are passing

---

## 🧠 Notes & Context (optional)
<!-- Add context for reviewers or document intent -->

### Golden Prompt Details
- **Test Coverage**: Ensure all major prompt patterns are covered
- **Version Compatibility**: All prompts are compatible with v3.5.10
- **Validation**: CI pipeline includes golden prompt validation
