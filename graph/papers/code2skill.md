---
id: paper:code2skill
type: paper
title: "Grounded Skill Synthesis from Code at Scale for Agentic Intelligence"
authors:
  - "Yongqi Tong"
  - "Pan Wang"
  - "Hang Wang"
  - "Jianshe Li"
  - "Xin Zhang"
  - "Jiang-Ming Yang"
  - "Wei Wu"
year: 2026
month: 9
arxiv_id: "2609.05571"
url: "https://arxiv.org/abs/2609.05571"
methods:
  - method:code2skill
cites:
  - paper:ace
  - paper:mini-swe-agent
tags:
  - agents
  - agent-memory
  - skills
  - code2skill
---

# Grounded Skill Synthesis from Code at Scale for Agentic Intelligence

## Abstract Summary
Reusable skills give agents transferable procedural knowledge. Trajectory-derived banks need interaction experience; document-derived skills often lack executable evidence. Code2Skill (Ant International) lifts selected code units into verified atomic-operation, composite-workflow, and recurring-pattern skill records, then checks each record with source-body-blind reconstruction and source-aware comparison. Applied to 19,769 popular GitHub repositories it yields CodeSkillBank: 1,006,822 accepted records with workflow, boundary, provenance, and source-evidence metadata. Retrieved skills improve matched agent loops before the agent has accumulated task-specific trajectories, and they beat trajectory-derived banks on shared benches under a unified downstream interface.

## Key Contributions
1. **Code-to-skill pipeline**: rank source units, emit typed records, reconstruct without the source body, judge against the original.
2. **CodeSkillBank**: ~1.0M accepted records from 19,769 repos, with provenance and retrieval-facing views.
3. **Before-experience skills**: repository-derived procedures help at planning and post-generation review, including a coding-RL interface study.

## Empirical Highlights
- Macro-average 42.90 → 47.90 (+11.7% relative) across 72 protocol-matched evaluations / 8 benches / 9 model settings; 57 of 72 improve.
- Under a shared loop, Code2Skill 49.5 vs Trace2Skill 31.0 / ExpeL 27.9 / SkillRL-Bank 32.8 on seven shared benches.
- SWE-World coding RL at step 150: post-generation review 38% resolve vs no-skill 24%.
- Skills from tested AI-generated code pass 93.50% vs 93.00% for human-written code on a 400-task LiveCodeBench subset.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.05571`
- Code: `https://github.com/ant-intl/Code2Skill` (pre-release publication implementation as of 2026-09-21)
- Dataset: `https://huggingface.co/datasets/ant-intl/DeveloperSkills-Code2Skill`
- Site: `https://ant-international-research.github.io/developer-skill-hubs/`
