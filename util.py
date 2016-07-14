from __future__ import division
import platform

def get_default_port():
    if platform.system() == 'Linux':
        return '/dev/ttyUSB0'
    elif platform.system() == 'Mac':
        return '/dev/tty.usbserial-ENT095626'

def percent_to_dmx(int_percent):
    return int(int_percent/100 * 255)

def degrees_to_dmx(degrees, min_range=0, max_range=360):
    return int(degrees/(max_range-min_range) * 255)

def brightness_percent_to_dmx(int_percent):
    return 255 - percent_to_dmx(int_percent)
