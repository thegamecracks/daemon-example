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
$ thedaemon check
Failed to connect to daemon; did you start it?
```

## License

This project is written under the MIT license.
