from .txapi.txmapper import TxMapper

from tinkerforge.bricklet_humidity import BrickletHumidity


class TXHumidity(TxMapper):

    device = BrickletHumidity

    def __init__(self, uid, ip_con):
        super(TXHumidity, self).__init__(uid, ip_con)