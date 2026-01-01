---
name: reporting-maintainer
description: Report template for Maintainer - metrics, alerts, recommendations
---

# Reporting Template - Maintainer

Use this template to generate your project health report.

## Maintainer Report - [TAG or DATE]

### Executive Summary

| Indicator | Value |
|-----------|-------|
| Overall health | [Good / Warning / Critical] |
| Recommended actions | [number] |
| Files to watch | [number] |
| Critical alerts | [number] |

### Evolution Metrics

| Metric | Current | Previous | Change |
|--------|---------|----------|--------|
| Total lines | X | Y | +/-Z |
| Total files | X | Y | +/-Z |
| Lines added | X | - | - |
| Lines removed | X | - | - |

### Alerts

#### Large Files
| File | Lines | Severity |
|------|-------|----------|
| `path/to/file.py` | 523 | CRITICAL |
| `path/to/other.ts` | 380 | WARNING |

#### TODO/FIXME
- TODO: [count] in [X] files
- FIXME: [count] in [X] files

### Recommendations

#### High Priority
1. [ ] [Urgent action]

#### Medium Priority
2. [ ] [Recommended action]

#### Low Priority
3. [ ] [Optional action]

---

## Useful Commands

```bash
# Count lines by extension
find . -name "*.py" -not -path "./node_modules/*" | xargs wc -l | tail -1

# Files > 300 lines
find . -name "*.py" -exec wc -l {} \; | awk '$1 > 300'

# TODO count
grep -rn "TODO" --include="*.py" | wc -l

# Git stats since tag
git diff --shortstat v0.7.0..HEAD
```

## Reference Thresholds

| Metric | OK | Warning | Critical |
|--------|----|---------|----------|
| Lines/file | < 300 | 300-500 | > 500 |
| Files/folder | < 10 | 10-15 | > 15 |
| Total TODOs | < 10 | 10-20 | > 20 |
