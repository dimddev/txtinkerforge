from .txapi.txmapper import TxMapper

from tinkerforge.bricklet_lcd_16x2 import BrickletLCD16x2


class TXLCD16x2(TxMapper):

    device = BrickletLCD16x2

    def __init__(self, uid, ip_con):
        super(TXLCD16x2, self).__init__(uid, ip_con)