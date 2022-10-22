import logging
from fusion.logger.config import load_logging_config, configure_logger


# load logging config
log_config = load_logging_config(False)

# configure logger
configure_logger(log_config)

logging.basicConfig(level=logging.DEBUG)
_logger = logging.getLogger(__name__)

_logger.debug("debug message")
_logger.info("info message")
_logger.warning("warning message")
_logger.error("error message")
_logger.exception("exception message")
