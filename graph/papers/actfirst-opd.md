---
id: paper:actfirst-opd
type: paper
title: "Act First, Reason Later: Accelerating On-Policy Distillation for Multi-Turn Agents via Reference-Conditioned Inverse Dynamics"
authors:
  - "Zubin Zheng"
  - "Jiahao Wu"
  - "Shaofeng Zhang"
  - "Zhirui Zhang"
  - "Yew-Soon Ong"
  - "Shengcai Liu"
year: 2026
month: 9
arxiv_id: "2609.36608"
url: "https://arxiv.org/abs/2609.36608"
methods:
  - method:actfirst-opd
cites:
  - paper:opd
tags:
  - post-training
  - distillation
  - agentic
  - on-policy
  - actfirst-opd
---

# Act First, Reason Later: Accelerating On-Policy Distillation for Multi-Turn Agents via Reference-Conditioned Inverse Dynamics

## Abstract Summary
Vanilla multi-turn OPD waits for a full think-then-act response before each environment step. On Qwen3-1.7B ALFWorld, reasoning is 81–95% of per-turn rollout time. Direct-action rollouts are faster but more repetitive and less successful. ActFirst-OPD decouples acting from reasoning: the student infers an action from its current context plus a reference next observation (inverse dynamics), falls back to autonomous next-action prediction when the transition leaves the reference, and asynchronously generates full think-then-act responses on collected contexts for token-level teacher OPD. Average wall-clock speedups vs Vanilla OPD: 2.3× ALFWorld, 1.8× WebShop, 4.9× ScienceWorld on Qwen3 0.6B/1.7B/4B, matching or beating compared OPD baselines on eight of nine benchmark–model settings. Code: `https://anonymous.4open.science/r/ActFirst-OPD`.

## Key Contributions
1. **Reasoning-blocked transitions**: lengthy CoT delays environment steps; naive direct-action rollouts lose quality.
2. **Reference-conditioned inverse dynamics** plus a deviation switch to autonomous next-action prediction.
3. **Async full-response distill**: teacher reverse-KL on think-then-act tokens generated off the critical path.

## Empirical Highlights
- 2.3× / 1.8× / 4.9× wall-clock vs Vanilla OPD on ALFWorld / WebShop / ScienceWorld under matched hardware and update steps.
- Mean task success matches or exceeds compared OPD baselines on 8/9 settings.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.36608`
- Code: `https://anonymous.4open.science/r/ActFirst-OPD` (`code_status: announced`).
