---
id: paper:lccp-scaling
type: paper
title: 'Don''t Stop Long-Context Continual Pre-Training Too Early: An Empirical Scaling Law'
authors:
- 'Ziqing Qiao'
- 'Xiaoyue Xu'
- 'Sikui Zhang'
- 'Yinuo Xu'
- 'Bingxiang He'
- 'Chaojun Xiao'
- 'Xu Han'
year: 2026
month: 10
arxiv_id: '2610.29352'
url: https://arxiv.org/abs/2610.29352
methods:
- method:muon2
cites:
- paper:olmo-3
tags:
- pretrain
- long-context
- gotcha
---

# Don't Stop Long-Context Continual Pre-Training Too Early

## Abstract Summary
Long-context continual pre-training (LCCP) follows an additive power law in model size and the short- vs long-context token budgets. Stopping LCCP early leaves LongPPL on the table; the fitted law extrapolates across held-out scales.

## Key Contributions
1. Additive LCCP scaling law plus ContextPPL-style monitoring.

## Empirical Highlights
- Code thunlp/dont-stop-lccp. Does not retarget Muon2 or RLM.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.29352`
- Code: `https://github.com/thunlp/dont-stop-lccp` (`code_status: released`).
