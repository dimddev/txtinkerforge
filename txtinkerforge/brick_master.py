__author__ = 'dimd'

from txtinkerforge.txapi.txmapper import TxMapper
from tinkerforge.brick_master import BrickMaster


class TXMaster(TxMapper):

    device = BrickMaster

    def __init__(self, uid, ip_con):
        super(TXMaster, self).__init__(uid, ip_con)