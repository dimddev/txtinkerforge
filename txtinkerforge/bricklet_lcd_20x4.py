from .txapi.txmapper import TxMapper

from tinkerforge.bricklet_lcd_20x4 import BrickletLCD20x4


class TXLCD20x4(TxMapper):

    device = BrickletLCD20x4

    def __init__(self, uid, ip_con):
        super(TXLCD20x4, self).__init__(uid, ip_con)