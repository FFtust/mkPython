import time 
import os

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
pin0 = pin0_c() 
pin1 = pin1_c() 
pin2 = pin2_c() 
pin3 = pin3_c() 
speaker = speaker_c()
mesh = mesh_c()
wifi = wifi_c()