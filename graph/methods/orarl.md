---
id: method:orarl
type: method
title: "OraRL (Annotations as Rollouts for Video MLLMs)"
category: "multimodal-rl"
status: sota
sota_for:
  - task:rl-video-mllm
supersedes: []
papers:
  - paper:orarl
recipes:
  - recipe:orarl
claims:
  - benchmark: "TimeLens (temporal mIoU), GOT-10k (tracking AO), RefCOCO (cIoU), VSI-Bench"
    metric: "perception accuracy & training step time"
    value: "Video-ORA-9B achieves 66.0 mIoU, 78.2 AO, 73.1 VSI-Bench at 2.2x SFT step time (vs 4.9x for GRPO with CoT)"
    baseline: "GRPO with CoT / SFT / Standard Group RL"
    date: "2026-08-27"
    verified: true
    notes: "Treats dataset annotations as oracle rollouts, decouples advantage baseline to prevent advantage inversion, and uses sign-balanced pruning."
tags:
  - video-mllm
  - multimodal-rl
  - post-training
  - orarl
  - sota
---

# OraRL (Annotations as Rollouts for Video MLLMs)

## Method Overview
OraRL optimizes video multimodal language models without requiring slow, expensive chain-of-thought (CoT) rollouts:
1. **Annotation as Oracle Rollout**: Appends ground-truth annotations directly into the sampled on-policy group as high-reward oracle rollouts.
2. **Decoupled Baseline Estimation**: Excludes the oracle from the advantage baseline calculation, ensuring positive on-policy exploration is never inverted to negative advantage.
3. **Oracle-Policy Gap Modulation**: Modulates a directional gain on above-average rollouts and a decaying weight on the detached oracle update as policy performance approaches the oracle.
4. **Sign-Balanced Pruning**: Retains only the oracle and the highest-magnitude positive and negative rollouts for backpropagation, followed by mean and variance correction.

## When to Use
- When post-training multimodal LLMs for video perception tasks (temporal grounding, spatial segmentation, video tracking, video QA).
- When on-policy exploration rarely hits precise spatial/temporal coordinates and CoT rollouts are too slow or compute-prohibitive.

## Relation to Existing SOTA
- Complements `method:sapo` (general multimodal/MoE RL) specifically for sample-starved fine-grained video perception.
