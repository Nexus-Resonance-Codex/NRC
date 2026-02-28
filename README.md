<div align="center">
  <img src="https://img.shields.io/badge/Nexus_Resonance_Codex-v1.0.0-indigo?style=for-the-badge&logo=math" alt="NRC Logo"/>
  <h1>🌌 Nexus Resonance Codex (NRC)</h1>
  <p><b>A Mathematical Framework of Golden-Ratio-Weighted Series, Modular Exclusion Patterns, Multi-Scale Transforms, and High-Dimensional Lattice Projections</b></p>

<a href="https://github.com/Nexus-Resonance-Codex/NRC/actions"><img src="https://img.shields.io/badge/Build-Passing-brightgreen?style=flat-square&logo=githubactions" alt="Build Status"></a>
<a href="https://github.com/Nexus-Resonance-Codex/NRC/releases"><img src="https://img.shields.io/github/v/release/Nexus-Resonance-Codex/NRC?style=flat-square&color=blue&logo=github" alt="Release"></a>
<a href="https://github.com/Nexus-Resonance-Codex/NRC/blob/main/LICENSE.md"><img src="https://img.shields.io/badge/License-NRC_L_v2.0-blue.svg?style=flat-square&logo=open-source-initiative" alt="License"></a>
<a href="https://Nexus-Resonance-Codex.github.io/NRC"><img src="https://img.shields.io/badge/Website-Live_on_Pages-orange?style=flat-square&logo=githubpages" alt="Website"></a>
<a href="https://huggingface.co/Nexus-Resonance-Codex"><img src="https://img.shields.io/badge/Hub-HuggingFace-yellow?style=flat-square&logo=huggingface" alt="HuggingFace"></a>

<hr></hr>
</div>

<br/>

## 🪐 Overview

The **Nexus Resonance Codex (NRC)** is the definitive repository housing the core mathematical framework authored by James Trageser.
At its heart, the Codex explores the deep relationships unifying **Number Theory, Analytic Number Theory, Modular Forms**, and **High-Dimensional Geometry**. It introduces a rigorous stabilization mechanism via the Golden Inverse Attractor ($\phi^{-1}$), driving the mathematical collapse and loss-less fractalization of continuous functions.

> _"The ultimate limit resides at $\phi^{-\infty} = 0$, leading to zero residual error, zero entropy deviation, and perfect structural collapse."_

<br/>

## 💠 Core Mathematical Engines

The `nrc` Python module exposes the exact formulations mapped in the Codex:

| Component                                    | Description                                                                              | Operator / Constant                                     |
| :------------------------------------------- | :--------------------------------------------------------------------------------------- | :------------------------------------------------------ |
| **Golden Inverse Attractor**                 | Universal convergence rate for stabilized resonant iterations.                           | $\phi^{-1} \approx 0.61803$                             |
| **MST (Multi-Scale Transform)**              | Dominant-QRT capped iterations bounding attractors.                                      | $\lfloor 1000 \sinh(\phi^{-n}x) \rfloor$                |
| **QRT (Quantum Resonance Damping)**          | Bounded sinusoidal waves oscillating at Giza-harmonic frequencies.                       | $\psi(x) = \sin(\phi\sqrt{2}\cdot 51.85x)e^{-x^2/\phi}$ |
| **TUPT (Trinary Universal Phase Transform)** | Modular exclusion logic acting as an LWE-hard security field over $\mathbb{Z}_{12289}$.  | $x \pmod{2187} \notin \{3,6,7,9\}$                      |
| **$\phi^\infty$ Topological Folding**        | Fractal compression algorithms pushing density structures precisely into $E8 \times 64$. | Folded Tensor Projection                                |

<br/>

## 🗂️ Ecosystem Repositories

The NRC is part of an interconnected ecosystem of advanced modeling and research:

- **[🟢 NRC (Core)](https://github.com/Nexus-Resonance-Codex/NRC)**: The main mathematical paper, LaTeX source, and core geometric Python package.
- **[🧬 Protein Folding](https://github.com/Nexus-Resonance-Codex/Protein-Folding)**: Practical applications of the NRC framework mapped into 2048D spatial biology for sequence simulation.
- **[🧠 AI Enhancements](https://github.com/Nexus-Resonance-Codex/Ai-Enhancements)**: 30 strict PyTorch drop-in modules built entirely on NRC scaling principles.

<br/>

## 🛠️ Installation & Cross-Platform Execution (Exhaustive Guide)

The core NRC mathematical engine is built for infinite-precision testing and interactive data visualization. Below are explicitly expanded, foolproof protocols across three dominant operating spheres (Linux, Windows, macOS).

**General Requirements:** 
- `python3` (Version 3.10+ recommended)
- `git`
- Access to terminal/command line

### ☁️ Remote Access (Google Colab)

For users lacking the physical compute capabilities required to run these interactive mathematical visualizations natively, Google Colab provides an immediate external environment executing in the cloud.

1. Navigate to **Google Colab** (https://colab.research.google.com).
2. At the top menu, select **File > Open Notebook**.
3. Select the **GitHub** tab.
4. Input the Repository URL: `https://github.com/Nexus-Resonance-Codex/NRC`
5. Click on the file **`interactive_nrc_explorer.ipynb`**.
6. When the notebook opens, you **must prepend** a unique install command to the first cell to load required math operators in Colab. Insert a new block at the beginning containing:
   ```python
   !pip install mpmath sympy matplotlib
   ```
7. Press `Shift + Enter` to sequentially run and evaluate each interactive mathematical module.

### 🐧 Linux (Pop!_OS / Ubuntu / Debian) - Primary Target

Linux is the premier, biologically analog environment allowing strict control over computational matrices and background physics required by the NRC.

1. **System Core Dependencies Update:**
   Open an interactive terminal session and execute sequentially:
   ```bash
   sudo apt update && sudo apt upgrade -y
   sudo apt install -y git python3-venv python3-pip python3-dev curl build-essential
   ```

2. **Install `uv` Configuration Wizard:**
   `uv` rapidly constructs virtual environments minimizing package overlap:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   # Reactivate session profiles
   source $HOME/.bashrc
   ```

3. **Clone & Mount Repository:**
   ```bash
   git clone https://github.com/Nexus-Resonance-Codex/NRC.git
   cd NRC
   ```

4. **Virtual Environment Isolation:**
   ```bash
   uv venv .venv
   source .venv/bin/activate
   ```

5. **Install The Engine In Editable Mode:**
   ```bash
   uv pip install -e .
   ```

6. **Deploy Interactive Notebook Server:**
   This environment grants you graphical mathematical outputs of the NRC framework:
   ```bash
   uv pip install jupyterlab
   # Execute locally
   jupyter lab interactive_nrc_explorer.ipynb
   ```
   *(A browser window will automatically launch displaying the geometric constants and scripts.)*

### 🪟 Windows 11 (via WSL2 / Ubuntu)

Avoid utilizing standalone PowerShell or Command Prompt, as path separation structures (backslash \) and C-libraries diverge from standard POSIX compliances, introducing mathematical anomalies. Instead, Windows users must project their processes into the Windows Subsystem for Linux (WSL).

1. **Enable Virtual Windows Subsystem (WSL2):**
   Execute from an elevated **Administrator** PowerShell window:
   ```powershell
   wsl --install
   ```
   Reboot your PC to finalize. When Windows returns, an Ubuntu terminal will pop up. Establish a UNIX user/pass (the password won't show visually while typing).

2. **Update Core OS Features within WSL2:**
   Inside the Ubuntu window run:
   ```bash
   sudo apt update && sudo apt upgrade -y
   sudo apt install -y git python3-venv python3-pip curl build-essential
   ```

3. **Secure the Mathematics Repository:**
   (Ensure you clone this directly into the native Linux filesystem path `~`, not `/mnt/c/`)
   ```bash
   git clone https://github.com/Nexus-Resonance-Codex/NRC.git
   cd NRC
   ```

4. **Create Protective Environment boundaries:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install --upgrade pip
   ```

5. **Install Core & Deploy Jupyter Interactive Server:**
   ```bash
   pip install -e .
   pip install jupyterlab
   # Deploy
   jupyter lab interactive_nrc_explorer.ipynb
   ```
   *(Select the Jupyter link provided in the terminal output, beginning with http://127.0.0.1..., and paste it into Chrome/Edge).*

### 🍏 macOS (Apple Silicon M1/M2/M3 & Intel)

Apple's UNIX underpinning allows the raw mathematical engine to run remarkably fast over its high-memory buses. 

1. **Deploy Homebrew Management Script:**
   Open Terminal and run:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
   *(Append to .zprofile if instructed by the Homebrew installation output).*

2. **Install Exact Python Architecture:**
   ```bash
   brew install python@3.11 git
   ```

3. **Clone Data Stream:**
   ```bash
   git clone https://github.com/Nexus-Resonance-Codex/NRC.git
   cd NRC
   ```

4. **Establish Venv:**
   ```bash
   python3.11 -m venv .venv
   source .venv/bin/activate
   pip install --upgrade pip
   ```

5. **Compile Engine and Run Scripts dynamically:**
   ```bash
   pip install -e .
   pip install jupyterlab
   
   # Deploy Interactive Lab
   jupyter lab interactive_nrc_explorer.ipynb
   ```
   *(Jupyter Lab will launch in Safari or your default browser automatically).*

<br/>

## 📄 Documentation & Assets

- **[Gradio Interactive Space](./gradio/)**: A local/live visualizer for generating QRT waves and mapping strings to the $\phi$-lattice.
- **Compiled PDF**: ArXiv & Vixra preprint (Pending publication).
- **HuggingFace Hub Datasets**: 50,000-row synthetic `parquet` dataset capturing NRC invariant mappings.

> 🔗 For a complete list of relevant external links and references, please see **[LINKS.md](./LINKS.md)**.

<br/>

## 🤝 Contributing & Contact

We welcome rigorous mathematical proofs, review, and structural improvements over the algorithmic implementations. The repository enforces deterministic formatting via `ruff`.

- **Website**: [Nexus-Resonance-Codex.github.io/NRC](https://Nexus-Resonance-Codex.github.io/NRC)
- **Contact**: Nexus-Resonance-Codex@gmail.com
