from .txapi.txmapper import TxMapper

from tinkerforge.bricklet_piezo_speaker import BrickletPiezoSpeaker


class TXPiezoSpeaker(TxMapper):

    device = BrickletPiezoSpeaker

    def __init__(self, uid, ip_con):
        super(TXPiezoSpeaker, self).__init__(uid, ip_con)