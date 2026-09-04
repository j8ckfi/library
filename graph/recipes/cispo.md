---
id: recipe:cispo
type: recipe
title: "CISPO Dense Reasoning RL Recipe"
method: method:cispo
task: task:math-code-rl-dense
target_hardware: "16x NVIDIA H100 80GB"
framework: "PyTorch 2.5+ / MiniMax-M1"
repo_url: "https://github.com/MiniMax-AI/MiniMax-M1"
pip_dependencies:
  - "torch>=2.5.0"
  - "vllm>=0.7.0"
  - "transformers>=4.48.0"
tags:
  - recipe
  - rl-alignment
  - cispo
---

# CISPO Dense Reasoning RL Recipe

```python
import torch

print("CISPO MiniMax-M1 / ScaleRL reasoning RL recipe loaded")
```

## Gotchas
- Group-relative magnitude can still reward lucky guesses on bounded-answer / search-agent settings (`paper:spurious-advantage-grpo`). CISPO clips IS weights; it does not remove composition-dependent $|\hat{A}|$. Do not swap CISPO for SignBalance or revive GRPO.
- Optional plug-ins that do not change this default: `method:gmts` (token filter), `method:diem` (example reweight), `method:cliff` (first-mistake credit), `method:self-routing` (sample-level recipe router).
