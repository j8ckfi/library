---
id: paper:looped-models-done-right
type: paper
title: "Towards Looped Models Done Right, Part II: Rethinking at Fixed Points"
authors:
  - Benhao Huang
  - Chufan Shi
  - Junlin Chen
  - Shicheng Wen
  - Zhengzhong Liu
  - Eric Xing
  - Xuezhe Ma
year: 2026
month: 10
arxiv_id: "2610.06833"
url: "https://arxiv.org/abs/2610.06833"
methods:
  - method:looped-models-done-right
cites:
  - paper:recurrent-looped-transformer
  - paper:smelt
tags:
  - pretraining
  - architecture
  - looped-transformer
  - looped-models-done-right
---

# Towards Looped Models Done Right, Part II: Rethinking at Fixed Points

## Abstract Summary
Huginn-style fixed-point looped LMs: closer recurrent states get to fixed points, the less the path matters. Enables truncated BPTT; terminal KV sharing for decode with almost no accuracy loss; a distilled student that prefills up to 1.79x faster; RL gradients from saved rollout states 2x faster than backprop through the replayed trajectory. Learns the depth prior from prediction feedback (entropy keeps it broad) and uses orthogonal input injection. 100M–1.6B: lower perplexity vs Huginn prior / existing injection. At 1.6B, learned prior with a 3x smaller KV cache matches the downstream average of fixed-depth training with the full cache. Code: https://github.com/ifm-ai/xllm-loop. Active beside RLT; does not retarget RLT or SMELT.

## Key Contributions
1. **Learned depth prior** with an entropy term, vs Huginn's broad prior.
2. **Orthogonal injection** so the state's input-aligned component cannot cancel the injection.
3. **Fixed-point cheap path**: truncated BPTT, terminal KV sharing, distilled prefill up to 1.79x, RL from saved states 2x.

## Empirical Highlights
- 100M–1.6B: lower perplexity vs Huginn prior and existing injection.
- 1.6B: 3x smaller KV matches fixed-depth full-cache downstream average.
- Distilled prefill up to 1.79x; RL saved-state grads 2x.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.06833`
- Code: `https://github.com/ifm-ai/xllm-loop` (`code_status: released`; HTTP 200 as of 2026-10-06).
