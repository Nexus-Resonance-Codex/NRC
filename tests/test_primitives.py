"""Tests for NRC Math Vault primitives."""

import numpy as np

from nrc_math import (
    MST_MOD,
    PHI,
    PHI_INT,
    TTT_CYCLE,
    TUPT_MOD,
    mst_recurrence,
    phi_infinity_shard,
    qrt_damping,
    tupt_mix,
)


def test_constants() -> None:
    """Verify core math constants."""
    assert PHI > 1.61
    assert PHI_INT == 1618
    assert len(TTT_CYCLE) == 4
    assert PHI_INT < TUPT_MOD


def test_tupt_mix() -> None:
    """Verify TUPT mixing rounds."""
    val = tupt_mix(100, 0)
    assert isinstance(val, int)
    assert 0 <= val < TUPT_MOD

    # Check cycle logic
    val2 = tupt_mix(100, 4)  # Should match step 0
    assert val2 == val


def test_qrt_damping() -> None:
    """Verify QRT damping behavior."""
    # Scalar check
    out = qrt_damping(1.0)
    assert isinstance(out, float)

    # Array check
    x = np.linspace(-1, 1, 10)
    out_arr = qrt_damping(x)
    assert len(out_arr) == 10
    assert isinstance(out_arr, np.ndarray)


def test_mst_recurrence() -> None:
    """Verify MST recurrence stability."""
    val = mst_recurrence(1.0)
    assert isinstance(val, int)
    assert 0 <= val < MST_MOD

    # Check determinism
    assert mst_recurrence(1.0) == val


def test_mst_overflow() -> None:
    """Verify MST recurrence handling for large inputs."""
    # math.sinh(1000) will overflow
    val = mst_recurrence(1000.0)
    assert isinstance(val, int)
    assert 0 <= val < MST_MOD


def test_phi_infinity_shard() -> None:
    """Verify φ^∞ shard generation."""
    x = np.array([1.0, 2.0, 3.0])
    shard = phi_infinity_shard(x, 0)
    # At k=0: s_0 = x * φ^0 + roll(x,0) * φ^0 = x + x = 2x
    np.testing.assert_allclose(shard, 2 * x)

    shard_k1 = phi_infinity_shard(x, 1)
    assert shard_k1.shape == (3,)


def test_metadata() -> None:
    """Verify package metadata."""
    from nrc_math import __about__

    assert __about__.__version__ == "1.0.0"
    assert __about__.__author__ == "James Trageser"
