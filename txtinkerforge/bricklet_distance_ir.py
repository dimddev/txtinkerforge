from .txapi.txmapper import TxMapper

from tinkerforge.bricklet_distance_ir import BrickletDistanceIR


class TXDistanceIR(TxMapper):

    device = BrickletDistanceIR

    def __init__(self, uid, ip_con):
        super(TXDistanceIR, self).__init__(uid, ip_con)