import selectors
import socket
import sys

from .constants import ADDRESS, PORT

BACKLOG = 5


def bind_and_listen() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        # Instead of opening a pidfile to check if the daemon process is
        # running, simply attempt to bind to the socket. If it is bound,
        # the daemon process is probably running and OSError should be
        # raised. However, it could also be possible that another process
        # is using our port. In that case, tough luck!
        print("Binding...")
        server.bind((ADDRESS, PORT))

        print("Listening for clients...")
        server.listen(BACKLOG)
        server.setblocking(False)

        handler = Handler()
        handler.register(server)
        handler.run_forever()


class Handler:
    def __init__(self) -> None:
        self.selector = selectors.DefaultSelector()

    def register(self, server: socket.socket) -> None:
        self.selector.register(server, selectors.EVENT_READ, self._accept)

    def run_forever(self) -> None:
        while True:
            # FIXME: handle signals in case --no-daemon is used to host
            events = self.selector.select()
            for key, mask in events:
                callback = key.data
                callback(key.fileobj, mask)

    def _accept(self, server: socket.socket, mask: int) -> None:
        client, addr = server.accept()
        client.setblocking(False)
        self.selector.register(client, selectors.EVENT_READ, self._data_received)

    def _data_received(self, client: socket.socket, mask: int) -> None:
        data = client.recv(1024)  # FIXME: may not receive all data, should buffer
        if data == b"ping\n":
            client.send(b"pong\n")  # FIXME: may not send all data
        elif data == b"stop\n":
            client.send(b"stop\n")  # FIXME: may not send all data
            sys.exit()
        elif data == b"":
            self.selector.unregister(client)
            client.close()
