"""
Quantum Resonance Theory (QRT) Damping Functions.
=================================================
Fractal waveform math to resolve unstable gradients via smooth friction
instead of stochastic dropout.
"""
import math
import numpy as np
from typing import Union
from .phi import PHI_FLOAT, GIZA_SLOPE_DEG

SQRT_2 = math.sqrt(2.0)
PI = math.pi

def qrt_damping(x: Union[float, np.ndarray]) -> Union[float, np.ndarray]:
    """
    Determines the QRT wave topology at arbitrary spacial point x.

    QRT(x) = sin(φ · √2 · 51.85 · x) · exp(-x² / φ) + cos(π/φ · x)

    This equation forces extreme outliers exponentially downwards towards 0,
    while gently oscillating stable regions using the Giza slope amplitude.

    Args:
        x: Input scalar or numpy array (activations, gradients, physical wave point).

    Returns:
        The damped output bounding safely within the QRT fractal topology.
    """
    freq_sin = PHI_FLOAT * SQRT_2 * GIZA_SLOPE_DEG
    freq_cos = PI / PHI_FLOAT

    term1 = np.sin(freq_sin * x)
    term2 = np.exp(-(x**2) / PHI_FLOAT)
    term3 = np.cos(freq_cos * x)

    return (term1 * term2) + term3
