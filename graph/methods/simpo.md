---
id: method:simpo
type: method
title: "SimPO (Simple Preference Optimization)"
category: "rl-alignment"
status: sota
sota_for:
  - task:direct-preference-alignment
supersedes:
  - method:dpo
papers:
  - paper:simpo-paper
recipes:
  - recipe:simpo-alignment
claims:
  - benchmark: "AlpacaEval 2 & Arena-Hard"
    metric: "length-controlled win rate"
    value: 44.7
    baseline: "DPO (38.2 on LLaMA3-8B-Instruct)"
    date: "2024-05"
    verified: true
    notes: "Direct reward formulation using length-normalized sequence log probabilities with target margin gamma."
tags:
  - post-training
  - preference-alignment
  - direct-alignment
---

# SimPO (Simple Preference Optimization)

## Method Overview
SimPO (Simple Preference Optimization) simplifies offline direct preference alignment by addressing two major flaws in DPO: reference model memory overhead and length exploitation.

Instead of defining implicit rewards via the ratio between policy and reference log-probabilities \(\log \frac{\pi_\theta(y|x)}{\pi_{\text{ref}}(y|x)}\), SimPO defines the reward directly as the average per-token log-likelihood of the generation:
\[
r_{\text{SimPO}}(x, y) = \frac{\beta}{|y|} \sum_{i=1}^{|y|} \log \pi_\theta(y_i | x, y_{<i})
\]
The loss function minimizes a Bradley-Terry preference objective with an explicit margin target \(\gamma\):
\[
\mathcal{L}_{\text{SimPO}} = -\log \sigma \left( r_{\text{SimPO}}(x, y_w) - r_{\text{SimPO}}(x, y_l) - \gamma \right)
\]

## When to Use
- **Offline Instruction Alignment**: Default choice for aligning instruction-tuned models on paired preference datasets (e.g. UltraFeedback, Orca).
- **GPU Memory Constraints**: Eliminates the reference model entirely from GPU memory, saving 50% activation and parameter VRAM compared to DPO.

## Gotchas & Failure Modes
1. **Target Margin (\(\gamma\))**: Must be tuned appropriately (typical optimal range is \(0.5 \leq \gamma \leq 1.5\)); too large a margin causes gradient saturation.
2. **Pre-training Degradation**: If \(\beta\) is set too high, the model may suffer token probability collapse on out-of-distribution prompts.
