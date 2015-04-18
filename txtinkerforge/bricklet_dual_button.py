from .txapi.txmapper import TxMapper

from tinkerforge.bricklet_dual_button import BrickletDualButton


class TXDualButton(TxMapper):

    device = BrickletDualButton

    def __init__(self, uid, ip_con):
        super(TXDualButton, self).__init__(uid, ip_con)