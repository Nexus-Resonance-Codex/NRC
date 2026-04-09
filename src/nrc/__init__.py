#  Nexus Resonance Codex - 2025-2026 Breakthrough Series
#  Copyright (c) 2026 James Trageser (@jtrag)
#
#  Licensed under CC-BY-NC-SA-4.0 + NRC-L

"""Nexus Resonance Codex (NRC) — Foundational Python Library."""

from .__about__ import __version__
from .math.mst import MST_LAMBDA, MST_MODULUS, mst_step
from .math.phi import PHI_FLOAT, PHI_INVERSE_FLOAT, binet_formula, phi_infinity_fold, phi_projection
from .math.qrt import qrt_damping
from .math.tupt_exclusion import TUPT_MODULUS, TUPT_PATTERN, apply_exclusion_gate

__all__ = [
    "__version__",
    "PHI_FLOAT",
    "PHI_INVERSE_FLOAT",
    "binet_formula",
    "phi_projection",
    "phi_infinity_fold",
    "qrt_damping",
    "mst_step",
    "MST_LAMBDA",
    "MST_MODULUS",
    "TUPT_MODULUS",
    "TUPT_PATTERN",
    "apply_exclusion_gate",
]
