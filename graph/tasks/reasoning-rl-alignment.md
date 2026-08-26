---
id: task:reasoning-rl-alignment
type: task
title: "Reinforcement Learning & Reasoning Post-Training"
domain: "post-training"
summary: "Aligning foundation language models with rule-based verifiers and group-relative policy optimization for long-horizon mathematical and code reasoning."
current_sota:
  - method: method:grpo
    as_of: "2025-01"
    benchmark: "AIME 2024 / MATH-500"
    metric: "pass@1 accuracy"
    value: 79.8
    notes: "Enables large-scale RL reasoning without separate critic/value networks by baseline-normalizing reward groups."
methods:
  - method:grpo
  - method:ppo-rlhf
tags:
  - post-training
  - reinforcement-learning
  - reasoning
---

# Reinforcement Learning & Reasoning Post-Training

## Problem Definition
Post-training foundation models to generate verifiable reasoning chains (e.g. multi-step mathematical proofs, code synthesis, logic puzzle solving) requires reinforcement learning with deterministic rule-based verifiers and outcome rewards. Standard PPO requires maintaining a separate critic/value model equal in size to the actor, consuming 50% or more of available accelerator memory.

## Evaluation Protocol & Benchmarks
- **Standard Benchmarks**: MATH-500, AIME 2024, GPQA Diamond, LiveCodeBench.
- **Verification Hazards**:
  - Reward hacking when heuristic or LLM-as-a-judge reward models are used without ground-truth format/correctness verifiers.
  - Test-time contamination on standard contest math datasets.

## SOTA Landscape
DeepSeek-R1 popularized large-scale pure RL using **GRPO** (Group Relative Policy Optimization). By computing baseline advantages from a group of sample outputs rather than a value network, memory and compute efficiency improve drastically, allowing training longer reasoning rollouts.
