

import socket
from fusion.core.interface import Interface


class TCPSocket(Interface):

    def __init__(self, idn: str, target: str) -> None:
        super().__init__(idn, target)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def get_host(self) -> str:
        return '127.0.0.1'

    def open(self) -> None:
        self.socket.connect(self.target)

    def close(self) -> None:
        self.socket.close()

    def write(self, _: str) -> None:
        ...
