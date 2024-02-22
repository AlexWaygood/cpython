from __future__ import annotations

from dataclasses import dataclass, field
from typing import Annotated, ClassVar

@dataclass
class Foo:
    x: Annotated[ClassVar[int], "foooo"]


f = Foo()
