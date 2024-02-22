import sys
import subprocess
import dataclasses
from dataclasses import dataclass, asdict, astuple
from timeit import timeit
from decimal import Decimal


def new_best_case_test(iterations=10_000):
    @dataclass
    class ListExample:
        l: list[int]

    example = ListExample([i for i in range(1000)])

    print(f"Test Iterations: {iterations}")

    new = timeit(lambda: asdict(example), number=iterations)

    print(f"List of Int case asdict: {new:.2f}s\n")


def new_worst_case_test(iterations=1_000):
    @dataclass
    class ListExample:
        l: list[Decimal]

    example = ListExample([Decimal(i) for i in range(1000)])

    print(f"Test Iterations: {iterations}")

    new = timeit(lambda: asdict(example), number=iterations)

    print(f"List of Decimal case asdict: {new:.2f}s\n")


def best_case_test(iterations=1_000_000):
    # Best case - everything skips deepcopy

    @dataclass
    class AtomicExample:
        p: str = "usr/bin/python"
        major: int = 3
        minor: int = 11
        installed: bool = True

    atomic_ex = AtomicExample()

    print(f"Test Iterations: {iterations}")

    new = timeit(lambda: asdict(atomic_ex), number=iterations)

    print(f"Basic types case asdict: {new:.2f}s")

    new = timeit(lambda: astuple(atomic_ex), number=iterations)

    print(f"Basic types astuple: {new:.2f}s")
    print("")


def worst_case_test(iterations=100_000):
    # Worst case - everything has to be deepcopied

    class PyVer:
        def __init__(self, major=3, minor=11):
            self.major = major
            self.minor = minor

        def __hash__(self):
            return hash((self.major, self.minor))

        def __eq__(self, other):
            if self.__class__ == other.__class__:
                return (self.major, self.minor) == (other.major, other.minor)
            return NotImplemented

    @dataclass
    class WorstExample:
        v311: PyVer = PyVer()
        v310: PyVer = PyVer(3, 10)
        v309: PyVer = PyVer(3, 9)
        v27: PyVer = PyVer(2, 7)

    non_atomic_ex = WorstExample()

    print(f"Test Iterations: {iterations}")

    new = timeit(lambda: asdict(non_atomic_ex), number=iterations)

    print(f"Opaque types asdict: {new:.2f}s")

    new = timeit(lambda: astuple(non_atomic_ex), number=iterations)

    print(f"Opaque types astuple: {new:.2f}s")
    print("")


def mixed_containers_test(iterations=100):
    from timeit import timeit

    # Extended from the tests ORJSON uses to claim how slow
    # json is for dataclasses using asdict

    class Spam:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __repr__(self) -> str:
            return f"Spam({self.x!r}, {self.y!r})"

        def __eq__(self, other):
            if self.__class__ == other.__class__:
                return (self.x, self.y) == (other.x, other.y)
            return NotImplemented

        def __hash__(self):
            return hash((self.x, self.y))

    @dataclasses.dataclass
    class Eggs:
        x: int
        y: str

    @dataclasses.dataclass
    class Member:
        id: int
        active: bool

    @dataclasses.dataclass
    class Object:
        id: int
        name: str
        members: list[Member]
        spam: Spam
        eggs: Eggs

    @dataclasses.dataclass
    class ObjectHolder:
        objects: dict[str, Object]

    objects_as_dataclass = {
        f"object_{i}": Object(
            i,
            str(i) * 3,
            [Member(j, True) for j in range(0, 10)],
            Spam(i, str(i)),
            Eggs(i, str(i))
        )
        for i in range(100000, 101000)
    }

    objectholder = ObjectHolder(objects_as_dataclass)

    print(f"Test Iterations: {iterations}")

    new = timeit(
        lambda: asdict(objectholder),
        number=iterations
    )

    print(f"Mixed containers asdict: {new:.2f}s")

    new = timeit(
        lambda: astuple(objectholder),
        number=iterations
    )

    print(f"Mixed containers astuple: {new:.2f}s")
    print("")


class CustomDict(dict):
    # This is just here to NOT get special cased
    pass


if __name__ == "__main__":
    print("Dataclasses asdict/astuple speed tests")
    print("--------------------------------------")

    print("Python v{v.major}.{v.minor}.{v.micro}{v.releaselevel}{v.serial}".format(v=sys.version_info))
    branch = subprocess.run("git branch --show-current", shell=True, capture_output=True)
    branch = branch.stdout.decode('utf8').strip()

    print(f"GIT branch: {branch}")

    new_best_case_test()
    new_worst_case_test()
    best_case_test()
    worst_case_test()
    mixed_containers_test()
