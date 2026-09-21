---
id: task:mllm-finegrained-perception-rl
type: task
title: "MLLM Fine-grained Perception RL"
domain: "post-training"
summary: "Region-level reinforcement learning for fine-grained image perception: a lightweight RoI proposal network selects coherent regions while a frozen MLLM reader scores them."
scope: "Region-level RL on a small RoI head attached to a frozen MLLM. Actions are coherent image regions; the reader scores leave-one-out gold-answer likelihood. Not prompt curriculum, not video annotation-as-rollout."
out_of_scope:
  - "Online adaptive prompt selection / teacher scaffolding for image/VL GRPO (EPS)"
  - "Video annotation-as-rollout / fine-grained video perception RL (OraRL)"
  - "Single-turn dense text math/code Pass@1 RLVR (CISPO)"
  - "MoE/VL RLVR loss rather than region proposal (SAPO)"
redirects:
  - when: "online adaptive prompt selection / teacher scaffolding for image/VL GRPO"
    to: "task:mllm-rl-prompt-curriculum"
  - when: "video annotation-as-rollout / fine-grained video perception RL"
    to: "task:rl-video-mllm"
  - when: "single-turn dense text math/code Pass@1 RLVR"
    to: "task:math-code-rl-dense"
  - when: "MoE/VL RLVR loss rather than region proposal"
    to: "task:math-code-rl-moe"
current_sota:
  - method: method:vision-rl2
    as_of: "2026-09-21"
    benchmark: "Six-bench average at 16,384 source tokens, Qwen3.5-9B"
    metric: "average accuracy vs base / Vision-OPD-9B"
    value: "80.1 vs 74.6 / 78.7; 4B aligned 71.1 vs SD-RPN 66.6 with 4.2× fewer tokens"
    notes: "Vision-RL2 (2609.19745). Active region-level RL. Method status active (not sota). Does not replace EPS prompt scaffolding."
methods:
  - method:vision-rl2
  - method:eps-prompt-scaffolding
  - method:orarl
  - method:cispo
  - method:sapo
last_reviewed: "2026-09-21"
tags:
  - post-training
  - multimodal-rl
  - finegrained-perception
  - vision-rl2
---

# MLLM Fine-grained Perception RL

## Problem Definition
Fine-grained image perception wastes visual tokens on background while localization still works from a coarse view. This task trains a lightweight region proposal network: connected components of a dense RoI map are the actions, a frozen MLLM reader scores leave-one-out gold-answer log-odds, and sparse encoding zooms the crop. The backbone stays frozen.

This is not a prompt curriculum and not video annotation-as-rollout.

## Evaluation Protocol
- **Primary Benchmarks**: V*, ZoomBench, and the paper's six-bench average at a fixed source-token budget; training-aligned 576-token protocol vs SD-RPN at 4096.
- **Evaluation Pitfalls**: Do not rank this against EPS prompt rewrites or OraRL video annotation-as-rollout. Trailing full-model FT on some benches is the frozen-reader design.

## SOTA Recommendation (as of 2026-09-21)
- **Primary Method (this task only)**: **Vision-RL2** (`method:vision-rl2`, `paper:vision-rl2` `arXiv:2609.19745`). Status `active`. Listed here as first hop; method `sota_for` stays empty.
- **Not This Task**: `method:eps-prompt-scaffolding` remains the multimodal prompt-curriculum first hop; `method:orarl` remains video annotation-as-rollout; `method:cispo` remains dense Pass@1; `method:sapo` remains the MoE/VL loss.
