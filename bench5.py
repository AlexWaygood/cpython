from typing import *
import time

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
    t: int
    u: int
    v: int
    w: int
    x: int
    y: int
    z: int

class Bar(Foo): pass

objs = [type('a', (), {})() for _ in range(1_000_000)]
start = time.perf_counter()
for obj in objs:
    isinstance(obj, Bar)
print(time.perf_counter() - start)
