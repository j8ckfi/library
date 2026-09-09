---
id: paper:dataflex-rl
type: paper
title: "DataFlex-RL: An Evaluation Platform for RLVR Data Policies"
authors:
  - "Hao Liang"
  - "Mingrui Chen"
  - "Hengyi Feng"
  - "Meiyi Qiang"
  - "Wentao Zhang"
year: 2026
month: 9
arxiv_id: "2609.06107"
url: "https://arxiv.org/abs/2609.06107"
methods:
  - method:dataflex-rl
cites:
  - paper:grpo
tags:
  - post-training
  - rlvr
  - data-policy
  - dataflex-rl
---

# DataFlex-RL: An Evaluation Platform for RLVR Data Policies

## Abstract Summary
DataFlex-RL compares RLVR data policies (which rollouts, what weights, which domains) under a shared GRPO recipe. Primary experiment: 13 configurations × 12 matched seeds, Qwen2.5-7B-Base, 12 math/logic/science benches. Uniform GRPO gains +7.76 pp domain-balanced average over the untrained checkpoint. None of eight rollout-selection/reweighting methods has a paired 95% CI excluding zero vs uniform; none of three adaptive mixtures beats a fixed equal mixture at that precision. Llama-3.1-8B-Base 12-seed extension likewise has no consistent winner. Rankings from a math-heavy 6-bench summary vs the 12-bench summary are negatively correlated (r=−0.33). Negative result: changing the data policy changes the process but does not reproducibly beat uniform in these controls. Shelf: ThinkPrior (cold-start waste, also no accuracy claim).

## Key Contributions
1. **Shared GRPO evaluation platform** for data policies.
2. **Negative result at 95% CI** vs uniform.
3. **Eval-summary sensitivity** (6-bench vs 12-bench rankings anti-correlated).

## Empirical Highlights
- Uniform GRPO +7.76 pp vs untrained on 12-bench domain-balanced average.
- Zero of 8 selection/reweight methods beat uniform at paired 95% CI.

## Open Source Repository & Resources
- No official GitHub as of 2026-09-09.
