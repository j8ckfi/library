---
id: paper:mesh-learning
type: paper
title: "All Work And No Play Makes Jack a Dull Boy: Understanding and Preventing Catastrophic Strategy Collapse in RLVR"
authors:
  - "Qiyuan Huang"
  - "Tianshi Xu"
  - "Meng Li"
year: 2026
month: 10
arxiv_id: "2610.02835"
url: "https://arxiv.org/abs/2610.02835"
methods:
  - method:mesh-learning
cites:
  - paper:minimax-m1
  - paper:grpo
tags:
  - post-training
  - rl-alignment
  - rlvr
  - strategy-collapse
  - mesh-learning
---

# All Work And No Play Makes Jack a Dull Boy: Understanding and Preventing Catastrophic Strategy Collapse in RLVR

## Abstract Summary
RLVR can collapse a diverse strategy set onto one surviving mode even as Pass@1 rises. Mesh Learning is the paper's usable fix: Coach Prompting plus Strategy-Balancing Regularization over \(m\) concurrent strategy heads. Active plug-in beside CISPO on dense math/code RLVR. Code: `https://github.com/Ayanami-0123/Open-Mesh-Learning`.

## Key Contributions
1. **Diagnosis**: catastrophic strategy collapse under outcome RLVR (not just entropy collapse).
2. **Mesh Learning**: Coach Prompting + Strategy-Balancing Regularization.
3. **Qwen3-4B \(m=4\) AIME26 56.7** vs GRPO 43.3; **Qwen2.5-7B \(m=4\) AIME26 13.3** vs GRPO 9.2.

## Empirical Highlights
- Table 2 also reports other benches in the same rows; AIME26 is the headline Pass@1-style number used here.
- GRPO is the paper baseline; CISPO remains the library Pass@1 default.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.02835`
- Code: `https://github.com/Ayanami-0123/Open-Mesh-Learning` (`code_status: released`; HTTP 200 as of 2026-10-05).
