import os
import logging
from fusion.config import Environment as env
from fusion.logger.config import configure_logger

# load dev state
runtime = env.PROD if os.environ.get('FUSION_DEV') else env.DEV
# configure logger
configure_logger(runtime)

logging.basicConfig(level=logging.DEBUG)
_logger = logging.getLogger(__name__)

_logger.debug("debug message")
_logger.info("info message")
_logger.warning("warning message")
_logger.error("error message")
_logger.exception("exception message")
