from link.find_device import get_port

import adapter.halo
adapter.halo.set_channel(get_port())

from device.api_halocode import *

led = led_c()
button = button_c() 
touchpad0 = touchpad0_c() 
touchpad1 = touchpad1_c() 
touchpad2 = touchpad2_c() 
touchpad3 = touchpad3_c() 
microphone = microphone_c()
motion_sensor = motion_sensor_c()
