from .txapi.txmapper import TxMapper

from tinkerforge.brick_stepper import BrickStepper


class TXStepper(TxMapper):

    device = BrickStepper

    def __init__(self, uid, ip_con):
        super(TXStepper, self).__init__(uid, ip_con)