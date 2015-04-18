from .txapi.txmapper import TxMapper

from tinkerforge.bricklet_io4 import BrickletIO4


class TXIO4(TxMapper):

    device = BrickletIO4

    def __init__(self, uid, ip_con):
        super(TXIO4, self).__init__(uid, ip_con)