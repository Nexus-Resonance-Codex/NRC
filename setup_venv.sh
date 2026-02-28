#!/usr/bin/env bash
# =================================================================
#  NRC Core — Virtual Environment Setup Script
# =================================================================
#  Creates a local Python virtual environment for running NRC
#  example scripts (zero_search, variance_reduction, etc.)
#  without modifying your system Python.
#
#  USAGE:
#    chmod +x setup_venv.sh
#    ./setup_venv.sh
#
#  PREREQUISITES:
#    Pop!_OS / Ubuntu / Debian:  sudo apt install python3.12-venv
#    macOS: (included with Python from Homebrew or python.org)
#    Windows: (included with Python from python.org)
# =================================================================

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="${SCRIPT_DIR}/.venv"

echo "═══════════════════════════════════════════════════════════"
echo "  NRC Core — Virtual Environment Setup"
echo "═══════════════════════════════════════════════════════════"

if [ -d "${VENV_DIR}" ]; then
    echo "[!] .venv already exists. Delete it first: rm -rf .venv"
    exit 1
fi

echo "[1/3] Creating virtual environment..."
python3 -m venv "${VENV_DIR}"

echo "[2/3] Installing dependencies..."
source "${VENV_DIR}/bin/activate"
pip install --upgrade pip
pip install numpy mpmath sympy

echo "[3/3] Verifying..."
python -c "
import mpmath; mpmath.mp.dps = 50
phi = (mpmath.mpf(1) + mpmath.sqrt(5)) / 2
print(f'  φ = {phi}')
print('  All imports OK!')
"

echo ""
echo "  Activate with: source .venv/bin/activate"
echo "  Run examples:  python examples/zero_search.py"
echo "═══════════════════════════════════════════════════════════"
