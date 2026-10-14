---
id: task:reasoning-rl-alignment
type: task
title: "Reinforcement Learning & Reasoning Post-Training"
domain: "post-training"
summary: "Aligning foundation language models with rule-based verifiers and group-relative policy optimization for long-horizon mathematical and code reasoning."
redirects:
  - when: "NO-THINK-mode GRPO gains that reactivate THINK-mode behavior"
    to: "paper:thinking-leakage"
current_sota:
  - method: method:cispo
    as_of: "2026-08-26"
    benchmark: "AIME 2024 / MATH-500"
    metric: "pass@1 accuracy"
    value: "SOTA for Dense Long-CoT"
    notes: "CISPO for dense policies (2506.13585, 2510.13786); SAPO for MoE/VL (2511.20347)."
  - method: method:sapo
    as_of: "2026-08-26"
    benchmark: "Qwen MoE / VL Reasoning"
    metric: "pass@1 accuracy"
    value: "SOTA for MoE/VL RL"
    notes: "SAPO (2511.20347) for MoE and Vision-Language policies."
methods:
  - method:latentgrm
  - method:cispo
  - method:sapo
  - method:opdvr
  - method:dapo
  - method:gspo
  - method:cppo
  - method:dr-grpo
  - method:grpo
  - method:ppo-rlhf
  - method:cliff
  - method:diem
  - method:self-routing
  - method:verigate
  - method:ngu
  - method:eapo
  - method:cis-rl
  - method:graft
last_reviewed: '2026-10-14'
tags:
  - post-training
  - reinforcement-learning
  - reasoning
---

# Reinforcement Learning & Reasoning Post-Training

## SOTA Recommendation (as of 2026-09-04)
- **Dense Policies**: **CISPO** (`method:cispo`). Unchanged.
- **MoE / VL Policies**: **SAPO** (`method:sapo`). Unchanged.
- **Process Supervision**: **VeriGate** (`method:verigate`, 2605.30451). Unchanged.
- **Optional plug-ins (do not steal current_sota)**: `method:cliff` (first-mistake credit, not a PRM), `method:diem` (example reweight), `method:self-routing` (sample-level GRPO/OPSD router), `method:ngu` (async sampler until ≥1 correct; not a CISPO/SAPO/GRPO loss), `method:eapo` (entropy×sign exploration credit), `method:cis-rl` (MoE train–infer mismatch IS), `method:graft` (peer all-fail salvage).
- **Gotcha**: `paper:spurious-advantage-grpo` on group-relative magnitude. Do not revive GRPO.
- **Optional latent generative reward model (not this first hop)**: `method:latentgrm` (`arXiv:2610.09788`) judges in latent space. ~9× shorter eval trajectories; 6–7× faster at vote@5; 4B/8B vote@5 Avg-8 67.8/69.0 vs Rubric-RM 67.0/68.1. Code EADMO/LatentGRM. Does not replace CISPO or SAPO.
- **Gotcha (abstention)**: `paper:llm-abstention` (`arXiv:2610.13821`). RL variants did not consistently improve abstention on Qwen3-14B; a learned answer selector raised TriviaQA coverage 20.2%→30.9% and cut error 23.0%→14.5%. Does not retarget CISPO.
- **Gotcha (thinking leakage)**: `paper:thinking-leakage` (`arXiv:2610.14270`). Qwen3-8B AIME 0.17→0.43 no-think GRPO vs think-mode 0.74; 8D subspace removes 75%. Evaluate NO-THINK RL against a THINK baseline. Does not retarget CISPO.
