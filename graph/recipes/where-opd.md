---
id: recipe:where-opd
type: recipe
title: "Where-OPD Spatial-Hint MLLM OPSD"
method: method:where-opd
task: task:privileged-teacher-opsd
target_hardware: "MLLM OPSD box; paper: Qwen3.5-4B/9B and Qwen3-VL-4B"
framework: "PyTorch OPSD host plus a procedural scene generator"
repo_url: "https://github.com/sirkosophia/Where-OPD"
code_status: released
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - where-opd
  - distillation
  - multimodal
---

# Where-OPD Spatial-Hint MLLM OPSD

## Hardware & Environment Setup
- Official: `https://github.com/sirkosophia/Where-OPD`. `code_status: released`.
- Text-math privileged OPSD stays VISTA. Region-level RL stays Vision-RL2.

```bash
git clone https://github.com/sirkosophia/Where-OPD.git && cd Where-OPD
```

## Quickstart Implementation

```python
from __future__ import annotations


def spatial_hint(objects: list[tuple[str, float, float]]) -> str:
    if not objects:
        raise ValueError("need at least one object with coordinates")
    lines = []
    for name, x, y in objects:
        if not name:
            raise ValueError("object name is empty")
        lines.append(f"{name} at ({x:.1f}, {y:.1f})")
    return "Relevant objects: " + "; ".join(lines)


def teacher_context(image_id: str, question: str, hint: str) -> dict[str, str]:
    if not image_id or not question or not hint:
        raise ValueError("image, question, and hint are required")
    return {"image": image_id, "question": question, "hint": hint}


def student_context(image_id: str, question: str) -> dict[str, str]:
    if not image_id or not question:
        raise ValueError("image and question are required")
    return {"image": image_id, "question": question}
```

Sample \(y\sim\pi_\theta(\cdot\mid I,Q)\). Score prefixes with the teacher given \(h\). Drop \(h\) at inference. Do not crop or zoom the teacher's image.

## Critical Hyperparameters & Tuning Advice
- Post-train on synthetic counting scenes. ChartQA lifts are transfer, not a VISTA math bake-off.
- Human boxes or an external grounder are a different recipe.
