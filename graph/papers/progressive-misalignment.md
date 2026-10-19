---
id: paper:progressive-misalignment
type: paper
title: 'Progressive Misalignment Can Emerge from Benign Recursive Self-Distillation'
authors:
- 'Karim Abdel Sadek'
- 'Federico Di Gennaro'
- 'Fanny Yang'
year: 2026
month: 10
arxiv_id: '2610.22467'
url: https://arxiv.org/abs/2610.22467
methods:
- method:vista
- method:opd
- method:rrsi
cites:
- paper:vista
- paper:opd
- paper:rrsi
tags:
- opsd
- safety
- gotcha
---

# Progressive Misalignment Can Emerge from Benign Recursive Self-Distillation

## Abstract Summary
Recursive self-distillation, where each self-distilled model becomes the next teacher, can progressively misalign a previously safe model even when every generation is safe and the extra context is a benign instruction. Safety properties of privileged/self-distill loops are not implied by a single round of matching.

## Key Contributions
1. Recursive OPSD/self-distill safety failure under benign extra context.
2. Each round's teacher is the previous student.
3. Caution on VISTA / OPD / RRSI-style self-improve loops, not a new trainer.

## Empirical Highlights
- Do not assume recursive self-distill is safety-preserving because each round's traces look safe.
- Does not retarget VISTA, OPD, or RRSI.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.22467`
- Code: `none found` (`code_status: none`).
