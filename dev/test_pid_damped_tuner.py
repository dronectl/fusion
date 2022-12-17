


from enum import Enum
from typing import Dict



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

class InterfaceType(Enum):

    SOCKET = "socket"
    UART = "uart"

class DeviceType(Enum):

    RAPTOR = "raptor"
    ESC = "esc"

class Interface:

    def __init__(self, address:str) -> None:
        self.address = address

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str) -> None:
        self.__address = address

class Device:
    def __init__(self, interfaces: Dict[InterfaceType, Interface], devices: Dict[DeviceType, 'Device']={}) -> None:
        self.interfaces = interfaces
        self.devices = devices

    @property
    def interfaces(self) -> Dict[InterfaceType, Interface]:
        return self.__interfaces

    @interfaces.setter
    def interfaces(self, interfaces: Dict[InterfaceType, Interface]) -> None:
        self.__interfaces = interfaces


class Raptor(Device):
    def __init__(self, interfaces: Dict[InterfaceType, Interface]) -> None:
        super().__init__(interfaces)

    def connect(self) -> None:
        raise NotImplementedError


class ESC(Device):
    def __init__(self, interfaces: Dict[InterfaceType, Interface]) -> None:
        super().__init__(interfaces)

    def arm(self) -> None:
        raise NotImplementedError

class Topology:

    def __init__(self, devices: Dict[DeviceType, Device]) -> None:
        self.devices = devices 

    @property
    def interfaces(self) -> Dict[InterfaceType, Interface]:
        return self.__interfaces

    @interfaces.setter
    def interfaces(self, interfaces: Dict[InterfaceType, Interface]) -> None:
        self.__interfaces = interfaces

    @property
    def devices(self) -> Dict[DeviceType, Device]:
        return self.__devices

    @devices.setter
    def devices(self, devices: Dict[DeviceType, Device]) -> None:
        self.__devices = devices

    def provision(self) -> None:
        raise NotImplementedError


class PIDDampedTuner:

    def __init__(self) -> None:
        # build topology required for test setup
        self.topology = Topology(
            devices={
                DeviceType.RAPTOR: Raptor(
                    interfaces={
                        InterfaceType.SOCKET: Interface("10.2.3.4:5025")
                    }
                ),
                DeviceType.ESC: ESC(

                ) 
            }
        )
        self.topology.provision()

    def 