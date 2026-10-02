---
id: paper:where-opd
type: paper
title: "Where-OPD: Spatially Guided On-Policy Self-Distillation of MLLMs with Synthetic Scenes"
authors:
  - "Sophia Sirko-Galouchenko"
  - "Monika Wysoczanska"
  - "Andrei Bursuc"
  - "Nicolas Thome"
  - "Spyros Gidaris"
year: 2026
month: 10
arxiv_id: "2610.02117"
url: "https://arxiv.org/abs/2610.02117"
methods:
  - method:where-opd
cites:
  - paper:opd
  - paper:vista
  - paper:vision-rl2
tags:
  - post-training
  - distillation
  - self-distillation
  - multimodal
  - where-opd
---

# Where-OPD: Spatially Guided On-Policy Self-Distillation of MLLMs with Synthetic Scenes

## Abstract Summary
Privileged-teacher OPSD for MLLMs usually gives the teacher a different image (crop/zoom). Those gains do not transfer uniformly: Vision-OPD can win V*/ZoomBench and drop CountQA. Where-OPD instead gives the teacher a textual list of relevant objects and coordinates from a procedurally generated scene; student and teacher share the same image. Post-train is synthetic counting; transfer is real-world perception. Valeo.ai / Sorbonne. Code: `https://github.com/sirkosophia/Where-OPD`.

## Key Contributions
1. **Textual spatial privilege**: teacher \(\pi_{\bar\theta}(I,Q,h)\); student \(\pi_\theta(I,Q)\); inference drops \(h\).
2. **Simulator hints**: object ids and coordinates known by construction; no human boxes, no external grounder.
3. **Synthetic-to-real**: counting-scene post-train lifts ChartQA / EvoChart and a six-bench real-world average.

## Empirical Highlights
- Qwen3.5-4B real-world average (CVBench / V* / ZoomBench / BLINK / HR-Bench / MME-RealWorld) +3.23 vs base. 9B / Qwen3-VL-4B averages +1.07 / +1.29.
- Qwen3.5-4B ChartQA / EvoChart / CountQA / OCRBench +7.20 / +10.11 / +2.53 / +1.93. Vision-OPD can drop CountQA −10.73 while winning zoom benches.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.02117`
- Code: `https://github.com/sirkosophia/Where-OPD` (`code_status: released`).
