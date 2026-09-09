---
id: paper:datpo
type: paper
title: "Difficulty-Adaptive Tree-Structured Policy Optimization for Expanding Reasoning Coverage in RLVR"
authors:
  - "Youngjun Yu"
  - "Sanghwan Jang"
  - "Hwanjo Yu"
year: 2026
month: 9
arxiv_id: "2609.08650"
url: "https://arxiv.org/abs/2609.08650"
methods:
  - method:datpo
cites:
  - paper:grpo
  - paper:dapo
tags:
  - post-training
  - rlvr
  - passk
  - datpo
---

# Difficulty-Adaptive Tree-Structured Policy Optimization for Expanding Reasoning Coverage in RLVR

## Abstract Summary
RLVR often raises Pass@1 while failing to expand Pass@k because train-time exploration is limited. DATPO (Difficulty-Adaptive Sentence-entropy-guided Tree-structured Policy Optimization) combines three design choices: difficulty-adaptive tree expansion, tree rollouts instead of parallel sampling, and sentence-entropy forking to avoid token-entropy localization. A sibling-diversity advantage (embedding cosine among child blocks) is annealed to keep semantic diversity early then decay. On Qwen2.5-3B-Base and Qwen3-4B-Base trained on MATH, DATPO leads aggregate avg@k and especially pass@k versus GRPO, Dr.GRPO, TreeRL, and AttnRL. Code is based on GRPO-Zero; no separate official repo.

## Key Contributions
1. **Difficulty-adaptive rollout** as a coverage mechanism, not only an efficiency heuristic.
2. **Tree vs parallel**: prefix sharing raises PassRate per generated token.
3. **Sentence-entropy forking** vs token-entropy localization (AIME26 inference PassRate 17.3 vs tok-entropy 12.0).
4. **Annealed sibling-diversity** advantage on block-level PPO.

## Empirical Highlights
- Qwen2.5-3B-Base five-bench: DATPO avg@k 22.4 / pass@k 54.9 vs GRPO 20.7/48.2 vs AttnRL 21.3/53.0.
- Qwen3-4B-Base: 31.3/60.4 vs GRPO 30.1/58.3 vs AttnRL 30.7/57.4.
- OOD: GPQA-Diamond 28.5 vs AttnRL 25.9 (3B); 39.6 vs 38.4 (4B).
- Wall-clock on 1×A100: DATPO 60.3h vs GRPO 26.3h vs AttnRL 55.5h (tree sequential bottleneck).

## Open Source Repository & Resources
- Built on `https://github.com/policy-gradient/GRPO-Zero`. No DATPO-named GitHub as of 2026-09-09.
