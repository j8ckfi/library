---
id: paper:oasis
type: paper
title: "Overcoming Scaling Limits in On-Policy Self-Distillation for LLM Reasoning"
authors:
  - "Md Ismail Hossain"
  - "Humaira Kousar"
  - "Isidora Chara Tourni"
year: 2026
month: 9
arxiv_id: "2609.37915"
url: "https://arxiv.org/abs/2609.37915"
methods:
  - method:oasis
cites:
  - paper:vista
  - paper:u-opsd
tags:
  - post-training
  - distillation
  - self-distillation
  - privileged-teacher
  - oasis
---

# Overcoming Scaling Limits in On-Policy Self-Distillation for LLM Reasoning

## Abstract Summary
Vanilla OPSD supervises unverified student rollouts while the teacher sees a gold solution. Scaffold correctness dominates context correctness: unverified scaffolds create an imitation gap that shrinks with scale, yet OPSD still spends most updates on trajectories that never reach a correct answer. OPSD's gain over the base model falls from 3.05 points at 1.7B to 0.14 at 8B. OASIS keeps the OPSD objective, supervises the shortest verified on-policy scaffold, and conditions the teacher on another same-problem rollout (typically an unverified attempt), so only final-answer labels are required. Across Qwen3-1.7B/4B/8B on AIME 2024/2025 and HMMT 2025, OASIS stays ~+3.2–3.8 over base and beats OPSD by +3.05 at 8B. North South University / KAIST / Andria Labs. No public GitHub as of 2026-10-01.

## Key Contributions
1. **Scale collapse of unverified OPSD**: gold-context recovery advantage concentrates on failed prefixes and shrinks with model size.
2. **Scaffold vs context factorial**: verified scaffolds remain useful even when the teacher is not given a written gold solution.
3. **Answer-label OASIS**: shortest verified on-policy scaffold + distinct same-problem rollout as teacher context.

## Empirical Highlights
- OPSD vs base: +3.05 / +1.98 / +0.14 at 1.7B / 4B / 8B. OASIS vs base: +3.2–3.8 across the same sizes.
- OASIS vs OPSD: +0.59 / +1.86 / +3.05. Written traces replaced by final-answer verification at extra rollout cost.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.37915`
- Code: none found as of 2026-10-01 (`code_status: none`).
