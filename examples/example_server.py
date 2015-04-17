from twisted.internet.protocol import Protocol
from twisted.internet.protocol import Factory
from twisted.internet import reactor, defer
from twisted.internet.endpoints import TCP4ServerEndpoint

from tinkerforge.ip_connection import IPConnection
from txtinkerforge.brick_master import TXMaster as Master

# thinker settings
HOST = "localhost"
PORT = 4223
UID = '6K9d341Li7'

# this connections is blocking
ipcon = IPConnection()
ipcon.connect(HOST, PORT)


class TinkerCommands(Protocol):

    def __init__(self):

        self.master = Master(UID, ipcon)

    def dataReceived(self, data):

        data = data.strip('\r\n')

        if data == 'reset':
            self.get_voltage()

    def connectionMade(self):
        print 'Client comes in to Tinker Server\r\n'

    @defer.inlineCallbacks
    def get_voltage(self):

        # self.master.get_stack_voltage() will return defer
        voltage = yield self.master.get_stack_voltage()

        if voltage == 0:

            self.master.reset()
            print '+++ RESET MASTER BRICK, VOTLAGE IS {}'.format(voltage)
            self.transport.write('+++ RESET BRICK MASTER DEVICE, VOTLAGE IS {}'.format(voltage) + '\r\n')
            self.transport.loseConnection()


class TinkerFactory(Factory):

    def buildProtocol(self, addr):
        return TinkerCommands()

endpoint = TCP4ServerEndpoint(reactor, 8007)
endpoint.listen(TinkerFactory())
reactor.run()