---
id: paper:longzero
type: paper
title: 'LongZero: Enhancing Long-Context Reasoning in LLMs from Zero Data'
authors:
- 'Zhennan Wan'
- 'Jianfei Chen'
year: 2026
month: 10
arxiv_id: '2610.30132'
url: https://arxiv.org/abs/2610.30132
methods:
- method:longzero
cites:
- paper:j-zero
tags:
- long-context
- rlvr
- active
---

# LongZero

## Abstract Summary
LongZero has the model propose long, diverse, verifiable reasoning tasks and then RL on those tasks, so long-context gains do not wait on annotated long sequences or a stronger teacher.

## Key Contributions
1. LongZero as an active plug-in on `task:data-free-self-evolution`.

## Empirical Highlights
- lets an LLM improve long-context reasoning from tasks it proposes itself without external corpora or a stronger teacher. Does not retarget `method:j-zero`.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.30132`
- Code: `https://github.com/zhennan1/LongZero` (`code_status: released`).
