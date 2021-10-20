from __future__ import annotations

import unittest

from dataclasses import dataclass
from test import _typing_imports_helper
import typing
from typing import get_type_hints, NamedTuple

class TestFutureAnnotations(unittest.TestCase):
    def test_named_tuple(self):
        class IdenticalNamedTuple(NamedTuple):
            a: typing.Optional[int]

        self.assertEqual(
            get_type_hints(_typing_imports_helper.FooNamedTuple),
            get_type_hints(IdenticalNamedTuple)
        )

        self.assertEqual(
            get_type_hints(_typing_imports_helper.FooNamedTuple.__init__),
            get_type_hints(IdenticalNamedTuple.__init__)
        )

        self.assertEqual(
            get_type_hints(_typing_imports_helper.FooNamedTuple.__new__),
            get_type_hints(IdenticalNamedTuple.__new__)
        )

    def test_dataclass(self):
        @dataclass
        class IdenticalDataclass:
            a: typing.Optional[int]

        self.assertEqual(
            get_type_hints(_typing_imports_helper.FooDataclass),
            get_type_hints(IdenticalDataclass)
        )

        self.assertEqual(
            get_type_hints(_typing_imports_helper.FooDataclass.__init__),
            get_type_hints(IdenticalDataclass.__init__)
        )

        self.assertEqual(
            get_type_hints(_typing_imports_helper.FooDataclass.__new__),
            get_type_hints(IdenticalDataclass.__new__)
        )

    def test_standard_class(self):
        class IdenticalStandardClass:
            def __init__(self, a: typing.Optional[int]) -> None: ...

        self.assertEqual(
            get_type_hints(_typing_imports_helper.FooStandardClass),
            get_type_hints(IdenticalStandardClass)
        )

        self.assertEqual(
            get_type_hints(_typing_imports_helper.FooStandardClass.__init__),
            get_type_hints(IdenticalStandardClass.__init__)
        )

        self.assertEqual(
            get_type_hints(_typing_imports_helper.FooStandardClass.__new__),
            get_type_hints(IdenticalStandardClass.__new__)
        )


if __name__ == '__main__':
    unittest.main(verbosity=2)
    
