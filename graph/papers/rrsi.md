---
id: paper:rrsi
type: paper
title: "RRSI: Regularized Recursive Self-Improvement of Agent Harnesses"
authors:
  - "Peng Xia"
  - "Rujun Han"
  - "Zifeng Wang"
  - "Yanfei Chen"
  - "Yufan Zhang"
  - "Yoonho Lee"
  - "Chengsong Huang"
  - "Han Yu"
  - "Zhongying CuiZhu"
  - "Yifei Ming"
  - "Huaxiu Yao"
  - "Burak Gokturk"
  - "Tomas Pfister"
  - "Chen-Yu Lee"
year: 2026
month: 9
arxiv_id: "2609.24972"
url: "https://arxiv.org/abs/2609.24972"
methods:
  - method:rrsi
cites:
  - paper:harness-playbook
  - paper:neohorse-1
  - paper:sol-pi
  - paper:mini-swe-agent
  - paper:harness-onpolicy-correction
tags:
  - agents
  - agent-harness
  - rsi
  - rrsi
---

# RRSI: Regularized Recursive Self-Improvement of Agent Harnesses

## Abstract Summary
Harness RSI (iterative propose-and-select edits of prompts, control flow, tools, memory, and context around a frozen backbone) overfits the evolve split: in-distribution gains shrink or vanish out of distribution. RRSI keeps the edit space open and regularizes the search. The proposer uses a temporally annealed edit budget, conditions on edit history, and redirects stalled runs toward unexplored components. The selector uses a critic that screens benchmark-specific proposals before evaluation, plus a pruner that drops changes that are too small, too expensive, or no longer useful. Across eight benches in coding, agentic workspace, and engineering design, RRSI gains up to 14.1 points on the evolve split and up to 4.7 on five OOD benches, with about 30% fewer policy tokens than unregularized evolution.

## Key Contributions
1. **Proposal regularization**: annealed edit budget, history-conditioned proposer, exploration of untried components on stall.
2. **Selection regularization**: critic leakage screen before scoring, noise-adjusted floor, cost rule, prune-set of unused machinery.
3. **Transfer evidence**: evolve on one suite, freeze the harness, evaluate held-out and OOD benches without rescoring the search.

## Empirical Highlights
- Gemini 3.5 Flash coding: Terminal-Bench 2.1 64.6 → 78.7 (+14.1); SWE-bench Verified OOD 76.8 → 79.0 (+2.2).
- Claude Opus 4.8 coding: Terminal-Bench 2.1 74.2 → 80.2; SWE-bench Verified 82.0 → 83.8.
- Agentic workspace OOD (JobBench / GDPval / APEX-Agents) gains 3.5–4.7 points; Frontier-Eng +4.3 Medal points (24.3% relative). No held-out split regresses.
- Final harness uses ~30% fewer policy tokens than unregularized evolution.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.24972`
- Code: `https://github.com/google-research/rrsi` (`code_status: released`).
- Project: `https://regularized-rsi.com/`
