from __future__ import annotations

import sys
import unittest

from test import _typing_imports_helper
from typing import get_type_hints
from dataclasses import dataclass


class AnnotationsOutputTest(unittest.TestCase):
    """Base class for several below tests"""
    def tearDown(self):
        globals().pop('collections', None)
        sys.modules.pop('collections', None)


class TypedDictTest(AnnotationsOutputTest):
    def test_typed_dict(self):
        annotations = get_type_hints(_typing_imports_helper.FooTypedDict)
        from collections import OrderedDict
        expected_annotations = {'a': OrderedDict}
        self.assertEqual(annotations, expected_annotations)


class TypedDictSubclassTest(AnnotationsOutputTest):
    def test_typed_dict_subclass(self):
        class FooTypedDictSubclass(_typing_imports_helper.FooTypedDict):
            b: int

        annotations = get_type_hints(FooTypedDictSubclass)
        from collections import OrderedDict
        expected_annotations = {'a': OrderedDict, 'b': int}
        self.assertEqual(annotations, expected_annotations)


class NamedTupleTest(AnnotationsOutputTest):
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


class NamedTupleSubclassTest(AnnotationsOutputTest):
    class FooNamedTupleSubclass(_typing_imports_helper.FooNamedTuple):
        b: int
    
    def test_named_tuple_subclass(self):
        annotations = get_type_hints(self.FooNamedTupleSubclass)
        from collections import OrderedDict
        expected_annotations = {'a': OrderedDict, 'b': int}
        self.assertEqual(annotations, expected_annotations)

    # Doesn't make sense to test __new__ for the subclass,
    # since __new__ is not automatically generated
    # for a subclass of a NamedTuple class
    

class DataclassTest(AnnotationsOutputTest):
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


class DataclassSubclassOfDataclassTest(AnnotationsOutputTest):
    @dataclass
    class FooDataclassSubclass(_typing_imports_helper.FooDataclass):
        b: int

    def test_dataclass(self):
        annotations = get_type_hints(self.FooDataclassSubclass)
        from collections import OrderedDict
        expected_annotations = {'a': OrderedDict, 'b': int}
        self.assertEqual(annotations, expected_annotations)

    def test_dataclass_new(self):
        annotations = get_type_hints(self.FooDataclassSubclass.__new__)
        self.assertEqual(annotations, {})

    def test_dataclass_init(self):
        annotations = get_type_hints(self.FooDataclassSubclass.__init__)
        from collections import OrderedDict
        expected_annotations = {'a': OrderedDict, 'b': int, 'return': type(None)}
        self.assertEqual(annotations, expected_annotations)


class StandardSubclassOfDataclassTest(AnnotationsOutputTest):
    class FooDataclassSubclass(_typing_imports_helper.FooDataclass):
        b: int

    def test_dataclass(self):
        annotations = get_type_hints(self.FooDataclassSubclass)
        from collections import OrderedDict
        expected_annotations = {'a': OrderedDict, 'b': int}
        self.assertEqual(annotations, expected_annotations)

    def test_dataclass_new(self):
        annotations = get_type_hints(self.FooDataclassSubclass.__new__)
        self.assertEqual(annotations, {})

    def test_dataclass_init(self):
        annotations = get_type_hints(self.FooDataclassSubclass.__init__)
        from collections import OrderedDict
        expected_annotations = {'a': OrderedDict, 'return': type(None)}
        self.assertEqual(annotations, expected_annotations)


class StandardClassInitAnnotationsTest(AnnotationsOutputTest):
    def test_standard_class(self):
        annotations = get_type_hints(_typing_imports_helper.FooStandardClassInitAnnotations)
        self.assertEqual(annotations, {})

    def test_standard_class_new(self):
        annotations = get_type_hints(_typing_imports_helper.FooStandardClassInitAnnotations.__new__)
        self.assertEqual(annotations, {})

    def test_standard_class_init(self):
        annotations = get_type_hints(_typing_imports_helper.FooStandardClassInitAnnotations.__init__)
        from collections import OrderedDict
        expected_annotations = {'a': OrderedDict, 'return': type(None)}
        self.assertEqual(annotations, expected_annotations)


# Doesn't make sense to test a subclass of a class with __init__ annotations,
# since __init__ is not auto-generated in a subclass.    


class StandardClassClassAnnotationsTest(AnnotationsOutputTest):
    def test_standard_class(self):
        annotations = get_type_hints(_typing_imports_helper.FooStandardClassClassAnnotations)
        from collections import OrderedDict
        self.assertEqual(annotations, {'a': OrderedDict})

    def test_standard_class_new(self):
        annotations = get_type_hints(_typing_imports_helper.FooStandardClassClassAnnotations.__new__)
        self.assertEqual(annotations, {})

    def test_standard_class_init(self):
        annotations = get_type_hints(_typing_imports_helper.FooStandardClassClassAnnotations.__init__)
        self.assertEqual(annotations, {})


class StandardSubclassClassAnnotationsTest(AnnotationsOutputTest):
    class StandardClassSubclass(_typing_imports_helper.FooStandardClassClassAnnotations):
        b: int
    
    def test_standard_class(self):
        annotations = get_type_hints(self.StandardClassSubclass)
        from collections import OrderedDict
        self.assertEqual(annotations, {'a': OrderedDict, 'b': int})

    def test_standard_class_new(self):
        annotations = get_type_hints(self.StandardClassSubclass.__new__)
        self.assertEqual(annotations, {})

    def test_standard_class_init(self):
        annotations = get_type_hints(self.StandardClassSubclass.__init__)
        self.assertEqual(annotations, {})


if __name__ == '__main__':
    unittest.main(verbosity=2)
    
