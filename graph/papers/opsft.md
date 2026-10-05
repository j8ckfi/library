---
id: paper:opsft
type: paper
title: "On-Policy Parameter Update Direction Underlies Generalization in LLM Post-Training"
authors:
  - "Shufan Shen"
  - "Zhongni Hou"
  - "Junshu Sun"
  - "Yufei Zhang"
  - "Wei Lin"
  - "Guojun Yin"
  - "Qingming Huang"
  - "Shuhui Wang"
year: 2026
month: 9
arxiv_id: "2609.36659"
url: "https://arxiv.org/abs/2609.36659"
methods:
  - method:opsft
cites:
  - paper:olmo-3
  - paper:minimax-m1
tags:
  - post-training
  - sft
  - on-policy
  - opsft
---

# On-Policy Parameter Update Direction Underlies Generalization in LLM Post-Training

## Abstract Summary
Post-training generalization tracks whether the parameter update stays aligned with the on-policy (current-model) gradient, not whether the tokens were sampled on-policy. OPSFT applies that diagnosis as a usable SFT variant: constrain or project the SFT update onto the on-policy direction. On Qwen3-4B DeepMath, OPSFT mean 40.11 vs GRPO 38.96 vs SFT 34.22 in 6.4 h vs GRPO 16.5 h. Active plug-in on instruct SFT with a mention on dense math RLVR. Code: `https://github.com/ssfgunner/OPSFT`.

## Key Contributions
1. **Update-direction explanation**: on-policy parameter direction, not rollout policy, drives post-train generalization.
2. **OPSFT**: SFT whose step is aligned with the on-policy gradient.
3. **Qwen3-4B DeepMath mean 40.11** vs GRPO 38.96 vs SFT 34.22 (6.4 h vs 16.5 h); Qwen3-8B 41.67 vs GRPO 40.31 vs SFT 38.41. Post-GRPO continue 38.96→41.36 vs SFT drop to 36.25.

## Empirical Highlights
- Vanilla SFT after GRPO drops 38.96→36.25; OPSFT continues 38.96→41.36.
- CISPO remains Pass@1; OLMo-3 remains instruct SFT default.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.36659`
- Code: `https://github.com/ssfgunner/OPSFT` (`code_status: released`; HTTP 200 as of 2026-10-05).
