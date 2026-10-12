---
id: paper:mcgpo
type: paper
title: Matched-Context Group Policy Optimization for LLM Agent Training
authors:
- Chenxu Zhang
- Yaorui Shi
- Wenlong Zhang
- Jianchao Tan
- Zihan Wang
- Yiming Cheng
year: 2026
month: 10
arxiv_id: '2610.13755'
url: https://arxiv.org/abs/2610.13755
methods:
- method:mcgpo
cites:
- paper:canopy
- paper:sao
tags:
- post-training
- agentic
- gpo
- mcgpo
---

# Matched-Context Group Policy Optimization for LLM Agent Training

## Abstract Summary
Useful action comparisons inside a sibling group depend on matched pre-action context and rubric progress. MCGPO builds weighted pairwise preferences from already-collected trajectories (exact then coarse two-action matching, opposite-fold evidence so candidates are not scored with their own terminals) and adds that auxiliary pairwise loss beside shared GraphGPO task learning. Critic-free; original histories kept.

## Key Contributions
1. Matched-context pairwise preferences from existing sibling rollouts.
2. Opposite-fold evidence so terminals that orient a preference are not the candidate's own outcome.
3. Consistent mean-success lifts vs matched GraphGPO, largest on WebShop Qwen3.

## Empirical Highlights
- See `method:mcgpo` claims (`as_of` 2026-10-12).

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.13755`
- Code: `none found` (`code_status: none`).
