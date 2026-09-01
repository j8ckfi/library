---
id: paper:foldgrpo
type: paper
title: "Scaling Long-Horizon LLM Agent via Context-Folding"
authors:
  - "Weiwei Sun"
  - "Miao Lu"
  - "Zhan Ling"
  - "Kang Liu"
  - "Xuesong Yao"
  - "Yiming Yang"
  - "Jiecao Chen"
year: 2025
month: 10
arxiv_id: "2510.11967"
url: "https://arxiv.org/abs/2510.11967"
methods:
  - method:foldgrpo
cites: []
tags:
  - agents
  - agent-recursion
  - context-folding
  - foldgrpo
---

# Scaling Long-Horizon LLM Agent via Context-Folding

## Abstract Summary
Context-Folding plus FoldGRPO trains a long-horizon tool agent that keeps a small active context by folding completed sub-trajectories. This is a **trajectory** problem (many tool/web/SWE steps), not dumped-prompt RLM and not the SWE harness default.

SOTA here is 36B-class (Seed-OSS-36B, 32K×10). GPT-5 ReAct is still ahead on the paper's BrowseComp-Plus / SWE-Bench Verified numbers.

## Key Contributions
1. Fold completed sub-trajectories so the active window stays 32K while the logical horizon is longer.
2. FoldGRPO: RL on the folded agent (open reimplementation in `sunnweiwei/FoldAgent` on verl).
3. Equal-context comparison vs ReAct 32K and vs ReAct 327K+GRPO.

## Empirical Highlights (Seed-OSS-36B, 32K×10)
- BrowseComp-Plus: FoldGRPO **0.620** vs ReAct 327K+GRPO 0.540 vs ReAct 32K 0.286.
- SWE-Bench Verified: FoldGRPO **0.580** vs ReAct 327K+GRPO 0.574.
- GPT-5 ReAct still ahead: 0.793 / 0.718. Recorded as frontier-model gap, not a retarget.

## Open Source
- `https://github.com/sunnweiwei/FoldAgent`
