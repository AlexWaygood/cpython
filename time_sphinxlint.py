import statistics
import subprocess
import sys


files = [f"cpython/Doc/library/{module}.rst" for module in ("os", "typing", "sqlite3", "stdtypes", "argparse", "enum")]
files.append("cpython/Doc/reference/datamodel.rst")
argv = ["foo"] + files

script = f"""\
import time
from sphinxlint.__main__ import main
t0 = time.perf_counter()
main({argv})
t1 = time.perf_counter() - t0
raise SystemExit(t1)"""


command = [sys.executable, "-c", "; ".join(script.splitlines())]
timings = [
    float(subprocess.run(command, capture_output=True, text=True).stderr.strip())
    for _ in range(5)
]
print(timings)
print(statistics.mean(timings))
