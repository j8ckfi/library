---
id: paper:truncated-backprop-looped
type: paper
title: 'How Much Gradient Does Truncated Backprop Lose in Looped Transformers?'
authors:
- 'Aur Shalev Merin'
year: 2026
month: 10
arxiv_id: '2610.28871'
url: https://arxiv.org/abs/2610.28871
methods:
- method:looped-models-done-right
- method:recurrent-looped-transformer
cites:
- paper:looped-models-done-right
tags:
- looped-lm
- gotcha
---

# How Much Gradient Does Truncated Backprop Lose in Looped Transformers?

## Abstract Summary
Truncating backprop to the last k loops of a looped transformer throws away a measurable fraction of the weight gradient. On trained models the lost gradient saturates once loop count is well above k (~0.03 from 32 to 64 loops on three models).

## Key Contributions
1. Exact last-k gradient-loss measurement on nine looped LMs.

## Empirical Highlights
- Code Aur-Shalev-Merin/lost-gradient-looped-transformers. Does not retarget Looped Models Done Right or RLT.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.28871`
- Code: `https://github.com/Aur-Shalev-Merin/lost-gradient-looped-transformers` (`code_status: released`).
