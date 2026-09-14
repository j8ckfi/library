---
id: paper:scope-opsd
type: paper
title: "SCOPE-OPSD: Fisher-Conditioned Privileged Subspaces for On-Policy Self-Distillation"
authors:
  - "Yunmeng Chen"
  - "Kunyu Wang"
  - "Peihan Li"
  - "Yi Wang"
  - "Shuyin Xia"
  - "Yi Liu"
  - "Xinyong Cheng"
  - "Dehui Wang"
  - "Xiangyong Zhai"
  - "Yanxing Liu"
  - "Song Liu"
year: 2026
month: 9
arxiv_id: "2609.12579"
url: "https://arxiv.org/abs/2609.12579"
methods:
  - method:scope-opsd
cites:
  - paper:vista
  - paper:nsd
  - paper:grpo
tags:
  - post-training
  - distillation
  - opsd
  - privileged-teacher
  - scope-opsd
---

# SCOPE-OPSD: Fisher-Conditioned Privileged Subspaces for On-Policy Self-Distillation

## Abstract Summary
On-policy self-distillation scores student-generated prefixes with a solution-conditioned self-teacher, but transfers supervision only through next-token probabilities. SCOPE-OPSD asks whether the aligned final-layer teacher-student residual is a useful second channel. It projects that privileged residual onto a frozen rank-64 factor estimated from residual covariance and language-model-head Fisher sensitivity. The auxiliary reuses the forwards already required by OPSD and adds neither rollouts nor inference-time modules. A matched Random control preserves the structured factor's rank and nonzero spectrum and uses per-arm gradient-RMS calibration, isolating orientation from auxiliary strength.

## Key Contributions
1. **Fisher-conditioned privileged subspace**: rank-64 projection of the teacher-student residual, frozen after a 128-prompt calibration.
2. **Matched Random control**: same rank and spectrum, same gradient-RMS scale; tests data-dependent orientation.
3. **Short-budget OPSD protocol**: complete 25/50/75/100-step trajectories on Qwen3-1.7B/4B/8B; step 75 is the shared deployable checkpoint.

## Empirical Highlights
- Step 75 Macro Avg@12 (AIME24/AIME25/HMMT25): Structured 43.33 / 63.80 / 65.28 vs Pure OPSD 41.48 / 62.13 / 64.45 vs matched Random 41.94 / 63.43 / 64.35 on Qwen3-1.7B / 4B / 8B.
- Structured is never below Pure OPSD across 12 scale-checkpoint pairs (tie at 4B step 25); exceeds matched Random in 10 of 12.
- Cross-fitted diagnostic: 4.40x held-out privileged-gap capture vs matched random orientation.
- Rank 64 beats 32 and 128 in the 1.7B step-75 ablation. Local GRPO best checkpoint 39.44 vs Structured 43.33 (contextual, not a matched causal delta).

## Open Source Repository & Resources
- No official GitHub found as of 2026-09-14. Training stack in the paper: PyTorch 2.9.0, VERL with a PPU-compatible backend, FSDP, SGLang eval, OpenThoughts Math OPSD 29,434 examples.
