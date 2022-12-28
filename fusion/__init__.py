# -*- coding: utf-8 -*-
"""
Fusion API
==========

Copyright © 2022 dronectl. All rights reserved.
"""
import os
import logging
from fusion.__version__ import __version__
from fusion.config import Environment as env
from fusion.logger.config import configure_logger

# load dev state
runtime = env.PROD if os.environ.get('FUSION_DEV') else env.DEV
# configure logger
configure_logger(runtime)

logging.basicConfig(level=logging.DEBUG)
_logger = logging.getLogger(__name__)
_logger.debug("Fusion version %s", __version__)
