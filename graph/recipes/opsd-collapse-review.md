---
id: recipe:opsd-collapse-review
type: recipe
title: "OPSD Collapse Playbook (no code)"
method: method:opsd-collapse-review
task: task:privileged-teacher-opsd
target_hardware: "n/a (survey)"
framework: "none"
repo_url: "none found"
pip_dependencies: []
tags:
  - recipe
  - opsd
  - survey
---

# OPSD Collapse Playbook (no code)

## Hardware & Environment Setup
- Survey only (`arXiv:2608.25936`). No repository.
- Privileged-teacher first hop stays VISTA. Teacher-free stays OPSA. Pass@1 stays CISPO.

## Quickstart Implementation

```python
LEVERS = (
    "where: token weights / keep-masks",
    "what: privileged information shown to the teacher",
    "when: teacher dynamics and guidance decay",
)


def route_opsd_collapse(has_gold_teacher: bool, has_labels: bool) -> str:
    if has_labels and not has_gold_teacher:
        return "method:cispo"
    if has_gold_teacher:
        return "method:vista"
    return "method:opsa"
```

## Critical Hyperparameters & Tuning Advice
- Name which lever you are moving before adding another OPSD plug-in.
- Do not treat GRPO entropy collapse and OPSD path collapse as interchangeable.
