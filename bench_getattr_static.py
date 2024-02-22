from timeit import timeit
from statistics import mean, stdev
from inspect import getattr_static

class Foo:
    @property
    def x(self) -> int:
        return 42

class Bar:
    x = 42

class WithParentClassX(Bar): ...

class Baz:
    def __init__(self):
        self.x = 42

class WithParentX(Baz): ...

class Missing: ...

class Slotted:
    __slots__ = ('x',)
    def __init__(self):
        self.x = 42

class Method:
    def x(self): ...

class ClsMethod:
    @classmethod
    def x(cls): ...

class StMethod:
    @staticmethod
    def x(): ...

import gc
gc.disable()

times = []
def stats():
    ts = [t * 1e8 for t in sorted(times)[:5]]
    return f'{round(mean(ts)):4} ± {round(stdev(ts)):2} ns '

def bench(obj):
    # Warmup:
    for _ in range(5):
        number = 100
        timeit(lambda: getattr_static(obj, 'x', None), number=number)

    # Actual bench:
    for _ in range(50):
        number = 1000
        t = timeit(lambda: getattr_static(obj, 'x', None), number=number) / number
        times.append(t)

    bench_name = (
        f'type[{obj.__name__}]'
        if isinstance(obj, type)
        else obj.__class__.__name__
    )
    print(f"{bench_name: <25}: {stats()}")
    times.clear()


bench(Foo)
bench(Foo())
bench(Bar)
bench(Bar())
bench(WithParentClassX())
bench(Baz())
bench(WithParentX())
bench(Missing)
bench(Missing())
bench(Slotted())
bench(Method())
bench(StMethod())
bench(ClsMethod())
