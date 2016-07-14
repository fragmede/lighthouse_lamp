import time

import lighthouse

l = lighthouse.Lighthouse()
l.lamp(10)
time.sleep(5)
l.lamp(100)
time.sleep(3)
l.lamp(50)
l.set_pan_position(0)
l.dmx.disconnect()
