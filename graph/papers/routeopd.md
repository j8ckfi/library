---
id: paper:routeopd
type: paper
title: "Distillation as Probability Transport: Routed On-Policy Distillation"
authors:
  - "Tianle Xia"
  - "Lingxiang Hu"
  - "Yiding Sun"
  - "Linfang Shang"
  - "Ming Xu"
  - "Lan Xu"
  - "Ning Zheng"
  - "Wei Xu"
  - "Jie Jiang"
year: 2026
month: 9
arxiv_id: "2609.08337"
url: "https://arxiv.org/abs/2609.08337"
methods:
  - method:routeopd
cites:
  - paper:opd
  - paper:dapo
tags:
  - post-training
  - distillation
  - on-policy
  - routeopd
---

# Distillation as Probability Transport: Routed On-Policy Distillation

## Abstract Summary
Sampled OPD reduces the teacher to scalar credit on the realized token, which says whether that token should gain or lose probability but not where the mass should go. RouteOPD recasts OPD as teacher-guided probability transport: at each student-visited state it builds a detached union of teacher and behavior-student top-k tokens, splits disagreement into student-excess sources and teacher-deficit destinations, and samples explicit source–destination pairs from the independent-product coupling. Pairwise log-odds are driven toward jointly realizable targets from one bounded teacher potential, with the transport budget adapted to teacher-demand concentration (Herfindahl). Across four teacher–student settings and four math benches, adaptive RouteOPD beats sampled reverse-KL OPD by 2.19–3.61 Avg@16 points (macro +2.70). Default k=32, m=2 adds 2.5% end-to-end time and 2.0GB peak memory.

## Key Contributions
1. **Transport view**: excess sources coupled to deficit destinations, not scalar token credit.
2. **Shared bounded potential**: cycle-consistent pairwise log-odds (independent edge clipping has 27.6% four-cycle violations).
3. **Adaptive budget** from teacher-demand concentration.
4. **O(k+m) routing** after top-k, no extra teacher forward.

## Empirical Highlights
- Qwen3-4B-GRPO→1.7B Avg@16: RouteOPD 33.79 vs sampled-RKL 31.44 vs full-vocab RKL 32.35.
- JustRL-DeepSeek-1.5B→R1-Distill-1.5B: 65.53 vs 63.34 vs 64.40.
- JustRL-Nemotron-1.5B→OpenMath-Nemotron-1.5B: 83.34 vs 79.73 vs 82.13.
- DeepSeek-7B→1.5B: 56.25 vs 53.59 vs 55.07.
- Routing fidelity 90.4 vs sampled-RKL 35.4; leakage median 11.2 vs 70.1 on the fixed probe bank.

## Open Source Repository & Resources
- No official GitHub as of 2026-09-09.
