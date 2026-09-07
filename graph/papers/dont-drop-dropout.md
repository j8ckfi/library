---
id: paper:dont-drop-dropout
type: paper
title: "Don't Drop Dropout: Optimizing Layer Sparsity for Efficient LLM Training and Inference"
authors:
  - "Mostafa Elhoushi"
  - "Alex Pretko"
  - "Nolan Dey"
  - "Bin Claire Zhang"
  - "Gavia Gray"
  - "Gurpreet Gosal"
  - "Abdulrahman Mahmoud"
  - "Shane Bergsma"
  - "Joel Hestness"
year: 2026
month: 9
arxiv_id: "2609.05275"
url: "https://arxiv.org/abs/2609.05275"
methods:
  - method:layer-dropout
cites:
  - paper:muon2
tags:
  - pretraining
  - regularization
  - stochastic-depth
  - layer-dropout
---

# Don't Drop Dropout: Optimizing Layer Sparsity for Efficient LLM Training and Inference

## Abstract Summary
Layer dropout (stochastic depth) disappeared from LLM pretrain recipes as models and datasets scaled, after scattered reports that dropout hurt accuracy. This ICML 2026 extended version shows it belongs in SOTA LLM pretraining when the layer distribution, time schedule, and optimizer hyperparameters are set correctly — especially the residual scale $r_{\mathrm{train}}=1/\rho$ ($\rho=1-p$ is layer density), not $r_{\mathrm{train}}=1$. At matched training FLOPs, layer dropout reaches lower loss. At matched step count, models hit similar or better validation loss while saving up to 25% training FLOPs. The same sparsity enables early-exit, intermediate-layer skipping, and self-speculative decoding (up to 1.5× inference) with negligible accuracy loss. More than 2400 runs, 271M–8.2B, ≤160B tokens, all on Cerebras CS-3. No paper-specific repo; practical implementations are torchtune `layer_dropout.py` and fairseq LayerDrop.

## Key Contributions
1. **Residual scale**: $r_{\mathrm{train}}=1/\rho$ is required for stable hyperparameter transfer. Original stochastic depth used $r_{\mathrm{train}}=1$; fairseq/torchtune historically set both train and eval scales to 1.
2. **Increasing layer distribution (ILD)**: $p^{\ell}=\ell/(L-1)\cdot p_{\max}$, combined with a decreasing time schedule (DTS) $p^{t}=p^{\ell}(1-t/(T-1))$.
3. **Same-FLOPs lower loss / same-steps up to 25% FLOP save**, after retuning LR, batch, and weight decay per dropout rate.
4. **Inference**: early exit, skip-alternate-layers, and self-speculative decoding up to 1.5× with small accuracy loss, because training already saw reduced depth.

## Empirical Highlights
- 1.8B, 20 tokens/parameter: val loss 1.836 at 15% FLOP savings ($p_{\max}=0.6$, ILD+DTS) vs 1.849 dense; skip-alternate-layers 2.282 vs 4.260.
- 3.9B: 20% FLOP savings at $p_{\max}=0.8$, val 1.745 vs dense 1.732.
- 8.2B: 25% FLOP savings at $p_{\max}=0.99$, val 1.663 (dropout-only column in Table 5).
- Self-speculative decoding: up to 1.5× (abstract); 270M ILD $p_{\max}=0.4$ is 1.35× in Table 4.

## Open Source Repository & Resources
- No paper-specific GitHub. Implementations: `https://github.com/meta-pytorch/torchtune/blob/main/torchtune/modules/layer_dropout.py` and fairseq `LayerDrop`. Set $r_{\mathrm{train}}=1/\rho$, $r_{\mathrm{eval}}=1$ even if those libraries historically used 1/1.
