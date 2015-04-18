from .txapi.txmapper import TxMapper

from tinkerforge.bricklet_industrial_digital_out_4 import BrickletIndustrialDigitalOut4


class TXIndustrialDigitalOut4(TxMapper):

    device = BrickletIndustrialDigitalOut4

    def __init__(self, uid, ip_con):
        super(TXIndustrialDigitalOut4, self).__init__(uid, ip_con)