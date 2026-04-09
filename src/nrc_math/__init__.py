"""nrc_math: Modular Institutional-Grade Core Mathematics.

This package provides the foundational mathematical engine for the Nexus Resonance Codex.
All modules are stabilized according to TTT (Trageser Tensor Theorem) standards.
"""

from .primitives import (
    PHI,
    PHI_FLOAT,
    PHI_INT,
    TTT_CYCLE,
    MST_MOD,
    TUPT_MOD,
    TUPT_PATTERN,
    apply_exclusion_gate,
    mst_recurrence,
    phi_infinity_shard,
    qrt_damping,
    tupt_mix,
)

# Convenience aliases matching legacy structure for easier transition
mst_step = mst_recurrence
execute_qrt_damping_tensor = qrt_damping

__all__ = [
    "PHI",
    "PHI_FLOAT",
    "PHI_INT",
    "TTT_CYCLE",
    "MST_MOD",
    "TUPT_MOD",
    "TUPT_PATTERN",
    "tupt_mix",
    "qrt_damping",
    "mst_recurrence",
    "phi_infinity_shard",
    "apply_exclusion_gate",
    "execute_qrt_damping_tensor",
    "mst_step",
]
