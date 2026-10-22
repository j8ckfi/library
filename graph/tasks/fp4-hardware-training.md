---
id: task:fp4-hardware-training
type: task
title: "Native FP4 Hardware Training"
domain: "compression"
summary: "End-to-end 4-bit floating-point forward and backward pass training on modern GPU accelerators."
redirects:
  - when: "2:4 semi-structured sparsity vs dropping to the next lower precision"
    to: "paper:sparsity-24-vs-quant"
  - when: "NVFP4 pretrain recipe ingredients at 8B / 30B-A3B (not Quartet-II default)"
    to: "method:nvfp4-pretrain-recipe"
  - when: "dual-scale calibration-free W+A PTQ for AR LLMs (not native FP4 training)"
    to: "method:dualquant"
  - when: "calibration-free dLLM quantization (SoloQ; mask/step activation shift)"
    to: "method:soloq"
  - when: "FP4 RL train-side vs rollout-side quantization mismatch (TRACE / TRIAGE)"
    to: "task:fp4-rl-train-rollout-alignment"
  - when: "mixed-precision scaling law for which forward/backward pass to keep high precision"
    to: "method:mixed-precision-scaling"
current_sota:
  - method: method:quartet-ii
    as_of: "2026-08-26"
    benchmark: "NVFP4 Hardware Training Benchmarks"
    metric: "training throughput & numerical stability"
    value: "Default SOTA for NVFP4 hardware training"
    notes: "Quartet-II NVFP4 (2601.22813) / MXFP4 (2605.09825) / Kimi-K3 QAT."
  - method: method:mxfp4-mi355x
    as_of: "2026-08-26"
    benchmark: "Microscaled FP4 Benchmark"
    metric: "numerical stability"
    value: "Co-Default SOTA for microscaling FP4"
    notes: "MXFP4 (2605.09825)."
methods:
  - method:nvfp4-pretrain-recipe
  - method:mixed-precision-scaling
  - method:dualquant
  - method:soloq
  - method:quartet-ii
  - method:mxfp4-mi355x
  - method:kimi-k3
  - method:gradcodes
  - method:kbbq
  - method:trace
  - method:triage
last_reviewed: '2026-10-22'
tags:
  - compression
  - quantization
  - fp4
  - hardware-training
---

# Native FP4 Hardware Training

## SOTA Recommendation (as of 2026-08-26)
- **Primary Method**: **Quartet-II NVFP4** (`method:quartet-ii`, 2601.22813) / **MXFP4** (`method:mxfp4-mi355x`, 2605.09825) / **Kimi-K3 QAT**. Unchanged.
- **Fully low-bit fine-tune of an already-quantized checkpoint**: `method:gradcodes` on `task:full-lowbit-finetune`. Not native FP4 hardware training.
- **Optional W4A4 noise-law / spectrum-flattening note**: `method:kbbq` (`arXiv:2609.08135`). Active PTQ-style inference niche. Does not replace Quartet-II or MXFP4.
- **Optional calibration-free W+A PTQ (not this training default)**: `method:dualquant` (`arXiv:2610.13767`) dual-scale reconstruction MSE; matches or exceeds SmoothQuant without calibration; packed W4A4 up to 2.61× memory cut. No public code. Does not replace Quartet-II, KBBQ, or AQLoRA-Q.
- **Optional calibration-free dLLM PTQ (not this training default)**: `method:soloq` (`arXiv:2610.07121`) rotation PTQ for full-sequence and block-diffusion LMs; NVFP4 up to 2.61× peak-memory / 2.24× e2e. GitHub Intelligent-Computing-Lab-Panda/SoloQ 404. Does not replace Quartet-II or A2D.
- **Not this task (FP4 RL train–rollout mismatch)**: `task:fp4-rl-train-rollout-alignment` / `method:trace` (`arXiv:2610.07767`) + `method:triage` (`arXiv:2610.07043`). Dual-active. Does not replace Quartet-II.

- **Optional mixed-precision scaling law (not this training default)**: `method:mixed-precision-scaling` (`arXiv:2610.17637`). Separates capacity vs optimization-error of forward/backward quantization. Fwd-only NVFP4 +0.94–1.22% vs bwd-only +0.32–0.72% on 430M Qwen3 at 12.8B tokens. No public code. Does not replace Quartet-II / MXFP4.
- **Optional NVFP4 pretrain recipe ablation**: `method:nvfp4-pretrain-recipe` (`arXiv:2610.24343`, ICML 2026 AdaptFM). Selective high-precision layers; stacked recipe vs NVIDIA 2025 / Quartet-II / TetraJet. Does not replace Quartet-II.
