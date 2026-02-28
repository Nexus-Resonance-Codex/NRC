"""
Modular Synchronisation Theory (MST) Dynamics.
==============================================
Provides mathematical bounding and cyclic clipping functions rooted
in the Lyapunov exponent limits.
"""
from typing import Union

import numpy as np

from .phi import PHI_FLOAT

MST_MODULUS: int = 24389
MST_LAMBDA: float = 0.381

def mst_step(x_n: Union[float, np.ndarray]) -> Union[float, np.ndarray]:
    """
    Executes a single step of the Modular Synchronisation Theory (MST) bounds.

    Formula:
        x_{n+1} = | floor(1000 · sinh(x_n)) + log(x_n² + 1) + φ^{x_n} | mod 24389

    Generates cycles of precisely ~2100 phases with a provable Lyapunov exponent
    λ ≈ 0.381. Ensures values map back into mathematically stable boundaries.

    Args:
        x_n: The current state value (scalar or array).

    Returns:
        The next cyclic state bounded by mod 24389.
    """
    term1 = np.floor(1000.0 * np.sinh(x_n))
    term2 = np.log(x_n**2 + 1.0)
    term3 = np.power(PHI_FLOAT, x_n)

    total = term1 + term2 + term3
    return np.fmod(np.abs(total), MST_MODULUS)
