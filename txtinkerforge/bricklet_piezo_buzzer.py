from .txapi.txmapper import TxMapper

from tinkerforge.bricklet_piezo_buzzer import BrickletPiezoBuzzer


class TXPiezoBuzzer(TxMapper):

    device = BrickletPiezoBuzzer

    def __init__(self, uid, ip_con):
        super(TXPiezoBuzzer, self).__init__(uid, ip_con)