# -*- coding: utf-8 -*-
"""
Fusion Payload
==============

Copyright © 2022 dronectl. All rights reserved.
"""

import abc

class Payload:

    def __init__(self, psize: int) -> None:
        self.psize = psize

    @property
    def psize(self) -> int:
        return self.__psize
    
    @psize.setter
    def psize(self, payload_size:int) -> None:
        self.__psize = payload_size

    @abc.abstractmethod
    def unpack(self, raw:bytes):
        """
        Unpack the byte struct and save to properties.

        :param raw: byte struct
        :type raw: bytes
        """
        raise NotImplementedError
    
    @abc.abstractmethod
    def pack(self) -> bytes:
        """
        Pack this payload instance into a bytestream.

        :return: packed bytestream
        :rtype: bytes
        """
        raise NotImplementedError
