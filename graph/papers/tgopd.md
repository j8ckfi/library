---
id: paper:tgopd
type: paper
title: "Verify Before You Distill: Prompt-Level Teacher Gating for On-Policy Distillation"
authors:
  - "Zhiwei Zhang"
  - "Zechen Sun"
  - "Fei Zhao"
  - "Kang Peng"
  - "Bin Liang"
  - "Huayu Deng"
  - "Yao Hu"
  - "Kam-Fai Wong"
  - "Mu Chuan"
year: 2026
month: 9
arxiv_id: "2609.02998"
url: "https://arxiv.org/abs/2609.02998"
methods:
  - method:tgopd
cites:
  - paper:opd
  - paper:ra-opd
  - paper:tropd
  - paper:grpo
  - paper:open-mopd
tags:
  - post-training
  - distillation
  - on-policy
  - teacher-gating
  - tgopd
---

# Verify Before You Distill: Prompt-Level Teacher Gating for On-Policy Distillation

## Abstract Summary
Vanilla OPD admits dense reverse-KL supervision on every prompt without checking whether the teacher is reliable for that prompt. Because reverse KL is mode-seeking, a confidently wrong teacher induces a strong misleading update. Distributional proxies (entropy, teacher–student agreement) do not test outcome correctness. TGOPD estimates prompt-level reliability from a small set of verifier-scored teacher probes and routes exclusively to dense OPD if the check passes, else to verifier-grounded GRPO. The two branches are never blended. Across 4B and 35B students in math, code, and instruction following, TGOPD beats Vanilla OPD in all six single-domain settings and raises seven-benchmark averages under multi-domain training. Probe decode uses otherwise-idle teacher capacity: 4B SOPD teacher-node GPU utilization 9.8% → 78.9%. No official code as of 2026-09-08.

## Key Contributions
1. **Prompt-level reliability gate**: $q_T(x)=K_T^{-1}\sum_k r_k$ from $K_T$ teacher probes; admit dense OPD iff $q_T(x)\ge\tau$, else GRPO (if the student group has reward variation).
2. **Selector, not mix**: $\hat A^{\mathrm{TGOPD}}=g(x)\hat A^{\mathrm{OPD}}+(1-g(x))\hat A^{\mathrm{GRPO}}$ with $g\in\{0,1\}$.
3. **Idle-capacity probes**: overlap teacher decode with student rollout so most audit work fills the scoring idle window.
4. **Code is the failure mode**: teacher confidence AUROC 0.51 on code vs 0.73 on math; highest-confidence low-reliability answers are wrong 84% (code) / 61% (math).

## Empirical Highlights
- Qwen3.5-4B LiveCodeBench: Vanilla OPD 42.3 closes 21% of the 39.4→53.3 base-to-teacher gap; TGOPD 47.1 closes 55% (Table 1).
- Qwen3.6-35B-A3B LCB: TGOPD 64.0 vs base 61.0 vs teacher 62.7; every other distill method is negative transfer (Vanilla OPD 60.2).
- 4B / 35B MOPD seven-bench avg 53.40→54.54 and 60.99→61.94 at 199 steps, $K_T=3$, $\tau=2/3$ (Table 2).
- 4B SOPD teacher utilization 9.8% (59% idle) → 78.9% (0% idle); cluster 51.5% → 69.5% (Table 3).

## Open Source Repository & Resources
- No official GitHub as of 2026-09-08. Paper trains in slime with IcePop; $K_T=3$, $\tau=2/3$.
