from .txapi.txmapper import TxMapper

from tinkerforge.bricklet_rotary_poti import BrickletRotaryPoti


class TXRotaryPoti(TxMapper):

    device = BrickletRotaryPoti

    def __init__(self, uid, ip_con):
        super(TXRotaryPoti, self).__init__(uid, ip_con)