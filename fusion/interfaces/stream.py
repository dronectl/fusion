# -*- coding: utf-8 -*-
"""
Fusion Interface - Stream
=========================

Streaming interface.

Copyright © 2022 dronectl. All rights reserved.
"""

import socket

from fusion.core.interface import Interface


class Stream(Interface):

    def __init__(self, address: str, port: int, format) -> None:
        self.address = address
        self.port = port

    def connect(self) -> None:
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(f'{self.address}:{self.port}')

    def disconnect(self) -> None:
        self.socket.close()
