import subprocess

tex_dir = "/home/jtrag/NRC/github-repos/Nexus-Resonance-Codex/Protein-Folding/docs/Nexus-Resonance-Codex-tex-files"

# Run pdflatex
res = subprocess.run(
    ["pdflatex", "-interaction=nonstopmode", "NRC-Protein-Folding.tex"],
    cwd=tex_dir,
    capture_output=True,
    text=True,
)

if res.returncode == 0:
    print("Protein-Folding PDFLaTeX Compilation Successful!")
else:
    print("Protein-Folding PDFLaTeX Compilation FAILED")

# Extract simple error log
lines = res.stdout.split("\n")
for i, line in enumerate(lines):
    if line.startswith("!"):
        print("\n".join(lines[i : i + 6]))

# Output some details if we want
with open("latex_output.log", "w") as f:
    f.write(res.stdout)
