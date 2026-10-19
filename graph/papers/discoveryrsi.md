---
id: paper:discoveryrsi
type: paper
title: 'DiscoveryRSI: Recursively Learning to Discover Valuable Hypotheses'
authors:
- 'Jianyuan Zhong'
- 'Chenwei Wu'
- 'Zhaochen Yu'
- 'Xixian Jiang'
- 'Xuewei Li'
- 'Hao Xiao'
- 'Xilin Dai'
- 'Junyang Wang'
- 'Jiaru Zou'
- 'Zhiqing Cui'
- 'Boyuan Zheng'
- 'Jing Xiong'
- 'Zhen Zhang'
- 'Qiang Gao'
- 'Michael Morley'
- 'Luis Nakayama'
- 'Qiang Xu'
- 'Liyue Shen'
- 'Tao Gui'
- 'Leo Anthony Celi'
- 'James Zou'
- 'Zhenfei Yin'
- 'Yingcheng Wu'
- 'Ling Yang'
year: 2026
month: 10
arxiv_id: '2610.23839'
url: https://arxiv.org/abs/2610.23839
methods:
- method:discoveryrsi
cites:
- paper:harness-playbook
- paper:harness-rsi
tags:
- harness
- rsi
- science
- active
---

# DiscoveryRSI

## Abstract Summary
Scientific discovery requires developing worthwhile hypotheses into practical investigations, yet learning from this evolving research process remains challenging. We introduce an operational definition of valuable and testable research hypotheses: evidence-grounded claims about consequential uncertainties, coupled with feasible investigations, explicit decision criteria, and alternative explanations. Our DiscoveryRSI framework develops hypothesis trees through multi-agent evolutionary search, compiles selected investigations into executable Harbor tasks, and recursively learns through three mechanisms: hypothesis credit optimization attributes scientific assessments to documented research c

## Key Contributions
1. DiscoveryRSI grows hypothesis trees with multi-agent evolutionary search, compiles selected investigations into Harbor tasks, and learns via hypothesis credit, harness replay, and rediscovery of accepted improvements.

## Empirical Highlights
- 4.86→5.39 after two rounds; DiscoveryRSI-27B 6.3% vs GPT-6 2.5% / Opus 5 2.3%

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.23839`
- Code: `https://github.com/Gen-Verse/DiscoveryRSI` (`code_status: released`).
