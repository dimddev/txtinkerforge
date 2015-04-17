HOST = "192.168.10.138"
PORT = 4223
UID = "6K9Li7" # Change to your UID

from tinkerforge.ip_connection import IPConnection

from txtinkerforge.brick_master import TXMaster as Master

from twisted.internet import reactor

if __name__ == "__main__":

    ipcon = IPConnection() # Create IP connection

    master = Master(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd

    def result(res):
       print 'RES IS: %s' % res

    voltage = master.get_stack_voltage()

    voltage.addCallback(result)

    reactor.run()
