import time 
import os

from link.find_device import get_port
from adapter.mbuild import adapter_mbuild


adapter_default = adapter_mbuild(get_port())
adapter_default.start()



import device.mbuild_modules.servo_driver as servo_driver
import device.mbuild_modules.speaker as speaker
import device.mbuild_modules.dc_motor_driver as dc_motor_driver
import device.mbuild_modules.pir_sensor as pir_sensor
import device.mbuild_modules.ultrasonic_sensor as ultrasonic_sensor
import device.mbuild_modules.led_strip as led_strip
import device.mbuild_modules.ranging_sensor as ranging_sensor
import device.mbuild_modules.humiture_sensor as humiture_sensor
import device.mbuild_modules.slider as slider
import device.mbuild_modules.dual_rgb_sensor as dual_rgb_sensor
import device.mbuild_modules.led_panel as led_panel


import device.mbuild_modules.button as button
import device.mbuild_modules.angle_sensor as angle_sensor
import device.mbuild_modules.flame_sensor as flame_sensor

import device.mbuild_modules.gas_sensor as mq2_gas_sensor
import device.mbuild_modules.ir_sensor as ir_transceiver
import device.mbuild_modules.joystick as joystick
import device.mbuild_modules.light_sensor as light_sensor
import device.mbuild_modules.motion_sensor as motion_sensor

import device.mbuild_modules.mult_touch as multi_touch
import device.mbuild_modules.soil_moisture_sensor as soil_moisture
import device.mbuild_modules.sound_sensor as sound_sensor
import device.mbuild_modules.temp_sensor as temp_sensor

# add for 006
import device.mbuild_modules.rgb_led as rgb_led
import device.mbuild_modules.magnetic_sensor as magnetic_sensor
# two names about samrt servo
import device.mbuild_modules.smartservo as smartservo
smart_servo = smartservo

import device.mbuild_modules.smart_camera as smart_camera
import device.mbuild_modules.mbot as mbot
# compatible
dual_rgb_color_sensor = dual_rgb_sensor
led_driver = led_strip
motor_driver = dc_motor_driver


# colorful_handle
import device.mbuild_modules.colorful_handle as colorful_handle