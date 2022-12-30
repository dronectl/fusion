
from fusion.core.device import Device
from fusion.core.interface import Interface
from fusion.core.registry import Registry


class Raptor(Device):
    def __init__(self, idn: str, hw_version: str, fw_version: str, interfaces: Registry[Interface]) -> None:
        super().__init__(idn, hw_version, fw_version, interfaces)
