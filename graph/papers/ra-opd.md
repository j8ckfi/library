---
id: paper:ra-opd
type: paper
title: "When Teacher Guidance Misleads: Reward-Aligned On-Policy Distillation"
authors:
  - "Siyuan Gan"
  - "Yuhan Li"
  - "Xiran Wang"
  - "Linjian Meng"
  - "Boyan Wang"
  - "Zhen Zhao"
  - "Jing Huo"
  - "Yang Gao"
year: 2026
month: 8
arxiv_id: "2608.27960"
url: "https://arxiv.org/abs/2608.27960"
methods:
  - method:ra-opd
cites:
  - paper:opd
  - paper:gkd
tags:
  - post-training
  - distillation
  - on-policy
  - ra-opd
---

# When Teacher Guidance Misleads: Reward-Aligned On-Policy Distillation

## Abstract Summary
Teacher guidance on student prefixes can point away from correct trajectories. RA-OPD keeps a trajectory only when its length-normalized distillation return $G$ agrees in sign with the binary outcome reward $R$, i.e. $(2R-1)G\geq 0$. No extra rollouts or teacher evaluations. Across Qwen3 and DeepSeek-R1 math/code setups, RA-OPD beats standard OPD, ExOPD, and Uni-OPD while matching OPD wall-clock (Uni-OPD is ~3.2x slower because it needs group rollouts).

## Key Contributions
1. **Absolute per-trajectory reliability** vs Uni-OPD's relative group margin: well-defined with one rollout per prompt and for reward-homogeneous groups.
2. **Zero extra sampling**: reuses the OPD trajectory and teacher log-probs.
3. **Both conflict types matter**: masking only correct-negative or only incorrect-positive helps; masking both is best.

## Empirical Highlights
- Qwen3-4B-Base math avg@k: RA-OPD 45.88 vs OPD 40.68 vs ExOPD 42.36 vs Uni-OPD 41.70.
- Qwen3-8B-Base math avg@k: RA-OPD 49.43 vs OPD 44.34 vs ExOPD 46.95 vs Uni-OPD 45.20.
- DeepSeek-R1-Distill-Qwen-7B (Skywork-OR1-Math-7B teacher) math avg@k: RA-OPD 69.34 vs OPD 64.43 vs Uni-OPD 66.55.
- Qwen3-4B-Base code avg: RA-OPD 58.97 vs OPD +3.93 (HumanEval+ 78.81, MBPP+ 70.97, LiveCodeBench v6 27.14).
- Dropped-trajectory fraction averages 48.63% (Qwen3) and 68.23% (DeepSeek-R1). Training time 4.48h vs OPD 4.38h vs Uni-OPD 14.41h.

## Open Source Repository & Resources
- No official GitHub found as of 2026-09-01. Filter is Algorithm 1 in the paper (`recipe:ra-opd`).
