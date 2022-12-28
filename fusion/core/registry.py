# -*- coding: utf-8 -*-
"""
Fusion Core - Registry
======================

Registries are custom object containers

Copyright © 2022 dronectl. All rights reserved.
"""

from fusion.core.device import Device
from fusion.core.interface import Interface

from typing import List, Dict, Generator, Generic, Type, TypeVar

_R = TypeVar('_R', Device, Interface)


class Registry(Generic[_R]):

    """
    {
        Raptor: [
            Raptor("rpt-123"),
            Raptor("rpt-159")
        ],
        ESC: [
            ESC("esc-234")
        ]
    }
    raptor: Raptor = devices.get(Raptor, "rpt-123")
    esc: ESC = devices.get(ESC, "esc-234")
    """

    def __init__(self, items: Dict[Type[_R], List[_R]]) -> None:
        self.entries = items

    def __iter__(self) -> Generator[Type[_R], None, None]:
        for x in self.entries:
            yield x

    def get(self, _type: Type[_R], idn: str) -> _R:
        """
        Get target entry in registry

        :param _type: type subset of entry
        :type entry: Type[_T]
        :raises ValueError: if subset or target is not found in registry
        :return: target entry in subset
        :rtype: _T
        """
        subset = self.entries.get(_type)
        if subset is None:
            raise ValueError(f"Entry of type {_type} is not found in registry")
        for target in subset:
            if target.idn == idn:
                return target
        raise ValueError(f"Entry with idn: {idn} not found in subset {_type}")
