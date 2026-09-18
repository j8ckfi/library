---
id: paper:opd-eos
type: paper
title: "When EOS Tokens Disagree: Understanding Length Inflation in On-Policy Distillation"
authors:
  - "Yuxiao Yang"
  - "Tianrun Yu"
  - "Shangzhe Li"
  - "Kaixiang Zhao"
  - "Xuchao Zhang"
  - "Chetan Bansal"
  - "Huaxiu Yao"
  - "Taylor W. Killian"
  - "Weitong Zhang"
year: 2026
month: 9
arxiv_id: "2609.20511"
url: "https://arxiv.org/abs/2609.20511"
methods:
  - method:opd-eos
  - method:opd
cites:
  - paper:opd
tags:
  - post-training
  - distillation
  - opd
  - eos
  - gotcha
---

# When EOS Tokens Disagree: Understanding Length Inflation in On-Policy Distillation

## Abstract Summary
On-policy distillation can inflate student length until the generation budget is exhausted. A load-bearing cause is **termination-token mismatch**: a base student and a post-trained teacher put stopping mass on different EOS ids even when their declared stop sets match (Qwen `<|endoftext|>` vs `<|im_end|>`; Llama one id vs three). The teacher is confident the turn is over on a token the student never samples, so that mass never gets a gradient, while the student's native stop gets no teacher support. Aligning the decoding stop set is not enough. Treating functionally equivalent EOS tokens as one semantic stop action removes most mismatch-driven inflation across Qwen3, Llama, and Gemma. A K2-Horizon stage sweep shows termination preference can flip during training, and a later inflation mode remains after alignment — mismatch is important, not exhaustive. Code: `https://github.com/UNCSciML/opd-eos`.

## Key Contributions
1. **Gotcha on OPD**: teacher/student EOS mismatch suppresses the student's stop action and inflates length.
2. **Semantic-class stop** (`EOS_MODE=semantic_class`): score equivalent EOS ids as one action with summed teacher terminal mass.
3. **Stage-dependent termination** on K2-Horizon; residual late inflation after alignment.

## Empirical Highlights
- Qwen3-1.7B-Base → Qwen3-4B: student stop probability at the actual stop position rises then collapses to ~0 by step 150 without the fix; length saturates the budget.
- Gemma-3-4B (already aligned ids): isolates the loss; semantic class still helps vs other conditions.
- Gemma with the fix: ~100% clip at 7168 → mean ~2000 tokens near the teacher's median, clipping near zero. Llama ~3500–4000 tokens and about half the clip rate.

## Open Source Repository & Resources
- Code: `https://github.com/UNCSciML/opd-eos` (verl vendored + `verl/utils/eos_semantics.py`; Slurm launchers).
- This is a gotcha plus a niche fix on `method:opd`, not a new distill default.
