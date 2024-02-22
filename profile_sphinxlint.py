import cProfile
import sys
from sphinxlint.__main__ import main

files = [f"cpython/Doc/library/{module}.rst" for module in ("os", "typing", "sqlite3", "stdtypes", "argparse", "enum")]
files.append("cpython/Doc/reference/datamodel.rst")
cmd = f'main({["foo"] + files})'
cProfile.run(cmd, sort="cumulative")
