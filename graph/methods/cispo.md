---
id: method:cispo
type: method
title: "CISPO (Clipped IS-weight Policy Optimization)"
category: "rl-alignment"
status: sota
sota_for:
  - task:math-code-rl-dense
  - task:reasoning-rl-alignment
supersedes:
  - method:dapo
last_reviewed: "2026-09-04"
papers:
  - paper:minimax-m1
  - paper:scalerl
  - paper:spurious-advantage-grpo
recipes:
  - recipe:cispo
claims:
  - benchmark: "MATH-500 / AIME 2024 / LiveCodeBench"
    metric: "pass@1 accuracy & sample efficiency"
    value: "Default SOTA for dense long-CoT reasoning RL"
    baseline: "DAPO / GRPO / PPO"
    date: "2026-08-26"
    verified: true
    notes: "MiniMax-M1 and ScaleRL recipe with clipped importance sampling."
tags:
  - post-training
  - rl-alignment
  - dense-rl
  - cispo
  - sota
---

# CISPO (Clipped IS-weight Policy Optimization)

## Method Overview
CISPO (Clipped IS-weight Policy Optimization) establishes the state-of-the-art reinforcement learning standard for dense reasoning models:
1. **Clipped IS-Weight Formulation**: Clips \(\text{sg}(\text{clip}(\rho))\) directly on the importance sampling weight (with stop-gradient) rather than standard PPO-surrogate objective clipping, ensuring every token (including rare forks) receives a non-zero gradient.
2. **Dense Reasoning Alignment**: Maximizes verifiable pass@1 accuracy across competitive math and programming benchmarks.

## Implementation & Frameworks
- Repository: `https://github.com/MiniMax-AI/MiniMax-M1`
- Supported in NeMo-RL and ms-swift via `loss_type=cispo`.

## When to Use
- Default SOTA optimizer for dense model math and code reasoning RL.

## Relation to Existing SOTA
- Remains the dense math/code RLVR default for Pass@1 when labels exist. GRPO inside `method:j-zero` is that method's inner self-play optimizer, not a change to this default.
- For Pass@K / reasoning coverage or a no-backward memory budget, use `method:es-reasoning` on `task:passk-reasoning-coverage`. That is not a GRPO revival and does not replace CISPO.
- Optional token-filter plug-in: `method:gmts`. Example-reweight plug-in: `method:diem`. First-mistake process credit: `method:cliff` (not a PRM; does not replace VeriGate). Sample-level GRPO/OPSD router: `method:self-routing`. Teacher-free unlabeled train-time self-adaptation: `method:opsa`. None of these replace CISPO when labels exist.

## Supersession
- Supersedes `method:dapo` as the dense RL default (DAPO remains as a systems reference).

## Gotchas & Failure Modes
- Group-relative magnitude $|\hat{A}|=\sqrt{n^-/n^+}$ can reward lucky guesses on bounded-answer items, bounded sub-cases inside open math (~56% of MATH-7.5K by answer shape), and search-agent trajectories that cash out via outcome-only exact match (`paper:spurious-advantage-grpo`). CISPO still clips IS weights, not this composition-dependent scale. Do not revive GRPO or promote SignBalance over CISPO.
