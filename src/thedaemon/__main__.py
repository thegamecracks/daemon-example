import argparse
import os
import sys

from . import daemonize
from .client import connect_to_server
from .server import bind_and_listen


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.set_defaults(command=lambda args: parser.print_help())
    parser.add_argument(
        "-P",
        "--port",
        default=os.environ.get("THEDAEMON_PORT", 21365),
        help="The daemon port to use. (default: %(default)s)",
        type=int,
    )
    subcmd = parser.add_subparsers()

    start = subcmd.add_parser("start", help="Start the daemon process.")
    start.set_defaults(command=start_server)
    start.add_argument(
        "--daemon",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Enable/disable daemonization of the server",
    )

    ping = subcmd.add_parser("ping", help="Check if the daemon process is running.")
    ping.set_defaults(command=ping_server)

    stop = subcmd.add_parser("stop", help="Stop the daemon process.")
    stop.set_defaults(command=stop_server)

    args = parser.parse_args()
    args.command(args)


# Commands
def start_server(args) -> None:
    check_server_not_running(port=args.port)

    if args.daemon:
        daemonize(win_args=["-m", "thedaemon", "-P", str(args.port), "start"])

    bind_and_listen(port=args.port)


def ping_server(args) -> None:
    with connect_to_server(port=args.port) as client:
        client.sendall(b"ping\n")
        print(client.recv(1024).decode().rstrip())


def stop_server(args) -> None:
    with connect_to_server(port=args.port) as client:
        client.sendall(b"stop\n")
        print(client.recv(1024).decode().rstrip())


# Utilities
def check_server_not_running(*, port: int) -> None:
    # Normally if the server is already running, binding will raise OSError.
    # However, let's try connecting to it before daemonization so we can give
    # a useful message to the user.
    try:
        with connect_to_server(port=port) as client:
            pass
    except SystemExit:
        pass
    else:
        sys.exit("Daemon already running")


if __name__ == "__main__":
    main()
