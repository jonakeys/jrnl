# Copyright © 2012-2023 jrnl contributors
# License: https://www.gnu.org/licenses/gpl-3.0.html

import os.path


def home_dir() -> str:
    return os.path.expanduser("~")


def expand_path(path: str) -> str:
    return os.path.expanduser(os.path.expandvars(path))


def absolute_path(path: str) -> str:
    return os.path.abspath(expand_path(path))
