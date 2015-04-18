from .txapi.txmapper import TxMapper

from tinkerforge.bricklet_barometer import BrickletBarometer


class TXBarometer(TxMapper):

    device = BrickletBarometer

    def __init__(self, uid, ip_con):
        super(TXBarometer, self).__init__(uid, ip_con)