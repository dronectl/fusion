# -*- coding: utf-8 -*-
"""
Fusion Core - Topology 
======================

Topology describes the arrangmenet of devices on discoverable by the test platform. The topology 
scopes the test execution by provisioning based on the availablility of devices.

Copyright © 2022 dronectl. All rights reserved.
"""

import sys
import logging

from typing import Any, Dict, List
from fusion.core.interface import Interface
from fusion.core.utils import pformat
from fusion.core.device import Device
from fusion.core.registry import Registry
from fusion.core.exceptions import TopologyError


class Topology:

    DEVICE_PATH = 'fusion.devices'
    INTERFACE_PATH = 'fusion.interfaces'

    def __init__(self) -> None:
        self._logger = logging.getLogger(__name__)
        self.name = ""
        self.devices = Registry()

    @property
    def nodes(self) -> int:
        """
        Number of device nodes

        :return: number of available devices
        :rtype: int
        """
        return self.devices.size

    @property
    def name(self) -> str:
        """
        Topology name

        :return: topology name
        :rtype: str
        """
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        """
        Topology name

        :param name: topology name
        :type name: str
        """
        self.__name = name

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

    def load(self, topology: Dict[str, Any]) -> None:
        """
        Load and instantiate topology instances
        """
        topology_doc = topology.get('topology')
        if topology_doc is None:
            raise TopologyError("Topology document must begin with the `topology` key")
        self._logger.info("Loading topology: %s", pformat(topology_doc))
        name = topology_doc.get('name')
        if name is None:
            raise TopologyError("Topology must have a name")
        self.name = name
        devices = topology_doc.get('devices')
        if devices is None:
            raise TopologyError("Must specify at least 1 device in topology document.")
        # build device tree
        device_objs:List[Device] = []
        for device in devices:
            # all keys except for type and interface relate 1-1 with device type
            try:
                d_qualname = device.pop('type')
            except KeyError: 
                raise TopologyError("Interface must define a type.")
            if d_qualname is None:
                raise TopologyError("Device must define a type.")
            # build interfaces
            try:
                interfaces = device.pop('interfaces')
            except KeyError: 
                raise TopologyError("Interface must define a type.")
            if interfaces is None:
                raise TopologyError("Devices must define at least 1 interface.")
            interface_objs:List[Interface] = []
            for interface in interfaces:
                # all keys except for type relate 1-1 with interface type
                try:
                    i_qualname = interface.pop('type')
                except KeyError: 
                    raise TopologyError("Interface must define a type.")
                interface_cls = getattr(sys.modules[str(self.INTERFACE_PATH)], i_qualname)
                interface_objs.append(interface_cls(**interface))
            device_cls = getattr(sys.modules[str(self.DEVICE_PATH)], d_qualname)
            device['interfaces'] = Registry(*interface_objs)
            device_objs.append(device_cls(**device))
        self.devices = Registry(*device_objs) 