import time 
import os

from link.find_device import get_port
from adapter.halo import adapter_halo

from device.api_halocode import *


# class halo_c():
#     def __init__(slef, port, bauadrate = 115200):
#         self.adapter = adapter_halo(port, bauadrate)
#         self.adapter.start()

#         self.led = led_c(self.adapter)
#         self.button = button_c(self.adapter) 
#         self.touchpad0 = touchpad0_c(self.adapter) 
#         self.touchpad1 = touchpad1_c(self.adapter) 
#         self.touchpad2 = touchpad2_c(self.adapter) 
#         self.touchpad3 = touchpad3_c(self.adapter) 
#         self.microphone = microphone_c(self.adapter)
#         self.motion_sensor = motion_sensor_c(self.adapter)
#         self.pin0 = pin0_c(self.adapter) 
#         self.pin1 = pin1_c(self.adapter) 
#         self.pin2 = pin2_c(self.adapter) 
#         self.pin3 = pin3_c(self.adapter) 
#         self.speaker = speaker_c(self.adapter)
#         self.mesh = mesh_c(self.adapter)
#         self.wifi = wifi_c(self.adapter)

adapter_default = adapter_halo(get_port())
adapter_default.start()

led = led_c(adapter_default)
button = button_c(adapter_default) 
touchpad0 = touchpad0_c(adapter_default) 
touchpad1 = touchpad1_c(adapter_default) 
touchpad2 = touchpad2_c(adapter_default) 
touchpad3 = touchpad3_c(adapter_default) 
microphone = microphone_c(adapter_default)
motion_sensor = motion_sensor_c(adapter_default)
pin0 = pin0_c(adapter_default) 
pin1 = pin1_c(adapter_default) 
pin2 = pin2_c(adapter_default) 
pin3 = pin3_c(adapter_default) 
speaker = speaker_c(adapter_default)
mesh = mesh_c(adapter_default)
wifi = wifi_c(adapter_default)

class api_template():
    def __init__(self):
        pass

import device.api_mbuild 
from adapter.halo_mbuild import bind_to_device

bind_to_device(adapter_default)

mbuild = api_template()

mbuild.dual_rgb_sensor = device.api_mbuild.dual_rgb_sensor_c(adapter_default)