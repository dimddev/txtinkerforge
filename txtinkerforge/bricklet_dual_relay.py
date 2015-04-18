from .txapi.txmapper import TxMapper

from tinkerforge.bricklet_dual_relay import BrickletDualRelay


class TXDualRelay(TxMapper):

    device = BrickletDualRelay

    def __init__(self, uid, ip_con):
        super(TXDualRelay, self).__init__(uid, ip_con)