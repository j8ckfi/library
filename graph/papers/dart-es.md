---
id: paper:dart-es
type: paper
title: "DART-ES: Difficulty-Aware Reweighting and Targeted Replay for Fine-Tuning LLMs with Evolution Strategies"
authors:
  - Zhishen Sun
  - Hongzhan Wang
  - Sizhe Dang
  - Guang Dai
  - Haishan Ye
year: 2026
month: 10
arxiv_id: "2610.06993"
url: "https://arxiv.org/abs/2610.06993"
methods:
  - method:dart-es
cites:
  - paper:es-reasoning
tags:
  - post-training
  - evolution-strategies
  - passk
  - dart-es
---

# DART-ES: Difficulty-Aware Reweighting and Targeted Replay for Fine-Tuning LLMs with Evolution Strategies

## Abstract Summary
DART-ES adds difficulty-aware reweighting and targeted replay on top of evolution-strategies LLM fine-tuning. GSM8K avg 73.53 vs ES 72.07 vs GRPO 73.26; five hard math 49.20 vs ES 48.34; 15.2–50.2% faster and 21.1–51.1% less GPU mem vs GRPO. Code szs777/DART-ES-Code. Active beside ES-reasoning. Does not replace ES-reasoning or CISPO.

## Key Contributions
1. **Difficulty-aware reweighting** of ES directions.
2. **Targeted replay** of hard prompts.
3. **Faster / cheaper than GRPO** in the paper's memory comparison.

## Empirical Highlights
- GSM8K 73.53 vs ES 72.07 vs GRPO 73.26.
- Five hard math 49.20 vs ES 48.34.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.06993`
- Code: `https://github.com/szs777/DART-ES-Code` (`code_status: released`; HTTP 200 as of 2026-10-07).
