---
id: method:semicat
type: method
title: SemiCat / DoubleCat
category: architecture
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: "Large Flow Language Models (Lafa blockwise flow from AR init)"
  reason: "SemiCat remains the experimental continuous-DLM hop; Lafa is blockwise flow from AR"
  use_instead: "method:lafa"
- when: recycle an AR post-training weight delta onto a converted discrete dLLM
  reason: A2D remains discrete-dLLM AR-delta recycle; SemiCat is continuous diffusion
    LM pretrain
  use_instead: method:a2d
- when: curriculum RL for a discrete diffusion LM (canvas anneal)
  reason: CanvasAnneal remains discrete-DLM RL; SemiCat is continuous pretrain design
    space
  use_instead: method:canvasanneal
- when: aligning text-to-image diffusion or flow models with rewards
  reason: Image/flow alignment is DiffusionOPSD / Self-OPD
  use_instead: method:diffusion-opsd
assumptions:
- 'Continuous diffusion LM pretrain. Paper: TinyGSM plus 1.7B likelihood evals. Evidence
  is experimental (design-space, not a 7B bake-off).'
- No public code as of 2026-10-13.
last_reviewed: '2026-10-21'
papers:
- paper:dlm-ar-compute-gap
- paper:semicat
recipes:
- recipe:semicat
claims:
- benchmark: TinyGSM; 1.7B likelihood evals vs discrete diffusion
  metric: TinyGSM accuracy; win count on 6 likelihood evals
  value: SemiCat 49.94% TinyGSM (tuned sampler); 1.7B beats discrete diffusion on
    4/6 likelihood evals
  baseline: continuous diffusion without self-conditioning; discrete diffusion LM
  date: '2026-10-13'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.13834
  notes: DoubleCat TinyGSM 4.42%→16.00%; SemiCat 32.90% untuned / 49.94% tuned. Experimental
    first hop. Does not retarget A2D or CanvasAnneal.
tags:
- pretraining
- diffusion-lm
- semicat
- active
---

# SemiCat / DoubleCat

## Method Overview
Continuous diffusion LMs mismatch train and inference unless the network sees its own prediction (self-conditioning). DoubleCat is a two-level interpolant that supplies that match without a second forward. SemiCat additionally reveals discrete tokens during the continuous path.

## When to Use
- Pretrain a continuous diffusion LM. Start from DoubleCat; add SemiCat discrete reveals if TinyGSM-style discrete evals matter.

## When NOT to Use
Discrete dLLM AR-delta recycle → `method:a2d`. Discrete-DLM canvas RL → `method:canvasanneal`. Image/flow reward alignment → `method:diffusion-opsd`.

## Relation to Existing SOTA
Active first hop on `task:continuous-diffusion-lm-pretrain` (`sota_for: []`). Evidence is experimental (design-space, 1.7B). Does **not** replace A2D, CanvasAnneal, or DiffusionOPSD.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-13.
- 49.94% TinyGSM needs the tuned sampler; the untuned SemiCat number is 32.90%.
- Discrete dLLM questions route to `task:diffusion-lm-ar-delta-recycle`, not this card.
