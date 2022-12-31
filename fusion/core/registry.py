# -*- coding: utf-8 -*-
"""
Fusion Core - Registry
======================

Registries are custom object containers

Copyright © 2022 dronectl. All rights reserved.
"""

from typing import List, Dict, Generator, Generic, Type, TypeVar, Union

class RegistryElemMixin:

    @property
    def idn(self) -> str:
        """
        Registry element identification string

        :return: registry identification string
        :rtype: str
        """
        return self.__idn

    @idn.setter
    def idn(self, idn: str) -> None:
        """
        Registry element identification string

        :param idn: registry identification string
        :type idn: str
        """
        self.__idn = idn

_R = TypeVar('_R', bound=RegistryElemMixin)
_T = TypeVar('_T', bound=_R) # type: ignore

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

    @property
    def size(self) -> int:
        return len(self.entries)

    def get(self, _type: Type[_T], idn: str) -> _T:
        """
        Get target entry in registry

        :param _type: type subset of entry
        :type entry: Type[_T]
        :raises ValueError: if subset or target is not found
        :return: target entry in subset
        :rtype: _T
        """
        subset = self.entries.get(_type) # type: ignore
        if subset is None:
            raise ValueError(f"Entry of type {_type} is not found in registry")
        for target in subset:
            if target.idn == idn:
                return target # type: ignore
        raise ValueError(f"Entry with idn: {idn} not found in subset {_type}")
