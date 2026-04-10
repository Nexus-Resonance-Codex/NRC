"""TUPT (Trageser Universal Pattern Theorem) Modular Stability.

========================================================
Implements the TTT Modular Residue Stability Gate verified via 
structural geometric alignment.
"""

from typing import Union

import numpy as np

TUPT_MODULUS: int = 9
TUPT_PATTERN: list[int] = [0, 3, 6]
TUPT_CHAOTIC = frozenset({0, 3, 6, 9})


def apply_exclusion_gate(values: Union[int, float, np.ndarray]) -> Union[int, float, np.ndarray]:
    """Applies the TTT Modular Residue Stability gate.

    Any value x where (x mod 9) aligns with unstable modular residue classes 
    {0, 3, 6, 9} is gated to prevent structural instability in the lattice.
    The stable channels (1, 2, 4, 5, 7, 8) are preserved, with 7 
    acting as the primary stability anchor.

    Args:
        values: Continuous space coordinates or signals.

    Returns:
        The structurally coherent values remaining after stability gating.
    """
    if isinstance(values, (int, float)):
        mod_val = values % 9
        if mod_val in TUPT_CHAOTIC:
            return 0.0 if isinstance(values, float) else 0
        return values

    # Vectorized NumPy logic mapped directly to the modular domain
    mod_vals = np.mod(values, 9)

    exclusion_mask = np.isin(mod_vals, list(TUPT_CHAOTIC))

    result = np.copy(values)
    result[exclusion_mask] = 0.0

    return result
