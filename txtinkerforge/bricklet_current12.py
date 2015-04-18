from .txapi.txmapper import TxMapper

from tinkerforge.bricklet_current12 import BrickletCurrent12


class TXCurrent12(TxMapper):

    device = BrickletCurrent12

    def __init__(self, uid, ip_con):
        super(TXCurrent12, self).__init__(uid, ip_con)