from .txapi.txmapper import TxMapper

from tinkerforge.bricklet_joystick import BrickletJoystick


class TXJoystick(TxMapper):

    device = BrickletJoystick

    def __init__(self, uid, ip_con):
        super(TXJoystick, self).__init__(uid, ip_con)