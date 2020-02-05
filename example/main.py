import adapter.halo
adapter.halo.set_channel("COM3")

from device.halocode import halo 

# halo = halo()

# import time,math
# a = 0
# while True:
#     a += 1 
#     # halo.led_show_all(0,math.fabs(math.sin(a/200)) *255 + 3,0)
#     if halo.button_is_pressed():
#         halo.led_show_all(100, 0, 0)
#     else:
#         halo.led_show_all(0, 0, 0)

from device.api_halocode_api import led, button 

import time,math
a = 0
# while True:
    # a += 1 
    # halo.led_show_all(0,math.fabs(math.sin(a/200)) *255 + 3,0)
    # if button.is_pressed():
led.show_all(100, 1000, 0, 100)
    # else:
        # led.ring_graph(0)