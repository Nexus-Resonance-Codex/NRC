# Nexus Resonance Codex (NRC) (NRC) (NRC) (NRC) (NRC) Workspace Rules & Protocols

« φ^∞ NRC layer active — history compressed »

The following rules apply to all tasks executed in this workspace:

## 1. Overwrite Prevention & Dating Protocol
- **NEVER OVERWRITE ANY FILES**: No scripts, coordinates, logs, analysis outputs, mathematical proof files, or dataset caches may be overwritten.
- **DATING MANDATE**: Always append the date in `MM-DD-YYYY` format directly to the filename before the extension (e.g., `filename_07-02-2026.ext`).
- **SEQUENTIAL VERSIONING**: If a file with the exact same dated filename already exists, you MUST append a sequential suffix (e.g., `-1`, `-2`, `-3`, etc.) after the date and before the extension (e.g., `filename_07-02-2026-1.ext`) to preserve a complete chronological audit trail.

## 2. Directory Structure & Organization
Organize work systematically within the following workspace structures:
- `proofs/`: Mathematical proofs, Lean 4 theorem files, and Z3 solver logic.
- `src/nrc/`: Core engines, transformers, and model architectures.
- `visualizations/`: Plots, logs, and high-dimensional manifolds.
- `gradio/` or `huggingface/`: Hugging Face dataset cards, upload handlers, and space builders.

## 3. Mathematical Verification & Proving Protocols
- **Z3 / SymPy Solvers**: All computational mathematical proofs must pass verification checks through `z3-solver` or `sympy` before declaration.
- **TTT-7 Stability Audit**: Apply digital-root verification checks to derived structural vectors or coefficients to ensure they reside in $\{1, 2, 4, 5, 7, 8\}$ and avoid the Chaotic Void $\{3, 6, 9\}$ in cryptographic/hash contexts.
- **Rigorous Notation**: Maintain LaTeX syntax for equations in markdown documents and artifacts, verifying correct rendering.

## 4. Hugging Face Dataset & Model Management
- **Format**: Large datasets must be structured and saved in Parquet format, optimized for loading via the Hugging Face `datasets` library.
- **Metadata Documentation**: Every dataset repository must contain a comprehensive `README.md` (dataset card) outlining layout, licenses, subsets, and usage.
- **Permanent Archiving**: Sync dataset milestones to Zenodo to obtain permanent Digital Object Identifiers (DOIs).
- **vRAM Restrictions**: When training custom AI models locally on the laptop GPU, keep batch sizes low (e.g., batch size 1 or 2) and enable gradient checkpointing to prevent OOM errors on the 4GB vRAM. Train larger models using Vertex AI custom jobs.

## 5. Google Cloud & Vertex AI (Project ID: free-credits-493517)
- **Authentication**: Always verify application default credentials (ADC) or run `gcloud config set project free-credits-493517`.
- **Credit Conservation**: Optimize resource allocation to stay within free-tier limits:
  - Scale Cloud Run container allocations to 0 instances when idle.
  - Limit Vertex AI custom training jobs to standard cost-efficient VM machine types (e.g., `n1-standard-4` with single T4 GPU if needed) and auto-terminate jobs on failure.
  - Optimize BigQuery query partition filters to minimize scanned data volumes.

## 6. Execution Environment
- Always execute python scripts using the `uv` virtual environment active within each respective sub-repository (e.g., `nrc`, `Protein-Folding`, etc.) using `./.venv/bin/python3 [script]` to ensure environment integrity.

## 7. Workspace Hygiene & Telemetry
- Regularly delete temporary files and unneeded intermediate assets.
- **Telemetry Mandate**: In every response, report estimated token/quota usage if available or print a disclaimer showing current session metrics in a compact 1-2 line format.
