---
id: paper:opd-one-example
type: paper
title: "Rethinking On-Policy Distillation of Large Language Models II: One Training Example"
authors:
  - "Zixuan Fu"
  - "Bingxiang He"
  - "Yuxin Zuo"
  - "Haohuan Huang"
  - "Jinqian Zhang"
  - "Ruhang Xiao"
  - "Cheng Qian"
  - "Qinyu Luo"
  - "Huan-ang Gao"
  - "Yudong Wang"
  - "Zhiyuan Liu"
  - "Ning Ding"
  - "Chaojun Xiao"
year: 2026
month: 9
arxiv_id: "2609.04172"
url: "https://arxiv.org/abs/2609.04172"
methods:
  - method:opd-one-example
  - method:opd
cites:
  - paper:opd
  - paper:open-mopd
  - paper:gkd
tags:
  - post-training
  - distillation
  - on-policy
  - data-efficiency
  - opd
---

# Rethinking On-Policy Distillation of Large Language Models II: One Training Example

## Abstract Summary
Companion to OPD (2604.13016). OPD is data-overfed but algorithm-starved: a single query recovers most of full-data OPD's gain because rollouts already cover most of the states full-data OPD visits, while the student absorbs the remaining teacher-student gap at a rate that barely depends on query count. Sixteen semantically diverse queries reach 98.9% state coverage and match full-data OPD / MOPD. Content-light templates and off-domain WildChat prompts can approach real-query baselines via the same state-coverage mechanism. The bottleneck for a training run is step-efficiency of student absorption, not more prompts.

## Key Contributions
1. **One-shot OPD**: one query recovers most full-data OPD gain across math, code, instruction following, and agentic tool use, and across Qwen, Llama, and OLMo families.
2. **State coverage**: a query is worth the teacher-supervised prefixes its rollouts reach; one query hits 71.5% of full-data clusters (most within 100 steps); 16 semantically distinct queries hit 98.9% and match full data.
3. **Absorption-rate bottleneck**: the fraction of remaining teacher-student gap closed per update declines similarly on one query and on the full 17k set.
4. **Content vs coverage**: WildChat / content-light templates can approach real-query OPD because they start the student reasoning.

## Empirical Highlights
- Math (R1-Distill-1.5B, avg of MATH-500 / AMC 2023 / AIME 2025): one-shot 68.5 vs full-data OPD 69.8 at step 300 (87% of full-data gain; 69% of teacher-student gap); at step 1000, 68.4 vs 72.1 (72% of full-data gain).
- State coverage: 65.9% by step 100, 71.5% by step 300 (one query); 98.9% at 16 semantically diverse queries.
- Cross-domain gap recovery: code 73%, instruction following 66%, agentic tool use 64%.
- Cross-family math (MATH-500 + AMC 2023, AIME 2025 dropped for Llama): R1-Distill-1.5B 77.1 -> 85.5; Llama-3B-It 28.2 -> 40.2; OLMo-7B-It-DPO 70.8 -> 82.4.
- Hard query the student never solves is as effective as an always-solved easy query.

## Open Source Repository & Resources
- Code: `https://github.com/Thinking-Space/One-Shot-OPD` (listed in the HTML paper; not on the abs page). Implemented in veRL.
