import adapter.halo
adapter.halo.set_channel("COM3")
from device.halocode import halo 

halo = halo()

import time,math
a = 0
while True:
    a += 1 
    # halo.led_show_all(0,math.fabs(math.sin(a/200)) *255 + 3,0)
    print(halo.button_is_pressed())
    time.sleep(5)