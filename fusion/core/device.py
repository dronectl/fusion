# -*- coding: utf-8 -*-
"""
Fusion Core - Device
====================

Fusion device abstract class

Copyright © 2022 dronectl. All rights reserved.
"""


import re
import abc
from fusion.core.interface import Interface
from fusion.core.registry import Registry, RegistryElemMixin


class Device(RegistryElemMixin):

    # semver regex
    SEMVER_REGEX = re.compile(r"([0-9]+)\.([0-9]+)\.([0-9]+)")

    def __init__(self, idn: str, hw_version: str, fw_version: str, interfaces: Registry[Interface]) -> None:
        self.idn = idn
        self.hw_version = hw_version
        self.fw_version = fw_version
        self.interfaces = interfaces

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
        if (self.SEMVER_REGEX.match(hw_version) is None):
            raise ValueError(f"Hardware version {hw_version} fails semver regex check")
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
        if (self.SEMVER_REGEX.match(fw_version) is None):
            raise ValueError(f"Firmware version {fw_version} fails semver regex check")
        self.__fw_version = fw_version

    @property
    def interfaces(self) -> Registry[Interface]:
        """
        Device communication interface registry

        :return: device communication interface registry
        :rtype: Registry[Interface]
        """
        return self.__interfaces

    @interfaces.setter
    def interfaces(self, interfaces: Registry[Interface]) -> None:
        """
        Device communication interface registry

        :param interfaces: device communication interface registry
        :type interfaces: Registry[Interface]
        """
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
