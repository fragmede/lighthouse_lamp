import time
import sys

import lighthouse

l = lighthouse.Lighthouse()
#l.foo()
#time.sleep(5)
#l.bar()
#l.dmx.disconnect()
#sys.exit(0)

print 'hi gerald'
l.dmx.setChannel(5, 255)
l.dmx.render()
time.sleep(10)
l.dmx.setChannel(5, 0)
l.dmx.render()
l.dmx.disconnect()
sys.exit(0)



l.lamp(100)
print 'lamp on'
#l.foo()
time.sleep(5)
l.set_pan_position(0)
time.sleep(5)
l.set_pan_position(90)
#time.sleep(15)
time.sleep(5)
l.lamp(0)
print 'lamp off'
l.dmx.disconnect()
#l.bar()
