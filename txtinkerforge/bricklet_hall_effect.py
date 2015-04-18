from .txapi.txmapper import TxMapper

from tinkerforge.bricklet_hall_effect import BrickletHallEffect


class TXHallEffect(TxMapper):

    device = BrickletHallEffect

    def __init__(self, uid, ip_con):
        super(TXHallEffect, self).__init__(uid, ip_con)