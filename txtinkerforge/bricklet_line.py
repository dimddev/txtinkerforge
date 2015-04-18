from .txapi.txmapper import TxMapper

from tinkerforge.bricklet_line import BrickletLine


class TXLine(TxMapper):

    device = BrickletLine

    def __init__(self, uid, ip_con):
        super(TXLine, self).__init__(uid, ip_con)