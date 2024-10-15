# daemon-example

[![](https://img.shields.io/github/actions/workflow/status/thegamecracks/daemon-example/black-lint.yml?style=flat-square&label=black)](https://black.readthedocs.io/en/stable/)
[![](https://img.shields.io/github/actions/workflow/status/thegamecracks/daemon-example/pyright-lint.yml?style=flat-square&label=pyright)](https://microsoft.github.io/pyright/#/)

A simple demonstration of managing daemon processes.

## Usage

With Python 3.11+, install the package with:

```py
python -m venv
source .venv/bin/activate  # .venv\Scripts\activate on Windows
pip install .
```

Then play around with the CLI:

```sh
$ thedaemon  # or python -m thedaemon
usage: thedaemon [-h] {start,check,stop} ...

positional arguments:
  {start,check,stop}
    start             Start the daemon process.
    check             Check if the daemon process is running.
    stop              Stop the daemon process.

options:
  -h, --help          show this help message and exit

$ thedaemon start

$ thedaemon start
Daemon already running

$ thedaemon check
pong

$ thedaemon stop
stop

$ thedaemon check
Failed to connect to daemon; did you start it?
```

## Implementation

`thedaemon start` starts a socket server to serve as the workload for the
background process. It can be communicated with by using `thedaemon check`.
`thedaemon stop` will connect to the server and send a stop command.

On Unix, a double-fork is performed to daemonize the server.

On Windows, daemonization is not implemented and will simply take control of
the current terminal.

## References

- https://github.com/Muterra/py_daemoniker
- https://stackoverflow.com/questions/881388/what-is-the-reason-for-performing-a-double-fork-when-creating-a-daemon
- https://gist.github.com/dcai/1075904/6f7be00f7f411d5c2e7cd1691dcbb68efacb789c
- https://aeb.win.tue.nl/linux/lk/lk-10.html

## License

This project is written under the MIT license.
