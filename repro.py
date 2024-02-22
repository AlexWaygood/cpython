from typing import no_type_check_decorator, Self

@no_type_check_decorator
def dummy_decorator(func):
    return func


class Foo:
    def return_self(self) -> Self:
        return self

@dummy_decorator
def non_type_checked_decorated_func(x: int, y: str) -> 6:
    # This is to ensure that we avoid using a local variable that's already in use
    _call_memo = "foo"  # noqa: F841
    return "foo"


def non_type_checked_decorated_func2(x: int, y: str) -> 6:
    # This is to ensure that we avoid using a local variable that's already in use
    _call_memo = "foo"  # noqa: F841
    return "foo"

