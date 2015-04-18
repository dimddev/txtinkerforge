from .txapi.txmapper import TxMapper

from tinkerforge.bricklet_segment_display_4x7 import BrickletSegmentDisplay4x7


class TXSegmentDisplay4x7(TxMapper):

    device = BrickletSegmentDisplay4x7

    def __init__(self, uid, ip_con):
        super(TXSegmentDisplay4x7, self).__init__(uid, ip_con)