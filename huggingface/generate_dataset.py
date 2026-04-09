#!/usr/bin/env python3
"""Nexus Resonance Codex - HuggingFace Dataset Generator.

Institutional-grade script to generate the synthetic NRC mathematical manifold
dataset for AI training and resonance exploration.
"""

import math
from typing import Any, Dict, List

import numpy as np
import pandas as pd


def binet_formula_gen(n: float) -> float:
    """Calculates n-th Fibonacci value via continuous Binet projection."""
    phi = (1 + 5**0.5) / 2
    return float((phi**n - (-phi) ** (-n)) / (5**0.5))


def qrt_eternal_wave_gen(x: float) -> float:
    """Computes the QRT eternal wave for a given scalar input."""
    phi = (1 + 5**0.5) / 2
    giza_deg = 51.85
    return float(
        math.sin(phi * math.sqrt(2) * giza_deg * x) * math.exp(-(x**2) / phi)
        + math.cos(math.pi / phi * x)
    )


def mst_map_step_gen(x: float) -> float:
    """Calculates a single step of the Modular Synchronisation map."""
    phi = (1 + 5**0.5) / 2
    xp = abs(x) + 1e-9
    val = (
        math.floor(1000.0 * math.sinh(min(xp, 20.0)))
        + math.log(xp**2 + 1.0)
        + (phi ** min(xp, 20.0))
    )
    return float(val % 24389)


def generate_row(x: float, index: int) -> Dict[str, Any]:
    """Generates a single multi-primitive dataset row from a scalar x."""
    return {
        "index": index,
        "input_x": x,
        "binet": binet_formula_gen(x % 20),
        "qrt": qrt_eternal_wave_gen(x),
        "mst": mst_map_step_gen(x),
        "phi_projection": float((1 + 5**0.5) / 2 * x),
    }


def generate_nrc_dataset(
    n_uniform: int = 1000,
    n_gaussian: int = 1000,
    n_fibonacci: int = 500,
) -> List[Dict[str, Any]]:
    """Generates an institutional-grade row battery for NRC resonance training."""
    n_rows = n_uniform + n_gaussian + n_fibonacci
    print(f"Generating {n_rows} NRC rows...")

    rng = np.random.default_rng(seed=42)

    xs_uniform = rng.uniform(-10.0, 10.0, size=n_uniform)
    xs_gaussian = rng.normal(0.0, 2.0, size=n_gaussian)
    xs_fib = [binet_formula_gen(i % 20) * rng.uniform(0.1, 1.0) for i in range(n_fibonacci)]

    all_xs = list(xs_uniform) + list(xs_gaussian) + xs_fib
    indices = list(range(1, n_rows + 1))

    rows: List[Dict[str, Any]] = []
    for i, x in enumerate(all_xs):
        try:
            row = generate_row(float(x), indices[i])
            rows.append(row)
        except Exception:
            continue

    return rows


def save_parquet(rows: List[Dict[str, Any]], path: str) -> None:
    """Saves the generated NRC row list as a high-density Parquet dataset."""
    try:
        df = pd.DataFrame(rows)
        df.to_parquet(path, index=False, compression="gzip")
        print(f"  Saved {len(df)} rows → {path}")
    except Exception as e:
        print(f"  Failed to save Parquet: {e}")


if __name__ == "__main__":
    dataset_rows = generate_nrc_dataset()
    save_parquet(dataset_rows, "nrc_training_corpus.parquet")
    print("Dataset generation complete.")
