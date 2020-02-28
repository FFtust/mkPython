import time 
import os

from link.find_device import get_port
from adapter.halo import adapter_halo

from device.api_halocode import *

def exit():
	adapter_default.link_obj.close()
# create default adapter, bind to default device
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
gamepad = gamepad_c(adapter_default)

class api_template():
    def __init__(self):
        pass

# mbuild use the same adapter with halo
import device.api_mbuild 
from adapter.halo_mbuild import bind_to_device

bind_to_device(adapter_default)
mbuild = api_template()

# rename api, compatiable with micropython API
mbuild.dual_rgb_sensor = device.api_mbuild.dual_rgb_sensor_c(adapter_default)

mbuild.servo_driver = device.api_mbuild.servo_driver_c(adapter_default)
mbuild.speaker = device.api_mbuild.speaker_c(adapter_default)
mbuild.dc_motor_driver = device.api_mbuild.dc_motor_driver_c(adapter_default)
mbuild.pir_sensor = device.api_mbuild.pir_sensor_c(adapter_default)
mbuild.ultrasonic_sensor = device.api_mbuild.ultrasonic_sensor_c(adapter_default)
mbuild.led_strip = device.api_mbuild.led_strip_c(adapter_default)
mbuild.ranging_sensor = device.api_mbuild.ranging_sensor_c(adapter_default)
mbuild.humiture_sensor = device.api_mbuild.humiture_sensor_c(adapter_default)
mbuild.slider = device.api_mbuild.slider_c(adapter_default)
mbuild.led_panel = device.api_mbuild.led_panel_c(adapter_default)
mbuild.button = device.api_mbuild.button_c(adapter_default)
mbuild.angle_sensor = device.api_mbuild.angle_sensor_c(adapter_default)
mbuild.flame_sensor = device.api_mbuild.flame_sensor_c(adapter_default)
mbuild.mq2_gas_sensor = device.api_mbuild.gas_sensor_c(adapter_default)
mbuild.ir_transceiver = device.api_mbuild.ir_sensor_c(adapter_default)
mbuild.joystick = device.api_mbuild.joystick_c(adapter_default)
mbuild.light_sensor = device.api_mbuild.light_sensor_c(adapter_default)
mbuild.motion_sensor = device.api_mbuild.motion_sensor_c(adapter_default)
mbuild.multi_touch = device.api_mbuild.mult_touch_c(adapter_default)
mbuild.soil_moisture = device.api_mbuild.soil_moisture_sensor_c(adapter_default)
mbuild.sound_sensor = device.api_mbuild.sound_sensor_c(adapter_default)
mbuild.temp_sensor = device.api_mbuild.temp_sensor_c(adapter_default)


mbuild.rgb_led = device.api_mbuild.rgb_led_c(adapter_default)
mbuild.magnetic_sensor = device.api_mbuild.magnetic_sensor_c(adapter_default)

mbuild.smartservo = device.api_mbuild.smartservo_c(adapter_default)
mbuild.smart_servo = mbuild.smartservo
mbuild.smart_camera = device.api_mbuild.smart_camera_c(adapter_default)

# compatible
mbuild.dual_rgb_color_sensor = mbuild.dual_rgb_sensor
mbuild.led_driver = mbuild.led_strip
mbuild.motor_driver = mbuild.dc_motor_driver
