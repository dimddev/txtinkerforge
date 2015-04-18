from .txapi.txmapper import TxMapper

from tinkerforge.bricklet_industrial_dual_0_20ma import BrickletIndustrialDual020mA


class TXIndustrialDual020mA(TxMapper):

    device = BrickletIndustrialDual020mA

    def __init__(self, uid, ip_con):
        super(TXIndustrialDual020mA, self).__init__(uid, ip_con)