---
id: recipe:opd
type: recipe
title: "OPD Student Distillation Recipe"
method: method:opd
task: task:student-distillation
target_hardware: "8x NVIDIA H100 80GB"
framework: "PyTorch 2.5+ / OPD"
repo_url: "https://github.com/thunlp/OPD"
pip_dependencies:
  - "torch>=2.5.0"
  - "transformers>=4.48.0"
  - "vllm>=0.7.0"
tags:
  - recipe
  - distillation
  - opd
---

# OPD Student Distillation Recipe

```python
import torch

print("OPD student rollout generator and teacher logit scorer initialized")
```

## Part-II query-set guidance (`paper:opd-one-example`)
- Prefer ~16 semantically diverse queries per domain before dumping the full prompt set. Cluster with BGE-M3 (or equivalent) and take one representative per cluster.
- One query already recovers most full-data OPD gain via state coverage; content-light / WildChat prompts can approach real-query baselines. The bottleneck is absorption rate, not more prompts.
- Same loss as this recipe. Details: `recipe:opd-one-example`. Does not replace this host loop.
