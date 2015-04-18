from .txapi.txmapper import TxMapper

from tinkerforge.bricklet_io16 import BrickletIO16


class TXIO16(TxMapper):

    device = BrickletIO16

    def __init__(self, uid, ip_con):
        super(TXIO16, self).__init__(uid, ip_con)