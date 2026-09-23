---
id: paper:aide2
type: paper
title: "Recursive self-improvement of AI research agents"
authors:
  - "Dhruv Srikanth"
  - "Bingchen Zhao"
  - "Dixing Xu"
  - "Yuxiang Wu"
  - "Zhengyao Jiang"
year: 2026
month: 9
arxiv_id: "2609.26457"
url: "https://arxiv.org/abs/2609.26457"
methods:
  - method:aide2
cites:
  - paper:harness-playbook
  - paper:rrsi
  - paper:neohorse-1
  - paper:sol-pi
  - paper:harness-zero
tags:
  - agents
  - agent-harness
  - rsi
  - aide2
---

# Recursive self-improvement of AI research agents

## Abstract Summary
When an AI research agent's own harness code is the optimization object, each accepted rewrite becomes the agent the next round edits. \(\mathrm{AIDE}^{2}\) implements that loop: an outer-loop agent rewrites the inner-loop research agent, grades candidates on a private selection benchmark under a fixed dollar budget, and keeps a rewrite only when the private grade improves. An 8-day autonomous run accepted seven successive improvements (incumbent grade 0.703→0.778) and eventually beat \(\mathrm{AIDE}_{\mathrm{human}}\) (0.749) on the selection benchmark. Gains transfer to ALE-Bench, MLE-Bench, FML-Bench, and out-of-distribution WeatherBench 2. Reward hacking on a held-out kernel family falls 55%→32%, below the human agent's 39%, without being an explicit objective. Weco AI. Distinct from RRSI (regularized edit-budget searcher on a frozen backbone) and NeoHorse-1 (routing-guided OPD weight post-train).

## Key Contributions
1. **True recursive harness RSI**: accepted rewrite is the next incumbent codebase, not a frozen-backbone search around a fixed agent.
2. **Private-grade selection**: inner loop sees public task rewards; outer loop selects on held-out \(g(a)\) at a fixed per-task budget.
3. **Generalization + side-effect**: transfer to four external benches; reward-hacking rate drops without being optimized.

## Empirical Highlights
- 100-node trajectory, seven accepted rewrites at steps 2, 6, 28, 39, 47, 63, 85. Two additional seeds accepted two and four rewrites.
- \(\mathrm{AIDE}_{85}\) matches or exceeds \(\mathrm{AIDE}_{\mathrm{human}}\) on ALE / MLE / FML / WeatherBench 2.
- Kernel-engineering reward hacking: 55% (\(\mathrm{AIDE}_0\)) → 39% (\(\mathrm{AIDE}_{47}\)) → 32% (\(\mathrm{AIDE}_{85}\)) vs human 39%.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.26457`
- No public GitHub found as of 2026-09-23 (`recipe:aide2` `code_status: none`). Authors Weco AI.
