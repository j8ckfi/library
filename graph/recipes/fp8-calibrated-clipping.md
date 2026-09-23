---
id: recipe:fp8-calibrated-clipping
type: recipe
title: "Calibrated Clipping for Full-Pipeline FP8 RL"
method: method:fp8-calibrated-clipping
task: task:frontier-rl-posttrain-stack
target_hardware: "VeRL + vLLM + TorchAO box; paper: 8B–32B, seq 4K/8K/16K"
framework: "PyTorch / VeRL / vLLM / TorchAO"
repo_url: none found
code_status: none
pip_dependencies:
  - "torch>=2.5.0"
  - "verl"
  - "vllm"
  - "torchao"
tags:
  - recipe
  - fp8
  - clipping
  - training-systems
---

# Calibrated Clipping for Full-Pipeline FP8 RL

## Hardware & Environment Setup
- No public standalone GitHub as of 2026-09-23 (`arXiv:2609.22870`). `repo_url: none found`. `code_status: none`. Implemented in VeRL experiments (ByteDance Seed / UW–Madison). FlashRL supplies the paper's FP8 rollout patch, not this method.
- Engine default stays Miles. Pass@1 stays CISPO. Skip this plug-in on BF16-only stacks.

## Quickstart Implementation

```python
from __future__ import annotations


def calibrated_bounds(
    fp8_ratios: list[float],
    bf16_ratios: list[float],
    neg_mask: list[bool],
    eps_low: float,
    eps_high: float,
) -> tuple[float, float]:
    """Match FP8 lower-bound clip quantile to BF16; rebalance the upper bound."""
    if len(bf16_ratios) < 2 or len(fp8_ratios) < 2:
        return 1.0 - eps_low, 1.0 + eps_high
    bf16_neg = [r for r, n in zip(bf16_ratios, neg_mask) if n]
    q = (sum(1 for r in bf16_neg if r < 1.0 - eps_low) / len(bf16_neg)) if bf16_neg else 0.0
    fp8_neg = sorted(r for r, n in zip(fp8_ratios, neg_mask) if n)
    if not fp8_neg:
        return 1.0 - eps_low, 1.0 + eps_high
    idx = min(len(fp8_neg) - 1, max(0, int(q * (len(fp8_neg) - 1))))
    lo = fp8_neg[idx]
    hi = 1.0 + (1.0 - lo) * (eps_high / max(eps_low, 1e-8))
    return lo, hi
```

Recompute bounds from a BF16 reference (or a running BF16-ratio snapshot). Apply the calibrated \([1-\epsilon_{\mathrm{lo}}', 1+\epsilon_{\mathrm{hi}}']\) to the FP8 importance ratio.

## Critical Hyperparameters & Tuning Advice
- Match the **lower-bound** quantile first; then rebalance the upper bound. One-sided calibration over-clips negatives.
- Tensorwise FP8 is the ~1.5× throughput setting; blockwise is ~10–20%.
- TIS-style mismatch correction does not replace this clip calibration.
