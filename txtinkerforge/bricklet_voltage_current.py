from .txapi.txmapper import TxMapper

from tinkerforge.bricklet_voltage_current import BrickletVoltageCurrent


class TXVoltageCurrent(TxMapper):

    device = BrickletVoltageCurrent

    def __init__(self, uid, ip_con):
        super(TXVoltageCurrent, self).__init__(uid, ip_con)