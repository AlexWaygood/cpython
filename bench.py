import time
from typing import Protocol, runtime_checkable

@runtime_checkable
class HasX(Protocol):
    x: int

@runtime_checkable
class SupportsInt(Protocol):
    def __int__(self) -> int: ...

@runtime_checkable
class SupportsIntAndX(Protocol):
    x: int
    def __int__(self) -> int: ...

class Empty:
    description = "Empty class with no attributes"

class Registered:
    description = "Subclass registered using ABCMeta.register"

HasX.register(Registered)
SupportsInt.register(Registered)
SupportsIntAndX.register(Registered)

class PropertyX:
    description = "Class with a property x"
    @property
    def x(self) -> int:
        return 42

class HasIntMethod:
    description = "Class with an __int__ method"
    def __int__(self):
        return 42

class PropertyXWithInt:
    description = "Class with a property x and an __int__ method"
    @property
    def x(self) -> int:
        return 42
    def __int__(self):
        return 42

class ClassVarX:
    description = "Class with a ClassVar x"
    x = 42

class ClassVarXWithInt:
    description = "Class with a ClassVar x and an __int__ method"
    x = 42
    def __int__(self):
        return 42

class InstanceVarX:
    description = "Class with an instance var x"
    def __init__(self):
        self.x = 42

class InstanceVarXWithInt:
    description = "Class with an instance var x and an __int__ method"
    def __init__(self):
        self.x = 42
    def __int__(self):
        return 42
    
class NominalX(HasX):
    description = "Class that explicitly subclasses HasX"
    def __init__(self):
        self.x = 42

class NominalSupportsInt(SupportsInt):
    description = "Class that explicitly subclasses SupportsInt"
    def __int__(self):
        return 42

class NominalXWithInt(SupportsIntAndX):
    description = "Class that explicitly subclasses NominalXWithInt"
    def __init__(self):
        self.x = 42


num_instances = 500_000

classes = {}
for cls in (
    Empty, Registered, PropertyX, PropertyXWithInt, ClassVarX, ClassVarXWithInt,
    InstanceVarX, InstanceVarXWithInt, NominalX, NominalXWithInt, HasIntMethod,
    NominalSupportsInt
):
    classes[cls] = [cls() for _ in range(num_instances)]


def bench(objs, title, protocol):
    start_time = time.perf_counter()
    for obj in objs:
        isinstance(obj, protocol)
    elapsed = time.perf_counter() - start_time
    print(f"{title}: {elapsed:.2f}")


print("Protocols with no callable members\n")
for cls in Empty, Registered, PropertyX, ClassVarX, InstanceVarX, NominalX:
    bench(classes[cls], cls.description, HasX)

print("\nProtocols with only callable members\n")
for cls in Empty, Registered, HasIntMethod, NominalSupportsInt:
    bench(classes[cls], cls.description, SupportsInt)

print("\nProtocols with callable and non-callable members\n")
for cls in (
    Empty, Registered, PropertyXWithInt, ClassVarXWithInt, InstanceVarXWithInt,
    NominalXWithInt
):
    bench(classes[cls], cls.description, SupportsIntAndX)
