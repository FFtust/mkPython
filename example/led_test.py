import adapter.halo
adapter.halo.set_channel("COM3")

from device.api_halocode_api import led, button 

import time,math
a = 0
while True:
    a += 1 
    # led.show_all(0,math.fabs(math.sin(a/100)) *100 + 3,0, 100)
    if button.is_pressed():
        led.show_all(100, 100, 0, 100)
    else:
        led.show_all(0, 0, 0, 100)
