import logging.config
from typing import Dict
from enum import Enum


def load_logging_config(prod: bool) -> Dict[str, str]:
    """
    Load config from yaml config file and translate it to a dictionary
    """
    ...


def configure_logger(config: Dict[str, str]) -> None:
    """
    Configure python logger with dict config
    """
    ...
