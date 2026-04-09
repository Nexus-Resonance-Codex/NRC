# mypy: ignore-errors
#!/usr/bin/env python3
"""NRC Interactive Gradio Space.

Three-tab interactive app demonstrating the full Nexus Resonance Codex
mathematical and AI framework. Runs on HuggingFace Spaces (CPU tier).
"""

import math
from typing import Any, Tuple

import numpy as np

import gradio as gr

# ─────────────────────────── NRC Math (inline, no pip install needed) ──────────
PHI = (1.0 + math.sqrt(5.0)) / 2.0
PHI_INV = 1.0 / PHI
SQRT5 = math.sqrt(5.0)
SQRT2 = math.sqrt(2.0)
PI = math.pi
GIZA_DEG = 51.853
GIZA_RAD = GIZA_DEG * (PI / 180.0)


def binet(n: int) -> float:
    """Calculates the n-th Fibonacci value via continuous Binet projection."""
    return (PHI**n - (-PHI) ** (-n)) / SQRT5


def qrt(x: float) -> float:
    """Computes the Quantum Residue Turbulence (QRT) fractal damping at point x."""
    return math.sin(PHI * SQRT2 * GIZA_DEG * x) * math.exp(-(x**2) / PHI) + math.cos(PI / PHI * x)


def mst(x: float) -> float:
    """Calculates a single step of the Modular Synchronisation Theory (MST) map."""
    xp = abs(x) + 1e-9
    return (math.floor(1000.0 * math.sinh(xp)) + math.log(xp**2 + 1.0) + (PHI**xp)) % 24389


def tupt_gate(x: float) -> float:
    """Applies the TUPT 3-6-9-7 Exclusion Principle; returns 0 if excluded."""
    mod_val = x % 9
    if mod_val in [0, 3, 6, 9]:
        return 0.0
    return x


def phi_fold(x: float, iterations: int = 5) -> float:
    """Applies recursive Phi-Infinity folding to the scalar input x."""
    for n in range(1, iterations + 1):
        x = (PHI**n) * x + (1.0 / SQRT5)
    return x


def lattice_norm(x: float) -> float:
    """Projects scalar x into the 2048D lattice and returns the Euclidean norm."""
    dims = np.arange(2048, dtype=np.float64)
    vec = x * np.power(PHI, -dims / 2048) * np.cos(dims * GIZA_RAD)
    return float(np.linalg.norm(vec))


# Amino acid masses
AA_MASS = {
    "A": 71.04,
    "R": 156.19,
    "N": 114.10,
    "D": 115.09,
    "C": 103.14,
    "E": 129.12,
    "Q": 128.13,
    "G": 57.05,
    "H": 137.14,
    "I": 113.16,
    "L": 113.16,
    "K": 128.17,
    "M": 131.19,
    "F": 147.18,
    "P": 97.12,
    "S": 87.08,
    "T": 101.11,
    "W": 186.21,
    "Y": 163.18,
    "V": 99.13,
}


# ─────────────────────────── Tab 1: NRC Math Explorer ──────────────────────────
def explore_nrc_math(x_val: float, fib_n: int) -> Tuple[str, Any]:
    """Executive explorer function calculating all NRC primitives for a given input."""
    qrt_v = qrt(x_val)
    mst_v = mst(x_val)
    tupt_v = tupt_gate(x_val)
    fold_v = phi_fold(x_val)
    bn = binet(int(fib_n))
    l_norm = lattice_norm(x_val)

    stability = (
        "🔴 EXCLUDED (Void)"
        if tupt_v == 0
        else ("🟡 RESONANT" if abs(qrt_v) < 0.5 else "🟢 STABLE")
    )

    table_md = f"""
| Operation | Result |
|:----------|-------:|
| **φ (Golden Ratio)** | `{PHI:.15f}` |
| **QRT Wave** `QRT({x_val})` | `{qrt_v:.8f}` |
| **MST Step** `MST({x_val})` | `{mst_v:.4f}` |
| **TUPT Gate** | `{tupt_v:.4f}` |
| **φ^∞ Fold** (5 iter) | `{fold_v:.6f}` |
| **Binet F({int(fib_n)})** | `{bn:.4f}` |
| **2048D Lattice ‖L‖** | `{l_norm:.6f}` |
| **NRC Stability** | {stability} |
"""

    return table_md, None


# ─────────────────────────── Tab 2: Protein Sequence → Lattice ─────────────────
def project_sequence(sequence: str) -> str:
    """Projects a raw amino acid sequence into the 2048-dimensional φ-lattice."""
    sequence = sequence.upper().strip()
    if not sequence:
        return "_Please enter a valid amino acid sequence._"

    masses = [AA_MASS.get(aa, 0.0) for aa in sequence]
    valid = [(aa, m) for aa, m in zip(sequence, masses, strict=False) if m > 0]
    unknown = [aa for aa in sequence if aa not in AA_MASS]

    if not valid:
        return "⚠️ No recognized amino acids found."

    mass_arr = np.array([m for _, m in valid]) * PHI
    dims = np.arange(2048, dtype=np.float64)
    scale = np.power(PHI, -dims / 2048) * np.cos(dims * GIZA_RAD)

    coord_norms = [float(np.linalg.norm(m_val * scale)) for m_val in mass_arr]

    out = f"### Sequence Analysis: `{sequence}`\n\n"
    stats = f"**Length:** {len(sequence)} residues | **Valid:** {len(valid)}"
    out += f"{stats} | **Unknown:** {len(unknown) if unknown else 0}\n\n"

    out += "| # | Residue | Mass (Da) | 2048D Lattice ‖L‖ | TUPT Gate |\n"
    out += "|:--|:--------|----------:|------------------:|:---------:|\n"
    for i, ((aa, mass), cnorm) in enumerate(zip(valid[:25], coord_norms[:25], strict=False)):
        gated = tupt_gate(mass)
        gate_sym = "🔴 EXC" if gated == 0 else "🟢 OK"
        out += f"| {i + 1} | **{aa}** | `{mass:.2f}` | `{cnorm:.4f}` | {gate_sym} |\n"

    total_norm = float(np.linalg.norm(coord_norms))
    excluded_count = sum(1 for _, m in valid if tupt_gate(m) == 0)
    out += f"\n**Total Lattice Energy (‖L‖):** `{total_norm:.6f}`  \n"
    out += f"**TUPT-Excluded Residues:** `{excluded_count}` / {len(valid)} "
    out += f"(`{excluded_count / len(valid) * 100:.1f}%`)\n"

    return out


# ─────────────────────────── Tab 3: AI Enhancement Browser ─────────────────────
ENHANCEMENTS = [
    ("PhiInfinityShardFolding", "Attention", "φ^∞ fractal shard folding"),
    ("NRCProteinFoldingEngine", "Scaffold", "2048D lattice + TUPT exclusion"),
    ("GoldenAttractorFlowNorm", "LayerNorm", "φ-attractor normalization"),
    ("TripleThetaInitializer", "Weight Init", "3θ resonance seed"),
    ("ResonanceShardKVCache", "KV-Cache", "φ^n memory sharding"),
    ("BiologicalExclusionGradientRouter", "Grad Routing", "TUPT mod-9 gate"),
    ("HodgePhiTTorsionAttention", "Self-Attention", "Hodge torsion biasing"),
    ("E8GoldenBasisEmbedding", "Embedding", "E8 root basis + φ"),
    ("PhiInfinityLosslessLoRA", "LoRA", "φ^∞ lossless adapter"),
    ("NavierStokesDampingRegularizer", "Regularizer", "NS fractional damping"),
    ("PrimeDensityConditionedGeneration", "Sampling", "Prime density seeds"),
    ("GTTEntropyCollapseRegularizer", "Entropy Loss", "GTT threshold collapse"),
    ("PhiInverseMomentumAccelerator", "Momentum", "φ⁻¹ velocity scaling"),
    ("TUPTAttractorSyncSeed", "RNG Seed", "TUPT cycle sync"),
    ("QRTKernelConvolution", "Conv1D/2D", "QRT wave kernel"),
    ("LucasWeightedSparseAttention", "Sparse Attn", "Lucas number masking"),
    ("PhiPoweredResonantWeighting", "Weight Init", "φ^n spectral decay"),
    ("GizaLatticeIsomorphism", "Projection", "51.85° slope map"),
    ("MSTLyapunovGradientClipping", "Grad Clipping", "MST λ≈0.381 bound"),
    ("PisanoModulatedLRSchedule", "LR Schedule", "Pisano period cycle"),
    ("LucasPellHybridWeightDecay", "Weight Decay", "Lucas-Pell recursion"),
    ("TUPTExclusionTokenPruning", "Token Pruning", "Mod-9 pruning gate"),
    ("PhiVoidResonancePositionalEncoding", "Positional Enc.", "φ-void sinusoidal PE"),
    ("InfiniteEInfinityContextUnfolder", "Context Window", "E∞ recursive unfolding"),
    ("TUPTModularDropout", "Dropout", "TUPT-gated structural drop"),
    ("QRTTurbulenceOptimizer", "Optimizer", "QRT turbulence gradient"),
    ("GizaSlopeAttentionBias", "Attention Bias", "51.85° Giza weighting"),
    ("FloorSinhActivation", "Activation", "floor(1000·sinh(x)) + φ·x"),
    ("GoldenSpiralRotaryEmbedding", "RoPE", "φ-spiral rotation matrix"),
    ("NRCEntropyAttractorEarlyStopping", "Early Stopping", "NRC entropy convergence"),
]


def browse_enhancement(name: str) -> str:
    """Retrieves technical specifications for an NRC enhancement."""
    match = next((e for e in ENHANCEMENTS if e[0] == name), None)
    if not match:
        return "_Enhancement not found._"

    cls, replaces, desc = match
    code = f"""```python
import torch, torch.nn as nn
from nrc_ai import {cls}

# Example: wrapping a standard layer
layer = nn.Linear(512, 512)
enhancement = {cls}()

# Forward pass with NRC physics
x = torch.randn(8, 64, 512)
out = enhancement(x)
print(f"Output shape: {{out.shape}}")
```"""

    return f"### `{cls}`\n\n**Replaces:** `{replaces}`\n**Description:** {desc}\n\n{code}"


# ─────────────────────────── Build Gradio App ──────────────────────────────────
THEME = gr.themes.Soft(
    primary_hue="violet",
    secondary_hue="indigo",
    neutral_hue="slate",
    font=[gr.themes.GoogleFont("Inter"), "sans-serif"],
)

with gr.Blocks(title="NRC Interactive — Nexus Resonance Codex", theme=THEME) as demo:
    gr.Markdown("""
# 🌀 Nexus Resonance Codex — Interactive Explorer
*Real-time computation of NRC mathematics, protein lattice projections, and AI enhancement browser.*

[![GitHub](https://img.shields.io/badge/GitHub-Nexus--Resonance--Codex-181717?logo=github)](https://github.com/Nexus-Resonance-Codex)
""")

    with gr.Tabs():
        # ── Tab 1 ──────────────────────────────────────────────────────────────
        with gr.Tab("🔢 NRC Math Explorer"):
            gr.Markdown(
                "Enter any real number to see all NRC mathematical operations applied in real time."
            )
            with gr.Row():
                with gr.Column(scale=1):
                    x_input = gr.Slider(-10, 10, value=1.618, step=0.001, label="Input x")
                    n_input = gr.Slider(1, 30, value=10, step=1, label="Fibonacci index n")
                    math_btn = gr.Button("⚡ Compute", variant="primary")
                with gr.Column(scale=2):
                    math_out = gr.Markdown()
            math_btn.click(explore_nrc_math, inputs=[x_input, n_input], outputs=[math_out])

        # ── Tab 2 ──────────────────────────────────────────────────────────────
        with gr.Tab("🧬 Protein Sequence → Lattice"):
            gr.Markdown(
                "Enter an amino acid sequence (1-letter FASTA codes) to project it "
                "into the 2048D φ-lattice."
            )
            with gr.Row():
                with gr.Column(scale=1):
                    seq_input = gr.Textbox(
                        label="Amino Acid Sequence",
                        placeholder="e.g. MKTIIALSYIFCLVFAQC",
                        value="MKTIIALSYIFCLVFAQC",
                        lines=3,
                    )
                    seq_btn = gr.Button("🔬 Analyze", variant="primary")
                with gr.Column(scale=2):
                    seq_out = gr.Markdown()
            seq_btn.click(project_sequence, inputs=seq_input, outputs=seq_out)

        # ── Tab 3 ──────────────────────────────────────────────────────────────
        with gr.Tab("🤖 AI Enhancement Browser"):
            gr.Markdown(
                "Browse all 30 NRC AI Enhancement modules with descriptions, formulas, "
                "and PyTorch examples."
            )
            with gr.Row():
                with gr.Column(scale=1):
                    enh_dropdown = gr.Dropdown(
                        choices=[e[0] for e in ENHANCEMENTS],
                        value=ENHANCEMENTS[0][0],
                        label="Select Enhancement",
                    )
                with gr.Column(scale=2):
                    enh_out = gr.Markdown()
            enh_dropdown.change(browse_enhancement, inputs=enh_dropdown, outputs=enh_out)

    gr.Markdown("""
---
*Built with the NRC Python Libraries — open source, mathematically rigorous, φ-grounded.*
""")

if __name__ == "__main__":
    demo.launch(share=False)
