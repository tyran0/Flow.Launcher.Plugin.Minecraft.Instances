import sys
from config import DEFAULT_VIRTUAL_ENV
from pathlib import Path


PYTHON_PATH = sys.executable


class VENV:
    NAME = DEFAULT_VIRTUAL_ENV
    PATH = Path().cwd().joinpath(NAME)
    PYTHON_PATH = Path(PATH).joinpath("Scripts", "python.exe")
    PIP_PATH = Path(PATH).joinpath("Scripts", "pip.exe")
