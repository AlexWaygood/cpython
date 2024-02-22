import ast
import sys
import keyword
import seaborn
from pathlib import Path
from collections import Counter
from dataclasses import dataclass


LENGTHS_COUNT = Counter[int]()
NAMES_COUNT = Counter[str]()


@dataclass
class ExpectedAnIdentifier(Exception):
    node_dump: str
    lineno: int


class NameFinder(ast.NodeVisitor):
    def generic_visit(self, node: ast.AST) -> None:
        # A few fields are special-cased:
        # - ast.ImportFrom has the 'module' field;
        # - ast.Constant has the 'value' field;
        # - ast.alias has the 'name' field
        # All of these fields might have str values
        # that might not be identifiers
        if not isinstance(node, (ast.TypeIgnore, ast.Constant)):
            for field, value in ast.iter_fields(node):
                match node, field, value:
                    case _, "type_comment", _:
                        continue
                    case (ast.ImportFrom(), "module", str()):
                        if "." in value:
                            continue
                    case ast.alias(), "name", str():
                        if "." in value or value == "*":
                            continue
                    case _, _, str():
                        pass
                    case _, _, _:
                        continue
                if keyword.iskeyword(value) or not value.isidentifier():
                    raise ExpectedAnIdentifier(ast.dump(node, indent=2), node.lineno)
                LENGTHS_COUNT[len(value)] += 1
                NAMES_COUNT[value] += 1
        return super().generic_visit(node)


for path in Path(sys.argv[1]).rglob("*.py"):
    try:
        source = path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"Skipping {path} due to {e}")
        continue
    try:
        tree = ast.parse(source)
    except Exception as e:
        print(f"Skipping {path} due to {e}")
        continue
    try:
        NameFinder().visit(tree)
    except ExpectedAnIdentifier:
        print(f"Failed on {path}")
        raise

lengths_data = {i: LENGTHS_COUNT[i] for i in range(1, 31)}
seaborn.barplot(lengths_data)
