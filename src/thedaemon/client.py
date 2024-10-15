import socket
import sys

from .constants import ADDRESS, PORT


def connect_to_server() -> socket.socket:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((ADDRESS, PORT))
    except ConnectionRefusedError:
        client.close()
        sys.exit("Failed to connect to daemon; did you start it?")
    except BaseException:
        client.close()
        raise

    return client
