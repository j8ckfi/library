---
id: paper:dco
type: paper
title: "Drift-Constrained Optimization: Only Direction Matters in Fine-Tuning Instruct Models"
authors:
  - "Fei Yuan"
  - "Changjiang Gao"
  - "Yilei Tu"
  - "Yifeng Liu"
  - "Shujian Huang"
  - "Yu Qiao"
year: 2026
month: 9
arxiv_id: "2609.13680"
url: "https://arxiv.org/abs/2609.13680"
methods:
  - method:dco
cites:
  - paper:delta-learning
  - paper:olmo-3
tags:
  - post-training
  - instruct
  - sft
  - drift
  - dco
---

# Drift-Constrained Optimization: Only Direction Matters in Fine-Tuning Instruct Models

## Abstract Summary
Instruct fine-tuning often raises a target task while drifting away from the reference model and losing reasoning. DCO treats that drift as a budget $\delta$ on anchored KL, not a post-hoc regularizer: $\min T(\theta)$ s.t. $D_{\mathrm{ref}}(\theta)\le\delta$. Locally the Fisher metric at $\theta_0$ splits an update into radius (how far) and direction (how the budget is spent). Full FT, LoRA, and parameter-subset tuning then differ by feasible directions, not step size. A coarse layer-selective probe (LST: freeze most layers; split $b_n t_m$ trains bottom $n$ then top $m$) reverses QA-only FT failure on Qwen3-8B/14B: the model still generates CoT at inference while training on answer-only pairs. Split LST matches or beats Seed-X-PPO-7B / Tower-Plus-9B on FLORES-101 xCOMET over $>$100 languages and is a stronger RL initialization than the base instruct model. Code: LLaMA-Factory freeze scripts; weights on Hugging Face.

## Key Contributions
1. **Drift-first SFT**: anchored KL as the organizing constraint; shared Fisher coordinates $(\rho, v)$ around the reference.
2. **Fine-tuning as direction selection**: at matched radius, maximize directional efficiency $\eta(u)=(-g^\top u)/\sqrt{u^\top F u}$.
3. **Layer-selective probe**: two-segment freeze $M=\{1,\ldots,l_1\}\cup\{l_2,\ldots,L\}$ finds families of good directions without solving the full natural-gradient problem.
4. **QA-only $\to$ keep CoT**: reverses the MegaScience/SmolInstruct collapse of full FT while preserving AIME/LCB/BBEH general avg.

## Empirical Highlights
- FLORES-101 xCOMET, QA-only (Table 1): Qwen3-8B LST b4t16 $52.66$ / $55.60$ vs reference $47.07$ / $51.40$ (Seed-X-PPO-7B $47.76$ / $51.31$, Tower-Plus-9B $46.95$ / $52.44$). General avg $38.85$ vs $42.22$. b4t8 keeps general avg $42.32$ ($\Delta$ $+0.10$) with $50.35$ / $53.67$.
- Qwen3-14B LST b4t16: $56.51$ / $58.31$ vs reference $51.85$ / $55.21$; general avg $43.76$ vs $48.95$.
- SmolInstruct (Table 2): Qwen3-8B FFT $59.65$ but general avg $33.60$ (from $42.22$); LST b4t16 $29.61$ with general $44.03$; b16 $35.15$ with general $42.20$.
- Translation RL init (Figure 6b): Qwen3-8B+LST already beats Qwen3-8B+RL (WALAR) on every pivot; LST then RL is the strongest of the four.
- Repo demo (BenchMAX FLORES spBLEU, b4t8, 1 epoch): en→zh $35.89$ vs $34.78$; zh→en $32.76$ vs $31.26$.

## Open Source Repository & Resources
- Code: `https://github.com/CONE-MT/DCO` (confirmed 2026-09-16). LLaMA-Factory `finetuning_type: freeze` two-stage LST; `specialist_distillation/*/lst_scripts/submit_lst.sh`.
- Weights: `https://huggingface.co/collections/LLaMAX/dco` (DCO-Translation / DCO-Smol Qwen3-8B/14B b16, b4t8, b4t12, b4t16; GlotMAX-101 LST; `LLaMAX/bilingual_zh_en`).
