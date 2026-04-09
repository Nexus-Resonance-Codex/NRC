"""NRC Mathematics Library.
=======================
The official Nexus Resonance Codex mathematics suite for Python.
Provides high-precision calculations for the Golden Ratio (φ), Binet's Formula,
the Quantum Resonance Theory (QRT) wave function, the Modular Synchronisation
Theory (MST) dynamics, and TUPT exclusion principles.
"""

from .__about__ import __version__
from .math.mst import MST_LAMBDA, MST_MODULUS, mst_step
from .math.phi import PHI_FLOAT, PHI_INVERSE_FLOAT, binet_formula
from .math.qrt import qrt_damping
from .math.tupt_exclusion import TUPT_MODULUS, TUPT_PATTERN, apply_exclusion_gate

__all__ = [
    "__version__",
    "PHI_FLOAT",
    "PHI_INVERSE_FLOAT",
    "binet_formula",
    "qrt_damping",
    "mst_step",
    "MST_MODULUS",
    "MST_LAMBDA",
    "apply_exclusion_gate",
    "TUPT_MODULUS",
    "TUPT_PATTERN",
]
