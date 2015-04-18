from .txapi.txmapper import TxMapper

from tinkerforge.bricklet_sound_intensity import BrickletSoundIntensity


class TXSoundIntensity(TxMapper):

    device = BrickletSoundIntensity

    def __init__(self, uid, ip_con):
        super(TXSoundIntensity, self).__init__(uid, ip_con)