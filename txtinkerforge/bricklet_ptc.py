from .txapi.txmapper import TxMapper

from tinkerforge.bricklet_ptc import BrickletPTC


class TXPTC(TxMapper):

    device = BrickletPTC

    def __init__(self, uid, ip_con):
        super(TXPTC, self).__init__(uid, ip_con)