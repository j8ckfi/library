---
id: recipe:on-policy-distillation
type: recipe
title: "On-Policy Distillation (GKD) Training Pipeline"
method: method:on-policy-distillation
task: task:student-distillation
target_hardware: "4x or 8x NVIDIA A100 / H100 80GB"
framework: "PyTorch 2.5+ / vLLM / Hugging Face TRL"
repo_url: "https://github.com/huggingface/trl"
pip_dependencies:
  - "torch>=2.5.0"
  - "trl>=0.14.0"
  - "transformers>=4.48.0"
  - "vllm>=0.7.0"
tags:
  - distillation
  - on-policy
  - gkd
---

# On-Policy Distillation (GKD) Training Pipeline

## Hardware & Environment Setup
- Recommended Hardware: 4x or 8x NVIDIA H100 80GB (SXM).
- Framework: PyTorch 2.5.0+, Hugging Face TRL GKDTrainer / custom on-policy rollout.

## Quickstart Code

```python
import torch
import torch.nn.functional as F
from transformers import AutoModelForCausalLM, AutoTokenizer

def on_policy_distill_step(
    student_model,
    teacher_model,
    prompt_ids: torch.Tensor,
    max_new_tokens: int = 256,
    beta: float = 0.5
):
    """Executes one on-policy distillation step by sampling from student and scoring with teacher."""
    student_model.eval()
    
    # 1. On-Policy Rollout: Sample completion tokens from STUDENT
    with torch.no_grad():
        student_rollout = student_model.generate(
            prompt_ids,
            max_new_tokens=max_new_tokens,
            do_sample=True,
            temperature=0.8,
            top_p=0.95
        )
    
    # 2. Compute logits across the generated sequence
    student_model.train()
    student_logits = student_model(student_rollout).logits
    with torch.no_grad():
        teacher_logits = teacher_model(student_rollout).logits
    
    # 3. Calculate sequence-level reverse/mixed KL divergence on rollout tokens
    student_logprobs = F.log_softmax(student_logits, dim=-1)
    teacher_probs = F.softmax(teacher_logits, dim=-1)
    
    # Mixed reverse KL divergence loss
    kl_loss = F.kl_div(student_logprobs, teacher_probs, reduction="batchmean")
    return kl_loss
```

## Critical Guidance
- **Student Sampling**: Always sample from the student policy during training to expose the student to its own generation distribution.
- **Teacher Scoring**: Teacher remains frozen in FP16/BF16 (or hosted via vLLM inference engine).
