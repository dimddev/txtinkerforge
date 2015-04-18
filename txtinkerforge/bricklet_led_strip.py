from .txapi.txmapper import TxMapper

from tinkerforge.bricklet_led_strip import BrickletLEDStrip


class TXLEDStrip(TxMapper):

    device = BrickletLEDStrip

    def __init__(self, uid, ip_con):
        super(TXLEDStrip, self).__init__(uid, ip_con)