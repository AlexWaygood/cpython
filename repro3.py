import unittest

from typing import TypeVar, runtime_checkable, Protocol

class ProtocolTest(unittest.TestCase):
    def assertIsSubclass(self, cls, class_or_tuple, msg=None):
        if not issubclass(cls, class_or_tuple):
            message = '%r is not a subclass of %r' % (cls, class_or_tuple)
            if msg is not None:
                message += ' : %s' % msg
            raise self.failureException(message)

    def assertNotIsSubclass(self, cls, class_or_tuple, msg=None):
        if issubclass(cls, class_or_tuple):
            message = '%r is a subclass of %r' % (cls, class_or_tuple)
            if msg is not None:
                message += ' : %s' % msg
            raise self.failureException(message)
    
    def test_protocols_issubclass(self):
        T = TypeVar('T')

        @runtime_checkable
        class P(Protocol):
            def x(self): ...

        @runtime_checkable
        class PG(Protocol[T]):
            def x(self): ...

        class BadP(Protocol):
            def x(self): ...

        class BadPG(Protocol[T]):
            def x(self): ...

        class C:
            def x(self): ...

        self.assertIsSubclass(C, P)
        self.assertIsSubclass(C, PG)
        self.assertIsSubclass(BadP, PG)

        no_subscripted_generics = (
            "Subscripted generics cannot be used with class and instance checks"
        )

        with self.assertRaisesRegex(TypeError, no_subscripted_generics):
            issubclass(C, PG[T])
        with self.assertRaisesRegex(TypeError, no_subscripted_generics):
            issubclass(C, PG[C])

        only_runtime_checkable_protocols = (
            "Instance and class checks can only be used with "
            "@runtime_checkable protocols"
        )

        with self.assertRaisesRegex(TypeError, only_runtime_checkable_protocols):
            issubclass(C, BadP)
        with self.assertRaisesRegex(TypeError, only_runtime_checkable_protocols):
            issubclass(C, BadPG)

        with self.assertRaisesRegex(TypeError, no_subscripted_generics):
            issubclass(P, PG[T])
        with self.assertRaisesRegex(TypeError, no_subscripted_generics):
            issubclass(PG, PG[int])

        only_classes_allowed = r"issubclass\(\) arg 1 must be a class"

        with self.assertRaisesRegex(TypeError, only_classes_allowed):
            issubclass(1, P)
        with self.assertRaisesRegex(TypeError, only_classes_allowed):
            issubclass(1, PG)
        with self.assertRaisesRegex(TypeError, only_classes_allowed):
            issubclass(1, BadP)
        with self.assertRaisesRegex(TypeError, only_classes_allowed):
            issubclass(1, BadPG)

        self.assertNotIsSubclass(object, Protocol)
        self.assertNotIsSubclass(str, Protocol)
        self.assertNotIsSubclass(C, Protocol)
        for proto in P, PG, BadP, BadPG:
            with self.subTest(proto=proto.__name__):
                self.assertIsSubclass(proto, Protocol)


if __name__ == "__main__":
    unittest.main()

