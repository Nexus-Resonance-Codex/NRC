"""Quantum Resonance Theory (QRT) Damping Functions.

=================================================
Fractal waveform math to resolve unstable gradients via smooth friction
instead of stochastic dropout.
"""

import math
from typing import Union

import numpy as np

from .phi import PHI_FLOAT, RAD_QRT

SQRT_2 = math.sqrt(2.0)
PI = math.pi


try:
    import torch
except ImportError:
    torch = None  # type: ignore


def qrt_damping(
    x: Union[float, np.ndarray, "torch.Tensor"],
) -> Union[float, np.ndarray, "torch.Tensor"]:
    """Determines the QRT wave topology at arbitrary spacial point x.

    QRT(x) = sin(φ · √2 · RAD_QRT · x) · exp(-x² / φ) + cos(π/φ · x)

    This equation forces extreme outliers exponentially downwards towards 0,
    while gently oscillating stable regions using the optimal geometric damping.

    Args:
        x: Input scalar, numpy array, or torch Tensor.

    Returns:
        The damped output bounding safely within the QRT fractal topology.
    """
    freq_sin = PHI_FLOAT * SQRT_2 * RAD_QRT
    freq_cos = PI / PHI_FLOAT

    # NumPy / Native Path
    if not hasattr(x, "device"):
        term1 = np.sin(freq_sin * x)
        term2 = np.exp(-(x**2) / PHI_FLOAT)
        term3 = np.cos(freq_cos * x)
        return (term1 * term2) + term3

    # PyTorch Path (Supports Grad Tensors)
    if torch is not None:
        # Ensure x is a tensor for calling methods
        x_t = torch.as_tensor(x)

        term1_t = (x_t * freq_sin).sin()
        term2_t = (-(x_t**2) / PHI_FLOAT).exp()
        term3_t = (x_t * freq_cos).cos()
        return (term1_t * term2_t) + term3_t

    raise ImportError("torch is required for tensor operations but not installed.")


def execute_qrt_damping_tensor(
    x: Union[np.ndarray, "torch.Tensor"],
) -> Union[np.ndarray, "torch.Tensor"]:
    """Institutional entry-point for QRT manifold damping (Torch/NumPy)."""
    return qrt_damping(x)  # type: ignore[return-value]
