import os
import sys


def daemonize(*, win_args: list[str]) -> None:
    """Daemonize the current process by double-forking.

    The parent process will always exit after calling this function.

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
