from .txapi.txmapper import TxMapper

from tinkerforge.brick_red import BrickRED


class TXRED(TxMapper):

    device = BrickRED

    def __init__(self, uid, ip_con):
        super(TXRED, self).__init__(uid, ip_con)