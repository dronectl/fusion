


from enum import Enum
from typing import Dict, TypeVar

from fusion.core.registry import Registry

"""
topology:
    host:
        type: RPI
        links:
            - type: socket
              direction: r/w
            - type: http
              direction: r/w
        devices:
            - type: Raptor
              links:
                - type: socket
                  direction: r/w
                devices:
                    - type: ESC
                      devices:
                      links:
                        - type: uart
                          direction: r/w
                    pa:
                        type: KD44544
                        devices:
                        links:
                            - type: i2c 
                              direction: r/w
                    pd:
                        devices:
                        links:
                            - type: gpio 
                              direction: w
                    sd:
                        links:
                            - type: spi 
                              direction: r/w
"""

_T = TypeVar('_T')

class ESCCommands(Enum):
    SLEEP = 0x45
    ARM = 0x34
    WAKE = 0x67

class Command:
    pass

class InterfaceType(Enum):

    SOCKET = "socket"
    UART = "uart"

class DeviceType(Enum):

    RAPTOR = "raptor"
    ESC = "esc"

class Interface:

    def __init__(self, address:str) -> None:
        self.address = address

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        return

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str) -> None:
        self.__address = address

    def connect(self):
        ...
    
    def disconnect(self):
        ...
    
    def write(self, bytes:bytes):
        ...

class Socket(Interface):
    ...

class Device:
    def __init__(self, interfaces: Registry[Interface]) -> None:
        self.interfaces = interfaces

    @property
    def interfaces(self) -> Registry[Interface]:
        return self.__interfaces

    @interfaces.setter
    def interfaces(self, interfaces: Registry[Interface]) -> None:
        self.__interfaces = interfaces


class Raptor(Device):
    def __init__(self, interfaces: Registry[Interface]) -> None:
        super().__init__(interfaces)

    def connect(self) -> None:
        raise NotImplementedError
    
    def send(self, command: Command) -> None:
        ...

class ESC(Device):
    def __init__(self, interfaces: Registry[Interface]) -> None:
        super().__init__(interfaces)

    def arm(self) -> None:
        raise NotImplementedError

class Topology:

    def __init__(self, devices: Registry[Device]) -> None:
        self.devices = devices

    @property
    def devices(self) -> Registry[Device]:
        return self.__devices

    @devices.setter
    def devices(self, devices: Registry[Device]) -> None:
        self.__devices = devices

    def provision(self) -> None:
        raise NotImplementedError


def construct_link(host:Device, target:Device, interface: _T) -> _T:
    ...

class PIDDampedTuner:

    def __init__(self) -> None:
        # build topology required for test setup
        self.topology = Topology()
        self.topology.provision()

    def test_dampener(self) -> None:
        """
        """
        raptor = self.topology.devices.get(Raptor)
        with raptor.interfaces.get(Socket) as socket:
            socket.write(b"send arm command to esc")
        # instruct raptor to send arm command to ESC
        # raptor is assumed to run fusion server interpreter
        raptor.devices.get(DeviceType.ESC).send(ESCCommands.WAKE)