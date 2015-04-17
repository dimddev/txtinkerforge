from .txapi.txmapper import TxMapper

from tinkerforge.brick_dc import BrickDC


class TXDC(TxMapper):

    device = BrickDC

    def __init__(self, uid, ip_con):
        super(TXDC, self).__init__(uid, ip_con)