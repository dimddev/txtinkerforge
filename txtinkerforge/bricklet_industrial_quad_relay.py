from .txapi.txmapper import TxMapper

from tinkerforge.bricklet_industrial_quad_relay import BrickletIndustrialQuadRelay


class TXIndustrialQuadRelay(TxMapper):

    device = BrickletIndustrialQuadRelay

    def __init__(self, uid, ip_con):
        super(TXIndustrialQuadRelay, self).__init__(uid, ip_con)