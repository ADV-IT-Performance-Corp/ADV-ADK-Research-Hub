# Legacy Version Mapping

This document tracks the migration and deprecation of previous versions of the O3 Deep Research prompt system.

## Version History

### Current Version
- **v3.5.1** (2025-05-23)
  - Location: `docs/prompt/prompt_kernel_v3.5.md`
  - Patch update adding simulation and evaluation sections
- **v3.5.0** (2025-05-22)
  - Location: `docs/prompt/prompt_kernel_v3.5.md`
  - Key Features:
    - Multi-agent coordination
    - ReAct patterns implementation
    - Enhanced CI/CD integration
    - Comprehensive evaluation framework
    - Multi-agent coordination
    - ReAct patterns implementation
    - Enhanced CI/CD integration
    - Comprehensive evaluation framework

### Deprecated Versions

#### v3.4.1 (2025-05-20)
- **Status**: Deprecated
- **Location**: `docs/legacy/prompt/prompt_kernel_v3.4.md`
- **Deprecation Date**: 2025-05-22
- **Migration Notes**:
  - Replaced by v3.5.0 with enhanced multi-agent support
  - Key differences in architecture and evaluation metrics

#### v3.4.0 (2025-05-20)
- **Status**: Deprecated
- **Location**: `docs/legacy/prompt/prompt_kernel_v3.4.md`
- **Deprecation Date**: 2025-05-20

#### v3.2.0 (2025-05-18)
- **Status**: Deprecated
- **Location**: `docs/legacy/prompt/prompt_kernel_v3.md`
- **Deprecation Date**: 2025-05-20

## Migration Guide

### From v3.4.1 to v3.5.0
1. **New Features**:
   - Added multi-agent coordination system
   - Implemented ReAct pattern for better reasoning
   - Enhanced evaluation framework

2. **Breaking Changes**:
   - Updated configuration format
   - New required fields in prompt templates
   - Modified evaluation metrics

3. **Deprecations**:
   - Removed single-agent execution mode
   - Simplified configuration structure

## File Structure Changes

### Added
- `docs/prompt/prompt_kernel_v3.5.md`
- `docs/meta/prompt_evolution_log/v3.5.yaml`
- `docs/meta/meta_evaluation.json`
- `.github/workflows/validate_repo.yml`

### Moved to Legacy
- `docs/prompt/prompt_kernel_v3.4.md` → `docs/legacy/prompt/prompt_kernel_v3.4.md`
- `docs/prompt/prompt_kernel_v3.md` → `docs/legacy/prompt/prompt_kernel_v3.md`

## Version Compatibility

| Component          | v3.5.0 | v3.4.1 | v3.4.0 | v3.2.0 |
|-------------------|--------|--------|--------|--------|
| Multi-Agent      | ✅     | ❌     | ❌     | ❌     |
| ReAct Patterns   | ✅     | ❌     | ❌     | ❌     |
| CI/CD Integration| ✅     | ✅     | ✅     | ❌     |
| Legacy Support   | ✅     | ✅     | ✅     | ❌     |

> Note: This table will be updated with future releases.
