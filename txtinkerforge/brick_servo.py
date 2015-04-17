__author__ = 'dimd'

from .txapi.txmapper import TxMapper
from tinkerforge.brick_master import BrickServo


class TXServo(TxMapper):

    device = BrickServo

    def __init__(self, uid, ip_con):
        super(TXServo, self).__init__(uid, ip_con)