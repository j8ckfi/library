---
id: paper:sao
type: paper
title: "Single-Rollout Asynchronous Optimization for Agentic Reinforcement Learning"
authors:
  - "SAO Research Authors"
year: 2026
month: 7
arxiv_id: "2607.07508"
url: "https://arxiv.org/abs/2607.07508"
methods:
  - method:sao
cites:
  - paper:grpo
  - paper:dr-grpo
tags:
  - post-training
  - rl-alignment
  - agentic
  - async-rl
  - sao
---

# Single-Rollout Asynchronous Optimization for Agentic Reinforcement Learning

## Abstract Summary
SAO (Single-Rollout Asynchronous Optimization) addresses the challenge of multi-turn agentic environments (tool calls, bash execution, software engineering sandboxes) where variable environment latency causes severe straggler bottlenecks under synchronous group RL (like GRPO).

## Key Contributions
1. **Single-Rollout Asynchronous Framework**: Uses 1 rollout per prompt combined with a value model, eliminating synchronous rollout barriers.
2. **Double-Sided Token Clipping**: Employs double-sided token-level clipping bounds to ensure update stability under asynchronous off-policy drift.
3. **Agentic SOTA**: Default state-of-the-art optimizer for asynchronous agent and tool-use reinforcement learning (utilized on GLM-5.2).

## Open Source Repository
- Implementation: `none found`
