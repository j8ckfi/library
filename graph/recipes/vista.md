---
id: recipe:vista
type: recipe
title: "VISTA Privileged-Teacher OPSD Recipe"
method: method:vista
task: task:privileged-teacher-opsd
target_hardware: "8x NVIDIA H800 80GB"
framework: "PyTorch 2.8 / verl 0.6.1 / vLLM 0.11.0"
repo_url: "none found"
pip_dependencies:
  - "torch==2.8.0"
  - "verl==0.6.1"
  - "vllm==0.11.0"
  - "transformers>=4.51.0"
  - "peft>=0.14.0"
tags:
  - recipe
  - distillation
  - privileged-teacher
  - opsd
  - vista
---

# VISTA Privileged-Teacher OPSD Recipe

## Hardware & Environment Setup
- Recommended Hardware: 8x NVIDIA H800 80GB (paper; H100 is the closest substitute).
- Stack: Python 3.12, CUDA 12.8, PyTorch 2.8, verl 0.6.1, vLLM 0.11.0.
- No official GitHub as of 2026-08-31. Reimplement Algorithm 1 on verl with independent student and teacher LoRA adapters.

## Quickstart Implementation

```python
import torch
import torch.nn.functional as F


def clipped_full_vocab_kl(p: torch.Tensor, log_q: torch.Tensor, tau: float) -> torch.Tensor:
    """Pointwise-clipped full-vocab KL: sum_v min(P(v) log P(v)/Q(v), tau)."""
    log_p = p.clamp_min(1e-12).log()
    per_vocab = p * (log_p - log_q)
    return torch.minimum(per_vocab, torch.full_like(per_vocab, tau)).sum(dim=-1)


def compute_vista_losses(
    student_logits: torch.Tensor,
    teacher_logits: torch.Tensor,
    verified: bool,
    k: int = 32,
    tau: float = 0.05,
) -> tuple[torch.Tensor, torch.Tensor]:
    """VISTA minibatch losses for one student rollout (paper Algorithm 1).

    Args:
        student_logits: Problem-only student logits on prefixes y_<t, shape [T, V].
        teacher_logits: Privileged teacher logits on the same prefixes, shape [T, V].
        verified: True iff a deterministic outcome verifier accepts the completed rollout.
        k: Top-k teacher-update positions (32 for 1.7B/4B, 16 for 8B).
        tau: Pointwise KL clip (paper uses 0.05).

    Returns:
        (L_S, L_T) where L_T is zero on unverified rollouts. Combine as L_S + lambda L_T
        with lambda = eta_T / eta_S = 0.75, or step each adapter with eta_S and eta_T.
    """
    p_s = F.softmax(student_logits, dim=-1)
    p_t = F.softmax(teacher_logits, dim=-1)
    log_s = F.log_softmax(student_logits, dim=-1)
    log_t = F.log_softmax(teacher_logits, dim=-1)

    # Student: forward KL D(sg[P^T] || P^S) on every prefix.
    student_loss = clipped_full_vocab_kl(p_t.detach(), log_s, tau).mean()

    if not verified or student_logits.size(0) == 0:
        teacher_loss = student_logits.new_zeros(())
        return student_loss, teacher_loss

    # Rank by unclipped teacher-first KL(P^T || P^S).
    ranking_kl = (p_t.detach() * (p_t.detach().clamp_min(1e-12).log() - log_s.detach())).sum(dim=-1)
    topk = min(k, ranking_kl.numel())
    selected = torch.topk(ranking_kl, k=topk, largest=True).indices

    # Teacher: reverse KL D(P^T || sg[P^S]) on selected positions only.
    teacher_kl = clipped_full_vocab_kl(p_t[selected], log_s.detach()[selected], tau)
    teacher_loss = teacher_kl.mean()
    return student_loss, teacher_loss
```

## Critical Hyperparameters & Tuning Advice
- **LoRA**: Independent student and teacher adapters, $r=64$, $\alpha=128$, targets `q_proj,k_proj,v_proj,o_proj,gate_proj,up_proj,down_proj`.
- **Rates**: $\eta_S=4\times 10^{-6}$, $\eta_T=3\times 10^{-6}$ ($\lambda=0.75$). AdamW, zero weight decay.
- **Position budget $k$**: 32 for 1.7B/4B, 16 for 8B. Best $k$ in $\{16, 32\}$.
- **Clip $\tau$**: 0.05. Full-vocab forward KL ($\beta=0$) for the student.
- **Budget**: 100 updates, global batch 32, one rollout per prompt, score first 1,024 tokens, verify up to 4,096 new tokens.
- **Data / models**: OpenThoughts mathematical-reasoning pool; Qwen3-1.7B/4B/8B instruct. Student sees the problem only (thinking off); teacher sees problem plus reference (thinking on).
- **Teacher gate**: Verifier-accepted rollouts only. Do not use fail-only adaptation.
