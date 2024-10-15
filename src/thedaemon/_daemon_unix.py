import os
import sys
from typing import Sequence


def daemonize(*, win_args: Sequence[str]) -> None:
    """Daemonize the current process by double-forking.

    The parent process will always exit after calling this function.

    :param win_args:
        The command-line arguments to pass to the detached process.
        Only used in the Windows implementation of daemonize().

    """
    pid = os.fork()
    if pid > 0:
        sys.exit()

    os.setsid()

    pid = os.fork()
    if pid > 0:
        sys.exit()

    sys.stdin = open(os.devnull, "r")
    sys.stdout = open(os.devnull, "w")
    sys.stderr = open(os.devnull, "w")
