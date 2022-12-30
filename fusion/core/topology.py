# -*- coding: utf-8 -*-
"""
Fusion Core - Topology 
======================

Topology describes the arrangmenet of devices on discoverable by the test platform. The topology 
scopes the test execution by provisioning based on the availablility of devices.

Copyright © 2022 dronectl. All rights reserved.
"""

import logging
from pathlib import Path
from typing import Dict, List

from fusion.core.device import Device
from fusion.core.registry import Registry
from fusion.core.exceptions import TopologyError


class Topology:

    DEVICE_PATH = Path(__file__).parent.joinpath("devices").resolve()
    INTERFACE_PATH = Path(__file__).parent.joinpath("interfaces").resolve()

    def __init__(self) -> None:
        self._logger = logging.getLogger(__name__)
        self.devices = Registry({})

    @property
    def nodes(self) -> int:
        """
        Number of device nodes

        :return: number of available devices
        :rtype: int
        """
        return self.devices.size

    @property
    def devices(self) -> Registry[Device]:
        """
        Registered devices in topology

        :return: device registry
        :rtype: Registry[Device]
        """
        return self.__devices

    @devices.setter
    def devices(self, devices: Registry[Device]) -> None:
        """
        Registered devices in topology

        :param devices: device registry 
        :type devices: Registry[Device]
        """
        self.__devices = devices

    def load(self, topology: Dict[str, List[Dict]]) -> None:
        """
        Load and instantiate topology instances
        """
        devices = topology.get('devices')
        if devices is None:
            raise TopologyError("Must specify at least 1 device in topology document.")
        for device in devices:
            qualname = device.get("type")
            if qualname is None:
                raise TopologyError("Device must define a type.")
