from .txapi.txmapper import TxMapper

from tinkerforge.bricklet_solid_state_relay import BrickletSolidStateRelay


class TXSolidStateRelay(TxMapper):

    device = BrickletSolidStateRelay

    def __init__(self, uid, ip_con):
        super(TXSolidStateRelay, self).__init__(uid, ip_con)