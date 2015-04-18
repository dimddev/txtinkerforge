from .txapi.txmapper import TxMapper

from tinkerforge.bricklet_analog_in import BrickletAnalogIn


class TXAnalogIn(TxMapper):

    device = BrickletAnalogIn

    def __init__(self, uid, ip_con):
        super(TXAnalogIn, self).__init__(uid, ip_con)