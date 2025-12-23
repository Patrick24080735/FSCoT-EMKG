# FSCoT-EMKG
# FSCoT-EMKG: Few-shot and CoT Prompting for Equipment O&M KG Construction

This repository contains the core components of the FSCoT-EMKG framework.

## Contents
-`prompts/`: Structured templates for LLM-based extraction.
- `data/`: A de-identified subset of 20 annotated O&M records from the NEV domain.
- `scripts/`:
    - `relation_induction.py`: Implements relation ontology construction using MiniLMv2 and GMM.
    - `example_selection.py`: Implements the performance-driven few-shot selection loop (Algorithm 1).

## Quick Start
1. **Relation Induction**: Run `relation_induction.py` to cluster O&M texts and discover potential relation categories.
2. **Example Selection**: Run `example_selection.py` to identify high-quality few-shot examples based on their F1-score performance.

## Citation
If you use this code or dataset, please cite our paper.
