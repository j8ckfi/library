---
id: recipe:opd-then-rlvr
type: recipe
title: "OPD-then-RLVR Sequential Recipe"
method: method:opd-then-rlvr
task: task:student-distillation
target_hardware: "8x NVIDIA H100 80GB class (paper: veRL, Qwen3-1.7B student + 8B teacher)"
framework: "PyTorch / veRL"
repo_url: "https://github.com/StringNLPLAB/opd-rlvr"
pip_dependencies:
  - "torch>=2.5.0"
  - "verl>=0.4.0"
  - "transformers>=4.51.0"
  - "vllm>=0.7.0"
tags:
  - recipe
  - opd
  - rlvr
  - scheduling
---

# OPD-then-RLVR Sequential Recipe

## Hardware & Environment Setup
- Official code: `https://github.com/StringNLPLAB/opd-rlvr`. veRL + vLLM, FSDP bf16. Paper: student Qwen3-1.7B-Base, teacher Qwen3-8B non-thinking, G=8, AdamW $1\times10^{-6}$, clip 0.2, no KL penalty.
- Stage 2 in the paper is GRPO. For Pass@1 labeled RLVR outside this reproduction, use `method:cispo` as the RL algorithm; keep the OPD-then-RL *order*.
- Host distill algorithm stays `method:opd`. Single-step gated fusion stays `method:opdvr`.

## Quickstart Implementation

```python
def advantage_for_step(step: int, switch_s: int, opd_adv, rl_adv):
    """Exclusive stages. Never add OPD and RL advantages on the same step."""
    if int(step) <= int(switch_s):
        return opd_adv
    return rl_adv


def should_switch(opd_val_history, plateau_steps: int = 20) -> bool:
    """Switch when OPD validation has stopped climbing, not at a blind step count."""
    if len(opd_val_history) < plateau_steps + 1:
        return False
    recent = opd_val_history[-plateau_steps:]
    return max(recent) <= opd_val_history[-plateau_steps - 1] + 1e-6
```

## Critical Hyperparameters & Tuning Advice
- Paper default $S=60$ (logic 150 steps / DeepMath 120). Prefer the OPD val plateau over copying 60.
- Mask the final EOS position in the teacher term if student and teacher EOS ids differ.
- Do not anneal a joint $\beta$ as a substitute; KDRL-Annealing lost to hard switch (logic 68.9 vs 80.6).
- Does not replace OPD, CISPO, or OPDVR.
