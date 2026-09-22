---
id: paper:ier-opd
type: paper
title: "1% of Tokens Can Be Enough: On Gradient Estimation in On-Policy Distillation"
authors:
  - "Huanxin Sheng"
  - "Zhiling Ye"
  - "Haonan Wang"
  - "Jian Wang"
  - "Jinjie Gu"
  - "Jian Kang"
year: 2026
month: 9
arxiv_id: "2609.24432"
url: "https://arxiv.org/abs/2609.24432"
methods:
  - method:ier-opd
cites:
  - paper:opd
  - paper:sparse-opd-supervision
  - paper:ida-opd
  - paper:cal-opd
tags:
  - post-training
  - distillation
  - on-policy
  - sparse-supervision
  - opd
  - ier-opd
---

# 1% of Tokens Can Be Enough: On Gradient Estimation in On-Policy Distillation

## Abstract Summary
Sparse OPD already keeps teacher loss on a small token subset. Usefulness of a token is not the same as reliability of its one-sample reverse-KL gradient: a useful teacher correction can still point the wrong way when the next token is sampled once. IER-OPD studies that estimation error at a fixed prefix in information geometry and defines an information-efficiency ratio as signal over noise under the optimal scalar baseline. A top-K candidate-set approximation ranks tokens by IER and fuses the rank with existing usefulness scores via soft OR / AND, while the training objective stays sampled reverse-KL OPD. On math and medical reasoning, adding IER improves several usefulness selectors; 0.1%–1% token budgets match or exceed full OPD.

## Key Contributions
1. **IER**: signal-to-noise of the one-sample reverse-KL gradient under the variance-minimizing scalar baseline; reciprocal IER is relative MSE.
2. **Candidate-set ranking**: top-K student and teacher logits plus the sampled token approximate full-vocabulary IER cheaply.
3. **IER-OR / IER-AND**: fuse normalized IER rank with usefulness scores; keep sampled reverse-KL, not a new distill loss.

## Empirical Highlights
- JustRL-Nemotron-1.5B → OpenMath-Nemotron-1.5B, Bayes@32: at 0.1% IER 58.9 / 34.1 on AIME26 / HMMT26 vs full OPD 59.9 / 34.7; TA-OPD+IER-AND at 1% is comparable to full OPD.
- JustRL-Qwen3-4B → Qwen3-1.7B: at 0.1% IER exceeds full OPD on three of four benches (AIME25 15.8 vs 14.4; AIME26 15.2 vs 12.5; HMMT25 9.5 vs 8.7). TIP+IER-AND at 0.1% beats full OPD on that pair.
- HealthBench overall: IER 0.1% 45.25 vs full OPD 45.77; TIP+IER-OR 46.08; Prefix+IER-OR lifts Prefix 38.30 → 44.98.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.24432`
- Code: `https://github.com/BruceSheng1202/IER-OPD` (slime / TA-OPD stack; `code_status: released`).
