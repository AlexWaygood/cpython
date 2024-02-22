import cProfile
import typing

cProfile.run("""\
for _ in range(10_000):
    isinstance(0, typing.SupportsIndex)"""
)
