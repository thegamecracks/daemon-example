import os
import subprocess
import sys
from pathlib import PurePath
from typing import Sequence


def daemonize(*, win_args: Sequence[str]) -> None:
    """Create a detached process and invoke pythonw.exe with ``win_args``.

    The parent process will always exit after calling this function.
    However, through setting the environment variable ``__IS_DAEMON__``,
    this function becomes a no-op in the child process.

    Note that it is not necessary for the invocation of ``win_args``
    to lead to the same code path as the parent process.

    :param win_args:
        The command-line arguments to pass to the detached process.
        Only used in the Windows implementation of daemonize().

    """
    if os.getenv("__IS_DAEMON__") is not None:
        return

    # Carefully replace "python" with "pythonw" in case we're running a
    # free-threaded build where the windowed executable is pythonw3.11t.exe.
    python = PurePath(sys.executable)
    python = python.with_name(python.name.replace("python", "pythonw"))
    python = str(python)

    args = [python]
    args.extend(win_args)

    # https://docs.python.org/3/library/subprocess.html#subprocess.Popen
    # If specified, env must provide any variables required for the program to execute.
    env = os.environ.copy()
    env["__IS_DAEMON__"] = "1"

    subprocess.Popen(args, env=env, creationflags=subprocess.DETACHED_PROCESS)
    sys.exit()
