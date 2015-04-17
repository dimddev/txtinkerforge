from .txapi.txmapper import TxMapper

from tinkerforge.brick_imu import BrickIMU


class TXIMU(TxMapper):

    device = BrickIMU

    def __init__(self, uid, ip_con):
        super(TXIMU, self).__init__(uid, ip_con)