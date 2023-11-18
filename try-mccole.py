import importlib.resources
from pathlib import Path
import shutil
import sys

src_dir = Path(importlib.resources.files("mccole"))
print(f"root directory {src_dir}")
target_dir = Path(sys.argv[1])
if target_dir.exists():
    shutil.rmtree(target_dir)
shutil.copytree(src_dir / "lib", target_dir)
