---
id: paper:dce-srcl
type: paper
title: "Recursive Self-Improvement via On-Policy Distillation for Reasoning"
authors:
  - "Shangjian Yin"
  - "Zehao Zhao"
  - "Kavosh Asadi"
  - "Rui Liu"
  - "Yuchen Lu"
  - "Shike Mei"
  - "Hang Cui"
  - "Luke Simon"
  - "Zhouxing Shi"
  - "Hamed Firooz"
year: 2026
month: 9
arxiv_id: "2609.30652"
url: "https://arxiv.org/abs/2609.30652"
methods:
  - method:dce-srcl
cites:
  - paper:vista
  - paper:u-opsd
  - paper:self-opd
tags:
  - post-training
  - distillation
  - self-distillation
  - privileged-teacher
  - opsd
  - dce-srcl
---

# Recursive Self-Improvement via On-Policy Distillation for Reasoning

## Abstract Summary
Vanilla on-policy self-distillation freezes a gold-conditioned copy of the student as the privileged teacher. The paper argues that freeze keeps the teacher from absorbing revision behavior the student learns, so later prefixes are scored by a supervisor that prefers EOS over reflection on incorrect traces. Dynamic Co-Evolution (DCE) refreshes both roles from the updated checkpoint each round. Self-Refined Concise Learning (SRCL) adds shorter, verified rewrites of the same on-policy responses to curb verbosity. On Qwen3-8B, DCE+SRCL reaches 65.97% Average@12 on four competition-math contests, +35.62 pp vs their OPSD baseline, with −7.80% mean length vs DCE alone. Meta AI / UC Riverside. Reproducibility promised; no public repo found as of 2026-09-28.

This paper's OPSD baseline (~30% Average@12 on Qwen3-8B non-thinking) is **not** comparable to the library VISTA bake-off (OPSD 64.8 → VISTA 66.9 on a matched instruct protocol). File as an active plug-in; bake before any future retarget of `method:vista`.

## Key Contributions
1. **DCE**: after each update, \(\theta_{k+1}\) initializes both the problem-only student and a detached gold-conditioned privileged teacher, so revision acquired in round \(k\) supervises round \(k+1\).
2. **SRCL**: rewrite the on-policy response without the gold solution; keep the rewrite only if it is shorter, naturally terminated, structurally valid, and answer-correct; train token-level CE on accepted rewrites.
3. **Multi-scale math**: DCE is the accuracy driver; SRCL is the length (and sometimes accuracy) regularizer. OPSD-TTS 16K token forcing does not close the gap.

## Empirical Highlights
- Qwen3-8B non-thinking, AIME24/25/26 + HMMT25 Avg@12: DCE+SRCL 65.97 / 17,561 tok vs DCE 65.76 / 19,046 vs OPSD 30.35 / 6,009 vs GRPO 20.28.
- Qwen3-4B: 61.88 vs OPSD 22.85. Qwen3-1.7B: 26.88 vs OPSD 10.35 (SRCL raises length at 1.7B).
- Gemma-4-12B-IT transfer: DCE+SRCL 63.61 vs OPSD 51.04 vs Base 56.18.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.30652`
- Code: none found as of 2026-09-28 (`recipe:dce-srcl` `code_status: none`).
