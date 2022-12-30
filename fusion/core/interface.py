# -*- coding: utf-8 -*-
"""
Fusion Core - Interface
=======================

Copyright © 2022 dronectl. All rights reserved.
"""


import abc


class Interface(abc.ABC):

    def __init__(self, idn: str, target: str) -> None:
        self.idn = idn
        self.target = target
        self.host = self.get_host()
        self.outgoing_transaction_log_fmt = f"{self.host} -> {self.target} | %s"
        self.incoming_transaction_log_fmt = f"{self.host} <- {self.target} | %s"

    def __enter__(self):
        self.open()
        return self

    def __exit__(self) -> None:
        self.close()

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

    @property
    def host(self) -> str:
        """
        Host address string

        :return: host address identification
        :rtype: str
        """
        return self.__host

    @host.setter
    def host(self, host: str) -> None:
        """
        Host address string

        :param host: host address identification
        :type host: str
        """
        self.__host = host

    @property
    def target(self) -> str:
        """
        Target device address string

        :return: target device address identification
        :rtype: str
        """
        return self.__target

    @target.setter
    def target(self, target: str) -> None:
        """
        Target device address string

        :param target: target device address identification
        :type target: str
        """
        self.__target = target

    @abc.abstractmethod
    def open(self) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def close(self) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def get_host(self) -> str:
        raise NotImplementedError
