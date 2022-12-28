# -*- coding: utf-8 -*-
"""
Fusion Core - Interface
=======================

Copyright © 2022 dronectl. All rights reserved.
"""


import abc

class Interface:

    def __init__(self, idn:str) -> None:
        self.idn = idn

    @property
    def idn(self) -> str:
        """
        Interface identification string

        :return: interface identification string
        :rtype: str
        """
        return self.__idn

    @idn.setter
    def idn(self, idn: str) -> None:
        """
        Interface identification string

        :param idn: interface identification string
        :type idn: str
        """
        self.__idn = idn

    @abc.abstractmethod
    def connect(self) -> None:
        ...

    @abc.abstractmethod
    def disconnect(self) -> None:
        ...