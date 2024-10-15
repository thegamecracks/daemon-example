import argparse
import sys

from . import daemonize
from .client import connect_to_server
from .server import bind_and_listen


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.set_defaults(command=lambda args: parser.print_help())
    subcmd = parser.add_subparsers()

    start = subcmd.add_parser("start", help="Start the daemon process.")
    start.set_defaults(command=start_server)

    stop = subcmd.add_parser("check", help="Check if the daemon process is running.")
    stop.set_defaults(command=ping_server)

    stop = subcmd.add_parser("stop", help="Stop the daemon process.")
    stop.set_defaults(command=stop_server)

    args = parser.parse_args()
    args.command(args)


# Commands
def start_server(args) -> None:
    check_server_not_running()
    daemonize()
    bind_and_listen()


def ping_server(args) -> None:
    with connect_to_server() as client:
        client.sendall(b"ping\n")
        print(client.recv(1024).decode().rstrip())


def stop_server(args) -> None:
    with connect_to_server() as client:
        client.sendall(b"stop\n")
        print(client.recv(1024).decode().rstrip())


# Utilities
def check_server_not_running() -> None:
    # Normally if the server is already running, binding will raise OSError.
    # However, let's try connecting to it before daemonization so we can give
    # a useful message to the user.
    try:
        with connect_to_server() as client:
            pass
    except SystemExit:
        pass
    else:
        sys.exit("Daemon already running")


if __name__ == "__main__":
    main()
