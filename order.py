class Meta(type):
    def __new__(mcls, name, *args, **kwargs):
        print(f'{name}: entering metaclass __new__')
        cls = super().__new__(mcls, name, *args, **kwargs)
        print(f'{name}: exiting metaclass __new__')
        return cls

    def __init__(cls, *args, **kwargs):
        print(f'{cls.__name__}: entering metaclass __init__')
        super().__init__(*args, **kwargs)
        print(f'{cls.__name__}: exiting metaclass __init__')

    def __call__(cls, *args, **kwargs):
        print(f'{cls.__name__}: entering metaclass __call__')
        new = super().__call__(*args, **kwargs)
        print(f'{cls.__name__}: exiting metaclass __call__')
        return new


class Klass(metaclass=Meta):
    def __init_subclass__(cls, *args, **kwargs):
        print(f'{cls.__name__}: entering class __init_subclass__')
        super().__init_subclass__(*args, **kwargs)
        print(f'{cls.__name__}: exiting class __init_subclass__')

    def __new__(cls, *args, **kwargs):
        print(f'{cls.__name__}: entering class __new__')
        obj = super().__new__(cls, *args, **kwargs)
        print(f'{cls.__name__}: exiting class __new__')
        return obj

    def __init__(self, *args, **kwargs):
        print(f'{self.__class__.__name__}: entering class __init__')
        super().__init__(*args, **kwargs)
        print(f'{self.__class__.__name__}: exiting class __init__')

    def __call__(self, *args, **kwargs):
        print(f'{self.__class__.__name__}: entering class __call__')
        print(f'{self.__class__.__name__}: exiting class __call__')
        return 42


class SubKlass(Klass): pass

obj = Klass()
obj()
