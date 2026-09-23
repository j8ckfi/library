---
id: paper:category-aware-swe-experts
type: paper
title: "One to More, More to One: Category-Aware Iterative Expert Training for Software Engineering Agents"
authors:
  - "Jie Zhao"
  - "Ziyu Jiang"
  - "Xiaoxiao Xu"
  - "Lin Qu"
  - "Minghui Shan"
  - "Suhang Zheng"
year: 2026
month: 9
arxiv_id: "2609.23377"
url: "https://arxiv.org/abs/2609.23377"
methods:
  - method:category-aware-swe-experts
cites:
  - paper:mini-swe-agent
  - paper:open-mopd
  - paper:opd
  - paper:codemidas
  - paper:sao
  - paper:miles
  - paper:grpo
tags:
  - post-training
  - agentic
  - swe
  - experts
---

# One to More, More to One: Category-Aware Iterative Expert Training for Software Engineering Agents

## Abstract Summary
Pooled agentic RL on heterogeneous SWE categories shows a category see-saw: gains in one category regress another while aggregate resolution hides the trade-off. The paper organizes executable SWE tasks with SWE Labeler, trains same-origin category experts that alternate Agentic-miniRL with Refresh–Repair–Expand (RRE), then consolidates them by label-routed multi-teacher OPD with ReLU-gated reward extrapolation. No external teacher trajectories. Alibaba Logics-SWE-Qwen3.6-27B line. Mean resolution Pro-618 58.04% (+5.39 vs base) and SWE-bench Multilingual 59.00% (+2.78). Code: alibaba/AgenticBigBang.

## Key Contributions
1. **Category see-saw**: pooled RL can raise the aggregate while \(G_{\mathrm{sim}}=\min_c\Delta_c\) goes negative.
2. **SWE Labeler + RRE experts**: evidence-grounded multi-axis labels; experts refresh instance mastery, Repair-SFT on their own verified successes, then expand the training frontier.
3. **Label-routed MOPD**: ReLU-gated reward extrapolation keeps only each teacher's improving direction over the reference; one deployable student.

## Empirical Highlights
- Pro-618 mean resolution 58.04% (+5.39 vs base). SWE-bench Multilingual 59.00% (+2.78).
- Pro-A/B/C (service-data-security / user-facing / systems-tooling) are the operational evaluation groups on the audit-filtered 618-task Pro split.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.23377`
- Code: `https://github.com/alibaba/AgenticBigBang` (`code_status: released`).
