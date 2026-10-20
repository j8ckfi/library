---
id: paper:what-rl-brings
type: paper
title: 'What RL Brings to Reasoning: A Few Decisions the Base Model Would Not Make'
authors:
- 'Siyu Zhang'
- 'Yuquan Lu'
- 'Yoshua Y. Li'
- 'Yifan Ding'
- 'Kun Zeng'
- 'Yu Huo'
- 'Yifu Guo'
- 'Rongxiang Weng'
- 'Xunliang Cai'
- 'Xiaoying Tang'
year: 2026
month: 10
arxiv_id: '2610.24663'
url: https://arxiv.org/abs/2610.24663
methods:
- method:cispo
cites:
- paper:minimax-m1
tags:
- rlvr
- gotcha
---

# What RL Brings

## Abstract Summary
On Qwen3-4B-Base vs its GRPO pair (AIME pass@1 10.00→19.32), replacing only the ~4% of greedy tokens where the models disagree recovers 90.5% of the pass@1 gain. Power sampling under the same 8192-token cap adds nothing beyond greedy. At k=256 the sparse-replace decoder solves 67.5% vs RL 61.4%.

## Key Contributions
1. rl-replace localizes RLVR gains to a sparse set of decisions.

## Empirical Highlights
- Code CyrusZhang04/WhatRLBrings. Does not retarget CISPO.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.24663`
- Code: `https://github.com/CyrusZhang04/WhatRLBrings` (`code_status: released`).
