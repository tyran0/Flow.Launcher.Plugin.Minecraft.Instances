from config import load_config
from os import path
from constants import VENV, PYTHON_PATH
from subprocess import run


def main():
    config = load_config()

    if not path.exists(VENV.PATH):
        print("Creating virtual environment '{}'...".format(config.virtual_env))
        run("{} -m venv {}".format(PYTHON_PATH, config.virtual_env))
        print("Finished!")

    print("Installing dependencies...")
    for requirements in [config.requirements, config.requirements_dev]:
        if not path.exists(requirements):
            continue
        run("{} install -U -r {}".format(VENV.PIP_PATH, requirements))
    print("Finished!")


if __name__ == "__main__":
    main()
