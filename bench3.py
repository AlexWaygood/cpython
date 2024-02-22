from typing import *
import cProfile

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

class Bar:
    def __init__(self):
        for attrname in 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j':
            setattr(self, attrname, 42)

bars = [Bar() for _ in range(100_000)]

cProfile.run("""\
for bar in bars:
    isinstance(bar, Foo)
"""
)
