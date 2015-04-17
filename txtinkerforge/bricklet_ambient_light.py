from .txapi.txmapper import TxMapper

from tinkerforge.bricklet_ambient_light import BrickletAmbientLight


class TXAmbientLight(TxMapper):

    device = BrickletAmbientLight

    def __init__(self, uid, ip_con):
        super(TXAmbientLight, self).__init__(uid, ip_con)