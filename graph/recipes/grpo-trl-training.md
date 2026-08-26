---
id: recipe:grpo-trl-training
type: recipe
title: "Large-Scale Reasoning RL with GRPO via Hugging Face TRL"
method: method:grpo
task: task:reasoning-rl-alignment
target_hardware: "4x or 8x NVIDIA H100 80GB SXM"
framework: "PyTorch 2.5+ / HuggingFace TRL (>=0.14.0)"
repo_url: "https://github.com/huggingface/trl"
pip_dependencies:
  - "torch>=2.5.0"
  - "trl>=0.14.0"
  - "transformers>=4.48.0"
  - "accelerate>=1.2.0"
  - "vllm>=0.7.0"
tags:
  - rl-alignment
  - reasoning
  - deepseek-r1
  - grpo
---

# Large-Scale Reasoning RL with GRPO via Hugging Face TRL

## Hardware & Environment Setup
- Recommended GPU: 8x NVIDIA H100 80GB SXM (enables high-throughput vLLM rollout generation).
- Minimum GPU: 4x A100 80GB.
- Software Stack: PyTorch 2.5.0+, TRL 0.14.0+, vLLM 0.7.0+.

## Quickstart Code

```python
import re
from trl import GRPOTrainer, GRPOConfig
from datasets import load_dataset

# 1. Deterministic Rule-Based Verifiers
def correctness_reward_func(prompts, completions, answer, **kwargs) -> list[float]:
    """Extracts boxed final answer and evaluates exact mathematical equivalence."""
    rewards = []
    for completion, target in zip(completions, answer):
        # Extract content inside \boxed{...} or <answer>...</answer>
        match = re.search(r"\\boxed\{(.*?)\}", completion)
        if match:
            pred = match.group(1).strip()
            rewards.append(1.0 if pred == str(target).strip() else 0.0)
        else:
            rewards.append(0.0)
    return rewards

def format_reward_func(completions, **kwargs) -> list[float]:
    """Rewards adherence to structured reasoning markup (<think>...</think><answer>...</answer>)."""
    pattern = r"^<think>.*?</think>\s*<answer>.*?</answer>$"
    return [0.5 if re.match(pattern, c, re.DOTALL) else 0.0 for c in completions]

# 2. Configure GRPO Training Parameters
training_args = GRPOConfig(
    output_dir="./grpo_reasoning_output",
    learning_rate=1e-6,
    per_device_train_batch_size=2,
    gradient_accumulation_steps=4,
    num_generations=8,             # Group size G sampled per prompt
    max_prompt_length=512,
    max_completion_length=2048,
    beta=0.04,                     # KL penalty coefficient
    use_vllm=True,                 # Accelerated rollout engine
    vllm_device="auto",
    vllm_gpu_memory_utilization=0.5,
    logging_steps=10
)

# 3. Instantiate and Train
# trainer = GRPOTrainer(
#     model="Qwen/Qwen2.5-7B-Instruct",
#     reward_funcs=[correctness_reward_func, format_reward_func],
#     args=training_args,
#     train_dataset=dataset,
# )
# trainer.train()
```

## Critical Hyperparameters & Guidance
- **Group Size (`num_generations`)**: Set to 8 or 16 for stable group variance estimation.
- **KL Coefficient (`beta`)**: 0.01 to 0.05. If training collapses or outputs become repetitive, increase \(\beta\).
- **vLLM Rollout Acceleration**: Essential to maintain high GPU compute utilization during multi-step reasoning rollouts.
