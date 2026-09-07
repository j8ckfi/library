---
id: method:layer-dropout
type: method
title: "Layer Dropout (Don't Drop Dropout)"
category: "architecture"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the ~7B dense pretrain optimizer"
    reason: "Layer dropout is residual-path sparsity during pretrain; Muon2 + KL-SOAP remains the optimizer default"
    use_instead: "method:muon2"
  - when: "PEFT-only fine-tune on a frozen backbone"
    reason: "The paper's gains are from pretraining with structured layer sparsity, not adapter stacks"
    use_instead: "method:lr-matters-lora"
  - when: "budget ~1.5-2B consumer-GPU pretrain recipe"
    reason: "Puro-2B remains that first-hop; layer dropout is an optional regularizer on top, not a replacement"
    use_instead: "method:puro-2b"
assumptions:
  - "Pretraining a dense transformer from scratch (paper: 271M–8.2B, ≤160B tokens, Cerebras CS-3, >2400 runs). Retune LR / batch / weight decay per dropout rate."
  - "Critical residual scale r_train=1/ρ with ρ=1-p, r_eval=1. ILD across depth plus DTS over time is the large-run recipe."
  - "Not a substitute for Muon2. Compatible with standard AdamW ablations in the paper; optimizer choice is orthogonal."
last_reviewed: "2026-09-07"
papers:
  - paper:dont-drop-dropout
recipes:
  - recipe:layer-dropout
claims:
  - benchmark: "1.8B dense LLM, 20 tokens/parameter, Cerebras CS-3"
    metric: "validation loss (lower better) at 15% FLOP savings"
    value: 1.836
    baseline: "Dense (no dropout) 1.849"
    date: "2026-09-07"
    verified: true
    evidence_level: "peer-reviewed"
    source_url: "https://arxiv.org/abs/2609.05275"
    notes: "Table 5. p_max=0.6, increasing layer dist., decreasing time schedule. ICML 2026 extended version. Skip-alternate-layers 2.282 vs dense 4.260."
  - benchmark: "8.2B dense LLM, 20 tokens/parameter"
    metric: "training FLOP savings at matched steps"
    value: "25%"
    baseline: "Dense pretrain at the same step count"
    date: "2026-09-07"
    verified: true
    evidence_level: "peer-reviewed"
    source_url: "https://arxiv.org/abs/2609.05275"
    notes: "Table 5. p_max=0.99, ILD+DTS, val loss 1.663. Abstract: same-FLOPs lower loss; same-steps up to 25% FLOP save."
  - benchmark: "Self-speculative decoding after layer-dropout pretrain"
    metric: "inference speedup"
    value: "up to 1.5× with negligible accuracy loss"
    baseline: "Dense-pretrained model without reduced-depth training"
    date: "2026-09-07"
    verified: true
    evidence_level: "peer-reviewed"
    source_url: "https://arxiv.org/abs/2609.05275"
    notes: "Abstract. Table 4: 270M ILD p_max=0.4 is 1.35×. Also early-exit and intermediate-layer skip."
tags:
  - pretraining
  - architecture
  - regularization
  - stochastic-depth
  - layer-dropout
  - active
---

# Layer Dropout (Don't Drop Dropout)

## Method Overview
Layer dropout (stochastic depth) skips transformer residual branches during pretrain. For layer density $\rho=1-p$,

\[
\mathbf{H}^{\ell+1,t}=\mathbf{H}^{\ell,t}+r_{\mathrm{train}}\,\mathbf{M}^{\ell,t}f^{\ell}(\mathbf{H}^{\ell,t}),
\]

with $\mathbf{M}\sim\mathrm{Bernoulli}(\rho)$ per sequence (or per attn/FFN sublayer). **Set $r_{\mathrm{train}}=1/\rho$**, $r_{\mathrm{eval}}=1$. Using $r_{\mathrm{train}}=1$ (Huang 2016 stochastic depth, and the historical fairseq/torchtune default) breaks hyperparameter transfer.

Large-run recipe: increasing layer distribution $p^{\ell}=\frac{\ell}{L-1}p_{\max}$ plus decreasing time schedule $p^{\ell,t}=p^{\ell}(1-t/(T-1))$. Retune LR, batch size, and weight decay at each dropout rate. Same FLOPs: lower loss. Same steps: up to 25% fewer FLOPs at similar val loss. The trained model is already robust to early exit, layer skip, and self-speculative decoding (~1.5×).

## When to Use
- Dense LLM pretrain where you can retune optimizer hyperparameters and want FLOP savings or elastic-depth inference from one checkpoint.
- Stack with `method:muon2`; do not swap the optimizer for dropout.

## When NOT to Use
- Optimizer choice -> `method:muon2`.
- PEFT-only fine-tune -> `method:lr-matters-lora`.
- Tight ~2B consumer recipe -> `method:puro-2b` (dropout can sit on top; it is not that recipe).

## Relation to Existing SOTA
- Active regularizer on `task:llm-pretraining-optimization` and `task:pretrain-dense-7b`. Does **not** supersede `method:muon2`. Optional note on `task:budget-consumer-pretrain`.
- Orthogonal to `method:mhc` / `method:attnres` (residual topology) and to `method:qwen38-next` (production hybrid architecture).

## Gotchas & Failure Modes
- $r_{\mathrm{train}}=1/\rho$ is load-bearing. Do not copy fairseq/torchtune scale=1 defaults blindly.
- Uniform dropout across depth is worse than ILD at the same mean FLOP save.
- Do not compare to an untuned dense baseline: the paper retunes LR/batch/WD per rate.
- Experiments are Cerebras CS-3, 271M–8.2B, ≤160B tokens. Transfer to trillion-token GPU pretrain is plausible but not the measured regime.
