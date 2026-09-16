---
id: method:dco
type: method
title: "Drift-Constrained Optimization (DCO)"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the open instruct / chat SFT stack"
    reason: "DCO is a drift-budget direction probe on an existing instruct model; OLMo-3 Dolci remains the open instruct default"
    use_instead: "method:olmo-3"
  - when: "24GB quality LoRA is the library task"
    reason: "Quality default remains vanilla LoRA + rsLoRA + LR sweep; DCO freezes layers under a KL budget"
    use_instead: "method:lr-matters-lora"
  - when: "RLVR-stable rank-normalized LoRA A"
    reason: "NoRA normalizes adapter A; DCO is instruct layer-selective FT"
    use_instead: "method:nora"
  - when: "optimizer-shape / effective-rank LoRA"
    reason: "Iso-LoRA spectrally couples BA; DCO does not retarget LoRA geometry"
    use_instead: "method:iso-lora"
  - when: "activation-space directional deltas without a Fisher drift budget"
    reason: "Delta Learning shifts representations; DCO selects parameter-space directions under anchored KL"
    use_instead: "method:delta-learning"
  - when: "multi-teacher on-policy distillation"
    reason: "Open-MOPD remains multi-teacher distill; DCO is single-model instruct FT"
    use_instead: "method:open-mopd"
assumptions:
  - "Start from a strong instruct checkpoint. Paper: Qwen3-8B/14B, QA-only SmolInstruct 300k or Lego-MT ~2.8M, 8x H200. Inference still runs the model's reasoning path."
  - "Operational probe is two-stage LST (bottom layers, then top) via LLaMA-Factory freeze. Freeze lm_head / embeddings; jointly updating them raised KL without helping accuracy."
  - "Does not claim instruct SOTA. Does not replace OLMo-3 / Nemotron-Cascade 2 / LoRA quality / Delta Learning / Open-MOPD."
last_reviewed: "2026-09-16"
papers:
  - paper:dco
recipes:
  - recipe:dco
claims:
  - benchmark: "FLORES-101 xCOMET, Qwen3-8B QA-only translation, lg→x / x→lg"
    metric: "xCOMET"
    value: "52.66 / 55.60 (LST b4t16)"
    baseline: "Qwen3-8B 47.07 / 51.40; Seed-X-PPO-7B 47.76 / 51.31; Tower-Plus-9B 46.95 / 52.44; FFT 42.05 / 47.02; LoRA rank-64 40.78 / 46.50"
    date: "2026-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.13680"
    notes: "Table 1. b4t8 keeps general avg 42.32 vs ref 42.22 with 50.35 / 53.67. b4t16 general avg 38.85. >100 languages, four pivots (en/zh/ne/ceb)."
  - benchmark: "FLORES-101 xCOMET, Qwen3-14B QA-only, lg→x / x→lg"
    metric: "xCOMET"
    value: "56.51 / 58.31 (LST b4t16)"
    baseline: "Qwen3-14B 51.85 / 55.21; FFT 43.82 / 48.11"
    date: "2026-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.13680"
    notes: "Table 1. b4t8 53.85 / 56.60 with general avg 46.98 vs ref 48.95."
  - benchmark: "SmolInstruct chemistry, Qwen3-8B QA-only"
    metric: "SmolInstruct overall / general avg (AIME+LCB+BBEH)"
    value: "LST b4t16 29.61 / 44.03; LST b16 35.15 / 42.20"
    baseline: "Qwen3-8B 19.34 / 42.22; FFT 59.65 / 33.60; LoRA 28.57 / 42.65"
    date: "2026-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.13680"
    notes: "Table 2. FFT wins the target by dumping general capability. Split LST is the drift-efficient family under a tight budget."
  - benchmark: "Qwen3-8B translation RL init (WALAR pipeline)"
    metric: "xCOMET vs Qwen3-8B + RL"
    value: "LST already beats base+RL on every pivot; LST+RL is strongest"
    baseline: "Qwen3-8B and Qwen3-8B + RL (Liu et al. 2026 WALAR)"
    date: "2026-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.13680"
    notes: "Figure 6b. Stronger RL warm-start, not a CISPO/SAPO replacement."
tags:
  - post-training
  - instruct
  - sft
  - drift
  - dco
  - active
---

# Drift-Constrained Optimization (DCO)

## Method Overview
DCO fine-tunes an instruct model under an explicit behavioral-drift budget. Anchored KL $D_{\mathrm{ref}}(\theta)=\mathbb{E}_{x\sim D_{\mathrm{general}}}\mathrm{KL}(\pi_{\theta_0}(\cdot|x)\|\pi_\theta(\cdot|x))$ is the constraint. Around $\theta_0$ the Fisher metric makes radius $\rho=\sqrt{\Delta\theta^\top F\Delta\theta}$ the spent budget and $v=\Delta\theta/\rho$ the remaining degree of freedom. Locally the best direction is $-F^{-1}g$. The paper does not invert $F$; it probes feasible families by freezing layers (LST). Split $b_n t_m$ trains the bottom $n$ layers, then the top $m$, middle frozen. At matched KL, that family beats full FT and often LoRA/ASFT on the task–general plane, including QA-only training that must still emit CoT at inference.

## When to Use
- Domain FT of a strong instruct model (science, many-language translation) when full SFT wrecks reasoning.
- You can freeze layers in LLaMA-Factory (`finetuning_type: freeze`) and sweep a few split configs (b4t8 / b4t12 / b4t16) under a KL budget.
- You want a better SFT init before a later RL pass on the same target.

## When NOT to Use
- Open instruct stack $\to$ `method:olmo-3`. 24GB LoRA quality $\to$ `method:lr-matters-lora`. NoRA / Iso-LoRA stay LoRA-geometry tools. Activation-space deltas $\to$ `method:delta-learning`. Multi-teacher distill $\to$ `method:open-mopd`.

## Relation to Existing SOTA
- Active plug-in on `task:instruct-sft-alignment`. Mention on `task:parameter-efficient-fine-tuning` (layer freeze, not LoRA). Does **not** enter `current_sota`. Does **not** supersede `method:olmo-3`, `method:lr-matters-lora`, `method:nora`, `method:iso-lora`, `method:delta-learning`, or `method:open-mopd`.

## Gotchas & Failure Modes
- Continuous bottom-only b16 can look cheap in KL and still lose the target (translation Table 1). Split vs contiguous preference flips with the drift budget: split for low drift, contiguous when more drift is allowed.
- Updating `lm_head` / embeddings with the selected layers raised KL and slightly hurt accuracy.
- QA-only is the stress test. If you already have CoT traces, this is not an argument against them (`method:partial-reasoning-traces` is the trace-shaping plug-in).
- Code lives under LLaMA-Factory freeze YAMLs, not a standalone trainer. HF collection: `LLaMAX/dco`.
