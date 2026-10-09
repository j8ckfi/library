---
id: paper:mimo-v26
type: paper
title: "MiMo-V2.6: Scaling Reinforcement Learning Towards Self-Improvement"
authors:
  - "Xiaomi LLM-Core Team"
year: 2026
month: 10
arxiv_id: "2610.11959"
url: "https://arxiv.org/abs/2610.11959"
methods:
  - method:mimo-v26
cites:
  - paper:miles
  - paper:rufus-air
tags:
  - training-systems
  - moe
  - rlvr
  - mimo-v26
---

# MiMo-V2.6: Scaling Reinforcement Learning Towards Self-Improvement

## Abstract Summary
Omni-modal MiMo-V2.6 report on scaling RL compute: larger async batches (1568 samples, 2.7-3.7B tokens/step, context up to 1M), mixed-task agent harnesses, and groupwise agentic grading. Freeze the MoE router during RL. Multi-layer reward-hacking defenses. Open-sources training dynamics, RL environments, and RL framework. Beside Miles / Rufus-Air. Not a Miles replacement.

## Key Contributions
1. Scale RL along batch/throughput, environment diversity, and grader compute.
2. Freeze the MoE router during RL; groupwise agentic grading for long-horizon tasks.
3. Infrastructure for mixed-task agentic RL: unified trajectories, multi-framework rollout, train-infer consistency.

## Empirical Highlights
- Async training consumes 1568 samples and 2.7-3.7B tokens per step at context lengths up to 1M.
- Groupwise agentic grading steers toward shorter, more token-efficient solutions.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.11959`
- Code: Training dynamics, RL environments, and RL framework announced in the paper (`code_status: announced` as of 2026-10-09).
