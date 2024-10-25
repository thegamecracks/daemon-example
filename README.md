# daemon-example

[![](https://img.shields.io/github/actions/workflow/status/thegamecracks/daemon-example/black-lint.yml?style=flat-square&label=black)](https://black.readthedocs.io/en/stable/)
[![](https://img.shields.io/github/actions/workflow/status/thegamecracks/daemon-example/pyright-lint.yml?style=flat-square&label=pyright)](https://microsoft.github.io/pyright/#/)

A simple demonstration of managing daemon processes.

## Usage

With Python 3.11+, install the package with:

```py
python -m venv
source .venv/bin/activate  # .venv\Scripts\activate on Windows
pip install git+https://github.com/thegamecracks/daemon-example@v1.2.0
```

Then play around with the CLI:

```sh
$ thedaemon  # or python -m thedaemon
usage: thedaemon [-h] [-P PORT] {start,ping,stop} ...

positional arguments:
  {start,ping,stop}
    start               Start the daemon process.
    ping                Check if the daemon process is running.
    stop                Stop the daemon process.

options:
  -h, --help            show this help message and exit
  -P PORT, --port PORT  The daemon port to use. (default: 21365)

$ thedaemon start

$ thedaemon start
Daemon already running

$ thedaemon ping
pong

$ thedaemon stop
stop

$ thedaemon ping
Failed to connect to daemon; did you start it?
```

`thedaemon start` can be passed a `--no-daemon` flag if you simply want
to run the server in the foreground. Beware that on Windows, the server
will be unable to handle signals like SIGINT (keyboard interrupt).

## Implementation

`thedaemon start` starts a socket server to serve as the workload for the
background process. It can be communicated with by using `thedaemon ping`.
`thedaemon stop` will connect to the server and send a stop command.

On Unix, a double-fork is performed to daemonize the server.

On Windows, a detached process is created using pythonw.exe as the executable.

## References

- https://github.com/Muterra/py_daemoniker
- https://stackoverflow.com/questions/881388/what-is-the-reason-for-performing-a-double-fork-when-creating-a-daemon
- https://gist.github.com/dcai/1075904/6f7be00f7f411d5c2e7cd1691dcbb68efacb789c
- https://aeb.win.tue.nl/linux/lk/lk-10.html

## License

This project is written under the MIT license.
