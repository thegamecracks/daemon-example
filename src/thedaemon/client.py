import socket
import sys

from .constants import ADDRESS


def connect_to_server(*, port: int) -> socket.socket:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    if sys.platform == "win32":
        # Windows might take a bit before refusing a connection.
        # Let's add a timeout to speed things along.
        client.settimeout(0.1)

    try:
        client.connect((ADDRESS, port))
    except (ConnectionRefusedError, TimeoutError):
        client.close()
        sys.exit("Failed to connect to daemon; did you start it?")
    except BaseException:
        client.close()
        raise

    if sys.platform == "win32":
        client.settimeout(None)

    return client
