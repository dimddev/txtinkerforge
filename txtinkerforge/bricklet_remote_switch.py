__author__ = 'dimd'

from .txapi.txmapper import TxMapper
from tinkerforge.bricklet_remote_switch import BrickletRemoteSwitch


class TXRemoteSwitch(TxMapper):

    device = BrickletRemoteSwitch

    def __init__(self, uid, ip_con):
        super(TXRemoteSwitch, self).__init__(uid, ip_con)