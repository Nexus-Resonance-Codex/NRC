---
title: NRC Interactive — Nexus Resonance Codex
emoji: 🌀
colorFrom: violet
colorTo: indigo
sdk: gradio
sdk_version: "4.44.1"
app_file: app.py
pinned: true
license: other
short_description: Live NRC math explorer, protein lattice projections & AI enhancement browser
tags:
  - mathematics
  - golden-ratio
  - Protein-Folding
  - deep-learning
  - interactive
  - nrc
---

# NRC Interactive Space

This Space provides a live, interactive explorer for the mathematical and AI framework of the **Nexus Resonance Codex**.

## Features

- **NRC Math Explorer** — compute QRT, MST, TUPT, φ^∞ folding, and Binet's formula for any real number, with a live QRT wave plot
- **Protein Sequence → Lattice** — map any amino acid sequence into the 2048D Golden Ratio lattice and see per-residue stability
- **AI Enhancement Browser** — explore all 30 PyTorch enhancement modules with descriptions, formulas, and code examples

## Source Code

All source code is available in the [NRC GitHub Organization](https://github.com/Nexus-Resonance-Codex).

## 🚀 Running the Interactive Space Locally & Remote Analysis

This suite enables users to natively explore the NRC mathematical constructs through any Web Browser. Follow the explicit procedures corresponding to your OS environment, or use external instances like Google Colab.

### Remote Access (Google Colab / Cloud Notebooks)

If you lack requisite local memory (8GB minimum) or GPU capability, access the `interactive_nrc_explorer.ipynb` file from the cloud:
1. Open Google Colab (colab.research.google.com).
2. Go to **File > Open Notebook > GitHub Tab**.
3. Search for the URL `https://github.com/Nexus-Resonance-Codex/NRC`.
4. Open the `interactive_nrc_explorer.ipynb` file located in the root repository.
5. In the first executable block, prepend this library fetch command: `!pip install gradio mpmath matplotlib`.
6. Use Shift+Enter to run each cell interactively from any Operating System globally.

### 🐧 Linux (Pop!_OS / Ubuntu) - Primary

For native Linux environments, execution overhead is minimized giving mathematically precise speed.

```bash
# 1. Update APT Dependencies and Virtual Managers
sudo apt update && sudo apt install -y git python3-venv python3-pip

# 2. Clone the core repository and orient inward
git clone https://github.com/Nexus-Resonance-Codex/NRC.git
cd NRC/gradio

# 3. Securely separate your environment
python3 -m venv .venv
source .venv/bin/activate

# 4. Integrate required scientific algorithms
pip install --upgrade pip
pip install -r requirements.txt

# 5. Bring the Space Online
python3 app.py
```

### 🪟 Windows 11 (via WSL2 / Ubuntu)

Standalone CMD and PowerShell are discouraged due to directory and module discrepancy. Projection into the WSL environment is mandatory.

```powershell
# 1. Establish the WSL capability in an Administrator PowerShell Console
wsl --install
```
*Wait for installation, reboot your computer, then create a user account in the newly launched Ubuntu console.*

```bash
# 2. Inside the Ubuntu console: Install Linux utilities
sudo apt update && sudo apt install -y git python3-venv python3-pip

# 3. Mount repository directly to inner Linux filesystem (Do not use /mnt/c/)
git clone https://github.com/Nexus-Resonance-Codex/NRC.git
cd NRC/gradio

# 4. Initialize Sandbox and install mathematical libraries
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# 5. Launch Service locally
python3 app.py
```

### 🍏 macOS (M-Series Silicon & Intel)

Utilizing Python binaries from package managers like Homebrew guarantees library paths are preserved efficiently across macOS spaces.

```bash
# 1. Install standard tools via Homebrew (https://brew.sh if absent)
brew install python@3.11 git

# 2. Extract repository 
git clone https://github.com/Nexus-Resonance-Codex/NRC.git
cd NRC/gradio

# 3. Instantiate the Virtual System
python3.11 -m venv .venv
source .venv/bin/activate

# 4. Finalize Mathematics installations
pip install --upgrade pip
pip install -r requirements.txt

# 5. Execute 
python3.11 app.py
```

### Accessing the Web Interface

Upon executing `python3 app.py` (or Python equivalent on your OS), the server terminal will generate a `localhost` URL, typically:
> `http://127.0.0.1:7860/`

**Open this link inside Google Chrome, Safari, or Microsoft Edge** to interact with the Nexus Resonance Codex!

