from .txapi.txmapper import TxMapper

from tinkerforge.bricklet_moisture import BrickletMoisture


class TXMoisture(TxMapper):

    device = BrickletMoisture

    def __init__(self, uid, ip_con):
        super(TXMoisture, self).__init__(uid, ip_con)