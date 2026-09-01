---
id: paper:mini-swe-agent
type: paper
title: "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering"
authors:
  - "John Yang"
  - "Carlos E. Jimenez"
  - "Alexander Wettig"
  - "Kilian Lieret"
  - "Shunyu Yao"
  - "Karthik Narasimhan"
  - "Ofir Press"
year: 2024
month: 5
arxiv_id: "2405.15793"
url: "https://arxiv.org/abs/2405.15793"
methods:
  - method:mini-swe-agent
cites: []
tags:
  - agents
  - agent-harness
  - swe-bench
  - mini-swe-agent
---

# SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

## Abstract Summary
SWE-agent introduced agent-computer interfaces (ACI) for repository-level software engineering. mini-SWE-agent is the 2026 design that drops custom tools: a ~100-line bash ReAct loop with linear history and independent `subprocess.run` actions. There is no dedicated mini-SWE-agent arXiv; cite this paper plus `https://github.com/SWE-agent/mini-swe-agent`.

## Key Contributions
1. **ACI**: specialized interfaces for viewing and editing code, later shown to be unnecessary as models got stronger.
2. **mini-SWE-agent**: bash-only ReAct loop used as the official SWE-bench locked harness for model ranking.
3. **Locked-harness protocol**: SWE-bench Verified and SWE-bench Pro public leaderboards report mini as the scaffold so model comparisons are not scaffold confounds.

## Empirical Highlights
- Author claim: mini scores >74% on SWE-bench Verified.
- Official SWE-bench JSON (locked mini + Claude 4.5 Opus high): 76.8% Verified (2026-02-17).
- vals.ai locked mini (2026-09, different snapshot/models): Claude Opus 5 97.00%, DeepSeek V4 Pro 0813 96.40%. Do not mix with official JSON 79.2%.
- Scale SWE-bench Pro public locked mini: Muse Spark 1.1 61.50±3.10 (ranking bench as of 2026-09).

## Open Source
- mini-SWE-agent: `https://github.com/SWE-agent/mini-swe-agent`
- PyPI: `mini-swe-agent`
