---
id: task:mllm-rl-prompt-curriculum
type: task
title: "MLLM Online RL Prompt Curriculum"
domain: "post-training"
summary: "Online adaptive prompt selection and teacher scaffolding so multimodal RL post-training spends rollout budget on currently informative prompts, not saturated or currently-impossible ones."
scope: "Online adaptive prompt selection and task-preserving teacher scaffolding for multimodal (image/VL) RL post-training. EPS from on-policy rollout rewards; GRPO-family host."
out_of_scope:
  - "Video annotation-as-rollout / fine-grained video perception RL (OraRL)"
  - "Single-turn dense text math/code Pass@1 RLVR (CISPO)"
  - "MoE/VL RLVR loss rather than prompt curriculum (SAPO)"
  - "Static RLVR data-policy evaluation under uniform GRPO (DataFlex-RL)"
  - "RFT example-reweight without prompt rewrite (DIEM)"
  - "Outcome-only long-horizon agent RL (CANOPY / DRACO)"
redirects:
  - when: "video annotation-as-rollout / fine-grained video perception RL"
    to: "task:rl-video-mllm"
  - when: "single-turn dense text math/code Pass@1 RLVR"
    to: "task:math-code-rl-dense"
  - when: "MoE/VL RLVR loss rather than prompt curriculum"
    to: "task:math-code-rl-moe"
  - when: "outcome-only long-horizon agent RL (coverage / anti-drift or rubric credit)"
    to: "task:outcome-only-long-horizon-agent-rl"
current_sota:
  - method: method:eps-prompt-scaffolding
    as_of: "2026-09-15"
    benchmark: "Geometry3K / MMK12, Qwen3-VL-4B, GRPO 3000 steps"
    metric: "in-domain accuracy vs GRPO"
    value: "Geo3K 65.39 vs 60.57; MMK12 71.15 vs 68.05"
    notes: "EPS prompt scaffolding (2609.15051, EMNLP 2026 main). Narrow multimodal prompt-curriculum task only. Does not replace CISPO / SAPO / OraRL / DataFlex / GRPO / CANOPY / DIEM."
methods:
  - method:eps-prompt-scaffolding
  - method:orarl
  - method:dataflex-rl
  - method:cispo
  - method:sapo
  - method:grpo
  - method:diem
last_reviewed: "2026-09-15"
tags:
  - post-training
  - multimodal-rl
  - prompt-curriculum
  - eps
  - grpo
---

# MLLM Online RL Prompt Curriculum

## Problem Definition
Online RL for MLLMs assigns equal rollout budget to every training prompt. Some prompts are already saturated; others are currently too hard to yield a usable group-relative signal. This task is the online loop that scores prompt utility from on-policy rewards, routes low-utility prompts to a teacher for task-preserving rewrites, and refreshes a dynamic prompt pool.

## Evaluation Protocol
- **Primary Benchmarks**: Geometry3K and MMK12 in-domain accuracy; OOD MathVerse, MathVision, MMMU-Val, MMMU-Pro.
- **Evaluation Pitfalls**: Do not rank this against dense-text Pass@1 (CISPO), video annotation-as-rollout (OraRL), or static data-policy CIs (DataFlex-RL). Host loss stays GRPO-family; this is not a replacement optimizer.

## SOTA Recommendation (as of 2026-09-15)
- **Primary Method (this task only)**: **EPS prompt scaffolding** (`method:eps-prompt-scaffolding`, `paper:eps-prompt-scaffolding` `arXiv:2609.15051`).
- **Not This Task**: `method:orarl` remains video annotation-as-rollout; `method:cispo` remains dense Pass@1; `method:sapo` remains the MoE/VL loss; `method:dataflex-rl` remains the static-policy null; `method:diem` remains example-reweight; `method:canopy` remains outcome-only agents; GRPO stays the host, not the first hop.
