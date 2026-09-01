---
id: method:vista
type: method
title: "VISTA (Verifier-Informed Student-to-Teacher Adaptation)"
category: "distillation"
status: sota
sota_for:
  - task:privileged-teacher-opsd
supersedes: []
papers:
  - paper:vista
recipes:
  - recipe:vista
claims:
  - benchmark: "AIME24 / AIME25 / HMMT25 Avg@12, Qwen3-1.7B instruct"
    metric: "Avg@12 accuracy"
    value: 44.0
    baseline: "OPSD 43.4 / GRPO 37.7"
    date: "2026-08-31"
    verified: true
    notes: "Matched OPSD protocol, OpenThoughts math, 100 updates, global batch 32, 8x H800."
  - benchmark: "AIME24 / AIME25 / HMMT25 Avg@12, Qwen3-4B instruct"
    metric: "Avg@12 accuracy"
    value: 64.3
    baseline: "OPSD 63.6 / GRPO 62.7"
    date: "2026-08-31"
    verified: true
    notes: "Same protocol as 1.7B; k=32 teacher-update positions."
  - benchmark: "AIME24 / AIME25 / HMMT25 Avg@12, Qwen3-8B instruct"
    metric: "Avg@12 accuracy"
    value: 66.9
    baseline: "OPSD 64.8 / GRPO 64.0"
    date: "2026-08-31"
    verified: true
    notes: "Largest gain, +2.1 over OPSD; k=16. Ablation: reverse (fail-only) teacher gate 64.5 < OPSD; verified-only 66.9. Best k in {16, 32}."
tags:
  - post-training
  - distillation
  - self-distillation
  - privileged-teacher
  - opsd
  - vista
  - sota
---

# VISTA (Verifier-Informed Student-to-Teacher Adaptation)

## Method Overview
VISTA keeps the standard on-policy self-distillation (OPSD; Zhao et al., arXiv:2601.18734) student update and adds selective student-to-teacher adaptation:
1. **Privileged OPSD student update**: Problem-only student samples $y \sim \pi_S(\cdot \mid x)$. Privileged teacher $\pi_T(\cdot \mid x, y^\star)$ also sees the gold reference solution. Student loss is clipped full-vocab forward KL $D^{\mathrm{clip}}_{\mathcal{V},\tau}(\operatorname{sg}[P_t^T] \| P_t^S)$ on every student prefix, with $\tau=0.05$.
2. **Outcome-verified teacher gate**: Teacher adaptation is enabled only when a deterministic verifier accepts the completed rollout. Fail-only (reverse) gating underperforms vanilla OPSD.
3. **Top-$k$ teacher-first KL positions**: Within a verified rollout, update the teacher only at the $\min(k, |y|)$ positions with largest $D_{\mathrm{KL}}(P_t^T \| P_t^S)$. Paper uses $k=32$ for 1.7B/4B and $k=16$ for 8B.
4. **Reverse-KL teacher loss**: $L_T$ is reverse KL $D^{\mathrm{clip}}_{\mathcal{V},\tau}(P_t^T \| \operatorname{sg}[P_t^S])$ (mode-seeking) with stop-grad on the student. Combined $L_{\mathrm{total}} = L_S + \lambda L_T$. Independent LoRA adapters ($r=64$, $\alpha=128$); $\eta_S=4\times 10^{-6}$, $\eta_T=3\times 10^{-6}$ so $\lambda=\eta_T/\eta_S=0.75$.
5. **Inference**: Keep only the problem-only student. The privileged teacher is training-time only.

## When to Use
- When gold reference solutions and a deterministic outcome verifier are available, and the teacher is a privileged same-model copy that sees the gold solution — not a larger frozen teacher.
- When vanilla OPSD's teacher-superiority assumption misdirects the student (reference-specific tokens, suppressed valid alternatives).

## Relation to Existing SOTA
- First-hop for `task:privileged-teacher-opsd` only. Does **not** replace `method:opd` (single-teacher student distillation), `method:open-mopd` (multi-teacher), `method:opdvr` (OPD + RLVR with a teacher model and ReLU correctness gating), `method:cispo` (dense math/code RLVR), or `method:u-opsd` (unlabeled / no ground truth).
- Improves vanilla OPSD (Zhao et al. 2601.18734) in the privileged-teacher setting. VISTA does not supersede OPD.
- Teacher-OPD trajectory filtering is `method:ra-opd`; teacher-free self-adaptation is `method:opsa`. Neither replaces VISTA in the privileged-teacher setting.

## Gotchas & Failure Modes
- Requires gold solutions plus a rule-based outcome verifier. Without both, this is the wrong shelf (`method:u-opsd` or `method:ttpo`).
- Reverse (fail-only) teacher gating drops below OPSD (64.5 vs 64.8 on Qwen3-8B). Do not adapt the teacher on rejected rollouts.
- $k$ too small under-adapts; $k$ too large (or all tokens) collapses the teacher toward the student and weakens later supervision. Stay in $\{16, 32\}$.
- Independent student/teacher LoRA adapters are required; a shared adapter would mix the two stop-grad KL directions.
