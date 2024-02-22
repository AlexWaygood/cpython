from dataclasses import dataclass, asdict
from collections import OrderedDict
import timeit

@dataclass
class Foo:
    x: int

@dataclass
class Bar:
    x: Foo
    y: Foo
    z: Foo

@dataclass
class Baz:
    x: Bar
    y: Bar
    z: Bar

foo = Foo(42)
bar = Bar(foo, foo, foo)
baz = Baz(bar, bar, bar)

print(timeit.timeit(lambda: asdict(baz), number=250_000))

print(timeit.timeit(
    lambda: asdict(baz, dict_factory=OrderedDict),
    number=250_000
))
