from functools import singledispatch, singledispatchmethod
import time

class Test:
    __slots__ = ()
    @singledispatchmethod
    def go(self, item, arg):
        print('general')
    
    @go.register
    def _(self, item:int, arg):
        return item + arg

t0 = time.perf_counter()
test = Test()
for _ in range(10_000_000):
    test.go(1, 2)
print(time.perf_counter() - t0)
