# -*- coding: utf-8 -*-
"""
Fusion Configuration
====================

Copyright © 2022 dronectl. All rights reserved.
"""

from enum import Enum

class Environment(Enum):
    """
    Environment Enums. Note these string values must match the configuration file names.
    """
    DEV="dev"
    PROD="prod"

TOPOLOGY_CONF = ""