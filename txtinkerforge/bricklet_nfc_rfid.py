from .txapi.txmapper import TxMapper

from tinkerforge.bricklet_nfc_rfid import BrickletNFCRFID


class TXNFCRFID(TxMapper):

    device = BrickletNFCRFID

    def __init__(self, uid, ip_con):
        super(TXNFCRFID, self).__init__(uid, ip_con)