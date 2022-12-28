# -*- coding: utf-8 -*-
"""
Fusion Core - Device
====================

Copyright © 2022 dronectl. All rights reserved.
"""


import abc
from fusion.core.registry import Registry

class Device:

    def __init__(self, idn:str, hw_version:str, fw_version:str, interfaces: Registry) -> None:
        self.idn = idn
        self.hw_version = hw_version
        self.fw_version = fw_version

    @property
    def idn(self) -> str:
        """
        Device identification string

        :return: device identification string
        :rtype: str
        """
        return self.__idn

    @idn.setter
    def idn(self, idn: str) -> None:
        """
        Device identification string

        :param idn: device identification string
        :type idn: str
        """
        self.__idn = idn

    @property
    def hw_version(self) -> str:
        """
        Hardware version string

        :return: hardware version string
        :rtype: str
        """
        return self.__hw_version

    @hw_version.setter
    def hw_version(self, hw_version: str) -> None:
        """
        Hardware version string

        :param hw_version: hardware version string
        :type hw_version: str
        """
        self.__hw_version = hw_version

    @property
    def fw_version(self) -> str:
        """
        Firmware version string

        :return: _description_
        :rtype: str
        """
        return self.__fw_version

    @fw_version.setter
    def fw_version(self, fw_version: str) -> None:
        """
        Firmware version string

        :param fw_version: _description_
        :type fw_version: str
        """
        self.__fw_version = fw_version
    
    @property
    def interfaces(self) -> Registry:
        return self.__interfaces
    
    @interfaces.setter
    def interfaces(self, interfaces: Registry) -> None:
        self.__interfaces = interfaces

    @abc.abstractmethod
    def provision(self) -> None:
        """
        Provision device for testing. Check that interfaces defined are valid and a connection can be established.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def deprovision(self) -> None:
        """
        Deprovision device. Disconnect all interfaces.
        """
        raise NotImplementedError

