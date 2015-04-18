from .txapi.txmapper import TxMapper

from tinkerforge.bricklet_rotary_encoder import BrickletRotaryEncoder


class TXRotaryEncoder(TxMapper):

    device = BrickletRotaryEncoder

    def __init__(self, uid, ip_con):
        super(TXRotaryEncoder, self).__init__(uid, ip_con)