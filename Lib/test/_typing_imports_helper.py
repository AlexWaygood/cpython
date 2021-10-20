from __future__ import annotations

from typing import Optional, NamedTuple
from dataclasses import dataclass

OptionalIntType = Optional[int]

class FooNamedTuple(NamedTuple):
    a: OptionalIntType

@dataclass
class FooDataclass:
    a: OptionalIntType

class FooStandardClass:
    def __init__(self, a: OptionalIntType) -> None: ...
