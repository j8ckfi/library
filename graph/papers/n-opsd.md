---
id: paper:n-opsd
type: paper
title: "Better Supervision Is Nearby: Neighborhood On-Policy Self-Distillation"
authors:
  - "Xincheng Wei"
  - "Yifan Ding"
  - "Yoshua Li"
  - "Yuquan Lu"
  - "Ziheng Li"
  - "Yi Lu"
  - "Dongsheng Ma"
  - "Rongxiang Weng"
  - "Xunliang Cai"
year: 2026
month: 9
arxiv_id: "2609.39687"
url: "https://arxiv.org/abs/2609.39687"
methods:
  - method:n-opsd
cites:
  - paper:vista
  - paper:oasis
  - paper:dce-srcl
tags:
  - post-training
  - distillation
  - self-distillation
  - privileged-teacher
  - n-opsd
---

# Better Supervision Is Nearby: Neighborhood On-Policy Self-Distillation

## Abstract Summary
Standard privileged OPSD uses one teacher \(\theta\) at every student prefix. Local parameter perturbations yield complementary reference-aligned corrections at different gold positions. N-OPSD builds an offline greedy pool of frozen neighborhood experts, then routes online with MaxPeak plus a quantile rule so the student matches the chosen expert's full next-token distribution under clipped forward-KL. Inference uses only the distilled student. No public code as of 2026-10-02.

## Key Contributions
1. **Neighborhood experts**: frozen local perturbations cover more reference positions than the unperturbed privileged teacher.
2. **Greedy pool**: filtered reference-token gains beyond the pool's current best; highest-peak expert is not always the training target.
3. **Routing split**: MaxPeak picks the anchor token; quantile selection chooses among experts whose top token matches it.

## Empirical Highlights
- AIME 2024 / AIME 2025 / HMMT February 2025 Average@12 vs OPSD, three independent runs: +2.75 / +1.67 / +1.94 on Qwen3-1.7B / 4B / 8B.
- Student-prefix continuations support using the pool beyond the reference trajectories used for selection. Not a VISTA bake-off (64.8→66.9) retarget.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.39687`
- Code: none found as of 2026-10-02 (`code_status: none`).
