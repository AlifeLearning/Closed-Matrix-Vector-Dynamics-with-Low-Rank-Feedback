# run_all_spd.py
from pathlib import Path
import subprocess
import sys

FIG_SCRIPTS = [
    "figures/fig02_traj.py",
    "figures/fig03_windows.py",
    "figures/fig04_stages.py",
    "figures/fig05_eigs.py",
    "figures/fig06_coeffs.py",
    "figures/fig07_geometry.py",
]

def main():
    root = Path(__file__).resolve().parent
    for rel in FIG_SCRIPTS:
        p = root / rel
        if not p.exists():
            raise FileNotFoundError(p)
        print(f"\n=== RUN {rel} ===")
        r = subprocess.run([sys.executable, str(p)], cwd=str(root))
        if r.returncode != 0:
            raise SystemExit(r.returncode)
    print("\n✓ all SPD figures done")

if __name__ == "__main__":
    main()
