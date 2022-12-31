# -*- coding: utf-8 -*-
"""
System Tests
============

Copyright © 2022 dronectl. All rights reserved.
"""

import unittest
from pathlib import Path
from fusion.core.topology import Topology
from fusion.core.utils import parse_yaml
from fusion.devices.raptor import Raptor
from fusion.interfaces.socket import TCPSocket


class TestSystem(unittest.TestCase):

    def setUp(self):
        # build topology required for test setup
        self.topology = Topology()
        topology_path = str(Path(__file__).parent.parent.joinpath('topology.yaml').resolve())
        topology_document = parse_yaml(topology_path)
        self.topology.load(topology_document)

    def test_invalid_device(self):
        with self.assertRaises(ValueError):
            _ = self.topology.devices.get(Raptor, 'rpt-10')

    def test_valid_device(self):
        self.assertTrue(isinstance(self.topology.devices.get(Raptor, 'rpt-102'), Raptor))

    def test_local_connection(self):
        raptor = self.topology.devices.get(Raptor, 'rpt-102')
        with self.assertRaises(ConnectionRefusedError):
            with raptor.interfaces.get(TCPSocket, 'scpi') as socket:
                socket.write("test:scpi:command")
        
