import time
from typing import Protocol, runtime_checkable

@runtime_checkable
class HasX(Protocol):
    x: int

class Foo:
    @property
    def x(self) -> int:
        return 42

class Bar:
    x = 42

class Baz:
    def __init__(self):
        self.x = 42

class Egg: ...

class Nominal(HasX):
    def __init__(self):
        self.x = 42

class Registered: ...

HasX.register(Registered)

num_instances = 500_000
foos = [Foo() for _ in range(num_instances)]
bars = [Bar() for _ in range(num_instances)]
bazzes = [Baz() for _ in range(num_instances)]
basket = [Egg() for _ in range(num_instances)]
nominals = [Nominal() for _ in range(num_instances)]
registereds = [Registered() for _ in range(num_instances)]


def bench(objs, title):
    start_time = time.perf_counter()
    for obj in objs:
        isinstance(obj, HasX)
    elapsed = time.perf_counter() - start_time
    print(f"{title}: {elapsed:.2f}")


bench(foos, "Time taken for objects with a property")
bench(bars, "Time taken for objects with a classvar")
bench(bazzes, "Time taken for objects with an instance var")
bench(basket, "Time taken for objects with no var")
bench(nominals, "Time taken for nominal subclass instances")
bench(registereds, "Time taken for registered subclass instances")
