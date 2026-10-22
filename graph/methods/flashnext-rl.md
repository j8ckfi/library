---
id: method:flashnext-rl
type: method
title: 'FlashNext-RL'
category: training-systems
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'the locked first hop on task:frontier-rl-posttrain-stack'
  reason: 'FlashNext-RL is an active plug-in; method:miles remains the first hop'
  use_instead: method:miles
assumptions:
- '8xB200 trainer + vLLM SWE rollouts. prime-rl host. No dedicated public repo as of 2026-10-22.'
last_reviewed: '2026-10-22'
papers:
- paper:flashnext-rl
recipes:
- recipe:flashnext-rl
claims:
- benchmark: 'Qwen3.8-Flash-Next 48-layer BF16 on 8xB200; live SWE RL'
  metric: 'tokens/s/GPU and iteration time at 131K'
  value: 'full-model non-padding throughput 395 to 4438 tok/s/GPU (32K to 131K optimized); steps 5-15 average 22.4 min/iter at 1024 trainable rollouts / 131072 context'
  baseline: 'initial 32K-token Flash-Next RL configuration at ~395 tok/s/GPU'
  date: '2026-10-22'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.28998'
  notes: 'Does not retarget method:miles.'
tags:
- systems
- agentic-rl
- active
---

# FlashNext-RL

## Method Overview
FlashNext-RL is a prime-rl + vLLM stack for Qwen3.8-Flash-Next: freeze early layers / n-gram / indexer / MTP, then host-offload, MoE, sparse-attention, and gated-residual kernels so 131K SWE RL fits one 8xB200 node.

## When to Use
- Long-horizon SWE RL on Qwen3.8-Flash-Next when generic Miles/slime configs OOM or stall on Flash-Next operators.

## When NOT to Use
Generic production stack → `method:miles`. Architecture recipe → `method:qwen38-next`. Async algorithm → `method:sao`.

## Relation to Existing SOTA
Active plug-in (`sota_for: []`). Does **not** replace `method:miles`.

## Gotchas & Failure Modes
- Model-specific; not a Miles replacement.
- First two layers, n-gram table, sparse-attention indexer, and MTP head stay frozen in the paper recipe.
