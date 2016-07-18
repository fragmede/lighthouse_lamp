import lighthouse
import types
from OSC import OSCServer


recvPort = 7000


class ServerLighthouse(object):

    def __init__(self, address='192.168.1.145', recvPort=recvPort):

        self.address = address
        self.recvPort = recvPort

        # Setup a reciever for OSC.
        self.server = OSCServer((self.address, self.recvPort))
        self.server.timeout = 0
        self.server.handleTimeout = types.MethodType(self.handleTimeout, self.server)

        # Startup light
        self.intitializeLight()

    def handleTimeout(self):
        self.timedOut = True

    def eachFrame(self):
        # clear timed_out flag
        self.server.timed_out = False

        # handle all pending requests then return
        while not self.server.timed_out:
            self.server.handle_request()

    def handleEvent(self, address, functionToCall):
        def internalFunction(path, tags, args, source):
            arg = int(args[0])
            functionToCall(arg)

        def internalFunctionZ(path, tags, args, source):
            pass

        self.server.addMsgHandler(address, internalFunction)
        self.server.addMsgHandler('%s/z' % address, internalFunctionZ)


class LighthouseMotion(ServerLighthouse):

    def __init__(self):
        super(LighthouseMotion, self).__init__()

    def intitializeLight(self):
        # Allow lamp to move at 25% speed.

        self.light = lighthouse.Lighthouse()
        self.light.set_speed(25)  # set speed to quarter AKA Rabtule (rabbit turtle)

    def panLight(self, address):
        self.handleEvent(address, self.light.set_pan_position)
        return 'pan'

    def tiltLight(self, address):
        self.handleEvent(address, self.light.set_tilt)
        return 'tilt'

    def setSpeed(self, address):
        self.handleEvent(address, self.light.set_speed)
        return 'speed'

    def lightOnOff(self, address):
        self.handleEvent(address, self.light.set_lamp)

    def setBrightness(self, address):
        self.handleEvent(address, self.light.set_lamp)

    def setStrobe(self, address):
        self.handleEvent(address, self.light.set_strobe)

if __name__ == "__main__":
    light = LighthouseMotion()
    light.panLight('/1/pan')
    light.tiltLight('/1/tilt')
    light.setSpeed('/1/speed')
    light.lightOnOff('/1/lightControl')
    light.setBrightness('/1/brightness')
    light.setStrobe('/1/strobe')
    while True:
        light.eachFrame()
