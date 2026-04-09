import subprocess

# Professional multi-line path configuration for E501 compliance
TEX_ROOT = "/home/jtrag/NRC/github-repos/Nexus-Resonance-Codex"
tex_dir = f"{TEX_ROOT}/Protein-Folding/docs/Nexus-Resonance-Codex-tex-files"

# Run pdflatex
subprocess.run(["pdflatex", "-interaction=nonstopmode", "main.tex"], cwd=tex_dir)
