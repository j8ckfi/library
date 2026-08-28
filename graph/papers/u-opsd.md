---
id: paper:u-opsd
type: paper
title: "On-Policy Self-Distillation without Any Supervision"
authors:
  - "Yijiang Li"
  - "Bingyang Wang"
  - "Yijun Liang"
  - "Yunjie Tian"
  - "Di Fu"
  - "Nuno Vasconcelos"
year: 2026
month: 8
arxiv_id: "2608.06296"
url: "https://arxiv.org/abs/2608.06296"
methods:
  - method:u-opsd
cites:
  - paper:opd
  - paper:minimax-m1
  - paper:scalerl
  - paper:grpo
tags:
  - post-training
  - distillation
  - label-free
  - self-distillation
  - reasoning
  - u-opsd
---

# On-Policy Self-Distillation without Any Supervision

## Abstract Summary
Unsupervised On-Policy Self-Distillation (u-OPSD) achieves post-training reasoning improvements on large language models without any external supervision, ground-truth annotations, environmental verifiers, or larger teacher models. By sampling multiple rollouts per unlabeled problem and determining an internal consistency pseudo-solution via majority vote with a self-consistency threshold $\tau$, u-OPSD conditions the model's forward distribution on its own pseudo-solution and distills this teacher distribution onto the disagreeing completions. This enables the model to self-correct specifically at token positions where it was confidently erroneous.

## Key Contributions
1. **Unsupervised Self-Conditioning via Consensus**: Discards external ground-truth solutions by identifying consensus pseudo-solutions among multiple on-policy rollouts above confidence threshold $\tau=0.5$.
2. **Disagreement-Targeted Token Distillation**: Focuses the distillation budget strictly on rollouts that disagreed with the consensus pseudo-solution, transferring solution-conditioned next-token distributions into the solution-free policy.
3. **Broad Empirical Superiority**: Evaluated across 5 mathematical reasoning benchmarks (AIME24, AIME25, HMMT25, MATH500, AMC23) on Qwen3 models (4B and 8B in thinking and non-thinking modes, plus Instruct variants). Improves over base models by +8.5% to +10.7% in non-thinking mode, outperforming supervised OPSD by +2.3% to +3.2%, while matching/surpassing supervised OPSD and GRPO in thinking mode.

## Open Source Repository & Resources
- Project Page: `https://williamium3000.github.io/u-opsd/`
- Code Repository: `https://github.com/williamium3000/u-opsd`
