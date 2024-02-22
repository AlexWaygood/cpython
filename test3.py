from functools import singledispatchmethod

class Foo:
    @singledispatchmethod
    def neg(self, arg):
        raise NotImplementedError

    @neg.register(int)
    def _(self, arg):
        return -arg

    neg2 = neg

print(Foo().neg2(42))
