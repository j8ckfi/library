---
id: paper:ugpc
type: paper
title: 'Learning More by Training Less: Uncertainty-Guided Progressive Contraction
  for Efficient Reasoning Post-Training'
authors:
- Suorong Yang
- Jiaxin Wang
- Jiaming Su
- Chentao Yue
- Furao Shen
- Peng Ye
- Soujanya Poria
year: 2026
month: 10
arxiv_id: '2610.12933'
url: https://arxiv.org/abs/2610.12933
methods:
- method:ugpc
cites:
- paper:opd
tags:
- post-training
- distillation
- data-selection
- ugpc
---

# Learning More by Training Less: Uncertainty-Guided Progressive Contraction

## Abstract Summary
UGPC contracts CoT-SFT supervision in two stages. Monte Carlo reasoning trees expose process uncertainty and shrink the teacher corpus. Online routing during SFT then keeps the learner-relevant subset. Matches or beats full-data reasoning SFT with as little as 0.22% of the optimization budget. Plug-in on `task:student-distillation` (CoT-SFT data selection).

## Key Contributions
1. Monte Carlo reasoning trees for process-level uncertainty without internal teacher access.
2. Teacher-side corpus contraction into an uncertainty-rich pool.
3. Learner-aware online routing during SFT.

## Empirical Highlights
- As little as 0.22% of the full-data SFT optimization budget (range 0.22–1.91% on Qwen3.5-4B/9B, DAPO-17k).
- SFT wall-clock 8.47/9.23h → 0.01–0.07h; >800× under ρ=1%.
- Cross-family students at ~0.45% budget; closed-source teachers (DeepSeek-V4-Pro / Kimi-K2.6) up to +13.4%.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.12933`
- Code: `https://github.com/Jackbrocp/Learning-More-by-Training-Less` (`code_status: released`; HTTP 200 as of 2026-10-13).
