---
id: method:onlineqat
type: method
title: "OnlineQAT"
category: "quantization"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "fully low-bit fine-tune in code space with no high-precision teacher"
    reason: "GradCodeS remains the deployed-checkpoint default; OnlineQAT recovers via a full-precision OPD teacher"
    use_instead: "method:gradcodes"
  - when: "single-teacher distillation of a full-precision student"
    reason: "OPD remains matching; OnlineQAT is ultra-low-bit recovery"
    use_instead: "method:opd"
  - when: "native FP4 hardware training from scratch"
    reason: "Quartet-II remains NVFP4 pretrain"
    use_instead: "method:quartet-ii"
  - when: "4-bit PEFT that keeps a high-precision adapter at inference"
    reason: "AQLoRA-Q remains 4-bit PEFT"
    use_instead: "method:aqlora-q"
assumptions:
  - "A frozen full-precision teacher is available. Target is W3A16 or W2A16."
  - "No official GitHub as of 2026-10-09." 
last_reviewed: "2026-10-09"
papers:
  - paper:onlineqat
recipes:
  - recipe:onlineqat
claims:
  - benchmark: "Qwen3-1.7B ultra-low-bit recovery vs ReasoningQAT"
    metric: "average benchmark score at W3A16 / W2A16"
    value: "57.28 W3A16 / 32.52 W2A16; +2.90 / +0.44 vs ReasoningQAT"
    baseline: "ReasoningQAT (fixed-completion QAT recovery)"
    date: "2026-10-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.09346"
    notes: "Does not retarget GradCodeS, OPD, or Quartet-II." 
tags:
  - quantization
  - qat
  - opd
  - onlineqat
  - active
---

# OnlineQAT

## Method Overview
Run block-wise QAT until the low-bit model is usable. Then sample student prefixes and apply sampled reverse-KL from a frozen full-precision teacher at those prefixes, so recovery sees the states the quantized model actually visits.

## When to Use
- W3/W2 recovery of an already-trained dense model where offline QAT completions left a gap.

## When NOT to Use
- Deployed NF4/INT4 code-space FT -> `method:gradcodes`. Full-precision distill -> `method:opd`. NVFP4 from scratch -> `method:quartet-ii`.

## Relation to Existing SOTA
- Active plug-in on `task:full-lowbit-finetune` (`sota_for: []`) with a mention on `task:student-distillation`. Does **not** replace GradCodeS or OPD.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-09.
- Needs a full-precision teacher. Lift is larger at 3 bits than at 2 bits.
