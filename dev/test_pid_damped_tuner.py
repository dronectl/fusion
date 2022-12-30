
from fusion.core.topology import Topology
from fusion.devices.raptor import Raptor
from fusion.interfaces.socket import TCPSocket


class PIDDampedTuner:

    def __init__(self) -> None:
        # build topology required for test setup
        self.topology = Topology(**{})

    def test_cmd(self) -> None:
        """
        """
        raptor = self.topology.devices.get(Raptor, 'rpt-102')
        with raptor.interfaces.get(TCPSocket, 'scpi') as socket:
            socket.write(b"test:scpi:command")
