from .txapi.txmapper import TxMapper

from tinkerforge.bricklet_industrial_digital_in_4 import BrickletIndustrialDigitalIn4


class TXIndustrialDigitalIn4(TxMapper):

    device = BrickletIndustrialDigitalIn4

    def __init__(self, uid, ip_con):
        super(TXIndustrialDigitalIn4, self).__init__(uid, ip_con)