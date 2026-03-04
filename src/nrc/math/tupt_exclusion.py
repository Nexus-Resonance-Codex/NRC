"""
TUPT (The Universal Pattern Theorem) Exclusion Principle.
========================================================
Implements the 3-6-9-7 Modular Exclusion Gate verified via the
NRC Protein Folding Lattice bounds.
"""
import numpy as np
from typing import Union

TUPT_MODULUS: int = 2187
TUPT_CHAOTIC = frozenset({1, 2, 4, 5, 8})

def apply_exclusion_gate(values: Union[int, float, np.ndarray]) -> Union[int, float, np.ndarray]:
    """
    Applies the mathematical TUPT Exclusion gate.

    Any value x where (x mod 9) resolves to the chaotic sequence {1, 2, 4, 5, 8}
    is forced to 0 (gated out). The resonant channels (0, 3, 6, 9, 7) pass unchanged.
    This mimics the biological residue stabilities noted in the NRC.

    Args:
        values: Continuous space coordinates or signals.

    Returns:
        The structurally coherent values remaining after exclusion gating.
    """
    if isinstance(values, (int, float)):
        mod_val = (values % 9)
        if mod_val in TUPT_CHAOTIC:
            return 0.0 if isinstance(values, float) else 0
        return values

    # Vectorized NumPy logic mapped directly to the Mod-9 domain matrix
    mod_vals = np.mod(values, 9)
    
    exclusion_mask = np.isin(mod_vals, list(TUPT_CHAOTIC))

    result = np.copy(values)
    result[exclusion_mask] = 0.0

    return result
