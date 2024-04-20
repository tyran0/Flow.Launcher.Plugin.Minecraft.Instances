from config import DataFile, load_config
from constants import VENV
from pathlib import Path
from subprocess import run


def build(main_file: str, icon: str, data_files: list[DataFile]):
    args = [
        "{} -m nuitka".format(VENV.PYTHON_PATH),
        "{}".format(main_file),
        "--assume-yes-for-downloads",
        "--standalone",
    ]

    if Path(icon).exists():
        args.append("--windows-icon-from-ico={}".format(icon))
    if data_files is not None:
        for data_file in data_files:
            src = data_file["src"]
            dest = data_file["dest"]

            args.append("--include-data-file={}={}".format(src, dest))

    run(" ".join(args))


def main():
    config = load_config()
    build(config.main_file, config.icon, config.data_files)


if __name__ == "__main__":
    main()
