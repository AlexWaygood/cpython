import enum, pickle
        

class InnerClass:
    def __init__(self, owner):
        classes = ["dog", "cat", "cow"]
        self.list_enum = enum.Enum(
            "list_enum",
            classes,
            start=0,
            module=__name__,
            qualname=(
                f"{owner.__class__.__qualname__}."
                f"{self.__class__.__qualname__}."
                f"list_enum"
            ),
        )


class OuterClass:
    def __init__(self):
        self.inner_class = InnerClass(self)

