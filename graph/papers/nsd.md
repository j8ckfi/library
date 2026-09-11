---
id: paper:nsd
type: paper
title: "Negative Self-Distillation: Learning to Reason by Avoiding Flaws"
authors:
  - "Rongcan Pei"
  - "Zhepei Wei"
  - "Shuyao Xu"
  - "Xinyu Zhu"
  - "Wei-Lin Chen"
  - "Yu Meng"
year: 2026
month: 9
arxiv_id: "2609.11699"
url: "https://arxiv.org/abs/2609.11699"
methods:
  - method:nsd
cites:
  - paper:vista
  - paper:opsd-collapse-review
  - paper:grpo
  - paper:opd
tags:
  - post-training
  - distillation
  - opsd
  - nsd
  - self-distillation
---

# Negative Self-Distillation: Learning to Reason by Avoiding Flaws

## Abstract Summary
On-policy self-distillation (OPSD) can degrade complex reasoning: imitating a privileged, artificially confident trace suppresses uncertainty and self-correction. Negative Self-Distillation (NSD) instead diverges from a self-generated negative condition (a "careless reasoner") rather than imitating gold or privileged solutions. Naive unlearning would also punish ordinary language tokens; a dynamic gate isolates reasoning-critical tokens. Default training generates the negative condition online, without ground-truth answers.

## Key Contributions
1. **Diverge, do not imitate**: push the student away from a question-specific negative teacher instead of matching privileged gold traces.
2. **Gated unlikelihood**: penalize only tokens where the negative teacher over-assigns relative to a reference, plus a KL anchor.
3. **Online negative conditions**: default recipe generates the negative prompt from the model itself.

## Empirical Highlights
- Average gains +2.3% / +7.5% / +6.0% on Qwen3-1.7B / 4B / 8B across AIME 24/25/26, HMMT, AMC, OlympiadBench, MATH vs OPSD / Intuitor / TTRL (Table 1).
- Qwen3-4B reflection-token frequency 7.5 vs OPSD 2.2 vs Intuitor 0.8 (Table 2).

## Open Source Repository & Resources
- Code: `https://github.com/Prongcan/NSD`
- Checkpoints: `https://huggingface.co/collections/PassionPrc/nsd-negative-self-distillation`
