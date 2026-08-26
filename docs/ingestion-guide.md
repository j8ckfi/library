# 5-Minute Paper Ingestion Guide

Follow these steps whenever adding a new paper or method to `j8ckfi/library`.

---

## Ingestion Checklist

```
[ ] 1. Choose a clean kebab-case slug for the paper and method
[ ] 2. Scaffold node templates
[ ] 3. Fill in YAML frontmatter and markdown sections
[ ] 4. Update parent task's current_sota (if new SOTA)
[ ] 5. Run validation: python -m library validate
```

---

## Step 1: Scaffold Files

Run the CLI scaffolding command:

```bash
# Scaffold the paper
python -m library new paper <paper-slug> --title "Paper Title"

# Scaffold the method
python -m library new method <method-slug> --title "Method Name"

# Scaffold the recipe
python -m library new recipe <recipe-slug> --title "Recipe Title"
```

Files are automatically generated in `graph/papers/`, `graph/methods/`, and `graph/recipes/`.

---

## Step 2: Complete the Nodes

### Paper (`graph/papers/<paper-slug>.md`)
- Populate `authors`, `year`, `month`, `arxiv_id`, and `url`.
- Add linked `methods: [method:<method-slug>]`.
- Write a 2-3 paragraph abstract summary and bulleted key contributions.

### Method (`graph/methods/<method-slug>.md`)
- Define `category`, `status` (`sota`, `active`, `superseded`, `niche`, `experimental`).
- Add relations:
  - `sota_for: [task:<task-slug>]`
  - `supersedes: [method:<old-slug>]`
  - `papers: [paper:<paper-slug>]`
  - `recipes: [recipe:<recipe-slug>]`
- Add dated `claims` with benchmark, metric, baseline, and verification status.
- Write: Overview, When to Use, Gotchas & Failure Modes.

### Recipe (`graph/recipes/<recipe-slug>.md`)
- Specify `target_hardware`, `framework`, `repo_url`, and `pip_dependencies`.
- Provide a clean, executable PyTorch/JAX code snippet and critical hyperparameter guidance.

---

## Step 3: Handle Supersession (If Replacing Existing SOTA)

If this method beats an existing SOTA method:
1. In the old method's file (`graph/methods/<old-slug>.md`), set:
   ```yaml
   status: superseded
   superseded_by: method:<new-slug>
   ```
2. In the corresponding task (`graph/tasks/<task-slug>.md`), update `current_sota`:
   ```yaml
   current_sota:
     - method: method:<new-slug>
       as_of: "2026-02"
       benchmark: "MMLU-Pro"
       metric: "accuracy"
       value: 78.4
       notes: "Evaluated at equal compute budget"
   ```

---

## Step 4: Validate

Ensure graph consistency, referential integrity, and absence of cycles:

```bash
python -m library validate
```

Ensure the CLI query finds the new method:

```bash
python -m library sota <task-slug>
```
