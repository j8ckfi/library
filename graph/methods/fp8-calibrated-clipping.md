---
id: method:fp8-calibrated-clipping
type: method
title: "Calibrated Clipping (FP8 RL)"
category: "training-systems"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the RL engine (SGLang / Megatron / LoRA RL / OPD)"
    reason: "Miles remains the frontier post-train stack; Calibrated Clipping is an FP8 clip-bound plug-in"
    use_instead: "method:miles"
  - when: "choosing the dense Pass@1 algorithm"
    reason: "CISPO remains Pass@1; this paper hosts GRPO/DAPO in VeRL"
    use_instead: "method:cispo"
  - when: "BF16-only stacks where FP8 is not the goal"
    reason: "The failure mode is compounded FP8 noise on the IS ratio; BF16 does not need this calibration"
    use_instead: "method:miles"
assumptions:
  - "Full-pipeline FP8 (rollout + train). TIS-style train–inference mismatch correction is already in play and is not sufficient."
  - "Paper: VeRL + vLLM + TorchAO, GRPO and DAPO, 8B–32B, tensorwise and blockwise FP8, sequence lengths 4K/8K/16K. ByteDance Seed / UW–Madison."
  - "No public standalone GitHub as of 2026-09-23. Implemented in VeRL experiments."
last_reviewed: "2026-09-23"
papers:
  - paper:fp8-calibrated-clipping
recipes:
  - recipe:fp8-calibrated-clipping
claims:
  - benchmark: "Full-pipeline FP8 RL vs BF16, GRPO/DAPO, 8B–32B (VeRL + vLLM + TorchAO)"
    metric: "quality vs BF16 / training throughput"
    value: "BF16-level quality restored; tensorwise up to ~1.5× BF16 throughput"
    baseline: "naive full-pipeline FP8 entropy-surges; TIS mismatch correction does not stop the surge"
    date: "2026-09-23"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.22870"
    notes: "Blockwise FP8 ~10–20% throughput. Not a Miles or CISPO retarget. No public standalone repo."
tags:
  - systems
  - training-systems
  - fp8
  - clipping
  - active
---

# Calibrated Clipping (FP8 RL)

## Method Overview
Full-pipeline FP8 RL still entropy-surges after train–inference mismatch corrections such as TIS. Compounded FP8 quantization noise distorts the importance ratio, disproportionately pushing negative-advantage tokens outside the trust region and zeroing their gradients. Pathological outputs are then not penalized and accumulate.

Calibrated Clipping restores trust-region semantics in quantized space. It matches the FP8 lower-bound clipping quantile to a BF16 reference distribution and rebalances the upper bound so the positive-to-negative update ratio is not warped. Miles remains the engine. CISPO remains Pass@1.

## When to Use
- Full FP8 rollout+train on a GRPO/DAPO-family host where entropy surges and garbled outputs persist after TIS.

## When NOT to Use
- Choosing the RL engine → `method:miles`. Pass@1 algorithm → `method:cispo`. BF16-only stacks → stay on the host loss; this plug-in is for FP8.

## Relation to Existing SOTA
- Active plug-in on `task:frontier-rl-posttrain-stack` beside Miles. Does **not** enter `current_sota`. Does **not** replace `method:miles` or `method:cispo`.

## Gotchas & Failure Modes
- No public standalone GitHub as of 2026-09-23. Reimplement the quantile match inside VeRL; do not treat FlashRL's FP8 rollout patch as this method.
- Calibrating only one clip bound without rebalancing the other recreates the over-clip of negative-advantage tokens.
- Throughput gains are largest for coarse (tensorwise) scaling; blockwise is smaller (~10–20%).
