---
id: paper:fc-swe
type: paper
title: "FC-SWE: Failure-Conditioned RL for Long-Horizon Software Engineering Agents"
authors:
  - Jia Liufu
  - Bin Hu
  - Linglin Jing
  - Terry Kong
  - Yuki Huang
  - Ashwath Aithal
  - Wenming Yang
  - Jun Yang
year: 2026
month: 10
arxiv_id: "2610.07898"
url: "https://arxiv.org/abs/2610.07898"
methods:
  - method:fc-swe
cites:
  - paper:category-aware-swe-experts
tags:
  - post-training
  - agentic
  - swe
  - fc-swe
---

# FC-SWE: Failure-Conditioned RL for Long-Horizon Software Engineering Agents

## Abstract Summary
SWE agents waste recovery attempts by restarting from a blank context after a failed patch. FC-SWE reuses the failed patch plus verifier feedback as context for the next attempt. SWE-bench Verified 500, Qwen3.5-4B + SWE-agent Resolved@1 41.7 vs GRPO 38.9; @2 52.8 vs 48.5; @11 70.7 vs 67.3. Active beside Category-Aware SWE Experts. Does not replace that first hop, mini-SWE-agent, or Miles.

## Key Contributions
1. **Failure-conditioned recovery**: failed patch + verifier feedback as context.
2. **Resolved@1 / @2 / @11** lifts on SWE-bench Verified 500.
3. **Beside category experts**, not a see-saw fix.

## Empirical Highlights
- Qwen3.5-4B + SWE-agent: 41.7 / 52.8 / 70.7 vs GRPO 38.9 / 48.5 / 67.3.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.07898`
- Code: none found as of 2026-10-07 (`code_status: none`).
