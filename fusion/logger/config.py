# -*- coding: utf-8 -*-
"""
Logging Configuration Helpers
=============================

Copyright © 2022 dronectl. All rights reserved.
"""

import yaml
import logging.config

from pathlib import Path
from fusion.config import Environment


def configure_logger(runtime: Environment) -> None:
    """
    Configure python logger from runtime environment

    :param runtime: prod or dev runtime enum
    :type runtime: Environment
    """
    logging_conf_path = Path(__file__).parent.joinpath(f'config/{runtime.value}.yaml').resolve()
    # load dict from path stream
    log_conf = yaml.safe_load(logging_conf_path.read_text())
    # configure logger
    logging.config.dictConfig(log_conf)
