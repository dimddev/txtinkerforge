from .txapi.txmapper import TxMapper

from tinkerforge.bricklet_voltage import BrickletVoltage


class TXVoltage(TxMapper):

    device = BrickletVoltage

    def __init__(self, uid, ip_con):
        super(TXVoltage, self).__init__(uid, ip_con)