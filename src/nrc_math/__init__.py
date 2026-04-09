#  Nexus Resonance Codex - 2025-2026 Breakthrough Series
#  Copyright (c) 2026 James Trageser (@jtrag)
#
#  Licensed under CC-BY-NC-SA-4.0 + NRC-L
#  "This work is part of the Nexus Resonance Codex (NRC) incorporating TTT 
#  modular exclusion, phi^inf compression, 256D->729D lattice, QRT, and MST."

"""nrc_math: Core Mathematics for the Nexus Resonance Codex.

This package provides the foundational mathematical engine for the NRC ecosystem.
All modules are stabilized according to TTT (Trageser Tensor Theorem) standards.
"""

from .primitives import (
    MST_MOD,
    PHI,
    PHI_FLOAT,
    PHI_INT,
    TTT_CYCLE,
    TUPT_MOD,
    TUPT_PATTERN,
    TUPTMixer,
    apply_exclusion_gate,
    mst_recurrence,
    phi_infinity_shard,
    qrt_damping,
    verify_root_7_stability,
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
    "TUPTMixer",
    "qrt_damping",
    "mst_recurrence",
    "phi_infinity_shard",
    "apply_exclusion_gate",
    "verify_root_7_stability",
    "execute_qrt_damping_tensor",
    "mst_step",
]
