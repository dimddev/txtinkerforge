from .txapi.txmapper import TxMapper

from tinkerforge.bricklet_tilt import BrickletTilt


class TXTilt(TxMapper):

    device = BrickletTilt

    def __init__(self, uid, ip_con):
        super(TXTilt, self).__init__(uid, ip_con)