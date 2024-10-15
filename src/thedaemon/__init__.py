import sys

if sys.platform == "win32":
    from ._daemon_win import daemonize
else:
    from ._daemon_unix import daemonize
