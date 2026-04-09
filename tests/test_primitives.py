#  Nexus Resonance Codex - 2025-2026 Breakthrough Series
#  Copyright (c) 2026 James Trageser (@jtrag)
#
#  Licensed under CC-BY-NC-SA-4.0 + NRC-L

"""Tests for NRC Math Vault primitives."""

import numpy as np
import pytest
from hypothesis import given, strategies as st
from nrc_math import __about__
from nrc_math.primitives import (
    MST_MOD,
    PHI,
    PHI_INT,
    TTT_CYCLE,
    TUPT_MOD,
    TUPTMixer,
    apply_exclusion_gate,
    mst_recurrence,
    phi_infinity_shard,
    qrt_damping,
    verify_root_7_stability,
)

def test_constants() -> None:
    """Verify core math constants."""
    assert PHI > 1.61
    assert PHI_INT == 1618
    assert len(TTT_CYCLE) == 4
    assert PHI_INT < TUPT_MOD

def test_tupt_mixer() -> None:
    """Verify stateful TUPT mixer logic."""
    mixer = TUPTMixer(seed=7)
    val1 = mixer.next_residue()
    assert 0 <= val1 < TUPT_MOD
    
    mixer2 = TUPTMixer(seed=7)
    assert mixer2.next_residue() == val1

def test_qrt_damping() -> None:
    """Verify QRT damping behavior."""
    out = qrt_damping(1.0)
    assert isinstance(out, float)

    x = np.linspace(-1, 1, 10)
    out_arr = qrt_damping(x)
    assert len(out_arr) == 10

@given(st.floats(min_value=-1000, max_value=1000, allow_nan=False, allow_infinity=False))
def test_mst_recurrence_range(x: float) -> None:
    """Property: MST recurrence must always stay within the modular field."""
    val = mst_recurrence(x)
    assert 0 <= val < MST_MOD

def test_mst_nominal_coverage() -> None:
    """Ensure nominal path of MST recurrence is covered."""
    # Small value to ensure no overflow and int conversion path
    val = mst_recurrence(1.0)
    assert isinstance(val, int)
    assert 0 <= val < MST_MOD

def test_phi_infinity_shard() -> None:
    """Verify φ^∞ shard generation."""
    x = np.array([1.0, 2.0, 3.0], dtype=np.float64)
    shard = phi_infinity_shard(x, 0)
    np.testing.assert_allclose(shard, 2 * x)

def test_exclusion_gate() -> None:
    """Verify TUPT Exclusion gate for Root-7 stabilization."""
    assert apply_exclusion_gate(9.0) == 0.0
    assert apply_exclusion_gate(7.0) == 7.0 
    
    arr = np.array([3, 7, 9, 16], dtype=np.float64)
    gated = apply_exclusion_gate(arr)
    expected = np.array([0, 7, 0, 16], dtype=np.float64)
    np.testing.assert_array_equal(gated, expected)

@given(st.integers(min_value=1, max_value=1000000))
def test_root_7_stability_property(x: int) -> None:
    """Property: Stability audit must correctly identify the Root-7 manifold."""
    d_root = x % 9
    if d_root == 0: d_root = 9
    is_stable = verify_root_7_stability(x)
    if d_root == 7:
        assert is_stable
    else:
        assert not is_stable

def test_metadata_coverage() -> None:
    """Audit metadata to ensure 100% coverage of __about__.py."""
    assert __about__.__version__ == "1.2.0"
    assert __about__.__author__ == "James Trageser"
    assert "nrc" in __about__.__package_name__

def test_exclusion_gate_torch() -> None:
    """Verify TUPT Exclusion gate for PyTorch tensors (Step 97 alignment)."""
    import torch
    # 0, 3, 6 mod 9 should be zeroed (including negative triggers)
    x = torch.tensor([0.0, 1.0, 3.0, 6.0, 7.0, 9.0, -3.0], dtype=torch.float32)
    gated = apply_exclusion_gate(x)
    
    assert torch.is_tensor(gated)
    assert gated[0] == 0.0
    assert gated[2] == 0.0
    assert gated[3] == 0.0
    assert gated[5] == 0.0
    assert abs(gated[6]) < 1e-6 # -3 mod 9 is 6, so should be 0.0
    assert gated[1] == 1.0
    assert gated[4] == 7.0

def test_qrt_damping_torch() -> None:
    """Verify QRT damping for PyTorch tensors."""
    import torch
    x = torch.linspace(-1, 1, 10, requires_grad=True)
    out = qrt_damping(x)
    assert torch.is_tensor(out)
    assert out.shape == x.shape
    assert out.requires_grad
