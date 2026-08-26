---
id: task:math-code-rl-dense
type: task
title: "Mathematical and Code RL Reasoning (Dense Policies)"
domain: "post-training"
summary: "Reinforcement learning on verifiable mathematical and coding tasks using dense transformer policies."
current_sota:
  - method: method:dapo
    as_of: "2026-08-26"
    benchmark: "MATH-500 / AIME 2024 / LiveCodeBench"
    metric: "pass@1 accuracy & training stability"
    value: "SOTA for Dense Long-CoT"
    notes: "DAPO with clip-higher, dynamic sampling, token-level loss, overlong shaping. Combine with Dr. GRPO de-biasing."
methods:
  - method:dapo
  - method:dr-grpo
  - method:grpo
tags:
  - post-training
  - reasoning
  - math
  - code
  - dapo
---

# Mathematical and Code RL Reasoning (Dense Policies)

## Problem Definition
Training dense language models to generate long chains of thought (CoT) and verifiable solutions for competitive math and coding problems.

## SOTA Recommendation (as of 2026-08-26)
- **Primary Method**: **DAPO** (`method:dapo`) for dense long-CoT (clip-higher, dynamic sampling, token-level loss, overlong shaping).
- **De-biasing**: Apply **Dr. GRPO** (`method:dr-grpo`) de-biasing (drop length and std-normalization) so incorrect traces don't get rewarded for being long.
- **Reward**: Ground-truth unit-test / math verifier / boxed-answer match. Learned process-reward models (PRMs) are optional and dangerous; if used, gate them behind a verifier (VeriGate-style `paper:verigate`).
