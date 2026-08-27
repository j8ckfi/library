---
id: method:sspo
type: method
title: "SSPO (Soft Sequence Policy Optimization)"
category: "rl-alignment"
status: active
papers:
  - paper:sspo
recipes:
  - recipe:sspo
claims:
  - benchmark: "Math & Coding Reasoning Benchmarks"
    metric: "accuracy & optimization stability"
    value: "Outperforms GRPO/GSPO/SAPO via soft gated sequence importance weights"
    baseline: "GRPO / GSPO / SAPO"
    date: "2026-02-24"
    verified: true
    notes: "Geometric mean of token-level soft gates (arctan log-ratio) inside sequence-level importance weights."
tags:
  - post-training
  - rl-alignment
  - reasoning
  - sspo
---

# SSPO (Soft Sequence Policy Optimization)

## Method Overview
SSPO (Soft Sequence Policy Optimization) is an off-policy objective in the GRPO algorithm family that combines sequence-level coherence with soft token-level gating:
1. **Geometric Mean Soft Gating**: Computes the geometric mean of token-level soft gates within sequence-level importance weights.
2. **Unified Objective**: Unifies the sequence-level trajectory coherence of GSPO/GMPO with SAPO-style soft bounding.
3. **Arctan Log-Ratio Gate**: Uses an arctan function on token log-probability ratios as the default gating mechanism to smoothly temper extreme off-policy updates.

## When to Use
- Off-policy reinforcement learning for math and code reasoning requiring smooth sequence-level importance weighting without abrupt hard clipping.
