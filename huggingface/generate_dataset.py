#!/usr/bin/env python3
"""
NRC Synthetic Training Dataset Generator
=========================================
Generates a richly-structured Parquet dataset capturing the exact outputs
of every NRC mathematical operation. Suitable for uploading to the
HuggingFace Datasets Hub or use as a local benchmark.

Usage:
    python generate_dataset.py --rows 50000 --output nrc_dataset.parquet
    python generate_dataset.py --rows 10000 --output nrc_dataset.jsonl --format jsonl

Upload to HuggingFace Hub (after dataset is generated):
    python push_dataset_to_hub.py --dataset nrc_dataset.parquet
"""

import argparse
import math
import sys
import numpy as np

# Attempt to import from the installed nrc package; fall back to inline math
# so this script can also be run in clean environments (e.g. HF Spaces)
try:
    from nrc.math.phi import PHI_FLOAT, binet_formula, phi_infinity_fold
    from nrc.math.qrt import qrt_damping
    from nrc.math.mst import mst_step
    from nrc.math.tupt_exclusion import apply_exclusion_gate
    from nrc.lattice.phi_projection import phi_lattice_project
    _NRC_AVAILABLE = True
except ImportError:
    _NRC_AVAILABLE = False
    print("[warn] nrc library not found — using inline math definitions.")
    PHI_FLOAT = (1.0 + math.sqrt(5.0)) / 2.0
    _SQRT5 = math.sqrt(5.0)
    _SQRT2 = math.sqrt(2.0)
    _PI = math.pi
    _GIZA_DEG = 51.853
    _GIZA_RAD = _GIZA_DEG * (_PI / 180.0)

    def binet_formula(n: int) -> float:
        return (PHI_FLOAT**n - (-PHI_FLOAT)**(-n)) / _SQRT5

    def phi_infinity_fold(x: float, iterations: int = 5) -> float:
        for n in range(1, iterations + 1):
            x = (PHI_FLOAT**n) * x + (1.0 / _SQRT5)
        return x

    def qrt_damping(x: float) -> float:
        freq_sin = PHI_FLOAT * _SQRT2 * _GIZA_DEG
        freq_cos = _PI / PHI_FLOAT
        return math.sin(freq_sin * x) * math.exp(-(x**2) / PHI_FLOAT) + math.cos(freq_cos * x)

    def mst_step(x: float) -> float:
        total = math.floor(1000.0 * math.sinh(x)) + math.log(x**2 + 1.0) + (PHI_FLOAT**x)
        return abs(total) % 24389

    def apply_exclusion_gate(x: float) -> float:
        mod_val = x % 2187
        if any(mod_val % p == 0 for p in [3, 6, 7, 9] if p != 0):
            return 0.0
        return x

    def phi_lattice_project(x: float) -> np.ndarray:
        dims = np.arange(2048, dtype=np.float64)
        return x * np.power(PHI_FLOAT, -dims / 2048) * np.cos(dims * _GIZA_RAD)


def classify_point(x: float, qrt_val: float, tupt_gated: float) -> str:
    """Label a data point based on NRC stability criteria."""
    if tupt_gated == 0.0:
        return "excluded"
    if abs(qrt_val) < 0.5 and abs(x) < 3.0:
        return "resonant"
    return "stable"


def generate_row(x: float, n: int) -> dict:
    """Generate a single dataset row from a scalar input x and Fibonacci index n."""
    # Core math outputs
    if _NRC_AVAILABLE:
        qrt_val = float(qrt_damping(np.array([x]))[0])
        mst_val = float(mst_step(np.array([abs(x) + 1e-8]))[0])
        tupt_val = float(apply_exclusion_gate(np.array([x]))[0])
        phi_fold = float(phi_infinity_fold(np.array([x]))[0])
        lattice = phi_lattice_project(np.array([x]))
        lattice_norm = float(np.linalg.norm(lattice))
    else:
        qrt_val = qrt_damping(x)
        mst_val = mst_step(abs(x) + 1e-8)
        tupt_val = apply_exclusion_gate(x)
        phi_fold = phi_infinity_fold(x)
        lattice = phi_lattice_project(x)
        lattice_norm = float(np.linalg.norm(lattice))

    binet_val = binet_formula(n) if _NRC_AVAILABLE else binet_formula(n)

    return {
        "input_x":      round(x, 8),
        "phi_fold":     round(phi_fold, 8),
        "qrt_wave":     round(qrt_val, 8),
        "mst_state":    round(mst_val, 8),
        "tupt_gated":   round(tupt_val, 8),
        "binet_n":      n,
        "binet_val":    round(float(binet_val), 8),
        "lattice_norm": round(lattice_norm, 8),
        "phi_const":    round(PHI_FLOAT, 15),
        "label":        classify_point(x, qrt_val, tupt_val),
    }


def generate_dataset(n_rows: int, seed: int = 42) -> list:
    """Generate n_rows of NRC-labeled data points."""
    rng = np.random.default_rng(seed)

    # Draw inputs from several distributions to cover diverse behaviors
    n_uniform   = n_rows // 3
    n_gaussian  = n_rows // 3
    n_fibonacci = n_rows - n_uniform - n_gaussian

    xs_uniform  = rng.uniform(-10.0, 10.0, size=n_uniform)
    xs_gaussian = rng.normal(0.0, 2.0, size=n_gaussian)
    # Fibonacci-scaled inputs
    xs_fib = [binet_formula(i % 20) * rng.uniform(0.1, 1.0)
              for i in range(n_fibonacci)]

    all_xs = list(xs_uniform) + list(xs_gaussian) + xs_fib
    indices = list(range(1, n_rows + 1))

    rows = []
    for i, x in enumerate(all_xs):
        try:
            row = generate_row(float(x), indices[i % 30])
            rows.append(row)
        except (OverflowError, ValueError, ZeroDivisionError):
            # Skip numerically degenerate points
            continue

    print(f"  Generated {len(rows)} valid rows ({n_rows - len(rows)} skipped as degenerate)")
    return rows


def save_parquet(rows: list, path: str) -> None:
    try:
        import pandas as pd
        df = pd.DataFrame(rows)
        df.to_parquet(path, index=False, compression="gzip")
        print(f"  Saved {len(df)} rows → {path}")
        print(f"  Columns: {list(df.columns)}")
        label_counts = df["label"].value_counts().to_dict()
        print(f"  Label distribution: {label_counts}")
    except ImportError:
        print("[error] pandas not installed. Run: pip install pandas pyarrow")
        sys.exit(1)


def save_jsonl(rows: list, path: str) -> None:
    import json
    with open(path, "w") as f:
        for row in rows:
            f.write(json.dumps(row) + "\n")
    print(f"  Saved {len(rows)} rows → {path}")


def main():
    parser = argparse.ArgumentParser(description="Generate NRC synthetic training dataset")
    parser.add_argument("--rows", type=int, default=50_000, help="Number of data rows (default: 50000)")
    parser.add_argument("--output", type=str, default="nrc_dataset.parquet", help="Output file path")
    parser.add_argument("--format", choices=["parquet", "jsonl"], default="parquet")
    parser.add_argument("--seed", type=int, default=42, help="RNG seed for reproducibility")
    args = parser.parse_args()

    print(f"\n{'='*60}")
    print(f"  NRC Synthetic Dataset Generator")
    print(f"  Rows: {args.rows:,}  |  Format: {args.format}  |  Seed: {args.seed}")
    print(f"{'='*60}\n")

    print("[1/2] Generating data points ...")
    rows = generate_dataset(args.rows, seed=args.seed)

    print("[2/2] Saving dataset ...")
    if args.format == "parquet":
        save_parquet(rows, args.output)
    else:
        save_jsonl(rows, args.output)

    print(f"\n✓ Done! Dataset ready at: {args.output}")
    print("  Upload to HuggingFace Hub with:")
    print("    python push_dataset_to_hub.py")


if __name__ == "__main__":
    main()
