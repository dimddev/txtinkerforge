from .txapi.txmapper import TxMapper

from tinkerforge.bricklet_temperature_ir import BrickletTemperatureIR


class TXTemperatureIR(TxMapper):

    device = BrickletTemperatureIR

    def __init__(self, uid, ip_con):
        super(TXTemperatureIR, self).__init__(uid, ip_con)