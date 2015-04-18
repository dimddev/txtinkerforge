from .txapi.txmapper import TxMapper

from tinkerforge.bricklet_analog_out import BrickletAnalogOut


class TXAnalogOut(TxMapper):

    device = BrickletAnalogOut

    def __init__(self, uid, ip_con):
        super(TXAnalogOut, self).__init__(uid, ip_con)