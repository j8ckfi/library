---
id: paper:opsd-collapse-review
type: paper
title: "One Symptom, Three Levers: A Critical Review of On-Policy Self-Distillation"
authors:
  - "Justin Robert"
  - "Raheel Qader"
year: 2026
month: 8
arxiv_id: "2608.25936"
url: "https://arxiv.org/abs/2608.25936"
methods:
  - method:opsd-collapse-review
  - method:vista
  - method:opsa
  - method:grpo
cites:
  - paper:vista
  - paper:grpo
tags:
  - post-training
  - opsd
  - survey
  - opsd-collapse-review
---

# One Symptom, Three Levers: A Critical Review of On-Policy Self-Distillation

## Abstract Summary
On-policy distillation trains a model on its own generations while a teacher scores them token by token. OPSD removes the larger-teacher cost by using the same model with privileged information (reference solution, plan, environment feedback). Early results matched RL accuracy at fewer generated tokens, but the same asymmetry biases the signal. The dominant failure is collapse: progressive narrowing of reasoning paths. Collapse is not unique to OPSD; privileged information aggravates it. The review treats collapse as one symptom with three levers: (i) where the signal is applied (token weights), (ii) what the teacher is shown (privileged information), (iii) when the signal changes (teacher dynamics / guidance decay). Scope is mathematical reasoning. No new experiments.

## Key Contributions
1. **Shared vocabulary** for OPSD collapse vs GRPO entropy collapse vs OPSA-style self-adaptation.
2. **Three levers** as a playbook, not a new optimizer.
3. **Line between settled and disputed** — survey only.

## Empirical Highlights
- None original. Use as ontology for VISTA / OPSD / GRPO / OPSA routing, not as a bake-off.

## Open Source Repository & Resources
- No code (survey).
