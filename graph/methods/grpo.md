---
id: method:grpo
type: method
title: "GRPO (Group Relative Policy Optimization)"
category: "rl-alignment"
status: active
sota_for: []
supersedes:
  - method:ppo-rlhf
superseded_by: method:dapo
last_reviewed: "2026-09-04"
papers:
  - paper:grpo
  - paper:deepseek-r1
  - paper:deepseek-math-paper
  - paper:deepseek-r1-paper
  - paper:spurious-advantage-grpo
recipes:
  - recipe:grpo-trl-training
claims:
  - benchmark: "MATH-500 & AIME 2024"
    metric: "pass@1 accuracy"
    value: 79.8
    baseline: "PPO with Critic Network (Equal GPU hours, 50% less VRAM consumption)"
    date: "2025-01"
    verified: true
    notes: "Averaged across DeepSeek-R1-Zero / R1 scaling runs without supervised fine-tuning warmstart."
tags:
  - rl-alignment
  - reasoning
  - post-training
  - policy-gradient
---

# GRPO (Group Relative Policy Optimization)

## Method Overview
Group Relative Policy Optimization (GRPO) simplifies and scales reinforcement learning for autoregressive language models by removing the need for a separate value/critic network.

For each query \(q\), the actor model samples a group of \(G\) candidate responses \(\{o_1, o_2, \dots, o_G\}\). Reward scores \(\{r_1, r_2, \dots, r_G\}\) are obtained using verifiable rule-based reward functions (e.g. mathematical correctness, code unit test pass, regex XML formatting). The baseline advantage for the \(i\)-th output is computed by standardizing rewards across the group:
\[
A_i = \frac{r_i - \text{mean}(\{r_j\})}{\text{std}(\{r_j\}) + \epsilon}
\]
The policy is then updated using clipped surrogate objectives with a token-level KL divergence penalty against the reference model.

## When to Use
- **Reasoning RL**: Training models on math, competitive programming, and formal logic where deterministic verifiers can score outputs without human annotation.
- **VRAM-Constrained RL**: When training multi-billion parameter models where instantiating a separate critic network would trigger OOM errors.

## Gotchas & Failure Modes
1. **Group Size (\(G\))**: \(G\) must be sufficiently large (typically \(G \geq 8\) or \(16\)) to compute meaningful sample variance; small \(G\) produces noisy advantage estimates.
2. **Reward Variance Collapse**: If all samples in a group produce the exact same reward (e.g. all fail or all succeed), the standard deviation is zero, resulting in zero gradient signal for that batch.
3. **Length Explosion**: Models can develop degenerative verbose rambling to game rule penalties unless length caps or per-token penalties are enforced.
4. **Spurious advantage** (`paper:spurious-advantage-grpo`, 2609.04063): within-group magnitude $|\hat{A}^+|=\sqrt{n^-/n^+}$ does not distinguish reasoning from guessing. Bounded-answer tasks (k-way choice), bounded shapes inside open math (55.95% of MATH-7.5K), and search agents with a large action budget all inflate lucky-correct rollouts. PPO clip bounds the importance ratio, not $|\hat{A}|$. SignBalance is the paper's estimator; it is not a library method and does not retarget CISPO. Dense Pass@1 default remains `method:cispo`.
