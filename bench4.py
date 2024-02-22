from typing import *
import time

@runtime_checkable
class Foo(Protocol):
    a: int
    b: int
    c: int
    d: int
    e: int
    f: int
    g: int
    h: int
    i: int
    j: int
    k: int
    l: int
    m: int
    n: int
    o: int
    p: int
    q: int
    r: int
    s: int
#    t: int
#    u: int
#    v: int
#    w: int
#    x: int
#    y: int
#    z: int

class Bar:
    def __init__(self):
        for attrname in 'abcdefghijklmnopqrs':
            setattr(self, attrname, 42)

bars = [Bar() for _ in range(100_000)]
start = time.perf_counter()
for bar in bars:
    isinstance(bar, Foo)
print(time.perf_counter() - start)

objs = [object() for _ in range(100_000)]
start = time.perf_counter()
for obj in objs:
    isinstance(obj, Foo)
print(time.perf_counter() - start)
