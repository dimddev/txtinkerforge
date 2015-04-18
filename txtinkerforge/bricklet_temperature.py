from .txapi.txmapper import TxMapper

from tinkerforge.bricklet_temperature import BrickletTemperature


class TXTemperature(TxMapper):

    device = BrickletTemperature

    def __init__(self, uid, ip_con):
        super(TXTemperature, self).__init__(uid, ip_con)