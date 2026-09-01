---
id: paper:ce-moe
type: paper
title: "Training Communication-Efficient Mixture-of-Experts Language Models with Layer Re-Configuration"
authors:
  - "Simeng Sun"
  - "Roger Waleffe"
year: 2026
month: 8
arxiv_id: "2608.28511"
url: "https://arxiv.org/abs/2608.28511"
methods:
  - method:ce-moe
cites:
  - paper:deepseek-v4
tags:
  - architecture
  - moe
  - communication
  - ce-moe
---

# Training Communication-Efficient Mixture-of-Experts Language Models with Layer Re-Configuration

## Abstract Summary
Under expert parallelism, all-to-all dispatch and combine can dominate MoE step time. CE-MoE uses a heterogeneous layer pattern that decouples token-mixing depth from channel-mixing depth: expert capacity is concentrated in a few routed MoE layers, while depth is kept by extra token-mixing and dense-FFN layers. Across a 2B–31.5B scaling ladder with matched total and activated parameters, CE-MoE reduces training cost while matching validation loss and downstream scores of full-MoE baselines. At 31.5B it uses 33.3% fewer GPU-hours and improves average downstream score and inference throughput.

## Key Contributions
1. **Layout, not a new router**: concentrate experts in fewer routed layers instead of interleaving MoE after every token-mixing layer.
2. **Matched-parameter scaling ladder** from 2B to 31.5B under expert parallelism.
3. **Communication saving** of 33.3% GPU-hours at 31.5B with better downstream and throughput.

## Empirical Highlights
- Abstract-level claim (preprint): 2B–31.5B matched total and activated params; at 31.5B, 33.3% fewer GPU-hours plus better average downstream score and inference throughput vs full-MoE.
- No public training code as of 2026-09-01.

## Open Source Repository & Resources
- No official GitHub stated on the arXiv page as of 2026-09-01.
