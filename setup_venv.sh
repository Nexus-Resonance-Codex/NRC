#!/usr/bin/env bash
# ===========================================================
#  NRC Core Library — Virtual Environment Setup
# ===========================================================
#  Creates an isolated .venv, installs the `nrc` math
#  package in editable mode, and validates the install.
#
#  PREREQUISITE (one-time, Pop!_OS / Ubuntu / Debian):
#    sudo apt install python3.12-venv
#
#  USAGE:  ./setup_venv.sh
#          source .venv/bin/activate
#          python examples/zero_search.py
# ===========================================================

set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="${SCRIPT_DIR}/.venv"
RED='\033[0;31m'; GREEN='\033[0;32m'; CYAN='\033[0;36m'; NC='\033[0m'

echo -e "${CYAN}═══════════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}  NRC Core Library — Virtual Environment Setup${NC}"
echo -e "${CYAN}═══════════════════════════════════════════════════════════${NC}"

# ── Prerequisite check ─────────────────────────────────────
if ! python3 -m venv --help &>/dev/null; then
    echo -e "${RED}[!] python3-venv is not available on this system.${NC}"
    echo ""
    echo "    Run this first, then re-run ./setup_venv.sh:"
    echo ""
    echo "      Pop!_OS / Ubuntu / Debian:"
    echo "        sudo apt install python3.12-venv"
    echo "      Fedora:"
    echo "        sudo dnf install python3-venv"
    echo "      macOS (Homebrew):"
    echo "        brew install python@3.12"
    echo ""
    exit 1
fi

# ── Guard against re-creation ──────────────────────────────
if [ -d "${VENV_DIR}" ]; then
    echo -e "${RED}[!] .venv already exists. To recreate: rm -rf .venv${NC}"
    exit 1
fi

echo "[1/4] Creating virtual environment at .venv ..."
python3 -m venv "${VENV_DIR}"

echo "[2/4] Upgrading pip ..."
"${VENV_DIR}/bin/pip" install --upgrade pip --quiet

echo "[3/4] Installing nrc package (editable) + dev tools ..."
"${VENV_DIR}/bin/pip" install -e ".[dev]" --quiet

echo "[4/4] Verifying installation ..."
"${VENV_DIR}/bin/python" -c "
import nrc
from nrc.math.phi import PHI_FLOAT
from nrc.math.qrt import qrt_damping
from nrc.math.mst import mst_step
from nrc.math.tupt_exclusion import apply_exclusion_gate
import numpy as np

wave = qrt_damping(np.linspace(-1, 1, 10))
print(f'  nrc version : {nrc.__version__}')
print(f'  φ           : {PHI_FLOAT:.15f}')
print(f'  QRT(-1..1)  : {wave[:3]} ...')
print('  ✓ All imports OK!')
"

echo ""
echo -e "${GREEN}═══════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}  ✓ Setup complete!${NC}"
echo ""
echo "  Activate with:   source .venv/bin/activate"
echo "  Run tests:       pytest tests/ -v"
echo "  Deactivate:      deactivate"
echo -e "${GREEN}═══════════════════════════════════════════════════════════${NC}"
