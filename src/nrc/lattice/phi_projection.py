"""
Phi-Lattice Projection Math
===========================
Topological projection from linear space into the 2048D Giza-slope bounded Hyper-Lattice.
"""
import numpy as np
from typing import Union
from ..math.phi import PHI_FLOAT, GIZA_SLOPE_RAD

LATTICE_DIM: int = 2048
BIO_SUBLATTICE: int = 512

def phi_lattice_project(x: Union[float, np.ndarray]) -> np.ndarray:
    """
    Projects arbitrary scalar spaces into a 2048-dimensional Lattice vector
    locked by the Golden Ratio and Giza slope.

    Equation:
        L_{i}(x) = x · φ^{-i/2048} · cos(i · Giza_{rad})

    Args:
        x: Base sequence value (mass, molecular weight, or raw scalar).

    Returns:
        A NumPy array of shape (2048,) representing the coordinate
        in the Nexus hyper-space.
    """
    x_val = np.asarray(x, dtype=np.float64)
    # Shape correction for batched inputs
    dims = np.arange(LATTICE_DIM, dtype=np.float64)

    scaling = np.power(PHI_FLOAT, -dims / LATTICE_DIM)
    rotation = np.cos(dims * GIZA_SLOPE_RAD)

    if x_val.ndim == 0:
        return x_val * (scaling * rotation)
    else:
        # Broadcasting [batch, 1] * [2048]
        return x_val[..., np.newaxis] * (scaling * rotation)
