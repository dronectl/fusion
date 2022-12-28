# -*- coding: utf-8 -*-
"""
Fusion Core - Topology 
======================

Copyright © 2022 dronectl. All rights reserved.
"""

from typing import List
from pathlib import Path

from fusion.core.exceptions import TopologyError


class Topology:

    DEVICE_PATH = Path(__file__).parent.joinpath("devices").resolve()
    INTERFACE_PATH = Path(__file__).parent.joinpath("interfaces").resolve()

    def __init__(self, devices: List[dict]) -> None:
        for device in devices:
            qualname = device.get("type")
            if qualname is None:
                raise TopologyError("Device must define a type.")
