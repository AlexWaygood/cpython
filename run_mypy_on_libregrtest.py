import argparse
import tempfile
import shutil
import subprocess
import sys
from pathlib import Path

def run_mypy_on_libregrtest(stdlib_dir: Path) -> None:
    with tempfile.TemporaryDirectory() as td:
        td_path = Path(td)
        new_test_dir = td_path / "test"
        new_test_dir.mkdir()
        for subdir_name in "support", "libregrtest":
            shutil.copytree(
                stdlib_dir / "test" / subdir_name, new_test_dir / subdir_name
            )
        mypy_command = [
            "mypy",
            "-p",
            "test.libregrtest",
            "--config-file",
            "test/libregrtest/mypy.ini",
        ]
        subprocess.run(mypy_command, cwd=td)


def main() -> None:
    parser = argparse.ArgumentParser("Script to run mypy on Lib/test/regrtest/")
    parser.add_argument(
        "--stdlib-dir",
        "-s",
        type=Path,
        required=True,
        help="path to the Lib/ dir where the Python stdlib is located",
    )
    args = parser.parse_args()
    stdlib_dir = args.stdlib_dir
    if not (stdlib_dir.exists() and stdlib_dir.is_dir()):
        parser.error(
            "--stdlib-dir must point to a directory that exists on your filesystem!"
        )
    run_mypy_on_libregrtest(args.stdlib_dir)


if __name__ == "__main__":
    main()
