---
id: method:vision-rl2
type: method
title: "Vision-RL2"
category: "multimodal-rl"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "online adaptive prompt selection / teacher scaffolding for image/VL GRPO"
    reason: "EPS prompt scaffolding remains that first hop; Vision-RL2 trains a region proposal network"
    use_instead: "method:eps-prompt-scaffolding"
  - when: "video annotation-as-rollout / fine-grained video perception RL"
    reason: "OraRL treats dataset annotations as oracle rollouts for video MLLMs"
    use_instead: "method:orarl"
  - when: "single-turn dense text math/code Pass@1 RLVR"
    reason: "CISPO remains Pass@1"
    use_instead: "method:cispo"
  - when: "MoE/VL RLVR loss rather than region proposal"
    reason: "SAPO remains the MoE/VL algorithm"
    use_instead: "method:sapo"
assumptions:
  - "Starts from a trained SD-RPN predictor attached to a frozen MLLM. RL pool: 7K VisualCoT QA (5K InfographicVQA, 1K TextVQA, 1K DocVQA). Train source-image limit 576 tokens. One epoch, batch 32, lr 1.5e-5."
  - "Reader is the frozen backbone scoring leave-one-out gold-answer log-odds. No region boxes, no response sampling, no CoT trajectories."
  - "Code, weights, and data released: YuHengsss/VisionRL2; HF collection YuhengSSS/visionrl2."
last_reviewed: "2026-09-21"
papers:
  - paper:vision-rl2
recipes:
  - recipe:vision-rl2
claims:
  - benchmark: "Six-bench average at 16,384 source tokens, Qwen3.5-9B"
    metric: "average accuracy"
    value: 80.1
    baseline: "Qwen3.5-9B 74.6 / Vision-OPD-9B 78.7"
    date: "2026-09-21"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.19745"
    notes: "Table 1. V* 95.3, ZoomBench 68.4. Updates only the RoI predictor. Not an EPS prompt-curriculum result."
  - benchmark: "Six-bench average, Qwen3.5-4B training-aligned 576-token protocol"
    metric: "average accuracy"
    value: 71.1
    baseline: "base 56.2 / SD-RPN 66.6"
    date: "2026-09-21"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.19745"
    notes: "Table 2. Matches SD-RPN at 4096 tokens with 4.2× fewer visual tokens. Region-level RL +3.0; sparse encoding +1.5."
tags:
  - post-training
  - multimodal-rl
  - finegrained-perception
  - vision-rl2
  - active
---

# Vision-RL2

## Method Overview
Localization tolerates several times more token compression than recognition. Vision-RL2 localizes from a coarse view and spends resolution on selected evidence.

A lightweight SD-RPN head, attached after frozen MLLM blocks, predicts a dense RoI map. Connected components of that map are the actions. A frozen reader scores each masked image by the log-odds of the gold answer. Subtractive RL prunes regions whose leave-one-out contribution sits inside a control-region noise margin; additive RL recovers missed evidence from frozen response-to-image attention. Sparse encoding then zooms the crop by foreground occupancy and drops background tokens. Only the predictor is trained.

## When to Use
- Fine-grained image perception where visual tokens are the budget, and you can freeze the MLLM while training a small RoI head.

## When NOT to Use
- Multimodal prompt curriculum → `method:eps-prompt-scaffolding`. Video annotation-as-rollout → `method:orarl`. Dense text Pass@1 → `method:cispo`. MoE/VL loss → `method:sapo`.

## Relation to Existing SOTA
- Active first hop on `task:mllm-finegrained-perception-rl` only (method status active; listed in that task's `current_sota`). Mention on `task:mllm-rl-prompt-curriculum`. Does **not** replace `method:eps-prompt-scaffolding` or `method:orarl`.

## Gotchas & Failure Modes
- Trails full-model FT on MME-RealWorld at 4B because the reader is frozen. That gap is the design, not a missed hyperparameter.
- Cell-level keep-sets underperform coherent regions (−1.2). Do not treat per-token Bernoulli inclusion as the action space.
- Binary generation-accuracy rewards lose relative credit (−2.3). Keep the clipped log-odds reader.
- Gemma-4 has no native-resolution mode; use its largest visual-token tier (1,120).
