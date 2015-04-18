from .txapi.txmapper import TxMapper

from tinkerforge.bricklet_color import BrickletColor


class TXColor(TxMapper):

    device = BrickletColor

    def __init__(self, uid, ip_con):
        super(TXColor, self).__init__(uid, ip_con)