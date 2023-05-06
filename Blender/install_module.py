import sys
import subprocess
from pathlib import Path
import bpy


TIMEOUT_SEC = 60

py_exec = Path(sys.executable)
command_args = [
    [str(py_exec), "-m", "ensurepip", "--user"],
    [str(py_exec), "-m", "pip", "install", "--upgrade", "pip"],
    [str(py_exec),"-m", "pip", "install", "--user", "scipy"]
]


def install_scipy():
    for args in command_args:
        success = subprocess.run(args, timeout=TIMEOUT_SEC).returncode
        if(success != 0)
            return False
    return True