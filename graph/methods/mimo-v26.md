---
id: method:mimo-v26
type: method
title: "MiMo-V2.6"
category: "training-systems"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the production RL engine (SGLang / Megatron / LoRA RL / OPD)"
    reason: "Miles remains the frontier post-train stack; MiMo-V2.6 is a scaled-RL playbook"
    use_instead: "method:miles"
  - when: "full open 8-stage serial post-train recipe on slime"
    reason: "Rufus-Air remains that recipe; MiMo-V2.6 is an omni-modal scaled-RL report"
    use_instead: "method:rufus-air"
  - when: "async straggler algorithm / importance-corrected replay"
    reason: "SAO remains the async-algorithm default"
    use_instead: "method:sao"
  - when: "MoE/VL RLVR loss"
    reason: "SAPO remains MoE/VL"
    use_instead: "method:sapo"
assumptions:
  - "Hybrid-SWA pretrained MoE, omni-modal mid-train, then scaled RL. Freeze the router during RL."
  - "Code announced in the paper; no dedicated GitHub URL confirmed as of 2026-10-09." 
last_reviewed: "2026-10-09"
papers:
  - paper:mimo-v26
recipes:
  - recipe:mimo-v26
claims:
  - benchmark: "MiMo-V2.6 scaled RL report vs prior MiMo / generic async PPO"
    metric: "async tokens per step and training stability knobs"
    value: "1568 samples / 2.7-3.7B tokens per step at up to 1M context; freeze MoE router; groupwise agentic grading"
    baseline: "prior async RL without router freeze / groupwise grading"
    date: "2026-10-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.11959"
    notes: "Playbook, not a Miles retarget. code_status: announced." 
tags:
  - training-systems
  - moe
  - rlvr
  - mimo-v26
  - active
---

# MiMo-V2.6

## Method Overview
After multimodal mid-training, scale RL on three axes: async batch and context, mixed-task harnesses, and groupwise agentic graders. Freeze the MoE router. Keep train-infer consistency and a reward-hacking defense stack.

## When to Use
- Frontier MoE RL at long context where router drift or noisy long-horizon grades are the failure mode.

## When NOT to Use
- Production engine -> `method:miles`. Open 8-stage slime recipe -> `method:rufus-air`. Async stragglers -> `method:sao`.

## Relation to Existing SOTA
- Active plug-in on `task:frontier-rl-posttrain-stack` (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace Miles.

## Gotchas & Failure Modes
- **code: announced** as of 2026-10-09; no dedicated GitHub URL confirmed.
- Router freeze is a stability knob, not a SAPO replacement.
