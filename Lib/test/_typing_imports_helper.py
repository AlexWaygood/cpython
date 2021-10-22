from __future__ import annotations

from typing import Optional, NamedTuple, TypedDict
from dataclasses import dataclass
from collections import OrderedDict

class FooTypedDict(TypedDict):
    a: OrderedDict

class FooNamedTuple(NamedTuple):
    a: OrderedDict

@dataclass
class FooDataclass:
    a: OrderedDict

class FooStandardClass:
    def __init__(self, a: OrderedDict) -> None: ...
