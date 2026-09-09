---
id: paper:online-draft-cotrain
type: paper
title: "Online Draft Co-Training for Speculative Decoding in Large-Scale, Long-Context RL Post-Training"
authors:
  - "Zili Wang"
  - "Zhaopeng Qiu"
  - "Yuekai Zhang"
  - "Shuang Yu"
  - "Junjie Lai"
year: 2026
month: 9
arxiv_id: "2609.07108"
url: "https://arxiv.org/abs/2609.07108"
methods:
  - method:online-draft-cotrain
cites: []
tags:
  - systems
  - speculative-decoding
  - rl
  - online-draft-cotrain
---

# Online Draft Co-Training for Speculative Decoding in Large-Scale, Long-Context RL Post-Training

## Abstract Summary
Speculative decoding speeds RL rollouts; online co-training of the draft raises acceptance. Scaling to large models and long contexts breaks standard causal context-parallel (no branch attention) and pipeline-parallel (target features span stages). The paper extends packed zigzag ring attention with rank-local branch attention merged into causal main-sequence attention, and TapChannel to ship intermediate target features across PP stages off the pipeline schedule. Co-trained drafts track the policy through 122B with rollout and end-to-end speedups; CP scales at 256K tokens with memory savings. Systems niche, not Uno (diffusion-augmented AR serving) and not a train kernel. Code path: NVIDIA-NeMo/RL#3698.

## Key Contributions
1. **Branch attention under CP** on packed zigzag ring attention.
2. **TapChannel** PP feature transport without changing the pipeline schedule.
3. **Online draft co-train** through 122B / 256K.

## Empirical Highlights
- Drafts track the co-trained policy through 122B with rollout and e2e speedups.
- CP at 256K tokens; PP transport overhead modest.

## Open Source Repository & Resources
- `https://github.com/NVIDIA-NeMo/RL/issues/3698`
