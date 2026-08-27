---
id: paper:sao
type: paper
title: "SAO: Synchronous-Asynchronous Policy Optimization for Agentic RL"
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

# SAO: Synchronous-Asynchronous Policy Optimization for Agentic RL

## Abstract Summary
SAO (Synchronous-Asynchronous Policy Optimization) addresses the challenge of multi-turn agentic environments where tool calls, bash execution, and environment latencies cause severe straggler bottlenecks under synchronous group RL (like GRPO).

## Key Contributions
1. **Async Rollout Buffering**: Decouples environment interaction from policy gradient updates with importance-corrected off-policy weights.
2. **Agentic SOTA**: Default state-of-the-art optimizer for asynchronous agent and tool-use reinforcement learning.

## Open Source Repository
- Implementation: `none found`
