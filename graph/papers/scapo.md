---
id: paper:scapo
type: paper
title: "Semifactual Credit-Augmented Policy Optimization"
authors:
  - "Junshu Pan"
  - "Zhizhang Fu"
  - "Shulin Huang"
  - "Yiran Ding"
  - "Zifan Cheng"
  - "Wenqi Shao"
  - "Qiaosheng Zhang"
  - "Yue Zhang"
year: 2026
month: 9
arxiv_id: "2609.40360"
url: "https://arxiv.org/abs/2609.40360"
methods:
  - method:scapo
cites:
  - paper:grpo
  - paper:cliff
tags:
  - post-training
  - rlvr
  - credit-assignment
  - scapo
---

# Semifactual Credit-Augmented Policy Optimization

## Abstract Summary
RLVR models stay sensitive to task-irrelevant prompt features. Semifactual interventions that keep the problem and answer expose token-level drift. Suppressing high-drift candidates at decode already helps without a weight update. GRPO assigns the same outcome advantage to every token and can reinforce that spurious dependence. SCAPO probes fixed responses with semifactuals, estimates group-relative stability, and rescales token credit. Qwen3-4B / 1.7B AIME 2024-2026 +5.63 / +4.17 vs GRPO. Code: DtYXs/SCAPO. HF Daily 2026-10-08. Beside CISPO / Cliff.

## Key Contributions
1. Semifactual prompt probes measure token-level sensitivity while holding the answer fixed.
2. Decode-time suppression of high-drift candidates already lifts reasoning accuracy.
3. SCAPO rescales GRPO token credit by group-relative stability during early training.

## Empirical Highlights
- Qwen3-4B-Base / Qwen3-1.7B-Base AIME 2024-2026 +5.63 / +4.17 vs GRPO.
- Best among compared methods on most math and all OOD benchmarks at both scales.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.40360`
- Code: `https://github.com/DtYXs/SCAPO` (`code_status: released`).
