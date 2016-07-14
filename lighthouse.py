
#import util
from util import (
    get_default_port,
    percent_to_dmx,
    degrees_to_dmx,
)
from enttec_usb_dmx_pro import EnttecUsbDmxPro

CHANNEL_MASTER_CONTROL = 4
MASTER_LAMP_OFF = 100
MASTER_LAMP_ON = 255

CHANNEL_BRIGHTNESS = 6
# simple 0-255 scale

CHANNEL_PAN_LOCATION = 8

CHANNEL_PAN_MOVMENT = 12
PAN_GOTO_POS = 0
PAN_CW = 128
PAN_CCW = 250

CHANNEL_SPEED = 15
# Speed must be < 50% to safely change direction

CHANNEL_TILT = 10
TILT_LOW = 0
TILT_VERTICAL = 128
TILT_LOW_CONTROLBOX_SIDE = 255
TILT_LOW_DEGREES = -120
TILT_VERTICAL_DEGREES = 0

CHANNEL_STROBE = 7
STROBE_MIN = 25


class Lighthouse(object):

    def __init__(self):
        self.brightness = 0

        self.dmx = EnttecUsbDmxPro.EnttecUsbDmxPro()
        self.port = get_default_port()
        self.dmx.setPort(self.port)
        self.dmx.connect()
        #self.dmx.setChannel(CHANNEL_MASTER_CONTROL, MASTER_LAMP_OFF)

    def lamp(self, int_brightness):
        """
        Brightness is a percentage, 0-100%

        """
        self.brightness = int_brightness
        if self.brightness == 0:
            self.dmx.setChannel(CHANNEL_MASTER_CONTROL, MASTER_LAMP_OFF)
            return
        self.dmx.setChannel(CHANNEL_MASTER_CONTROL, MASTER_LAMP_ON)
        self.dmx.setChannel(CHANNEL_BRIGHTNESS, percent_to_dmx(self.brightness))

    def set_pan_position(self, position_degrees):
        """
            Moves lamp to a specific rotation
            TODO - Add in don't-burn-down-lighthouse safeguard
        """
        self.dmx.setChannel(CHANNEL_PAN_LOCATION, degrees_to_dmx(position_degrees))
        #self.dmx.setChannel(1, 255)

    def set_rotation(self, clockwise, speed=100):
        """
            Set rotation and speed
            TODO - assert speed < 50% if already moving
        """
        self.dmx.setChannel(CHANNEL_SPEED, percent_to_dmx(0))
        if clockwise:
            self.dmx.setChannel(CHANNEL_PAN_MOVMENT, PAN_CW)
        else:
            self.dmx.setChannel(CHANNEL_PAN_MOVMENT, PAN_CCW)
        self.dmx.setChannel(CHANNEL_SPEED, percent_to_dmx(speed))

    def set_tilt(self, tilt_degrees_from_vertical):
        raise NotImplemented('set_tilt')
        #value = degrees_to_dmx(tilt_degrees_from_vertical, min_range=)
        #self.dmx.setChannel(CHANNEL_TILT, value)

    def foo(self):
        self.dmx.setChannel(1, 255)
        self.dmx.setChannel(3, 255)
        self.dmx.setChannel(4, 255)
        self.dmx.setChannel(5, 255)
        self.dmx.render()

    def bar(self):
        self.dmx.setChannel(1, 0)
        self.dmx.setChannel(3, 0)
        self.dmx.setChannel(4, 0)
        self.dmx.setChannel(5, 0)
        self.dmx.render()

        
class Lumin_Slick_Par(object):
    def foo(self):
        self.dmx.setChannel(1, 255)
        self.dmx.setChannel(3, 255)
        self.dmx.setChannel(4, 255)
        self.dmx.setChannel(5, 255)
        self.dmx.render()

    def bar(self):
        self.dmx.setChannel(1, 0)
        self.dmx.setChannel(3, 0)
        self.dmx.setChannel(4, 0)
        self.dmx.setChannel(5, 0)
        self.dmx.render()

