import time
from typing import Protocol, runtime_checkable

start = time.perf_counter()

for _ in range(500_000):
    @runtime_checkable
    class X(Protocol):
        a: int
        b: int
        c: int
        d: int
        e: int

end = time.perf_counter() - start
print(end)
