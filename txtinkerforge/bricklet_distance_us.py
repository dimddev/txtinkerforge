from .txapi.txmapper import TxMapper

from tinkerforge.bricklet_distance_us import BrickletDistanceUS


class TXDistanceUS(TxMapper):

    device = BrickletDistanceUS

    def __init__(self, uid, ip_con):
        super(TXDistanceUS, self).__init__(uid, ip_con)