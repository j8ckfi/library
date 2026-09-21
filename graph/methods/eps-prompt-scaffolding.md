---
id: method:eps-prompt-scaffolding
type: method
title: "EPS Prompt Scaffolding"
category: "rl-alignment"
status: sota
sota_for:
  - task:mllm-rl-prompt-curriculum
supersedes: []
do_not_use_for:
  - when: "video annotation-as-rollout / fine-grained video perception RL"
    reason: "OraRL treats dataset annotations as oracle rollouts for video MLLMs; EPS rewrites image/VL training prompts"
    use_instead: "method:orarl"
  - when: "single-turn dense text math/code Pass@1 RLVR"
    reason: "EPS is a multimodal prompt-curriculum plug-in on GRPO; CISPO remains Pass@1"
    use_instead: "method:cispo"
  - when: "MoE/VL RLVR loss rather than prompt curriculum"
    reason: "SAPO remains the MoE/VL algorithm; EPS does not change the host loss"
    use_instead: "method:sapo"
  - when: "static RLVR data-policy evaluation (uniform vs selection, not online scaffolding)"
    reason: "DataFlex-RL is the static-policy null under text GRPO; EPS is online adaptive scaffolding"
    use_instead: "method:dataflex-rl"
  - when: "RFT example-reweight without rewriting the prompt"
    reason: "DIEM reweights minibatch examples; EPS rewrites low-EPS prompts"
    use_instead: "method:diem"
  - when: "outcome-only long-horizon agent RL"
    reason: "CANOPY / DRACO own sparse-outcome coverage; EPS is single-turn multimodal prompt routing"
    use_instead: "method:canopy"
  - when: "region-level RL for fine-grained MLLM perception (RoI proposal, frozen reader)"
    reason: "EPS rewrites prompts; Vision-RL2 trains a region head on a frozen MLLM"
    use_instead: "method:vision-rl2"
assumptions:
  - "Host is GRPO (paper: 3000 steps, 8 rollouts/prompt, batch 16, 8-GPU FSDP, lr 1e-6, clip 0.2, KL 0.01, max response 3072). Default routing threshold τ=0."
  - "Student is a VLM (paper: Qwen3-VL-2B/4B) on Geometry3K and MMK12. Verifiable reward via MathRuler. Teacher is Qwen-VL-Max."
  - "Scaffolding is answer-aware in the paper: the teacher sees the reference answer and is instructed not to reveal it. Fully answer-free scaffolding is listed as future work."
  - "No official public training repo as of 2026-09-15. Project page only; Appendix A has the loop."
last_reviewed: "2026-09-21"
papers:
  - paper:eps-prompt-scaffolding
recipes:
  - recipe:eps-prompt-scaffolding
claims:
  - benchmark: "Geometry3K in-domain, Qwen3-VL-4B, GRPO 3000 steps"
    metric: "accuracy"
    value: 65.39
    baseline: "GRPO 60.57; SFT 55.07"
    date: "2026-09-15"
    verified: true
    evidence_level: "peer-reviewed"
    source_url: "https://arxiv.org/abs/2609.15051"
    notes: "OOD avg (MathVerse / MathVision / MMMU-Val / MMMU-Pro) 49.75 vs GRPO 48.54. EMNLP 2026 main."
  - benchmark: "MMK12 in-domain, Qwen3-VL-4B, GRPO 3000 steps"
    metric: "accuracy"
    value: 71.15
    baseline: "GRPO 68.05; SFT 56.48"
    date: "2026-09-15"
    verified: true
    evidence_level: "peer-reviewed"
    source_url: "https://arxiv.org/abs/2609.15051"
    notes: "MathVision 44.41 vs GRPO 41.78. OOD avg 52.67 vs 50.87."
  - benchmark: "MMK12 path, Qwen3-VL-2B relative lifts vs GRPO"
    metric: "relative accuracy"
    value: "+9.7% in-domain; +11.5% MathVision; +11.1% MMMU-Pro"
    baseline: "GRPO MMK12 51.40 / MathVision 28.62 / MMMU-Pro 36.59"
    date: "2026-09-15"
    verified: true
    evidence_level: "peer-reviewed"
    source_url: "https://arxiv.org/abs/2609.15051"
    notes: "Absolute: in-domain 56.40, MathVision 31.91, MMMU-Pro 40.64. Paper headline relatives."
tags:
  - post-training
  - multimodal-rl
  - prompt-curriculum
  - eps
  - grpo
  - sota
---

# EPS Prompt Scaffolding

## Method Overview
GRPO spends the same rollout budget on every prompt. EPS Prompt Scaffolding scores each prompt from the rewards GRPO already collected, keeps high-EPS prompts for the policy update, and sends low-EPS prompts to a teacher for a task-preserving rewrite rather than answer imitation.

Exploration Potential Score from \(N\) on-policy rewards \(r_i\):

\[\hat{\mathcal{E}}(x)=\sum_{i=1}^{N} r_i\cdot\mathrm{softmax}(r_i/\beta)_i-\bar{r}\]

\(\beta\) is the KL temperature. Idealized EPS is non-negative; finite-sample scores can go negative, so default \(\tau=0\) routes those prompts to rewrite. Loop: score, filter, rewrite (async teacher), refresh the pool and periodically reactivate reserved originals.

## When to Use
- Post-training a VLM/MLLM with online GRPO when prompt utility is uneven (Geometry3K / MMK12-class visual math).
- When a teacher can rewrite the training condition without the student imitating teacher answers.

## When NOT to Use
- Video annotation-as-rollout → `method:orarl`. Dense text Pass@1 → `method:cispo`. MoE/VL loss → `method:sapo`. Static data-policy eval → `method:dataflex-rl`. Example reweight → `method:diem`. Outcome-only agents → `method:canopy`. Region-level perception RL → `method:vision-rl2`.

## Relation to Existing SOTA
- First hop for `task:mllm-rl-prompt-curriculum` only. Does **not** supersede `method:orarl`, `method:dataflex-rl`, `method:cispo`, `method:sapo`, `method:grpo`, `method:canopy`, or `method:diem`. DataFlex is the static-policy null; EPS is online adaptive scaffolding. Region-level perception RL is `method:vision-rl2`.

## Gotchas & Failure Modes
- Teacher scaffolding in the paper is answer-aware. Do not treat results as answer-free distillation.
- EPS is a ranking/routing signal, not a calibrated forecast of future learnability. Small \(N\) or small \(\beta\) raises variance.
- Code is Appendix A only as of 2026-09-15; no official training GitHub.
