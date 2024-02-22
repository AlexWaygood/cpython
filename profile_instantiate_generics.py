import cProfile

class Foo[T]: ...

cProfile.run("""\
for _ in range(100_000):
    Foo[int]()"""
)
