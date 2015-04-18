from .txapi.txmapper import TxMapper

from tinkerforge.bricklet_multi_touch import BrickletMultiTouch


class TXMultiTouch(TxMapper):

    device = BrickletMultiTouch

    def __init__(self, uid, ip_con):
        super(TXMultiTouch, self).__init__(uid, ip_con)