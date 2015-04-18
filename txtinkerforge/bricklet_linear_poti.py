from .txapi.txmapper import TxMapper

from tinkerforge.bricklet_linear_poti import BrickletLinearPoti


class TXLinearPoti(TxMapper):

    device = BrickletLinearPoti

    def __init__(self, uid, ip_con):
        super(TXLinearPoti, self).__init__(uid, ip_con)