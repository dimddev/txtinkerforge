from .txapi.txmapper import TxMapper

from tinkerforge.bricklet_current25 import BrickletCurrent25


class TXCurrent25(TxMapper):

    device = BrickletCurrent25

    def __init__(self, uid, ip_con):
        super(TXCurrent25, self).__init__(uid, ip_con)