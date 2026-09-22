---
id: recipe:harness-zero
type: recipe
title: "Harness-Zero Agent-as-Harness Distillation"
method: method:harness-zero
task: task:harness-distillation
target_hardware: "Docker host for Harbor sandboxes plus a model endpoint; Tinker for SFT"
framework: "Python 3.12–3.13 / uv / Harbor 0.21.0"
repo_url: "https://github.com/metaevo-ai/harness-zero"
code_status: released
pip_dependencies:
  - "harbor==0.21.0"
  - "openai>=2.54.0"
tags:
  - recipe
  - harness-zero
  - agent-harness
  - distillation
---

# Harness-Zero Agent-as-Harness Distillation

## Hardware & Environment Setup
- Official: `https://github.com/metaevo-ai/harness-zero`. Models: Hugging Face `metaevo-ai`.
- `uv sync` for rollout + eval. `uv sync --group tinker` for training. Copy `.env.example` to `.env`.
- Target harness stays mini-SWE-agent-style bash. Distill default stays OPD. Kernel stays omp².

```bash
git clone https://github.com/metaevo-ai/harness-zero.git && cd harness-zero
uv sync
```

## Quickstart Implementation

```bash
printf 'uspto-train-000\nuspto-train-001\n' > /tmp/tasks.txt

harness-zero run-rollout \
  --dataset data/uspto \
  --components harness_bank/uspto \
  --teacher-middleware-factory harness_bank.uspto.middlewares:build_teacher_middlewares \
  --tasks-file /tmp/tasks.txt \
  --attempts 1 --concurrency 8 \
  --student-model openai:<student-model> --student-reasoning-effort high \
  --teacher-provider openai --teacher-model <harnessing-model> --teacher-reasoning-effort high \
  --job-name demo --output-dir runs

harness-zero build-sft --trials runs/demo --output sft.jsonl --reward-threshold 1.0
```

The harnessing agent PASS/REPLACE-corrects each student reply into the target action space before execution. Only accepted replies enter the student-visible trajectory.

## Critical Hyperparameters & Tuning Advice
- Do not SFT on \(h^\star\) trajectories. The action-space mismatch is the method.
- Mask reviewer-perspective reasoning in the SFT loss.
- Remove \(h^\star\), \(K\), and the harnessing agent at deploy. The reported 44.3% is under the target harness alone.
