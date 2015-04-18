from .txapi.txmapper import TxMapper

from tinkerforge.bricklet_motion_detector import BrickletMotionDetector


class TXMotionDetector(TxMapper):

    device = BrickletMotionDetector

    def __init__(self, uid, ip_con):
        super(TXMotionDetector, self).__init__(uid, ip_con)