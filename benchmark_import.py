import sys
import time
import statistics
import subprocess

times = []

for _ in range(500):
    ret = subprocess.run(
        [sys.executable, "-c", "import time; t0 = time.perf_counter(); import typing; print(time.perf_counter() - t0)"],
        check=True,
        capture_output=True,
        text=True
    )
    times.append(float(ret.stdout.strip()))

print(statistics.mean(times))
