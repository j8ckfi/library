---
id: paper:autosft
type: paper
title: 'AutoSFT: An Agentic System for Automated Data Research in Supervised Fine-Tuning'
authors:
- Bingxiang He
- Pengqi Sun
- Shihao Peng
- Shaoxuan Li
- Huiyu Xiao
- Hongjian Shi
- Zixuan Fu
- Ziqing Qiao
- Yuxin Zuo
- Cheng Qian
- Xinqiang Yu
- Jiayi Li
- Xiusi Chen
- Yizhen Song
- Xiangyang Wang
- Iofai Lei
- Yudong Wang
- Ning Ding
- Zhiyuan Liu
- Xiaozhi Wang
- Chaojun Xiao
year: 2026
month: 10
arxiv_id: '2610.22194'
url: https://arxiv.org/abs/2610.22194
methods:
- method:autosft
cites:
- paper:olmo-3
tags:
- sft
- data-curriculum
- agentic
---

# AutoSFT

## Abstract Summary
SFT data research is a multi-action loop (proportion, prune, repair, replace, synthesize), not row selection. A single agent collapses to one action and fills its context. AutoSFT splits execution from analysis, gathers proposals, and synthesizes missing capabilities while the model, trainer, and budget stay fixed.

## Key Contributions
1. Multi-action SFT data space instead of one generator.
2. Executor / analysis / synthesis split so context is not discarded mid-search.
3. Retrain-from-base each round so components are attributable.

## Empirical Highlights
- Analysis subagents +6.5 IFEval; synthesis +3.4 IFEval / +2.9 IFBench.
- Same loop on code: analysis +3.7 MBPP+ over a single agent that does not improve.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.22194`
- Code: `https://github.com/Thinking-Space/AutoSFT` (`code_status: released`).

