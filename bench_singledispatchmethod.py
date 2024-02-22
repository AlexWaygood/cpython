import pyperf

setup="""
from functools import singledispatch, singledispatchmethod

class Test:
    @singledispatchmethod
    def go(self, item, arg):
        pass

    @go.register
    def _(self, item: int, arg):
        return item + arg

class Slot:
    __slots__ = ('a', 'b')
    @singledispatchmethod
    def go(self, item, arg):
        pass

    @go.register
    def _(self, item: int, arg):
        return item + arg

t = Test()
s= Slot()
"""

runner = pyperf.Runner()
runner.timeit(name="bench singledispatchmethod", stmt="""_ = t.go(1, 1)""", setup=setup )
runner.timeit(name="bench singledispatchmethod slots", stmt="""_ = s.go(1, 1)""", setup=setup )
