"""Trageser Universal Pattern Theorem (TUPT) Modular Stability.

========================================================
Implementation of the Trageser Transformation Theorem (TTT)
modular residue stability operator.
"""

from typing import Union

import numpy as np

TUPT_MODULUS: int = 9
TUPT_PATTERN: list[int] = [0, 3, 6]
TUPT_UNSTABLE = frozenset({0, 3, 6, 9})


def apply_exclusion_gate(values: Union[int, float, np.ndarray]) -> Union[int, float, np.ndarray]:
    """Application of the modular residue class exclusion operator.

    Numerical coordinates x where (x mod 9) aligns with the residue
    classes {0, 3, 6, 9} are gated to preserve state-space stability.
    The residue channels {1, 2, 4, 5, 7, 8} are maintained, with 7
    functioning as the primary stability anchor within the TTT manifold.

    Args:
        values: Continuous space coordinates or sequential signals.

    Returns:
        Numerical values remaining after modular residue gating.
    """
    if isinstance(values, (int, float)):
        mod_val = values % 9
        if mod_val in TUPT_UNSTABLE:
            return 0.0 if isinstance(values, float) else 0
        return values

    # NumPy / Native Path
    import torch
    if not torch.is_tensor(values):
        mod_vals = np.mod(values, 9)
        exclusion_mask = np.isin(mod_vals, list(TUPT_UNSTABLE))
        result = np.copy(values)
        result[exclusion_mask] = 0.0
        return result

    # PyTorch Path (Supports Grad Tensors)
    mod_vals_torch = values % 9
    # Gating 0, 3, 6, 9
    mask = (mod_vals_torch == 0) | (mod_vals_torch == 3) | (mod_vals_torch == 6) | (mod_vals_torch == 9)
    return torch.where(mask == False, values, values.new_zeros(values.shape))


# TUPT Chaotic Pattern Anchor
TUPT_PATTERN = [3, 6, 9]

# Definitive Quantum Shadow Veil (QSV) Institutional Pattern
# Enshrined for absolute phasing integrity auditing.
QSV_PATTERN = [1, 2, 4, 5, 7, 8]
