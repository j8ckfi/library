---
id: method:mixed-precision-scaling
type: method
title: Mixed Precision Scaling Laws (Quantized Pretraining)
category: quantization
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: native FP4 forward/backward hardware training from scratch
  reason: This is a loss-prediction / precision-allocation law, not an FP4 kernel.
    Quartet-II remains NVFP4 training
  use_instead: method:quartet-ii
- when: full-param memory is the constraint rather than pass precision
  reason: SCALE remains the memory-efficient full-param first hop
  use_instead: method:scale
assumptions:
- Qwen3 experiments up to 0.9B / 35.8B tokens plus published Quartet Llama-style
  grid. Forward/backward formats are MXFP8 or NVFP4 (or BF16).
- No public code as of 2026-10-14.
last_reviewed: '2026-10-14'
papers:
- paper:mixed-precision-scaling
recipes:
- recipe:mixed-precision-scaling
claims:
- benchmark: 430M Qwen3 at 12.8B tokens; Qwen3 grid to 0.9B / 35.8B tokens; Quartet
    Llama-style published grid
  metric: val-loss increase vs BF16; held-out MSE vs existing quantized-pretrain laws
  value: fwd-only NVFP4 +0.94–1.22% vs bwd-only +0.32–0.72%; law up to 11× lower MSE
  baseline: BF16; Kumar/Frantar/Panferov capacity laws; Quartet law (single-paper)
  date: '2026-10-14'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.17637
  notes: Table 1 decomposition. Does not retarget Quartet-II as the NVFP4 train default.
tags:
- quantization
- fp4
- scaling-laws
- mixed-precision
- active
---

# Mixed Precision Scaling Laws (Quantized Pretraining)

## Method Overview
Fit \(L(N,D;\psi_f,\psi_b)\) with effective parameter/data rescalings \(\rho_N(\psi_f),\rho_D(\psi_b)\) plus additive persistent optimization-error terms \(\varepsilon_f,\varepsilon_b\). Forward quantization hits capacity and rounding-boundary oscillation; backward quantization hits biased gradients. Layer-wise mix interpolates two scheme losses with a block-selection exponent.

## When to Use
- Choose which pass (or which Transformer blocks) to keep in MXFP8 / BF16 vs NVFP4 before a quantized pretrain run.

## When NOT to Use
Native FP4 training kernels → `method:quartet-ii`. Optimizer-state / full-param memory → `method:scale`. RL train–rollout FP4 mismatch → `method:trace` / `method:triage`.

## Relation to Existing SOTA
Active plug-in on `task:fp4-hardware-training` (`sota_for: []`). Mention on `task:full-param-memory-efficient-pretrain`. Does **not** replace Quartet-II / MXFP4.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-14.
- Uniform 4-bit (even Quartet II) still trails BF16 on the 430M ablation; the law is for mixed precision, not a claim that NVFP4 matches BF16.
- Single-paper baselines vs prior quantized-pretrain laws. No library supersession.
