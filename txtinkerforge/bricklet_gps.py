from .txapi.txmapper import TxMapper

from tinkerforge.bricklet_gps import BrickletGPS


class TXGPS(TxMapper):

    device = BrickletGPS

    def __init__(self, uid, ip_con):
        super(TXGPS, self).__init__(uid, ip_con)