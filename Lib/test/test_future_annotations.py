from __future__ import annotations

import sys
import unittest

from test import _typing_imports_helper
from typing import get_type_hints

class TestNoExceptionsRaised(unittest.TestCase):
    def test_typed_dict(self):
        get_type_hints(_typing_imports_helper.FooTypedDict)
    
    def test_named_tuple(self):
        get_type_hints(_typing_imports_helper.FooNamedTuple)
        get_type_hints(_typing_imports_helper.FooNamedTuple.__new__)

    def test_dataclass(self):
        get_type_hints(_typing_imports_helper.FooDataclass)
        get_type_hints(_typing_imports_helper.FooDataclass.__new__)
        get_type_hints(_typing_imports_helper.FooDataclass.__init__)

    def test_standard_class(self):
        get_type_hints(_typing_imports_helper.FooStandardClass)
        get_type_hints(_typing_imports_helper.FooStandardClass.__new__)
        get_type_hints(_typing_imports_helper.FooStandardClass.__init__)


class AnnotationsOutputTest(unittest.TestCase):
    """Base class for several below tests"""
    def tearDown(self):
        sys.modules.pop('collections', None)


class TestTypedDictOutput(AnnotationsOutputTest):
    def test_typed_dict(self):
        annotations = get_type_hints(_typing_imports_helper.FooTypedDict)
        from collections import OrderedDict
        expected_annotations = {'a': OrderedDict}
        self.assertEqual(annotations, expected_annotations)


class TestNamedTupleOutput(AnnotationsOutputTest):
    def test_named_tuple(self):
        annotations = get_type_hints(_typing_imports_helper.FooNamedTuple)
        from collections import OrderedDict
        expected_annotations = {'a': OrderedDict}
        self.assertEqual(annotations, expected_annotations)

    def test_named_tuple_new(self):
        annotations = get_type_hints(_typing_imports_helper.FooNamedTuple.__new__)
        from collections import OrderedDict
        expected_annotations = {'a': OrderedDict}
        self.assertEqual(annotations, expected_annotations)
    

class TestDataclassOutput(AnnotationsOutputTest):
    def test_dataclass(self):
        annotations = get_type_hints(_typing_imports_helper.FooDataclass)
        from collections import OrderedDict
        expected_annotations = {'a': OrderedDict}
        self.assertEqual(annotations, expected_annotations)

    def test_dataclass_new(self):
        annotations = get_type_hints(_typing_imports_helper.FooDataclass.__new__)
        self.assertEqual(annotations, {})

    def test_dataclass_init(self):
        annotations = get_type_hints(_typing_imports_helper.FooDataclass.__init__)
        from collections import OrderedDict
        expected_annotations = {'a': OrderedDict, 'return': type(None)}
        self.assertEqual(annotations, expected_annotations)


class TestStandardClassOutput(AnnotationsOutputTest):
    def test_standard_class(self):
        annotations = get_type_hints(_typing_imports_helper.FooStandardClass)
        self.assertEqual(annotations, {})

    def test_standard_class_new(self):
        annotations = get_type_hints(_typing_imports_helper.FooStandardClass.__new__)
        self.assertEqual(annotations, {})

    def test_standard_class_init(self):
        annotations = get_type_hints(_typing_imports_helper.FooStandardClass.__init__)
        from collections import OrderedDict
        expected_annotations = {'a': OrderedDict, 'return': type(None)}
        self.assertEqual(annotations, expected_annotations)

    


if __name__ == '__main__':
    unittest.main(verbosity=2)
    
