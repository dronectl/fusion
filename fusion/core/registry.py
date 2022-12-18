# -*- coding: utf-8 -*-
"""
Fusion Core - Registry
======================

Registries are custom object containers

Copyright © 2022 dronectl. All rights reserved.
"""

from typing import Generator, Generic, Type, TypeVar

_R = TypeVar('_R')
_T = TypeVar('_T')

class Registry(Generic[_R]):

    def __init__(self, *args) -> None:
        self.entries = set(args)

    def __iter__(self) -> Generator[_R, None, None]:
        for x in self.entries:
            yield x

    def get(self, entry: Type[_T]) -> _T:
        """
        Get entry in registry of type

        :param entry: type of entry
        :type entry: Type[_T]
        :raises ValueError: _description_
        :return: _description_
        :rtype: _T
        """
        for e in self.entries:
            if type(e) == entry:
                return e
        raise ValueError(f"Entry of type {entry} is not found in registry")
